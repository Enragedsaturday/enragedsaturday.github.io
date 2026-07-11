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

## GROUP: _overhaul2/lake/cases/Connick v. Thompson.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Connick v. Thompson"
type: case
citation: ""
parallel_cite: "179 L. Ed. 2d 417; 131 S. Ct. 1350; 563 U.S. 51; 22 Fla. L. Weekly Fed. S 887; 79 U.S.L.W. 4195"
neutral_cite: 2011 U.S. LEXIS 2594
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-03-29
docket: 09-571
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-03-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Connick v. Thompson
  varies_by_point: false
  scope_note: "Good law: a single Brady violation, without a pattern, does not establish municipal failure-to-train liability."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7343085/connick-v-thompson/"
  cluster_id: 7343085
  opinion_id: 7261027
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Brady and Giglio]]"
    role: "Related (cross-doctrine)"
related: ["[[City of Canton v. Harris]]", "[[Monell v. Department of Social Services]]", "[[Brady v. Maryland]]"]
aliases: []
tags: ["case", "section-1983", "municipal-liability", "failure-to-train", "deliberate-indifference", "brady"]
holding: "A single Brady violation, without a pattern of similar violations, generally cannot establish the deliberate indifference required for municipal failure-to-train liability; prosecutorial Brady training is not within Canton's narrow single-incident exception."
lake:
  record_id: Connick v. Thompson
  status: verified
  projected_at: 2026-07-09
---

# Connick v. Thompson

*563 U.S. 51 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
John Thompson was convicted of armed robbery and murder in New Orleans and spent years on death row before it emerged that prosecutors in District Attorney Harry Connick's office had suppressed a crime-lab report (blood-type evidence) favorable to him, in violation of [[Brady v. Maryland]]. His convictions were [[Reading and Citing Cases#vacated|vacated]] and he was acquitted on retrial. He sued the District Attorney's Office under § 1983, claiming Connick had been deliberately indifferent in failing to train prosecutors on their *[[Brady v. Maryland|Brady]]* obligations. A jury awarded him $14 million.

## Issue
Whether a district attorney's office may be held liable under § 1983 for failure to train its prosecutors on *[[Brady v. Maryland|Brady]]* based on a single violation, absent a pattern of similar violations.

## Rule
A pattern of violations is ordinarily required. "A pattern of similar constitutional violations by untrained employees is 'ordinarily necessary' to demonstrate deliberate indifference for purposes of failure to train." — 563 U.S. at 62. ^pin-62

