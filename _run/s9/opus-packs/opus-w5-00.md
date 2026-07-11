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

## GROUP: _overhaul2/lake/cases/Gilbert v. California.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Gilbert v. California"
type: case
citation: "388 U.S. 263 (1967)"
parallel_cite: "87 S. Ct. 1951; 18 L. Ed. 2d 1178"
neutral_cite: 1967 U.S. LEXIS 1086
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gilbert v. California
  varies_by_point: false
  scope_note: "Wade-Gilbert right to counsel attaches only at/after initiation of adversary judicial proceedings (Kirby v. Illinois)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107487/gilbert-v-california/"
  cluster_id: 107487
  opinion_id: 107487
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Anchor"
related: ["[[United States v. Wade]]", "[[Stovall v. Denno]]", "[[Kirby v. Illinois]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "lineup", "eyewitness-identification", "per-se-exclusion"]
holding: "Testimony that a witness identified the accused at an uncounseled post-indictment lineup must be excluded per se — a strict rule (no…"
lake:
  record_id: Gilbert v. California
  status: verified
  projected_at: 2026-07-06
---

# Gilbert v. California

*388 U.S. 263 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gilbert was convicted of armed robbery and the murder of a police officer. Sixteen days after his indictment and the appointment of counsel, police conducted a lineup in a Los Angeles auditorium — without notice to his counsel — before roughly 100 eyewitnesses to various robberies. At trial, several witnesses identified Gilbert in court, and the State also elicited testimony that they had identified him at the uncounseled lineup.

## Issue
What relief is required when the State introduces (1) in-court identifications by witnesses who viewed an uncounseled post-indictment lineup and (2) testimony that those witnesses identified the accused at that lineup.

## Rule
The two categories are treated differently. In-court identifications require a [[United States v. Wade]] hearing to determine whether they rest on an [[Inevitable Discovery and Independent Source|independent source]] untainted by the illegal lineup. But testimony that a witness identified the accused at the uncounseled lineup is the direct product of the constitutional violation and is subject to automatic exclusion: "Only a per se exclusionary rule as to such testimony can be an effective sanction to assure that law enforcement authorities will respect the accused's constitutional right to the presence of his counsel at the critical lineup." — 388 U.S. at 273. ^pin-273

## Application
The lineup occurred after Gilbert's indictment and the appointment of counsel, yet counsel received no notice — a Sixth Amendment violation under *[[United States v. Wade|Wade]]*. The in-court identifications therefore had to be [[Reading and Citing Cases#on-remand|remanded]] for an independent-source determination, but the testimony that the apartment manager and the eight penalty-stage witnesses had identified Gilbert at that very lineup was the direct result of the illegal lineup, so its admission was error subject to [[Common Legal Terms#per-se|per se]] exclusion rather than an independent-source inquiry.

## Conclusion
Admission of the witnesses' testimony about their uncounseled-lineup identifications was constitutional error requiring reversal under a [[Common Legal Terms#per-se|per se]] exclusionary rule; the in-court identifications were [[Reading and Citing Cases#on-remand|remanded]] for a *[[United States v. Wade|Wade]]* independent-source hearing.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Gilbert*'s holding. The *[[United States v. Wade|Wade]]*-*Gilbert* right to counsel attaches only at or after the initiation of adversary judicial proceedings ([[Kirby v. Illinois]]); *Gilbert*'s own lineup was post-indictment and remains within the rule.

## Appears on
- [[Eyewitness Identification]] — *Key — Anchor*

## Sources
- *Gilbert v. California*, 388 U.S. 263 (1967) — https://www.courtlistener.com/opinion/107487/gilbert-v-california/ — pinpoint: 273.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7693463cdddd3ec6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Gilbert v. California"}, "payload": {"all": [{"cite": "388 U.S. 263", "page": "263", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "388"}, {"cite": "87 S. Ct. 1951", "page": "1951", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "18 L. Ed. 2d 1178", "page": "1178", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "18"}, {"cite": "1967 U.S. LEXIS 1086", "page": "1086", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": "388 U.S. 263", "official": {"cite": "388 U.S. 263", "page": "263", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "388"}, "official_selection_present": true, "record_id": "Gilbert v. California"}}
{"assertion_id": "abb55e50a191274d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-273", "record_id": "Gilbert v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-273", "pinpoint_status": "slip-only", "quote": "--- # Gilbert v. California *388 U.S. 263 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gilbert was convicted of armed robbery and the murder of a police officer. Sixteen days after his indictment and the appointment of counsel, police conducted a lineup in a Los Angeles auditorium — without notice to his counsel — before roughly 100 eyewitnesses to various robberies. At trial, several witnesses identified Gilbert in court, and the State also elicited testimony that they had identified him at the uncounseled lineup. ## Issue What relief is required when the State introduces (1) in-court identifications by witnesses who viewed an uncounseled post-indictment lineup and (2) testimony that those witnesses identified the accused at that lineup. ## Rule The two categories are treated differently. In-court identifications require a [[United States v. Wade]] hearing to determine whether they rest on an independent source untainted by the illegal lineup. But testimony that a witness identified the accused at the uncounseled lineup is the direct product of the constitutional violation and is subject to automatic exclusion:", "quote_fidelity": "mismatch", "record_id": "Gilbert v. California", "star_marker": null}}
{"assertion_id": "e589497514fd23b7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Gilbert v. California"}, "payload": {"as_of_content": "1967-06-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Gilbert v. California", "scope_note": "Wade-Gilbert right to counsel attaches only at/after initiation of adversary judicial proceedings (Kirby v. Illinois).", "varies_by_point": false}}
```

### lake record — Gilbert v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gilbert v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gilbert v. California",
    "case_name_short": "",
    "case_name_full": "Gilbert v. California",
    "input_case_name": "Gilbert v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-12",
    "year": 1967,
    "docket": null,
    "cluster_id": 107487,
    "lead_opinion_id": 107487,
    "sibling_ids": [
      107487,
      9423477,
      9423478,
      9423479,
      9423480,
      9423481
    ],
    "absolute_url": "/opinion/107487/gilbert-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "388 U.S. 263",
      "volume": "388",
      "reporter": "U.S.",
      "page": "263",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1951",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1951",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1178",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1178",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1086",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1086",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "388 U.S. 263",
        "volume": "388",
        "reporter": "U.S.",
        "page": "263",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1951",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1951",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1178",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1178",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1086",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1086",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "388 U.S. 263",
    "official_selection": {
      "court_class": "scotus",
      "selected": "388 U.S. 263",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-273",
      "page": null,
      "quote": "--- # Gilbert v. California *388 U.S. 263 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gilbert was convicted of armed robbery and the murder of a police officer. Sixteen days after his indictment and the appointment of counsel, police conducted a lineup in a Los Angeles auditorium \u2014 without notice to his counsel \u2014 before roughly 100 eyewitnesses to various robberies. At trial, several witnesses identified Gilbert in court, and the State also elicited testimony that they had identified him at the uncounseled lineup. ## Issue What relief is required when the State introduces (1) in-court identifications by witnesses who viewed an uncounseled post-indictment lineup and (2) testimony that those witnesses identified the accused at that lineup. ## Rule The two categories are treated differently. In-court identifications require a [[United States v. Wade]] hearing to determine whether they rest on an independent source untainted by the illegal lineup. But testimony that a witness identified the accused at the uncounseled lineup is the direct product of the constitutional violation and is subject to automatic exclusion:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gilbert v. California",
    "varies_by_point": false,
    "scope_note": "Wade-Gilbert right to counsel attaches only at/after initiation of adversary judicial proceedings (Kirby v. Illinois).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Minnesota v. Matthew Vaughn Diamond",
          "cluster_id": 4338873,
          "cite": [
            "890 N.W.2d 143",
            "2017 Minn. App. LEXIS 9",
            "2017 WL 163710"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
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
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Guzman-Rincon",
          "cluster_id": 4247752,
          "cite": [
            "2015 COA 166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Longoria v. State",
          "cluster_id": 1397963,
          "cite": [
            "154 S.W.3d 747",
            "2004 WL 2851775"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gary Allen Lott, United States of America v. Johnny Marton Lott, AKA Johnny Martin Lott",
          "cluster_id": 779902,
          "cite": [
            "310 F.3d 1231",
            "2002 U.S. App. LEXIS 23050"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cervantes",
          "cluster_id": 2633363,
          "cite": [
            "29 P.3d 225",
            "111 Cal. Rptr. 2d 148",
            "26 Cal. 4th 860",
            "2001 Cal. Daily Op. Serv. 7469",
            "2001 Daily Journal DAR 9125",
            "2001 Cal. LEXIS 5597"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Blais",
          "cluster_id": 6577730,
          "cite": [
            "428 Mass. 294",
            "701 N.E.2d 314",
            "1998 Mass. LEXIS 547"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane1_negative"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neil v. Biggers",
          "cluster_id": 108639,
          "cite": [
            "34 L. Ed. 2d 401",
            "93 S. Ct. 375",
            "409 U.S. 188",
            "1972 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manson v. Brathwaite",
          "cluster_id": 109693,
          "cite": [
            "53 L. Ed. 2d 140",
            "97 S. Ct. 2243",
            "432 U.S. 98",
            "1977 U.S. LEXIS 116"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 111353,
          "cite": [
            "84 L. Ed. 2d 1",
            "105 S. Ct. 1038",
            "470 U.S. 1",
            "1985 U.S. LEXIS 49",
            "53 U.S.L.W. 4159"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Florida",
          "cluster_id": 108186,
          "cite": [
            "26 L. Ed. 2d 446",
            "90 S. Ct. 1893",
            "399 U.S. 78",
            "1970 U.S. LEXIS 98",
            "53 Ohio Op. 2d 55"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nobles",
          "cluster_id": 109292,
          "cite": [
            "45 L. Ed. 2d 141",
            "95 S. Ct. 2160",
            "422 U.S. 225",
            "1975 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
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
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dionisio",
          "cluster_id": 108709,
          "cite": [
            "35 L. Ed. 2d 67",
            "93 S. Ct. 764",
            "410 U.S. 1",
            "1973 U.S. LEXIS 110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 2411822,
          "cite": [
            "839 S.W.2d 54",
            "1992 Tenn. LEXIS 348"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andresen v. Maryland",
          "cluster_id": 109522,
          "cite": [
            "49 L. Ed. 2d 627",
            "96 S. Ct. 2737",
            "427 U.S. 463",
            "1976 U.S. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desist v. United States",
          "cluster_id": 107875,
          "cite": [
            "22 L. Ed. 2d 248",
            "89 S. Ct. 1030",
            "394 U.S. 244",
            "1969 U.S. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harper v. Virginia Department of Taxation",
          "cluster_id": 112890,
          "cite": [
            "125 L. Ed. 2d 74",
            "113 S. Ct. 2510",
            "509 U.S. 86",
            "1993 U.S. LEXIS 4212",
            "7 Fla. L. Weekly Fed. S 456",
            "16 Employee Benefits Cas. (BNA) 2313",
            "93 Daily Journal DAR 7730",
            "93 Cal. Daily Op. Serv. 4491",
            "61 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. State",
          "cluster_id": 1577216,
          "cite": [
            "790 S.W.2d 568",
            "1989 Tex. Crim. App. LEXIS 151",
            "1989 WL 69709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gouveia",
          "cluster_id": 111193,
          "cite": [
            "81 L. Ed. 2d 146",
            "104 S. Ct. 2292",
            "467 U.S. 180",
            "1984 U.S. LEXIS 91",
            "52 U.S.L.W. 4659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gilbert v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107487 OR 9423477 OR 9423478 OR 9423479 OR 9423480 OR 9423481) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OTgxMjgwMDAwMDAmcz0xNTM1MTQyJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107487+OR+9423477+OR+9423478+OR+9423479+OR+9423480+OR+9423481%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(107487 OR 9423477 OR 9423478 OR 9423479 OR 9423480 OR 9423481)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01Nzcmcz0xMDgzMDMmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107487+OR+9423477+OR+9423478+OR+9423479+OR+9423480+OR+9423481%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107487 OR 9423477 OR 9423478 OR 9423479 OR 9423480 OR 9423481)",
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
    "complete_query": "cites:(107487 OR 9423477 OR 9423478 OR 9423479 OR 9423480 OR 9423481)",
    "indexed_citing_opinions": 2609,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107487,
        "count": 2461,
        "count_source": "search"
      },
      {
        "opinion_id": 9423477,
        "count": 235,
        "count_source": "search"
      },
      {
        "opinion_id": 9423478,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423479,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423480,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423481,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3797,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gilbert-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY4MzA0Nzgmcz0xMDM2NzQ0NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107487+OR+9423477+OR+9423478+OR+9423479+OR+9423480+OR+9423481%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107487,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 105440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 105859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107342,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 273233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 1160583,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 1193668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 1421049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 1801408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107487,
        "cited_id": 2611155,
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
    "date_created": "2026-07-05T05:31:03Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:35:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:31:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gilbert v. California

```
<div>
<center><b><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U.S. 263</a></span> (1967)</b></center>
<center><h1>GILBERT<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 223.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 15-16, 1967.</center>
<center>Decided June 12, 1967.</center>
CERTIORARI TO THE SUPREME COURT OF CALIFORNIA.
<p><span class="star-pagination">*264</span> <i>Luke McKissack</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Norman H. Sokolow,</i> Deputy Attorney General of California, and <i>William E. James,</i> Assistant Attorney General, argued the cause for respondent. With them on the brief was <i>Thomas C. Lynch,</i> Attorney General.</p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>This case was argued with <i>United States</i> v. <i>Wade, ante,</i> p. 218, and presents the same alleged constitutional error in the admission in evidence of in-court identifications there considered. In addition, petitioner alleges constitutional <span class="star-pagination">*265</span> errors in the admission in evidence of testimony of some of the witnesses that they also identified him at the lineup, in the admission of handwriting exemplars taken from him after his arrest, and in the admission of out-of-court statements by King, a co-defendant, mentioning petitioner's part in the crimes. which statements, on the co-defendant's appeal decided with petitioner's, were held to have been improperly admitted against the co-defendant. Finally, he alleges that his Fourth Amendment rights were violated by a police seizure of photographs of him from his locked apartment after entry without a search warrant, and the admission of testimony of witnesses that they identified him from those photographs within hours after the crime.</p>
<p>Petitioner was convicted in the Superior Court of California of the armed robbery of the Mutual Savings and Loan Association of Alhambra and the murder of a police officer who entered during the course of the robbery. There were separate guilt and penalty stages of the trial before the same jury, which rendered a guilty verdict and imposed the death penalty. The California Supreme Court affirmed, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">63 Cal. 2d 690</a></span>, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">408 P. 2d 365</a></span>. We granted certiorari, <span class="citation" data-id="107279"><a href="/opinion/107279/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">384 U. S. 985</a></span>, and set the case for argument with <i>Wade</i> and with <i>Stovall</i> v. <i>Denno, post,</i> p. 293. If our holding today in <i>Wade</i> is applied to this case, the issue whether admission of the in-court and lineup identifications is constitutional error which requires a new trial could be resolved on this record only after further proceedings in the California courts. We must therefore first determine whether petitioner's other contentions warrant any greater relief.</p>
<p></p>
<h2>I.</h2>
<p></p>
<h2>THE HANDWRITING EXEMPLARS.</h2>
<p>Petitioner was arrested in Philadelphia by an FBI agent and refused to answer questions about the Alhambra <span class="star-pagination">*266</span> robbery without the advice of counsel. He later did answer questions of another agent about some Philadelphia robberies in which the robber used a handwritten note demanding that money be handed over to him, and during that interrogation gave the agent the handwriting exemplars. They were admitted in evidence at trial over objection that they were obtained in violation of petitioner's Fifth and Sixth Amendment rights. The California Supreme Court upheld admission of the exemplars on the sole ground that petitioner had waived any rights that he might have had not to furnish them. "[The agent] did not tell Gilbert that the exemplars would not be used in any other investigation. Thus, even if Gilbert believed that his exemplars would not be used in California, it does not appear that the authorities improperly induced such belief." <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#708" aria-description="Citation for case: People v. Gilbert">63 Cal. 2d, at 708</a></span>. <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#376" aria-description="Citation for case: People v. Gilbert">408 P. 2d, at 376</a></span>. The court did not, therefore, decide petitioner's constitutional claims.</p>
<p>We pass the question of waiver since we conclude that the taking of the exemplars violated none of petitioner's constitutional rights.</p>
<p><i>First.</i> The taking of the exemplars did not violate petitioner's Fifth Amendment privilege against self-incrimination. The privilege reaches only compulsion of "an accused's communications, whatever form they might take, and the compulsion of responses which are also communications, for example, compliance with a subpoena to produce one's papers," and not "compulsion which makes a suspect or accused the source of `real or physical evidence' . . . ." <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#763" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 763-764</a></span>. One's voice and handwriting are, of course, means of communication. It by no means follows, however, that every compulsion of an accused to use his voice or write compels a communication within the cover of the privilege. A mere handwriting exemplar, in contrast to the content of what is <span class="star-pagination">*267</span> written, like the voice or body itself, is an identifying physical characteristic outside its protection. <i>United States</i> v. <i>Wade, supra</i><i>,</i> at 222-223. No claim is made that the content of the exemplars was testimonial or communicative matter. Cf. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>.</p>
<p><i>Second.</i> The taking of the exemplars was not a "critical" stage of the criminal proceedings entitling petitioner to the assistance of counsel. Putting aside the fact that the exemplars were taken before the indictment and appointment of counsel, there is minimal risk that the absence of counsel might derogate from his right to a fair trial. Cf. <i>United States</i> v. <i>Wade, supra</i><i>.</i> If, for some reason, an unrepresentative exemplar is taken, this can be brought out and corrected through the adversary process at trial since the accused can make an unlimited number of additional exemplars for analysis and comparison by government and defense handwriting experts. Thus, "the accused has the opportunity for a meaningful confrontation of the [State's] case at trial through the ordinary processes of cross-examination of the [State's] expert [handwriting] witnesses and the presentation of the evidence of his own [handwriting] experts." <i>United States</i> v. <i>Wade, supra</i><i>,</i> at 227-228.</p>
<p></p>
<h2>II.</h2>
<p></p>
<h2>ADMISSION OF CO-DEFENDANT'S STATEMENTS.</h2>
<p>Petitioner contends that he was denied due process of law by the admission during the guilt stage of the trial of his accomplice's pretrial statements to the police which referred to petitioner 159 times in the course of reciting petitioner's role in the robbery and murder. The statements were inadmissible hearsay as to petitioner, and were held on King's aspect of this appeal to be improperly obtained from him and therefore to be inadmissible against him under California law. <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#699" aria-description="Citation for case: People v. Gilbert">63 Cal. 2d, at 699-701</a></span>, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#370" aria-description="Citation for case: People v. Gilbert">408 P. 2d, at 370-371</a></span>.</p>
<p><span class="star-pagination">*268</span> Petitioner would have us reconsider <i>Delli Paoli</i> v. <i>United States,</i> <span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">352 U. S. 232</a></span> (where the Court held that appropriate instructions to the jury would suffice to prevent prejudice to a defendant from the references to him in a co-defendant's statement), at least as applied to a case, as here, where the co-defendant gained a reversal because of the improper admission of the statements. We have no occasion to pass upon this contention. The California Supreme Court has rejected the <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> rationale, and relying at least in part on the reasoning of the <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> dissent, regards cautionary instructions as inadequate to cure prejudice. <i>People</i> v. <i>Aranda,</i> <span class="citation" data-id="9542298"><a href="/opinion/1160583/people-v-aranda/" aria-description="Citation for case: People v. Aranda">63 Cal. 2d 518</a></span>, <span class="citation" data-id="9542298"><a href="/opinion/1160583/people-v-aranda/" aria-description="Citation for case: People v. Aranda">407 P. 2d 265</a></span>. The California court applied <i><span class="citation" data-id="9542298"><a href="/opinion/1160583/people-v-aranda/" aria-description="Citation for case: People v. Aranda">Aranda</a></span></i> in this case but held that any error as to Gilbert in the admission of King's statements was harmless. The harmless-error standard applied was that "there is no reasonable possibility that the error in admitting King's statements and testimony might have contributed to Gilbert's conviction," a standard derived by the court from our decision in <i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85</a></span>.<sup>[1]</sup><i>Fahy</i> was the basis of our holding in <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>, and the standard applied by the California court satisfies the standard as defined in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>.</i></p>
<p>It may be that the California Supreme Court will review the application of its harmless-error standard to King's statements if on the remand the State presses harmless error also in the introduction of the in-court and lineup identifications. However, this at best implies an ultimate application of <i><span class="citation" data-id="9542298"><a href="/opinion/1160583/people-v-aranda/" aria-description="Citation for case: People v. Aranda">Aranda</a></span></i> and only confirms that petitioner's argument for reconsideration of <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> need not be considered at this time.</p>
<p></p>
<h2>
<span class="star-pagination">*269</span> III.</h2>
<p></p>
<h2>THE SEARCH-AND-SEIZURE CLAIM.</h2>
<p>The California Supreme Court rejected Gilbert's challenge to the admission of certain photographs taken from his apartment pursuant to a warrantless search. The court justified the entry into the apartment under the circumstances on the basis of so-called "hot pursuit" and "exigent circumstances" exceptions to the warrant requirement. We granted certiorari to consider the important question of the extent to which such exceptions may permit warrantless searches without violation of the Fourth Amendment. A closer examination of the record than was possible when certiorari was granted reveals that the facts do not appear with sufficient clarity to enable us to decide that question. See Appendix to this opinion; compare <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>. We therefore vacate certiorari on this issue as improvidently granted. <i>The Monrosa</i> v. <i>Carbon Black Export, Inc.,</i> <span class="citation" data-id="9421781"><a href="/opinion/105859/the-monrosa-v-carbon-black-export-inc/#184" aria-description="Citation for case: The Monrosa v. Carbon Black Export, Inc.">359 U. S. 180, 184</a></span>.</p>
<p></p>
<h2>IV.</h2>
<p></p>
<h2>THE IN-COURT AND LINEUP IDENTIFICATIONS.</h2>
<p>Since none of the petitioner's other contentions warrants relief, the issue becomes what relief is required by application to this case of the principles today announced in <i>United States</i> v. <i>Wade, supra</i><i>.</i></p>
<p>Three eyewitnesses to the Alhambra crimes who identified Gilbert at the guilt stage of the trial had observed him at a lineup conducted without notice to his counsel in a Los Angeles auditorium 16 days after his indictment and after appointment of counsel. The manager of the apartment house in which incriminating evidence was found, and in which Gilbert allegedly resided, identified Gilbert in the courtroom and also testified, in substance, to her prior lineup identification on examination by the <span class="star-pagination">*270</span> State. Eight witnesses who identified him in the courtroom at the penalty stage were not eyewitnesses to the Alhambra crimes but to other robberies allegedly committed by him. In addition to their in-court identifications, these witnesses also testified that they identified Gilbert at the same lineup.</p>
<p>The lineup was on a stage behind bright lights which prevented those in the line from seeing the audience. Upwards of 100 persons were in the audience, each an eyewitness to one of the several robberies charged to Gilbert. The record is otherwise virtually silent as to what occurred at the lineup.<sup>[2]</sup></p>
<p><span class="star-pagination">*271</span> At the guilt stage, after the first witness, a cashier of the savings and loan association, identified Gilbert in the courtroom, defense counsel moved, out of the presence of the jury, to strike her testimony on the ground that she identified Gilbert at the pretrial lineup conducted in the absence of counsel in violation of the Sixth Amendment made applicable to the States by the Fourteenth Amendment. <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>. He requested a hearing outside the presence of the jury to present evidence supporting his claim that her in-court identification was, and others to be elicited by the State from other eyewitnesses would be, "predicated at least in large part upon their identification or purported identification of Mr. Gilbert at the showup . . . ." The trial judge denied the motion as premature. Defense counsel then elicited the fact of the cashier's lineup identification on cross-examination and again moved to strike her identification testimony. Without passing on the merits of the Sixth Amendment claim, the trial judge denied the motion on the ground that, assuming a violation, it would not in any event entitle Gilbert to suppression of the in-court identification. Defense counsel thereafter elicited the fact of lineup identifications from two other eyewitnesses who on direct examination identified Gilbert in the courtroom. Defense counsel unsuccessfully objected at the penalty stage, to the testimony of the eight witnesses to the other robberies that they identified Gilbert at the lineup.</p>
<p><span class="star-pagination">*272</span> The admission of the in-court identifications without first determining that they were not tainted by the illegal lineup but were of independent origin was constitutional error. <i>United States</i> v. <i>Wade, supra</i><i>.</i> We there held that a post-indictment pretrial lineup at which the accused is exhibited to identifying witnesses is a critical stage of the criminal prosecution; that police conduct of such a lineup without notice to and in the absence of his counsel denies the accused his Sixth Amendment right to counsel and calls in question the admissibility at trial of the in-court identifications of the accused by witnesses who attended the lineup. However, as in <i>Wade,</i> the record does not permit an informed judgment whether the in-court identifications at the two stages of the trial had an independent source. Gilbert is therefore entitled only to a vacation of his conviction pending the holding of such proceedings as the California Supreme Court may deem appropriate to afford the State the opportunity to establish that the in-court identifications had an independent source, or that their introduction in evidence was in any event harmless error.</p>
<p>Quite different considerations are involved as to the admission of the testimony of the manager of the apartment house at the guilt phase and of the eight witnesses at the penalty stage that they identified Gilbert at the lineup.<sup>[3]</sup> That testimony is the direct result of the illegal <span class="star-pagination">*273</span> lineup "come at by exploitation of [the primary] illegality." <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 488</a></span>. The State is therefore not entitled to an opportunity to show that that testimony had an independent source. Only a <i>per se</i> exclusionary rule as to such testimony can be an effective sanction to assure that law enforcement authorities will respect the accused's constitutional right to the presence of his counsel at the critical lineup. In the absence of legislative regulations adequate to avoid the hazards to a fair trial which in-here in lineups as presently conducted, the desirability of deterring the constitutionally objectionable practice must prevail over the undesirability of excluding relevant evidence. Cf. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. That conclusion is buttressed by the consideration that the witness' testimony of his lineup identification will enhance the impact of his in-court identification on the jury and <span class="star-pagination">*274</span> seriously aggravate whatever derogation exists of the accused's right to a fair trial. Therefore, unless the California Supreme Court is "able to declare a belief that it was harmless beyond a reasonable doubt," <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 24</a></span>, Gilbert will be entitled on remand to a new trial or, if no prejudicial error is found on the guilt stage but only in the penalty stage, to whatever relief California law affords where the penalty stage must be set aside.</p>
<p>The judgment of the California Supreme Court and the conviction are vacated, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>THE CHIEF JUSTICE joins this opinion except for Part III, from which he dissents for the reasons expressed in the opinion of MR. JUSTICE DOUGLAS.</p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT.</h2>
<p>Photographs of Gilbert introduced at the guilt stage of the trial had been viewed by eyewitnesses within hours after the robbery and murder. Officers had entered his apartment without a warrant and found them in an envelope on the top of a bedroom dresser. The envelope was of the kind customarily used in delivering developed prints, with the words "Marlboro Photo Studio" imprinted on it. The officers entered the apartment because of information given by an accomplice which led them to believe that one of the suspects might be inside the apartment. Assuming that the warrantless entry into the apartment was justified by the need immediately to search for the suspect, the issue remains whether the subsequent search was reasonably supported by those same exigent circumstances. If the envelope <span class="star-pagination">*275</span> were come upon in the course of a search for the suspect, the answer might be different from that where it is come upon, even though in plain view, in the course of a general, indiscriminate search of closets, dressers, etc., after it is known that the occupant is absent. Still different considerations may be presented where officers, pursuing the suspect, find that he is absent from the apartment but conduct a limited search for suspicious objects in plain view which might aid in the pursuit. The problem with the record in the present case is that it could reasonably support any of these factual conclusions upon which our constitutional analysis should rest, and the trial court made no findings on the scope of search. The California Supreme Court, which had no more substantial basis upon which to resolve the conflict than this Court, stated that the photos were come upon "while the officers were looking through the apartment for their suspect . . . ." As will appear, a contrary conclusion is equally reasonable.</p>
<p>(1) Agent Schlatter testified that immediately upon entering the apartment which he put at "approximately 1:05," the officers made a quick search for the occupant, which took at most a minute, and that the continued presence of the officers became "a matter of a stake-out under the assumption that the person or persons involved would come back." He testified that the officer who found the photographs, Agent Crowley, had entered the apartment with him. Agent Schlatter's testimony might support the California Supreme Court's view of the scope of search; (2) Agent Crowley testified that he arrived within five minutes <i>after</i> Agent Schlatter, "around 1:30, give or take a few minutes either way," that the apartment had already been searched for the suspects, and that he was instructed "to look through the apartment for anything we could find that we could use to identify or continue the pursuit of this person <span class="star-pagination">*276</span> without conducting a detailed search." Crowley's further testimony was that the search, pursuant to which the photos were found, was limited in this manner, and that he merely inspected objects in plain sight which would aid in identification. He stated that a detailed search for guns and money was not conducted until after a warrant had issued over three hours later. (3) Agent Townsend said he arrived at the apartment "sometime between perhaps 1:30 and 2:00," and that "well within an hour" he, Agent Crowley, another agent and a local officer conducted a detailed search of the bedroom. He stated that they "looked through the bedroom closet and dresser and I think . . . the headstand." A substantial sum of money was found in the dresser. Townsend could not "specifically say" whether Crowley was in the bedroom at the time the money was found. This testimony might support a finding that the officers were engaged in a general search of the bedroom at the time the photos were found.</p>
<p>The testimony of the agents concerning their time of arrival in the apartment is not inconsistent with any of the three possible conclusions as to the scope of search. Taking Townsend's testimony together with Crowley's, it can be concluded that the two arrived at about the same time. Agent Schlatter's testimony that Crowley arrived with him at 1:05, however, supports a conclusion that Crowley had begun his activities before Townsend arrived. Then there is the testimony of Agent Kiel, who did not enter the apartment, that he obtained the photos while talking with the landlady "approximately 1:25 to 1:30," about the same time that both Crowley and Townsend testified they arrived. In sum, the testimony concerning the timing of the events surrounding the search is both approximate and itself contradictory.</p>
<p><span class="star-pagination">*277</span> MR. JUSTICE BLACK, concurring in part and dissenting in part.</p>
<p>Petitioner was convicted of robbery and murder partially on the basis of handwriting samples he had given to the police while he was in custody without counsel and partially on evidence that he had been identified by eyewitnesses at a lineup identification ceremony held by California officers in a Los Angeles auditorium without notice to his counsel. The Court's opinion shows that the officers took Gilbert to the auditorium while he was a prisoner, formed a lineup of Gilbert and other persons, required each one to step forward, asked them certain questions, and required them to repeat certain phrases, while eyewitnesses to this and other crimes looked at them in efforts to identify them as the criminals. At his trial, Gilbert objected to the handwriting samples and to the identification testimony given by witnesses who saw him at the auditorium lineup on the ground that the admission of this evidence would violate his Fifth Amendment privilege against self-incrimination and Sixth Amendment right to counsel. It is well-established now that the Fourteenth Amendment makes both the Self Incrimination Clause of the Fifth Amendment and the Right to Counsel Clause of the Sixth Amendment obligatory on the States. See, <i>e. g., </i><i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span>; <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>.</p>
<p></p>
<h2>I.</h2>
<p>(a) Relying on <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>, the Court rejects Gilbert's Fifth Amendment contention as to both the handwriting exemplars and the lineup identification. I dissent from that holding. For reasons set out in my separate opinion in <i>United State</i> v. <i>Wade, ante,</i> p. 243, as well as in my dissent to <i>Schmerber,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#773" aria-description="Citation for case: Schmerber v. California">384 U. S., at 773</a></span>, I think that case wholly unjustifiably detracts from the protection against compelled self-incrimination <span class="star-pagination">*278</span> the Fifth Amendment was designed to afford. It rests on the ground that compelling a suspect to submit to or engage in conduct the sole purpose of which is to supply evidence against himself nonetheless does not compel him to be a witness against himself. Compelling a suspect or an accused to be "the source of `real or physical evidence' . . . ," so says <i>Schmerber,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California">384 U. S., at 764</a></span>, is not compelling him to be a witness against himself. Such an artificial distinction between things that are in reality the same is in my judgment wholly out of line with the liberal construction which should always be given to the Bill of Rights. See <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>.</p>
<p>(b) The Court rejects Gilbert's right-to-counsel contention in connection with the handwriting exemplars on the ground that the taking of the exemplars "was not a `critical' stage of the criminal proceedings entitling petitioner to the assistance of counsel." In all reality, however, it was one of the most "critical" stages of the government proceedings that ended in Gilbert's conviction. As to both the State's case and Gilbert's defense, the handwriting exemplars were just as important as the lineup and perhaps more so, for handwriting analysis, being, as the Court notes, "scientific" and "systematized," <i>United States</i> v. <i>Wade, ante,</i> at 227, may carry much more weight with the jury than any kind of lineup identification. The Court, however, suggests that absence of counsel when handwriting exemplars are obtained will not impair the right of cross-examination at trial. But just as nothing said in our previous opinions "links the right to counsel only to protection of Fifth Amendment rights." <i>United States</i> v. <i>Wade, ante,</i> at 226, nothing has been said which justifies linking the right to counsel only to the protection of other Sixth Amendment rights. And there is nothing in the Constitution to justify considering the right to counsel as a second-class, <span class="star-pagination">*279</span> subsidiary right which attaches only when the Court deems other specific rights in jeopardy. The real basis for the Court's holding that the stage of obtaining handwriting exemplars is not "critical," is its statement that "there is minimal risk that the absence of counsel might derogate from his right to a fair trial." The Court considers the "right to a fair trial" to be the overriding "aim of the right to counsel," <i>United States</i> v. <i>Wade, ante,</i> at 226, and somehow believes that this Court has the power to balance away the constitutional guarantee of right to counsel when the Court believes it unnecessary to provide what the Court considers a "fair trial." But I think this Court lacks constitutional power thus to balance away a defendant's absolute right to counsel which the Sixth and Fourteenth Amendments guarantee him. The Framers did not declare in the Sixth Amendment that a defendant is entitled to a "fair trial," nor that he is entitled to counsel on the condition that this Court thinks there is more than a "minimal risk" that without a lawyer his trial will be "unfair." The Sixth Amendment settled that a trial without a lawyer is constitutionally unfair, unless the court-created balancing formula has somehow changed it. <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span>, and <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, I thought finally established the right of an accused to counsel without balancing of any kind.</p>
<p>The Court's holding here illustrates the danger to Bill of Rights guarantees in the use of words like a "fair trial" to take the place of the clearly specified safeguards of the Constitution. I think it far safer for constitutional rights for this Court to adhere to constitutional language like "the accused shall . . . have the Assistance of Counsel for his defence" instead of substituting the words not mentioned, "the accused shall have the assistance of counsel only if the Supreme Court thinks it necessary to assure a fair trial." In my judgment the guarantees <span class="star-pagination">*280</span> of the Constitution with its Bill of Rights provide the kind of "fair trial" the Framers sought to protect. Gilbert was entitled to have the "assistance of counsel" when he was forced to supply evidence for the Government to use against him at his trial. I would reverse the case for this reason also.</p>
<p></p>
<h2>II.</h2>
<p>I agree with the Court that Gilbert's case should not be reversed for state error in admitting the pretrial statements of an accomplice which referred to Gilbert. But instead of squarely rejecting petitioner's reliance on the dissent in <i>Delli Paoli</i> v. <i>United States,</i> <span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/#246" aria-description="Citation for case: Delli Paoli v. United States">352 U. S. 232, 246</a></span>, the Court avoids the issue by pointing to the fact that the California Supreme Court, even assuming the error to be a federal constitutional one, applied a harmless-error test which measures up to the one we subsequently enunciated in <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>. And the Court then goes on to suggest that the California Supreme Court may desire to reconsider whether that is so upon remand.</p>
<p>I think the Court should clearly indicate that neither <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> nor <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> has any relevance here. <i><span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/" aria-description="Citation for case: Delli Paoli v. United States">Delli Paoli</a></span></i> rested on the admissibility of evidence in federal, not state, courts. The introduction of evidence in state courts is exclusively governed by state law unless its introduction would violate some federal constitutional provision and there is no such federal provision here. See <i>Spencer</i> v. <i>Texas,</i> <span class="citation" data-id="9423324"><a href="/opinion/107342/spencer-v-texas/" aria-description="Citation for case: Spencer v. Texas">385 U. S. 554</a></span>. That being so, any error in admitting the accomplice's pretrial statements is only an error of state law, and <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> providing a federal constitutional harmless-error rule, has absolutely no relevance here. Instead of looking at the harmless-error test applied by the California Supreme Court in order to ascertain whether it comports with <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> I would make it clear that this Court is leaving to the <span class="star-pagination">*281</span> States their unbridled power to control their own state courts in the absence of conflicting federal constitutional provisions.</p>
<p></p>
<h2>III.</h2>
<p>One witness who identified Gilbert at the guilt stage of his trial and eight witnesses who identified him at the penalty stage testified on direct examination that they had identified him in the auditorium lineup. I agree with the Court that the admission of this testimony was constitutional error and that Gilbert is entitled to a new trial unless the state courts, applying <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> conclude that this error was harmless. However, these witnesses also identified Gilbert in the courtroom and two other witnesses at the guilt stage identified him solely in the courtroom. As to these, the Court holds that "[t]he admission of the in-court identifications without first determining that they were not tainted by the illegal lineup . . . was constitutional error." I dissent from this holding in this case and in <i>United States</i> v. <i>Wade, ante,</i> p. 243, for the reasons there given.</p>
<p>For the reasons here stated, I would vacate the judgment of the California Supreme Court and remand for consideration of whether the admission of the handwriting exemplars and the out-of-court lineup identification was harmless error.<sup>[*]</sup></p>
<p>MR. JUSTICE DOUGLAS, concurring in part and dissenting in part.</p>
<p>While I agree with the Court's opinion except for Part I,<sup>[]</sup> I would reverse and remand for a new trial on <span class="star-pagination">*282</span> the search and seizure point. The search of the petitioner's home is sought to be justified by the doctrine of "hot pursuit," even though the officers conducting the search knew that petitioner, the suspected criminal, was not at home.</p>
<p>At about 10:30 a. m. on January 3, 1964, a California bank was robbed by two armed men; a police officer was killed by one of the robbers. Another officer shot one of the robbers. Weaver, who was captured a few blocks from the scene of the crime. Weaver told the police that he had participated in the robbery and that a person known to him as "Skinny" Gilbert was his accomplice. He told the officers that Gilbert lived in Apartment 28 of "a Hawaiian sounding named apartment house" on Los Feliz Boulevard. This information was given to the Federal Bureau of Investigation and was broadcast to a field agent, Kiel, who was instructed to find the apartment. Kiel located the "Lanai," an apartment on Los Feliz Boulevard, at about 1 p. m., informed the radio control, and engaged the apartment manager in conversation. While they were talking, a man gave a key to the manager and told her that he was going to San Francisco for a few days. Agent Kiel learned from the manager that Flood, one of the two men who had rented Apartment 28 the previous day, was the man who had just turned in the key and left by the rear exit. The agent ran out into the alleyway but saw no one.</p>
<p>In the meantime, the federal officers learned from Weaver that Gilbert was registered under the name of Flood. They also learned that three men may have been involved in the robberythe two who entered the bank and a third driving the getaway car. About 1:10 p. m., additional federal agents arrived at the apartment, in response to Agent Kiel's radio summons. Kiel told them that the resident of Apartment 28 was a Robert Flood who had just left. The agents obtained a key from the <span class="star-pagination">*283</span> manager, entered the apartment and searched for a person or a hiding place for a person. They found no one. But they did find an envelope containing pictures of petitioner; the pictures were seized and shown to bank employees for identification. The agents also found a notebook containing a diagram of the area surrounding the bank, a clip from an automatic pistol, and a bag containing rolls of coins bearing the marking of the robbed bank. On the basis of this information, a search warrant was issued, and the automatic clip, notebook, and coin rolls were seized. Petitioner was arrested in Pennsylvania on February 26. The items seized during the search of his apartment were introduced in evidence at his trial for murder.</p>
<p>The California Supreme Court justified the search on the ground that the police were in hot pursuit of the suspected bank robbers. The entry of the apartment was lawful. The subsequent search and seizure was lawful since the officers were trying to further identify suspects and to facilitate continued pursuit. <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">63 Cal. 2d 690</a></span>, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">408 P. 2d 365</a></span>.</p>
<p>I have set forth the testimony relating to the search more fully in the Appendix to this opinion. For the reasons stated there, I cannot agree that "the facts do not appear with sufficient clarity to enable us to decide" the serious question presented.</p>
<p>Since the search and seizure took place without a warrant, it can stand only if it comes within one of the narrowly defined exceptions to the rule that a search and seizure must rest upon a validly executed search warrant. See, <i>e. g., </i><i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">357 U. S. 493</a></span>; <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261</a></span>; <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>. One of these exceptions is that officers having probable cause to arrest may enter a dwelling to make the arrest and conduct a contemporaneous <span class="star-pagination">*284</span> search of the place of arrest "in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody." <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>. This, of course, assumes that an arrest has been made, and that the search "is substantially contemporaneous with the arrest and is confined to the immediate vicinity of the arrest." <i>Stoner</i> v. <i>California, supra,</i> at 486. In this case, the exemption is not applicable since the arrest was made many days after the search and at a location far removed from the search.</p>
<p>Here, the officers entered the apartment, searched for petitioner and did not find him. Nevertheless, they continued searching the apartment and seized the pictures; the inescapable conclusion is that they were searching for evidence linking petitioner to the bank robbery, not for the suspected robbers. The court below said that, having legally entered the apartment, the officers "could properly look through the apartment for anything that could be used to identify the suspects or to expedite the pursuit." 63 Cal. 2d, at 707, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#375" aria-description="Citation for case: People v. Gilbert">408 P. 2d, at 375</a></span>.</p>
<p>Prior to this case, police could enter and search a house without a warrant only incidental to a valid arrest. If this judgment stands, the police can search a house for evidence, even though the suspect is not arrested. The purpose of the search is, in the words of the California Supreme Court, "limited to and incident to the purpose of the officers' entry"that is, to apprehend the suspected criminal. Under that doctrine, the police are given license to search for any evidence linking the home-owner with the crime. Certainly such evidence is well calculated "to identify the suspects," and will "expedite the pursuit" since the police can then concentrate on the person whose home has been ransacked. <i><span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/" aria-description="Citation for case: People v. Gilbert">Ibid.</a></span></i></p>
<p><span class="star-pagination">*285</span> The search and seizure in this case violates another limitation, which concededly the ill-starred decision in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, flouted, <i>viz.,</i> that a general search for evidence, even when the police are in "hot pursuit" or have a warrant of arrest, does not make constitutional a general search of a room or of a house (<i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#463" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 463-464</a></span>). If it did, then the police, acting without a search warrant, could search more extensively than when they have a warrant. For the warrant must, as prescribed by the Fourth Amendment, "particularly" describe the "things to be seized." As stated by the Court in <i>United States</i> v. <i><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz, supra,</a></span></i> at 464:</p>
<blockquote>"The authority of officers to search one's house or place of business contemporaneously with his lawful arrest therein upon a valid warrant of arrest certainly is not greater than that conferred by a search warrant issued upon adequate proof and sufficiently describing the premises and the things sought to be obtained. Indeed, the informed and deliberate determinations of magistrates empowered to issue warrants as to what searches and seizures are permissible under the Constitution are to be preferred over the hurried action of officers and others who may happen to make arrests. Security against unlawful searches is more likely to be attained by resort to search warrants than by reliance upon the caution and sagacity of petty officers while acting under the excitement that attends the capture of persons accused of crime."</blockquote>
<p>Indeed, if at the very start, there had been a search warrant authorizing the seizure of the automatic clip, notebook, and coin rolls, the envelope containing pictures of petitioner could not have been seized. "The requirement that warrants shall particularly describe the things <span class="star-pagination">*286</span> to be seized . . . prevents the seizure of one thing under a warrant describing another. As to what is to be taken, nothing is left to the discretion of the officer executing the warrant." <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span>.</p>
<p>The modern police technique of ransacking houses, even to the point of seizing their entire contents as was done in <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>, is a shocking departure from the philosophy of the Fourth Amendment. For the kind of search conducted here was indeed a general search. And if the Fourth Amendment was aimed at any particular target it was aimed at that. When we take that step, we resurrect one of the deepest-rooted complaints that gave rise to our Revolution. As the Court stated in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, 625:</p>
<blockquote>"The practice had obtained in the colonies of issuing writs of assistance to the revenue officers, empowering them, in their discretion, to search suspected places for smuggled goods, which James Otis pronounced `the worst instrument of arbitrary power, the most destructive of English liberty, and the fundamental principles of law, that ever was found in an English law book'; since they placed `the liberty of every man in the hands of every petty officer.' This was in February, 1761, in Boston, and the famous debate in which it occurred was perhaps the most prominent event which inaugurated the resistance of the colonies to the oppressions of the mother country. `Then and there,' said John Adams, `then and there was the first scene of the first act of opposition to the arbitrary claims of Great Britain. Then and there the child Independence was born.' "</blockquote>
<p>I would not allow the general search to reappear on the American scene.</p>
<p></p>
<h2>
<span class="star-pagination">*287</span> APPENDIX TO OPINION OF MR. JUSTICE DOUGLAS.</h2>
<p>As the Court notes, there is some confusion in the record respecting the timing of events surrounding the search and the breadth of purpose with which the search was conducted. The confusion results from the testimony of the agents involved.</p>
<p>Agent Kiel testified that Agents Schlatter and Onsgaard arrived at the apartment at about 1:10 and entered the apartment a minute or two after their arrival. Kiel received the photographs from Agent Schlatter between 1:25 and 1:30.</p>
<p>Agent Schlatter testified that he, Agent Onsgaard and some local police arrived at the apartment about 1:05 and that Agent Crowley and one or two local police officers arrived in another car at the same time. Schlatter briefly talked to Kiel and the apartment manager and then entered the apartment. Upon entering he saw no one. He "made a very fast search of the apartment for a person or a hiding place of a person and . . . found none." This search took "a matter of seconds or a minute at the outside" and "[a]fter we had searched for [a] person or persons, and no one was there, it then became a matter of a stake-out under the assumption that the person or persons involved would come back." It seemed to Schlatter that "an agent had [the photograph] in his hand," when he first saw it, that it "was in the hands of an agent or an officer," and Schlatter had "a vague recollection that [the agent or officer told him he had found it] in the bedroom . . . ." There were a number of photographs. Schlatter took the photographs out to Kiel and instructed him to take one of them to the savings and loan association and see if anyone there could recognize the photograph. Schlatter testified that he was in the apartment for about 30 minutes after making the search and left other agents behind when he left.</p>
<p><span class="star-pagination">*288</span> Agent Crowley testified that he entered the apartment "around 1:30, give or take a few minutes either way" and that he would say that the other officers had been in the apartment less than five minutes before he entered. He believed that "the officers and the other agent who had been with [him] at the rear of the building when the first entry was made, entered with [him]." When Crowley entered the apartment it "had already been searched for people." He received "instructions . . . to look through the apartment for anything we could find that we could use to identify or continue the pursuit of this person without conducting a detailed search." In the bedroom, on the dresser, Crowley saw an envelope bearing the name "Marlboro Photo Studio"; it appeared to him to be an envelope containing photos and he could see that there was something inside. Crowley opened the envelope and saw several copies of photographs. He discussed the matter with "Onsgaard who was in charge in the building and he instructed [Crowley] to give it to another agent for him to utilize in pursuing the investigation, and [he was] reasonably certain that that agent was Mr. Schlatter." This was about 1:30 according to Crowley. In the course of his search which turned up the photographs, Crowley "turned over [items] to see what was on the reverse, such as business cards, sales slips from local stores, that sort of item which might have been folded and would appear to possibly contain information of value to pursuit." He relayed the information obtained in this manner to the man coordinating the operation. Crowley remained in the apartment until the next morning.</p>
<p>Agent Townsend testified that he arrived at the apartment "[s]ometime between perhaps 1:30 and 2:00." Within an hour of his arrival, he began a search. Townsend testified that he, Agent Crowley, another agent and a local officer "looked through the bedroom closet and <span class="star-pagination">*289</span> the dresser and I think the headstand." This was after it was known that no one, other than agents and police officers, was in the apartment. Townsend stated that the agents and officers were "[i]n and out of the bedroom," that he found money in the bedroom dresser about an hour after he arrived in the apartment, and that he could not "say specifically" whether Crowley was there at that time.</p>
<p>Thus, there is some conflict regarding the times at which the events took place and with respect to the nature of the searches conducted by the various officers. The way I read the record, however, it is not in such a state "that the facts do not appear with sufficient clarity to enable us to decide" the question presented. Crowley's testimony that he came upon the photographs while searching "for anything . . . that we could use to identify or continue the pursuit" stands uncontradicted, as does his testimony that the apartment had already been searched for a person prior to his search uncovering the photographs. Schlatter's testimony that the operation "became a matter of a stake-out" after the unsuccessful search for a person does not contradict Crowley's testimony. A search for identifying evidence is certainly compatible with a "stake-out." And Crowley best knew what he was doing when he discovered the photographs. Nor does Townsend's testimony that he and others, perhaps including Crowley, conducted a detailed search conflict with Crowley's testimony. First, the record indicates that the detailed search was conducted after the photographs had been found. According to the testimony of Kiel and Schlatter, Schlatter gave the photographs to Kiel at about 1:30; according to Townsend, he arrived sometime between 1:30 and 2. Second, even if the detailed search took place before Crowley found the photographs and Crowley participated in that search, that does not indicate that Crowley's search which turned <span class="star-pagination">*290</span> up the photographs was more limited than Crowley claimed. If anything, it would indicate that his search was more general than he stated. Finally, Townsend's testimony as to the general search does not conflict with Schlatter's testimony that the operation became a "stake-out" after the suspect was not found. As I have said, a "stake-out" does not preclude a detailed search for evidence. And, the record indicates that Schlatter was not in the apartment when Townsend and the others conducted the detailed search.</p>
<p>The way I read the record, the photographs were discovered in the course of a general search for evidence. But even if Crowley is not believed and his testimony relating to the nature of his search is thrown out and it is simply assumed that he came upon the envelope in the course of a search for the suspect, there was no reason to pry into the envelope and seize the picturesother than to obtain evidence. An envelope would contain neither the suspect nor the weapon.</p>
<p>MR. JUSTICE WHITE, whom MR. JUSTICE HARLAN and MR. JUSTICE STEWART join, concurring in part and dissenting in part.</p>
<p>I concur in Parts I, II, and III of the Court's opinion, but for the reasons stated in my separate opinion in <i>United States</i> v. <i>Wade, ante,</i> p. 250, I dissent from Part IV of the Court's opinion and would therefore affirm the judgment of the Supreme Court of California.</p>
<p>MR. JUSTICE FORTAS, with whom THE CHIEF JUSTICE joins, concurring in part and dissenting in part.</p>
<p>I concur in the resultthe vacation of the judgment of the California Supreme Court and the remand of the casebut I do not believe that it is adequate. I would reverse and remand for a new trial on the additional ground that petitioner was entitled by the Sixth and <span class="star-pagination">*291</span> Fourteenth Amendments to be advised that he had a right to counsel before and in connection with his response to the prosecutor's demand for a handwriting exemplar.</p>
<p>1. The giving of a handwriting exemplar is a "critical stage" of the proceeding, as my Brother BLACK states. It is a "critical stage" as much as is a lineup. See <i>United States</i> v. <i>Wade, ante,</i> p. 218. Depending upon circumstances, both may be inoffensive to the Constitution, totally fair to the accused, and entirely reliable for the administration of justice. On the other hand, each may be constitutionally offensive, totally unfair to the accused, and prejudicial to the ascertainment of truth. An accused whose handwriting exemplar is sought needs counsel: Is he to write "Your money or your life?" Is he to emulate the holdup note by using red ink, brown paper, large letters, etc.? Is the demanded handwriting exemplar, in effect, an inculpationa confession? Cf. the eloquent arguments as to the need for counsel, in the Court's opinion in <i>United States</i> v. <i>Wade, supra</i><i>.</i></p>
<p>2. The Court today appears to hold that an accused may be compelled to give a handwriting exemplar. Cf. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966). Presumably, he may be punished if he adamantly refuses. Unlike blood, handwriting cannot be extracted by a doctor from an accused's veins while the accused is subjected to physical restraint, which <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> permits. So presumably, on the basis of the Court's decision, trial courts may hold an accused in contempt and keep him in jail indefinitelyuntil he gives a handwriting exemplar.</p>
<p>This decision goes beyond <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>.</i> Here the accused, in the absence of any warning that he has a right to counsel, is compelled to cooperate, not merely to submit; to engage in a volitional act, not merely to suffer the inevitable consequences of arrest and state custody; to take affirmative action which may not merely identify <span class="star-pagination">*292</span> him, but tie him directly to the crime. I dissented in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>.</i> For reasons stated in my separate opinion in <i>United States</i> v. <i>Wade, supra</i><i>,</i> I regard the extension of <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> as impermissible.</p>
<p>In <i>Wade,</i> the accused, who is compelled to utter the words used by the criminal in the heat of his act, has at least the comfort of counseleven if the Court denies that the accused may refuse to speak the wordsbecause the compelled utterance occurs in the course of a lineup. In the present case, the Court deprives him of even this source of comfort and whatever protection counsel's ingenuity could provide in face of the Court's opinion. This is utterly insupportable, in my respectful opinion. This is not like fingerprinting, measuring, photographing or even blood-taking. It is a process involving the use of discretion. It is capable of abuse. It is in the stream of inculpation. Cross-examination can play only a limited role in offsetting false inference or misleading coincidence from a "stacked" handwriting exemplar. The Court's reference to the efficacy of cross-examination in this situation is much more of a comfort to an appellate court than a source of solace to the defendant and his counsel.</p>
<p>3. I agree with the Court's condemnation of the lineup identifications here and the consequent in-court identifications, and I join in this part of its opinion. I would also reverse and remand for a new trial because of the use of the handwriting exemplars which were unconstitutionally obtained in the absence of advice to the accused as to the availability of counsel. I could not conclude that the violation of the privilege against self-incrimination implicit in the facts relating to the exemplars was waived in the absence of advice as to counsel. <i>In re Gault,</i> <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#41" aria-description="Citation for case: In Re GAULT">387 U. S. 1, 41-42</a></span> (1967); <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<h2>NOTES</h2>
<p>[1]  The California Supreme Court also held that ". . . the erroneous admission of King's statements at the trial on the issue of guilt was not prejudicial on the question of Gilbert's penalty," again citing <i>Fahy,</i> 63 Cal. 2d, at 702, <span class="citation" data-id="9626099"><a href="/opinion/1421049/people-v-gilbert/#372" aria-description="Citation for case: People v. Gilbert">408 P. 2d, at 372</a></span>.</p>
<p>[2]  The record in <i>Gilbert</i> v. <i>United States,</i> <span class="citation" data-id="9452205"><a href="/opinion/273233/jesse-james-gilbert-v-united-states/" aria-description="Citation for case: Jesse James Gilbert v. United States">366 F. 2d 923</a></span>, involving the federal prosecutions of Gilbert, apparently contains many more details of what occurred at the lineup. The opinion of the Court of Appeals for the Ninth Circuit states, <span class="citation" data-id="9452205"><a href="/opinion/273233/jesse-james-gilbert-v-united-states/" aria-description="Citation for case: Jesse James Gilbert v. United States">366 F. 2d, at 935</a></span>:
</p>
<p>"The lineup occurred on March 26, 1964, after Gilbert had been indicted and had obtained counsel. It was held in an auditorium used for that purpose by the Los Angeles police. Some ten to thirteen prisoners were placed on a lighted stage. The witnesses were assembled in a darkened portion of the room, facing the stage and separated from it by a screen. They could see the prisoners but could not be seen by them. State and federal officers were also present and one of them acted as `moderator' of the proceedings.</p>
<p>"Each man in the lineup was identified by number, but not by name. Each man was required to step forward into a marked circle, to turn, presenting both profiles as well as a face and back view, to walk, to put on or take off certain articles of clothing. When a man's number was called and he was directed to step into the circle, he was asked certain questions: where he was picked up, whether he owned a car, whether, when arrested, he was armed, where he lived. Each was also asked to repeat certain phrases, both in a loud and in a soft voice, phrases that witnesses to the crimes had heard the robbers use: `Freeze, this is a stickup; this is a holdup; empty your cash drawer; this is a heist; don't anybody move.'</p>
<p>"Either while the men were on the stage, or after they were taken from it, it is not clear which, the assembled witnesses were asked if there were any that they would like to see again, and told that if they had doubts, now was the time to resolve them. Several gave the numbers of men they wanted to see, including Gilbert's. While the other prisoners were no longer present, Gilbert and 2 or 3 others were again put through a similar procedure. Some of the witnesses asked that a particular prisoner say a particular phrase, or walk a particular way. After the lineup, the witnesses talked to each other; it is not clear that they did so during the lineup. They did, however, in each other's presence, call out the numbers of men they could identify."</p>
<p>[3]  There is a split among the States concerning the admissibility of prior extrajudicial identifications, as independent evidence of identity, both by the witness and third parties present at the prior identification. See <span class="citation no-link">71 ALR 2d 449</span>. It has been held that the prior identification is hearsay, and, when admitted through the testimony of the identifier, is merely a prior consistent statement. The recent trend, however, is to admit the prior identification under the exception that admits as substantive evidence a prior communication by a witness who is available for cross-examination at trial. See 5 ALR 2d Later Case Service 1225-1228. That is the California rule. In <i>People</i> v. <i>Gould,</i> <span class="citation" data-id="1801408"><a href="/opinion/1801408/people-v-gould/#626" aria-description="Citation for case: People v. Gould">54 Cal. 2d 621, 626</a></span>, <span class="citation" data-id="1801408"><a href="/opinion/1801408/people-v-gould/#867" aria-description="Citation for case: People v. Gould">354 P. 2d 865, 867</a></span>, the Court said:
</p>
<p>"Evidence of an extrajudicial identification is admissible, not only to corroborate an identification made at the trial (<i>People</i> v. <i>Slobodion,</i> <span class="citation" data-id="1193668"><a href="/opinion/1193668/people-v-slobodion/#560" aria-description="Citation for case: People v. Slobodion">31 Cal. 2d 555, 560</a></span> [<span class="citation" data-id="1193668"><a href="/opinion/1193668/people-v-slobodion/" aria-description="Citation for case: People v. Slobodion">191 P. 2d 1</a></span>]), but as independent evidence of identity. Unlike other testimony that cannot be corroborated by proof of prior consistent statements unless it is first impeached . . . evidence of an extrajudicial identification is admitted regardless of whether the testimonial identification is impeached, because the earlier identification has greater probative value than an identification made in the courtroom after the suggestions of others and the circumstances of the trial may have intervened to create a fancied recognition in the witness' mind. . . . The failure of the witness to repeat the extrajudicial identification in court does not destroy its probative value, for such failure may be explained by loss of memory or other circumstances. The extrajudicial identification tends to connect the defendant with the crime, and the principal danger of admitting hearsay evidence is not present since the witness is available at the trial for cross-examination."</p>
<p>New York deals with the subject in a statute. See N. Y. Code Crim. Proc. § 393-b.</p>
<p>[*]  The Court dismisses as improvidently granted the Fourth Amendment search-and-seizure question raised by Gilbert in this case. I dissent from this, because I would decide that question against Gilbert. However, since the Court refuses to decide that question, I see no reason for expressing my views at length.</p>
<p>[]  On that phase of the case I agree with MR. JUSTICE BLACK and MR. JUSTICE FORTAS.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Glossip v. Oklahoma.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Glossip v. Oklahoma"
type: case
citation: "604 U.S. 226 (2025)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2025
date_decided: 2025-02-25
docket: 22-7466
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2025-02-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Glossip v. Oklahoma
  varies_by_point: false
  scope_note: "Good law (2025). Applies Napue v. Illinois: the prosecution's knowing failure to correct a key witness's false testimony violated due process and warranted a new trial. Slip opinion subject to formal revision. Distinct from Glossip v. Gross, 576 U.S. 863 (2015) (lethal-injection protocol)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10776870/glossip-v-oklahoma/"
  cluster_id: 10776870
  opinion_id: 11243457
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Napue v. Illinois]]", "[[Giglio v. United States]]", "[[Brady v. Maryland]]", "[[United States v. Bagley]]", "[[Banks v. Dretke]]", "[[Mooney v. Holohan]]"]
aliases: []
tags: ["case", "brady", "giglio", "napue", "false-testimony", "prosecutorial-misconduct", "due-process", "capital", "2025"]
holding: "The prosecution's knowing failure to correct a key witness's false testimony (the State's only direct-evidence witness denied his bipolar diagnosis and lithium prescription) violated the Napue due-process duty to correct false testimony; because the witness's credibility was necessarily determinative, there was a reasonable likelihood the false testimony affected the verdict, entitling the defendant to a new trial."
lake:
  record_id: Glossip v. Oklahoma
  status: verified
  projected_at: 2026-07-06