*[[City of Canton v. Harris|Canton]]* recognized a "narrow range" of single-incident liability where the need for training is so obvious and the violation so predictable that a pattern is unnecessary — but that exception is confined. "Failure to train prosecutors in their *Brady* obligations does not fall within the narrow range of *Canton's* hypothesized single-incident liability." — [*Id.* at 64](https://www.courtlistener.com/opinion/7343085/connick-v-thompson/#:~:text=a-,narrow%20range). ^pin-64

## Application
Thompson did not prove a pattern of similar *[[Brady v. Maryland|Brady]]* violations: the four earlier reversals in Connick's office involved different kinds of suppressed evidence and could not have put the office on notice that training on this type of *[[Brady v. Maryland|Brady]]* violation was deficient. Nor did the single-incident theory apply: unlike the untrained-officer-with-a-gun hypothetical in *[[City of Canton v. Harris|Canton]]*, prosecutors are trained lawyers who are expected to know and apply *[[Brady v. Maryland|Brady]]*, so the need to train them on it is not the kind of "patently obvious" need that supports liability without a pattern.

## Conclusion
Reversed. A single *[[Brady v. Maryland|Brady]]* violation, without a pattern of similar violations, is insufficient to establish the [[Section 1983 Liability and Qualified Immunity|deliberate indifference]] required for municipal failure-to-train liability; the $14 million judgment could not stand.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Connick* applies and tightens the deliberate-indifference / single-incident framework of [[City of Canton v. Harris]] within the [[Monell v. Department of Social Services]] municipal-liability line, at the intersection with the prosecutor's duty under [[Brady v. Maryland]]. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Brady and Giglio]] — *Related (cross-doctrine)*

## Sources
- *Connick v. Thompson*, 563 U.S. 51 (2011) — https://www.courtlistener.com/opinion/213505/connick-v-thompson/ — pinpoints: 62, 64 (lead opinion id 9441299).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bb786bc4e1f01dfb", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Connick v. Thompson"}, "payload": {"all": [{"cite": "179 L. Ed. 2d 417", "page": "417", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "179"}, {"cite": "2011 U.S. LEXIS 2594", "page": "2594", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2011"}, {"cite": "131 S. Ct. 1350", "page": "1350", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "131"}, {"cite": "563 U.S. 51", "page": "51", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "563"}, {"cite": "22 Fla. L. Weekly Fed. S 887", "page": "887", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "22"}, {"cite": "79 U.S.L.W. 4195", "page": "4195", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "79"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Connick v. Thompson"}}
{"assertion_id": "4aec096475b165af", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-62", "record_id": "Connick v. Thompson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-62", "pinpoint_status": "slip-only", "quote": "--- # Connick v. Thompson *563 U.S. 51 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background John Thompson was convicted of armed robbery and murder in New Orleans and spent years on death row before it emerged that prosecutors in District Attorney Harry Connick's office had suppressed a crime-lab report (blood-type evidence) favorable to him, in violation of [[Brady v. Maryland]]. His convictions were vacated and he was acquitted on retrial. He sued the District Attorney's Office under § 1983, claiming Connick had been deliberately indifferent in failing to train prosecutors on their *Brady* obligations. A jury awarded him $14 million. ## Issue Whether a district attorney's office may be held liable under § 1983 for failure to train its prosecutors on *Brady* based on a single violation, absent a pattern of similar violations. ## Rule A pattern of violations is ordinarily required.", "quote_fidelity": "mismatch", "record_id": "Connick v. Thompson", "star_marker": null}}
{"assertion_id": "5b1d880806251911", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-64", "record_id": "Connick v. Thompson"}, "payload": {"fragment": "#:~:text=a-,narrow%20range", "page": null, "pin_id": "pin-64", "pinpoint_status": "star-verified", "quote": "narrow range", "quote_fidelity": "matched", "record_id": "Connick v. Thompson", "star_marker": "428"}}
{"assertion_id": "10614f3c04f1ff5f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Connick v. Thompson"}, "payload": {"as_of_content": "2011-03-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Connick v. Thompson", "scope_note": "Good law: a single Brady violation, without a pattern, does not establish municipal failure-to-train liability.", "varies_by_point": false}}
```

### lake record — Connick v. Thompson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Connick v. Thompson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Connick v. Thompson",
    "case_name_short": "Connick",
    "case_name_full": "HARRY F. CONNICK, DISTRICT ATTORNEY v. JOHN THOMPSON",
    "input_case_name": "Connick v. Thompson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-03-29",
    "year": 2011,
    "docket": "09-571",
    "cluster_id": 7343085,
    "lead_opinion_id": 7261027,
    "sibling_ids": [
      7261027,
      7261028,
      7261029
    ],
    "absolute_url": "/opinion/7343085/connick-v-thompson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 213505,
        "score": 120,
        "case_name": "Connick v. Thompson"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "179 L. Ed. 2d 417",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "417",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 1350",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "1350",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 51",
        "volume": "563",
        "reporter": "U.S.",
        "page": "51",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 887",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "887",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 U.S.L.W. 4195",
        "volume": "79",
        "reporter": "U.S.L.W.",
        "page": "4195",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 2594",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "2594",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "179 L. Ed. 2d 417",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "417",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 2594",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "2594",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 1350",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "1350",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 51",
        "volume": "563",
        "reporter": "U.S.",
        "page": "51",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 887",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "887",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 U.S.L.W. 4195",
        "volume": "79",
        "reporter": "U.S.L.W.",
        "page": "4195",
        "type": 4,
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
      "id": "pin-62",
      "page": null,
      "quote": "--- # Connick v. Thompson *563 U.S. 51 (2011)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background John Thompson was convicted of armed robbery and murder in New Orleans and spent years on death row before it emerged that prosecutors in District Attorney Harry Connick's office had suppressed a crime-lab report (blood-type evidence) favorable to him, in violation of [[Brady v. Maryland]]. His convictions were vacated and he was acquitted on retrial. He sued the District Attorney's Office under \u00a7 1983, claiming Connick had been deliberately indifferent in failing to train prosecutors on their *Brady* obligations. A jury awarded him $14 million. ## Issue Whether a district attorney's office may be held liable under \u00a7 1983 for failure to train its prosecutors on *Brady* based on a single violation, absent a pattern of similar violations. ## Rule A pattern of violations is ordinarily required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-64",
      "page": null,
      "quote": "narrow range",
      "star_marker": "428",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 39484,
      "fragment": "#:~:text=a-,narrow%20range",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-03-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Connick v. Thompson",
    "varies_by_point": false,
    "scope_note": "Good law: a single Brady violation, without a pattern, does not establish municipal failure-to-train liability.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Connick v. Thompson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramona Hinojosa v. Brad Livingston",
          "cluster_id": 3155936,
          "cite": [
            "807 F.3d 657",
            "2015 U.S. App. LEXIS 20016",
            "2015 WL 7422990"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Prall v. City of Boston",
          "cluster_id": 8729956,
          "cite": [
            "985 F. Supp. 2d 115",
            "2013 WL 6076462",
            "2013 U.S. Dist. LEXIS 166128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Foley v. Town of Lee",
          "cluster_id": 8716566,
          "cite": [
            "871 F. Supp. 2d 39",
            "2012 DNH 081",
            "2012 WL 1624947",
            "2012 U.S. Dist. LEXIS 64907"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Town of East Haven",
          "cluster_id": 8441252,
          "cite": [
            "691 F.3d 72",
            "2012 U.S. App. LEXIS 15928",
            "2012 WL 3104523"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haley v. City of Boston",
          "cluster_id": 613874,
          "cite": [
            "657 F.3d 39",
            "2011 U.S. App. LEXIS 19223",
            "2011 WL 4347027"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Porter v. Epps",
          "cluster_id": 614341,
          "cite": [
            "659 F.3d 440",
            "2011 U.S. App. LEXIS 19756",
            "2011 WL 4471051"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Julie Helphenstine v. Lewis County",
          "cluster_id": 9374379,
          "cite": [
            "60 F.4th 305"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matusick v. Erie County Water Authority",
          "cluster_id": 8441814,
          "cite": [
            "757 F.3d 31",
            "2014 WL 700718"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
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
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saldivar v. Racine",
          "cluster_id": 3189097,
          "cite": [
            "818 F.3d 14",
            "2016 U.S. App. LEXIS 5623",
            "2016 WL 1169397"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tamika Johnson v. City of Philadelphia",
          "cluster_id": 4787333,
          "cite": [
            "975 F.3d 394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gray v. Cummings",
          "cluster_id": 4593291,
          "cite": [
            "917 F.3d 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pearlie Gambrel v. Knox Cnty., Ky.",
          "cluster_id": 6347889,
          "cite": [
            "25 F.4th 391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Reck v. Wexford Health Sources, Inc.",
          "cluster_id": 6444901,
          "cite": [
            "27 F.4th 473"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nathson Fields v. City of Chicago",
          "cluster_id": 4820969,
          "cite": [
            "981 F.3d 534"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henderson v. Harris County",
          "cluster_id": 8248448,
          "cite": [
            "51 F.4th 125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefebure v. D'aquila",
          "cluster_id": 5287572,
          "cite": [
            "15 F.4th 650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George v. Beaver County",
          "cluster_id": 6465265,
          "cite": [
            "32 F.4th 1246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teresa Graham v. Shannon Barnette",
          "cluster_id": 4900401,
          "cite": [
            "5 F.4th 872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniel Robbins v. City of Des Moines",
          "cluster_id": 4845312,
          "cite": [
            "984 F.3d 673"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. Walsh",
          "cluster_id": 4471312,
          "cite": [
            "884 F.3d 16"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerald Marshall v. Town of Dexter",
          "cluster_id": 3134066,
          "cite": [
            "2015 ME 135",
            "125 A.3d 1141",
            "2015 Me. LEXIS 147"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Friend v. Gasparino",
          "cluster_id": 9379829,
          "cite": [
            "61 F.4th 77"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crittindon v. LeBlanc",
          "cluster_id": 6476851,
          "cite": [
            "37 F.4th 177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Timmy Mosier v. Joseph Evans",
          "cluster_id": 9458549,
          "cite": [
            "90 F.4th 541"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Hightower v. City of Philadelphia",
          "cluster_id": 10352157,
          "cite": [
            "130 F.4th 352"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Connick v. Thompson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7261027 OR 7261028 OR 7261029) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 109,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 109,
        "triage_read": 5,
        "triage_snippet_classified": 104
      },
      "lane2_top_cited": {
        "query": "cites:(7261027 OR 7261028 OR 7261029)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMCZzPTg3MTI3MDkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%287261027+OR+7261028+OR+7261029%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(7261027 OR 7261028 OR 7261029)",
        "reviewed": 51,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 51,
        "triage_read": 0,
        "triage_snippet_classified": 51
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(7261027 OR 7261028 OR 7261029)",
    "indexed_citing_opinions": 171,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7261027,
        "count": 171,
        "count_source": "search"
      },
      {
        "opinion_id": 7261028,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 7261029,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4362,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/connick-v-thompson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4ODkxOTUmcz0xMDAwMTEzNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%287261027+OR+7261028+OR+7261029%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T01:01:06Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Connick v. Thompson

```
<opinion type="majority">
<p id="b520-12">OPINION OF THE COURT</p>
<p id="b520-5">[<span class="citation no-link">563 U.S. 54</span>]</p>
<author id="b520-6">Justice Thomas</author>
<p id="apa-dedup-2">delivered the opinion of the Court.</p>
<p id="b520-7">The Orleans Parish District Attorney’s Office now concedes that, in prosecuting respondent John Thompson for attempted armed robbery, prosecutors failed to disclose evidence that should have been turned over to the defense under <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S. Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L. Ed. 2d 215</a></span> (1963). Thompson was convicted. Because of that conviction Thompson elected not to testify defense in his later trial for murder, and he was again convicted. Thompson spent 18 years in prison, including 14 years on death row. One month before Thompson’s scheduled execution, his investigator discovered the undisclosed evidence from his armed robbery trial. The reviewing court determined that the evidence was exculpatory, and both of Thompson’s convictions were vacated.</p>
<p id="b520-8">After his release from prison, Thompson sued petitioner Harry Con-nick, in his official capacity as the Orleans Parish district attorney, for damages under Rev. Stat. § 1979, <span class="citation no-link">42 U.S.C. § 1983</span>. Thompson alleged that Connick had failed to train his prosecutors adequately about their duty to produce exculpatory evidence and that the lack of training had caused the nondisclosure in Thompson’s robbery case. The jury awarded Thompson $14 million, and the Court of Appeals for the Fifth Circuit affirmed by an evenly divided en banc court. We granted certiorari to decide whether  a district attorney’s office may be held liable under § 1983 for failure to train based on a single <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation. We hold that it cannot.</p>
<p id="b520-14">I</p>
<p id="b520-15">A</p>
<p id="b520-16">In early 1985, John Thompson was charged with the murder of Raymond T. Liuzza, Jr., in New Orleans. Publicity following the murder charge led <page-number citation-index="1" label="423">*423</page-number>the victims of an unrelated</p>
<p id="aof-dedup-1">[<span class="citation no-link">563 U.S. 55</span>]</p>
<p id="b521-4">armed robbery to identify Thompson as their attacker. The district attorney charged Thompson with attempted armed robbery.</p>
<p id="b521-6">As part of the robbery investigation, a crime scene technician took from one of the victims’ pants a swatch of fabric stained with the robber’s blood. Approximately one week before Thompson’s armed robbery trial, the swatch was sent to the crime laboratory. Two days before the trial, Assistant District Attorney Bruce Whittaker received the crime lab’s report, which stated that the perpetrator had blood type B. There is no evidence that the prosecutors ever had Thompson’s blood tested or that they knew what his blood type was. Whittaker claimed he placed the report on Assistant District Attorney James Williams’ desk, but Williams denied seeing it. The report was never disclosed to Thompson’s counsel.</p>
<p id="b521-7">Williams tried the armed robbery case with Assistant District Attorney Gerry Deegan. On the first day of trial, Deegan checked all of the physical evidence in the case out of the police property room, including the bloodstained swatch. Deegan then checked all of the evidence but the swatch into the courthouse property room. The prosecutors did not mention the swatch or the crime lab report at trial, and the jury convicted Thompson of attempted armed robbery.</p>
<p id="b521-8">A few weeks later, Williams and Special Prosecutor Eric Dubelier tried Thompson for the Liuzza murder. Because of the armed robbery conviction, Thompson chose not to testify in his own defense. He was convicted and sentenced to death. <em>State </em>v. <em>Thompson, </em><span class="citation" data-id="1678561"><a href="/opinion/1678561/state-v-thompson/" aria-description="Citation for case: State v. Thompson">516 So. 2d 349</a></span> (La. 1987). In the 14 years following Thompson’s murder conviction, state and federal courts reviewed and denied his challenges to the conviction and sentence. See <em>State ex rel. Thompson </em>v. <em>Cain, </em>95-2463 (La. 4/25/96), <span class="citation" data-id="7696643"><a href="/opinion/7759076/state-ex-rel-thompson-v-cain/" aria-description="Citation for case: State ex rel. Thompson v. Cain">672 So. 2d 906</a></span>; <em>Thompson </em>v. <em>Cain, </em><span class="citation" data-id="16134"><a href="/opinion/16134/thompson-v-cain/" aria-description="Citation for case: Thompson v. Cain">161 F.3d 802</a></span> (CA5 1998). The State scheduled Thompson’s execution for May 20, 1999.</p>
<p id="b521-9">[<span class="citation no-link">563 U.S. 56</span>]</p>
<p id="b521-10">In late April 1999, Thompson’s private investigator discovered the crime lab report from the armed robbery investigation in the files of the New Orleans Police Crime Laboratory. Thompson was tested and found to have blood type O, proving that the blood on the swatch was not his. Thompson’s attorneys presented this evidence to the district attorney’s office, which, in turn, moved to stay the execution and vacate Thompson’s armed robbery conviction.<footnotemark>1</footnotemark> The Louisiana Court of Appeal then reversed Thompson’s murder conviction, concluding that the armed robbery conviction unconstitutionally deprived Thompson of his right to testify in his own defense at the murder trial. <em>State </em>v. <em>Thompson, </em>2002-0361 (La. App. 7/17/02), <span class="citation" data-id="1714044"><a href="/opinion/1714044/state-v-thompson/" aria-description="Citation for case: State v. Thompson">825 So. 2d 552</a></span>. In 2003, the district attorney’s office retried Thomp<page-number citation-index="1" label="424">*424</page-number>son for Liuzza’s murder.<footnotemark>2</footnotemark> The jury found him not guilty.</p>
<p id="b522-4">B</p>
<p id="b522-5">Thompson then brought this action against the district attorney’s office, Connick, Williams, and others, alleging that their conduct caused him to be wrongfully convicted, incarcerated for 18 years, and nearly executed. The only claim that proceeded to trial was Thompson’s claim under § 1983 that the district attorney’s office had violated <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>by failing</p>
<p id="b522-6">[<span class="citation no-link">563 U.S. 57</span>]</p>
<p id="b522-7">to disclose the crime lab report in his armed robbery trial. See <em>Brady, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S. Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L. Ed. 2d 215</a></span>. Thompson alleged liability under two theories: (1) The <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation was caused by an unconstitutional policy of the district attorney’s office; and (2) the violation was caused by Connick’s deliberate indifference to an obvious need to train the prosecutors in his office in order to avoid such constitutional violations.</p>
<p id="b522-8">Before trial, Connick conceded that the failure to produce the crime lab report constituted a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation.<footnotemark>3</footnotemark> See Record EX608, EX880. Accordingly, the District Court instructed the jury that the “only issue” was whether the nondisclosure was caused by either a policy, practice, or custom of the district attorney’s office or a deliberately indifferent failure to train the office’s prosecutors. <em>Id., </em>at 1615.</p>
<p id="b522-9">Although no prosecutor remembered any specific training session regarding <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>prior to 1985, it was undisputed at trial that the prosecutors were familiar with the general <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>requirement that the State disclose to the defense evidence in its possession that is favorable to the accused. Prosecutors testified that office policy was to turn crime lab reports and other scientific evidence over to the defense. They also testified that, after the discovery of the undisclosed crime lab report in 1999, prosecutors disagreed about whether it had to be disclosed under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>absent knowledge of Thompson’s blood type.</p>
<p id="b522-11">The jury rejected Thompson’s claim that an unconstitutional office policy caused the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation, but found the district attorney’s office liable for failing to train the prosecutors. The jury awarded Thompson $14 million in damages, and the District Court added more than $1 million in attorney’s fees and costs.</p>
<p id="b522-12">After the verdict, Connick renewed his objection—which he had raised on summary judgment—that he could not have</p>
<p id="b522-13">[<span class="citation no-link">563 U.S. 58</span>]</p>
<p id="b522-14">been deliberately indifferent to an obvious need for more or different <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training because there was no evidence that he was aware of a pattern of similar <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations. The District Court rejected this argument for the reasons that it had given in the summary judgment order. In that order, the court had concluded that a pattern of violations is not necessary to prove deliberate indifference when the need for training is “so obvious.” No. Civ. A. 03-2045 (ED La., Nov. 15, 2005), App. to Pet. for Cert. <page-number citation-index="1" label="425">*425</page-number>141a, <span class="citation no-link">2005 WL 3541035</span>, *13. Relying on <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">489 U.S. 378</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (1989), the court had held that Thompson could demonstrate deliberate indifference by proving that “the DA’s office knew to a moral certainty that assis-tan[t] [district attorneys] would acquire <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material, that without training it is not always obvious what <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>requires, and that withholding <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material will virtually always lead to a substantial violation of constitutional rights.”<footnotemark>4</footnotemark> App. to Pet. for Cert. 141a, <span class="citation no-link">2005 WL 3541035</span>, *13.</p>
<p id="b523-4">A panel of the Court of Appeals for the Fifth Circuit affirmed. The panel acknowledged that Thompson did not present evidence of a pattern of similar <em>Brady </em>violations, <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#851" aria-description="Citation for case: Thompson v. Connick">553 F.3d 836, 851</a></span> (2008), but held that Thompson did not need to prove a pattern, <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#854" aria-description="Citation for case: Thompson v. Connick">id., at 854</a></span>. According to the panel, Thompson demonstrated that Connick was on notice of an obvious need for <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training by presenting evidence “that attorneys, often fresh out of law school, would undoubtedly be required to confront <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>issues while at the DA’s Office, that erroneous decisions regarding <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence would result in serious constitutional violations, that resolution of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>issues was often unclear, and that training in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>would have been helpful.” <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#854" aria-description="Citation for case: Thompson v. Connick">553 F.3d, at 854</a></span>.</p>
<p id="b523-5">[<span class="citation no-link">563 U.S. 59</span>]</p>
<p id="b523-6">The Court of Appeals sitting en banc vacated the panel opinion, granted rehearing, and divided evenly, thereby affirming the District Court. <span class="citation" data-id="9634025"><a href="/opinion/1456596/thompson-v-connick/" aria-description="Citation for case: Thompson v. Connick">578 F.3d 293</a></span> (CA5 2009) <em>(per curiam). </em>In four opinions, the divided en banc court disputed whether Thompson could establish municipal liability for failure to train the prosecutors based on the single <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation without proving a prior pattern of similar violations, and, if so, what evidence would make that showing. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.S./559/1004/">559 U.S. 1004</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./130/1880/">130 S. Ct. 1880</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/176/399/">176 L. Ed. 2d 399</a></span> (2010).</p>
<p id="b523-8">II</p>
<p id="b523-9">The <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation conceded in this case occurred when one or more of the four prosecutors involved with Thompson’s armed robbery prosecution failed to disclose the crime lab report to Thompson’s counsel. Under Thompson’s failure-to-train theory, he bore the burden of proving both (1) that Connick, the policymaker for the district attorney’s office, was deliberately indifferent to the need to train the prosecutors about their <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>disclosure obligation with respect to evidence of this type and (2) that the lack of training actually caused the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation in this case. Connick argues that he was entitled to judgment as a matter of law because Thompson did not prove that he was on actual or constructive notice of, and therefore deliberately indifferent to, a need for more or different <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training. We agree.<footnotemark>5</footnotemark></p>
<p id="b523-10">[<span class="citation no-link">563 U.S. 60</span>]</p>
<p id="b523-11">A</p>
<p id="b523-12">Title <span class="citation no-link">42 U.S.C. § 1983</span> provides in relevant part:</p>
<blockquote id="b523-13">“Every person who, under color of any statute, ordinance, <page-number citation-index="1" label="426">*426</page-number>regulation, custom, or usage, of any State . . . subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress . . . .”</blockquote>
<p id="b524-4">A municipality or other local government may be liable under this section if the governmental body itself “subjects” a person to a deprivation of rights or “causes” a person “to be subjected” to such deprivation. See <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#692" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S. 658, 692</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span> (1978). But, under § 1983, local governments are responsible only for “their <em>own </em>illegal acts.” <em>Pembaur </em>v. <em>Cincinnati, </em><span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#479" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U.S. 469, 479</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">106 S. Ct. 1292</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">89 L. Ed. 2d 452</a></span> (1986) (citing <em>Monell, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#665" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S., at 665-683</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>). They are not vicariously liable under § 1983 for their employees’ actions. See <em>id.., </em>at 691, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>; <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 392</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>; <em>Board of Comm’rs of Bryan Cty. </em>v. <em>Brown, </em><span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#403" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S. 397, 403</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span> (1997) (collecting cases).</p>
<p id="b524-6">Plaintiffs who seek to impose liability on local governments under § 1983 must prove that “action pursuant to official municipal policy” caused their injury. <em>Monell, </em>436 U.S.,</p>
<p id="b524-7">[<span class="citation no-link">563 U.S. 61</span>]</p>
<p id="b524-8">at 691, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>; see <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>id., </em>at 694</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>. Official municipal policy includes the decisions of a government’s lawmakers, the acts of its policymaking officials, and practices so persistent and widespread as to practically have the force of law. See <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#480" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>ibid.; Pembaur, supra, </em>at 480-481</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">106 S. Ct. 1292</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">89 L. Ed. 2d 452</a></span>; <em>Adickes </em>v. <em>S. H. Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#167" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U.S. 144, 167-168</a></span>, <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">90 S. Ct. 1598</a></span>, <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">26 L. Ed. 2d 142</a></span> (1970). These are “action [s] for which the municipality is actually responsible.” <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#479" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>Pembaur, supra, </em>at 479-480</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">106 S. Ct. 1292</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">89 L. Ed. 2d 452</a></span>.</p>
<p id="b524-9">In limited circumstances, a local government’s decision not to train certain employees about their legal duty to avoid violating citizens’ rights may rise to the level of an official government policy for purposes of § 1983. A municipality’s culpability for a depri<page-number citation-index="1" label="427">*427</page-number>vation of rights is at its most tenuous where a claim turns on a failure to train. See <em>Oklahoma City </em>v. <em>Tuttle, </em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#822" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U.S. 808, 822-823</a></span>, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">105 S. Ct. 2427</a></span>, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">85 L. Ed. 2d 791</a></span> (1985) (plurality opinion) (“[A] ‘policy’ of ‘inadequate training’ ” is “far more nebulous, and a good deal further removed from the constitutional violation, than was the policy in <em>Monell”). </em>To satisfy the statute, a municipality’s failure to train its employees in a relevant respect must amount to “deliberate indifference to the rights of persons with whom the [untrained employees] come into contact.” <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#388" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 388</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. Only then “can such a shortcoming be properly thought of as a city ‘policy or custom’ that is actionable under § 1983.” <em>Id., </em>at 389, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>.</p>
<p id="b525-4">“ ‘[Deliberate indifference’ is a stringent standard of fault, requiring proof that a municipal actor disregarded a known or obvious consequence of his action.” <em>Bryan Cty., </em><span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#410" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S., at 410</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Thus, when city policymakers are on actual or constructive notice that a particular omission in their training program causes city employees to violate citizens’ constitutional rights, the city may be deemed deliberately indifferent if the policymakers choose to retain that program. <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#407" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown"><em>Id., </em>at 407</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. The city’s “ ‘policy of inaction’ ” in light of notice that its program will cause constitutional violations “is the functional equivalent of a decision by the city itself to violate</p>
<p id="ApE_">[<span class="citation no-link">563 U.S. 62</span>]</p>
<p id="b525-5">the Constitution.” <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#395" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 395</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (O’Connor, J., concurring in part and dissenting in part). A less stringent standard of fault for a failure-to-train claim “would result in <em>de facto respondeat superior </em>liability on municipalities .... <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris"><em>" Id., </em>at 392</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>; see also <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#483" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>Pembaur, supra, </em>at 483</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">106 S. Ct. 1292</a></span>, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">89 L. Ed. 2d 452</a></span> (opinion of Brennan, J.) (“[M]unicipal liability under § 1983 attaches where—and only where—a deliberate choice to follow a course of action is made from among various alternatives by [the relevant] officials . . . ”).</p>
<p id="b525-7">B</p>
<p id="b525-8">A pattern of similar constitutional violations by untrained employees is “ordinarily necessary” to demonstrate deliberate indifference for purposes of failure to train. <em>Bryan Cty., </em><span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#409" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S., at 409</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Policymakers’ “continued adherence to an approach that they know or should know has failed to prevent tortious conduct by employees may establish the conscious disregard for the consequences of their action—the ‘deliberate indifference’—necessary to trigger municipal liability.” <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#407" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown"><em>Id., </em>at 407</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Without notice that a course of training is deficient in a particular respect, decisionmakers can hardly be said to have deliberately chosen a training program that will cause violations of constitutional rights.</p>
<p id="b525-9">Although Thompson does not contend that he proved a pattern of similar <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations, <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#851" aria-description="Citation for case: Thompson v. Connick">553 F.3d, at 851</a></span>, vacated, <span class="citation" data-id="9634025"><a href="/opinion/1456596/thompson-v-connick/" aria-description="Citation for case: Thompson v. Connick">578 F.3d 293</a></span> (en banc), he points out that, during the 10 years preceding his armed robbery trial, <page-number citation-index="1" label="428">*428</page-number>Louisiana courts had overturned four convictions because of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations by prosecutors in Connick’s office.<footnotemark>6</footnotemark> Those four reversals could not have put Connick on notice that the office’s <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training was inadequate with respect to the sort of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation at issue here. None of those cases involved failure to disclose blood evidence, a crime lab report, or physical or</p>
<p id="b526-4">[<span class="citation no-link">563 U.S. 63</span>]</p>
<p id="b526-5">scientific evidence of any kind. Because those incidents are not similar to the violation at issue here, they could not have put Connick on notice that specific training was necessary to avoid this constitutional violation.<footnotemark>7</footnotemark></p>
<p id="b526-6">C</p>
<p id="b526-7">1</p>
<p id="b526-8">Instead of relying on a pattern of similar <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations, Thompson relies on the “single-incident” liability that this Court hypothesized in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>. </em>He contends that the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation in his case was the “obvious” consequence of failing to provide specific <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training, and that this showing of “obviousness” can substitute for the pattern of violations ordinarily necessary to establish municipal culpability.</p>
<p id="b526-9">In <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>, </em>the Court left open the possibility that, “in a narrow range of circumstances,” a pattern of similar violations might not be necessary to show deliberate indifference. <em>Bryan Cty., supra, </em>at 409, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. The Court posed the hypothetical example of a city that arms its police force with firearms and deploys the armed officers into the public to capture fleeing felons without training the officers in the constitutional limitation on the use of deadly force. <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#390" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 390, n. 10</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. Given the known frequency with which police attempt to arrest fleeing felons and the “predictability that an officer lacking specific tools to handle that situation will violate citizens’ rights,” the Court theorized that a city’s decision not to train the officers about constitutional limits on</p>
<p id="AF9I">[<span class="citation no-link">563 U.S. 64</span>]</p>
<p id="b526-11">the use of deadly force could reflect the city’s deliberate indifference to the “highly predictable consequence,” namely, violations of constitutional rights. <em>Bryan Cty., supra, </em>at 409, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. The Court sought not to foreclose the possibility, however rare, that the unconstitutional consequences of failing to train could be so patently obvious that a city could be liable under § 1983 without proof of a pre-existing pattern of violations.</p>
<p id="b526-12">Failure to train prosecutors in their <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligations does not fall within the narrow range of <em>Canton’s </em>hypoth<page-number citation-index="1" label="429">*429</page-number>esized single-incident liability. The obvious need for specific legal training that was present in the <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>scenario is absent here. Armed police must sometimes make split-second decisions with life-or-death consequences. There is no reason to assume that police academy applicants are familiar with the constitutional constraints on the use of deadly force. And, in the absence of training, there is no way for novice officers to obtain the legal knowledge they require. Under those circumstances there is an obvious need for some form of training. In stark contrast, legal “[t] raining is what differentiates attorneys from average public employees.” <span class="citation" data-id="9634025"><a href="/opinion/1456596/thompson-v-connick/#304" aria-description="Citation for case: Thompson v. Connick">578 F.3d, at 304-305</a></span> (opinion of Clement, J.).</p>
<p id="b527-4">Attorneys are trained in the law and equipped with the tools to interpret and apply legal principles, understand constitutional limits, and exercise legal judgment. Before they may enter the profession and receive a law license, all attorneys must graduate from law school or pass a substantive examination; attorneys in the vast majority of jurisdictions must do both. See, <em>e.g., </em>La. State Bar Assn. (LSBA), Articles of Incorporation, La. Rev. Stat. Ann. § 37, ch. 4, App., Art. 14, § 7 (1988 West Supp.) (as amended through 1985). These threshold requirements are designed to ensure that all new attorneys have learned how to find, understand, and apply legal rules. Cf. <em>United States </em>v. <em>Cronic, </em><span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#658" aria-description="Citation for case: United States v. Cronic">466 U.S. 648, 658, 664</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">104 S. Ct. 2039</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">80 L. Ed. 2d 657</a></span> (1984) (noting that the presumption “that the lawyer is competent to provide the guiding hand that the defendant</p>
<p id="ABqa">[<span class="citation no-link">563 U.S. 65</span>]</p>
<p id="b527-5">needs” applies even to young and inexperienced lawyers in their first jury trial and even when the case is complex).</p>
<p id="b527-6">Nor does professional training end at graduation. Most jurisdictions require attorneys to satisfy continuing-education requirements. See, <em>e.g., </em>LSBA, Articles of Incorporation, Art. 16, Rule 1.1(b) (effective 1987); La. Sup. Ct. Rule XXX (effective 1988). Even those few jurisdictions that do not impose mandatory continuing-education requirements mandate that attorneys represent their clients competently and encourage attorneys to engage in continuing study and education. See, <em>e.g., </em>Mass. Rule Prof. Conduct 1.1 and comment 6 (West 2006). Before Louisiana adopted continuing-education requirements, it imposed similar general competency requirements on its state bar. LSBA, Articles of Incorporation, Art. 16, EC 1—1, 1-2, DR 6-101 (West 1974) (effective 1971).</p>
<p id="b527-7">Attorneys who practice with other attorneys, such as in district attorney’s offices, also train on the job as they learn from more experienced attorneys. For instance, here in the Orleans Parish District Attorney’s Office, junior prosecutors were trained by senior prosecutors who supervised them as they worked together to prepare cases for trial, and trial chiefs oversaw the preparation of the cases. Senior attorneys also circulated court decisions and instructional memo-randa to keep the prosecutors abreast of relevant legal developments.</p>
<p id="b527-8">In addition, attorneys in all jurisdictions must satisfy character and fitness standards to receive a law license and are personally subject to an ethical regime designed to reinforce the profession’s standards. See, <em>e.g., </em>LSBA, Articles of Incorporation, Art. 14, § 7 (1985); see generally <em>id., </em>Art. 16 (1971) (Code of Professional Responsibility). Trial lawyers have a “duty to bring to bear such skill and <page-number citation-index="1" label="430">*430</page-number>knowledge as will render the trial a reliable adversarial testing process.” <em>Strickland </em>v. <em>Washington, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#688" aria-description="Citation for case: Strickland v. Washington">466 U.S. 668, 688</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S. Ct. 2052</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">80 L. Ed. 2d 674</a></span> (1984). Prosecutors have a special “duty to seek justice, not merely to</p>
<p id="AvOL">[<span class="citation no-link">563 U.S. 66</span>]</p>
<p id="b528-4">convict.” LSBA, Articles of Incorporation, Art. 16, EC 7-13 (1971); ABA Standards for Criminal Justice 3-1.1(c) (2d ed. 1980). Among prosecutors’ unique ethical obligations is the duty to produce <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence to the defense. See, <em>e.g., </em>LSBA, Articles of Incorporation, Art. 16, EC 7-13 (1971); ABA Model Rule of Prof. Conduct 3.8(d) (1984).<footnotemark>8</footnotemark> An attorney who violates his or her ethical obligations is subject to professional discipline, including sanctions, suspension, and disbarment. See, <em>e.g., </em>LSBA, Articles of Incorporation, Art. 15, §§ 5, 6 (1971); <em>id.., </em>Art. 16, DR 1-102; ABA Model Rule of Prof. Conduct 8.4 (1984).</p>
<p id="b528-5">In light of this regime of legal training and professional responsibility, recurring constitutional violations are not the “obvious consequence” of failing to provide prosecutors with formal in-house training about how to obey the law. <em>Bryan Cty., </em><span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#409" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S., at 409</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Prosecutors are not only equipped</p>
<p id="aye-dedup-1">[<span class="citation no-link">563 U.S. 67</span>]</p>
<p id="b528-7">but are also ethically bound to know what <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>entails and to perform legal research when they are uncertain. A district attorney is entitled to rely on prosecutors’ professional training and ethical obligations in the absence of specific reason, such as a pattern of violations, to believe that those tools are insufficient to prevent future constitutional violations in “the usual and recurring situations with which [the prosecutors] must deal.”<footnotemark>9</footnotemark> <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 391</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. A licensed attorney making legal judgments, in his capacity as a prosecutor, about <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material simply does not present the same “highly predictable” constitutional danger as <em>Canton’s </em>untrained officer.</p>
<p id="b528-8">A second significant difference between this case and the example in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>is the nuance of the allegedly necessary training. The <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>hypothetical assumes that the armed po<page-number citation-index="1" label="431">*431</page-number>lice officers have no knowledge at all of the constitutional limits on the use of deadly force. But it is undisputed here that the prosecutors in Connick’s office were familiar with the general <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule. Thompson’s complaint therefore cannot rely on the utter lack of an ability to cope with constitutional situations that underlies the <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>hypothetical, but rather must assert that prosecutors were not trained about particular <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence or the specific scenario related to the violation in his case. That sort of nuance simply cannot support an inference of deliberate indifference here. As the Court said in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>, </em>“[i]n virtually every instance where a person has had his or her constitutional rights violated by a city employee, a § 1983 plaintiff will be able to point to something the city ‘could have done’ to prevent the unfortunate incident.” <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 392</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (citing <em>Tuttle, </em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U.S., at 823</a></span>, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">105 S. Ct. 2427</a></span>, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">85 L. Ed. 2d 791</a></span> (plurality opinion)).</p>
<p id="b529-4">[<span class="citation no-link">563 U.S. 68</span>]</p>
<p id="b529-5">Thompson suggests that the absence of any <em>formal </em>training sessions about <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>is equivalent to the complete absence of legal training that the Court imagined in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>. </em>But failure-to-train liability is concerned with the substance of the training, not the particular instructional format. The statute does not provide plaintiffs or courts <em>carte blanche </em>to micromanage local governments throughout the United States.</p>
<p id="b529-7">We do not assume that prosecutors will always make correct <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>decisions or that guidance regarding specific <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>questions would not assist prosecutors. But showing merely that additional training would have been helpful in making difficult decisions does not establish municipal liability. “[P]rov[ing] that an injury or accident could have been avoided if an [employee] had had better or more training, sufficient to equip him to avoid the particular injury-causing conduct” will not suffice. <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 391</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. The possibility of single-incident liability that the Court left open in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>is not this case.<footnotemark>10</footnotemark></p>
<p id="b529-8">2</p>
<p id="b529-9">The dissent rejects our holding that <em>Canton’s </em>hypothesized single-incident liability does not, as a legal matter, encompass failure to train prosecutors in their <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligation. It would instead apply the <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>hypothetical to this case, and thus devotes almost all of its opinion to explaining</p>
<p id="AmMq">[<span class="citation no-link">563 U.S. 69</span>]</p>
<p id="b529-10">why the evidence supports liability under that theory.<footnotemark>11</footnotemark> But the dissent’s attempt to address our holding—by pointing out that not all prosecutors will necessarily have enrolled in <page-number citation-index="1" label="432">*432</page-number>criminal procedure class—misses the point. See <em>post, </em>at 106-107, 179 L. Ed. 2d, at 454-455. The reason why the <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>hypothetical is inapplicable</p>
<p id="avi-dedup-2">[<span class="citation no-link">563 U.S. 70</span>]</p>
<p id="b530-4">is that attorneys, unlike police officers, are equipped with the tools to find, interpret, and apply legal principles.</p>
<p id="b530-5">By the end of its opinion, however, the dissent finally reveals that its real disagreement is not with our holding today, but with this Court’s precedent. The dissent does not see “any reason,” <em>post, </em>at 108, 179 L. Ed. 2d, at 456, for the Court’s conclusion in <em>Bryan County </em>that a pattern of violations is “ordinarily necessary” to demonstrate deliberate indifference for purposes of failure to train, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/#409" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">520 U.S., at 409</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>. Cf. <em>id,, </em>at 406-408, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span> (explaining why a pattern of violations is ordinarily necessary). But cf. <em>post, </em>at 108, 179 L. Ed. 2d, at 455-456 (describing our reliance on <em>Bryan County </em>as “implying]” a new “limitation” on § 1983). As our precedent makes clear, proving that a municipality itself actually caused a constitutional violation by failing to train the offending employee presents “difficult problems of proof,” and we must adhere to a “stringent standard of fault,” lest municipal liability under § 1983 collapse into <em>respondeat superior,</em><footnotemark><em>12</em></footnotemark><em> Bryan Cty., supra, </em>at <page-number citation-index="1" label="433">*433</page-number>406, 410, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>; see <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 391-392</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>.</p>
<p id="b531-5">3</p>
<p id="b531-6">The District Court and the Court of Appeals panel erroneously believed that Thompson had proved deliberate indifference by showing the “obviousness” of a need for additional training. They based this conclusion on Con-nick’s awareness that (1) prosecutors would confront <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>issues while</p>
<p id="AHum">[<span class="citation no-link">563 U.S. 71</span>]</p>
<p id="b531-7">at the district attorney’s office; (2) inexperienced prosecutors were expected to understand <em>Brady’s </em>requirements; (3) <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>has gray areas that make for difficult choices; and (4) erroneous decisions regarding <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>evidence would result in constitutional violations. <span class="citation" data-id="64218"><a href="/opinion/64218/thompson-v-connick/#854" aria-description="Citation for case: Thompson v. Connick">553 F.3d, at 854</a></span>; App. to Pet. for Cert. 141a, <span class="citation no-link">2005 WL 3541035</span>, *13. This is insufficient.</p>
<p id="b531-8">It does not follow that, because <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>has gray areas and some <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>decisions are difficult, prosecutors will so obviously make wrong decisions that failing to train them amounts to “a decision by the city itself to violate the Constitution.” <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#395" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 395</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (O’Connor, J., concurring in part and dissenting in part). To prove deliberate indifference, Thompson needed to show that Connick was on notice that, absent additional specified training, it was “highly predictable” that the prosecutors in his office would be confounded by those gray areas and make incorrect <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>decisions as a result. In fact, Thompson had to show that it was <em>so </em>predictable that failing to train the prosecutors amounted to <em>conscious disregard, </em>for defendants’ <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rights. See <em>Bryan Cty., supra, </em>at 409, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">117 S. Ct. 1382</a></span>, <span class="citation" data-id="9842136"><a href="/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/" aria-description="Citation for case: Board of the County Commissioners of Bryan County v. Brown">137 L. Ed. 2d 626</a></span>; <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#389" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 389</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>. He did not do so.</p>
<p id="b531-9">III</p>
<p id="b531-10">The role of a prosecutor is to see that justice is done. <em>Berger </em>v. <em>United States, </em><span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U.S. 78, 88</a></span>, <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/" aria-description="Citation for case: Berger v. United States">55 S. Ct. 629</a></span>, <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/" aria-description="Citation for case: Berger v. United States">79 L. Ed. 1314</a></span> (1935). “It is as much [a prosecutor’s] duty to refrain from improper methods calculated to produce a wrongful conviction as it is to use every legitimate means to bring about a just one.” <em><span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/" aria-description="Citation for case: Berger v. United States">Ibid.</a></span> </em>By their own admission, the prosecutors who tried Thompson’s armed robbery case failed to carry out that responsibility. But the only issue before us is whether Connick, as the policymaker for the district attorney’s office, was deliberately indifferent to the need to train the attorneys under his authority.</p>
<p id="b531-11">We conclude that this case does not fall within the narrow range of “single-incident” liability hypothesized in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>as</p>
<p id="b531-12">[<span class="citation no-link">563 U.S. 72</span>]</p>
<p id="b531-13">a possible exception to the pattern of violations necessary to prove deliberate indifference in § 1983 actions alleging failure to train. The District Court should have granted Connick judgment as a matter of law on the failure-to-train claim because Thompson did not prove a pattern of similar violations that would “establish that the ‘policy of inaction’ [was] the functional equivalent of a decision by the city itself to violate the Constitution.” <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#395" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 395</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (opinion of O’Connor, J.).</p>
<p id="b531-14">The judgment of the United States Court of Appeals for the Fifth Circuit is reversed.</p>
<p id="b531-15">It is so ordered.</p>
<footnote label="1">
<p id="b521-11">. After Thompson discovered the crime lab report, former Assistant District Attorney Michael Riehlmann revealed that Deegan had confessed to him in 1994 that he had “intentionally suppressed blood evidence in the armed robbery trial of John Thompson that in some way exculpated the defendant.’’ Record EX583; see also <em>id., </em>at 2677. Deegan apparently had been recently diagnosed with terminal cancer when he made his confession. Following a disciplinary complaint by the district attorney’s office, the Supreme Court of Louisiana reprimanded Riehl-mann for failing to disclose Deegan’s admission earlier. <em>In re Riehlmann, </em>2004-0680 (La. 1/19/05), <span class="citation" data-id="1755140"><a href="/opinion/1755140/in-re-riehlmann/" aria-description="Citation for case: In Re Riehlmann">891 So. 2d 1239</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b522-15">. Thompson testified in his own defense at the second trial and presented evidence suggesting that another man committed the murder. That man, the government’s key witness at the first murder trial, had died in the interval between the first and second trials.</p>
</footnote>
<footnote label="3">
<p id="b522-16">. Because Connick conceded that the failure to disclose the crime lab report violated <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>that question is not presented here, and we do not address it.</p>
</footnote>
<footnote label="4">
<p id="b523-14">. The District Court rejected Connick’s proposed deliberate indifference jury instruction— which would have required Thompson to prove a pattern of similar violations—for the same reasons as the summary judgment motion. Tr. 1013; Record 993; see also Tr. of Oral Arg. 26.</p>
</footnote>
<footnote label="5">
<p id="b523-15">. Because we conclude that Thompson failed to prove deliberate indifference, we need not reach causation. Thus, we do not address whether the alleged training deficiency, or some other cause, was the “ ‘moving force,’ ” <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#389" aria-description="Citation for case: City of Canton v. Harris">489 U.S. 378, 389</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (1989) (quoting <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S. 658, 694</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <page-number citation-index="1" label="426">*426</page-number><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span> (1978), and <em>Polk County </em>v. <em>Dodson, </em><span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/#326" aria-description="Citation for case: Polk County v. Dodson">454 U.S. 312, 326</a></span>, <span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/" aria-description="Citation for case: Polk County v. Dodson">102 S. Ct. 445</a></span>, <span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/" aria-description="Citation for case: Polk County v. Dodson">70 L. Ed. 2d 509</a></span> (1981)), that “actually caused’’ the failure to disclose the crime lab report, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 391</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span>.</p>
<p id="b524-11">The same cannot be said for the dissent, however. Affirming the verdict in favor of Thompson would require finding both that he proved deliberate indifference and that he proved causation. Perhaps unsurprisingly, the dissent has not conducted the second step of the analysis, which would require showing that the failure to provide particular training (which the dissent never clearly identifies) “actually caused’’ the flagrant—and quite possibly intentional—misconduct that occurred in this case. See <em>post, </em>at 98, 179 L. Ed. 2d, at 449 (opinion of Ginsburg, J.) (assuming that, “[h] ad Brady’s importance been brought home to prosecutors,’’ the violation at issue “surely” would not have occurred). The dissent believes that evidence that the prosecutors allegedly “misappre-hen[ded]” <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>proves causation. <em>Post, </em>at 104, n. 20, 179 L. Ed. 2d, at 453-454. Of course, if evidence of a need for training, by itself, were sufficient to prove that the lack of training “actually caused” the violation at issue, no causation requirement would be necessary because every plaintiff who satisfied the deliberate indifference requirement would necessarily satisfy the causation requirement.</p>
</footnote>
<footnote label="6">
<p id="b526-13">. Thompson had every incentive at trial to attempt to establish a pattern of similar violations, given that the jury instruction allowed the jury to find deliberate indifference based on, among other things, prosecutors’ “history of mishandling’’ similar situations. Record 1619.</p>
</footnote>
<footnote label="7">
<p id="b526-14">. Thompson also asserts that this case is not about a “single incident’’ because up to four prosecutors may have been responsible for the nondisclosure of the crime lab report and, according to his allegations, withheld additional evidence in his armed robbery and murder trials. But contemporaneous or subsequent conduct cannot establish a pattern of violations that would provide “notice to the cit[y] and the opportunity to conform to constitutional dictates <em>Canton, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#395" aria-description="Citation for case: City of Canton v. Harris">489 U.S., at 395</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">109 S. Ct. 1197</a></span>, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">103 L. Ed. 2d 412</a></span> (O’Connor, J., concurring in part and dissenting in part). Moreover, no court has ever found any of the other <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations that Thompson alleges occurred in his armed robbery and murder trials.</p>
</footnote>
<footnote label="8">
<p id="b528-9">. The Louisiana State Bar Code of Professional Responsibility included a broad understanding of the prosecutor’s duty to disclose in 1985:</p>
<blockquote id="b528-10">“With respect to evidence and witnesses, the prosecutor has responsibilities different from those of a lawyer in private practice: the prosecutor should make timely disclosure to the defense of available evidence, known to him, that tends to negate the guilt of the accused, mitigate the degree of the offense, or reduce the punishment. Further, a prosecutor should not intentionally avoid pursuit of evidence merely because he believes it will damage the prosecution’s case or aid the accused.’’ LSBA, Articles of Incorporation, Art. 16, EC 7-13 (1971); see also ABA Model Rule of Prof. Conduct 3.8(d) (1984) (“The prosecutor in a criminal case shall. . . make timely disclosure to the defense of all evidence or information known to the prosecutor that tends to negate the guilt of the accused or mitigates the offense . . . ’’).</blockquote>
<p id="b528-11">In addition to these ethical rules, the Louisiana Code of Criminal Procedure, with which Louisiana prosecutors are no doubt familiar, in 1985 required prosecutors, upon order of the court, to permit inspection of evidence “favorable to the defendant . . . which [is] material and relevant to the issue of guilt or punishment,’’ La. Code Crim. Proc. Ann., Art. 718 (West 1981) (added 1977), as well as “any results or reports’’ of “scientific tests or experiments, made in connection with or material to the particular case,’’ if those reports are exculpatory or intended for use at trial, <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">id.,</a></span> </em>Art. 719.</p>
</footnote>
<footnote label="9">
<p id="b528-12">. Contrary to the dissent’s assertion, see <em>post, </em>at 108, n. 26, 179 L. Ed. 2d, at 456 (citing <em>post, </em>at 96-98, 179 L. Ed. 2d, at 448-449), a prosecutor’s youth is not a “specific reason’’ not to rely on professional training and ethical obligations. See <em>supra, </em>at 64-65, 179 L. Ed. 2d, at 428-429 (citing <em>United States </em>v. <em>Cronic, </em><span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#658" aria-description="Citation for case: United States v. Cronic">466 U.S. 648, 658, 664</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">104 S. Ct. 2039</a></span>, <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/" aria-description="Citation for case: United States v. Cronic">80 L. Ed. 2d 657</a></span> (1984)).</p>
</footnote>
<footnote label="10">
<p id="b529-11">. Thompson also argues that he proved deliberate indifference by “direct evidence of policymaker fault’’ and so, presumably, did not need to rely on circumstantial evidence at all. Brief for Respondent 37. In support, Thompson contends that Connick created a “culture of indifference’’ in the district attorney’s office, <em>id., </em>at 38, as evidenced by Connick’s own allegedly inadequate understanding of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>the office’s unwritten <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>policy that was later incorporated into a 1987 handbook, and an officewide “restrictive discovery policy,’’ Brief for Respondent 39-40. This argument is essentially an assertion that Connick’s office had an unconstitutional policy or custom. The jury rejected this claim, and Thompson does not challenge that finding.</p>
</footnote>
<footnote label="11">
<p id="b529-12">. The dissent spends considerable time finding new <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations in Thompson’s trials. See <em>post, </em>at 81-90, 179 L. Ed. 2d, at 439-445. How these violations are relevant even to the dissent’s own legal analysis is “a mystery.’’ <em>Post, </em>at 81, n. 2, 179 L. Ed. 2d, at 439. The dissent does not list these violations among the “[a]bundant evidence’’ that it believes supports the jury’s finding that <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>training was obviously necessary. <em>Post, </em>at 93, 179 L. Ed. 2d, at 446. Nor does <page-number citation-index="1" label="432">*432</page-number>the dissent quarrel with our conclusion that contemporaneous or subsequent conduct cannot establish a pattern of violations. The only point appears to be to highlight what the dissent sees as sympathetic, even if legally irrelevant, facts.</p>
<p id="b530-8">In any event, the dissent’s findings are highly suspect. In finding two of the “new” violations, the dissent belatedly tries to reverse the Court of Appeals’ 1998 decision that those <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>claims were “without merit.” Compare <em>Thompson </em>v. <em>Cain, </em><span class="citation" data-id="16134"><a href="/opinion/16134/thompson-v-cain/#806" aria-description="Citation for case: Thompson v. Cain">161 F.3d 802, 806-808</a></span> (CA5) <em>(rejectingBrady </em>claims regarding the Perkins-Liuzza audiotapes and the Perkins police report), with <em>post, </em>at 85-86, 179 L. Ed. 2d, at 442-443 (concluding that these were <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations). There is no basis to the dissent’s suggestion that materially new facts have called the Court of Appeals’ 1998 decision into question. Cf. <em>State </em>v. <em>Thompson, </em>2002-0361, p. 6 (La. App. 7/17/02), <span class="citation" data-id="1714044"><a href="/opinion/1714044/state-v-thompson/#555" aria-description="Citation for case: State v. Thompson">825 So. 2d 552, 555</a></span> (noting Thompson’s admission that some of his current <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>claims “ha[ve] been rejected by both the Louisiana Supreme Court and the federal courts”). Regarding the bloodstained swatch, which the dissent asserts prosecutors “blocked” the defense from inspecting by sending it to the crime lab for testing, <em>post, </em>at 84, 179 L. Ed. 2d, at 441, Thompson’s counsel conceded at oral argument that trial counsel had access to the evidence locker where the swatch was recorded as evidence. See Tr. of OralArg. 37, 42; Record EX42, EX43 (evidence card identifying “One (1) Piece of Victims <em>[sic] </em>Right Pants Leg, W/Blood” among the evidence in the evidence locker and indicating that some evidence had been checked out); Tr. 401 (testimony from Thompson’s counsel that he “[w]ent down to the evidence room and checked all of the evidence”); <em>id., </em>at 103, 369-370, 586, 602 (testimony that evidence card was “available to the public,” would have been available to Thompson’s counsel, and would have been seen by Thompson’s counsel because it was stapled to the evidence bag in “the normal process”). Moreover, the dissent cannot seriously believe that the jury could have found <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violations—indisputably, questions of law. See <em>post, </em>at 89, n. 10, 92, n. 11, 179 L. Ed. 2d, at 444-445, 446.</p>
</footnote>
<footnote label="12">
<p id="b530-9">. Although the dissent acknowledges that “deliberate indifference liability and <em>respondeat superior </em>liability are not one and the same,” the opinion suggests that it believes otherwise. <em>Post, </em>at 109, n. 28, 179 L. Ed. 2d, at 456; see, <em>e.g., post, </em>at 109, 179 L. Ed. 2d, at 456 (asserting that “the buck stops with [the district attorney]”); <em>post, </em>at 100, 179 L. Ed. 2d, at 451 (suggesting municipal liability attaches when “the prosecutors” themselves are “deliberately indifferent to what the law requires”). We stand by the longstanding rule—reaffirmed by a unanimous Court earlier this Term—that to prove a violation of § 1983, a plaintiff must prove that “the municipality’s own wrongful conduct” caused his injury, not that the municipality is ultimately responsible for the torts of its employees. <em>Los Angeles County </em>v. <em>Humphries, ante, </em><span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/#38" aria-description="Citation for case: Los Angeles County v. Humphries">562 U.S. 29, 38</a></span>, <span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/" aria-description="Citation for case: Los Angeles County v. Humphries">131 S. Ct. 447</a></span>, <span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/" aria-description="Citation for case: Los Angeles County v. Humphries">178 L. Ed. 2d 460</a></span> (2010); see <span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/#35" aria-description="Citation for case: Los Angeles County v. Humphries"><em>id., </em>at 35, 36</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./131/447/">131 S. Ct. 447</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/178/460/">178 L. Ed. 2d 460</a></span> (citing <em>Monell, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#691" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S., at 691</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S. Ct. 2018</a></span>, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L. Ed. 2d 611</a></span>).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Cooper v. California.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Cooper v. California"
type: case
citation: "386 U.S. 58 (1967)"
parallel_cite: "87 S. Ct. 788; 17 L. Ed. 2d 730"
neutral_cite: 1967 U.S. LEXIS 2199
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-02-20
docket: 103
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-02-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Cooper v. California
  varies_by_point: false
  scope_note: "Pre-dates the modern inventory line (Opperman/Bertine) and the articulated automobile exception, but remains good law as a reasonableness-of-custodial-search holding; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107360/cooper-v-california/"
  cluster_id: 107360
  opinion_id: 9423351
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[South Dakota v. Opperman]]", "[[Colorado v. Bertine]]", "[[Florida v. White]]", "[[Cardwell v. Lewis]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "impound", "forfeiture", "custodial-search", "reasonableness"]
holding: "A warrantless search of a car the police lawfully hold in custody for forfeiture is reasonable where the search is closely related to the reason the car was seized and is being retained; reasonableness, not state-law authorization, is the Fourth Amendment test."
lake:
  record_id: Cooper v. California
  status: verified
  projected_at: 2026-07-09
---

# Cooper v. California

*386 U.S. 58 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Cooper's arrest for a narcotics offense, officers impounded his car under a California statute requiring that a vehicle used in narcotics activity be seized and held "as evidence until a forfeiture has been declared or a release ordered." A week later, without a warrant, an officer searched the impounded car and found a piece of a brown paper sack used to wrap heroin; forfeiture was not declared until over four months after seizure. The state appellate court, reading *[[Preston v. United States]]*, held the search unreasonable.

## Issue
Whether a warrantless search of an automobile that the police are required by state law to seize and hold in custody pending forfeiture is reasonable under the Fourth Amendment.

## Rule
Reasonableness — not state-law authorization — is the test, and it turns on the facts: "whether a search and seizure is unreasonable within the meaning of the Fourth Amendment depends upon the facts and circumstances of each case." — 386 U.S. at 59. ^pin-59

A custodial search tied to the reason for the impoundment is reasonable: the "subsequent search of the car — whether the State had 'legal title' to it or not — was closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained." — *Id.* at 61. ^pin-61

Thus: "Under the circumstances of this case, we cannot hold unreasonable under the Fourth Amendment the examination or search of a car validly held by officers for use as evidence in a forfeiture proceeding." — [*Id.* at 62](https://www.courtlistener.com/opinion/107360/cooper-v-california/#:~:text=Under%20the%20circumstances%20of%20this). ^pin-62

## Application
Unlike *[[Preston v. United States|Preston]]* — where the car's custody (after a vagrancy arrest) was "totally unrelated" to the charge — here the statute required officers to seize and retain Cooper's car as evidence pending forfeiture, and they had to keep it for months. The search was closely connected to the reason for that custody, and "[i]t would be unreasonable to hold that the police, having to retain the car in their custody for such a length of time, had no right, even for their own protection, to search it." That the police could have obtained a warrant was no answer, because the test is whether the search was reasonable, not whether a warrant could have been procured.

## Conclusion
Affirmed. The warrantless search of a car lawfully held in police custody for forfeiture, closely related to the reason for that custody, was reasonable under the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Cooper* is an early custodial/forfeiture-search holding later joined by the inventory line ([[South Dakota v. Opperman]], [[Colorado v. Bertine]]) and the forfeiture-seizure rule of [[Florida v. White]].

## Appears on
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Cooper v. California*, 386 U.S. 58 (1967) — https://www.courtlistener.com/opinion/107360/cooper-v-california/ — pinpoints: 59, 61, 62.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5bf7ef1966fed7a2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Cooper v. California"}, "payload": {"all": [{"cite": "386 U.S. 58", "page": "58", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "386"}, {"cite": "87 S. Ct. 788", "page": "788", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "17 L. Ed. 2d 730", "page": "730", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "17"}, {"cite": "1967 U.S. LEXIS 2199", "page": "2199", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": "386 U.S. 58", "official": {"cite": "386 U.S. 58", "page": "58", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "386"}, "official_selection_present": true, "record_id": "Cooper v. California"}}
{"assertion_id": "22d70f86e1e8ff48", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-59", "record_id": "Cooper v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-59", "pinpoint_status": "slip-only", "quote": "A week later, without a warrant, an officer searched the impounded car and found a piece of a brown paper sack used to wrap heroin; forfeiture was not declared until over four months after seizure. The state appellate court, reading *Preston v. United States*, held the search unreasonable. ## Issue Whether a warrantless search of an automobile that the police are required by state law to seize and hold in custody pending forfeiture is reasonable under the Fourth Amendment. ## Rule Reasonableness — not state-law authorization — is the test, and it turns on the facts:", "quote_fidelity": "mismatch", "record_id": "Cooper v. California", "star_marker": null}}
{"assertion_id": "4a76862e3fddea3d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-62", "record_id": "Cooper v. California"}, "payload": {"fragment": "#:~:text=Under%20the%20circumstances%20of%20this", "page": null, "pin_id": "pin-62", "pinpoint_status": "star-verified", "quote": "Under the circumstances of this case, we cannot hold unreasonable under the Fourth Amendment the examination or search of a car validly held by officers for use as evidence in a forfeiture proceeding.", "quote_fidelity": "matched", "record_id": "Cooper v. California", "star_marker": "62"}}
{"assertion_id": "4e58e63d9f677062", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-61", "record_id": "Cooper v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-61", "pinpoint_status": "slip-only", "quote": "subsequent search of the car — whether the State had 'legal title' to it or not — was closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained.", "quote_fidelity": "mismatch", "record_id": "Cooper v. California", "star_marker": null}}
{"assertion_id": "33e779f8bfae3dd0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Cooper v. California"}, "payload": {"as_of_content": "1967-02-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Cooper v. California", "scope_note": "Pre-dates the modern inventory line (Opperman/Bertine) and the articulated automobile exception, but remains good law as a reasonableness-of-custodial-search holding; no negative treatment.", "varies_by_point": false}}
```

### lake record — Cooper v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Cooper v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Cooper v. California",
    "case_name_short": "Cooper",
    "case_name_full": "Cooper v. California",
    "input_case_name": "Cooper v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-02-20",
    "year": 1967,
    "docket": "103",
    "cluster_id": 107360,
    "lead_opinion_id": 9423351,
    "sibling_ids": [
      107360,
      9423351,
      9423352
    ],
    "absolute_url": "/opinion/107360/cooper-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8967442,
        "score": 20,
        "case_name": "Cooper v. California"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "386 U.S. 58",
      "volume": "386",
      "reporter": "U.S.",
      "page": "58",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 788",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "788",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 730",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "730",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2199",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2199",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "386 U.S. 58",
        "volume": "386",
        "reporter": "U.S.",
        "page": "58",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 788",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "788",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 730",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "730",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2199",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2199",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "386 U.S. 58",
    "official_selection": {
      "court_class": "scotus",
      "selected": "386 U.S. 58",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-59",
      "page": null,
      "quote": "A week later, without a warrant, an officer searched the impounded car and found a piece of a brown paper sack used to wrap heroin; forfeiture was not declared until over four months after seizure. The state appellate court, reading *Preston v. United States*, held the search unreasonable. ## Issue Whether a warrantless search of an automobile that the police are required by state law to seize and hold in custody pending forfeiture is reasonable under the Fourth Amendment. ## Rule Reasonableness \u2014 not state-law authorization \u2014 is the test, and it turns on the facts:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-61",
      "page": null,
      "quote": "subsequent search of the car \u2014 whether the State had 'legal title' to it or not \u2014 was closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-62",
      "page": null,
      "quote": "Under the circumstances of this case, we cannot hold unreasonable under the Fourth Amendment the examination or search of a car validly held by officers for use as evidence in a forfeiture proceeding.",
      "star_marker": "62",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8973,
      "fragment": "#:~:text=Under%20the%20circumstances%20of%20this",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-02-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Cooper v. California",
    "varies_by_point": false,
    "scope_note": "Pre-dates the modern inventory line (Opperman/Bertine) and the articulated automobile exception, but remains good law as a reasonableness-of-custodial-search holding; no negative treatment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Clarence E. Johnson",
          "cluster_id": 4343883,
          "cite": [
            "208 So. 3d 843",
            "2017 Fla. App. LEXIS 995"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Jordan Heath Dentler",
          "cluster_id": 4472853,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opinion No.",
          "cluster_id": 3262306,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Yarborough v. State",
          "cluster_id": 5268654,
          "cite": [
            "981 S.W.2d 846",
            "1998 Tex. App. LEXIS 6575",
            "1998 WL 734396"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte Bowers",
          "cluster_id": 1529526,
          "cite": [
            "886 S.W.2d 346",
            "1994 WL 456838"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2425299,
          "cite": [
            "867 S.W.2d 63",
            "1993 WL 461699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bassano",
          "cluster_id": 2428155,
          "cite": [
            "827 S.W.2d 557",
            "1992 WL 51165"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Walter Bryan Roberson",
          "cluster_id": 537703,
          "cite": [
            "897 F.2d 1092",
            "1990 U.S. App. LEXIS 4639",
            "1990 WL 27247"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
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
        "journal_ref": "Cooper v. California:lane2_top_cited"
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
        "journal_ref": "Cooper v. California:lane2_top_cited"
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
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Mosley",
          "cluster_id": 109336,
          "cite": [
            "46 L. Ed. 2d 313",
            "96 S. Ct. 321",
            "423 U.S. 96",
            "1975 U.S. LEXIS 100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
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
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. DeFillippo",
          "cluster_id": 110127,
          "cite": [
            "61 L. Ed. 2d 343",
            "99 S. Ct. 2627",
            "443 U.S. 31",
            "1979 U.S. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 2424950,
          "cite": [
            "988 S.W.2d 770",
            "1999 Tex. Crim. App. LEXIS 33",
            "1999 WL 212791"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
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
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Hass",
          "cluster_id": 109221,
          "cite": [
            "43 L. Ed. 2d 570",
            "95 S. Ct. 1215",
            "420 U.S. 714",
            "1975 U.S. LEXIS 5"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lafayette",
          "cluster_id": 110976,
          "cite": [
            "77 L. Ed. 2d 65",
            "103 S. Ct. 2605",
            "462 U.S. 640",
            "1983 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berger v. New York",
          "cluster_id": 107483,
          "cite": [
            "18 L. Ed. 2d 1040",
            "87 S. Ct. 1873",
            "388 U.S. 41",
            "1967 U.S. LEXIS 2964"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "PruneYard Shopping Center v. Robins",
          "cluster_id": 110292,
          "cite": [
            "64 L. Ed. 2d 741",
            "100 S. Ct. 2035",
            "447 U.S. 74",
            "1980 U.S. LEXIS 129",
            "6 Media L. Rep. (BNA) 1311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gunwall",
          "cluster_id": 1390131,
          "cite": [
            "720 P.2d 808",
            "106 Wash. 2d 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heitman v. State",
          "cluster_id": 2461257,
          "cite": [
            "815 S.W.2d 681",
            "60 U.S.L.W. 2074",
            "1991 Tex. Crim. App. LEXIS 160",
            "1991 WL 111761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cardwell v. Lewis",
          "cluster_id": 109069,
          "cite": [
            "41 L. Ed. 2d 325",
            "94 S. Ct. 2464",
            "417 U.S. 583",
            "1974 U.S. LEXIS 75",
            "69 Ohio Op. 2d 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edwards",
          "cluster_id": 108995,
          "cite": [
            "39 L. Ed. 2d 771",
            "94 S. Ct. 1234",
            "415 U.S. 800",
            "1974 U.S. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hendrickson",
          "cluster_id": 1135960,
          "cite": [
            "917 P.2d 563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cooper v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107360 OR 9423351 OR 9423352) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MDA1NjY0MDAwMDAmcz0xOTkyMDA3JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107360+OR+9423351+OR+9423352%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107360 OR 9423351 OR 9423352)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzQmcz0xMzQ5MjU4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107360+OR+9423351+OR+9423352%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107360 OR 9423351 OR 9423352)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 0,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107360 OR 9423351 OR 9423352)",
    "indexed_citing_opinions": 993,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107360,
        "count": 935,
        "count_source": "search"
      },
      {
        "opinion_id": 9423351,
        "count": 97,
        "count_source": "search"
      },
      {
        "opinion_id": 9423352,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1583,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/cooper-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3MzQ1NDgmcz02NDY0NTgwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107360+OR+9423351+OR+9423352%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107360,
        "cited_id": 102004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107360,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107360,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107360,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107360,
        "cited_id": 106862,
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
    "date_created": "2026-07-05T01:14:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:20:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:14:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Cooper v. California

```
<opinion type="majority">
<author id="b136-11">Mr. Justice Black</author>
<p id="A4A">delivered the opinion of the Court.</p>
<p id="Aiq">Petitioner was convicted in a California state court of selling heroin to a police informer. The conviction rested in part on the introduction in evidence of a small piece of a brown paper sack seized by police without a warrant from the glove compartment of an automobile which police, upon petitioner’s arrest, had impounded and were holding in a garage. The search occurred a week after the arrest of petitioner. Petitioner appealed his convic<page-number citation-index="1" label="59">*59</page-number>tion to the California District Court of Appeal which, considering itself bound by our holding and opinion in <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>, held that the search and seizure violated the Fourth Amendment’s ban of unreasonable searches and seizures. That court went on, however, to determine that this was harmless error under Art. VI, § 4½, of California’s Constitution which provides that judgments should not be set aside or reversed unless the court is of the opinion that the error “resulted in a miscarriage of justice.” <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/" aria-description="Citation for case: People v. Cooper">234 Cal. App. 2d 587</a></span>, <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/" aria-description="Citation for case: People v. Cooper">44 Cal. Rptr. 483</a></span>. The California Supreme Court declined to hear the case. We granted certiorari along with <em>Chapman </em>v. <em>California, ante, </em>p. 18, to consider whether the California harmless-error constitutional provision could' be used in this way to ignore the alleged federal constitutional error. <span class="citation multiple-matches"><a href="/c/U.%20S./384/904/">384 U. S. 904</a></span>. We have today passed upon the question in <em>Chapman, </em>but do not reach it in this case because we are satisfied that the lower court erroneously decided that our <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>case required that this, search be held- an unreasonable one within the meaning of the Fourth Amendment.</p>
<p id="b137-5">We made it clear in <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>that whether a search and seizure is unreasonable within the meaning of the Fourth Amendment depends upon the facts and circumstances of each case and pointed out, in particular, that searches of cars that are constantly movable may make the search of a car without a warrant a reasonable one although the result might be the opposite in a search of a home, a store, or other fixed piece of property. <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#366" aria-description="Citation for case: Preston v. United States">376 U. S., at 366-367</a></span>. In <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>the search was sought to be justified primarily on the ground that it was incidental to and part of a lawful arrest. There we said that “[o]nce an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest.” <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Id.,</a></span> </em>at -367. In the <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>case, it was alternatively argued that the warrantless <page-number citation-index="1" label="60">*60</page-number>search, after the arrest was over and while Preston’s car was being held for him by the police, was justified because the officers had probable cause to believe the car was stolen. But the police arrested Preston for vagrancy, not theft, and no claim was made that the police had Authority to hold his car on that charge. The search was therefore to be treated as though his car was in his own or his agent’s possession, safe from intrusions by the police or anyone else. The situation involving petitioner’s car is quite different.</p>
<p id="b138-4">Here, California’s Attorney General concedes that the search was not incident to an arrest. It is argued, however, that the search was reasonable on other grounds. Section 11611 of the California Health &amp; Safety Code provides that any officer making an arrest for ⅝ narcotics violation shall seize and deliver to the State Division of Narcotic Enforcement any vehicle used to store, conceal, transport, sell or facilitate the possession of. narcotics, such vehicle “to be <em>held as evidence </em>until a forfeiture has been declared or a release ordered.” <footnotemark>1</footnotemark> (Emphasis supplied.) Petitioner’s vehicle, which evidence showed had been used to carry oh his narcotics possession and transportation, was impounded by the officers and their duty required that it be kept “as evidence” until forfeiture proceedings were carried to a conclusion. The lower court concluded, as a matter of state law, that the state forfeiture statute did not by “clear and express language” <page-number citation-index="1" label="61">*61</page-number>authorize the officers to search petitioner’s car. <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/#598" aria-description="Citation for case: People v. Cooper">234 Cal. App. 2d, at 598</a></span>, <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/#491" aria-description="Citation for case: People v. Cooper">44 Cal. Rptr., at 491</a></span>. But the question here is not whether the search was authorized by state "law. The question is rather whether the search was reasonable under the Fourth Amendment. Just as a search authorized by state law may be an unreasonable one under that amendment, so may a search not expressly authorized by state law be justified as a constitutionally reasonable one. While it is true, as the lower court said, that “lawful custody of an automobile does not of itself dispense with constitutional requirements of searches thereafter made of it,” <em>ibid., </em>the reason for and nature of the custody may constitutionally justify the search. Preston was arrested for vagrancy. An arresting officer took his car to the station rather than just leaving it on the street. It was not suggested that this was done other than for Preston’s convenience or that the police had any right to impound the car and keep it from Preston or whomever he might send for it. The fact that the police had custody of Preston’s car was totally'unrelated to the vagrancy charge for which they arrested him. So was their subsequent search of the car.* This case is not <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span>, </em>nor is it controlled by it. Here the officers seized petitioner’s car because they were required, to do so by state law. They seized it because of the crime for which they arrested petitioner. They seized it to impound it' and they had to keep it until forfeiture proceedings were concluded. Their subsequent search of the car — whether the State had “legal title” to it or not— was closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained. The forfeiture of petitioner’s car did not take place until over four months after it was lawfully seized. It would be unreasonable to hold that the police, having to retain the car in their custody for such a length of time, had no right, even for their own <page-number citation-index="1" label="62">*62</page-number>protection, to search it. It is rio answer to say that the police could have obtained a search warrant, for “[t]he relevant test is not whether it is reasonable to procure a search warrant, but whether the search was reasonable.” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66</a></span>. Under the circumstances of this case, we cannot hold unreasonable under the Fourth Amendment the examination or search of a car validly held by officers for use as evidence in a forfeiture proceeding.</p>
<p id="b140-5">Our holding, of course, does not affect the State’s power to impose higher standards on searches and seizures than required by the Federal Constitution if it chooses to do so. And when such state standards alone have been violated, the State is free, without review by us, to apply its own state harmless-error rule to such errors of state law. There being no federal constitutional error her.e, there is no need for us to determine whether the lower court properly applied its state harmless-error rule.<footnotemark>2</footnotemark></p>
<p id="AvO">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b138-5"> Cal. Health &amp;'Safety Code §11610 provides:</p>
<blockquote id="b138-6">"The interest of any registered owner of a vehicle used to unlawfully transport or facilitate the unlawful transportation of any narcotic, or in which any narcotic is unlawfully kept, deposited, or concealed or which is used to facilitate the unlawful keeping, depositing or concealment of any narcotic, or in which any narcotic is unlawfully possessed -by ah occupant thereof or which is used to facilitate the unlawful possession of any narcotic by an occupant thereof, shall be forfeited to the State.”</blockquote>
</footnote>
<footnote label="2">
<p id="b140-8">Petitioner also presents the contention here that he was unconstitutionally deprived of the right to confront a witness against him, because, the State did not produce the informant to testify against him. This contention we consider absolutely devoid of merit.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Corley v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Corley v. United States"
type: case
citation: "556 U.S. 303 (2009)"
parallel_cite: "129 S. Ct. 1558; 173 L. Ed. 2d 443"
neutral_cite: 2009 U.S. LEXIS 2512
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-04-06
docket: 07-10441
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-04-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Corley v. United States
  varies_by_point: false
  scope_note: "Good law; the controlling modern statement of the federal McNabb-Mallory prompt-presentment rule as modified by 18 U.S.C. §3501. A federal-court rule (Rule 5(a)/§3501), not a constitutional rule binding the States."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145888/corley-v-united-states/"
  cluster_id: 145888
  opinion_id: 145888
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (cross-doctrine)"
related: ["[[McNabb v. United States]]", "[[Mallory v. United States]]", "[[Miranda v. Arizona]]", "[[Dickerson v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "confessions", "mcnabb-mallory", "prompt-presentment", "section-3501", "voluntariness"]
holding: "18 U.S.C. §3501 modified but did not supplant the McNabb-Mallory rule: a federal confession made before presentment and more than six hours after arrest must be suppressed if the presentment delay was unreasonable or unnecessary."
lake:
  record_id: Corley v. United States
  status: verified
  projected_at: 2026-07-06
---

# Corley v. United States

*556 U.S. 303 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Johnnie Corley was suspected of a bank robbery. Federal agents arrested him about 8 a.m. on an unrelated state warrant after he fled and assaulted an officer. The FBI held him at a local station, took him to a hospital for a minor cut, and then to the Philadelphia FBI office. Although the nearest magistrate judges' chambers were in the same building, the agents did not present Corley but questioned him, and about 9.5 hours after arrest he began an oral confession to the robbery, followed later by a written one. He moved to suppress the confessions under the McNabb-Mallory rule for unreasonable delay in presentment.

## Issue
Whether 18 U.S.C. §3501 abolished the McNabb-Mallory rule entirely, or whether §3501(c) merely creates a six-hour safe harbor — leaving McNabb-Mallory to exclude a federal confession made during an unreasonable presentment delay beyond that window.

## Rule
Section 3501 modified, but did not supplant, McNabb-Mallory. The Court restated the rule it preserved: "the rule known simply as *McNabb-Mallory* 'generally render[s] inadmissible confessions made during periods of detention that violat[e] the prompt presentment requirement of Rule 5(a).'" — 556 U.S. at 309 (quoting *United States v. Alvarez-Sanchez*, 511 U.S. 350, 354 (1994)). ^pin-309

"We hold that §3501 modified *McNabb-Mallory* without supplanting it. Under the rule as revised by §3501(c), a district court with a suppression claim must find whether the defendant confessed within six hours of arrest . . . . If the confession occurred before presentment and beyond six hours, however, the court must decide whether delaying that long was unreasonable or unnecessary under the *McNabb-Mallory* cases, and if it was, the confession is to be suppressed." — *Id.* at 322. ^pin-322

## Application
Corley's oral confession came roughly 9.5 hours after his arrest, before he was presented to a magistrate. Because that placed the statement potentially outside §3501(c)'s six-hour window, the courts below had to determine whether the confession should be treated as made within six hours and, if not, whether the additional delay was unreasonable or unnecessary under McNabb-Mallory — and to make the same inquiry as to the written confession. The Third Circuit had instead held that §3501 abrogated McNabb-Mallory altogether and so never made those findings; that was error.

## Conclusion
Section 3501 modified McNabb-Mallory without supplanting it. The judgment of the Court of Appeals was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]] to determine whether Corley's confessions fell within the six-hour safe harbor and, if not, whether the presentment delay was unreasonable or unnecessary.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Corley* is the controlling modern statement of the federal prompt-presentment rule, applying [[McNabb v. United States]] and [[Mallory v. United States]] as modified by 18 U.S.C. §3501. It is a **federal-court** evidentiary rule (Federal Rule of Criminal Procedure 5(a) / §3501), not a constitutional rule binding the States. It draws on [[Dickerson v. United States]] for the background that §3501 was Congress's response to [[Miranda v. Arizona]] and McNabb-Mallory.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*
- [[Miranda and Custodial Interrogation]] — *Related (cross-doctrine)*

## Sources
- *Corley v. United States*, 556 U.S. 303 (2009) — https://www.courtlistener.com/opinion/145888/corley-v-united-states/ — pinpoints: 309, 322.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e659a6f441a1265b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Corley v. United States"}, "payload": {"all": [{"cite": "556 U.S. 303", "page": "303", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "556"}, {"cite": "129 S. Ct. 1558", "page": "1558", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "129"}, {"cite": "173 L. Ed. 2d 443", "page": "443", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "173"}, {"cite": "2009 U.S. LEXIS 2512", "page": "2512", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2009"}], "display": "556 U.S. 303", "official": {"cite": "556 U.S. 303", "page": "303", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "556"}, "official_selection_present": true, "record_id": "Corley v. United States"}}
{"assertion_id": "4c54a50a54360c7a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-322", "record_id": "Corley v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-322", "pinpoint_status": "slip-only", "quote": "We hold that §3501 modified *McNabb-Mallory* without supplanting it. Under the rule as revised by §3501(c), a district court with a suppression claim must find whether the defendant confessed within six hours of arrest . . . . If the confession occurred before presentment and beyond six hours, however, the court must decide whether delaying that long was unreasonable or unnecessary under the *McNabb-Mallory* cases, and if it was, the confession is to be suppressed.", "quote_fidelity": "mismatch", "record_id": "Corley v. United States", "star_marker": null}}
{"assertion_id": "54af65a12957cb41", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-309", "record_id": "Corley v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-309", "pinpoint_status": "slip-only", "quote": "--- # Corley v. United States *556 U.S. 303 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Johnnie Corley was suspected of a bank robbery. Federal agents arrested him about 8 a.m. on an unrelated state warrant after he fled and assaulted an officer. The FBI held him at a local station, took him to a hospital for a minor cut, and then to the Philadelphia FBI office. Although the nearest magistrate judges' chambers were in the same building, the agents did not present Corley but questioned him, and about 9.5 hours after arrest he began an oral confession to the robbery, followed later by a written one. He moved to suppress the confessions under the McNabb-Mallory rule for unreasonable delay in presentment. ## Issue Whether 18 U.S.C. §3501 abolished the McNabb-Mallory rule entirely, or whether §3501(c) merely creates a six-hour safe harbor — leaving McNabb-Mallory to exclude a federal confession made during an unreasonable presentment delay beyond that window. ## Rule Section 3501 modified, but did not supplant, McNabb-Mallory. The Court restated the rule it preserved:", "quote_fidelity": "mismatch", "record_id": "Corley v. United States", "star_marker": null}}
{"assertion_id": "4ea3278e5e49dc07", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Corley v. United States"}, "payload": {"as_of_content": "2009-04-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Corley v. United States", "scope_note": "Good law; the controlling modern statement of the federal McNabb-Mallory prompt-presentment rule as modified by 18 U.S.C. §3501. A federal-court rule (Rule 5(a)/§3501), not a constitutional rule binding the States.", "varies_by_point": false}}
```

### lake record — Corley v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Corley v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Corley v. United States",
    "case_name_short": "Corley",
    "case_name_full": "Corley v. United States",
    "input_case_name": "Corley v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-04-06",
    "year": 2009,
    "docket": "07-10441",
    "cluster_id": 145888,
    "lead_opinion_id": 145888,
    "sibling_ids": [
      145888
    ],
    "absolute_url": "/opinion/145888/corley-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 303",
      "volume": "556",
      "reporter": "U.S.",
      "page": "303",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 1558",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1558",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 443",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 2512",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "2512",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 303",
        "volume": "556",
        "reporter": "U.S.",
        "page": "303",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 1558",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1558",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 443",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 2512",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "2512",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 303",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 303",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-309",
      "page": null,
      "quote": "--- # Corley v. United States *556 U.S. 303 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Johnnie Corley was suspected of a bank robbery. Federal agents arrested him about 8 a.m. on an unrelated state warrant after he fled and assaulted an officer. The FBI held him at a local station, took him to a hospital for a minor cut, and then to the Philadelphia FBI office. Although the nearest magistrate judges' chambers were in the same building, the agents did not present Corley but questioned him, and about 9.5 hours after arrest he began an oral confession to the robbery, followed later by a written one. He moved to suppress the confessions under the McNabb-Mallory rule for unreasonable delay in presentment. ## Issue Whether 18 U.S.C. \u00a73501 abolished the McNabb-Mallory rule entirely, or whether \u00a73501(c) merely creates a six-hour safe harbor \u2014 leaving McNabb-Mallory to exclude a federal confession made during an unreasonable presentment delay beyond that window. ## Rule Section 3501 modified, but did not supplant, McNabb-Mallory. The Court restated the rule it preserved:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-322",
      "page": null,
      "quote": "We hold that \u00a73501 modified *McNabb-Mallory* without supplanting it. Under the rule as revised by \u00a73501(c), a district court with a suppression claim must find whether the defendant confessed within six hours of arrest . . . . If the confession occurred before presentment and beyond six hours, however, the court must decide whether delaying that long was unreasonable or unnecessary under the *McNabb-Mallory* cases, and if it was, the confession is to be suppressed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-04-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Corley v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; the controlling modern statement of the federal McNabb-Mallory prompt-presentment rule as modified by 18 U.S.C. \u00a73501. A federal-court rule (Rule 5(a)/\u00a73501), not a constitutional rule binding the States.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pharmaceutical Care Management Ass'n v. Gerhart",
          "cluster_id": 4337608,
          "cite": [
            "852 F.3d 722",
            "63 Employee Benefits Cas. (BNA) 1085",
            "2017 WL 104467",
            "2017 U.S. App. LEXIS 476"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "MSPA Claims 1, LLC v. Infinity Auto Insurance Company",
          "cluster_id": 4252384,
          "cite": [
            "835 F.3d 1351",
            "2016 U.S. App. LEXIS 15984"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Doscher v. Sea Port Group Securities, LLC",
          "cluster_id": 4246233,
          "cite": [
            "832 F.3d 372",
            "2016 U.S. App. LEXIS 14767",
            "2016 WL 4245427"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Natural Resources Defense Council, Inc. v. Pritzker",
          "cluster_id": 4238897,
          "cite": [
            "828 F.3d 1125",
            "2016 D.A.R. 7241",
            "82 ERC (BNA) 1979",
            "2016 U.S. App. LEXIS 13021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marx v. General Revenue Corp.",
          "cluster_id": 821305,
          "cite": [
            "185 L. Ed. 2d 242",
            "133 S. Ct. 1166",
            "568 U.S. 371",
            "2013 U.S. LEXIS 1859",
            "81 U.S.L.W. 4135",
            "84 Fed. R. Serv. 3d 1486",
            "24 Fla. L. Weekly Fed. S 60"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
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
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Forest Grove School District v. T. A.",
          "cluster_id": 145855,
          "cite": [
            "174 L. Ed. 2d 168",
            "129 S. Ct. 2484",
            "557 U.S. 230",
            "2009 U.S. LEXIS 4645",
            "77 U.S.L.W. 4550",
            "21 Fla. L. Weekly Fed. S 983"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walter Shuker v. Smith & Nephew PLC",
          "cluster_id": 4473712,
          "cite": [
            "885 F.3d 760"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mary Jo C. v. New York State and Local Retirement System et ano.",
          "cluster_id": 816224,
          "cite": [
            "707 F.3d 144",
            "2013 WL 322879",
            "2013 U.S. App. LEXIS 2013"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthew Alexander v. Verizon Wireless Services, LL",
          "cluster_id": 4442643,
          "cite": [
            "875 F.3d 243"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bloch v. Frischholz",
          "cluster_id": 1345471,
          "cite": [
            "587 F.3d 771",
            "2009 U.S. App. LEXIS 24917",
            "2009 WL 3789996"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ward v. Chavez",
          "cluster_id": 799476,
          "cite": [
            "678 F.3d 1042",
            "2012 WL 1592171",
            "2012 U.S. App. LEXIS 9316"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jane Doe v. Mercy Catholic Medical Center",
          "cluster_id": 4373438,
          "cite": [
            "850 F.3d 545",
            "2017 WL 894455",
            "2017 U.S. App. LEXIS 4004",
            "101 Empl. Prac. Dec. (CCH) 45,757"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Latiolais v. Eagle, Incorporated",
          "cluster_id": 4729521,
          "cite": [
            "951 F.3d 286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Landstar Express America, Inc. v. Federal Maritime Commission",
          "cluster_id": 187384,
          "cite": [
            "569 F.3d 493",
            "386 U.S. App. D.C. 336",
            "2009 U.S. App. LEXIS 13940",
            "2009 WL 1812746"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glaser v. Wound Care Consultants, Inc.",
          "cluster_id": 1196972,
          "cite": [
            "570 F.3d 907",
            "2009 U.S. App. LEXIS 14394",
            "2009 WL 1885500"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guedes v. Bureau of Alcohol, Tobacco, Firearms",
          "cluster_id": 4605646,
          "cite": [
            "920 F.3d 1"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kawashima v. Holder",
          "cluster_id": 623145,
          "cite": [
            "182 L. Ed. 2d 1",
            "132 S. Ct. 1166",
            "565 U.S. 478",
            "2012 U.S. LEXIS 1084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Khadidja Issa v. Lancaster School District",
          "cluster_id": 4343616,
          "cite": [
            "847 F.3d 121",
            "2017 WL 393164",
            "2017 U.S. App. LEXIS 1595",
            "339 Educ. L. Rep. 630"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G.G. v. Salesforce.com, Inc.",
          "cluster_id": 9417992,
          "cite": [
            "76 F.4th 544"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sioux Honey Ass'n v. Hartford Fire Insurance",
          "cluster_id": 624415,
          "cite": [
            "672 F.3d 1041",
            "2012 WL 379626",
            "33 I.T.R.D. (BNA) 1929",
            "2012 U.S. App. LEXIS 2399"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barnes v. Belice (In Re Belice)",
          "cluster_id": 2195918,
          "cite": [
            "461 B.R. 564",
            "2011 WL 6942900"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barton v. Barr",
          "cluster_id": 4747781,
          "cite": [
            "590 U.S. 222",
            "140 S. Ct. 1442",
            "206 L. Ed. 2d 682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dane Gillis",
          "cluster_id": 4660754,
          "cite": [
            "938 F.3d 1181"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Trinity Rolando Cabezas-Montano",
          "cluster_id": 4722792,
          "cite": [
            "949 F.3d 567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rubin v. Islamic Republic of Iran",
          "cluster_id": 4469600,
          "cite": [
            "583 U.S. 202",
            "138 S. Ct. 816",
            "200 L. Ed. 2d 58",
            "2018 U.S. LEXIS 1376"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Lehman Bros. Mortgage-Backed Securities",
          "cluster_id": 216493,
          "cite": [
            "650 F.3d 167"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Clenney",
          "cluster_id": 184207,
          "cite": [
            "631 F.3d 658",
            "2011 U.S. App. LEXIS 2117",
            "2011 WL 322640"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Redlightning",
          "cluster_id": 177836,
          "cite": [
            "624 F.3d 1090",
            "2010 U.S. App. LEXIS 21957",
            "2010 WL 4158583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Corley v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145888) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDMyNTk4NDAwMDAwJnM9MjgwMzQwOCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145888%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145888)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01OCZzPTg0NDEyMjcmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145888%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145888)",
        "reviewed": 47,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 47,
        "triage_read": 0,
        "triage_snippet_classified": 47
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145888)",
    "indexed_citing_opinions": 458,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145888,
        "count": 458,
        "count_source": "search"
      }
    ],
    "citation_count": 914,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/corley-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MzY5MjQmcz0xMDAzOTI2NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145888%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145888,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 104603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 110077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 110079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 110258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 111043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 111487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 112310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 112585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 112670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 112706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 117863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 117887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 117955,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 118324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 118347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 136987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 145646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 287662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 307188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 350606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 411243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 435237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 577700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 604116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 733387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 779209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 1087948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145888,
        "cited_id": 1193367,
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
    "date_created": "2026-07-05T01:20:16Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:21:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:21:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T01:27:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:21:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Corley v. United States

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

                     CORLEY v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE THIRD CIRCUIT

    No. 07–10441.       Argued January 21, 2009—Decided April 6, 2009
McNabb v. United States, 318 U. S. 332, and Mallory v. United States,
 354 U. S. 449, “generally rende[r] inadmissible confessions made dur
 ing periods of detention that violat[e] the prompt presentment re
 quirement of [Federal Rule of Criminal Procedure] 5(a).” United
 States v. Alvarez-Sanchez, 511 U. S. 350, 354. Rule 5(a), in turn, pro
 vides that a “person making an arrest . . . must take the defendant
 without unnecessary delay before a magistrate judge . . . .” Congress
 enacted 18 U. S. C. §3501 in response to Miranda v. Arizona, 384
 U. S. 436, and some applications of the McNabb-Mallory rule. In an
 attempt to eliminate Miranda, §3501(a) provides that “a confession
 . . . shall be admissible in evidence if it is voluntarily given,” and
 §3501(b) lists several considerations for courts to address in assess
 ing voluntariness. Subsection (c), which focuses on McNabb-Mallory,
 provides that “a confession made . . . by . . . a defendant . . . , while
 . . . under arrest . . . , shall not be inadmissible solely because of delay
 in bringing such person before a magistrate judge . . . if such confes
 sion is found by the trial judge to have been made voluntarily and . . .
 within six hours [of arrest]”; it extends that time limit when further
 delay is “reasonable considering the means of transportation and the
 distance to . . . the nearest available [magistrate].”
     Petitioner Corley was arrested for assaulting a federal officer at
 about 8 a.m. Around 11:45 FBI agents took him to a Philadelphia
 hospital to treat a minor injury. At 3:30 p.m. he was taken from the
 hospital to the local FBI office and told that he was a suspect in a
 bank robbery. Though the office was in the same building as the
 nearest magistrate judges, the agents did not bring him before a
 magistrate judge, but questioned him, hoping for a confession. At
 5:27 p.m., some 9.5 hours after his arrest, Corley began an oral con
2                      CORLEY v. UNITED STATES

                                  Syllabus

    fession that he robbed the bank. He asked for a break at 6:30 and
    was held overnight. The interrogation resumed the next morning,
    ending with his signed written confession. He was finally presented
    to a Magistrate Judge at 1:30 p.m., 29.5 hours after his arrest, and
    charged with armed bank robbery and related charges. The District
    Court denied his motion to suppress his confessions under Rule 5(a)
    and McNabb-Mallory. It reasoned that the oral confession occurred
    within §3501(c)’s six-hour window because the time of Corley’s medi
    cal treatment should be excluded from the delay. It also found the
    written confession admissible, explaining there was no unreasonable
    delay under Rule 5(a) because Corley had requested the break. He
    was convicted of conspiracy and bank robbery. The Third Circuit af
    firmed. Relying on Circuit precedent to the effect that §3501 abro
    gated McNabb-Mallory and replaced it with a pure voluntariness
    test, it concluded that if a district court found a confession voluntary
    after considering the points listed in §3501(b), it would be admissible,
    even if the presentment delay was unreasonable.
Held: Section 3501 modified McNabb-Mallory but did not supplant it.
 Pp. 8–18.
    (a) The Government claims that because §3501(a) makes a confes
 sion “admissible” “if it is voluntarily given,” it entirely eliminates
 McNabb-Mallory with its bar to admitting even a voluntary confes
 sion if given during an unreasonable presentment delay. Corley ar
 gues that §3501(a) was only meant to overrule Miranda, and notes
 that only §3501(c) touches on McNabb-Mallory, making the rule in
 applicable to confessions given within six hours of an arrest. He has
 the better argument. Pp. 8–16.
      (1) The Government’s reading renders §3501(c) nonsensical and
 superfluous. If subsection (a) really meant that any voluntary con
 fession was admissible, then subsection (c) would add nothing; if a
 confession was “made voluntarily” it would be admissible, period, and
 never “inadmissible solely because of delay,” even a delay beyond six
 hours. The Government’s reading is thus at odds with the basic in
 terpretive canon that “ ‘[a] statute should be construed [to give effect]
 to all its provisions, so that no part will be inoperative or superfluous,
 void or insignificant.’ ” Hibbs v. Winn, 542 U. S. 88, 101. The Gov
 ernment claims that in providing that a confession “shall not be ad
 missible,” Congress meant that a confession “shall not be [involun
 tary].” Thus read, (c) would specify a bright-line rule applying (a) to
 cases of delay: it would tell courts that delay alone does not make a
 confession involuntary unless the delay exceeds six hours. But
 “ ‘Congress did not write the statute that way.’ ” Russello v. United
 States, 464 U. S. 16, 23. The terms “inadmissible” and “involuntary”
 are not synonymous. Congress used both in (c), and this Court
                   Cite as: 556 U. S. ____ (2009)                     3

                              Syllabus

“would not presume to ascribe this difference to a simple mistake in
draftsmanship.” Ibid. There is also every reason to believe that
Congress used the distinct terms deliberately, specifying two criteria
that must be satisfied to prevent a confession from being “inadmissi
ble solely because of delay”: the confession must be “[1] made volun
tarily and . . . [2] within six hours [of arrest].” Moreover, under the
McNabb-Mallory rule, “inadmissible” and “involuntary” mean differ
ent things. Corley’s position, in contrast, gives effect to both (c) and
(a), by reading (a) as overruling Miranda and (c) as qualifying
McNabb-Mallory.          The Government’s counterargument—that
Corley’s reading would also create a conflict, since (a) makes all vol
untary confessions admissible while (c) would leave some voluntary
confessions inadmissible—falls short. First, (a) is a broad directive
while (c) aims only at McNabb-Mallory, and “a more specific statute
[is] given precedence over a more general one.” Busic v. United
States, 446 U. S. 398, 406. Second, reading (a) to create a conflict
with (c) not only would make (c) superfluous, but would also create
conflicts with so many other Rules of Evidence that the subsection
cannot possibly be given its literal scope. Pp. 8–12.
     (2) The legislative history strongly favors Corley’s reading. The
Government points to nothing in this history supporting its contrary
view. Pp. 13–15.
     (3) The Government’s position would leave the Rule 5 present
ment requirement without teeth, for if there is no McNabb-Mallory
there is no apparent remedy for a presentment delay. The prompt
presentment requirement is not just an administrative nicety. It
dates back to the common law. Under Rule 5, presentment is the
point at which the judge must take several key steps to foreclose
Government overreaching: e.g., informing the defendant of the
charges against him and giving the defendant a chance to consult
with counsel. Without McNabb-Mallory, federal agents would be free
to question suspects for extended periods before bringing them out in
the open, even though “custodial police interrogation, by its very na
ture, isolates and pressures the individual,” Dickerson v. United
States, 530 U. S. 428, 435, inducing people to confess to crimes they
never committed. Pp. 15–16.
   (b) There is no merit to the Government’s fallback claim that even
if §3501 preserved a limited version of McNabb-Mallory, Congress cut
it out by enacting Federal Rule of Evidence 402, which provides that
“[a]ll relevant evidence is admissible, except as otherwise provided by
the Constitution of the United States, by Act of Congress, by these
rules, or by other rules prescribed by the Supreme Court . . . .” The
Advisory Committee’s Notes expressly identified McNabb-Mallory as
a statutorily authorized rule that would survive Rule 402, and the
4                    CORLEY v. UNITED STATES

                               Syllabus

    Government has previously conceded before this Court that Rule 402
    preserved McNabb-Mallory. Pp. 16–18.
500 F. 3d 210, vacated and remanded.

   SOUTER, J., delivered the opinion of the Court, in which STEVENS,
KENNEDY, GINSBURG, and BREYER, JJ., joined. ALITO, J., filed a dissent
ing opinion, in which ROBERTS, C. J., and SCALIA and THOMAS, JJ.,
joined.
                       Cite as: 556 U. S. ____ (2009)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                 No. 07–10441
                                  _________________


     JOHNNIE CORLEY, PETITIONER v. UNITED 

                  STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE THIRD CIRCUIT

                                [April 6, 2009]


  JUSTICE SOUTER delivered the opinion of the Court.
  The question here is whether Congress intended 18
U. S. C. §3501 to discard, or merely to narrow, the rule in
McNabb v. United States, 318 U. S. 332 (1943), and Mal
lory v. United States, 354 U. S. 449 (1957), under which an
arrested person’s confession is inadmissible if given after
an unreasonable delay in bringing him before a judge. We
hold that Congress meant to limit, not eliminate, McNabb-
Mallory.
                             I

                             A

   The common law obliged an arresting officer to bring his
prisoner before a magistrate as soon as he reasonably
could. See County of Riverside v. McLaughlin, 500 U. S.
44, 61–62 (1991) (SCALIA, J., dissenting). This “present
ment” requirement tended to prevent secret detention and
served to inform a suspect of the charges against him, and
it was the law in nearly every American State and the
National Government. See id., at 60–61; McNabb, supra,
at 342, and n. 7.
   McNabb v. United States raised the question of how to
2                CORLEY v. UNITED STATES

                      Opinion of the Court

enforce a number of federal statutes codifying the pre
sentment rule. 318 U. S., at 342 (citing, among others, 18
U. S. C. §595 (1940 ed.), which provided that “ ‘[i]t shall be
the duty of the marshal . . . who may arrest a person . . . to
take the defendant before the nearest . . . judicial officer
. . . for a hearing’ ”). There, federal agents flouted the
requirement by interrogating several murder suspects for
days before bringing them before a magistrate, and then
only after they had given the confessions that convicted
them. 318 U. S., at 334–338, 344–345.
    On the defendants’ motions to exclude the confessions
from evidence, we saw no need to reach any constitutional
issue. Instead we invoked the supervisory power to estab
lish and maintain “civilized standards of procedure and
evidence” in federal courts, id., at 340, which we exercised
for the sake of making good on the traditional obligation
embodied in the federal presentment legislation. We saw
both the statutes and the traditional rule as aimed not
only at checking the likelihood of resort to the third degree
but meant generally to “avoid all the evil implications of
secret interrogation of persons accused of crime.” Id., at
344. We acknowledged that “Congress ha[d] not explicitly
forbidden the use of evidence . . . procured” in derogation
of the presentment obligation, id., at 345, but we realized
that “permit[ting] such evidence to be made the basis of a
conviction in the federal courts would stultify the policy
which Congress ha[d] enacted into law,” ibid., and in the
exercise of supervisory authority we held confessions
inadmissible when obtained during unreasonable pre
sentment delay.
    Shortly after McNabb, the combined action of the Judi
cial Conference of the United States and Congress pro
duced Federal Rule of Criminal Procedure 5(a), which
pulled the several statutory presentment provisions to
gether in one place. See Mallory, supra, at 452 (describing
Rule 5(a) as “a compendious restatement, without sub
                 Cite as: 556 U. S. ____ (2009)           3

                     Opinion of the Court

stantive change, of several prior specific federal statutory
provisions”). As first enacted, the rule told “[a]n officer
making an arrest under a warrant issued upon a com
plaint or any person making an arrest without a warrant
[to] take the arrested person without unnecessary delay
before the nearest available commissioner or before any
other nearby officer empowered to commit persons
charged with offenses against the laws of the United
States.” Fed. Rule Crim. Proc. 5(a) (1946). The rule re
mains much the same today: “A person making an arrest
within the United States must take the defendant without
unnecessary delay before a magistrate judge . . . .” Fed.
Rule Crim. Proc. 5(a)(1)(A) (2007).
   A case for applying McNabb and Rule 5(a) together soon
arose in Upshaw v. United States, 335 U. S. 410 (1948).
Despite the Government’s confession of error, the D. C.
Circuit had thought McNabb’s exclusionary rule applied
only to involuntary confessions obtained by coercion dur
ing the period of delay, 335 U. S., at 411–412, and so held
the defendant’s voluntary confession admissible into evi
dence. This was error, and we reiterated the reasoning of
a few years earlier. “In the McNabb case we held that the
plain purpose of the requirement that prisoners should
promptly be taken before committing magistrates was to
check resort by officers to ‘secret interrogation of persons
accused of crime.’ ” Id., at 412 (quoting McNabb, supra, at
344). Upshaw consequently emphasized that even volun
tary confessions are inadmissible if given after an unrea
sonable delay in presentment. 335 U. S., at 413.
   We applied Rule 5(a) again in Mallory v. United States,
holding a confession given seven hours after arrest inad
missible for “unnecessary delay” in presenting the suspect
to a magistrate, where the police questioned the suspect
for hours “within the vicinity of numerous committing
magistrates.” 354 U. S., at 455. Again, we repeated the
reasons for the rule and explained, as we had before and
4                    CORLEY v. UNITED STATES

                          Opinion of the Court

have since, that delay for the purpose of interrogation is
the epitome of “unnecessary delay.” Id., at 455–456; see
also McLaughlin, 500 U. S., at 61 (SCALIA, J., dissenting)
(“It was clear” at common law “that the only element
bearing upon the reasonableness of delay was not such
circumstances as the pressing need to conduct further
investigation, but the arresting officer’s ability, once the
prisoner had been secured, to reach a magistrate”); Up
shaw, supra, at 414. Thus, the rule known simply as
McNabb-Mallory “generally render[s] inadmissible confes
sions made during periods of detention that violat[e] the
prompt presentment requirement of Rule 5(a).” United
States v. Alvarez-Sanchez, 511 U. S. 350, 354 (1994).
   There the law remained until 1968, when Congress
enacted 18 U. S. C. §3501 in response to Miranda v. Ari
zona, 384 U. S. 436 (1966), and to the application of
McNabb-Mallory in some federal courts. Subsections (a)
and (b) of §3501 were meant to eliminate Miranda.1 See
Dickerson v. United States, 530 U. S. 428, 435–437 (2000);
infra, at 13–14. Subsection (a) provides that “[i]n any
criminal prosecution brought by the United States . . . , a
confession . . . shall be admissible in evidence if it is volun
tarily given,” while subsection (b) lists several considera
tions for courts to address in assessing voluntariness.2
——————
   1 We rejected this attempt to overrule Miranda in Dickerson v. United

States, 530 U. S. 428 (2000).
   2 In full, subsections (a) and (b) provide:

   “(a) In any criminal prosecution brought by the United States or by
the District of Columbia, a confession, as defined in subsection (e)
hereof, shall be admissible in evidence if it is voluntarily given. Before
such confession is received in evidence, the trial judge shall, out of the
presence of the jury, determine any issue as to voluntariness. If the
trial judge determines that the confession was voluntarily made it shall
be admitted in evidence and the trial judge shall permit the jury to
hear relevant evidence on the issue of voluntariness and shall instruct
the jury to give such weight to the confession as the jury feels it de
serves under all the circumstances.
                    Cite as: 556 U. S. ____ (2009)                   5

                         Opinion of the Court

Subsection (c), which focused on McNabb-Mallory, see
infra, at 13–14, provides that in any federal prosecution,
“a confession made . . . by . . . a defendant therein, while
such person was under arrest . . . , shall not be inadmissi
ble solely because of delay in bringing such person before a
magistrate judge . . . if such confession is found by the
trial judge to have been made voluntarily . . . and if such
confession was made . . . within six hours [of arrest]”;
the six-hour time limit is extended when further delay
is “reasonable considering the means of transportation
and the distance to be traveled to the nearest available
[magistrate].”3
——————
   “(b) The trial judge in determining the issue of voluntariness shall
take into consideration all the circumstances surrounding the giving of
the confession, including (1) the time elapsing between arrest and
arraignment of the defendant making the confession, if it was made
after arrest and before arraignment, (2) whether such defendant knew
the nature of the offense with which he was charged or of which he was
suspected at the time of making the confession, (3) whether or not such
defendant was advised or knew that he was not required to make any
statement and that any such statement could be used against him, (4)
whether or not such defendant had been advised prior to questioning of
his right to the assistance of counsel; and (5) whether or not such
defendant was without the assistance of counsel when questioned and
when giving such confession.
   “The presence or absence of any of the above-mentioned factors to be
taken into consideration by the judge need not be conclusive on the
issue of voluntariness of the confession.”
   3 In full, subsection (c) provides:

   “In any criminal prosecution by the United States or by the District
of Columbia, a confession made or given by a person who is a defendant
therein, while such person was under arrest or other detention in the
custody of any law-enforcement officer or law-enforcement agency, shall
not be inadmissible solely because of delay in bringing such person
before a magistrate judge or other officer empowered to commit persons
charged with offenses against the laws of the United States or of the
District of Columbia if such confession is found by the trial judge to
have been made voluntarily and if the weight to be given the confession
is left to the jury and if such confession was made or given by such
person within six hours immediately following his arrest or other
6                   CORLEY v. UNITED STATES

                         Opinion of the Court

  The issue in this case is whether Congress intended
§3501(a) to sweep McNabb-Mallory’s exclusionary rule
aside entirely, or merely meant §3501(c) to provide immu
nization to voluntary confessions given within six hours of
a suspect’s arrest.
                              B
  Petitioner Johnnie Corley was suspected of robbing a
bank in Norristown, Pennsylvania. After federal agents
learned that Corley was subject to arrest on an unrelated
local matter, some federal and state officers went together
to execute the state warrant on September 17, 2003, and
found him just as he was pulling out of a driveway in his
car. Corley nearly ran over one officer, then jumped out of
the car, pushed the officer down, and ran. The agents
gave chase and caught and arrested him for assaulting a
federal officer. The arrest occurred about 8 a.m. 500 F. 3d
210, 212 (CA3 2007).
  FBI agents first kept Corley at a local police station
while they questioned residents near the place he was
captured. Around 11:45 a.m. they took him to a Philadel
phia hospital to treat a minor cut on his hand that he got
during the chase. At 3:30 p.m. the agents took him from
the hospital to the Philadelphia FBI office and told him
that he was a suspect in the Norristown bank robbery.
Though the office was in the same building as the cham
bers of the nearest magistrate judges, the agents did not
bring Corley before a magistrate, but questioned him
instead, in hopes of getting a confession. App. 68–69, 83,
138–139.
——————
detention: Provided, That the time limitation contained in this subsec
tion shall not apply in any case in which the delay in bringing such
person before such magistrate judge or other officer beyond such six
hour period is found by the trial judge to be reasonable considering the
means of transportation and the distance to be traveled to the nearest
available such magistrate judge or other officer.”
                 Cite as: 556 U. S. ____ (2009)          7

                     Opinion of the Court

   The agents’ repeated arguments sold Corley on the
benefits of cooperating with the Government, and he
signed a form waiving his Miranda rights. At 5:27 p.m.,
some 9.5 hours after his arrest, Corley began an oral
confession that he robbed the bank, id., at 62, and spoke
on in this vein until about 6:30, when agents asked him to
put it all in writing. Corley said he was tired and wanted
a break, so the agents decided to hold him overnight and
take the written statement the next morning. At 10:30
a.m. on September 18 they began the interrogation again,
which ended when Corley signed a written confession. He
was finally presented to a magistrate at 1:30 p.m. that
day, 29.5 hours after his arrest. 500 F. 3d, at 212.
   Corley was charged with armed bank robbery, 18
U. S. C. §2113(a), (d), conspiracy to commit armed bank
robbery, §371, and using a firearm in furtherance of a
crime of violence, §924(c). When he moved to suppress his
oral and written confessions under Rule 5(a) and McNabb-
Mallory, the District Court denied the motion, with the
explanation that the time Corley was receiving medical
treatment should be excluded from the delay, and that the
oral confession was thus given within the six-hour window
of §3501(c). Crim. No. 03–775 (ED Pa., May 10, 2004),
App. 97. The District Court also held Corley’s written
confession admissible, reasoning that “a break from inter
rogation requested by an arrestee who has already begun
his confession does not constitute unreasonable delay
under Rule 5(a).” Id., at 97–98. Corley was convicted of
conspiracy and armed robbery but acquitted of using a
firearm during a crime of violence. 500 F. 3d, at 212–213.
   A divided panel of the Court of Appeals for the Third
Circuit affirmed the conviction, though its rationale for
rejecting Corley’s Rule 5(a) argument was different from
the District Court’s. The panel majority considered itself
bound by Circuit precedent to the effect that §3501 en
tirely abrogated the McNabb-Mallory rule and replaced it
8                   CORLEY v. UNITED STATES

                          Opinion of the Court

with a pure voluntariness test. See 500 F. 3d, at 212
(citing Government of the Virgin Islands v. Gereau, 502
F. 2d 914 (CA3 1974)). As the majority saw it, if a district
court found a confession voluntary after considering the
points listed in §3501(b), it would be admissible, regard
less of whether delay in presentment was unnecessary or
unreasonable. 500 F. 3d, at 217. Judge Sloviter read
Gereau differently and dissented with an opinion that
“§3501 does not displace Rule 5(a)” or abrogate McNabb-
Mallory for presentment delays beyond six hours. 500
F. 3d, at 236.
   We granted certiorari to resolve a division in the Circuit
Courts on the reach of §3501. 554 U. S. ___ (2008). Com
pare United States v. Glover, 104 F. 3d 1570, 1583 (CA10
1997) (§3501 entirely supplanted McNabb-Mallory);
United States v. Christopher, 956 F. 2d 536, 538–539 (CA6
1991) (same), with United States v. Mansoori, 304 F. 3d
635, 660 (CA7 2002) (§3501 limited the McNabb-Mallory
rule to periods more than six hours after arrest); United
States v. Perez, 733 F. 2d 1026, 1031–1032 (CA2 1984)
(same).4 We now vacate and remand.
                              II
  The Government’s argument focuses on §3501(a), which
provides that any confession “shall be admissible in evi
dence” in federal court “if it is voluntarily given.” To the
Government, subsection (a) means that once a district
court looks to the considerations in §3501(b) and finds a
confession voluntary, in it comes; (a) entirely eliminates
McNabb-Mallory with its bar to admitting even a volun
tary confession if given during an unreasonable delay in
presentment.
  Corley argues that §3501(a) was meant to overrule
——————
  4 We granted certiorari to resolve this question once before, in United

States v. Alvarez-Sanchez, 511 U. S. 350 (1994), but ultimately resolved
that case on a different ground, id., at 355–360.
                     Cite as: 556 U. S. ____ (2009)                   9

                         Opinion of the Court

Miranda and nothing more, with no effect on McNabb-
Mallory, which §3501 touches only in subsection (c). By
providing that a confession “shall not be inadmissible
solely because of delay” in presentment if “made voluntar
ily and . . . within six hours [of arrest],” subsection (c)
leaves McNabb-Mallory inapplicable to confessions given
within the six hours, but when a confession comes even
later, the exclusionary rule applies and courts have to see
whether the delay was unnecessary or unreasonable.
   Corley has the better argument.
                                 A
  The fundamental problem with the Government’s read
ing of §3501 is that it renders §3501(c) nonsensical and
superfluous. Subsection (c) provides that a confession
“shall not be inadmissible solely because of delay” in pre
sentment if the confession is “made voluntarily and . . .
within six hours [of arrest].” If (a) really meant that any
voluntary confession was admissible, as the Government
contends, then (c) would add nothing; if a confession was
“made voluntarily” it would be admissible, period, and
never “inadmissible solely because of delay,” no matter
whether the delay went beyond six hours. There is no way
out of this, and the Government concedes it. Tr. of Oral
Arg. 33 (“Congress never needed (c); (c) in the [G]overn
ment’s view was always superfluous”).
  The Government’s reading is thus at odds with one of
the most basic interpretive canons, that “ ‘[a] statute
should be construed so that effect is given to all its provi
sions, so that no part will be inoperative or superfluous,
void or insignificant . . . .’ ” Hibbs v. Winn, 542 U. S. 88,
101 (2004) (quoting 2A N. Singer, Statutes and Statutory
Construction §46.06, pp.181–186 (rev. 6th ed. 2000)).5 The
——————
  5 The dissent says that the antisuperfluousness canon has no place

here because “there is nothing ambiguous about the language of
§3501(a).” Post, at 2 (opinion of ALITO, J.). But this response violates
10                   CORLEY v. UNITED STATES

                           Opinion of the Court

Government attempts to mitigate its problem by rewriting
(c) into a clarifying, if not strictly necessary, provision:
although Congress wrote that a confession “shall not be
inadmissible solely because of delay” if the confession is
“made voluntarily and . . . within six hours [of arrest],” the
Government tells us that Congress actually meant that a
confession “shall not be [involuntary] solely because of
delay” if the confession is “[otherwise voluntary] and . . .
[made] within six hours [of arrest].” Thus rewritten, (c)
would coexist peacefully (albeit inelegantly) with (a), with
(c) simply specifying a bright-line rule applying (a) to
cases of delay: it would tell courts that delay alone does
not make a confession involuntary unless the delay ex
ceeds six hours.
    To this proposal, “ ‘[t]he short answer is that Congress
did not write the statute that way.’ ” Russello v. United
States, 464 U. S. 16, 23 (1983) (quoting United States v.
Naftalin, 441 U. S. 768, 773 (1979)). The Government
may say that we can sensibly read “inadmissible” as “in
voluntary” because the words are “virtually synonymous
. . . in this statutory context,” Brief for United States 23,
but this is simply not so. To begin with, Congress used

——————
“the cardinal rule that a statute is to be read as a whole,” King v. St.
Vincent’s Hospital, 502 U. S. 215, 221 (1991). Subsection 3501(a) seems
clear only if one ignores the absurd results of a literal reading, infra, at
11–12, and only until one reads §3501(c) and recognizes that if (a)
means what it literally says, (c) serves no purpose. Even the dissent
concedes that when (a) and (c) are read together, “[t]here is simply no
perfect solution to the problem before us.” Post, at 4. Thus, the dis
sent’s point that subsection (a) seems clear when read in isolation
proves nothing, for “[t]he meaning—or ambiguity—of certain words or
phrases may only become evident when placed in context.” FDA v.
Brown & Williamson Tobacco Corp., 529 U. S. 120, 132 (2000). When
subsection (a) is read in context, there is no avoiding the question,
“What could Congress have been getting at with both (a) and (c)?” The
better answer is that Congress meant to do just what Members explic
itly said in the legislative record. See infra, at 13–15.
                  Cite as: 556 U. S. ____ (2009)            11

                      Opinion of the Court

both terms in (c) itself, and “[w]e would not presume to
ascribe this difference to a simple mistake in draftsman
ship.” Russello, supra, at 23. And there is, in fact, every
reason to believe that Congress used the distinct terms
very deliberately. Subsection (c) specifies two criteria that
must be satisfied to prevent a confession from being “in
admissible solely because of delay”: the confession must be
“[1] made voluntarily and . . . [2] within six hours [of
arrest].” Because voluntariness is thus only one of several
criteria for admissibility under (c), “involuntary” and
“inadmissible” plainly cannot be synonymous. What is
more, the Government’s argument ignores the fact that
under the McNabb-Mallory rule, which we presume Con
gress was aware of, Cannon v. University of Chicago, 441
U. S. 677, 699 (1979), “inadmissible” and “involuntary”
mean different things. As we explained before and as the
Government concedes, McNabb-Mallory makes even vol
untary confessions inadmissible if given after an unrea
sonable delay in presentment, Upshaw, 335 U. S., at 413;
Tr. of Oral Arg. 33 (“[I]t was well understood that
McNabb-Mallory . . . excluded totally voluntary confes
sions”). So we cannot accept the Government’s attempt to
confuse the critically distinct terms “involuntary” and
“inadmissible” by rewriting (c) into a bright-line rule doing
nothing more than applying (a).
  Corley’s position, in contrast, gives effect to both (c) and
(a), by reading (a) as overruling Miranda and (c) as quali
fying McNabb-Mallory. The Government answers, how
ever, that accepting Corley’s argument would result in a
different problem: it would create a conflict between (c)
and (a), since (a) provides that all voluntary confessions
are admissible while Corley’s reading of (c) leaves some
voluntary confessions inadmissible. But the Government’s
counterargument falls short for two reasons. First, even if
(a) is read to be at odds with (c), the conflict is resolved by
recognizing that (a) is a broad directive while (c) aims only
12                  CORLEY v. UNITED STATES

                         Opinion of the Court

at McNabb-Mallory, and “a more specific statute will be
given precedence over a more general one . . . .” Busic v.
United States, 446 U. S. 398, 406 (1980). Second, and
more fundamentally, (a) cannot prudently be read to
create a conflict with (c), not only because it would make
(c) superfluous, as explained, but simply because reading
(a) that way would create conflicts with so many other
rules that the subsection cannot possibly be given its
literal scope. Subsection (a) provides that “[i]n any crimi
nal prosecution brought by the United States . . . , a con
fession . . . shall be admissible in evidence if it is voluntar
ily given,” and §3501(e) defines “confession” as “any
confession of guilt of any criminal offense or any self
incriminating statement made or given orally or in writ
ing.” Thus, if the Government seriously urged a literal
reading, (a) would mean that “in any criminal prosecution
brought by the United States . . . , [‘any self-incriminating
statement’ with respect to ‘any criminal offense’] . . . shall
be admissible in evidence if it is voluntarily given.” Thus
would many a Rule of Evidence be overridden in case after
case: a defendant’s self-incriminating statement to his
lawyer would be admissible despite his insistence on
attorney-client privilege; a fourth-hand hearsay statement
the defendant allegedly made would come in; and a defen
dant’s confession to an entirely unrelated crime committed
years earlier would be admissible without more. These
are some of the absurdities of literalism that show that
Congress could not have been writing in a literalistic
frame of mind.6
——————
   6 The dissent seeks to avoid these absurd results by claiming that

“§3501(a) does not supersede ordinary evidence Rules,” post, at 10, but
its only argument for this conclusion is that “there is no reason to
suppose that Congress meant any such thing,” post, at 9. The dissent is
certainly correct that there is no reason to suppose that Congress
meant any such thing; that is what our reductio ad absurdum shows.
But that leaves the dissent saying, “§3501(a) must be read literally”
                      Cite as: 556 U. S. ____ (2009)                    13

                          Opinion of the Court

                               B
  As it turns out, there is more than reductio ad absur
dum and the antisuperfluousness canon to confirm that
subsection (a) leaves McNabb-Mallory alone, for that is
what legislative history says. In fact, the Government
concedes that subsections (a) and (b) were aimed at
Miranda, while subsection (c) was meant to modify the
presentment exclusionary rule. Tr. of Oral Arg. 38 (“I will
concede to you . . . that section (a) was considered to over
rule Miranda, and subsection (c) was addressed to
McNabb-Mallory”). The concession is unavoidable. The
Senate, where §3501 originated, split the provision into
two parts: Division 1 contained subsections (a) and (b),
and Division 2 contained subsection (c). 114 Cong. Rec.
14171 (1968). In the debate on the Senate floor immedi
ately before voting on these proposals, several Senators,
including the section’s prime sponsor, Senator McClellan,
explained that Division 1 “has to do with the Miranda
decision,” while Division 2 related to Mallory. 114 Cong.
Rec. 14171–14172. This distinct intent was confirmed by
the separate Senate votes adopting the two measures,
Division 1 by 55 to 29 and Division 2 by 58 to 26, id., at
14171–14172, 14174–14175; if (a) did abrogate McNabb-
Mallory, as the Government claims, then voting for Divi
sion 2 would have been entirely superfluous, for the Divi
sion 1 vote would already have done the job. That aside, a
sponsor’s statement to the full Senate carries considerable
weight, and Senator McClellan’s explanation that Division
1 was specifically addressed to Miranda confirms that (a)
and (b) were never meant to reach far enough to abrogate
——————
(rendering §3501(c) superfluous), “but not too literally” (so that it would
override other Rules of Evidence). The dissent cannot have it both
ways. If it means to profess literalism it will have to take the absurdity
that literalism brings with it; “credo quia absurdum” (as Tertullian
may have said). If it will not take the absurd, then its literalism is no
alternative to our reading of the statute.
14                  CORLEY v. UNITED STATES

                          Opinion of the Court

other background evidentiary rules including McNabb-
Mallory.
   Further legislative history not only drives that point
home, but conclusively shows an intent that subsection (c)
limit McNabb-Mallory, not replace it. In its original draft,
subsection (c) would indeed have done away with McNabb-
Mallory completely, for the bill as first written would have
provided that “[i]n any criminal prosecution by the United
States . . . , a confession made or given by a person who is
a defendant therein . . . shall not be inadmissible solely
because of delay in bringing such person before a [magis
trate] if such confession is . . . made voluntarily.” S. 917,
90th Cong., 2d Sess., 44–45 (1968) (as reported by Senate
Committee on the Judiciary); 114 Cong. Rec. 14172. The
provision so conceived was resisted, however, by a number
of Senators worried about allowing indefinite presentment
delays. See, e.g., id., at 11740, 13990 (Sen. Tydings) (the
provision would “permit Federal criminal suspects to be
questioned indefinitely before they are presented to a
committing magistrate”); id., at 12290 (Sen. Fong) (the
provision “would open the doors to such practices as hold
ing suspects incommunicado for an indefinite period”).
After Senator Tydings proposed striking (c) from the bill
altogether, id., at 13651 (Amendment No. 788), Senator
Scott introduced the compromise of qualifying (c) with the
words: “ ‘and if such confession was made or given by such
person within six hours following his arrest or other de
tention.’ ” Id., at 14184–14185 (Amendment No. 805).7
The amendment was intended to confine McNabb-Mallory
to excluding only confessions given after more than six
hours of delay, see 114 Cong. Rec. 14184 (remarks of Sen.
Scott) (“My amendment provides that the period during
——————
  7 The proviso at the end of (c) relating to reasonable delays caused by

the means of transportation and distance to be traveled came later by
separate amendment. 114 Cong. Rec. 14787.
                 Cite as: 556 U. S. ____ (2009)           15

                     Opinion of the Court

which confessions may be received . . . shall in no case
exceed 6 hours”), and it was explicitly modeled on the
provision Congress had passed just months earlier to
govern presentment practice in the District of Columbia,
Title III of An Act Relating to Crime and Criminal Proce
dure in the District of Columbia (D. C. Crime Act),
§301(b), 81 Stat. 735–736, see, e.g., 114 Cong. Rec. 14184
(remarks of Sen. Scott) (“My amendment is an attempt to
conform, as nearly as practicable, to Title III of [the D. C.
Crime Act]”). By the terms of that Act, “[a]ny statement,
admission, or confession made by an arrested person
within three hours immediately following his arrest shall
not be excluded from evidence in the courts of the District
of Columbia solely because of delay in presentment.”
§301(b), 81 Stat. 735–736. Given the clear intent that
Title III modify but not eliminate McNabb-Mallory in the
District of Columbia, see, e.g., S. Rep. No. 912, 90th Cong.,
1st Sess., 17–18 (1967), using it as a model plainly shows
how Congress meant as much but no more in §3501(c).
  In sum, the legislative history strongly favors Corley’s
reading. The Government points to nothing in this history
supporting its view that (c) created a bright-line rule for
applying (a) in cases with a presentment issue.
                              C
   It also counts heavily against the position of the United
States that it would leave the Rule 5 presentment re
quirement without any teeth, for as the Government again
is forced to admit, if there is no McNabb-Mallory there is
no apparent remedy for delay in presentment. Tr. of Oral
Arg. 25. One might not care if the prompt presentment
requirement were just some administrative nicety, but in
fact the rule has always mattered in very practical ways
and still does. As we said, it stretches back to the common
law, when it was “one of the most important” protections
“against unlawful arrest.” McLaughlin, 500 U. S., at 60–
16                CORLEY v. UNITED STATES

                      Opinion of the Court

61 (SCALIA, J., dissenting). Today presentment is the
point at which the judge is required to take several key
steps to foreclose Government overreaching: informing the
defendant of the charges against him, his right to remain
silent, his right to counsel, the availability of bail, and any
right to a preliminary hearing; giving the defendant a
chance to consult with counsel; and deciding between
detention or release. Fed. Rule Crim. Proc. 5(d); see also
Rule 58(b)(2).
   In a world without McNabb-Mallory, federal agents
would be free to question suspects for extended periods
before bringing them out in the open, and we have always
known what custodial secrecy leads to. See McNabb, 318
U. S. 332. No one with any smattering of the history of
20th-century dictatorships needs a lecture on the subject,
and we understand the need even within our own system
to take care against going too far. “[C]ustodial police
interrogation, by its very nature, isolates and pressures
the individual,” Dickerson, 530 U. S., at 435, and there is
mounting empirical evidence that these pressures can
induce a frighteningly high percentage of people to confess
to crimes they never committed, see, e.g., Drizin & Leo,
The Problem of False Confessions in the Post-DNA World,
82 N. C. L. Rev. 891, 906–907 (2004).
   Justice Frankfurter’s point in McNabb is as fresh as
ever: “The history of liberty has largely been the history of
observance of procedural safeguards.” 318 U. S., at 347.
McNabb-Mallory is one of them, and neither the text nor
the history of §3501 makes out a case that Congress
meant to do away with it.
                           III
  The Government’s fallback claim is that even if §3501
preserved a limited version of McNabb-Mallory, Congress
cut out the rule altogether by enacting Federal Rule of
Evidence 402 in 1975. Act of Jan. 2, Pub. L. 93–595, 88
                  Cite as: 556 U. S. ____ (2009)           17

                      Opinion of the Court

Stat. 1926. So far as it might matter here, that rule pro
vides that “[a]ll relevant evidence is admissible, except as
otherwise provided by the Constitution of the United
States, by Act of Congress, by these rules, or by other
rules prescribed by the Supreme Court pursuant to statu
tory authority.” The Government says that McNabb-
Mallory excludes relevant evidence in a way not “other
wise provided by” any of these four authorities, and so has
fallen to the scythe.
   The Government never raised this argument in the
Third Circuit or the District Court, which would justify
refusing to consider it here, but in any event it has no
merit. The Advisory Committee’s Notes on Rule 402,
which were before Congress when it enacted the Rules of
Evidence and which we have relied on in the past to inter
pret the rules, Tome v. United States, 513 U. S. 150, 160
(1995) (plurality opinion), expressly identified McNabb-
Mallory as a statutorily authorized rule that would sur
vive Rule 402: “The Rules of Civil and Criminal Procedure
in some instances require the exclusion of relevant evi
dence. For example, . . . the effective enforcement of . . .
Rule 5(a) . . . is held to require the exclusion of statements
elicited during detention in violation thereof.” 28 U. S. C.
App., pp. 325–326 (citing Mallory, 354 U. S. 449, and 18
U. S. C. §3501(c)); see also Mallory, supra, at 451 (“Th[is]
case calls for a proper application of Rule 5(a) of the Fed
eral Rules of Criminal Procedure . . .”). Indeed, the Gov
ernment has previously conceded before this Court that
Rule 402 preserved McNabb-Mallory. Brief for United
States in United States v. Payner, O. T. 1979, No. 78–
1729, p. 32, and n. 13 (1979) (saying that Rule 402 “left to
the courts . . . questions concerning the propriety of ex
cluding relevant evidence as a method of implementing
the Constitution, a federal statute, or a statutorily author
ized rule,” and citing McNabb-Mallory as an example).
The Government was right the first time, and it would be
18               CORLEY v. UNITED STATES

                     Opinion of the Court

bizarre to hold that Congress adopted Rule 402 with a
purpose exactly opposite to what the Advisory Committee
Notes said the rule would do.
                              IV
   We hold that §3501 modified McNabb-Mallory without
supplanting it. Under the rule as revised by §3501(c), a
district court with a suppression claim must find whether
the defendant confessed within six hours of arrest (unless
a longer delay was “reasonable considering the means of
transportation and the distance to be traveled to the near
est available [magistrate]”). If the confession came within
that period, it is admissible, subject to the other Rules of
Evidence, so long as it was “made voluntarily and . . . the
weight to be given [it] is left to the jury.” Ibid. If the
confession occurred before presentment and beyond six
hours, however, the court must decide whether delaying
that long was unreasonable or unnecessary under the
McNabb-Mallory cases, and if it was, the confession is to
be suppressed.
   In this case, the Third Circuit did not apply this rule
and in consequence never conclusively determined
whether Corley’s oral confession “should be treated as
having been made within six hours of arrest,” as the Dis
trict Court held. 500 F. 3d, at 220, n. 7. Nor did the Cir
cuit consider the justifiability of any delay beyond six
hours if the oral confession should be treated as given
outside the six-hour window; and it did not make this
enquiry with respect to Corley’s written confession. We
therefore vacate the judgment of the Court of Appeals and
remand the case for consideration of those issues in the
first instance, consistent with this opinion.

                                            It is so ordered.
                      Cite as: 556 U. S. ____ (2009)         1

                           ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                               _________________

                              No. 07–10441
                               _________________


     JOHNNIE CORLEY, PETITIONER v. UNITED 

                  STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE THIRD CIRCUIT

                              [April 6, 2009]


   JUSTICE ALITO, with whom THE CHIEF JUSTICE, JUSTICE
SCALIA, and JUSTICE THOMAS join, dissenting.
   Section 3501(a) of Title 18, United States Code, directly
and unequivocally answers the question presented in this
case. After petitioner was arrested by federal agents, he
twice waived his Miranda1 rights and voluntarily con
fessed, first orally and later in writing, that he had par
ticipated in an armed bank robbery. He was then taken
before a Magistrate Judge for an initial appearance. The
question that we must decide is whether this voluntary
confession may be suppressed on the ground that there
was unnecessary delay in bringing petitioner before the
Magistrate Judge. Unless the unambiguous language of
§3501(a) is ignored, petitioner’s confession may not be
suppressed.
                               I
  Section 3501(a) states: “In any criminal prosecution
brought by the United States . . ., a confession . . . shall be
admissible in evidence if it is voluntarily given.”
  Applying “settled principles of statutory construction,”
“we must first determine whether the statutory text is
plain and unambiguous,” and “[i]f it is, we must apply the

——————
 1 See   Miranda v. Arizona, 384 U. S. 436 (1966).
2                  CORLEY v. UNITED STATES

                        ALITO, J., dissenting

statute according to its terms.” Carcieri v. Salazar, 555
U. S. ___, ___ (2009) (slip op., at 7). Here, there is nothing
ambiguous about the language of §3501(a), and the Court
does not claim otherwise. Although we normally presume
that Congress “means in a statute what it says there,”
Connecticut Nat. Bank v. Germain, 503 U. S. 249, 253–254
(1992), the Court today concludes that §3501(a) does not
mean what it says and that a voluntary confession may be
suppressed under the McNabb-Mallory rule.2 This super
visory rule, which requires the suppression of a confession
where there was unnecessary delay in bringing a federal
criminal defendant before a judicial officer after arrest,
was announced long before 18 U. S. C. §3501(a) was
adopted. According to the Court, this rule survived the
enactment of §3501(a) because Congress adopted that
provision for the sole purpose of abrogating Miranda and
apparently never realized that the provision’s broad lan
guage would also do away with the McNabb-Mallory rule.
I disagree with the Court’s analysis and therefore respect
fully dissent.
                             II 

                             A

  The Court’s first and most substantial argument in
vokes “the antisuperfluousness canon,” ante, at 12, under
which a statute should be read, if possible, so that all of its
provisions are given effect and none is superfluous. Ante,
at 9–12. Section 3501(c) provides that a voluntary confes
sion “shall not be inadmissible solely because of the delay”
in bringing the defendant before a judicial officer if the
defendant is brought before a judicial officer within six
hours of arrest. If §3501(a) means that a voluntary con
fession may never be excluded due to delay in bringing the

——————
 2 See McNabb v. United States, 318 U. S. 332 (1943), and Mallory v.

United States, 354 U. S. 449 (1957).
                 Cite as: 556 U. S. ____ (2009)           3

                     ALITO, J., dissenting

defendant before a judicial officer, the Court reasons, then
§3501(c), which provides a safe harbor for a subset of
voluntary confessions (those made in cases in which the
initial appearance occurs within six hours of arrest), is
superfluous.
   Canons of interpretation “are quite often useful in close
cases, or when statutory language is ambiguous. But we
have observed before that such ‘interpretative canon[s are]
not a license for the judiciary to rewrite language enacted
by the legislature.’ ” United States v. Monsanto, 491 U. S.
600, 611 (1989) (quoting United States v. Albertini, 472
U. S. 675, 680 (1985)). Like other canons, the antisuper
fluousness canon is merely an interpretive aid, not an
absolute rule. See Connecticut Nat. Bank, 503 U. S., at
254 (“When the words of a statute are unambiguous, then,
this first canon is also the last: ‘judicial inquiry is com
plete’ ”). There are times when Congress enacts provisions
that are superfluous, and this may be such an instance.
Cf. id., at 253 (noting that “[r]edundancies across statutes
are not unusual events in drafting”); Gutierrez de Martinez
v. Lamagno, 515 U. S. 417, 445–446 (1995) (SOUTER, J.,
dissenting) (noting that, although Congress “indulged in a
little redundancy,” the “inelegance may be forgiven” be
cause “Congress could sensibly have seen some practical
value in the redundancy”).
   Moreover, any superfluity created by giving subsection
(a) its plain meaning may be minimized by interpreting
subsection (c) to apply to confessions that are otherwise
voluntary.     The Government contends that §3501(c),
though inartfully drafted, is not superfluous because what
the provision means is that a confession is admissible if it
is given within six hours of arrest and it is otherwise vol
untary—that is, if there is no basis other than prepre
sentment delay for concluding that the confession was
coerced. Read in this way, §3501(c) is not superfluous.
   The Court rejects this argument on the ground that
4                 CORLEY v. UNITED STATES

                      ALITO, J., dissenting

“ ‘Congress did not write the statute that way,’ ” ante, at
10, and thus, in order to adhere to a narrow reading of
§3501(c), the Court entirely disregards the unambiguous
language of §3501(a). Although §3501(a) says that a
confession is admissible if it is “voluntarily given,” the
Court reads that provision to mean that a voluntary con
fession may not be excluded on the ground that the confes
sion was obtained in violation of Miranda. To this read
ing, the short answer is that Congress really did not write
the statute that way.
   As is true with most of the statutory interpretation
questions that come before this Court, the question in this
case is not like a jigsaw puzzle. There is simply no perfect
solution to the problem before us.
   Instead, we must choose between two imperfect solu
tions. The first (the one adopted by the Court) entirely
disregards the clear and simple language of §3501(a), rests
on the proposition that Congress did not understand the
plain import of the language it used in subsection (a), but
adheres to a strictly literal interpretation of §3501(c). The
second option respects the clear language of subsection (a),
but either accepts some statutory surplusage or interprets
§3501(c)’s reference to a voluntary confession to mean an
otherwise voluntary confession. To my mind, the latter
choice is far preferable.
                              B
  In addition to the antisuperfluousness canon, the Court
relies on the canon that favors a specific statutory provi
sion over a conflicting provision cast in more general
terms, ante, at 11, but that canon is inapplicable here. For
one thing, §3501(a) is quite specific; it specifically provides
that if a confession is voluntary, it is admissible. More
important, there is no other provision, specific or general,
that conflicts with §3501(a). See National Cable & Tele
communications Assn., Inc. v. Gulf Power Co., 534 U. S.
                 Cite as: 556 U. S. ____ (2009)           5

                     ALITO, J., dissenting

327, 335–336 (2002) (“It is true that specific statutory
language should control more general language when there
is a conflict between the two. Here, however, there is no
conflict” (emphasis added)). Subsection (c) is not conflict
ing because it does not authorize the suppression of any
voluntary confession. What the Court identifies is not a
conflict between two statutory provisions but a conflict
between the express language of one provision (§3501(a))
and the “negative implication” that the Court draws from
another (§3501(c)). United States v. Alvarez-Sanchez, 511
U. S. 350, 355 (1994). Because §3501(c) precludes the
suppression of a voluntary confession based solely on a
delay of less than six hours, the Court infers that Con
gress must have contemplated that a voluntary confession
could be suppressed based solely on a delay of more than
six hours. The Court cites no authority for a canon of
interpretation that favors a “negative implication” of this
sort over clear and express statutory language.
                               C
   The Court contends that a literal interpretation of
§3501(a) would leave the prompt presentment require
ment set out in Federal Rule of Criminal Procedure 5(a)(1)
“without any teeth, for . . . if there is no McNabb-Mallory
there is no apparent remedy for delay in presentment.”
Ante, at 15. There is nothing strange, however, about a
prompt presentment requirement that is not enforced by a
rule excluding voluntary confessions made during a period
of excessive prepresentment delay. As the Court notes,
“[t]he common law obliged an arresting officer to bring his
prisoner before a magistrate as soon as he reasonably
could,” ante, at 1, but the McNabb-Mallory supervisory
rule was not adopted until the middle of the 20th century.
To this day, while the States are required by the Fourth
Amendment to bring an arrestee promptly before a judi
cial officer, see, e.g., County of Riverside v. McLaughlin,
6                CORLEY v. UNITED STATES

                      ALITO, J., dissenting

500 U. S. 44, 56 (1991), we have never held that this con
stitutional requirement is backed by an automatic exclu
sionary sanction, see, e.g., Hudson v. Michigan, 547 U. S.
586, 592 (2006). And although the prompt presentment
requirement serves interests in addition to the prevention
of coerced confessions, the McNabb-Mallory rule provides
no sanction for excessive prepresentment delay in those
instances in which no confession is sought or obtained.
   Moreover, the need for the McNabb-Mallory exclusion
ary rule is no longer clear. That rule, which was adopted
long before Miranda, originally served a purpose that is
now addressed by the giving of Miranda warnings upon
arrest. As Miranda recognized, McNabb and Mallory
were “responsive to the same considerations of Fifth
Amendment policy” that the Miranda rule was devised to
address. Miranda v. Arizona, 384 U. S. 436, 463 (1966).
   In the pre-Miranda era, the requirement of prompt
presentment ensured that persons taken into custody
would, within a relatively short period, receive advice
about their rights. See McNabb v. United States, 318
U. S. 332, 344 (1943). Now, however, Miranda ensures
that arrestees receive such advice at an even earlier point,
within moments of being taken into custody. Of course,
arrestees, after receiving Miranda warnings, may waive
their rights and submit to questioning by law enforcement
officers, see, e.g., Davis v. United States, 512 U. S. 452,
458 (1994), and arrestees may likewise waive the prompt
presentment requirement, see, e.g., New York v. Hill, 528
U. S. 110, 114 (2000) (“We have . . . ‘in the context of a
broad array of constitutional and statutory provisions,’
articulated a general rule that presumes the availability of
waiver, . . . and we have recognized that ‘the most basic
rights of criminal defendants are . . . subject to waiver’ ”).
It seems unlikely that many arrestees who are willing to
waive the right to remain silent and the right to the assis
tance of counsel during questioning would balk at waiving
                   Cite as: 556 U. S. ____ (2009)                 7

                        ALITO, J., dissenting

the right to prompt presentment. More than a few courts
of appeals have gone as far as to hold that a waiver of
Miranda rights also constitutes a waiver under McNabb-
Mallory. See, e.g., United States v. Salamanca, 990 F. 2d
629, 634 (CADC), cert. denied, 510 U. S. 928 (1993);
United States v. Barlow, 693 F. 2d 954, 959 (CA6 1982),
cert. denied, 461 U. S. 945 (1983); United States v. Indian
Boy X, 565 F. 2d 585, 591 (CA9 1977), cert. denied, 439
U. S. 841 (1978); United States v. Duvall, 537 F. 2d 15, 23–
24, n. 9 (CA2), cert. denied, 426 U. S. 950 (1976); United
States v. Howell, 470 F. 2d 1064, 1067, n. 1 (CA9 1972);
Pettyjohn v. United States, 419 F. 2d 651, 656 (CADC
1969), cert. denied, 397 U. S. 1058 (1970); O’Neal v. United
States, 411 F. 2d 131, 136–137 (CA5), cert. denied, 396
U. S. 827 (1969). Whether or not those decisions are
correct, it is certainly not clear that the McNabb-Mallory
rule adds much protection beyond that provided by
Miranda.
                             D
  The Court contends that the legislative history of §3501
supports its interpretation, but the legislative history
proves nothing that is not evident from the terms of the
statute. With respect to §3501(a), the legislative history
certainly shows that the provision’s chief backers meant to
do away with Miranda,3 but the Court cites no evidence
that this was all that §3501(a) was intended to accom
plish. To the contrary, the Senate Report clearly says that
§3501(a) was meant to reinstate the traditional rule that a

——————
  3 At argument, the Government conceded “that section (a) was con

sidered to overrule Miranda and subsection (c) was addressed to
McNabb-Mallory.” See Tr. of Oral Arg. 38. It is apparent that the
attorney for the Government chose his words carefully and did not
concede, as the Court seems to suggest, that subsection (a) was in
tended to do no more than to overrule Miranda or that subsection (c)
was the only part of §3501 that affected the McNabb-Mallory rule.
8                CORLEY v. UNITED STATES

                     ALITO, J., dissenting

confession should be excluded only if involuntary, see
S. Rep. No. 1097, 90th Cong., 2d Sess., 38 (1968) (Senate
Report), a step that obviously has consequences beyond
the elimination of Miranda. And the Senate Report re
peatedly cited Escobedo v. Illinois, 378 U. S. 478 (1964), as
an example of an unsound limitation on the admission of
voluntary confessions, see Senate Report 41–51, thus
illustrating that §3501(a) was not understood as simply an
anti-Miranda provision. Whether a majority of the Mem
bers of the House and Senate had the McNabb-Mallory
rule specifically in mind when they voted for §3501(a) is
immaterial. Statutory provisions may often have a reach
that is broader than the specific targets that the lawmak
ers might have had in mind at the time of enactment.
   The legislative history relating to §3501(c) suggests
nothing more than that some Members of Congress may
mistakenly have thought that the version of §3501 that
was finally adopted would not displace the McNabb-
Mallory rule. As the Court relates, the version of §3501(c)
that emerged from the Senate Judiciary Committee would
have completely eliminated that rule. See ante, at 12–13.
Some Senators opposed this, and the version of this provi
sion that was eventually passed simply trimmed the rule.
It is possible to identify a few Senators who spoke out in
opposition to the earlier version of subsection (c) and then
voted in favor of the version that eventually passed, and it
is fair to infer that these Senators likely thought that the
amendment of subsection (c) had saved the rule. See 114
Cong. Rec. 14172–14175, 14798 (1968). But there is no
evidence that a majority of the House and Senate shared
that view, and any Member who took a few moments to
read subsections (a) and (c) must readily have understood
that subsection (a) would wipe away all non-constitution
ally based rules barring the admission of voluntary confes
sions, not just Miranda, and that subsection (c) did not
authorize the suppression of any voluntary confessions.
                     Cite as: 556 U. S. ____ (2009)                   9

                         ALITO, J., dissenting

The Court unjustifiably attributes to a majority of the
House and Senate a mistake that, the legislative history
suggests, may have been made by only a few.
                                E
  Finally, the Court argues that under a literal reading of
§3501(a), “many a rule of evidence [would] be overridden
in case after case.” Ante, at 12. In order to avoid this
absurd result, the Court says, it is necessary to read
§3501(a) as merely abrogating Miranda and not
the McNabb-Mallory rule. There is no merit to this
argument.4
  The language that Congress used in §3501(a)—a confes
sion is “admissible” if “voluntarily given”—is virtually a
verbatim quotation of the language used by this Court in
describing the traditional rule regarding the admission of
confessions. See, e.g., Haynes v. Washington, 373 U. S.
503, 513 (1963) (“ ‘ In short, the true test of admissibility is
that the confession is made freely, voluntarily and without
compulsion or inducement of any sort.’ ” (quoting Wilson v.
United States, 162 U. S. 613, 623 (1896))); Lyons v. Okla
homa, 322 U. S. 596, 602 (1944); Ziang Sung Wan v.
United States, 266 U. S. 1, 15 (1924); Bram v. United
States, 168 U. S. 532, 545 (1897). In making these state
ments, this Court certainly did not mean to suggest that a
voluntary confession must be admitted in those instances
in which a standard rule of evidence would preclude ad
mission, and there is no reason to suppose that Congress
meant any such thing either. In any event, the Federal

——————
   4 Contrary to the Court’s suggestion, cases in which one of the stan

dard Rules of Evidence might block the admission of a voluntary
confession would seem quite rare, and the Court cites no real-world
examples. The Court thus justifies its reading of §3501, which totally
disregards the clear language of subsection (a), based on a few essen
tially fanciful hypothetical cases that, in any event, have been covered
since 1975 by the Federal Rules of Evidence.
10               CORLEY v. UNITED STATES

                     ALITO, J., dissenting

Rules of Evidence now make it clear that §3501(a) does
not supersede ordinary evidence Rules, including Rules
regarding privilege (Rule 501), hearsay (Rule 802), and
restrictions on the use of character evidence (Rule 404).
Thus, it is not necessary to disregard the plain language of
§3501(a), as the Court does, in order to avoid the sort of
absurd results to which the Court refers.
  For all these reasons, I would affirm the decision of the
Court of Appeals, and I therefore respectfully dissent.

```

---

## GROUP: _overhaul2/lake/cases/County of Los Angeles v. Mendez.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: County of Los Angeles v. Mendez
type: case
citation: "581 U.S. 420 (2017)"
parallel_cite: "137 S. Ct. 1539; 198 L. Ed. 2d 52; 26 Fla. L. Weekly Fed. S 604; 85 U.S.L.W. 4292"
neutral_cite: "2017 U.S. LEXIS 3396; 2017 WL 2322832"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2017
date_decided: 2017-05-30
docket: No. 16-369
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
  opinion_url: "https://www.courtlistener.com/opinion/4395246/county-of-los-angeles-v-mendez/"
  cluster_id: 4395246
  opinion_id: null
  identity_checked: true
lake:
  record_id: County of Los Angeles v. Mendez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Use of Force]]"
    role: Anchor
related:
  - "[[Use of Force]]"
  - "[[Graham v. Connor]]"
tags:
  - case
  - fourth-amendment
  - excessive-force
  - provocation-rule
  - graham-v-connor
  - proximate-cause
holding: "The Fourth Amendment provides no basis for the Ninth Circuit's 'provocation rule'; an officer's objectively reasonable use of force cannot be rendered an unreasonable seizure by an earlier, separate Fourth Amendment violation (such as a warrantless entry) that provoked the confrontation, though that distinct violation may support its own claim and proximate-cause damages."
aliases:
  - County of Los Angeles v. Mendez
  - "County of Los Angeles v. Mendez (2017)"
---

# County of Los Angeles v. Mendez

*581 U.S. 420 (2017)* (No. 16-369) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4395246 → lead opinion 4172499 (Alito, J.; 581 U.S. 420, decided May 30, 2017). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text carries S. Ct. star-pagination (parallel 137 S. Ct. 1539), so the pin is to 137 S. Ct. at 1544 (page-label `*1544`) — the official U.S. Reports pagination is not present in the CL text. S9 promotes. -->

## Background
Los Angeles County sheriff's deputies searching for a wanted parolee entered the property where Angel Mendez and Jennifer Garcia were living and, without a warrant and without knocking or announcing, opened the door of a wooden shack in the backyard where the couple was resting. Mendez kept a BB gun to shoot pests; as he rose, he moved the BB gun, and the deputies — seeing the silhouette of what looked like a rifle — opened fire, seriously wounding both Mendez and Garcia. The district court found the shooting itself reasonable under *[[Graham v. Connor]]* but held the deputies liable under the Ninth Circuit's "provocation rule," reasoning that their unconstitutional warrantless entry had provoked the confrontation. The Ninth Circuit affirmed.

## Issue
Whether officers who use force that is objectively reasonable under *[[Graham v. Connor|Graham]]* may nonetheless be held liable for excessive force on the theory that a separate, earlier Fourth Amendment violation provoked the need to use force.

## Rule
The Court rejected the provocation rule root and branch: "We hold that the Fourth Amendment provides no basis for such a rule. A different Fourth Amendment violation cannot transform a later, reasonable use of force into an unreasonable seizure." — 137 S. Ct. at 1544. ^pin-1544

## Application
An excessive-force claim is governed solely by whether the force used was objectively reasonable under *[[Graham v. Connor|Graham]]*, judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] at the moment force is applied. The provocation rule instead conjured an excessive-force violation out of a distinct, antecedent wrong — the warrantless entry — and so permitted liability even where the force was reasonable. If the force was reasonable, there is no excessive-force claim at all; any separate constitutional violation must be litigated as its own claim, with its foreseeable harms recoverable under ordinary proximate-cause principles. The Court also held the Ninth Circuit's alternative proximate-cause theory was infected by the same error and [[Reading and Citing Cases#on-remand|remanded]].

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. Alito, J., delivered the opinion of a unanimous Court; Gorsuch, J., took no part in the consideration or decision of the case.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Mendez* keeps excessive-force analysis anchored to *[[Graham v. Connor|Graham]]*'s moment-of-force reasonableness and eliminates the provocation rule as a route to liability. It preserves, rather than forecloses, recovery for a distinct antecedent violation such as an unlawful entry — through a separate claim and ordinary proximate cause. Teach it as reinforcing that the "reasonableness" inquiry is not to be diluted by folding in earlier, independent Fourth Amendment wrongs.