---

# Glossip v. Oklahoma

*604 U.S. 226 (2025)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Richard Glossip was convicted and sentenced to death for allegedly paying Justin Sneed to beat Barry Van Treese to death at an Oklahoma motel Glossip managed. Sneed — who admitted he did the killing — was the only direct evidence linking Glossip to the murder. At trial Sneed denied that he had been prescribed lithium or seen a psychiatrist, testifying he received lithium after asking for cold medicine. Decades later the State disclosed boxes of withheld documents showing Sneed had been diagnosed with bipolar disorder and prescribed lithium by a jail psychiatrist, and that the prosecutor (Smothermon) knew this. Oklahoma's attorney general confessed error and asked the state court for a new trial, but the Oklahoma Court of Criminal Appeals (OCCA) denied relief, finding no *[[Napue v. Illinois|Napue]]* violation. The Supreme Court stayed Glossip's execution and granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
Whether the prosecution's failure to correct Sneed's false testimony about his psychiatric diagnosis and lithium prescription violated the due-process duty recognized in *[[Napue v. Illinois]]*, entitling Glossip to a new trial (and whether the Court had jurisdiction over the OCCA's procedural ruling).

## Rule
A prosecutor must correct testimony it knows to be false. Under [[Napue v. Illinois]], a conviction knowingly "obtained through use of false evidence" violates the Fourteenth Amendment's Due Process Clause; "[t]o establish a *Napue* violation, a defendant must show that the prosecution knowingly solicited false testimony or knowingly allowed it 'to go uncorrected when it appear[ed].'" — 604 U.S. 226 (slip op., at 16–17). ^pin-226

If shown, materiality is a forgiving, prosecution-burden standard: "a new trial is warranted so long as the false testimony 'may have had an effect on the outcome of the trial,' … that is, if it '"in any reasonable likelihood [could] have affected the judgment of the jury,"'" — *id.* (slip op., at 17) (quoting *Giglio v. United States*, 405 U.S. 150, 154 (1972), in turn quoting *[[Napue v. Illinois|Napue]]*, 360 U.S. at 271). ^pin-226b

False testimony "goes only to the credibility of the witness" can be material, for "[t]he jury's estimate of the truthfulness and reliability of a given witness may well be determinative of guilt or innocence." — *id.* (slip op., at 19) (quoting *Napue*, 360 U.S. at 269).

## Application
The Court first held it had jurisdiction: the OCCA's procedural bar was not an independent and adequate state ground because it turned on the antecedent federal-law ruling that there was no *[[Napue v. Illinois|Napue]]* error. On the merits, the record supported the attorney general's confession of error — Sneed's denial of his lithium prescription and psychiatric treatment was false, and the prosecution (which had access to Sneed's medical and competency records and whose notes referenced "lithium" and "Dr. Trumpet") knew it was false and let it stand. Materiality was clear because "Sneed's testimony was the only direct evidence of Glossip's guilt of capital murder," so "the jury's assessment of Sneed's credibility was necessarily determinative." Correcting the lie would have shown Sneed was willing to lie under oath and would have undercut the prosecution's portrayal of him as harmless, so there was a reasonable likelihood it would have affected the verdict. Additional misconduct (a sequestration violation, destroyed evidence, withheld statements) further undermined confidence in the verdict.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]. The prosecution's failure to correct Sneed's false testimony violated *[[Napue v. Illinois|Napue]]*, and because the Court had jurisdiction and the confession of error was amply supported, a new trial — not a remand for further evidentiary proceedings — was the appropriate remedy.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Sotomayor, J., joined by Roberts, C.J., and Kagan, Kavanaugh, and Jackson, JJ., and by Barrett, J., as to Part II; Barrett, J., concurring in part and dissenting in part; Thomas, J., joined by Alito, J., dissenting; Gorsuch, J., took no part). [[Reading and Citing Cases#slip-opinion|Slip opinion]] subject to formal revision before publication in the U.S. Reports.
- *Glossip* is the most recent SCOTUS application of the [[Napue v. Illinois]] / [[Giglio v. United States]] knowing-false-testimony rule, which descends from [[Mooney v. Holohan]] and runs alongside the [[Brady v. Maryland]] / [[United States v. Bagley]] / [[Banks v. Dretke]] disclosure line. No negative treatment.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Glossip v. Oklahoma*, 604 U.S. 226 (2025) — https://www.courtlistener.com/opinion/10339023/glossip-v-oklahoma/ — pinpoints: slip op., at 2, 16–17, 19 (CL stores the slip opinion "604 U.S. ___ (2025)," subject to formal revision; pins keyed to the official case-start page 226). Internal authorities pinpointed: *Napue*, 360 U.S. at 269, 271; *Giglio*, 405 U.S. at 154.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "283b829d7583a3c3", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Glossip v. Oklahoma"}, "payload": {"all": [{"cite": "604 U.S. 226", "page": "226", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "604"}], "display": "604 U.S. 226", "official": {"cite": "604 U.S. 226", "page": "226", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "604"}, "official_selection_present": true, "record_id": "Glossip v. Oklahoma"}}
{"assertion_id": "bcd2af82e521c981", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-226", "record_id": "Glossip v. Oklahoma"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-226", "pinpoint_status": "slip-only", "quote": "--- # Glossip v. Oklahoma *604 U.S. 226 (2025)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Richard Glossip was convicted and sentenced to death for allegedly paying Justin Sneed to beat Barry Van Treese to death at an Oklahoma motel Glossip managed. Sneed — who admitted he did the killing — was the only direct evidence linking Glossip to the murder. At trial Sneed denied that he had been prescribed lithium or seen a psychiatrist, testifying he received lithium after asking for cold medicine. Decades later the State disclosed boxes of withheld documents showing Sneed had been diagnosed with bipolar disorder and prescribed lithium by a jail psychiatrist, and that the prosecutor (Smothermon) knew this. Oklahoma's attorney general confessed error and asked the state court for a new trial, but the Oklahoma Court of Criminal Appeals (OCCA) denied relief, finding no *Napue* violation. The Supreme Court stayed Glossip's execution and granted certiorari. ## Issue Whether the prosecution's failure to correct Sneed's false testimony about his psychiatric diagnosis and lithium prescription violated the due-process duty recognized in *Napue v. Illinois*, entitling Glossip to a new trial (and whether the Court had jurisdiction over the OCCA's procedural ruling). ## Rule A prosecutor must correct testimony it knows to be false. Under [[Napue v. Illinois]], a conviction knowingly", "quote_fidelity": "mismatch", "record_id": "Glossip v. Oklahoma", "star_marker": null}}
{"assertion_id": "e03b94ed7a1ec698", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-226b", "record_id": "Glossip v. Oklahoma"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-226b", "pinpoint_status": "slip-only", "quote": "a new trial is warranted so long as the false testimony 'may have had an effect on the outcome of the trial,' … that is, if it '", "quote_fidelity": "mismatch", "record_id": "Glossip v. Oklahoma", "star_marker": null}}
{"assertion_id": "636666aed1ba86c4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Glossip v. Oklahoma"}, "payload": {"as_of_content": "2025-02-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Glossip v. Oklahoma", "scope_note": "Good law (2025). Applies Napue v. Illinois: the prosecution's knowing failure to correct a key witness's false testimony violated due process and warranted a new trial. Slip opinion subject to formal revision. Distinct from Glossip v. Gross, 576 U.S. 863 (2015) (lethal-injection protocol).", "varies_by_point": false}}
```

### lake record — Glossip v. Oklahoma

```json
{
  "schema_version": "s2.v1",
  "record_id": "Glossip v. Oklahoma",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Glossip v. Oklahoma",
    "case_name_short": "Glossip",
    "case_name_full": "",
    "input_case_name": "Glossip v. Oklahoma",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2025-02-25",
    "year": 2025,
    "docket": "22-7466",
    "cluster_id": 10776870,
    "lead_opinion_id": 11243457,
    "sibling_ids": [
      11243457
    ],
    "absolute_url": "/opinion/10776870/glossip-v-oklahoma/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 10339193,
        "score": 120,
        "case_name": "Glossip v. Oklahoma Revisions: 2/25/25"
      },
      {
        "cluster_id": 10339023,
        "score": 120,
        "case_name": "Glossip v. Oklahoma"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "604 U.S. 226",
      "volume": "604",
      "reporter": "U.S.",
      "page": "226",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "604 U.S. 226",
        "volume": "604",
        "reporter": "U.S.",
        "page": "226",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "604 U.S. 226",
    "official_selection": {
      "court_class": "scotus",
      "selected": "604 U.S. 226",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-226",
      "page": null,
      "quote": "--- # Glossip v. Oklahoma *604 U.S. 226 (2025)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Richard Glossip was convicted and sentenced to death for allegedly paying Justin Sneed to beat Barry Van Treese to death at an Oklahoma motel Glossip managed. Sneed \u2014 who admitted he did the killing \u2014 was the only direct evidence linking Glossip to the murder. At trial Sneed denied that he had been prescribed lithium or seen a psychiatrist, testifying he received lithium after asking for cold medicine. Decades later the State disclosed boxes of withheld documents showing Sneed had been diagnosed with bipolar disorder and prescribed lithium by a jail psychiatrist, and that the prosecutor (Smothermon) knew this. Oklahoma's attorney general confessed error and asked the state court for a new trial, but the Oklahoma Court of Criminal Appeals (OCCA) denied relief, finding no *Napue* violation. The Supreme Court stayed Glossip's execution and granted certiorari. ## Issue Whether the prosecution's failure to correct Sneed's false testimony about his psychiatric diagnosis and lithium prescription violated the due-process duty recognized in *Napue v. Illinois*, entitling Glossip to a new trial (and whether the Court had jurisdiction over the OCCA's procedural ruling). ## Rule A prosecutor must correct testimony it knows to be false. Under [[Napue v. Illinois]], a conviction knowingly",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-226b",
      "page": null,
      "quote": "a new trial is warranted so long as the false testimony 'may have had an effect on the outcome of the trial,' \u2026 that is, if it '",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2025-02-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Glossip v. Oklahoma",
    "varies_by_point": false,
    "scope_note": "Good law (2025). Applies Napue v. Illinois: the prosecution's knowing failure to correct a key witness's false testimony violated due process and warranted a new trial. Slip opinion subject to formal revision. Distinct from Glossip v. Gross, 576 U.S. 863 (2015) (lethal-injection protocol).",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11243457) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      },
      "lane2_top_cited": {
        "query": "cites:(11243457)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11243457)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(11243457)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11243457,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/glossip-v-oklahoma.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11243457,
        "cited_id": 103610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 108164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 112456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 121172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 145766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 1087618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 2581658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3183080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3803122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3805789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3817059,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3828772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 3835480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 4687472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5146505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5148027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5149077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5149899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 5515949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 6105120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 6496181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 6671986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 8413606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9323214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9373886,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9405083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9406339,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9416986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9420168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9422312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9422583,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9423348,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9426342,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9426498,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9428656,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9429592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9429915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9430189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9431798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9433091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9433120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9433984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9434187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9434809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9435084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9796753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9796834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9797364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9821185,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9823487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9841311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9841318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9842050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9842054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243457,
        "cited_id": 9842121,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T05:35:25Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:36:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Glossip v. Oklahoma (truncated)

```
                   PRELIMINARY PRINT

              Volume 604 U. S. Part 1
                             Pages 226–304




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                             February 25, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
226                     OCTOBER TERM, 2024

                                 Syllabus


                    GLOSSIP v. OKLAHOMA

      certiorari to the court of criminal appeals of
                         oklahoma
   No. 22–7466. Argued October 9, 2024—Decided February 25, 2025
In 1997, Justin Sneed beat Barry Van Treese to death with a baseball bat
  at an Oklahoma hotel owned by Van Treese and managed by petitioner
  Richard Glossip. Glossip initially made inconsistent statements to the
  police about Sneed's role in the murder, but he ultimately told police
  that Sneed admitted to killing Van Treese. Sneed later claimed Glossip
  had asked him to murder Van Treese because, among other things,
  Glossip had wanted to steal Van Treese's money. Glossip maintained
  his innocence and refused a plea deal that would have had him avoid the
  death penalty in return for testifying against Sneed. Sneed then testi-
  fed against Glossip at trial in exchange for avoiding the death penalty,
  and Sneed's testimony was the only direct evidence connecting Glossip
  to the murder. The jury convicted Glossip and sentenced him to death.
  The Oklahoma Court of Criminal Appeals (OCCA) overturned that con-
Page Proof Pending Publication
  viction because the defense had been ineffective in challenging Sneed's
  testimony and the remainder of the evidence only weakly corroborated
  Sneed's account. At the retrial, Sneed provided inconsistent testimony
  on potential motives for Glossip's murder. Sneed also denied that he
  had been prescribed lithium or seen a psychiatrist. After the defense
  established (through the State's medical examiner) that Van Treese had
  been attacked with a knife as well as a bat, Sneed testifed that he had
  repeatedly tried to stab Van Treese in the chest with a pocket knife.
  But Sneed had previously denied stabbing Van Treese both when ques-
  tioned by the police as well as at Glossip's frst trial. Glossip moved for
  a mistrial based on the prosecution's failure to notify the defense about
  Sneed's change in testimony, which the trial court denied after the
  prosecution disclaimed any knowledge about the change. Glossip was
  again convicted and sentenced to death, and a closely divided OCCA
  affrmed, holding that circumstantial evidence suggesting Glossip had
  mismanaged the hotel, combined with Glossip's concession that he had
  been dishonest in his initial statements after the murder, suffciently
  corroborated Sneed's testimony that he killed Van Treese at Glossip's
  direction.
     Glossip subsequently fled several unsuccessful habeas petitions.
  Concerns over the integrity of his conviction led a bipartisan group of
                       Cite as: 604 U. S. 226 (2025)                      227

                                  Syllabus

  Oklahoma legislators to commission an independent investigation by a
  law frm, Reed Smith. In June 2022, Reed Smith reported “grave
  doubt” about Glossip's conviction, citing factors such as the prosecution's
  deliberate destruction of key evidence and the false portrayal of Justin
  Sneed as a non-violent “puppet.” The State then disclosed seven boxes
  of previously withheld documents, including letters suggesting Sneed
  had considered recanting and a note from prosecutor Connie Smother-
  mon to Sneed's lawyer noting they should “get to” Sneed to discuss his
  problematic testimony about a knife found in Van Treese's room.
  Glossip fled for post-conviction relief based on this evidence and evi-
  dence revealed by Reed Smith. Glossip also argued that, during his
  second trial, Smothermon had interfered with Sneed's testimony about
  the knife in violation of the rule of sequestration, which prohibits wit-
  nesses from hearing each other's testimony. Oklahoma waived any pro-
  cedural defenses to Glossip's claims, and asked the OCCA to deny the
  claims on their merits. The OCCA denied Glossip's claims as procedur-
  ally barred and meritless.
     The State then discovered additional documents revealing that Sneed
  had been diagnosed with bipolar disorder and prescribed lithium, contra-
  dicting his trial testimony. The attorney general determined that

Page Proof Pending Publication
  Smothermon had knowingly elicited false testimony from Sneed and
  failed to correct it, violating Napue v. Illinois, 360 U. S. 264, which held
  that prosecutors have a constitutional obligation to correct false testi-
  mony. Glossip fled a successive petition for post-conviction relief,
  which the attorney general supported, conceding multiple errors that
  warranted a new trial. The OCCA denied the unopposed petition with-
  out a hearing, holding that Glossip's claims were procedurally barred
  under Oklahoma's Post-Conviction Procedures Act (PCPA), and further
  that the State's concession was not “based in law or fact” because it did
  not create a Napue error. This Court stayed Glossip's execution and
  granted certiorari.
Held:
    1. This Court has jurisdiction to review the OCCA's judgment. The
 independent and adequate state ground doctrine precludes the Court
 from considering a federal question if the state court's decision rests on
 an independent and adequate state-law ground. The OCCA's applica-
 tion of the PCPA was not such a ground, because the OCCA's decision
 to apply the PCPA depended on its antecedent rejection of the attorney
 general's confession of a Napue error, which was based solely on federal
 law. The OCCA held that the confession could not overcome the
 PCPA's limitations because it lacked a basis in law or fact, specifcally
 fnding no Napue error.
228                   GLOSSIP v. OKLAHOMA

                                Syllabus

    Oklahoma precedent confrms that the OCCA normally rejects an at-
 torney general's confession of error only after fnding it unsupported by
 law and the record. By making the application of the PCPA contingent
 on its determination that the attorney general's confession of federal
 constitutional error was baseless, the OCCA made the procedural bar
 dependent on an antecedent ruling on federal law. To the extent that
 the OCCA's reasoning on this point is insuffciently “clear from the face
 of the opinion,” the Court presumes reliance on federal law under Mich-
 igan v. Long, 463 U. S. 1032, 1040–1041. Pp. 242–246.
    2. The prosecution violated its constitutional obligation to correct
 false testimony. Pp. 246–258.
       (a) Under Napue, a conviction obtained through the knowing use
 of false evidence violates the Fourteenth Amendment's Due Process
 Clause. To establish a Napue violation, a defendant must show that
 the prosecution knowingly solicited or allowed false testimony to go
 uncorrected. If a violation is established, a new trial is warranted if
 the false testimony could in any reasonable likelihood have affected the
 jury's judgment; meaning, ordinarily, that the prosecution must estab-
 lish harmlessness beyond a reasonable doubt. United States v. Bagley,
 473 U. S. 667, 680, n. 9; Chapman v. California, 386 U. S. 18, 24. Here,
Page Proof Pending Publication
 Oklahoma's attorney general joins Glossip in asserting a Napue error,
 conceding that Sneed's testimony about his lithium prescription was
 false and that the prosecution knowingly failed to correct it. The rec-
 ord supports that confession of error. Evidence showed that Sneed was
 prescribed lithium to treat bipolar disorder, not after asking for cold
 medicine as he claimed at trial. The evidence likewise establishes that
 the prosecution knew Sneed's testimony was false. The prosecution al-
 most certainly had access to Sneed's medical fle through Sneed's compe-
 tency evaluation. And Smothermon's notes show that she had a pre-
 trial conversation with Sneed at which he mentioned “lithium” and “Dr.
 Trumpet.” The straightforward inference is that Smothermon was
 aware before trial that Sneed had received his lithium prescription from
 Dr. Trombka, a psychiatrist and the sole medical professional at the
 Oklahoma County jail authorized to prescribe lithium.
    Because Sneed's testimony was the only direct evidence of Glossip's
 guilt, the jury's assessment of Sneed's credibility was material and nec-
 essarily determinative. Correcting Sneed's lie would have undermined
 his credibility and revealed his willingness to lie under oath. The false
 testimony also bore on Glossip's guilt because evidence of Sneed's bipo-
 lar disorder, which could trigger impulsive violence when combined with
 his drug use, would have contradicted the prosecution's portrayal of
 Sneed as harmless without Glossip's infuence. Hence there is a reason-
                        Cite as: 604 U. S. 226 (2025)                      229

                                  Syllabus

  able likelihood that correcting Sneed's testimony would have affected
  the judgment of the jury. Napue, 360 U. S., at 271. Additional prose-
  cutorial misconduct, such as violating the rule of sequestration, destroy-
  ing evidence, and withholding witness statements, further undermines
  confdence in the verdict. Consequently, the prosecution's failure to
  correct Sneed's false testimony entitles Glossip to a new trial under
  Napue. Pp. 246–252.
       (b) The OCCA's contrary holding rests on a mistaken interpretation
  of Napue. The OCCA held that there was no violation because the
  defense was aware or should have been aware that Sneed was taking
  lithium. But Sneed's false testimony concerned the reasons for his pre-
  scription, not merely the fact that he had taken lithium. Moreover, the
  Due Process Clause imposes the duty to correct false testimony on the
  State, not the defense. The OCCA's holding that Sneed was likely in de-
  nial of his mental health disorders is beside the point; what matters is that
  the testimony was false and the prosecutor knowingly allowed it to stand.
     Additional arguments in support of the OCCA's position are unpersua-
  sive. Napue does not require that the false testimony itself must have
  directly affected the trial's outcome; Napue requires assessing whether
  the prosecutor's failure to correct the testimony could have contributed
  to the verdict. Also unpersuasive are arguments based on extra-record
Page Proof Pending Publication
  materials and insuffcient time spent interviewing the prosecutor.
     Because the attorney general's confession of error is supported by
  ample evidence, the Court declines to remand this case for further evi-
  dentiary proceedings. When the Court has jurisdiction, a new trial is
  the appropriate remedy for a violation of Napue. Pp. 252–258.
529 P. 3d 218, reversed and remanded.

   Sotomayor, J., delivered the opinion of the Court, in which Roberts,
C. J., and Kagan, Kavanaugh, and Jackson, JJ., joined, and in which
Barrett, J., joined as to Part II. Barrett, J., fled an opinion concur-
ring in part and dissenting in part, post, p. 258. Thomas, J., fled a dis-
senting opinion, in which Alito, J., joined, and in which Barrett, J.,
joined as to Parts IV–A–1, IV–A–2, and IV–A–3, post, p. 262. Gorsuch,
J., took no part in the consideration or decision of the case.

  Seth P. Waxman argued the cause for petitioner. With
him on the briefs were Catherine M. A. Carroll, Zaki
Anwar, Donald R. Knight, Amy P. Knight, John R. Mills,
and Joseph J. Perkovich.
  Paul D. Clement argued the cause for respondent under
this Court's Rule 12.6. With him on the briefs were Gentner
F. Drummond, Attorney General of Oklahoma, Garry M.
230                    GLOSSIP v. OKLAHOMA

                                 Syllabus

Gaskins II, Solicitor General, Matthew D. Rowen, and Jo-
seph J. DeMott.
  Christopher G. Michel, by invitation of the Court, 601 U. S.
1010, argued the cause and fled a brief as amicus curiae in
support of the judgment below. With him on the brief were
Rachel G. Frank, Alex Van Dyke, and Nicholas J. Caluda.*

  *Briefs of amici curiae urging reversal were fled for the District of
Columbia et al. by Brian L. Schwalb, Attorney General of the District
of Columbia, Caroline S. Van Zile, Solicitor General, Ashwin P. Phatak,
Principal Deputy Solicitor General, Graham E. Phillips, Deputy Solicitor
General, and Elissa R. Lowenthal, Assistant Attorney General, and by
the Attorneys General for their respective States as follows: Philip J.
Weiser of Colorado, Kwame Raoul of Illinois, Anthony G. Brown of Mary-
land, Andrea Joy Campbell of Massachusetts, Keith Ellison of Minnesota,
Aaron D. Ford of Nevada, Matthew J. Platkin of New Jersey, Raúl Torrez
of New Mexico, Letitia James of New York, and Ellen F. Rosenblum of
Oregon; for the American Civil Liberties Union et al. by William R.
Weaver, David D. Cole, Brian W. Stull, Randy Alan Bauman, and Megan
Page Proof Pending Publication
Lambert; for Former Members of the Oklahoma Death Penalty Review
Commission by Carter G. Phillips, Virginia A. Seitz, and Jacqueline G.
Cooper; for the Innocence Project by Andrianna D. Kastanek; for the
National Association of Criminal Defense Lawyers by Barbara E. Berg-
man and Hassan Ahmad; for R. Michael Cassidy et al. by Meaghan
VerGow, Joshua Revesz, and Bruce A. Green; for Kenneth T. Cuccinelli
II, by Emmet T. Flood; and for Rep. Kevin McDugle et al. by Gregory
G. Garre.
  Briefs of amici curiae were fled for the State of Texas by Ken Paxton,
Attorney General, Brent Webster, First Assistant Attorney General,
Aaron L. Nielson, Solicitor General, Philip A. Lionberger, Assistant
Solicitor General, and Matthew Ottoway and J. Andrew Mackenzie, Assist-
ant Attorneys General; for the State of Utah et al. by Sean D. Reyes,
Attorney General of Utah, Stanford E. Purser, Solicitor General, Andrew
F. Peterson, Deputy Solicitor General, and Ginger Jarvis and Mark C.
Field, Assistant Solicitors General, and by the Attorneys General for their
respective States as follows: Treg R. Taylor of Alaska, Tim Griffn of
Arkansas, Liz Murrill of Louisiana, Austin Knudsen of Montana, Alan
Wilson of South Carolina, and Jonathan Skrmetti of Tennessee; for the
Criminal Justice Legal Foundation by Kent S. Scheidegger; for Current
and Former State and Federal Prosecutors by David A. Senior and Ann
K. Tria; for Federal Courts Scholars by Melanie L. Bostwick, Thomas M.
                     Cite as: 604 U. S. 226 (2025)               231

                        Opinion of the Court

   Justice Sotomayor delivered the opinion of the Court.
   An Oklahoma jury convicted petitioner Richard Glossip of
paying Justin Sneed to murder Barry Van Treese and sen-
tenced him to death. At trial, Sneed admitted he beat Van
Treese to death, but testifed that Glossip had offered him
thousands of dollars to do so. Glossip confessed he helped
Sneed conceal his crime after the fact, but he denied any
involvement in the murder.
   Nearly two decades later, the State disclosed eight boxes
of previously withheld documents from Glossip's trial.
These documents show that Sneed suffered from bipolar dis-
order, which, combined with his known drug use, could have
caused impulsive outbursts of violence. They also estab-
lished, the State agrees, that a jail psychiatrist prescribed
Sneed lithium to treat that condition, and that the prosecu-
tion allowed Sneed falsely to testify at trial that he had
never seen a psychiatrist. Faced with that evidence, Okla-
homa's attorney general confessed error. Before the Okla-
Page Proof Pending Publication
homa Court of Criminal Appeals (OCCA), the State conceded
that the prosecution's failure to correct Sneed's testimony
violated Napue v. Illinois, 360 U. S. 264 (1959), which held
that prosecutors have a constitutional obligation to correct
false testimony. The attorney general accordingly asked
the court to grant Glossip a new trial. The OCCA declined
to grant relief because, it held, the State's concession was
not “based in law or fact.” 2023 OK CR 5, ¶25, 529 P. 3d
218, 226. Because the prosecution violated its obligations
under Napue, we reverse the judgment below and remand
the case for a new trial.
                              I
                                  A
  Barry Van Treese owned a Best Budget Inn in Tulsa and
in Oklahoma City. Richard Glossip managed the Oklahoma

Bondy, and Katherine M. Kopp; and for Derek Van Treese et al. by Paul
G. Cassell.
232                GLOSSIP v. OKLAHOMA

                      Opinion of the Court

City hotel and lived there with his girlfriend. In the sum-
mer of 1996, Justin Sneed and his stepbrother approached
Glossip and asked him about working for a room. 2 App.
648. Glossip agreed to let them stay in return for help with
maintenance and housekeeping. Sneed, however, had a his-
tory of violence, angry outbursts, and substance abuse that
included marijuana, methamphetamine, cocaine, and acid.
Id., at 700–701. When, on January 6, 1997, Van Treese vis-
ited the inn to collect cash deposits there, Sneed beat him to
death with a baseball bat. See 2007 OK CR 12, ¶¶4–5, 157
P. 3d 143, 147–148 (Glossip II).
   After killing Van Treese, Sneed evaded law enforcement
for several days. Police did promptly interview Glossip,
who told them that Sneed had knocked on his door that night
with a bump on his head “like somebody punched him.”
App. to Response to Petitioner's Succ. Application for Post-
Conviction Relief in No. PCD–2022–819, Tr. of Glossip Police
Page Proof Pending Publication
Interview 15 (Jan. 8, 1997). Glossip added that Sneed had
told him he slipped in the shower. Ibid. Glossip disclaimed
any knowledge of Van Treese's murder, but admitted that he
helped Sneed replace (from the outside) the broken window
of the room where Van Treese's body was later found. The
next day, offcers arrested Glossip in front of an attorney's
offce with approximately $1,700 in cash on him. 1 App. 291–
292. Glossip then admitted Sneed had told him “that he
killed Barry.” Tr. of Glossip Police Interview 10 (Jan. 9,
1997). When confronted with his prior inconsistent state-
ments about the murder and Van Treese's whereabouts,
Glossip said that he had been scared to tell the truth because
he feared his failure to notify the police immediately meant
he was “already involved in it.” Id., at 29–30.
   The State thereafter charged Sneed with capital murder
and Glossip as an accessory after the fact based on his inac-
curate statements to the police. Eventually, police located
and interviewed Sneed, who had $1,680 in bloody cash on
him. See 14 Tr. 18 (May 28, 2004); 15 Tr. 170 (June 1, 2004).
                   Cite as: 604 U. S. 226 (2025)           233

                      Opinion of the Court

The offcers told Sneed that before he “ma[de] up [his] mind
on anything” they wanted him “to hear some of the things”
they “[had] to say,” including that they did not think Sneed
had acted alone and that he should not “take the whole
thing” himself. 2 App. 645–646. “[E]verybody” was mak-
ing Sneed “the scapegoat in this,” they told him—especially
Glossip, who was “putting it on [him] the worst.” Id., at 655.
   Sneed initially responded to the offcers' prompts by at-
tempting to implicate his brother, ibid., but eventually said
that Glossip had wanted to steal Van Treese's money and
that Van Treese's death had been the result of a robbery
gone wrong. Id., at 655–660. Sneed described breaking
into Van Treese's room and beating him with a baseball bat
until he “fgured he was knocked out.” Id., at 665. Accord-
ing to Sneed, he then took Van Treese's car keys, stole an
envelope with approximately $4,000 in cash from his car, and
split the money with Glossip. Id., at 665–669. When off-
Page Proof Pending Publication
cers pressed him on the state of Van Treese's body, Sneed
asserted that, “[a]ctually,” Glossip had asked him to kill Van
Treese so that he “could run the motel without him being
the boss.” Id., at 675.
   Following Sneed's interview, Oklahoma charged Glossip,
too, with capital murder. The prosecution offered Glossip a
deal: plead guilty and avoid the death sentence in return for
testifying against Sneed. See App. to Pet. for Cert. in No.
22–6500, p. 144a. When Glossip refused, maintaining his in-
nocence, the State offered Sneed the same deal, and Sneed
accepted. 2001 OK CR 21, ¶5, 29 P. 3d 597, 599 (Glossip I).
Sneed then testifed at Glossip's trial that he beat Van Treese
to death “because [Glossip] asked him to do it.” Ibid.
When asked whether there was any “particular reason why
[Glossip] wanted to kill [Van Treese]” that night, Sneed re-
plied, “Not that I know of. Every time that Mr. Van Treese
showed up, [Glossip] was wanting me to kill him.” 6 Tr. 89
(June 8, 1998). In closing, the prosecution argued that
Glossip had asked Sneed to kill Van Treese because he be-
234                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

lieved Van Treese planned to fre him for embezzling hotel
profts. 8 Tr. 14–15 (June 10, 1998). The jury convicted
Glossip and sentenced him to death.
   The OCCA unanimously reversed. Sneed's testimony was
the only direct evidence connecting Glossip to the murder, it
held, and “[t]he evidence at trial tending to corroborate
Sneed's testimony was extremely weak.” Glossip I, 29
P. 3d, at 599. Defense counsel's failure to cross-examine
Sneed on his many inconsistent statements was therefore “so
ineffective” as to undermine any “confdence that a reliable
adversarial proceeding took place.” Ibid.
   In 2004, after Glossip rejected another plea offer, 3 App.
720, the State tried him a second time. Several witnesses
confrmed what Glossip had told the police in his second in-
terview: In the hours following Van Treese's killing, Glossip
feigned ignorance and lied about Van Treese's whereabouts.
As in the frst trial, however, only one witness, Justin Sneed,
testifed that Glossip was involved in anything more.1
Page Proof Pending Publication
   This time, moreover, the defense established (through the
State's medical examiner) that Van Treese had been attacked

  1
    The dissent's narrative, which presents as historical fact the testimony
of the prosecution's witnesses at Glossip's second trial, relies heavily on
Sneed's testimony to suggest that Glossip directed the crime and an elabo-
rate coverup. See post, at 262–267 (opinion of Thomas, J.). To the ex-
tent the dissent relies on witnesses other than Sneed, their testimony con-
frms no more than what Glossip himself admitted to the police. As for
Sneed's testimony, the dissent constructs its favored narrative from among
his multiple inconsistent accounts of the murder. See supra, at 232–235;
compare post, at 264 (dissent asserting that “Sneed left [Van Treese's
room] when he thought that he had killed Van Treese”), with 2 App. 665
(Sneed telling police he left Van Treese's room when he thought Van
Treese was “knocked out”); compare post, at 264 (dissent asserting Glossip
told Sneed “they would both be evicted if Glossip lost his job”), with 2
App. 655–665 (Sneed telling police that Van Treese's death was the acci-
dental result of a robbery gone wrong), 6 Tr. 89 (June 8, 1998) (Sneed
testifying that he did not know why Glossip wanted him to kill Van
Treese), and 12 Tr. 75 (May 26, 2004) (Sneed testifying that Glossip had
wanted to rob Van Treese).
                   Cite as: 604 U. S. 226 (2025)           235

                      Opinion of the Court

with a knife as well as with a baseball bat. 1 id., at 239–
245. Although Sneed had denied stabbing Van Treese to the
police and at Glossip's frst trial, he now said that he had
repeatedly tried to stab Van Treese in the chest with a
pocket knife. Glossip II, 157 P. 3d, at 148–149. Because
the prosecution had not notifed the defense about this
change in testimony, Glossip moved for a mistrial. 12 Tr.
105 (May 26, 2004). The trial court denied that motion after
the prosecution attested that the change was news to them,
too. Id., at 107–108 (“The chest thing we're all hearing at
the same time”).
  The prosecution also asked Sneed whether anyone had
prescribed him any medication:
    “Q. After you were arrested, were you placed on any
    type of prescription medication?
    “A. When I was arrested I asked for some Sudafed be-
    cause I had a cold, but then shortly after that somehow
Page Proof Pending Publication
    they ended up giving me Lithium for some reason, I don't
    know why. I never seen no psychiatrist or anything.
    “Q. So you don't know why they gave you that?
    “A. No.” Id., at 64.

Sneed then confrmed that he used illegal drugs including
marijuana and “crank” (methamphetamine) “twice a week”
prior to his arrest. Id., at 64–65. Finally, Sneed testifed
about Glossip's purported motives for killing Van Treese.
He asserted that Glossip had suggested “robbing Barry of
his money,” id., at 75, that he had “told [Sneed] at one point
that with Mr. Van Treese out of the way . . . he would be
able not only [to] manage the motel on Council but also an-
other one they had [in Tulsa],” id., at 89, and that he had
worried he “was going to get fred” because “a couple of the
rooms that were already supposed to be remodeled . . .
weren't,” id., at 95.
  The prosecution weaved these suggestions into its closing
argument along with its original theory that Glossip had
236                  GLOSSIP v. OKLAHOMA

                        Opinion of the Court

wanted Van Treese dead to avoid being fred for embezzle-
ment. See 15 Tr. 65 (June 1, 2004) (arguing Glossip's motive
was “a big wad of around 4,000 bucks of American good Yan-
kee dollars to split with the kid”); id., at 153, 163 (arguing
Glossip was going to be fred because of “missing money”);
id., at 164–165 (arguing Glossip was going to be fred because
of the condition of the rooms). It then argued that Sneed,
“satisfed and contented with [his] humble life,” id., at 68,
had no propensity to violence except at Glossip's direction:
      “[I]t's as if Justin Sneed was a Rottweiler puppy, let's
      say 11 months old, and Richard Glossip was the dog
      trainer. You can sure sick a dog on somebody, but if
      you're going to do that and you send a dog that's not
      trained or is a little bit too young, he might trip and fall,
      he might get scared and run away, he might do some-
      thing stupid, he might not do a good job. But no matter
      how you slice it, no matter how you parse it, the person
Page Proof Pending Publication
      that says `sick `em' is the person that makes the deci-
      sion.” Id., at 73.
   The jury again convicted Glossip of capital murder and
again sentenced him to death.
   A closely divided OCCA affrmed, holding that circumstan-
tial evidence suggesting Glossip had mismanaged the hotel,
combined with the concession that Glossip had been dishon-
est in his initial statements after the murder, suffciently cor-
roborated Sneed's testimony that he killed Van Treese at
Glossip's direction. Glossip II, 157 P. 3d, at 151–153. In
dissent, Judge Chapel and Judge A. Johnson argued that the
majority “overstate[d] the strength of the accomplice corrob-
oration evidence.” Id., at 164–165, 175.
                              B
  Glossip continued to maintain his innocence in the years
after his conviction, fling several habeas petitions in state
and federal court. Although that litigation did not result
in relief, mounting concerns over the integrity of Glossip's
                   Cite as: 604 U. S. 226 (2025)             237

                      Opinion of the Court

conviction drew the attention of the Oklahoma Legislature.
A bipartisan group of 62 Oklahoma legislators retained a law
frm, Reed Smith, to conduct an independent investigation
into the case. Pet. for Cert. 12; App. to Pet. for Cert. 390a–
391a. In June 2022, Reed Smith reported its “grave doubt
as to the integrity of Glossip's murder conviction and death
sentence.” Independent Investigation of State v. Richard E.
Glossip 6 (June 7, 2022). Among other things, Reed Smith
concluded the prosecution had deliberately destroyed “key
physical evidence” before Glossip's retrial, including several
items from the crime scene and the inn's receipts and deposit
books, which could have helped Glossip address the accusa-
tions of embezzlement. Id., at 7, 9, n. 25, 34, 48. Reed
Smith further concluded that the State had “falsely por-
trayed Sneed at trial as a meek and non-violent `puppet,' ”
id., at 10, and that key testimony about Glossip's motive and
actions on the morning after the murder had been provided
Page Proof Pending Publication
by a former police offcer of “ `very limited honesty and in-
tegrity' ” who was jailed for making false statements shortly
after Glossip's second trial, id., at 6–12.
   Two months after Reed Smith's report, the State disclosed
seven boxes of previously withheld documents from Glossip's
trials. Those boxes contained a note the head prosecutor,
Connie Smothermon, sent to Sneed's lawyer before Sneed
testifed at the second trial. Smothermon's note concerned
“a few items that have been testifed to that I needed to
discuss with Justin,” including the “biggest problem,” which
(the note said) was “still the knife.” 3 App. 953. The exam-
iners' testimony about the knife was problematic, Smother-
mon's note explained, because “Justin [told] the police that
the knife fell out of his pocket and that he didn't stab the
victim with it,” yet the victim had “ `lacerations' ” consistent
with the “knife blade.” Ibid. It did not “make much sense”
to Smothermon, moreover, “that Justin could have control of
the bat and a knife” on his own. Ibid. “[W]e should get to
him this afternoon,” the note concluded. Ibid.
238                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

   The boxes further contained letters from Sneed to his at-
torney suggesting he had expressed a desire to recant his
testimony prior to Glossip's second trial. See id., at 811–
816. For example, in a letter dated May 15, 2003, Sneed
wrote to his attorney asking “ `do I have the choice of recant-
ing my testimony at any time during my life,' ” and is “ `there
. . . anything you know, on [Glossip's] court date and about
re-canting.' ” Id., at 815 (emphasis deleted); App. to Pet. for
Cert. in Glossip v. Oklahoma, No. 22–6500, at 192a.2
   Based on this new evidence and the evidence revealed by
Reed Smith, Glossip fled another motion for post-conviction
relief with the OCCA. Among other things, Glossip argued
that, during his second trial, Smothermon had interfered
with Sneed's testimony about the knife in violation of the
rule of sequestration, which prohibits witnesses from hear-
ing each other's testimony. 3 App. 785–882. Oklahoma re-
sponded that Glossip's claims were meritless, but that it
Page Proof Pending Publication
would nonetheless waive any procedural defenses in order to
mitigate the damage from a “media campaign” on Glossip's
behalf. Id., at 717–718. Oklahoma further asked the OCCA
to deny Glossip's claims on their merits so as “to trigger the
state court deference anticipated in [the Antiterrorism and
Effective Death Penalty Act]” in any future federal review.
Id., at 718, n. 7. Noting that it alone would “determine
whether the rules of this Court should be abandoned,” the
OCCA held that Glossip's claims were procedurally barred
as well as meritless. Id., at 775–783.

   2
     The dissent claims Sneed thought the phrase “ `recan[t] my testimony' ”
meant “ `refuse to testify,' ” post, at 272, n. 2, meaning (on the dissent's
view) Sneed asked his lawyer: “If I [testify] again, do I have the choice of
[refusing to testify] at any time during my life?” The dissent further
points to an interview Sneed gave decades later, where (with Glossip's
execution imminent) he denied ever “ `want[ing] to change the truth.' ”
Post, at 271, n. 2. Of course, Sneed's much later denials do not erase his
prior statements about recanting.
                        Cite as: 604 U. S. 226 (2025)                      239

                            Opinion of the Court

   Shortly thereafter, the State “unearthed disturbing reve-
lations about the contents of ” an eighth box of trial docu-
ments “consisting of material it previously prevented the de-
fense from obtaining.” Brief for Respondent 10. “Buried
inside Box 8,” the State says, “was a page of notes handwrit-
ten by Smothermon during a pretrial interview with Sneed,”
indicating “that Sneed had told Smothermon that he was `on
lithium' not by mistake, but in connection with a `Dr. Trum-
pet.' ” Ibid. Oklahoma's attorney general “deduced the
import of these notes in short order”: Only a single psychia-
trist worked in the Oklahoma County jail when Sneed was
held there, and his name was Dr. Larry Trombka. Ibid.;
see also 3 App. 930. A summary of Sneed's medical records
(previously withheld from Glossip's counsel after motion
practice seeking their discovery) showed that Sneed had re-
ceived lithium to treat his undisclosed bipolar disorder.
Brief for Respondent 10; 3 App. 1005. After this discovery,
Page Proof Pending Publication
Dr. Trombka signed an affdavit attesting that he was the
only medical professional at the jail who would have pre-
scribed Sneed lithium. Id., at 1003.
   The attorney general accordingly determined that Sneed
“was not in fact mis-prescribed lithium, but rather diagnosed
with bipolar disorder and treated with lithium under the care
of a psychiatrist”—and “despite her knowledge of these
facts,” Smothermon “elicited false testimony from Sneed” on
that subject. Brief for Respondent 11.3

  3
    Also included in Box 8 were prosecutors' witness interview notes sug-
gesting the State may have omitted certain details from the summaries it
turned over to the defense. For example, one witness apparently told the
prosecution that Glossip had sold him a big screen TV and a couch for
$900, 3 App. 952—a sum that would account for much of the cash Glossip
had on his person at his arrest. That same witness testifed at trial that
he did not know how much money Glossip had received for those sales. 1
id., at 286. Glossip's girlfriend later explained in a post-trial affdavit that
Glossip had been selling their possessions to pay for an attorney. 2 id.,
at 706.
240                    GLOSSIP v. OKLAHOMA

                          Opinion of the Court

  The attorney general thereafter disclosed Box 8 to Glossip
and retained an independent counsel to conduct another re-
view of Glossip's conviction. As relevant here, the inde-
pendent counsel concluded that Smothermon's attempt to in-
terfere with Sneed's testimony about the knife violated the
rule of sequestration, that her failure to turn over Sneed's
statements about his mental health treatment violated
Brady v. Maryland, 373 U. S. 83 (1963), and that her failure
to correct Sneed's false trial testimony that he had been
given lithium after asking for cold medicine violated Napue,
360 U. S. 264. App. to Pet. for Cert. 50a, 58a. His report
concluded:
      “[T]he State must vacate Glossip's conviction due to its
      decades-long failure to disclose what I believe is Brady
      material, correct what I believe was false trial testi-
      mony of its star witness, and what I believe was a viola-
      tion of the Court ordered Rule of Sequestration of wit-
Page Proof Pending Publication
      nesses. . . . In my view, this case is also permeated by
      failures to secure, safeguard and maintain evidence in a
      capital murder case.” Id., at 62a.
   Following the Box 8 disclosure and the independent coun-
sel's recommendation, Glossip fled a successive petition for
post-conviction relief with the OCCA asserting Brady,
Napue, cumulative error, and actual innocence claims.4 The
attorney general fled a “Response in Support of Petitioner's
Successive Application for Post-Conviction Relief.” 3 App.
973. Although the attorney general did not endorse Gloss-
ip's actual innocence claim, he represented that his offce had
“concluded that Justin Sneed . . . made material misstate-
ments to the jury regarding his psychiatric treatment and

  4
    The dissent faults Glossip for “ignor[ing] the lithium issue on direct
appeal” years earlier. Post, at 269. Glossip had no reason to know at
the time of his direct appeal that Smothermon knowingly failed to correct
Sneed's false testimony about why he had been given lithium, however, so
he would have had no occasion to raise his Napue or Brady claims then.
                   Cite as: 604 U. S. 226 (2025)           241

                      Opinion of the Court

the reasons for his lithium prescription,” which the State
had failed to correct in violation of Napue. 3 App. 974. In
addition, the State indicated it was “concerned that there
were multiple and cumulative errors, such as violation of the
rule of sequestration and destruction of evidence, that when
taken together with Sneed's misstatements warrant” a new
trial. Ibid.; see also id., at 977 (“[T]he State believes
Glossip is entitled to post-conviction relief ”); id., at 978
(State is “compelled, consistent with Napue,” to correct mis-
statements); id., at 979 (“[T]he State requests that the Court
vacate Glossip's conviction and that the case be remanded to
the district court”). Because Oklahoma agreed with Glossip
on the pertinent facts, it did not request an evidentiary
hearing.
   The OCCA denied Glossip's unopposed petition without a
hearing. It acknowledged the attorney general's request
that Glossip's conviction be vacated, noting that this conces-
sion alone could not “directly” provide a ground for relief.
Page Proof Pending Publication
529 P. 3d, at 223. The court said the following about the
State's confession of Napue error:
    “Glossip claims that the State failed to disclose evidence
    of Justin Sneed's mental health treatment and that
    Sneed lied about his mental health treatment to the jury.
    Though the State in its response now concedes that this
    alleged false testimony combined with other unspecifed
    cumulative errors warrant postconviction relief, the con-
    cession alone cannot overcome the limitations on succes-
    sive post-conviction review. See 22 O.S. Supp. 2022,
    § 1089(D)(8). The State's concession is not based in law
    or fact.” 529 P. 3d, at 226 (footnote omitted).

The OCCA then applied Oklahoma's Post-Conviction Proce-
dures Act (PCPA) to hold that Glossip's claims were proce-
durally barred. It concluded separately that the evidence
presented by the parties did not “create a Napue error.”
Ibid. (footnote omitted).
242                   GLOSSIP v. OKLAHOMA

                         Opinion of the Court

   This Court thereafter stayed Glossip's execution at the
joint request of the parties and granted certiorari to consider
Glossip's Brady and Napue claims and the effect of the attor-
ney general's confession of error.5 601 U. S. 999 (2024).
The Court also requested argument on an additional ques-
tion: whether the OCCA's holding that the PCPA precluded
post-conviction relief is an adequate and independent state-
law ground for the judgment.
   Because Oklahoma agrees with Glossip on the merits of
his appeal, the Court appointed Christopher Michel as ami-
cus curiae to defend the judgment below. 601 U. S. 1010
(2024). He has ably discharged his responsibilities.

                                  II
                                  A
   We begin with this Court's jurisdiction to review the
Page Proof Pending Publication
OCCA's judgment. “ `This Court will not take up a question
of federal law presented in a case “if the decision of [the
state] court rests on a state law ground that is independent
of the federal question and adequate to support the judg-
ment.” ' ” Cruz v. Arizona, 598 U. S. 17, 25 (2023) (quoting
Lee v. Kemna, 534 U. S. 362, 375 (2002)). “In the context of
direct review of a state court judgment, the independent and
adequate state ground doctrine is jurisdictional.” Coleman
v. Thompson, 501 U. S. 722, 729 (1991). A state ground of
decision is independent only when it does not depend on a
federal holding, Foster v. Chatman, 578 U. S. 488, 498 (2016),
and also is not intertwined with questions of federal law,
Michigan v. Long, 463 U. S. 1032, 1040–1041 (1983).
“[W]hen the adequacy and independence of any possible
state law ground is not clear from the face of the opinion, we
will accept as the most reasonable explanation that the state

  5
   Because the Court grants relief under Napue, the Court need not reach
the merits of Glossip's Brady claim.
                   Cite as: 604 U. S. 226 (2025)            243

                      Opinion of the Court

court decided the case the way it did because it believed that
federal law required it to do so.” Ibid.
   Amicus argues this Court lacks jurisdiction because the
OCCA held that Glossip's claims were barred under the
PCPA, and the PCPA is “a paradigmatic independent and
adequate state-law ground.” Brief for Court-Appointed
Amicus Curiae 13. That argument fails because it over-
looks an antecedent holding that turned on federal law. The
OCCA frst rejected the attorney general's confession of
Napue error, deeming it meritless and therefore incapable of
“overcom[ing]” application of the PCPA. 529 P. 3d, at 226.
Only then did it apply the PCPA to Glossip. Because the
OCCA's decision to reject the attorney general's confession
of error rested exclusively on federal law, so too did its sub-
sequent decision to apply the PCPA.
   In his brief to the OCCA, the attorney general disclaimed
reliance on any procedural defenses, including the PCPA.
Page Proof Pending Publication
Instead, the attorney general “concede[d] error under
Napue,” 3 App. 978, acknowledging that, as a matter of fed-
eral law, the prosecution's knowing failure to correct Sneed's
“material misstatements” entitled Glossip to a new trial.
Id., at 977, 978, 979. The OCCA held that this confession of
Napue error could not “overcome the [PCPA's] limitations on
successive post-conviction review” because it was “not based
in law or fact.” 529 P. 3d, at 226. Specifcally, the OCCA
concluded that the underlying evidence “d[id] not create a
Napue error.” Ibid. (footnote omitted). Thus, the OCCA's
application of the PCPA over the attorney general's confes-
sion of error depended on its determination that no Napue
violation had occurred. That was a federal holding, and it
was the only reason the OCCA provided for its conclusion
that the attorney general's confession could not “overcome”
the PCPA. 529 P. 3d, at 226. The PCPA therefore poses
no impediment to our review in this case.
   Oklahoma precedent involving confessions of error by an
attorney general confrms this reading. As the OCCA has
244                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

repeatedly explained, it will normally reject an attorney
general's confession of error only after fnding that it lacks a
basis in the law and in the record. See, e. g., Bindrum v.
State, 27 Okla. Crim. 372, 228 P. 168 (1924) (“Where the At-
torney General confesses error, th[e] court will examine the
record, and, if the confession is sustained thereby, and is well
founded in law, the conviction will be reversed” (syllabus by
the court)).6 Otherwise, if the confession of error is sup-
ported by the law and the record, the OCCA will reverse
the underlying conviction and remand for a new trial.7 Ibid.
The OCCA applied that same rule here: It rejected the attor-
ney general's confession of error as having no basis “in law
or fact,” and explained that it would therefore apply the
PCPA. 529 P. 3d, at 226.
  In doing so, the OCCA “made application of the procedural
bar depend on an antecedent ruling on federal law, that is,
on the determination of whether federal constitutional error
ha[d] been committed.” Ake v. Oklahoma, 470 U. S. 68, 75
Page Proof Pending Publication
(1985). After all, it made application of the PCPA contin-

   6
     See also Raymer v. State, 27 Okla. Crim. 398, 228 P. 500 (1924) (“Where
the Attorney General confesses error, th[e] court will examine the record,
and, if the confession is sustained thereby and is well founded in law, the
conviction will be reversed” (syllabus by the court)); Dorsett v. State, 16
Okla. Crim. 65, 69, 180 P. 557, 558 (1919) (reversing conviction because
“the confession of error [of the attorney general] is well founded” in law);
Whittemore v. State, 26 Okla. Crim. 338, 223 P. 890 (1924) (per curiam)
(same); Day v. State, 352 P. 2d 935 (OCCA 1960) (“Where the Attorney
General confesses error, Court of Criminal Appeals will examine the rec-
ord, and, if confession is sustained thereby, and is well founded in law,
conviction will be reversed” (syllabus by the court)); Casey v. State, 440
P. 2d 208, 209 (OCCA 1968) (“When the Attorney General confesses error,
this Court will carefully examine the record for fundamental error”); Mc-
Connell v. State, 485 P. 2d 764, 765 (OCCA 1971) (similar); One Ford Tour-
ing Car v. State, 100 Okla. 267, 268, 229 P. 231, 232 (1924) (establishing
identical rule in civil forfeiture context).
   7
     The PCPA would not stand in the way of a reversal under this rule
because it is not a jurisdictional bar. See Valdez v. State, 2002 OK CR
20, ¶¶24–28, 46 P. 3d 703, 710.
                    Cite as: 604 U. S. 226 (2025)             245

                       Opinion of the Court

gent on its determination that the attorney general's confes-
sion of federal constitutional error had no basis in law or
fact. To the extent that the OCCA's reasoning on this point
is insuffciently “clear from the face of the opinion,” we none-
theless presume reliance on federal law under Michigan v.
Long, 463 U. S., at 1040–1041. This Court therefore has ju-
risdiction to review the judgment below.

                                 B
   The dissent dismisses all this as an “invent[ed] . . . federal
holding that the OCCA never made.” Post, at 279. As the
dissent sees it, the OCCA rejected the attorney general's
confession of error because (the dissent says) the State failed
adequately to address all of the PCPA's procedural require-
ments. See post, at 280. The OCCA plainly held that the
attorney general's confession was “not based in law or fact,”
529 P. 3d, at 226, however, forcing the dissent to provide
Page Proof Pending Publication
an awkward explanation that this holding about a federal
confession of error on the merits was only about the PCPA's
state-law, procedural requirements. Post, at 280. Yet the
State expressly attempted to waive those procedural re-
quirements by arguing that Glossip was entitled to a new
trial. 3 App. 979 (“[T]he State requests that the Court va-
cate Glossip's conviction and that the case be remanded to
the district court”). So to explain away the “based in law
or fact” language, the dissent must proceed on the assump-
tion that Oklahoma law requires applicants to satisfy the
PCPA's nonjurisdictional provisions even when the State
waives them and even if the State's confession of constitu-
tional error is otherwise meritorious—notwithstanding the
many other contexts where the OCCA privileges meritorious
confessions of error. See n. 6, supra (collecting cases); App.
to Brief for National Association of Criminal Defense Law-
yers as Amicus Curiae 1a–21a (cataloging the OCCA's deci-
sions in the 298 confession-of-error cases predating Glossip's,
all of which resulted in relief).
246                 GLOSSIP v. OKLAHOMA

                      Opinion of the Court

  That assumption is hardly “clear from the face of the opin-
ion” below. Long, 463 U. S., at 1041. Thus, we must “ac-
cept as the most reasonable explanation that the state court
decided the case the way it did because it believed that fed-
eral law required it to do so.” Ibid.

                              III
                              A
   Turning to the merits, we conclude that the prosecution
violated its constitutional obligation to correct false
testimony.
   In Napue v. Illinois, this Court held that a conviction
knowingly “obtained through use of false evidence” violates
the Fourteenth Amendment's Due Process Clause. 360
U. S., at 269. To establish a Napue violation, a defendant
must show that the prosecution knowingly solicited false tes-
timony or knowingly allowed it “to go uncorrected when it
Page Proof Pending Publication
appear[ed].” Ibid. If the defendant makes that showing, a
new trial is warranted so long as the false testimony “may
have had an effect on the outcome of the trial,” id., at 272—
that is, if it “ `in any reasonable likelihood [could] have af-
fected the judgment of the jury,' ” Giglio v. United States,
405 U. S. 150, 154 (1972) (quoting Napue, 360 U. S., at 271).
In effect, this materiality standard requires “ ` “the benef-
ciary of [the] constitutional error to prove beyond a reason-
able doubt that the error complained of did not contribute to
the verdict obtained.” ' ” United States v. Bagley, 473 U. S.
667, 680, n. 9 (1985) (quoting Chapman v. California, 386
U. S. 18, 24 (1967)).
   Here, Oklahoma's attorney general joins Glossip in assert-
ing a Napue error, conceding both that Sneed's testimony
was false and that the prosecution knowingly failed to cor-
rect it. The record supports that confession of error. A
summary of Sneed's medical records created by the local
sheriff 's department establishes that someone diagnosed
Sneed with bipolar disorder and prescribed him lithium. 3
                    Cite as: 604 U. S. 226 (2025)             247

                       Opinion of the Court

App. 1005. Dr. Trombka, a psychiatrist, attested in a sworn
affdavit that he was the only medical professional at the
Oklahoma County jail who would have issued Sneed that pre-
scription. Id., at 930–931. Dr. Trombka also confrmed,
and nobody contests, that lithium is used only in psychiatric
treatments and not for dental pain (as Sneed said at a pre-
trial hearing) or a cold (as Sneed testifed at Glossip's trial).
Ibid. Nor would anyone confuse lithium with Sudafed,
which is a cold medication. Ibid. Sneed's trial testimony
that he had been given lithium after asking for Sudafed and
had “never seen no psychiatrist or anything” was therefore
false.
   The evidence likewise establishes that the prosecution
knew Sneed's statements were false as he testifed to them.
The prosecution almost certainly had access to Sneed's medi-
cal fle, which would have listed both the lithium prescription
and the bipolar diagnosis. Among other things, those rec-
Page Proof Pending Publication
ords would have been provided to the State as part of
Sneed's competency evaluation, id., at 931, and the State op-
posed Glossip's discovery request of Sneed's medical fles on
its merits, 2 id., at 622–623; 3 id., at 933. As amicus and
the dissent emphasize, moreover, “[l]ithium is prescribed
only for mood disorders.” Brief for Court-Appointed Ami-
cus Curiae 14; post, at 268 (“It is undisputed that lithium's
sole medical purpose, both in 1997 and today, is to treat bipo-
lar disorder and other mental health disorders”). Yet the
prosecution knew that Sneed had previously told a compe-
tency evaluator that he had been prescribed lithium “after
his tooth was pulled,” 2 App. 700; that statement was part
of a competency record to which both the State and Glossip
had access, id., at 698–703. Prosecutors then heard Sneed
testify to a different version of events at trial: that the lith-
ium had been given to him after he asked for Sudafed be-
cause he had a cold. 1 id., at 312.
   In addition, Smothermon's notes show that she had a pre-
trial conversation with Sneed at which he mentioned “lith-
248                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

ium” and “Dr. Trumpet.” 3 id., at 927. Glossip argues, and
the attorney general admits, that this shows Sneed told
Smothermon that Dr. Trumpet (meaning Dr. Trombka) had
prescribed him lithium. As just discussed, the record shows
that, in fact, Dr. Trombka did diagnose Sneed with bipolar
disorder and prescribe him lithium. Sneed plainly discussed
these matters with the prosecution. In that private conver-
sation, he would have had little to gain from prevaricating
about his prescriptions, nor do the notes suggest he did any-
thing of the kind. The straightforward inference is that
Sneed told Smothermon that Dr. Trombka had prescribed
him the lithium.8
   That leaves materiality. Evidence can be material even if
it “goes only to the credibility of the witness,” Napue, 360
U. S., at 269; indeed, “[t]he jury's estimate of the truthfulness
and reliability of a given witness may well be determinative
of guilt or innocence,” ibid. Because Sneed's testimony was
the only direct evidence of Glossip's guilt of capital murder,
Page Proof Pending Publication
the jury's assessment of Sneed's credibility was necessarily
determinative here. Besides Sneed, no other witness and
no physical evidence established that Glossip orchestrated
Van Treese's murder. Thus, the jury could convict Glossip
only if it believed Sneed.
   Had the prosecution corrected Sneed on the stand, his
credibility plainly would have suffered. That correction
would have revealed to the jury not just that Sneed was
untrustworthy (as amicus points out, the jury already knew
he repeatedly lied to the police), but also that Sneed was
  8
    The dissent claims Sneed instead repeated his prior false statement
that he had been given the lithium after having his tooth pulled. See
post, at 273, 274, n. 3, 286, n. 6, 302–303. Yet the dissent's only source for
this theory, Smothermon's co-counsel Gary Ackley, acknowledged under
oath that he knew lithium was not a pain medication, 3 App. 940, meaning
he would have known this story, too, to be wrong. In any event, even if
the prosecution did believe Sneed had been given lithium for a toothache,
that still would have put them on notice that Sneed's testimony at trial
(about receiving lithium after asking for cold medication) was false.
                   Cite as: 604 U. S. 226 (2025)            249

                      Opinion of the Court

willing to lie to them under oath. Such a revelation would
be signifcant in any case, and was especially so here where
Sneed was already “nobody's idea of a strong witness.”
Brief for Court-Appointed Amicus Curiae 37. Even if
Sneed's bipolar disorder were wholly irrelevant, as amicus
argues, his willingness to lie about it to the jury was not.
“ `A lie is a lie, no matter what its subject.' ” Napue, 360
U. S., at 269–270 (quoting People v. Savvides, 1 N. Y. 2d 554,
557, 136 N. E. 2d 853, 854–855 (1956)).
   Sneed's false testimony also bore on Glossip's guilt in a
more direct way. As Smothermon's co-counsel Gary Ackley
has conceded, it “would have been an important fact for the
defense to know” that Sneed had been prescribed lithium to
treat bipolar disorder. 3 App. 940. After the Box 8 disclo-
sures, Dr. Trombka explained to Glossip's counsel that bipo-
lar disorder symptoms “can be exacerbated by illicit drug
use, such as methamphetamine,” to “cause an individual to be
Page Proof Pending Publication
more paranoid or potentially violent.” Id., at 932. Sneed
admitted at trial that he regularly used drugs, including
methamphetamine. His diagnosis with a disorder that could
trigger impulsive violence when combined with drug use
thus would have undermined the prosecution's theory that
Sneed was harmless on his own—a Rottweiler puppy be-
holden to his trainer. 15 Tr. 73 (June 1, 2004). That theory
was an important part of the prosecution's case and featured
prominently in its opening and closing statements. See, e.g.,
3 Tr. 209 (May 13, 2004) (arguing in opening that Sneed was
“pretty content . . . to do whatever it is that Richard Glossip
wanted him to do”); 15 Tr. 69–74 (June 1, 2004) (emphasizing
in closing that Sneed would have never committed murder
without Glossip). Hence there is a reasonable likelihood
that correcting Sneed's testimony would have affected the
judgment of the jury. Napue, 360 U. S., at 271.
   Amicus objects that “the jury already knew that Sneed
had been prescribed lithium, used illegal drugs, and behaved
impulsively; he admitted that he beat a man to death with a
250                 GLOSSIP v. OKLAHOMA

                      Opinion of the Court

baseball bat in the middle of the night with no advanced
planning.” Brief for Court-Appointed Amicus Curiae 36.
As amicus sees it, the additional evidence provided by
Sneed's lie and his treatment for bipolar disorder could
hardly have made a difference in light of so much other im-
peaching evidence. Id., at 36–37. Of course, at trial, the
prosecution urged the jury to believe just the opposite: that
despite his prior dishonesty and violence, Sneed was now
telling the truth. See, e. g., 15 Tr. 153–155 (June 1, 2004).
A prosecutor's midtrial revelation that Sneed lied on the
stand would have signifcantly undercut that argument.
   In any event, amicus's position is self-defeating. If the
evidence impeaching Sneed's credibility was already over-
whelming, then no reasonable jury could have convicted
Glossip in the frst place, given that the prosecution's case
rested centrally on Sneed's credibility. Amicus appears to
assume the jury would have believed Sneed no matter what.
Page Proof Pending Publication
Such an assumption has no place in a materiality analysis,
which asks what a reasonable decisionmaker would have
done with the new evidence. See Wearry v. Cain, 577 U. S.
385, 393–394 (2016) (per curiam) (rejecting argument that
evidence was immaterial because witness's credibility was
“already impugned”); cf. Strickland v. Washington, 466 U. S.
668, 695 (1984).
   Although the prosecution's failure to correct Sneed's false
testimony was a material Napue violation on its own, addi-
tional conduct by the prosecution further undermines conf-
dence in the verdict. The attorney general has confessed
to “ `violation of the rule of sequestration' ” with respect to
Smothermon's apparent midtrial attempt to speak with
Sneed about the knife, as well as to “ `destruction of evi-
dence,' ” including the hotel's fnancial records and items
Glossip and Sneed allegedly handled in Van Treese's room.
See Brief for Respondent 13; 3 App. 935 (prosecutor Ackley
attesting under oath that “I was informed that a box of evi-
dence containing 10 items was destroyed by the Oklahoma
                       Cite as: 604 U. S. 226 (2025)                    251

                           Opinion of the Court

City Police Department. . . . It is likely that I was aware of
that fact during the 2004 retrial . . . . That this happened
horrifes me”); Independent Investigation of State v. Richard
E. Glossip, at 7, 12–13, 41–43 (cataloging destroyed items).
In addition, the eight boxes of documents released to Glossip
included statements from Sneed evincing a desire to recant
his testimony and witness notes with details not previously
turned over to the defense. For example, the fles suggest
one witness told the prosecution (contrary to his trial testi-
mony) that Glossip sold him a couch and a TV for $900. 3
App. 952. That evidence would have supported Glossip's ac-
count of the cash he carried at his arrest outside an attor-
ney's offce: that he had sold his possessions to pay for an
attorney. See 2 id., at 706. Because prejudice analysis re-
quires a “cumulative evaluation” of all the evidence, whether
or not that evidence is before the Court in the form of an
independent claim for relief, these documents reinforce our
conclusion that the Napue error here prejudiced the defense.
Page Proof Pending Publication
Kyles v. Whitley, 514 U. S. 419, 441 (1995).9

  9
    The dissent's attempts to minimize these issues are unpersuasive.
Sneed's letter inquiring about “ `the choice of recanting my testimony,' ” 3
App. 815, disproves the dissent's assertion that “there is no evidence that
Sneed wished to `recant' his testimony.” Post, at 293. That Glossip re-
called receiving only $490 for his possessions during his frst trial does
not absolve the prosecution from its ordinary duty to disclose inconsistent
statements by its witnesses. Contra, ibid. The State's conceded seques-
tration violation also is not merely an insignifcant state-law issue, post,
at 292; like any other attorney, a prosecutor may not seek to infuence the
content of a witness's testimony. See, e. g., Geders v. United States, 425
U. S. 80, 90, n. 3 (1976) (“An attorney must respect the important ethical
distinction between discussing testimony and seeking improperly to in-
fuence it”). The dissent labors to discredit certain “handwritten notes”
on which neither Glossip nor this Court relies, see post, at 293, n. 8, but
Smothermon undisputedly wrote to Sneed's counsel that she needed to
“get to” him “to discuss” his problematic testimony about the knife. 3
App. 953. The next day, Sneed's testimony corrected the very problem
raised by Smothermon's letter. Smothermon nonetheless disclaimed any
knowledge of Sneed's change in testimony when Glossip objected. 12 Tr.
252                     GLOSSIP v. OKLAHOMA

                           Opinion of the Court

  For these reasons, we conclude that the prosecution's fail-
ure to correct Sneed's trial testimony violated the Due Proc-
ess Clause. Glossip is entitled to a new trial.

                                    B
   The OCCA's contrary holding rested on a mistaken inter-
pretation of Napue. According to the OCCA, there was no
violation because the defense “was aware or should have
been aware that Sneed was taking lithium at the time of
trial,” and the prosecution could not have “knowingly con-
cealed” something the defense already knew. 529 P. 3d, at
226. As an initial matter, Sneed's false testimony concerned
the reasons for his lithium prescription, not the mere fact
that he had taken it. Glossip's counsel was aware of the
latter, not of the former. In any event, the Due Process
Clause imposes “ `the responsibility and duty to correct' ”
false testimony on “representatives of the State,” not on de-
fense counsel. Napue, 360 U. S., at 269–270 (quoting Sav-
Page Proof Pending Publication
vides, 1 N. Y. 2d, at 557, 136 N. E., at 854).
   The OCCA also held that Sneed's testimony was not
“clearly false” because Sneed was “more than likely in denial
of his mental health disorders.” 529 P. 3d, at 226, 227. It
is not apparent why the OCCA thought Sneed was in denial,
nor why such denial should have caused Sneed to believe
that he had never seen a psychiatrist, when in fact he had.
Even supposing it did, however, Sneed's beliefs are beside
the point. What matters is that his testimony was false and
a prosecutor knowingly let it stand nonetheless. Napue, 360
U. S., at 269 (“[I]t is established that a conviction obtained
through use of false evidence, known to be such by repre-
sentatives of the State, must fall under the Fourteenth
Amendment”).

107–108 (May 26, 2004). Finally, not even the original prosecutors dispute
that the police destroyed key evidence before Glossip's retrial; the dissent
nonetheless dismisses that claim, undisputed for over two decades, as this
Court's “own creation.” Post, at 292–293.
                       Cite as: 604 U. S. 226 (2025)                     253

                           Opinion of the Court

   The dissent's arguments in support of the OCCA's conclu-
sions fare no better. As an initial matter, even the dissent
does not dispute that Sneed falsely testifed he had never
seen a psychiatrist. See post, at 290 (suggesting Sneed
“misremembered” that a psychiatrist prescribed him lithium
to treat bipolar disorder). The dissent does maintain that
other aspects of Sneed's statement were true, noting that
because Sneed was in denial about his diagnosis, his “state-
ment about his own knowledge was not false.” Post, at 291.
Sneed's statement that he asked for “Sudafed” to treat “a
cold” and was given lithium instead, 12 Tr. 64 (May 26, 2004),
was not, however, a statement “about his own knowledge.”
Even if Sneed himself did not believe that he suffered from
bipolar disorder, moreover, that would not render true his
assertion that he had no idea why his doctor thought he
needed lithium.
   The dissent next claims that the false testimony must itself
have directly affected the trial's outcome to be material
Page Proof Pending Publication
under Napue. Post, at 288 (“[T]he relevant inquiry under
Napue is whether the content of the false testimony at issue
is material”). As Napue made clear, however, “ `[a] lie is a
lie, no matter what its subject.' ” 360 U. S., at 269–270
(quoting Savvides, 1 N. Y. 2d, at 557, 136 N. E. 2d, at 854–
855). Nothing in Napue requires ignoring the fact of
Sneed's perjury in the prejudice analysis. To the contrary,
materiality instead always requires courts to assess whether
“the error complained of ” could have contributed to the ver-
dict. Chapman, 386 U. S., at 24; Bagley, 473 U. S., at 680,
n. 9. Here, the prosecutor's failure to correct Sneed's false
testimony is the relevant error, so the Court asks whether a
correction could have made a material difference. The an-
swer is clearly yes. See supra, at 247–252.10
  10
     The dissent also argues Sneed's lithium use was immaterial because
“the defense chose not to turn” it “into an impeachment issue,” post, at 288,
but each premise in that argument is mistaken. First, the defense did not
choose “not to raise Sneed's mental condition,” post, at 287; they asked him
254                    GLOSSIP v. OKLAHOMA

                          Opinion of the Court

   The remaining arguments offered in defense of the OCCA's
position are likewise unpersuasive. In an amicus brief, the
Van Treese family argues that it was Glossip's counsel who
asked Sneed about his lithium prescription, and that Smoth-
ermon's notes reveal only that Sneed relayed those questions
to Smothermon. See Brief for Victim Family Members as
Amici Curiae 7–22. That argument relies heavily on extra-
record materials not properly before the Court, including a
recent unsworn statement from Smothermon adopting the
family's interpretation of the notes. (The dissent, which
criticizes the independent counsel for “impugning” the trial
prosecutors' reputation, post, at 276, justifes its reliance on
these materials by accusing the Oklahoma attorney general
of “collusively exclud[ing]” them from the record, see post,
at 303.) Nor would accepting the family's account change
the Napue analysis. Whatever the impetus for the conver-
sation, the family agrees that Sneed and Smothermon dis-
Page Proof Pending Publication
cussed Dr. Trombka and lithium. The natural inference is
that Sneed explained to Smothermon the circumstances that
led to his lithium use. To avoid that inference, the family in
turn suggests both that Sneed was never diagnosed with bi-
polar disorder in the frst place, Brief for Victim Family
Members as Amici Curiae 17, and that Glossip's counsel
“knew about [Dr. Trombka] more than two decades ago,” id.,
at 21. Yet for the reasons previously explained, defense
counsel's purported knowledge of Dr. Trombka's existence is
irrelevant, and the prison medical record supports the attor-

about it in cross-examination and Sneed repeated his false testimony. See
13 Tr. 15 (May 27, 2004). Second, the defense did not know during trial
that Sneed had been diagnosed with bipolar disorder; to the contrary,
Glossip later sought (and the State successfully opposed) discovery on that
issue. 2 App. 621–622. Third, even if the defense had made a conscious
choice not to raise the (then-uncertain) reasons for Sneed's lithium use,
that would be irrelevant to the prosecution's duty to correct false testi-
mony “when it appears.” Napue, 360 U. S., at 269.
                   Cite as: 604 U. S. 226 (2025)           255

                      Opinion of the Court

ney general's concession that Sneed received a lithium pre-
scription as treatment for his bipolar disorder.
   The family also maintains (and the dissent agrees) that
Reed Smith and the independent counsel spent insuffcient
time interviewing Smothermon. Neither the family nor
Smothermon raised that objection before the OCCA, nor
does anyone now explain its relevance to the Napue analy-
sis. The argument is also unpersuasive on its own terms.
Both investigators spoke to Smothermon. When they did,
Smothermon did not provide the account she now endorses:
that Sneed relayed to her a conversation with Glossip's coun-
sel about Dr. Trombka and lithium. Instead, during a third
interview, Smothermon asked the independent counsel “why
he thought it was Dr Trombka and not Dr Trumpet the jazz
musician and I was making a personal note or something
else.” App. to Brief for Victim Family Members as Amici
Curiae 31a. There is no compelling evidence that a fourth
Page Proof Pending Publication
or ffth consultation with Smothermon would have yielded
materially different results.
   The Court-appointed amicus, for his part, largely aban-
dons the OCCA's reasoning and focuses instead on ambigu-
ities in Smothermon's notes. Amicus maintains that too
many inferential steps separate those notes from the conclu-
sion that Sneed lied on the stand and that Smothermon knew
it. For example, amicus argues that “the parties do not ex-
plain the basis for their asserted link between `Dr. Trumpet?'
and Trombka,” reiterating Smothermon's earlier statements
that she “ `is not convinced that Dr. Trombka and “Dr. Trum-
pet” are the same person.' ” Brief for Court-Appointed
Amicus Curiae 32. As already explained, however, there is
ample evidence in the record before this Court supporting
the inference that Smothermon knew about Sneed's psychiat-
ric treatment and lithium prescription, including the prison
medical record, Dr. Trombka's attestations, and Smother-
mon's own notes.
256                   GLOSSIP v. OKLAHOMA

                         Opinion of the Court

   Because ample evidence supports the attorney general's
confession of error in this Court, there also is no need to
remand for further evidentiary proceedings at the OCCA.
Indeed, that such proceedings are not necessary is the one
point on which Glossip, Oklahoma, amicus, and the OCCA
unanimously agree. See Tr. of Oral Arg. 108 (amicus con-
ceding that “I guess we all agree that [an evidentiary hear-
ing is] not . . . that it's not necessary”). The partial concur-
rence suggests this Court should nonetheless remand for
further proceedings on the ground that the evidence does not
remove all doubt that the attorney general's view of the rec-
ord is correct. Post, at 262 (Barrett, J., concurring in part
and dissenting in part). Yet for the reasons already ex-
plained, the record establishes a violation of Napue. See
supra, at 246–252. This Court has not required an eviden-
tiary record free of doubt to fnd a Napue violation in any
case, much less when an attorney general confesses that his
own offce erroneously obtained a capital conviction.11
Page Proof Pending Publication
                                   C
   Finally, the dissent maintains this Court lacks the author-
ity to remand for a new trial, but its analysis proves the
contrary. The dissent emphasizes that “ `[o]ur only power
over state judgments is to correct them to the extent that
they incorrectly adjudge federal rights.' ” Post, at 294 (quot-
ing Herb v. Pitcairn, 324 U. S. 117, 125–126 (1945)). It further
  11
    The dissent would order a hearing to provide “the Van Treese family
[with] the opportunity to present its case.” Post, at 303 (opinion of
Thomas, J.). The family has not requested an evidentiary hearing (or
participation in one) at any stage before the OCCA and does not request
that relief before this Court. Nor has the OCCA ever extended Oklaho-
ma victims' right to participate in criminal proceedings to state post-
conviction hearings. Cf. post, at 303–304. The request to do so here is
the dissent's alone. In any event, this Court does not “cast aside the
family's interests,” on procedural or any other grounds. Post, at 304.
For the reasons already explained, considering the evidence submitted by
the family would not change the outcome. See supra, at 255.
                   Cite as: 604 U. S. 226 (2025)           257

                      Opinion of the Court

agrees that, where a state court relies on a procedural rule
whose application turns on “whether federal constitutional
error has been committed,” Ake, 470 U. S., at 75, this Court
may remand for a new trial if it “ha[s] confdence that no
other state ground could support the decision below,” post,
at 300. Those principles describe this case.
   As explained above, the OCCA “incorrectly adjudge[d]”
Glossip's “federal rights.” Herb, 324 U. S., at 126. In doing
so, it relied on a procedural rule whose application turned on
the merits of a federal claim: “ `Where the Attorney General
confesses error, [the OCCA] will examine the record, and, if
the confession is sustained thereby, and is well founded in
law, the conviction will be reversed.' ” See supra, at 244
(quoting Bindrum, 27 Okla. Crim., at 372, 228 P., at 168, and
collecting authorities). Here, the attorney general “con-
cede[d] error under Napue,” 3 App. 978, and the OCCA re-
jected that confession because it wrongly concluded that no
Page Proof Pending Publication
such federal error had occurred. See supra, at 244. Be-
cause the Napue confession was “well founded in law,” it fol-
lows that “the conviction will be reversed.” Bindrum, 27
Okla. Crim., at 372, 228 P., at 168. Accordingly, all that re-
mains below is to vacate the conviction, and a new trial fol-
lows a fortiori.
   The dissent concludes otherwise because, in its view, a re-
mand for further consideration of alternative state grounds
is mandatory in every case where Michigan v. Long resolves
lingering doubt over the Court's jurisdiction. Post, at 295–
296. Long describes the circumstances under which this
Court has jurisdiction to review a state-court judgment; it
does not limit the Court's remedial authority over an estab-
lished federal constitutional violation. Nor does any other
precedent support the dissent's rule. That state courts who
“grant relief to criminal defendants” under an erroneous in-
terpretation of federal law may later grant relief “as a mat-
ter of [more protective] state law,” Kansas v. Carr, 577 U. S.
108, 128 (2016) (Sotomayor, J., dissenting), plainly does not
258                 GLOSSIP v. OKLAHOMA

                     Opinion of Barrett, J.

deprive this Court of the authority to grant relief where it
fnds a federal violation, contra, post, at 295–296; cf. Arizona
v. Evans, 514 U. S. 1, 8 (1995) (“Under [Michigan v. Long] state
courts are absolutely free to interpret state constitutional
provisions to accord greater protection to individual rights
than do similar provisions of the United States Constitution”).
   The dissent inverts this precedent, asserting that state
courts should always have another opportunity to identify
additional grounds for denying relief, even where this Court
has found a federal constitutional violation. Yet there is no
reason to allow state courts a second (or third, or fourth) bite
at the apple to identify alternative state grounds for their
decision in every case involving a dependent ground. The
facts as conceded by the attorney general and supported by
the record establish a violation of Napue. A new trial is the
remedy for a Napue violation. See Giglio, 405 U. S., at 155.
Here, this Court has jurisdiction and a Napue violation oc-
curred. Thus, Glossip is entitled to a new trial. See Ake,
Page Proof Pending Publication
470 U. S., at 86–87 (vacating conviction and remanding case
to the OCCA under similar circumstances).

                         *     *     *
   The judgment of the Oklahoma Court of Criminal Appeals
is reversed, and the case is remanded for further proceedings
not inconsistent with this opinion.
                                              It is so ordered.

   Justice Gorsuch took no part in the consideration or de-
cision of this case.
  Justice Barrett, concurring in part and dissenting in
part.
  While I agree with much of the Court's analysis, I would
not order the Oklahoma Court of Criminal Appeals (OCCA)
to set aside Richard Glossip's conviction. The OCCA did
not make factual fndings on the most important questions,
                    Cite as: 604 U. S. 226 (2025)             259

                      Opinion of Barrett, J.

and the record is open to multiple plausible interpreta-
tions. Consistent with our ordinary practice, the Court
should have corrected the OCCA's misstatement of Napue v.
Illinois and remanded this case for further proceedings.
360 U. S. 264 (1959). Instead, the Court has drawn its own
conclusions about what the record shows, thereby exceeding
its role.
   I begin with the common ground. At the threshold, I
agree with the Court's jurisdictional holding and therefore
join Part II of its opinion. We lack jurisdiction to review a
state court's adjudication of federal claims if the state court's
decision “rests on a state law ground that is independent of
the federal question and adequate to support the judgment.”
Coleman v. Thompson, 501 U. S. 722, 729 (1991). But when
a state-law ground of decision is intertwined with analysis
of a federal question, we will treat the decision as independ-
ent only if the state court “make[s] clear by a plain state-
Page Proof Pending Publication
ment” that its resolution of the state-law question does not
depend on its resolution of the federal question. Michigan
v. Long, 463 U. S. 1032, 1041 (1983). Though it is a closer
question for me than it is for the Court, I agree that the
OCCA's opinion does not clear this bar. True, the OCCA
rejected Glossip's application based on state-law procedural
limits on postconviction relief. But the opinion can be read
to say that the OCCA refused to accept the attorney gener-
al's waiver of this procedural bar because his confession of
error was not “based in law.” 2023 OK CR 5, ¶25, 529 P. 3d
218, 226. If that is what the OCCA meant, then its reliance
on state law depended on the merits of Glossip's federal
claims. After all, if the trial contained federal constitutional
error, then the attorney general's confession of error may
have been “based in law.” Because the opinion lacks a
“plain statement” clarifying that the OCCA's reliance on
state law was truly independent of its assessment of Gloss-
ip's federal claims, the Court rightly proceeds to the merits.
Michigan, 463 U. S., at 1041.
260                 GLOSSIP v. OKLAHOMA

                     Opinion of Barrett, J.

   I also share the Court's view that the OCCA misapplied
Napue. The OCCA appeared to think that Justin Sneed's
testimony “was not clearly false” because he “was more than
likely in denial of his mental health disorders.” 529 P. 3d,
at 227. But for purposes of Napue, the question is not
whether a witness subjectively thought he was lying—it is
whether the prosecution knowingly presented untrue testi-
mony. The OCCA also stated that Sneed's “known mental
health treatment evidence” would not have created a “rea-
sonable probability that the result of the proceeding would
have been different had Sneed's testimony regarding his use
of lithium been further developed at trial.” 529 P. 3d, at
227. Yet the OCCA ignored the critical fact that—had the
prosecutor, Connie Smothermon, corrected Sneed's testi-
mony—the jury would have learned that Sneed made a false
statement on the stand. Sneed's testimony was the primary
evidence that the State offered to prove that Glossip planned
Page Proof Pending Publication
the murder. Faced with a prosecutor forced to correct her
star witness, a juror might have disbelieved Sneed's testi-
mony in its entirety. And if a juror went from belief to dis-
belief in Sneed, she might have changed her ultimate assess-
ment of whether the State had proved Glossip's guilt beyond
a reasonable doubt. So if Sneed really did give false testi-
mony, and if Smothermon really did knowingly allow that
testimony to go uncorrected, then Smothermon violated
Glossip's due process rights under Napue. The OCCA's con-
trary statements were wrong as a matter of federal law.
   I part ways with the Court on what comes next. In exer-
cising our appellate function, it is not our role to fnd facts;
instead, we review the factual fndings of lower courts, sub-
ject to a deferential standard of appellate review. See Price
v. Johnston, 334 U. S. 266, 291 (1948). This practice makes
good sense. This Court is well equipped to answer ques-
tions of federal law; it is ill equipped either to determine the
credibility of witnesses or to master voluminous trial rec-
ords. Other actors in our judicial system—including, where
                      Cite as: 604 U. S. 226 (2025)                  261

                         Opinion of Barrett, J.

appropriate, state courts like the OCCA—better serve these
functions, as our standard of review refects. In this case,
however, the Court has chosen to function as the initial
factfnder.
   To establish a violation of Napue, Glossip must show that
(1) Sneed gave false testimony and (2) Smothermon knew
that the testimony was false. To make these showings,
Glossip relies largely on notes taken by Smothermon, an af-
fdavit from Dr. Trombka, and a “medical information sheet.”
According to the Court, these documents clearly demon-
strate that (1) Sneed lied when he said that he did not know
why he had been given lithium and that he had never seen a
psychiatrist and (2) Smothermon knew that both of these
statements were lies. See ante, at 246–248, 255. Thus, the
Court concludes, there is no need for the OCCA to make its
own factual fndings.*

Page         Proof Pending Publication
  *The Court suggests that this shortcut is appropriate because Glossip,
the attorney general, the Court-appointed amicus, and the OCCA “unani-
mously agree” that the record is suffciently developed. Ante, at 256. I
do not think that this assertion fairly captures the views of either the
amicus or the OCCA. When asked whether he “object[ed] to an eviden-
tiary hearing,” amicus—whom we appointed to defend the judgment
below in this Court—expressed doubt that he “ha[d] standing to object to
an evidentiary hearing.” Tr. of Oral Arg. 107–108. When pushed on the
point, he responded that the current record supports affrmance “based on
the evidence that [Glossip has] chosen to present and particularly given
that he's now told you he wants the case decided on the current record
[and] without an evidentiary hearing.” Id., at 109 (emphasis added). In
other words, amicus simply stated that the current record did not support
Glossip's claim—not that the record was in any objective sense already
fully developed. Moreover, the question here is not only whether further
factual development is warranted, but also which court should fnd facts
in the frst instance. Amicus certainly did not concede that this Court,
rather than the OCCA, should play that role on this record. As for the
OCCA, its lack of explanation of the facts cannot be divorced from its
erroneous view of Napue. Nothing in its opinion indicates what it would
make of this record evidence if it confronted the relevant questions
under Napue.
262                GLOSSIP v. OKLAHOMA

                     Thomas, J., dissenting

   I respectfully disagree. Smothermon's notes, taken dur-
ing a jailhouse interview of Sneed, consist of the words “on
Lithium?” and “Dr Trumpet?” 3 App. 927. These notes
are hardly clear, and there are competing explanations of
what they mean. Glossip, the Oklahoma attorney general,
and the Court argue that they demonstrate Smothermon's
knowledge that Sneed had lied about Dr. Trombka's prescrib-
ing him lithium for bipolar disorder. See ante, at 247–248,
255. The Van Treese amicus brief and Justice Thomas
contend that the notes instead refect Sneed's account of a
conversation with Glossip's lawyers, who had asked Sneed
whether he had received lithium from a “Dr Trumpet.” See
post, at 272–275, and n. 3 (dissenting opinion). There are
other possibilities too: For instance, perhaps Smothermon
was confused by references to “Dr Trumpet” and lithium but
never investigated the issue further. Neither Dr. Trombka's
affdavit nor the attached medical information sheet nor any
of the other record evidence discussed by the Court fore-
Page Proof Pending Publication
closes any of these possibilities.
   When the record is susceptible to multiple plausible infer-
ences, this Court should not be in the business of choosing
between them. It should have corrected the OCCA's mis-
statements of federal law and vacated the judgment, leaving
next steps—including the decision whether to conduct an ev-
identiary hearing—to the OCCA. By doing otherwise, the
Court has both displaced the OCCA as factfnder and poten-
tially overridden state-law constraints on the OCCA's reme-
dial authority. See post, at 293–301 (Thomas, J., dissent-
ing). Because the Court has exceeded its appellate role, I
respectfully dissent in part.

  Justice Thomas, with whom Justice Alito joins, and
with whom Justice Barrett joins as to Parts IV–A–1, IV–
A–2, and IV–A–3, dissenting.
  Richard Glossip—a convicted murderer twice sentenced to
death by Oklahoma juries—challenges the denial of his ffth
                  Cite as: 604 U. S. 226 (2025)           263

                     Thomas, J., dissenting

application for state post-conviction relief. Although
Glossip won the support of Oklahoma's new attorney general,
he failed to persuade either body with authority to grant
him relief: The Oklahoma Court of Criminal Appeals (OCCA)
denied Glossip's application as both procedurally defcient
and nonmeritorious, and Oklahoma's Pardon and Parole
Board denied clemency. Because this Court lacks the power
to override these denials, that should have marked the end
of the road for Glossip. Instead, the Court stretches the law
at every turn to rule in his favor. At the threshold, it con-
cocts federal jurisdiction by misreading the decision below.
On the merits, it fnds a due process violation based on pat-
ently immaterial testimony about a witness's medical condi-
tion. And, for the remedy, it orders a new trial in violation
of black-letter law on this Court's power to review state-
court judgments. I respectfully dissent.

Page Proof Pending
              I
                   Publication
                               A
  This case arises from the 1997 murder of Barry Van
Treese, the owner of an Oklahoma City motel. Beginning
in 1995, Glossip began working for Van Treese as the motel's
manager. 4 Tr. 182–183 (May 14, 2004). In that capacity,
Glossip unoffcially hired 19-year-old Justin Sneed to be the
motel's handyman. Glossip did not pay Sneed; instead,
he let him live at the motel free of charge and occasionally
bought him food. Id., at 43–44; 5 Tr. 67–70 (May 17, 2004);
2 App. 644. In late 1996, Van Treese learned of discre-
pancies in Glossip's accounting suggesting that Glossip had
been allowing guests to stay at the motel off the books and
pocketing the money for himself. 4 Tr. 63, 68–71 (May 14,
2004); 7 Tr. 35, 39–40, 45–49 (May 19, 2004); 11 Tr. 172–173
(May 25, 2004). During a visit to the motel on January
6, 1997, Van Treese confronted Glossip about this issue,
and, having discovered unregistered guests staying at the
264                GLOSSIP v. OKLAHOMA

                     Thomas, J., dissenting

motel, he threatened to report Glossip to the police un-
less Glossip produced receipts for their rooms. 8 Tr. 82
(May 20, 2004).
   Hours later, after Van Treese had gone to bed, Sneed en-
tered Van Treese's motel room and repeatedly beat him over
the head with a baseball bat. 2 App. 662–664; 11 Tr. 55 (May
25, 2004). Sneed left when he thought that he had killed
Van Treese, although the State's forensic pathologist later
determined that Van Treese had initially survived the at-
tack, and died several hours later after slowly bleeding out.
Id., at 55–57, 61; App. to Response to Petitioner's Succ. Ap-
plication for Post-Conviction Relief in No. PCD–2022–819
(OCCA), Tr. of Glossip Police Interview 10 (Jan. 9, 1997).
Following his arrest, Sneed explained to police that Glossip
had urged him to kill Van Treese. 2 App. 645, 660. Accord-
ing to Sneed, Glossip told him that they would both be
evicted if Glossip lost his job, and Glossip had promised to
Page Proof Pending Publication
pay him $10,000 for carrying out the murder. 12 Tr. 95–96,
98 (May 26, 2004).
   Shortly after the attack, Sneed went to Glossip's motel
room and informed him that he had killed Van Treese. Tr.
of Glossip Police Interview 10 (Jan. 9, 1997). Glossip began
directing a coverup. On Sneed's account, Glossip frst told
Sneed to clean up glass shards from a window that Sneed
had broken during the attack. 12 Tr. 122 (May 26, 2004).
Glossip also sent Sneed to retrieve about $4,000 in cash from
Van Treese's car, and then to abandon the car in a nearby
credit union parking lot. Id., at 124, 129. When Sneed re-
turned, the two divided the cash. Id., at 128–129. They
then entered Van Treese's room, whereupon Glossip directed
Sneed to tape a shower curtain over the broken window and
run the air conditioning at full blast to eliminate any odor.
Id., at 130, 132. Glossip then dispatched Sneed to buy plexi-
glass, which the pair installed over the broken window on
the morning of January 7. Tr. of Glossip Police Interview
                        Cite as: 604 U. S. 226 (2025)                      265

                           Thomas, J., dissenting

14–15 (Jan. 9, 1997); 4 Tr. 163–165 (May 14, 2004); 13 Tr. 126
(May 27, 2004).1
  Glossip took additional steps to cover up the murder. He
told multiple witnesses that the window in Van Treese's
room was broken because two drunks had stayed there the
night before and smashed it in a brawl. 5 Tr. 85 (May 17,
2004); 7 Tr. 64 (May 19, 2004); 9 Tr. 46, 206 (May 21, 2004);
11 Tr. 188–189 (May 25, 2004). He told the housekeeper that
she did not need to clean the downstairs rooms—including
Van Treese's room. 8 Tr. 122–123 (May 20, 2004). Instead,
as Glossip explained to another employee and a motel resi-
dent, he and Sneed would cover those rooms. 7 Tr. 64 (May
19, 2004); 9 Tr. 49 (May 21, 2004). Glossip had never taken
such steps before. 8 Tr. 122–123 (May 20, 2004). He also
told various witnesses that he had seen Van Treese alive and
   1
     Despite its consistent theme that Sneed's testimony is too implausible
to sustain Glossip's conviction, the majority feels the need to bolster its
Page Proof Pending Publication
account by fnding “inconsisten[cies]” in his testimony that are not genu-
ine. Ante, at 234, n. 1. There is no contradiction in Sneed's claims that
he committed the murder as part of a robbery and that he did so to avoid
being “ `evicted if Glossip lost his job.' ” Ibid. At both of Glossip's trials,
Sneed consistently testifed that Glossip proposed taking the cash Van
Treese had with him and that Glossip told him that they would get evicted
if he did not kill Van Treese. 12 Tr. 95–96, 98, 124 (May 26, 2004); 6 Tr.
89–90, 95–96 (June 8, 1998). Contemporaneous evidence supports both
motivations. In his confession to police, Sneed stated that Glossip had
proposed killing Van Treese and taking the cash that Van Treese had with
him. 2 App. 675. And, two days after the murder, Glossip told police
that Sneed had committed the murder in part because “[h]e thought Barry
[Van Treese] was going to throw him out in the street.” Tr. of Glossip
Police Interview 13 (Jan. 9, 1997). Nor did Sneed ever claim that “he did
not know why Glossip wanted him to kill Van Treese.” Ante, at 234, n. 1.
He testifed only that he did not know “why Mr. Glossip wanted to kill
Mr. Van Treese on this particular night,” because “[e]very time that
Mr. Van Treese showed up, [Glossip] was wanting me to kill him.” 6 Tr.
89 (June 8, 1998) (emphasis added). As noted, Sneed clearly testifed at
the same trial that Glossip wanted Sneed to kill Van Treese so that they
would not be evicted. Id., at 90.
266                 GLOSSIP v. OKLAHOMA

                      Thomas, J., dissenting

well around 7 o'clock that morning. 4 Tr. 99 (May 14, 2004);
7 Tr. 62–63 (May 19, 2004); 9 Tr. 194 (May 21, 2004); 11 Tr.
126–127, 182–183 (May 25, 2004).
   That afternoon, the credit union called the motel to report
that Van Treese's car had been abandoned in its parking lot.
7 Tr. 70 (May 19, 2004). At that point, it became clear
to the motel's staff that Van Treese was missing. Id., at
72–74. Shortly thereafter, Glossip returned to the motel
from a shopping trip, during which he had made several
large purchases, including an engagement ring for his girl-
friend. Id., at 74; 14 Tr. 41 (May 28, 2004). He then pur-
ported to search the rooms and surrounding area for Van
Treese. 5 Tr. 97 (May 17, 2004); 9 Tr. 192–193 (May 21,
2004); 11 Tr. 185–186, 190 (May 25, 2004). He even assured
Van Treese's wife over the phone that everything was fne
and that he had seen Van Treese that morning. 4 Tr. 99–
100 (May 14, 2004).
Page Proof Pending Publication
   Glossip later repeated to a local police offcer the story that
two drunks had broken the window and that he had seen
Van Treese that morning. 9 Tr. 194, 206–207 (May 21, 2004).
Unpersuaded, the offcer checked the room with the broken
window and discovered Van Treese's body. Id., at 220, 224–
225; 11 Tr. 191, 194 (May 25, 2004). Glossip immediately told
the offcer that he suspected that Sneed had something to do
with the murder, explaining that he had heard glass breaking
and that Sneed had banged on his door, but he did not claim
to know anything more. 9 Tr. 233 (May 21, 2004).
   Homicide detectives interviewed Glossip later that night.
Tr. of Glossip Police Interview 1, 10–11 (Jan. 8, 1997). He
denied knowing that Van Treese had been murdered before
the body was discovered. Id., at 70, 86. And, he vacillated
between doubting that Sneed was involved and asserting
that he likely was. Id., at 27–28, 69–70.
   On the morning of January 8, Glossip began to sell all his
possessions, telling multiple witnesses that he would like to
leave town. 8 Tr. 88 (May 20, 2004); 11 Tr. 199 (May 25,
                   Cite as: 604 U. S. 226 (2025)           267

                     Thomas, J., dissenting

2004). On January 9, police picked up Glossip after he failed
to appear for a meeting with homicide detectives. 12 Tr. 7
(May 26, 2004). He had $1,757 in cash on his person and
no explanation for how he—living paycheck to paycheck and
having made only $490 from selling his possessions the pre-
vious day—had so much cash. Id., at 12–13; 14 Tr. 43–44
(May 28, 2004); 15 Tr. 17, 93 (June 1, 2004).
   Glossip sat for a second interview with homicide detectives
later that day. Tr. of Glossip Police Interview 1 (Jan. 9,
1997). This time, although continuing to deny that he had
ordered Sneed to kill Van Treese, Glossip admitted that
Sneed had told him about the murder just after committing
it, and that he had instructed Sneed to clean up the glass
and repair the window. Id., at 13–14, 36. Glossip also ad-
mitted that Van Treese “was upset because the motel wasn't
doing as well as it could.” Id., at 32. When asked why he
hid the murder, Glossip denied doing so to protect Sneed.
Page Proof Pending Publication
He said he covered up the murder instead to protect himself,
because he “was involved in it” and risked losing his girl-
friend otherwise. Id., at 29–30.
   During this interview, Glossip also tried to minimize his
involvement in the crime by insisting that he had not gone
inside Van Treese's hotel room after the attack. Id., at 18;
see also ante, at 232 (emphasizing this denial). At trial,
however, a motel resident testifed that, on the morning of
January 7, Glossip had said that he and Sneed had been “in
the room” after the window was broken. 9 Tr. 120 (May
21, 2004).
   Police arrested Sneed fve days later and charged him with
capital murder. 2 App. 644–645. He had $1,680 in cash in
his possession. 14 Tr. 12–18 (May 28, 2004). At frst, Sneed
denied involvement, claiming that his brother and Glossip
had once discussed the idea but that it never went beyond
talk. 2 App. 655–657. Later in the interview, however,
Sneed confessed to murdering Van Treese at Glossip's insti-
gation. Id., at 660, 664.
268                 GLOSSIP v. OKLAHOMA

                     Thomas, J., dissenting

                               B
                                1
   Glossip was convicted and sentenced to death in 1998, but
the OCCA ordered a retrial based on ineffective assistance
of counsel. 2001 OK CR 21, 29 P. 3d 597.
   At his second trial in 2004, a jury convicted Glossip again,
and the judge again sentenced him to death. Sneed testifed
against Glossip during the guilt phase, as he had at the frst
trial. While Sneed was providing background information
about himself at the outset of this testimony, the State's lead
prosecutor, Connie Smothermon, asked him whether he had
received any “prescription medication” after being arrested.
12 Tr. 63–64 (May 26, 2004). Sneed responded that he had
briefy been prescribed “Lithium for some reason, I don't
know why. I never seen no psychiatrist or anything.” Id.,
at 64. The matter did not come up again during the trial.
   It would not have been challenging for the parties to de-
Page Proof Pending Publication
duce the reason for Sneed's lithium prescription. It is un-
disputed that lithium's sole medical purpose, both in 1997 and
today, is to treat bipolar disorder and other mental health
disorders. See ante, at 247. Were there any doubt about
Sneed's condition, records long available to both sides resolve
it. In 1997, Sneed underwent a pretrial competency evalua-
tion with forensic psychologist Dr. Edith King. Dr. King's
report strongly suggested that although Sneed himself may
have been in denial, he was taking lithium to treat bipo-
lar disorder or a similar condition. During his evaluation,
Sneed asserted that he “d[id] not think he ha[d] any serious
mental problems.” 2 App. 701. And, he reported he was
given the lithium, apparently by mistake, “after his tooth
was pulled.” Id., at 700. Dr. King felt otherwise. Con-
cluding that Sneed qualifed as a “mentally ill person or a
person requiring treatment,” ibid., she determined that he
likely had “an atypical mood swing disorder in his past char-
acterized by `ups and downs' including anger outburst.” Id.,
                   Cite as: 604 U. S. 226 (2025)            269

                     Thomas, J., dissenting

at 702. “His present medication [i.e., the lithium] is prob-
ably helping him control his moods.” Ibid.
   The defense was well aware of this report before Glossip's
second trial. In fact, on direct appeal of his frst conviction,
Glossip's appellate counsel had faulted his trial counsel for
not using Dr. King's report to show the jury that Sneed was
taking lithium to control his anger. 1 id., at 18. Neverthe-
less, after the OCCA vacated his frst conviction, Glossip de-
clined to seek further pretrial discovery on the issue or raise
it during his second trial.
   After his second conviction and sentence, Glossip ignored
the lithium issue on direct appeal, instead raising a general
suffciency-of-the-evidence challenge. The OCCA unani-
mously rejected that challenge, fnding that there was suff-
cient evidence to convict and that the State had satisfed an
additional state-law requirement for corroborative evidence
where a conviction rests on accomplice testimony. 2007 OK
CR 12, ¶¶47–53, 157 P. 3d 143, 153–154. Two judges dis-
Page Proof Pending Publication
sented on different grounds but “agree[d] with the majority
that the State presented a strong circumstantial case against
Glossip.” Id., at 175 (Chapel, J.); see also ibid. (A. John-
son, J.).
                               2
   Glossip has spent the past two decades challenging his con-
viction and sentence through direct appeal, state and federal
collateral proceedings, and civil litigation under Rev. Stat.
§ 1979, 42 U. S. C. § 1983. Throughout that time, no court
has “determined error in [his] trial proceeding” or found that
“there [has] been a showing of actual innocence.” 2023 OK
CR 5, ¶2, 529 P. 3d 218, 229 (Lumpkin, J., specially concur-
ring). And, for almost that entire duration, the Oklahoma
attorney general has steadfastly defended the verdict and
sentence, insisting that the evidence the State presented in
1998 and 2004 has never “been credibly rebutted.” 3 App.
769.
270                 GLOSSIP v. OKLAHOMA

                      Thomas, J., dissenting

   In 2022, as Glossip's execution date approached, a group of
Oklahoma legislators opposed to his execution commissioned
the law frm Reed Smith LLP to conduct an independent
investigation of his case. The frm, which is publicly com-
mitted to “fghting the death penalty,” id., at 709, n. 3 (alter-
ation and internal quotation marks omitted), issued a fnal
report expressing “grave doubt as to the integrity of Gloss-
ip's murder conviction and death sentence,” Independent In-
vestigation of State v. Richard E. Glossip 6 (June 7, 2022)
(Reed Smith Report). The attorney general vigorously dis-
agreed. In subsequent post-conviction flings, the State as-
serted that the report was “built on assumptions, half-truths,
and (in some cases) outright falsehoods,” 3 App. 769, and
criticized its fndings at length, see id., at 754–769.
   In response to the Reed Smith Report, the attorney gener-
al's offce released all its fles from the case to Glossip, except
for one box of attorney work product. Based on this infor-
Page Proof Pending Publication
mation, Glossip fled a fourth motion for post-conviction relief
in the OCCA, raising two overarching claims. The frst
claim was that the State violated Brady v. Maryland, 373
U. S. 83 (1963), by withholding evidence that Sneed consid-
ered recanting his original testimony before the second trial.
The second claim was that Smothermon, the lead prosecutor,
committed misconduct and violated the rule of sequestration
(which prohibits witnesses from hearing other witnesses' tes-
timony) during trial. After the State's forensic pathologist
testifed that there was evidence Sneed used a knife in addi-
tion to the bat during the murder, Smothermon sent a memo-
randum to Sneed's attorney highlighting ways in which this
testimony was hard to square with some of Sneed's earlier
statements. Glossip thus claimed Smothermon violated the
rule of sequestration by conveying witness statements for
the purpose of coaching Sneed into altering his testimony to
ft the forensic evidence. Attorney General John O'Connor
opposed the application, urging the OCCA not to be cowed
                        Cite as: 604 U. S. 226 (2025)                      271

                           Thomas, J., dissenting

by the ongoing “public relations campaign” to “falsely” pres-
ent Glossip as “innocent.” 3 App. 717.
   The OCCA unanimously denied the application. Under
Oklahoma's Post-Conviction Procedure Act (PCPA), Glossip's
post-conviction application could not proceed unless he could
show (1) that the “factual basis for the claim” was previously
unavailable and (2) that, but for the alleged error, no rea-
sonable jury would have convicted him or sentenced him
to death. Okla. Stat., Tit. 22, § 1089(D)(8)(b) (2024). The
OCCA held that both claims failed the frst requirement be-
cause they were not based on new information. It also held
that Glossip's claims failed on the merits.
   As to the recantation claim, the OCCA held that Glossip's
frst claim was procedurally barred because the defense
knew even before the 2004 trial that Sneed was reluctant to
testify again. 3 App. 777. In fact, one of Glossip's attor-
neys had even visited Sneed before trial in an effort to per-
suade him not to testify. Ibid. On the merits, there was
Page Proof Pending Publication
“no evidence that Sneed had any desire to recant or change
his testimony.” Id., at 776. Sneed had even told Reed
Smith that “ `recant[ing]' ” was “ `impossible because I told the
truth.' ” Id., at 724. Sneed was reluctant to testify because
he wanted to obtain a better plea deal or to avoid the disrup-
tion to his life that testifying would cause. Id., at 776.2

  2
    The majority points to a letter from Sneed to his attorney in which Sneed
raised the prospect of “ ` “recanting” ' ” his trial testimony. Ante, at 238
(quoting 3 App. 815). But, in two subsequent interviews with Reed Smith
attorneys, Sneed made clear that, although he wanted to avoid testifying
again if possible, he continued to stand by the truth of his earlier testimony:
  “[REED SMITH ATTORNEY]: Yeah. Well, I think the bottom line
here, the most important things that we needed to clarify was like when
you're talking about recanting, you're not talking about changing your
story about what happened. Have you ever indicated to anybody that
you ever wanted to change your story about what happened?
  “JUSTIN SNEED: No, sir. I have not ever indicated that I wanted to
change the truth of him applying pressure to me.” App. to Response to
272                    GLOSSIP v. OKLAHOMA

                         Thomas, J., dissenting

  Turning to the sequestration claim, the OCCA pointed out
that Smothermon had acknowledged at trial that she had
spoken with Sneed's counsel, so the claim likewise lacked a
new factual basis. Id., at 780; see 12 Tr. 107–108 (May 26,
2004). On the merits, the court held that Oklahoma's se-
questration statute does not prohibit counsel from discussing
with a witness other witnesses' testimony. 3 App. 781.
Federal courts have similarly interpreted the federal seques-
tration rule to permit “witnesses . . . to discuss the case”
with “counsel for either side.” 2A C. Wright & P. Henning,
Federal Practice and Procedure § 416, p. 195, and n. 29 (4th
ed. 2009) (collecting cases). And, nothing in Smothermon's
memorandum indicates she was encouraging Sneed to lie. 3
App. 781–782.
                               3
  In January 2023, Gentner Drummond became Oklahoma's
attorney general. During his frst month in offce, Drum-
Page Proof Pending Publication
mond released the fnal box of evidence (Box 8) to Glossip.
He also appointed Rex Duncan, a personal friend and cam-
paign donor, as independent counsel to reexamine the legiti-
macy of Glossip's conviction.
  Among the materials released in Box 8 were handwritten
notes taken by Smothermon and her co-counsel Gary Ackley
during a 2003 meeting between them, Sneed, and Sneed's
attorney.

Petitioner's Succ. Application for Post-Conviction Relief in No. PCD–
2022–819 (OCCA), Tr. of Sneed Reed Smith Interview 46–47 (Aug. 15,
2022).
   See also id., Tr. of Sneed Reed Smith Interview 24 (Sept. 7, 2022)
(“There isn't any way of really making up some [new] storyline that isn't
going to cover all the evidence that is already there . . . ”). Sneed has
never on any occasion indicated that his testimony that Glossip directed
him to kill Van Treese was false, see 3 App. 724–725, and the majority
cites no such occasion. The best explanation for Sneed's letter, and the
one that the OCCA credited as factual, is thus that Sneed, an eighth-grade
dropout, used the phrase “recanting my testimony” imprecisely to mean
“refuse to testify.” Id., at 725, and n. 13, 776.
                     Cite as: 604 U. S. 226 (2025)          273

                       Thomas, J., dissenting

   Glossip's counsel quickly seized on Smothermon's notes.
In the top left corner of the notes, Smothermon had written
“on Lithium?” and “Dr Trumpet?” See Figure 1, infra.
According to Glossip's counsel, these phrases meant that
Sneed had admitted during the meeting that he had been
prescribed lithium by Dr. Lawrence Trombka, the psychia-
trist at the Oklahoma County Jail.
   Smothermon and Ackley disagree with this interpretation.
They assert before this Court that, during the meeting,
Sneed recounted two interviews that he previously had with
members of Glossip's defense team. In context, Smother-
mon's notes simply record that Sneed told her that Glossip's
defense team had asked him about his use of lithium and
about “Dr Trumpet.” The prosecutors claim that this fact
is apparent from the other notes on the page and from
Ackley's notes, both of which refer to details of these prior
interviews. Ackley's notes also highlight the phrase “ `tooth
pulled.' ” 3 App. 940. The prosecutors' interpretation of
Page Proof Pending Publication
their own notes thus suggests that Sneed recounted that he
had responded to questions about lithium and Dr. Trombka




Figure 1. Smothermon's handwritten notes. See 3 App. 927.
274                     GLOSSIP v. OKLAHOMA

                           Thomas, J., dissenting

with his earlier story that he was prescribed lithium in
error after having his tooth pulled. This interpretation
is explained at great length by the Van Treese family's
brief. See Brief for Victim Family Members as Amici
Curiae 7–22.3 And, as of yet, no one—including the par-
  3
    According to Smothermon, her notes refect two visits (“2X”) by de-
fense representatives—with notes about the two visits separated by a ho-
rizontal line. According to the notes above the line, Sneed's frst visitors
were “women,” one of whom was an investigator (“invest.”) who may have
been heavy set (“heavy set?”). These visitors may have been involved in
Glossip's earlier direct “appeal.” These women asked Sneed whether he
was “on Lithium?” and about a “Dr Trumpet?” The notes also document
a discussion of a “waiver for records,” “IQ test,” and “GED. VoTech.”
Similarly, Ackley's notes record that the “W[itness, i.e., Sneed,] was visited
by 2 women who said they rep Glossip.” They were “heavy,” “1 `Inv.' &
1 `Atty,' ” who may have been on Sneed's “Appellate” team. These two
women asked Sneed about lithium (“Li”), and he responded with some-
thing about getting his “ `tooth pulled.' ” Brief for Victim Family Mem-
bers as Amici Curiae 9–12.
Page Proof Pending Publication
   These notes correspond to Sneed's 2001 meeting with Wyndi Hobbs
(Glossip's post-conviction counsel) and an investigator named Lisa Cooper,
which was documented in the record of Glossip's fourth post-conviction
application. See 3 App. 729–730. At this meeting, Sneed “ `signed re-
leases for juvenile, jail, prison and criminal records,' ” id., at 729, which
corresponds to the “waiver for records” mentioned in Smothermon's notes.
Sneed later wrote a letter to Cooper to ensure that she received informa-
tion about his participation in a “vo-tech program,” id., at 730, which cor-
responds to the reference to “GED. VoTech.”
   According to Smothermon's notes below the line, Sneed's second visit
was from a “man” named “Burch” who tried to “con [him] out” of giving
“testimony” against Glossip. Burch “gave [Sneed a] case.” Ackley's
notes likewise indicate that Sneed “[l]ater” met with “1 guy” named
“Burch.” Sneed said of the meeting, ` “Basically all he was trying to do
was con me out of not [sic] getting onto the stand.' ” Brief for Victim
Family Members as Amici Curiae 9–13 (alteration in original).
   The flings from Glossip's fourth application also recount that Lynne
Burch, one of Glossip's attorneys, met with Sneed after the OCCA vacated
Glossip's frst conviction. 3 App. 731. Burch told Sneed “ `he didn't have
to testify' ” in Glossip's second trial, and (in line with Smothermon's notes)
gave Sneed a case, State v. Dyer, 2001 OK CR 31, 34 P. 3d 652, holding
that the State could not renege on a plea agreement for refusing to testify
at a codefendant's second trial. 3 App. 731–732.
                   Cite as: 604 U. S. 226 (2025)           275

                     Thomas, J., dissenting

ties and the majority—has attempted to refute it on the
merits.
   Based on Smothermon's notes, Glossip fled a ffth post-
conviction application in the OCCA in March 2023. He
framed the notes as new evidence of Sneed's previously un-
known bipolar disorder. Glossip attached an affdavit from
Dr. Trombka stating that he was the only person who would
have prescribed lithium while Sneed was in jail. Glossip
also attached what appears to be a jail record indicating that
Sneed has bipolar disorder. He argued that the State's re-
fusal to produce these notes before trial violated Brady, on
the theory that he could have used Sneed's condition to im-
peach his testimony.
   At the same time, Glossip recognized that he would need
additional evidence to prove his theory. Together with his
application, Glossip also fled a motion for an evidentiary
hearing, in which he sought to call Smothermon and Ackley
as witnesses. Motion for Evidentiary Hearing in No. PCD–
Page Proof Pending Publication
2023–267 (OCCA), p. 2. Glossip explained in the motion that
“the resolution” of his Brady claim “turns in part on inter-
pretation of prosecutors' notes.” Motion for Evidentiary
Hearing, at 1. “Without their testimony,” he acknowledged,
“any fnding about what they meant or what the attorneys
did or did not know when they wrote them would be specula-
tion.” Id., at 1–2.
   Independent Counsel Duncan, on the other hand, deter-
mined that no further evidence was needed. Duncan re-
leased his fnal report shortly after Glossip fled his ffth
application. He agreed that the State violated Glossip's
Brady rights and asserted that Smothermon's failure to cor-
rect Sneed's testimony amounted to a due process violation
under Napue v. Illinois, 360 U. S. 264 (1959). Duncan based
his conclusions on the speculation that “seasoned capital
homicide prosecutors . . . could be expected” to know that
“Trumpet” referred to Dr. Trombka and that Dr. Trombka
was the psychiatrist at the Oklahoma County Jail. App. to
Reply Brief in Support of Pet. for Cert. 23a. He then con-
276                    GLOSSIP v. OKLAHOMA

                         Thomas, J., dissenting

cluded the report with praise for Drummond, stating that
Drummond's “decision to seek a stay of execution and more
thoroughly examine this case may be the bravest leadership
decision I've ever witnessed.” Id., at 30a.
   Notably, Duncan failed to give Smothermon a meaningful
opportunity to explain what her notes may have meant or
what she knew about Sneed's medical history. Instead, he
discussed the matter with her only once, during a 3-minute
phone call. App. to Brief for Victim Family Members as
Amici Curiae 31a. Worse, he gave Smothermon no chance
to review the decades-old notes before asking her to explain
them during the brief call. Ibid. Drummond was likewise
uninterested in hearing from the attorney he and Duncan
were impugning. Following Duncan's report, both Smother-
mon and the Van Treese family contacted Drummond's offce
to request that Drummond speak with Smothermon about
the notes. Id., at 6a–7a, 71a. Their pleas were ignored.4
  At the attorney general's behest, the State supported
Page Proof Pending Publication
Glossip's post-conviction application. It argued that Smoth-
ermon's notes proved that the prosecutors violated Brady
and Napue, and that Glossip was entitled to relief under the
State's PCPA. It neglected to address, however, the strin-
gent limitations that the PCPA imposes on such subsequent
applications. See § 1089(D)(8)(b).

  4
    The majority insists that Smothermon had a fair opportunity to explain
her notes because she met once with attorneys at the Reed Smith law frm
and had an earlier, longer phone call with Duncan. Ante, at 255. But,
the Reed Smith meeting occurred before the release of Box 8. See Reed
Smith Report 80, n. 321 (noting that the Reed Smith meeting occurred in
May 2022, eight months before Box 8 was released in January 2023).
And—by his own admission—Duncan “forgot to ask” Smothermon about
“Dr. Larry Trombka” during his earlier, longer phone call. App. to Brief
for Victim Family Members as Amici Curiae 32a. The majority also
faults Smothermon for not having an explanation ready during the 3-
minute phone call. Ante, at 255. But, without giving Smothermon an
opportunity to review the notes, it was unreasonable to expect her instan-
taneously to recall their meaning 20 years later.
                  Cite as: 604 U. S. 226 (2025)           277

                     Thomas, J., dissenting

   The OCCA unanimously denied Glossip's ffth post-
conviction application. The court frst held that Glossip had
not satisfed either requirement of § 1089(D)(8)(b), and thus
that the Brady and Napue claims were procedurally barred.
529 P. 3d, at 226. The OCCA then held that both claims also
failed on the merits. No Brady violation occurred, the court
explained, because Sneed's 1997 pretrial competency report
already informed the defense of Sneed's prescription and
condition. The OCCA determined that defense counsel had
likely made a strategic decision not to base a defense on
them. 529 P. 3d, at 226. Nor was there any Napue viola-
tion, according to the court, because Sneed's testimony “was
not clearly false” and, in any event, was not material given
defense counsel's choice not to raise Sneed's condition. 529
P. 3d, at 226–227. After the OCCA issued its decision, Okla-
homa's Pardon and Parole Board denied clemency.
                             II
Page Proof Pending Publication
   As an initial matter, we lack jurisdiction to review this
case. “This Court from the time of its foundation has ad-
hered to the principle that it will not review judgments of
state courts that rest on adequate and independent state
grounds.” Herb v. Pitcairn, 324 U. S. 117, 125 (1945). “Be-
cause this Court has no power to review a state law deter-
mination that is suffcient to support the judgment, resolu-
tion of any independent federal ground for the decision could
not affect the judgment and would therefore be advisory.”
Coleman v. Thompson, 501 U. S. 722, 729 (1991). Thus, on
direct review of a state-court judgment, the presence of an
adequate and independent state ground imposes a “jurisdic-
tional” limitation. Ibid. The decision below rests on such
grounds, and the majority concludes otherwise only by
grossly mischaracterizing the state court's analysis.
                             A
  The PCPA authorizes a criminal defendant to collaterally
challenge his conviction on the ground that it violates the
278                 GLOSSIP v. OKLAHOMA

                      Thomas, J., dissenting

Federal Constitution. Okla. Stat., Tit. 22, § 1080(1). But,
given the extraordinary nature of collateral challenges, the
statute also imposes a variety of restrictions on relief. In
capital cases, the applicant must establish not just a constitu-
tional violation, but also, among other requirements, that his
claim “could not have been raised in a direct appeal” and that
“the outcome of the trial would have been different but for
the errors or that the defendant is factually innocent.”
§ 1089(C).
   

[...TRUNCATED 59914 of 179914 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Go-Bart Importing Co. v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Go-Bart Importing Co. v. United States"
type: case
citation: "282 U.S. 344 (1931)"
parallel_cite: "51 S. Ct. 153; 75 L. Ed. 374"
neutral_cite: 1931 U.S. LEXIS 842
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1931
date_decided: 1931-01-05
docket: 111
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1931-01-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Go-Bart Importing Co. v. United States
  varies_by_point: false
  scope_note: "Foundational early limit on search incident to arrest; the principle that a SITA may not become a general exploratory search of the premises survives and was reaffirmed/structured in Chimel v. California."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/101643/go-bart-importing-co-v-united-states/"
  cluster_id: 101643
  opinion_id: 101643
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Historical / Foundational"
related: ["[[Chimel v. California]]", "[[Agnello v. United States]]", "[[United States v. Robinson]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "general-search", "historical", "reasonableness"]
holding: "A search incident to arrest may not become a general exploratory search of the premises; a warrantless arrest used to justify ransacking an office for evidence is an unreasonable general search, judged on each case's own facts."
lake:
  record_id: Go-Bart Importing Co. v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Go-Bart Importing Co. v. United States

*282 U.S. 344 (1931)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Prohibition agents, acting on an invalid warrant issued by a commissioner who lacked authority, entered the petitioners' import-company office, arrested Gowen and Bartels, and — under a false claim of having a warrant and by threat of force — compelled Gowen to open his desk and safe. The agents then ransacked the desk, safe, filing cabinets, and other parts of the office, seizing papers, even though they had ample information and time to obtain a valid warrant.

## Issue
Whether a warrantless general search and seizure of papers throughout an office, conducted incident to an arrest, is a reasonable [[Search Incident to Arrest|search incident to arrest]] or an unconstitutional general search.

## Rule
Reasonableness is fact-specific: "There is no formula for the determination of reasonableness. Each case is to be decided on its own facts and circumstances." — 282 U.S. at 357. ^pin-357

A [[Search Incident to Arrest|search incident to arrest]] may not become a general rummaging of the premises: by "pretension of right and threat of force he compelled Gowen to open the desk and the safe and with the others made a general and apparently unlimited search, ransacking the desk, safe, filing cases and other parts of the office. It was a lawless invasion of the premises and a general exploratory search in the hope that evidence of crime might be found." — *Id.* at 358. ^pin-358

## Application
Unlike *Marron v. United States* — where officers executing a valid warrant seized a ledger and bills that were "visible and accessible and in the offender's immediate custody," with "no threat of force or general search or rummaging" — the agents here arrested the men without seeing any crime, then forced open the desk and safe and ransacked the entire office for evidence under a false claim of authority. That was a general exploratory search, not a permissible incident of the arrest, and was unreasonable.

## Conclusion
Reversed. The general search of the office was unreasonable; the papers had to be suppressed and returned. *Go-Bart* fixes an early outer limit on [[Search Incident to Arrest|search incident to arrest]] — it cannot be converted into a general exploratory search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The general-exploratory-search limit survives and was given its modern structure in [[Chimel v. California]] (SITA confined to the arrestee's person and the area within immediate control); it is companion to [[Agnello v. United States]]. (The Court's contemporaneous "mere evidence" assumptions, drawn from *[[Gouled v. United States|Gouled]]*, were later changed by *[[Warden v. Hayden]]* — but that does not disturb *Go-Bart*'s search-incident-to-arrest holding.)

## Appears on
- [[SIA Persons]] — *Key — Historical / Foundational*

## Sources
- *Go-Bart Importing Co. v. United States*, 282 U.S. 344 (1931) — https://www.courtlistener.com/opinion/101643/go-bart-importing-co-v-united-states/ — pinpoints: 357, 358.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "09a126fa30699b95", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Go-Bart Importing Co. v. United States"}, "payload": {"all": [{"cite": "282 U.S. 344", "page": "344", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "282"}, {"cite": "51 S. Ct. 153", "page": "153", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "51"}, {"cite": "75 L. Ed. 374", "page": "374", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "75"}, {"cite": "1931 U.S. LEXIS 842", "page": "842", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1931"}], "display": "282 U.S. 344", "official": {"cite": "282 U.S. 344", "page": "344", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "282"}, "official_selection_present": true, "record_id": "Go-Bart Importing Co. v. United States"}}
{"assertion_id": "40dc549b795e452f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-358", "record_id": "Go-Bart Importing Co. v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-358", "pinpoint_status": "slip-only", "quote": "pretension of right and threat of force he compelled Gowen to open the desk and the safe and with the others made a general and apparently unlimited search, ransacking the desk, safe, filing cases and other parts of the office. It was a lawless invasion of the premises and a general exploratory search in the hope that evidence of crime might be found.", "quote_fidelity": "mismatch", "record_id": "Go-Bart Importing Co. v. United States", "star_marker": null}}
{"assertion_id": "f1db8d6e64c82ff1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-357", "record_id": "Go-Bart Importing Co. v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-357", "pinpoint_status": "slip-only", "quote": "--- # Go-Bart Importing Co. v. United States *282 U.S. 344 (1931)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Prohibition agents, acting on an invalid warrant issued by a commissioner who lacked authority, entered the petitioners' import-company office, arrested Gowen and Bartels, and — under a false claim of having a warrant and by threat of force — compelled Gowen to open his desk and safe. The agents then ransacked the desk, safe, filing cabinets, and other parts of the office, seizing papers, even though they had ample information and time to obtain a valid warrant. ## Issue Whether a warrantless general search and seizure of papers throughout an office, conducted incident to an arrest, is a reasonable search incident to arrest or an unconstitutional general search. ## Rule Reasonableness is fact-specific:", "quote_fidelity": "mismatch", "record_id": "Go-Bart Importing Co. v. United States", "star_marker": null}}
{"assertion_id": "92a6efbf7a608f4e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Go-Bart Importing Co. v. United States"}, "payload": {"as_of_content": "1931-01-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Go-Bart Importing Co. v. United States", "scope_note": "Foundational early limit on search incident to arrest; the principle that a SITA may not become a general exploratory search of the premises survives and was reaffirmed/structured in Chimel v. California.", "varies_by_point": false}}
```

### lake record — Go-Bart Importing Co. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Go-Bart Importing Co. v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Go-Bart Importing Co. v. United States",
    "case_name_short": "",
    "case_name_full": "GO-BART IMPORTING COMPANY Et Al. v. UNITED STATES",
    "input_case_name": "Go-Bart Importing Co. v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1931-01-05",
    "year": 1931,
    "docket": "111",
    "cluster_id": 101643,
    "lead_opinion_id": 101643,
    "sibling_ids": [
      101643
    ],
    "absolute_url": "/opinion/101643/go-bart-importing-co-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "282 U.S. 344",
      "volume": "282",
      "reporter": "U.S.",
      "page": "344",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "51 S. Ct. 153",
        "volume": "51",
        "reporter": "S. Ct.",
        "page": "153",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 374",
        "volume": "75",
        "reporter": "L. Ed.",
        "page": "374",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1931 U.S. LEXIS 842",
        "volume": "1931",
        "reporter": "U.S. LEXIS",
        "page": "842",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "282 U.S. 344",
        "volume": "282",
        "reporter": "U.S.",
        "page": "344",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 S. Ct. 153",
        "volume": "51",
        "reporter": "S. Ct.",
        "page": "153",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 374",
        "volume": "75",
        "reporter": "L. Ed.",
        "page": "374",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1931 U.S. LEXIS 842",
        "volume": "1931",
        "reporter": "U.S. LEXIS",
        "page": "842",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "282 U.S. 344",
    "official_selection": {
      "court_class": "scotus",
      "selected": "282 U.S. 344",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-357",
      "page": null,
      "quote": "--- # Go-Bart Importing Co. v. United States *282 U.S. 344 (1931)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Prohibition agents, acting on an invalid warrant issued by a commissioner who lacked authority, entered the petitioners' import-company office, arrested Gowen and Bartels, and \u2014 under a false claim of having a warrant and by threat of force \u2014 compelled Gowen to open his desk and safe. The agents then ransacked the desk, safe, filing cabinets, and other parts of the office, seizing papers, even though they had ample information and time to obtain a valid warrant. ## Issue Whether a warrantless general search and seizure of papers throughout an office, conducted incident to an arrest, is a reasonable search incident to arrest or an unconstitutional general search. ## Rule Reasonableness is fact-specific:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-358",
      "page": null,
      "quote": "pretension of right and threat of force he compelled Gowen to open the desk and the safe and with the others made a general and apparently unlimited search, ransacking the desk, safe, filing cases and other parts of the office. It was a lawless invasion of the premises and a general exploratory search in the hope that evidence of crime might be found.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1931-01-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Go-Bart Importing Co. v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational early limit on search incident to arrest; the principle that a SITA may not become a general exploratory search of the premises survives and was reaffirmed/structured in Chimel v. California.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pacemaker Diagnostic Clinic of America, Inc., a Corporation, Plaintiff- Cross-Appellee v. Instromedix, Inc., a Corporation, Cross-Appellant",
          "cluster_id": 429819,
          "cite": [
            "725 F.2d 537",
            "1984 U.S. App. LEXIS 25408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gill v. State",
          "cluster_id": 1770662,
          "cite": [
            "625 S.W.2d 307",
            "1981 Tex. Crim. App. LEXIS 1283"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Superior Court",
          "cluster_id": 5806373,
          "cite": [
            "102 Cal. App. 3d 342",
            "162 Cal. Rptr. 295",
            "1980 Cal. App. LEXIS 1491"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Super Spuds, Inc. v. New York Mercantile Exchange",
          "cluster_id": 9343908,
          "cite": [
            "591 F.2d 174",
            "26 Fed. R. Serv. 2d 1010"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dolan",
          "cluster_id": 6330597,
          "cite": [
            "95 Misc. 2d 470",
            "1978 N.Y. Misc. LEXIS 2449",
            "408 N.Y.S.2d 249"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Bianco",
          "cluster_id": 7427525,
          "cite": [
            "55 Cal. App. Supp. 3d 8",
            "127 Cal. Rptr. 92",
            "1975 Cal. App. LEXIS 1842"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guzman v. Estelle",
          "cluster_id": 8905678,
          "cite": [
            "493 F.2d 532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Baird",
          "cluster_id": 2118432,
          "cite": [
            "18 Cal. App. 3d 450",
            "95 Cal. Rptr. 700",
            "1971 Cal. App. LEXIS 1399"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rabinowitz",
          "cluster_id": 104769,
          "cite": [
            "94 L. Ed. 2d 653",
            "70 S. Ct. 430",
            "339 U.S. 56",
            "1950 U.S. LEXIS 2298",
            "94 L. Ed. 653"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDonald v. United States",
          "cluster_id": 104605,
          "cite": [
            "93 L. Ed. 2d 153",
            "69 S. Ct. 191",
            "335 U.S. 451",
            "1948 U.S. LEXIS 1456"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freytag v. Commissioner",
          "cluster_id": 112644,
          "cite": [
            "115 L. Ed. 2d 764",
            "111 S. Ct. 2631",
            "501 U.S. 868",
            "1991 U.S. LEXIS 3818"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abel v. United States",
          "cluster_id": 106021,
          "cite": [
            "4 L. Ed. 2d 668",
            "80 S. Ct. 683",
            "362 U.S. 217",
            "1960 U.S. LEXIS 1412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. United States",
          "cluster_id": 104422,
          "cite": [
            "67 S. Ct. 1098",
            "331 U.S. 145",
            "91 L. Ed. 1399",
            "1947 U.S. LEXIS 2936"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "See v. City of Seattle",
          "cluster_id": 107474,
          "cite": [
            "18 L. Ed. 2d 943",
            "87 S. Ct. 1737",
            "387 U.S. 541",
            "1967 U.S. LEXIS 1255"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cobbledick v. United States",
          "cluster_id": 103311,
          "cite": [
            "309 U.S. 323",
            "60 S. Ct. 540",
            "84 L. Ed. 783",
            "1940 U.S. LEXIS 1091",
            "1940 Trade Cas. (CCH) 56,011"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(101643) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0tMjM1ODcyMDAwMDAmcz0yODQyNzEmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28101643%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(101643)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNzEmcz0xMTIyMDQzJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28101643%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(101643)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(101643)",
    "indexed_citing_opinions": 589,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 101643,
        "count": 589,
        "count_source": "search"
      }
    ],
    "citation_count": 885,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/go-bart-importing-co-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjUxOTcyODUmcz00MzIwNzMxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28101643%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 101643,
        "cited_id": 84827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 89309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 90713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 92143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 94069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 94212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 94408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 95422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 95722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 97412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 100375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 101264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 101354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 2425305,
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
    "date_created": "2026-07-05T05:36:41Z",
    "date_modified": "2026-07-06T07:51:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:36:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:36:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:40:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:36:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Go-Bart Importing Co. v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b412-5">
<span citation-index="1" class="star-pagination" label="348"> 
   *348
   </span>
  Mr. Justice Butler
 </author>
<p id="A9G">
  delivered the opinion of the Court.
 </p>
<p id="b412-6">
  In a criminal proceeding before a United States commissioner in the Southern District of New York in which Gowen, Bartels and others are defendants, the petitioners applied to the district court for an order enjoining the use as evidence of books and papers alleged to have been seized and taken from petitioners in violation' of the Fourth and Fifth Amendments and directing their return. The court made an order that the United States show' cause why the relief prayed should not be granted. The United States attorney appeared and opposed the motion, and affidavits of W. J. Calhoun, special agent in charge of special agents of the Bureau of Prohibition, and certain of his subordinates were filed in opposition. The district court denied the applications. The Circuit Court of Appeals affirmed as to the United States attorney and held that as to the special agent in charge the order to show cause should have been discharged. 40 F. (2d) 593.
 </p>
<p id="b412-7">
  Petitioners’ applications to the district court, which are in form affidavits, set forth the following:
 </p>
<p id="b413-2">
<span citation-index="1" class="star-pagination" label="349"> 
   *349
   </span>
  June 5, 1929, Calhoun went before the United States commissioner and, in order to have a warrant issued for the arrest of Gowen, Bartels and others, yerified and filed a complaint. He alleged, upon information and belief, that beginning January 1, 1929, and continuing down to the filing of the complaint Gowen, Bartels and other defendants conspired in that district to commit/ a nuisance against the United States, that is to say, to possess, transport, sell and solicit and receive orders for intoxicating liquor in violation of the National. Prohibition Act, and that, in pursuance of the conspiracy .and to effqct its objects, one Heath purchased an automobile on May 23, 1929. See <span class="citation no-link">27 U. S. C., §§ 33</span>, 35. The complaint did not specify any building, structure, location or place or set forth any particulars or other overt act or show any connection between the purchase of the automobile and any offense referred to in the complaint. On the same day the commissioner issued a warrant in the usual form commanding the marshal of the district and his deputies to apprehend the persons so accused and to bring them before the commissioner or some judge or justice of the United States to be dealt with according to law.
 </p>
<p id="b413-3">
  On the next day Calhoun's subordinates, prohibition agents O’Brien, Collins and Sipe, went to the petitioning company’s office at No. 200 Fifth Avenue. Bartels, the secretary-treasurer of the company, was there when they entered. O’Brien said he had a warrant to search the premises and exhibited a paper which he falsely claimed was such a warrant. The agents arrested Bartels, searched his person and took papers therefrom. While they were there Gowen, the president of the company, came to the office. O’Brien told him that he had a warrant for his arrest and a warrant to search the premises. The agents, arrested and searched Gowen and took papers from him. They took his keys and by threat of force compelled him to open a desk and safe, searched and took papers from
  <span citation-index="1" class="star-pagination" label="350"> 
   *350
   </span>
  them, searched other parts of the office and took therefrom other papers, journals, account books, letter files, insurance policies, cancelled checks, index cards and other things belonging respectively to.Gowen, Bartels and the company. For brevity these will be referred to herein as “ papers.”
 </p>
<p id="b414-4">
  Gowen and Bartels were on the same day arraigned before the commissioner and held on bail further to answer the complaint. A date was set for the examination, hearing has been postponed from time to time and no examination has been had. The paper's so seized were taken to the office of Calhoun in the Sub-Treasury Building where they were examined by him and the United States at-' torney and their subordinates, and such papers have since been kept and held there, as is later herein shown, under the control of the United States attorney in the care and custody of the special agent in charge, for use as evidence against Gowen and Bartels.
 </p>
<p id="b414-5">
  Soon after the seizures were made each of the petitioners brought a suit in equity in the federal court for that district against the special agent in charge and the United States attorney, to enjoin them from using such papers as evidence and to have them returned. The court dismissed these suits' on the ground that the proper remedy was by motion in the criminal proceedings.
 </p>
<p id="b414-6">
  Then Gowen and Bartels, each in his own behalf, and the company, acting through Bartels, made these applications. The court made its order that the United States show cause why an injunction should not issue restraining it and its officers from using as evidence the papers so seized and why an order should not issue directing their return.
 </p>
<p id="b414-7">
  ■ • In opposition, the affidavit of one Braidwood was submitted. It tends to show that in 1927. and 1928 petitioners and others acting together engaged in the unlawful sale of intoxicating liquor, that at the company’s office
  <span citation-index="1" class="star-pagination" label="351"> 
   *351
   </span>
  they exhibited and took orders for intoxicating- liquor some of which was delivered there and some elsewhere, and that in April,. 1929, he reported these facts to Calhoun. Calhoun’s affidavit states that Braidwood had so reported and that by independent investigations he had corroborated such statements and thus knew that a conspiracy unlawfully to sell intoxicating liquors in 1928 and 1929 had been entered into and overt acts in furtherance thereof had been performed within- the district and that he believed the petitioners had been parties to such conspiracy, that prior to the day of the arrests he communicated such statements and belief to O’Brien and assigned him to further investigate the case.
 </p>
<p id="b415-3">
  O’Brien’s affidavit states: From the information given him by Calhoun he believed petitioners and others had so conspired. Calhoun described to him the company’s office in detail and the personal appearance of Gowen and Bartels. On June 6, 1929, he took a certified copy of the complaint and warrant “ for the purpose of reference, as to the names of the various defendants ” and went to petitioners’ office. It-consisted of a suite of three rooms fitted up with office ..furniture including desks, filing cabinets and a safe. He told Bartels and Gowen that he was an officer of the United States and placed them under arrest, for such conspiracy. No warrant was “ served ” upon either of them. The office was searched and there were found and taken therefrom approximately a dozen-bottles of assorted intoxicating liquor, a large number of memo-randa, books of account, records, filing cases, and other papers all of which, pertained to unlawful dealings by Gowen and Bartels in intoxicating liquors.
 </p>
<p id="b415-4">
  O’Brien’s affidavit also states that the papers so seized are of such quantity and bulk that it is impracticable to attach copies to-the affidavit, that such papers are “ specifically incorporated herein by reference and made a part hereof and are further made ayailable for inspection at
  <span citation-index="1" class="star-pagination" label="352"> 
   *352
   </span>
  any time, if desired by the Court, in connection with the consideration of this order to show cause.”
 </p>
<p id="b416-5">
  In reply to O’Brien’s affidavit petitioners submitted affidavits of,. Gowen, Bartels and other defendants who were arrested at the company’s office on that occasion and affidavits of. other persons who were present during some part of the time that the prohibition agents were there. These affidavits show that O’Brien said he had a warrant of arrest and produced a paper which several of these affiants say they read and believe to be the warrant issued by the commissioner, a copy bf which was filed with the moving papers. As to these details there is no conflict in the evidence.
 </p>
<p id="AYZ9">
  The district court refused to sustain the contention that no use was made of thé warrant and accepted the state- ■ ments that O’Brien claimed to have warrants for the arrests and searches. The Circuit Court of Appeals did not definitely express opinion as to that matter. We have examined the evidence. It requires a finding that O’Brien did so claim, that he had the warrant issued by the commissioner or a copy of it and that when he arrested Gowen and Bartels he claimed and purported to act under the warrant. No warrant for the search of the premises was issued.
 </p>
<p id="b416-7">
  The orders dismissing petitioners’ suits in equity are not before us. The question whether the district court had jurisdiction summarily-to deal with petitioners’ applications, while not brought forward by the parties, arises upon the record, was considered by the Circuit Court of Appeals and suggested during the argument here.
 </p>
<p id="b416-8">
  United States, commissioners are inferior officers.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
<em>
   United States
  </em>
  v.
  <em>
   Allred,
  </em>
  <span class="citation" data-id="94069"><a href="/opinion/94069/united-states-v-allred/#594" aria-description="Citation for case: United States v. Allred">155 U. S. 591, 594</a></span>.
  <em>
   Rice
  </em>
  v.
  <em>
   Ames,
  </em>
<span citation-index="1" class="star-pagination" label="353"> 
   *353
   </span>
  <span class="citation" data-id="95422"><a href="/opinion/95422/rice-v-ames/#377" aria-description="Citation for case: Rice v. Ames">180 U. S. 371, 377, 378</a></span>. Cf.
  <em>
   Ex parte Hennen,
  </em>
  <span class="citation" data-id="2518125"><a href="/opinion/2518125/ex-parte-duncan-n-hennen/#257" aria-description="Citation for case: Ex Parte Duncan N. Hennen">13 Pet. 230, 257</a></span>,
  <em>
   et seg.
  </em>
  The Act of May 28, 1896, <span class="citation no-link">29 Stat. 184</span>, abolished commissioners of the circuit courts, authorized each district court to appoint United States commissioners, gave to them the same powers and duties that commissioners of the circuit courts had, required such appointments to be entered of record in the district courts, provided that the commissioners should hold their office subject to removal by the court appointing them (<span class="citation no-link">28 U. S. C., § 526</span>) and required them to keep records of proceedings before them in criminal cases and deliver the same to the clerks of the courts on the commissioners’ ceasing to hold office.
  <em>
   <span class="citation no-link">Id.,</span>
  </em>
  § 529. They are authorized by statute in respect of numerous matters
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  and the relations between them and the district courts vary as do their official acts. Cf.
  <em>
   United States
  </em>
  v.
  <em>
   Allred, ubi supra. Grin
  </em>
  v.
  <em>
   Shine,
  </em>
  <span class="citation" data-id="95722"><a href="/opinion/95722/grin-v-shine/#187" aria-description="Citation for case: Grin v. Shine">187 U. S. 181, 187</a></span>.
  <em>
   Todd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94212"><a href="/opinion/94212/todd-v-united-states/#282" aria-description="Citation for case: Todd v. United States">158 U. S. 278, 282</a></span>.
  <em>
   Collins
  </em>
  v.
  <em>
   Miller,
  </em>
  <span class="citation" data-id="99554"><a href="/opinion/99554/collins-v-miller/#369" aria-description="Citation for case: Collins v. Miller">252 U. S. 364, 369</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Berry,
  </em>
  <span class="citation" data-id="8121751"><a href="/opinion/8160102/united-states-v-berry/" aria-description="Citation for case: United States v. Berry">4 Fed. 779</a></span>.
  <em>
   Ex parte
  </em>
  Perkins, <span class="citation" data-id="8310779"><a href="/opinion/8342362/ex-parte-perkins/" aria-description="Citation for case: Ex parte Perkins">29 Fed. 900</a></span>.
  <em>
   The Mary,
  </em>
  <span class="citation" data-id="8799626"><a href="/opinion/8815150/the-mary/" aria-description="Citation for case: The Mary">233 Fed. 121</a></span>.
 </p>
<p id="b417-3">
  We need not consider what power the district court may exert over the commissioners dealing with matters unlike
  <span citation-index="1" class="star-pagination" label="354"> 
   *354
   </span>
  that now before us. Here the commissioner acted under R.'S., § 1014, which provides that for any crime or offense against the'United. States, the offender may by any justice or judge of the United States or by any commissioner of the circuit court to take bail (now United States commissioner) be arrested and imprisoned, or bailed, as the "case may be, for trial before such court of the United States as by law has cognizance of the offense. <span class="citation no-link">18 U. S. C., § 591</span>. All the commissioner’s acts and the things doné by the prohibition officers in respect of this matter were preparatory and preliminary to a consideration of the charge by a grand jury and, if an indictment should be found, the final disposition of the case in the district court. The commissioner acted not as a court, or as a judge of any court, but as a mere officer of the district court in proceedings of which that court had authority to take control at any time.
  <em>
   Todd
  </em>
  v.
  <em>
   United States, ubi supra. Collins
  </em>
  v.
  <em>
   Miller, ubi supra. United States
  </em>
  v.
  <em>
   <span class="citation" data-id="8121751"><a href="/opinion/8160102/united-states-v-berry/" aria-description="Citation for case: United States v. Berry">Berry, supra.</a></span> United States
  </em>
  v.
  <em>
   Casino,
  </em>
  <span class="citation" data-id="8829038"><a href="/opinion/8843817/united-states-v-casino/#979" aria-description="Citation for case: United States v. Casino">286 Fed. 976, 979</a></span>.
 </p>
<p id="Aba1">
  Notwithstanding the order to show cause was addressed to the United States alone, this is in substance and effect a proceeding against the United States attorney and the special agent in charge. The special agent in charge was the prosecuting witness. It was his duty under the statute to report violations to the United States attorney.
  <em>
   Donnelley
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101264"><a href="/opinion/101264/donnelley-v-united-states/" aria-description="Citation for case: Donnelley v. United States">276 U. S. 505</a></span>. And he was authorized, subject to. the control of the United States attorney, to “ conduct the prosecution at the committing trial for the purpose of having the offenders held for the action of a grand jury,” <span class="citation no-link">27 U. S. C., § 11</span>. It is immaterial whether he intended or was personally to conduct the prosecution before the commissioner. As the United States attorney had control of the prosecution‘before the commissioner, whether conducted by his assistants or prohibition agents, the papers were held subject to his control and direction although in the immediate care and custody
  <span citation-index="1" class="star-pagination" label="355"> 
   *355
   </span>
  of the prohibition officers. He and they voluntarily came before the court to defend the seizure, the retention and proposed use of the papers and so in effect became parties to the proceeding. By making the papers a part of O’Brien’s affidavit they brought the papers within the power of the court and constructively into its possession, if indeed the papers had not already come within its reach. In so far as it purports to run .against the United States, the form of the order may be treated as a mere irregularity.
 </p>
<p id="b419-3">
  The United States attorney and the special agent in charge, as officers authorized to conduct such prosecution and having .control and custody of the papers for that purpose, are, in respect of the acts relating to such prosecution, alike subject to the proper exertion of the disciplinary powers of the court. And on the facts here shown it is plain that the district court had jurisdiction summarily to determine whether the evidence should be suppressed and the papers returned to the petitioners.
  <em>
   Weeks
  </em>
  v.
  <em>
   United
  </em>
  States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#398" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 398</a></span>.
  <em>
   Wise
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="97412"><a href="/opinion/97412/wise-v-henkel/#558" aria-description="Citation for case: Wise v. Henkel">220 U. S. 556, 558</a></span>.
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#390" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 390</a></span>.
  <em>
   Cogen
  </em>
  v.
  <em>
   United States
  </em>
  <span class="citation" data-id="101354"><a href="/opinion/101354/cogen-v-united-states/#225" aria-description="Citation for case: Cogen v. United States">278 U. S. 221, 225</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Mills,
  </em>
  <span class="citation" data-id="8778272"><a href="/opinion/8794247/united-states-v-mills/" aria-description="Citation for case: United States v. Mills">185 Fed. 318</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   McHie,
  </em>
  <span class="citation" data-id="8782452"><a href="/opinion/8798345/united-states-v-mchie/#898" aria-description="Citation for case: United States v. McHie">194 Fed. 894, 898</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Lydecker,
  </em>
  <span class="citation" data-id="8822257"><a href="/opinion/8837179/united-states-v-lydecker/#980" aria-description="Citation for case: United States v. Lydecker">275 Fed. 976, 980</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Kraus,
  </em>
  <span class="citation" data-id="8819275"><a href="/opinion/8834265/united-states-v-kraus/#580" aria-description="Citation for case: United States v. Kraus">270 Fed. 578, 580</a></span>. Cf.
  <em>
   Applybe
  </em>
  v.
  <em>
   United States,
  </em>
  32 F. (2d) 873, 874.
 </p>
<p id="b419-4">
  The Government concedes that the warrant did not authorize O’Brien or other prohibition agents to make the arrests. The complaint, which in substance is recited in the warrant, was verified,merely on information and belief and does not state facts sufficient to constitute an offense.
  <em>
   Ex parte Burford,
  </em>
  <span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/#453" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448,453</a></span>.
  <em>
   Rice
  </em>
  v.
  <span class="citation" data-id="95422"><a href="/opinion/95422/rice-v-ames/#374" aria-description="Citation for case: Rice v. Ames"><em>
   Ames, supra,
  </em>
  374</a></span>.
  <em>
   Byars
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Cruikshank,
  </em>
  <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/#558" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542, 558</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Hess,
  </em>
  <span class="citation" data-id="92143"><a href="/opinion/92143/united-states-v-hess/" aria-description="Citation for case: United States v. Hess">124 U. S. 483</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Ruroede,
  </em>
  <span class="citation" data-id="8794535"><a href="/opinion/8810183/united-states-v-ruroede/" aria-description="Citation for case: United States v. Ruroede">220 Fed. 210</a></span>,
  <span citation-index="1" class="star-pagination" label="356"> 
   *356
   </span>
  212, 213. The warrant was improvidently issued and invalid on its face. It does not purport to authorize anyone other than the marshal and his deputies.
 </p>
<p id="b420-5">
  The company is not mentioned in the complaint or warrant and is a stranger to the proceeding before the commissioner. Unquestionably the order of the district court as to it was final and appealable.
  <em>
   Cogen
  </em>
  v.
  <em>
   United States, ubi supra. Ex parte Tiffany,
  </em>
  252 U., S. 32.
  <em>
   Savannah
  </em>
  v.
  <em>
   Jesup,
  </em>
  <span class="citation" data-id="9417350"><a href="/opinion/90713/savannah-v-jesup/" aria-description="Citation for case: Savannah v. Jesup">106 U. S. 563</a></span>.
  <em>
   Gumbel
  </em>
  v.
  <em>
   Pitkin,
  </em>
  <span class="citation" data-id="2425305"><a href="/opinion/2425305/gumbel-v-pitkin/" aria-description="Citation for case: Gumbel v. Pitkin">113 U. S. 545</a></span>: When the application was made, no information or indictment had been found'or returned against Gowen or Bartels. There was nothing to show that any criminal proceeding would ever be instituted in that court against them.
  <em>
   Post
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94408"><a href="/opinion/94408/post-v-united-states/#587" aria-description="Citation for case: Post v. United States">161 U. S. 583, 587</a></span>. And, as above shown, the complaint does not state an offense. It follows that the order of the district court was not made in. or dependent upon any case or proceeding there pending and therefore the order as to them was appealable.
  <em>
   Cogen
  </em>
  v.
  <em>
   United States, ubi supra. Perlman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99162"><a href="/opinion/99162/perlman-v-united-states/#13" aria-description="Citation for case: Perlman v. United States">247 U. S. 7, 13</a></span>.
  <em>
   Burdeau
  </em>
  v.
  <em>
   McDowell,
  </em>
  <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span>.
 </p>
<p id="b420-6">
  Without pausing to consider the matter, we assume, as held by the lower courts, that the facts of which Calhoun and O’Brien, had been informed prior to the arrests are sufficient to justify the apprehension without a warrant of Gowen and Bartels for the conspiracy referred to in Braidwood’s affidavit and on that basis we treat the arrests as lawful and valid.
 </p>
<p id="b420-7">
  No question is here raised as to the search of the persons. There remains for consideration the question whether the search of the premises, the seizure of the papers therefrom and their retention for use as evidence may. be sustained. The first, clause of the Fourth Amendment declares: “ The right of the people to be se
  <span citation-index="1" class="star-pagination" label="357"> 
   *357
   </span>
  cure in their persons, houses, papers, and effects, against unreasonable searches and seizures sh^ll not be violated.” It is general and forbids every search that is unreasonable; it protects all, those suspected or known to be offenders as well as the innocent, and unquestionably extends to the premises where the search was made and the papers taken.
  <em>
   Gouled
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#307" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 307</a></span>. The second clause declares: “ and no Warrants shall issue, but upon probable cause, supported by’ Oath or affirmation, ,and particularly describing the place to be searched, and the persons or things to be seized.” This prevents the issue of warrants on loose, vague or doubtful bases of. fact. It emphasizes the purpose to protect against all general searches. Since before the creation of our government, such searches have been deemed obnoxious to fundamental principles of liberty. They are denounced in the constitutions or statutes of every State in the Union.
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>. The need of protection against them is attested alike by history and present conditions. The Amendment is to be liberally construed and all owe the duty of vigilance for its effective enforcement lest there shall be impairment of the rights for the protection of which it was adopted.
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623</a></span>.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States, supra,
  </em>
  389-92.
 </p>
<p id="b421-4">
  There is no formula for the determination of reasonableness. Each case is to be decided on its own facts and circumstances. It is not, and could not be, claimed that the officers saw conspiracy being committed. And there is no suggestion that Gowen or Bartels was committing crime when arrested. In April, 1929, Braidwood reported to Calhoun the existence of a conspiracy and that in pursuance of it sales and deliveries of intoxicating liquor had been made in 1927 and 1928. The record does not show
  <span citation-index="1" class="star-pagination" label="358"> 
   *358
   </span>
  any criminal overt act in 1929. Calhoun's description to O'Brien of the company’s office in detail and of Gowen and Bartels shows that he knew the place and offenders. Notwithstanding he had. an abundance of information and time to swear out a valid warrant, he failed to do so. O'Brien falsely claimed to have a warrant ’or the search of the premises and he made the arrests under color of the invalid warrant.. By pretension of right and threat of force he compelled Gowen to open the desk ,and the safe and with the others made a general and apparently unlimited search, ransacking the desk, safe, filing cases and other parts of the office. It was a lawless invasion of the premises and a general exploratory search in the hope that evidence of crime might be found.
  <em>
   Federal Trade Commission
  </em>
  v.
  <em>
   American Tobacco Co.,
  </em>
  <span class="citation" data-id="100375"><a href="/opinion/100375/federal-trade-commission-v-american-tobacco-co/#306" aria-description="Citation for case: Federal Trade Commission v. American Tobacco Co.">264 U. S. 298, 306</a></span>.
 </p>
<p id="A28">
  Plainly the case before us is essentially different from
  <em>
   Marrón
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>.. There, officers executing a valid search warrant for intoxicating liquors found and arrested one Birdsall who in pursuance of a conspiracy was actually engaged in running a saloon. As an incident to the arrest they seized a ledger in a closet where the. liquor or some of it was kept and some bills beside the cash register. These things were visible and accessible and in the offender’s immediate custody. There was no threat of force or general search or rummaging of the place.
 </p>
<p id="b422-5">
  The .uncontradicted evidence requires a finding that here the search of the premises was unreasonable.
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, supra. Marron
  </em>
  v.
  <em>
   United States, supra,
  </em>
  199.
  <em>
   United States
  </em>
  v.
  <em>
   Kirschenblatt,
  </em>
  16 F. (2d) 202. The judgments below must be reversed and the case remanded to the district court with directions to enjoin the United States attorney and the special agent in charge from using the papers as evidence id to order the same returned to petitioners.
 </p>
<p id="b422-6">
<em>
   Reversed.
  </em>
</p>

<div class="footnotes"><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b417-4">
   The powers and duties of United States commissioners include: To arrest and imprison, or bail, for trial (18 U. S. C., ■§ 591; see also §§ 593-597) and in certain cases to take recognizances from witnesses on preliminary hearings • (<span class="citation no-link">28 U. S. C., § 657</span>); to issue warrants for and examine persons charged with being fugitives from justice (18 U. S. C., § .651); to hold to security of the peace and for good behavior (28 U. ,S. C., § 392); to issue search warrants (<span class="citation no-link">18 U. S. C., §§ 611-627</span>; <span class="citation no-link">26 U. S. C., § 1195</span>); to take bail and affidavits in civil causes (<span class="citation no-link">28 U. S. C., § 758</span>); to discharge poor uonvicts imprisoned for non-payment of fines (<span class="citation no-link">18 U. S. C., § 641</span>); to institute prosecutions under laws relating to the elective franchise and civil rights and to appoint persons to execute warrants thereunder (<span class="citation no-link">8 U. S. C., §§ 49</span>, 50); to enforce arbitration awards of foreign consuls in disputes between captains and crews of foreign vessels (<span class="citation no-link">28 U. S. C., § 393</span>); to summon master of ship to show cause why process should not issue against it for seaman’s wages (46 U. S. C., § '603); to take oaths and acknowledgments. <span class="citation no-link">5 U. S. C., § 92</span>,' 28 U. Sv C., § 525.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Goldey v. Fields.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Goldey v. Fields
type: case
citation: "606 U.S. 942 (2025)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2025
date_decided: ""
docket: 24-809
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
  opinion_url: "https://www.courtlistener.com/opinion/10776815/goldey-v-fields/"
  cluster_id: 10776815
  opinion_id: null
  identity_checked: true
lake:
  record_id: Goldey v. Fields
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
tags:
  - case
  - bivens
  - eighth-amendment
  - excessive-force
  - prisoner-litigation
  - federal-officer-liability
holding: "Bivens does not extend to allow a federal prisoner's Eighth Amendment excessive-force claim for damages against federal prison officials; the claim arises in a new Bivens context and special factors — Congress's active but remedy-free legislation in prisoner litigation, risks to prison operations, and existing alternative remedies — counsel against recognizing an implied damages action."
---

# Goldey v. Fields

*606 U.S. 942 (2025)* (No. 24-809) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776815 → opinion 11243402 (per curiam); quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Andrew Fields, a federal prisoner at the U.S. Penitentiary in Lee County, Virginia, was placed in solitary confinement, where he alleges prison officials physically abused him during periodic checks. He sued Bureau of Prisons officials for damages under *[[Bivens v. Six Unknown Named Agents|Bivens]]*, claiming excessive force in violation of the Eighth Amendment. The District Court dismissed the complaint, holding that Fields lacked a *[[Bivens v. Six Unknown Named Agents|Bivens]]* cause of action because the claim arose in a new context. A divided Fourth Circuit reversed, concluding that no special factors counseled against extending *[[Bivens v. Six Unknown Named Agents|Bivens]]*; Judge Richardson dissented. The prison officials, supported by the United States as amicus, sought review.

## Issue
Whether *[[Bivens v. Six Unknown Named Agents|Bivens]]* supplies an implied damages remedy for a federal prisoner's Eighth Amendment excessive-force claim against federal prison officials.

## Rule
Recognizing a cause of action under *[[Bivens v. Six Unknown Named Agents|Bivens]]* is "a disfavored judicial activity," and for more than four decades the Court has declined more than ten times to extend *[[Bivens v. Six Unknown Named Agents|Bivens]]* to new contexts. Courts apply a two-step test: whether the claim arises in "a new *Bivens* context" — one "different in a meaningful way" from the three contexts the Court has recognized — and, if so, whether any "special factors" counsel hesitation, with the ultimate question being whether Congress or the courts should create the remedy. Applying that test, the Court held: "*Bivens* does not extend to allow an Eighth Amendment excessive-force claim for damages against federal prison officials." — 606 U.S. at 942. ^pin-942

## Application
A federal prisoner's Eighth Amendment excessive-force claim is a new *[[Bivens v. Six Unknown Named Agents|Bivens]]* context — none of the three recognized contexts involved such a claim — and special factors foreclose an implied remedy. Congress has legislated extensively in the area of prisoner litigation (including the Prison Litigation Reform Act) yet has never created a statutory damages action for such claims; extending *[[Bivens v. Six Unknown Named Agents|Bivens]]* could have negative consequences for prison operations; and federal prisoners already have alternative remedial procedures, such as the Bureau of Prisons' administrative-remedy program. Those considerations counsel leaving any new damages remedy to Congress rather than the courts.

## Conclusion
The judgment of the Fourth Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. The opinion was **[[Common Legal Terms#per-curiam|per curiam]]**.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Goldey* continues the Court's post-*[[Ziglar v. Abbasi]]* / *[[Egbert v. Boule]]* trajectory of confining *[[Bivens v. Six Unknown Named Agents|Bivens]]* to its three recognized contexts and refusing new implied damages remedies against federal officers — here, foreclosing Eighth Amendment excessive-force claims by federal prisoners.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Goldey v. Fields*, 606 U.S. 942 (2025)](https://www.courtlistener.com/opinion/10776815/goldey-v-fields/) — pinpoint: 942 (holding, per curiam); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e527409dcd517603", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Goldey v. Fields"}, "payload": {"all": [{"cite": "606 U.S. 942", "page": "942", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "606"}], "display": "606 U.S. 942", "official": {"cite": "606 U.S. 942", "page": "942", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "606"}, "official_selection_present": true, "record_id": "Goldey v. Fields"}}
{"assertion_id": "26ad16707969afed", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Goldey v. Fields"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Goldey v. Fields", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Goldey v. Fields

```json
{
  "schema_version": "s2.v1",
  "record_id": "Goldey v. Fields",
  "status": "under_review",
  "identity": {
    "case_name": "Goldey v. Fields",
    "case_name_short": "Goldey",
    "case_name_full": "",
    "input_case_name": "Goldey v. Fields",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2025,
    "docket": "24-809",
    "cluster_id": 10776815,
    "lead_opinion_id": 11243402,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776815/goldey-v-fields/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "606 U.S. 942",
      "volume": "606",
      "reporter": "U.S.",
      "page": "942",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "606 U.S. 942",
        "volume": "606",
        "reporter": "U.S.",
        "page": "942",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "606 U.S. 942",
    "official_selection": {
      "court_class": "scotus",
      "selected": "606 U.S. 942",
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
    "date_created": "2026-07-06T12:13:01Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:13:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:13:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "goldey-v-fields--10776815",
      "to_record_id": "Goldey v. Fields",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Goldey v. Fields

```
                   PRELIMINARY PRINT

              Volume 606 U. S. Part 2
                             Pages 942–945




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                                June 30, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
942                     OCTOBER TERM, 2024

                               Per Curiam


 GOLDEY, ASSOCIATE WARDEN, et al. v. FIELDS
                   et al.
   on petition for writ of certiorari to the united
    states court of appeals for the fourth circuit
                   No. 24–809. Decided June 30, 2025
Prison offcials at the U. S. Penitentiary in Lee County, Virginia, placed
  respondent Fields in solitary confnement. Fields alleges that during
  periodic checks, offcials physically abused him. Fields sued the Bureau
  of Prisons and prison offcials for damages, claiming excessive force in
  violation of the Eighth Amendment. The District Court dismissed
  Fields's complaint, determining he lacked a cause of action under Bivens
  v. Six Unknown Fed. Narcotics Agents, 403 U. S. 388. The Fourth Cir-
  cuit reversed, concluding that Fields could proceed with his Eighth
  Amendment excessive-force claim for damages.
Held: Bivens does not extend to allow an Eighth Amendment excessive-
  force claim for damages against federal prison offcials. For 45 years,
  this Court has consistently declined to extend Bivens to new contexts.
Page Proof Pending Publication
  This case arises in a new context, and special factors counsel against
  recognizing an implied Bivens cause of action for Eighth Amendment
  excessive-force violations. Congress has actively legislated in prisoner
  litigation but has not enacted a statutory cause of action for money
  damages. Extending Bivens to excessive-force claims could have nega-
  tive consequences for prison operations, and alternative remedial proce-
  dures already exist for federal prisoners.
Certiorari granted; 109 F. 4th 264, reversed and remanded.

  Per Curiam.
  In Bivens v. Six Unknown Fed. Narcotics Agents, 403
U. S. 388 (1971), this Court recognized an implied cause of
action for damages against federal offcers for certain alleged
violations of the Fourth Amendment. The Court subse-
quently recognized two additional contexts where implied
Bivens causes of action were permitted, neither of which was
an Eighth Amendment excessive-force claim. After 1980,
we have declined more than 10 times to extend Bivens to
cover other constitutional violations. Those many post-1980
Bivens “cases have made clear that, in all but the most un-
                   Cite as: 606 U. S. 942 (2025)            943

                           Per Curiam

usual circumstances, prescribing a cause of action is a job for
Congress, not the courts.” Egbert v. Boule, 596 U. S. 482,
486 (2022). Despite those precedents, the U. S. Court of Ap-
peals for the Fourth Circuit permitted the plaintiff here
to maintain an Eighth Amendment excessive-force Bivens
claim for damages against federal prison offcials.
   This case began when prison offcials at the U. S. Peniten-
tiary in Lee County, Virginia, ordered that plaintiff Andrew
Fields be placed in solitary confnement. Prison offcials
monitored Fields while he was isolated. Fields alleges that
during their periodic checks, offcials would “physically
abuse” him. Fields v. Federal Bureau of Prisons, 109 F. 4th
264, 268 (CA4 2024).
   Fields sued the Bureau of Prisons (BOP), the prison war-
den, and several prison offcials in federal court for damages,
claiming that certain prison offcials used excessive force
against him in violation of the Eighth Amendment. The
Page Proof Pending Publication
U. S. District Court for the Western District of Virginia dis-
missed Fields's complaint. As relevant here, the court de-
termined that Fields lacked a cause of action under Bivens.
Because “the Supreme Court has never ruled that a damages
remedy exists for claims of excessive force by BOP offcers
against an inmate,” the District Court had “no diffculty in
concluding that these claims arise in a new context” and that
a Bivens remedy was unavailable. App. to Pet. for Cert.
49a; see id., at 45a–54a.
   Fields appealed. In a divided decision, the Fourth Circuit
reversed in relevant part, concluding that Fields could pro-
ceed with his Eighth Amendment excessive-force claim for
damages. The Court of Appeals determined that no “special
factors counseled against extending Bivens” here. 109
F. 4th, at 270.
   Judge Richardson dissented and stated: “A faithful applica-
tion of our precedent and the Supreme Court's leads squarely
to the conclusion that we cannot create a new Bivens action
here.” Id., at 283.
944                  GOLDEY v. FIELDS

                          Per Curiam

   After the Fourth Circuit denied rehearing en banc, prison
offcials sought review in this Court, with the support of the
United States as amicus curiae. We now grant the petition
for certiorari and reverse.
   This Court has repeatedly emphasized that “recognizing a
cause of action under Bivens is `a disfavored judicial activ-
ity.' ” Egbert, 596 U. S., at 491. To determine whether a
Bivens claim may proceed, the Court has applied a two-step
test. First, the Court asks whether the case presents “a
new Bivens context”—that is, whether the case “is different
in a meaningful way” from the cases in which this Court has
recognized a Bivens remedy. Ziglar v. Abbasi, 582 U. S.
120, 139 (2017); see Carlson v. Green, 446 U. S. 14 (1980);
Davis v. Passman, 442 U. S. 228 (1979); Bivens, 403 U. S. 388.
   Second, if so, we then ask whether there are “special fac-
tors” indicating that “the Judiciary is at least arguably less
equipped than Congress to `weigh the costs and benefts of
Page Proof Pending Publication
allowing a damages action to proceed.' ” Egbert, 596 U. S.,
at 492. That analysis is anchored in “separation-of-powers
principles.” Ziglar, 582 U. S., at 135.
   This case arises in a new context, and “special factors”
counsel against recognizing an implied Bivens cause of action
for Eighth Amendment excessive-force violations. To begin
with, Congress has actively legislated in the area of prisoner
litigation but has not enacted a statutory cause of action for
money damages. See Ziglar, 582 U. S., at 148–149. In ad-
dition, extending Bivens to allow an Eighth Amendment
claim for excessive force could have negative systemic con-
sequences for prison offcials and the “inordinately diffcult
undertaking” of running a prison. Turner v. Safey, 482
U. S. 78, 84–85 (1987). Moreover, “an alternative remedial
structure” already exists for aggrieved federal prisoners.
Ziglar, 582 U. S., at 137; see Correctional Services Corp. v.
Malesko, 534 U. S. 61, 74 (2001). The existence of such al-
ternative remedial procedures counsels against allowing
                   Cite as: 606 U. S. 942 (2025)                 945

                           Per Curiam

Bivens suits even if such “procedures are `not as effective as
an individual damages remedy.' ” Egbert, 596 U. S., at 498.
   For the past 45 years, this Court has consistently declined
to extend Bivens to new contexts. See Egbert, 596 U. S., at
490–491. We do the same here. The petition for certiorari
is granted, the judgment of the U. S. Court of Appeals for
the Fourth Circuit is reversed, and the case is remanded for
further proceedings consistent with this opinion.

                                                   It is so ordered.




Page Proof Pending Publication
                           Reporter’s Note

   The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
Page Proof Pending Publication
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
the Court. Other revisions may include adjustments to formatting, cap-
tions, citation form, and any errant punctuation. The following additional
edits were made:

None

```

---