## Appears on
- [[Use of Force]] — *Anchor*

## Sources
- [*County of Los Angeles v. Mendez*, 581 U.S. 420 (2017)](https://www.courtlistener.com/opinion/4395246/county-of-los-angeles-v-mendez/) — pinpoint: 137 S. Ct. 1539, 1544 (Alito, J., for the Court; the CL opinion text is paginated to the parallel S. Ct. reporter, carrying the page-label `*1544` at the holding — the U.S. Reports star-pagination is not present in the CL text). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b83d9defa108f4cf", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "County of Los Angeles v. Mendez"}, "payload": {"all": [{"cite": "581 U.S. 420", "page": "420", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "581"}, {"cite": "137 S. Ct. 1539", "page": "1539", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "198 L. Ed. 2d 52", "page": "52", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "198"}, {"cite": "2017 U.S. LEXIS 3396", "page": "3396", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2017"}, {"cite": "26 Fla. L. Weekly Fed. S 604", "page": "604", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "85 U.S.L.W. 4292", "page": "4292", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "85"}, {"cite": "2017 WL 2322832", "page": "2322832", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2017"}], "display": "581 U.S. 420", "official": {"cite": "581 U.S. 420", "page": "420", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "581"}, "official_selection_present": true, "record_id": "County of Los Angeles v. Mendez"}}
{"assertion_id": "1855cb9805152add", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "County of Los Angeles v. Mendez"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "County of Los Angeles v. Mendez", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — County of Los Angeles v. Mendez

```json
{
  "schema_version": "s2.v1",
  "record_id": "County of Los Angeles v. Mendez",
  "status": "under_review",
  "identity": {
    "case_name": "County of Los Angeles v. Mendez",
    "case_name_short": "Mendez",
    "case_name_full": "COUNTY OF LOS ANGELES, CALIFORNIA, Et Al., Petitioners v. Angel MENDEZ, Et Al.",
    "input_case_name": "County of Los Angeles v. Mendez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2017-05-30",
    "year": 2017,
    "docket": "No. 16-369",
    "cluster_id": 4395246,
    "lead_opinion_id": 4172499,
    "sibling_ids": [],
    "absolute_url": "/opinion/4395246/county-of-los-angeles-v-mendez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "581 U.S. 420",
      "volume": "581",
      "reporter": "U.S.",
      "page": "420",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "137 S. Ct. 1539",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "1539",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "198 L. Ed. 2d 52",
        "volume": "198",
        "reporter": "L. Ed. 2d",
        "page": "52",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 604",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4292",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4292",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 U.S. LEXIS 3396",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "3396",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 2322832",
        "volume": "2017",
        "reporter": "WL",
        "page": "2322832",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "581 U.S. 420",
        "volume": "581",
        "reporter": "U.S.",
        "page": "420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 1539",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "1539",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "198 L. Ed. 2d 52",
        "volume": "198",
        "reporter": "L. Ed. 2d",
        "page": "52",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. LEXIS 3396",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "3396",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 604",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4292",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4292",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 2322832",
        "volume": "2017",
        "reporter": "WL",
        "page": "2322832",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "581 U.S. 420",
    "official_selection": {
      "court_class": "scotus",
      "selected": "581 U.S. 420",
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
    "date_created": "2026-07-06T13:14:37Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:14:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:14:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "county-of-los-angeles-v-mendez--4395246",
      "to_record_id": "County of Los Angeles v. Mendez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — County of Los Angeles v. Mendez

```
(Slip Opinion)              OCTOBER TERM, 2016                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

  COUNTY OF LOS ANGELES, CALIFORNIA, ET AL. v. 

                MENDEZ ET AL. 


CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

      No. 16–369.      Argued March 22, 2017—Decided May 30, 2017
The Los Angeles County Sheriff’s Department received word from a
  confidential informant that a potentially armed and dangerous parol-
  ee-at-large had been seen at a certain residence. While other officers
  searched the main house, Deputies Conley and Pederson searched
  the back of the property where, unbeknownst to the deputies, re-
  spondents Mendez and Garcia were napping inside a shack where
  they lived. Without a search warrant and without announcing their
  presence, the deputies opened the door of the shack. Mendez rose
  from the bed, holding a BB gun that he used to kill pests. Deputy
  Conley yelled, “Gun!” and the deputies immediately opened fire,
  shooting Mendez and Garcia multiple times. Officers did not find the
  parolee in the shack or elsewhere on the property.
     Mendez and Garcia sued Deputies Conley and Pederson and the
  County under 42 U. S. C. §1983, pressing three Fourth Amendment
  claims: a warrantless entry claim, a knock-and-announce claim, and
  an excessive force claim. On the first two claims, the District Court
  awarded Mendez and Garcia nominal damages. On the excessive
  force claim, the court found that the deputies’ use of force was rea-
  sonable under Graham v. Connor, 490 U. S. 386, but held them liable
  nonetheless under the Ninth Circuit’s provocation rule, which makes
  an officer’s otherwise reasonable use of force unreasonable if (1) the
  officer “intentionally or recklessly provokes a violent confrontation”
  and (2) “the provocation is an independent Fourth Amendment viola-
  tion,” Billington v. Smith, 292 F. 3d 1177, 1189. On appeal, the
  Ninth Circuit held that the officers were entitled to qualified immun-
  ity on the knock-and-announce claim and that the warrantless entry
  violated clearly established law. It also affirmed the District Court’s
2               COUNTY OF LOS ANGELES v. MENDEZ

                                  Syllabus

    application of the provocation rule, and held, in the alternative, that
    basic notions of proximate cause would support liability even without
    the provocation rule.
Held: The Fourth Amendment provides no basis for the Ninth Circuit’s
 “provocation rule.” Pp. 5–10.
    (a) The provocation rule is incompatible with this Court’s excessive
 force jurisprudence, which sets forth a settled and exclusive frame-
 work for analyzing whether the force used in making a seizure com-
 plies with the Fourth Amendment. See Graham, supra, at 395. The
 operative question in such cases is “whether the totality of the cir-
 cumstances justifie[s] a particular sort of search or seizure.” Tennes-
 see v. Garner, 471 U. S. 1, 8–9. When an officer carries out a seizure
 that is reasonable, taking into account all relevant circumstances,
 there is no valid excessive force claim. The provocation rule, howev-
 er, instructs courts to look back in time to see if a different Fourth
 Amendment violation was somehow tied to the eventual use of force,
 an approach that mistakenly conflates distinct Fourth Amendment
 claims. The proper framework is set out in Graham. To the extent
 that a plaintiff has other Fourth Amendment claims, they should be
 analyzed separately.
    The Ninth Circuit attempts to cabin the provocation rule by defin-
 ing a two-prong test: First, the separate constitutional violation must
 “creat[e] a situation which led to” the use of force; and second, the
 separate constitutional violation must be committed recklessly or in-
 tentionally. 815 F. 3d 1178, 1193. Neither limitation, however,
 solves the fundamental problem: namely, that the provocation rule is
 an unwarranted and illogical expansion of Graham. In addition, each
 limitation creates problems of its own. First, the rule relies on a
 vague causal standard. Second, while the reasonableness of a search
 or seizure is almost always based on objective factors, the provocation
 rule looks to the subjective intent of the officers who carried out the
 seizure.
    There is no need to distort the excessive force inquiry in this way in
 order to hold law enforcement officers liable for the foreseeable con-
 sequences of all their constitutional torts. Plaintiffs can, subject to
 qualified immunity, generally recover damages that are proximately
 caused by any Fourth Amendment violation. See, e.g., Heck v.
 Humphrey, 512 U. S. 477, 483. Here, if respondents cannot recover
 on their excessive force claim, that will not foreclose recovery for in-
 juries proximately caused by the warrantless entry. Pp. 5–10.
    (b) The Ninth Circuit’s proximate-cause holding is similarly taint-
 ed. Its analysis appears to focus solely on the risks foreseeably asso-
 ciated with the failure to knock and announce—the claim on which
 the court concluded that the deputies had qualified immunity—
                     Cite as: 581 U. S. ____ (2017)                   3

                               Syllabus

  rather than the warrantless entry. On remand, the court should re-
  visit the question whether proximate cause permits respondents to
  recover damages for their injuries based on the deputies’ failure to
  secure a warrant at the outset. Pp. 10–11.
815 F. 3d 1178, vacated and remanded.

  ALITO, J., delivered the opinion of the Court, in which all other Mem-
bers joined, except GORSUCH, J., who took no part in the consideration
or decision of the case.
                       Cite as: 581 U. S. ____ (2017)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 16–369
                                  _________________


  COUNTY OF LOS ANGELES, CALIFORNIA, ET AL., 

     PETITIONERS v. ANGEL MENDEZ, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                                [May 30, 2017]


  JUSTICE ALITO delivered the opinion of the Court.
  If law enforcement officers make a “seizure” of a person
using force that is judged to be reasonable based on a
consideration of the circumstances relevant to that deter-
mination, may the officers nevertheless be held liable for
injuries caused by the seizure on the ground that they
committed a separate Fourth Amendment violation that
contributed to their need to use force? The Ninth Circuit
has adopted a “provocation rule” that imposes liability in
such a situation.
  We hold that the Fourth Amendment provides no basis
for such a rule. A different Fourth Amendment violation
cannot transform a later, reasonable use of force into an
unreasonable seizure.
                            I

                            A

  In October 2010, deputies from the Los Angeles County
Sheriff ’s Department were searching for a parolee-at-large
named Ronnie O’Dell. A felony arrest warrant had been
issued for O’Dell, who was believed to be armed and dan-
gerous and had previously evaded capture. Findings of
2           COUNTY OF LOS ANGELES v. MENDEZ

                     Opinion of the Court

Fact and Conclusions of Law, No. 2:11–cv–04771 (CD
Cal.), App. to Pet. for Cert. 56a, 64a. Deputies Christo-
pher Conley and Jennifer Pederson were assigned to assist
the task force searching for O’Dell. Id., at 57a–58a. The
task force received word from a confidential informant
that O’Dell had been seen on a bicycle at a home in Lan-
caster, California, owned by Paula Hughes, and the offic-
ers then mapped out a plan for apprehending O’Dell. Id.,
at 58a. Some officers would approach the front door of the
Hughes residence, while Deputies Conley and Pederson
would search the rear of the property and cover the back
door of the residence. Id., at 59a. During this briefing, it
was announced that a man named Angel Mendez lived in
the backyard of the Hughes home with a pregnant woman
named Jennifer Garcia (now Mrs. Jennifer Mendez). Ibid.
Deputy Pederson heard this announcement, but at trial
Deputy Conley testified that he did not remember it. Ibid.
  When the officers reached the Hughes residence around
midday, three of them knocked on the front door while
Deputies Conley and Pederson went to the back of the
property. Id., at 63a. At the front door, Hughes asked if
the officers had a warrant. Ibid. A sergeant responded
that they did not but were searching for O’Dell and had a
warrant for his arrest. Ibid. One of the officers heard
what he thought were sounds of someone running inside
the house. Id., at 64a. As the officers prepared to open
the door by force, Hughes opened the door and informed
them that O’Dell was not in the house. Ibid. She was
placed under arrest, and the house was searched, but
O’Dell was not found. Ibid.
  Meanwhile, Deputies Conley and Pederson, with guns
drawn, searched the rear of the residence, which was
cluttered with debris and abandoned automobiles. Id., at
60a, 65a. The property included three metal storage sheds
and a one-room shack made of wood and plywood. Id., at
60a. Mendez had built the shack, and he and Garcia had
                 Cite as: 581 U. S. ____ (2017)           3

                     Opinion of the Court

lived inside for about 10 months. Id., at 61a. The shack
had a single doorway covered by a blue blanket. Ibid.
Amid the debris on the ground, an electrical cord ran into
the shack, and an air conditioner was mounted on the
side. Id., at 62a. A gym storage locker and clothes and
other possessions were nearby. Id., at 61a. Mendez kept a
BB rifle in the shack for use on rats and other pests. Id.,
at 62a. The BB gun “closely resembled a small caliber
rifle.” Ibid.
   Deputies Conley and Pederson first checked the three
metal sheds and found no one inside. Id., at 65a. They
then approached the door of the shack. Id., at 66a. Unbe-
knownst to the officers, Mendez and Garcia were in the
shack and were napping on a futon. Id., at 67a. The
deputies did not have a search warrant and did not knock
and announce their presence. Id., at 66a. When Deputy
Conley opened the wooden door and pulled back the blan-
ket, Mendez thought it was Ms. Hughes and rose from the
bed, picking up the BB gun so he could stand up and place
it on the floor. Id., at 68a. As a result, when the deputies
entered, he was holding the BB gun, and it was “point[ing]
somewhat south towards Deputy Conley.” Id., at 69a.
Deputy Conley yelled, “Gun!” and the deputies immediately
opened fire, discharging a total of 15 rounds. Id., at 69a–
70a. Mendez and Garcia “were shot multiple times and
suffered severe injuries,” and Mendez’s right leg was later
amputated below the knee. Id., at 70a. O’Dell was not in
the shack or anywhere on the property. Ibid.
                           B
  Mendez and his wife (respondents here) filed suit under
Rev. Stat. §1976, 42 U. S. C. §1983, against petitioners,
the County of Los Angeles and Deputies Conley and Ped-
erson. As relevant here, they pressed three Fourth
Amendment claims. First, they claimed that the deputies
executed an unreasonable search by entering the shack
4           COUNTY OF LOS ANGELES v. MENDEZ

                     Opinion of the Court

without a warrant (the “warrantless entry claim”); second,
they asserted that the deputies performed an unreason-
able search because they failed to announce their presence
before entering the shack (the “knock-and-announce
claim”); and third, they claimed that the deputies effected
an unreasonable seizure by deploying excessive force in
opening fire after entering the shack (the “excessive force
claim”).
  After a bench trial, the District Court ruled largely in
favor of respondents. App. to Pet. for Cert. 135a–136a.
The court found Deputy Conley liable on the warrantless
entry claim, and the court also found both deputies liable
on the knock-and-announce claim. But the court awarded
nominal damages for these violations because “the act of
pointing the BB gun” was a superseding cause “as far as
damage [from the shooting was] concerned.” App. 238.
  The District Court then addressed respondents’ exces-
sive force claim. App. to Pet. for Cert. 105a–127a. The
court began by evaluating whether the deputies used
excessive force under Graham v. Connor, 490 U. S. 386
(1989). The court held that, under Graham, the deputies’
use of force was reasonable “given their belief that a man
was holding a firearm rifle threatening their lives.” App.
to Pet. for Cert. 108a. But the court did not end its exces-
sive force analysis at this point. Instead, the court turned
to the Ninth Circuit’s provocation rule, which holds that
“an officer’s otherwise reasonable (and lawful) defensive
use of force is unreasonable as a matter of law, if (1) the
officer intentionally or recklessly provoked a violent re-
sponse, and (2) that provocation is an independent consti-
tutional violation.” Id., at 111a. Based on this rule, the
District Court held the deputies liable for excessive force
and awarded respondents around $4 million in damages.
Id., at 135a–136a.
  The Court of Appeals affirmed in part and reversed in
part. 815 F. 3d 1178 (CA9 2016). Contrary to the District
                 Cite as: 581 U. S. ____ (2017)           5

                     Opinion of the Court

Court, the Court of Appeals held that the officers were
entitled to qualified immunity on the knock-and-announce
claim. Id., at 1191–1193. But the court concluded that
the warrantless entry of the shack violated clearly estab-
lished law and was attributable to both deputies. Id., at
1191, 1195. Finally, and most important for present
purposes, the court affirmed the application of the provo-
cation rule. The Court of Appeals did not disagree with
the conclusion that the shooting was reasonable under
Graham; instead, like the District Court, the Court of
Appeals applied the provocation rule and held the depu-
ties liable for the use of force on the theory that they had
intentionally and recklessly brought about the shooting by
entering the shack without a warrant in violation of clearly
established law. 815 F. 3d, at 1193.
   The Court of Appeals also adopted an alternative ra-
tionale for its judgment. It held that “basic notions of
proximate cause” would support liability even without the
provocation rule because it was “reasonably foreseeable”
that the officers would meet an armed homeowner when
they “barged into the shack unannounced.” Id., at 1194–
1195.
   We granted certiorari. 580 U. S. ___ (2016).
                             II
  The Ninth Circuit’s provocation rule permits an exces-
sive force claim under the Fourth Amendment “where an
officer intentionally or recklessly provokes a violent con-
frontation, if the provocation is an independent Fourth
Amendment violation.” Billington v. Smith, 292 F. 3d
1177, 1189 (CA9 2002). The rule comes into play after a
forceful seizure has been judged to be reasonable under
Graham. Once a court has made that determination, the
rule instructs the court to ask whether the law enforce-
ment officer violated the Fourth Amendment in some
other way in the course of events leading up to the seizure.
6           COUNTY OF LOS ANGELES v. MENDEZ

                     Opinion of the Court

If so, that separate Fourth Amendment violation may
“render the officer’s otherwise reasonable defensive use of
force unreasonable as a matter of law.” Id., at 1190–1191.
   The provocation rule, which has been “sharply ques-
tioned” outside the Ninth Circuit, City and County of San
Francisco v. Sheehan, 575 U. S. ___, ___, n. 4 (2015) (slip
op., at 14, n. 4), is incompatible with our excessive force
jurisprudence. The rule’s fundamental flaw is that it uses
another constitutional violation to manufacture an exces-
sive force claim where one would not otherwise exist.
   The Fourth Amendment prohibits “unreasonable
searches and seizures.” “[R]easonableness is always the
touchstone of Fourth Amendment analysis,” Birchfield v.
North Dakota, 579 U. S. ___, ___ (2016) (slip op., at 37),
and reasonableness is generally assessed by carefully
weighing “the nature and quality of the intrusion on the
individual’s Fourth Amendment interests against the
importance of the governmental interests alleged to justify
the intrusion.” Tennessee v. Garner, 471 U. S. 1, 8 (1985)
(internal quotation marks omitted).
   Our case law sets forth a settled and exclusive frame-
work for analyzing whether the force used in making a
seizure complies with the Fourth Amendment. See Gra-
ham, 490 U. S., at 395. As in other areas of our Fourth
Amendment jurisprudence, “[d]etermining whether the
force used to effect a particular seizure is ‘reasonable’ ”
requires balancing of the individual’s Fourth Amendment
interests against the relevant government interests. Id.,
at 396. The operative question in excessive force cases is
“whether the totality of the circumstances justifie[s] a
particular sort of search or seizure.” Garner, supra, at 8–9.
   The reasonableness of the use of force is evaluated
under an “objective” inquiry that pays “careful attention to
the facts and circumstances of each particular case.”
Graham, supra, at 396. And “[t]he ‘reasonableness’ of a
particular use of force must be judged from the perspective
                  Cite as: 581 U. S. ____ (2017)            7

                      Opinion of the Court

of a reasonable officer on the scene, rather than with the
20/20 vision of hindsight.” Ibid. “Excessive force claims
. . . are evaluated for objective reasonableness based upon
the information the officers had when the conduct oc-
curred.” Saucier v. Katz, 533 U. S. 194, 207 (2001). That
inquiry is dispositive: When an officer carries out a seizure
that is reasonable, taking into account all relevant cir-
cumstances, there is no valid excessive force claim.
    The basic problem with the provocation rule is that it
fails to stop there. Instead, the rule provides a novel and
unsupported path to liability in cases in which the use of
force was reasonable. Specifically, it instructs courts to
look back in time to see if there was a different Fourth
Amendment violation that is somehow tied to the eventual
use of force. That distinct violation, rather than the force-
ful seizure itself, may then serve as the foundation of the
plaintiff ’s excessive force claim. Billington, supra, at 1190
(“The basis of liability for the subsequent use of force is
the initial constitutional violation . . . ”).
    This approach mistakenly conflates distinct Fourth
Amendment claims. Contrary to this approach, the objec-
tive reasonableness analysis must be conducted separately
for each search or seizure that is alleged to be unconstitu-
tional. An excessive force claim is a claim that a law
enforcement officer carried out an unreasonable seizure
through a use of force that was not justified under the
relevant circumstances. It is not a claim that an officer
used reasonable force after committing a distinct Fourth
Amendment violation such as an unreasonable entry.
    By conflating excessive force claims with other Fourth
Amendment claims, the provocation rule permits excessive
force claims that cannot succeed on their own terms. That
is precisely how the rule operated in this case. The Dis-
trict Court found (and the Ninth Circuit did not dispute)
that the use of force by the deputies was reasonable under
Graham. However, respondents were still able to recover
8             COUNTY OF LOS ANGELES v. MENDEZ

                          Opinion of the Court

damages because the deputies committed a separate
constitutional violation (the warrantless entry into the
shack) that in some sense set the table for the use of force.
That is wrong. The framework for analyzing excessive
force claims is set out in Graham. If there is no excessive
force claim under Graham, there is no excessive force
claim at all. To the extent that a plaintiff has other
Fourth Amendment claims, they should be analyzed
separately.*
  The Ninth Circuit’s efforts to cabin the provocation rule
only undermine it further. The Ninth Circuit appears to
recognize that it would be going entirely too far to suggest
that any Fourth Amendment violation that is connected to
a reasonable use of force should create a valid excessive
force claim. See, e.g., Beier v. Lewiston, 354 F. 3d 1058,
1064 (CA9 2004) (“Because the excessive force and false
arrest factual inquiries are distinct, establishing a lack of
probable cause to make an arrest does not establish an
excessive force claim, and vice-versa”). Instead, that court
has endeavored to limit the rule to only those distinct
Fourth Amendment violations that in some sense “pro-
voked” the need to use force. The concept of provocation,
——————
  * Respondents do not attempt to defend the provocation rule. In-
stead, they argue that the judgment below should be affirmed under
Graham itself. Graham commands that an officer’s use of force be
assessed for reasonableness under the “totality of the circumstances.”
490 U. S., at 396 (internal quotation marks omitted). On respondents’
view, that means taking into account unreasonable police conduct prior
to the use of force that foreseeably created the need to use it. Brief for
Respondents 42–43. We did not grant certiorari on that question, and
the decision below did not address it. Accordingly, we decline to ad-
dress it here. See, e.g., McLane Co. v. EEOC, ante, at 11 (“[W]e are a
court of review, not of first view” (internal quotation marks omitted)).
All we hold today is that once a use of force is deemed reasonable under
Graham, it may not be found unreasonable by reference to some sepa-
rate constitutional violation. Any argument regarding the District
Court’s application of Graham in this case should be addressed to the
Ninth Circuit on remand.
                 Cite as: 581 U. S. ____ (2017)           9

                     Opinion of the Court

in turn, has been defined using a two-prong test. First,
the separate constitutional violation must “creat[e] a
situation which led to” the use of force; second, the sepa-
rate constitutional violation must be committed recklessly
or intentionally. 815 F. 3d, at 1193 (internal quotation
marks omitted).
   Neither of these limitations solves the fundamental
problem of the provocation rule: namely, that it is an
unwarranted and illogical expansion of Graham. But in
addition, each of the limitations creates problems of its
own. First, the rule includes a vague causal standard. It
applies when a prior constitutional violation “created a
situation which led to” the use of force. The rule does not
incorporate the familiar proximate cause standard. In-
deed, it is not clear what causal standard is being applied.
Second, while the reasonableness of a search or seizure is
almost always based on objective factors, see Whren v.
United States, 517 U. S. 806, 814 (1996), the provocation
rule looks to the subjective intent of the officers who car-
ried out the seizure. As noted, under the Ninth Circuit’s
rule, a prior Fourth Amendment violation may be held to
have provoked a later, reasonable use of force only if the
prior violation was intentional or reckless.
   The provocation rule may be motivated by the notion
that it is important to hold law enforcement officers liable
for the foreseeable consequences of all of their constitu-
tional torts. See Billington, 292 F. 3d, at 1190 (“[I]f an
officer’s provocative actions are objectively unreasonable
under the Fourth Amendment, . . . liability is established,
and the question becomes . . . what harms the constitu-
tional violation proximately caused”). However, there is
no need to distort the excessive force inquiry in order to
accomplish this objective. To the contrary, both parties
accept the principle that plaintiffs can—subject to quali-
fied immunity—generally recover damages that are prox-
imately caused by any Fourth Amendment violation. See,
10          COUNTY OF LOS ANGELES v. MENDEZ

                      Opinion of the Court

e.g., Heck v. Humphrey, 512 U. S. 477, 483 (1994) (§1983
“creates a species of tort liability” informed by tort princi-
ples regarding “damages and the prerequisites for their
recovery” (internal quotation marks omitted)); Memphis
Community School Dist. v. Stachura, 477 U. S. 299, 306
(1986) (“[W]hen §1983 plaintiffs seek damages for viola-
tions of constitutional rights, the level of damages is ordi-
narily determined according to principles derived from the
common law of torts”). Thus, there is no need to dress up
every Fourth Amendment claim as an excessive force
claim. For example, if the plaintiffs in this case cannot
recover on their excessive force claim, that will not fore-
close recovery for injuries proximately caused by the war-
rantless entry. The harm proximately caused by these
two torts may overlap, but the two claims should not be
confused.
                             III
  The Court of Appeals also held that “even without rely-
ing on [the] provocation theory, the deputies are liable for
the shooting under basic notions of proximate cause.” 815
F. 3d, at 1194. In other words, the court apparently con-
cluded that the shooting was proximately caused by the
deputies’ warrantless entry of the shack. Proper analysis
of this proximate cause question required consideration of
the “foreseeability or the scope of the risk created by the
predicate conduct,” and required the court to conclude that
there was “some direct relation between the injury asserted
and the injurious conduct alleged.” Paroline v. United
States, 572 U. S. ___, ___ (2014) (slip op., at 7) (internal
quotation marks omitted).
  Unfortunately, the Court of Appeals’ proximate cause
analysis appears to have been tainted by the same errors
that cause us to reject the provocation rule. The court
reasoned that when officers make a “startling entry” by
“barg[ing] into” a home “unannounced,” it is reasonably
                 Cite as: 581 U. S. ____ (2017)           11

                     Opinion of the Court

foreseeable that violence may result. 815 F. 3d, at 1194–
1195 (internal quotation marks omitted). But this ap-
pears to focus solely on the risks foreseeably associated
with the failure to knock and announce, which could not
serve as the basis for liability since the Court of Appeals
concluded that the officers had qualified immunity on that
claim. By contrast, the Court of Appeals did not identify
the foreseeable risks associated with the relevant constitu-
tional violation (the warrantless entry); nor did it explain
how, on these facts, respondents’ injuries were proximately
caused by the warrantless entry. In other words, the
Court of Appeals’ proximate cause analysis, like the provo-
cation rule, conflated distinct Fourth Amendment claims
and required only a murky causal link between the war-
rantless entry and the injuries attributed to it. On re-
mand, the court should revisit the question whether prox-
imate cause permits respondents to recover damages for
their shooting injuries based on the deputies’ failure to
secure a warrant at the outset. See Bank of America Corp.
v. Miami, ante, at 12 (declining to “draw the precise
boundaries of proximate cause” in the first instance). The
arguments made on this point by the parties and by the
United States as amicus provide a useful starting point for
this inquiry. See Brief for Petitioners 42–56; Brief for
Respondents 20–31, 51–59; Reply Brief 17–24; Brief for
United States as Amicus Curiae 26–32.
                        *     *    *
   For these reasons, the judgment of the Court of Appeals
is vacated, and the case is remanded for further proceed-
ings consistent with this opinion.
                                           It is so ordered.

  JUSTICE GORSUCH took no part in the consideration or
decision of this case.

```

---
