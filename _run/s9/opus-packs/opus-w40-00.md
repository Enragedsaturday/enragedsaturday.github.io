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

## GROUP: content/cases/Skinner v. Railway Labor Executives' Ass'n.md  (`case`, 5 assertions)

### content_page

```
---
title: "Skinner v. Railway Labor Executives' Ass'n"
type: case
citation: "489 U.S. 602 (1989)"
parallel_cite: "109 S. Ct. 1402; 103 L. Ed. 2d 639; 4 I.E.R. Cas. (BNA) 224; 1989 CCH OSHD 28,476; 57 U.S.L.W. 4324; 13 OSHC (BNA) 2065; 130 L.R.R.M. (BNA) 2857; 49 Empl. Prac. Dec. (CCH) 38,791"
neutral_cite: 1989 U.S. LEXIS 1568
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-03-21
docket: 87-1555
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Skinner v. Railway Labor Executives' Ass'n"
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112219/skinner-v-railway-labor-executives-assn/"
  cluster_id: 112219
  opinion_id: 112219
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Anchor"
related: ["[[National Treasury Employees Union v. Von Raab]]", "[[Vernonia School District 47J v. Acton]]", "[[Board of Education v. Earls]]", "[[Griffin v. Wisconsin]]", "[[Ferguson v. City of Charleston]]"]
aliases: ["Skinner v. Railway Labor Executives' Assn.", "Skinner v. Railway Labor Executives' Association", "Skinner v. Railway Labor Executives Association"]
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "administrative-search"]
holding: "Suspicionless drug/alcohol testing of railway employees after accidents is reasonable under the special-needs doctrine."
lake:
  record_id: "Skinner v. Railway Labor Executives' Ass'n"
  status: verified
  projected_at: 2026-07-06
---

# Skinner v. Railway Labor Executives' Ass'n

*489 U.S. 602 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal Railroad Administration regulations required blood and urine testing of railroad employees involved in major accidents, and authorized breath and urine testing on reasonable suspicion of impairment. A railway-labor group challenged the suspicionless post-accident testing as an unreasonable search.

## Issue
Whether suspicionless drug and alcohol testing of railroad employees following accidents is reasonable under the Fourth Amendment as a special-needs search.

## Rule
Where special needs make individualized suspicion impracticable, a search may be reasonable without it. "In limited circumstances, where the privacy interests implicated by the search are minimal, and where an important governmental interest furthered by the intrusion would be placed in jeopardy by a requirement of individualized suspicion, a search may be reasonable despite the absence of such suspicion." — 489 U.S. at 624. ^pin-624

The Court treated railroad-safety regulation as presenting "special needs, beyond the normal need for law enforcement," that justified departing from the warrant and probable-cause requirements.

## Application
The Court found the intrusion of blood and breath tests minimal and the urine-collection procedures regulated to limit intrusiveness, while the government's interest in railroad safety—where an impaired employee's momentary lapse could be catastrophic—was compelling. On that balance, the suspicionless post-accident testing was reasonable without a warrant or individualized suspicion.

## Conclusion
The post-accident toxicological testing program was a reasonable special-needs search and was upheld.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Decided with its companion [[National Treasury Employees Union v. Von Raab]]; the special-needs framework was applied to schools in [[Vernonia School District 47J v. Acton]] and [[Board of Education v. Earls]] (and to probation in [[Griffin v. Wisconsin]]), and its limit—a programmatic law-enforcement purpose defeats the exception—was drawn in [[Ferguson v. City of Charleston]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *Skinner v. Railway Labor Executives' Ass'n*, 489 U.S. 602 (1989) — https://www.courtlistener.com/opinion/112219/skinner-v-railway-labor-executives-assn/ — pinpoint: 624.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f3336f4be6c056f5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "489 U.S. 602 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1989 U.S. LEXIS 1568", "official_citation_present": true, "parallel_cite": "109 S. Ct. 1402; 103 L. Ed. 2d 639; 4 I.E.R. Cas. (BNA) 224; 1989 CCH OSHD 28,476; 57 U.S.L.W. 4324; 13 OSHC (BNA) 2065; 130 L.R.R.M. (BNA) 2857; 49 Empl. Prac. Dec. (CCH) 38,791", "title": "Skinner v. Railway Labor Executives' Ass'n", "year": "1989"}}
{"assertion_id": "45236ddee8284658", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Suspicionless drug/alcohol testing of railway employees after accidents is reasonable under the special-needs doctrine.", "title": "Skinner v. Railway Labor Executives' Ass'n"}}
{"assertion_id": "60a984379b6d3bcb", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Anchor", "title": "Skinner v. Railway Labor Executives' Ass'n"}}
{"assertion_id": "a7fdcb40534e98a7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1989-03-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Skinner v. Railway Labor Executives' Ass'n", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Skinner v. Railway Labor Executives' Ass'n", "varies_by_point": "false"}}
{"assertion_id": "f0c7e37c6ac10c14", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Skinner v. Railway Labor Executives' Ass'n"}}
```

### lake record — Skinner v. Railway Labor Executives' Ass'n

```json
{
  "schema_version": "s2.v1",
  "record_id": "Skinner v. Railway Labor Executives' Ass'n",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Skinner v. Railway Labor Executives' Assn.",
    "case_name_short": "Skinner",
    "case_name_full": "SKINNER, SECRETARY OF TRANSPORTATION, Et Al. v. RAILWAY LABOR EXECUTIVES\u2019 ASSOCIATION Et Al.",
    "input_case_name": "Skinner v. Railway Labor Executives' Ass'n",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-03-21",
    "year": 1989,
    "docket": "87-1555",
    "cluster_id": 112219,
    "lead_opinion_id": 112219,
    "sibling_ids": [
      112219,
      9431606,
      9431607,
      9431608
    ],
    "absolute_url": "/opinion/112219/skinner-v-railway-labor-executives-assn/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "489 U.S. 602",
      "volume": "489",
      "reporter": "U.S.",
      "page": "602",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1402",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1402",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 639",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "639",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 I.E.R. Cas. (BNA) 224",
        "volume": "4",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "224",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 CCH OSHD 28,476",
        "volume": "1989",
        "reporter": "CCH OSHD",
        "page": "28,476",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4324",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4324",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 OSHC (BNA) 2065",
        "volume": "13",
        "reporter": "OSHC (BNA)",
        "page": "2065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 L.R.R.M. (BNA) 2857",
        "volume": "130",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2857",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Empl. Prac. Dec. (CCH) 38,791",
        "volume": "49",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "38,791",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 1568",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1568",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "489 U.S. 602",
        "volume": "489",
        "reporter": "U.S.",
        "page": "602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1402",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1402",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 639",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "639",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 1568",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1568",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 I.E.R. Cas. (BNA) 224",
        "volume": "4",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "224",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 CCH OSHD 28,476",
        "volume": "1989",
        "reporter": "CCH OSHD",
        "page": "28,476",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4324",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4324",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 OSHC (BNA) 2065",
        "volume": "13",
        "reporter": "OSHC (BNA)",
        "page": "2065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 L.R.R.M. (BNA) 2857",
        "volume": "130",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2857",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Empl. Prac. Dec. (CCH) 38,791",
        "volume": "49",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "38,791",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "489 U.S. 602",
    "official_selection": {
      "court_class": "scotus",
      "selected": "489 U.S. 602",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-624",
      "page": null,
      "quote": "--- # Skinner v. Railway Labor Executives' Ass'n *489 U.S. 602 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal Railroad Administration regulations required blood and urine testing of railroad employees involved in major accidents, and authorized breath and urine testing on reasonable suspicion of impairment. A railway-labor group challenged the suspicionless post-accident testing as an unreasonable search. ## Issue Whether suspicionless drug and alcohol testing of railroad employees following accidents is reasonable under the Fourth Amendment as a special-needs search. ## Rule Where special needs make individualized suspicion impracticable, a search may be reasonable without it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Skinner v. Railway Labor Executives' Ass'n",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Bell",
          "cluster_id": 10747468,
          "cite": [
            "2025 ND 201"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 10018723,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 5144554,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Ryan Mark Thompson",
          "cluster_id": 4311783,
          "cite": [
            "886 N.W.2d 224",
            "2016 Minn. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Buie",
          "cluster_id": 112384,
          "cite": [
            "108 L. Ed. 2d 276",
            "110 S. Ct. 1093",
            "494 U.S. 325",
            "1990 U.S. LEXIS 1176"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas Omar Midgette",
          "cluster_id": 796984,
          "cite": [
            "478 F.3d 616",
            "2007 U.S. App. LEXIS 4153",
            "2007 WL 572127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Daniel Good Real Property",
          "cluster_id": 112914,
          "cite": [
            "126 L. Ed. 2d 490",
            "114 S. Ct. 492",
            "510 U.S. 43",
            "1993 U.S. LEXIS 7941",
            "7 Fla. L. Weekly Fed. S 665",
            "93 Daily Journal DAR 15706",
            "93 Cal. Daily Op. Serv. 9143",
            "62 U.S.L.W. 4013",
            "1993 WL 505539"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Everson v. Leis",
          "cluster_id": 1464717,
          "cite": [
            "556 F.3d 484",
            "2009 U.S. App. LEXIS 3288",
            "2009 WL 414625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Allegheny v. American Civil Liberties Union",
          "cluster_id": 112331,
          "cite": [
            "106 L. Ed. 2d 472",
            "109 S. Ct. 3086",
            "492 U.S. 573",
            "1989 U.S. LEXIS 3468",
            "57 U.S.L.W. 5045"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rossignol v. Voorhaar",
          "cluster_id": 2967705,
          "cite": [
            "316 F.3d 516",
            "2003 WL 124775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Parkell v. Carl Danberg",
          "cluster_id": 4248660,
          "cite": [
            "833 F.3d 313",
            "2016 U.S. App. LEXIS 15092",
            "2016 WL 4375620"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dubbs Ex Rel. Dubbs v. Head Start, Inc.",
          "cluster_id": 163684,
          "cite": [
            "336 F.3d 1194",
            "2003 U.S. App. LEXIS 14578",
            "2003 WL 21690533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Consolidated Rail Corporation v. Railway Labor Executives' Assn.",
          "cluster_id": 112300,
          "cite": [
            "105 L. Ed. 2d 250",
            "109 S. Ct. 2477",
            "491 U.S. 299",
            "1989 U.S. LEXIS 3000",
            "57 U.S.L.W. 4742",
            "131 L.R.R.M. (BNA) 2601",
            "50 Empl. Prac. Dec. (CCH) 39,068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. National Collegiate Athletic Assn.",
          "cluster_id": 1235436,
          "cite": [
            "865 P.2d 633",
            "7 Cal. 4th 1",
            "26 Cal. Rptr. 2d 834",
            "94 Cal. Daily Op. Serv. 681",
            "94 Daily Journal DAR 1141",
            "9 I.E.R. Cas. (BNA) 716",
            "1994 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112219 OR 9431606 OR 9431607 OR 9431608) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDU0MDI1NjAwMDAwJnM9MzE3Mzc0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112219+OR+9431606+OR+9431607+OR+9431608%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112219 OR 9431606 OR 9431607 OR 9431608)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTQmcz0xNDY0MzY2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112219+OR+9431606+OR+9431607+OR+9431608%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112219 OR 9431606 OR 9431607 OR 9431608)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 1,
        "triage_snippet_classified": 41
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112219 OR 9431606 OR 9431607 OR 9431608)",
    "indexed_citing_opinions": 1507,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112219,
        "count": 1348,
        "count_source": "search"
      },
      {
        "opinion_id": 9431606,
        "count": 184,
        "count_source": "search"
      },
      {
        "opinion_id": 9431607,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431608,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2566,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/skinner-v-railway-labor-executives-ass-n.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwOTI5Nzcmcz0xMDI4MzgzNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112219+OR+9431606+OR+9431607+OR+9431608%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112219,
        "cited_id": 92312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 96033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 97451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 98973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 99296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 103875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 104914,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 337776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 473627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 477827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 480401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 482045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 486563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 497255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 497335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 498019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 501767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 502437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 504461,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 506184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 1215534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 1908384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 2307499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 2370062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 2372481,
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
    "date_created": "2026-07-05T20:56:06Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:57:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:57:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:59:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:57:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Skinner v. Railway Labor Executives' Ass'n (truncated)

```
<div>
<center><b><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S. 602</a></span> (1989)</b></center>
<center><h1>SKINNER, SECRETARY OF TRANSPORTATION, ET AL.<br>
v.<br>
RAILWAY LABOR EXECUTIVES' ASSOCIATION ET AL.</h1></center>
<center>No. 87-1555.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 2, 1988</center>
<center>Decided March 21, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*605</span> <i>Attorney General Thornburgh</i> argued the cause for petitioners. On the briefs were <i>Solicitor General Fried, Assistant Attorney General Bolton, Deputy Solicitor General Merrill, Deputy Assistant Attorneys General Spears</i> and <i>Cynkar, Lawrence S. Robbins, Leonard Schaitman, Marc Richman, B. Wayne Vance, S. Mark Lindsey,</i> and <i>Daniel Carey Smith.</i></p>
<p><i>Lawrence M. Mann</i> argued the cause for respondents. With him on the brief were <i>W. David Holsberry, Harold A. Ross,</i> and <i>Clinton J. Miller III.</i><sup>[*]</sup></p>
<p>Briefs <i>of amici curiae</i> urging affirmance were filed for the American Civil Liberties Union et al. by <i>James D. Holzhauer, John A. Powell, Stephen R. Shapiro, Harvey Grossman,</i> and <i>Edward M. Chen;</i> and for the American Federation of Labor and Congress of Industrial Organizations by <i>David Silberman</i> and <i>Laurence Gold.</i></p>
<p><i>Scott D. Raphael</i> filed a brief for the Aircraft Owners &amp; Pilots Association as <i>amicus curiae.</i></p>
<p><span class="star-pagination">*606</span> JUSTICE KENNEDY delivered the opinion of the Court.</p>
<p>The Federal Railroad Safety Act of 1970 authorizes the Secretary of Transportation to "prescribe, as necessary, appropriate rules, regulations, orders, and standards for all areas of railroad safety." <span class="citation no-link">84 Stat. 971</span>, <span class="citation no-link">45 U. S. C. § 431</span>(a). Finding that alcohol and drug abuse by railroad employees poses a serious threat to safety, the Federal Railroad Administration (FRA) has promulgated regulations that mandate blood and urine tests of employees who are involved in certain train accidents. The FRA also has adopted regulations that do not require, but do authorize, railroads to administer breath and urine tests to employees who violate certain safety rules. The question presented by this case is whether these regulations violate the Fourth Amendment.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>The problem of alcohol use on American railroads is as old as the industry itself, and efforts to deter it by carrier rules began at least a century ago. For many years, railroads have prohibited operating employees from possessing alcohol or being intoxicated while on duty and from consuming alcoholic beverages while subject to being called for duty. More recently, these proscriptions have been expanded to forbid possession or use of certain drugs. These restrictions are <span class="star-pagination">*607</span> embodied in "Rule G," an industry-wide operating rule promulgated by the Association of American Railroads, and are enforced, in various formulations, by virtually every railroad in the country. The customary sanction for Rule G violations is dismissal.</p>
<p>In July 1983, the FRA expressed concern that these industry efforts were not adequate to curb alcohol and drug abuse by railroad employees. The FRA pointed to evidence indicating that on-the-job intoxication was a significant problem in the railroad industry.<sup>[1]</sup> The FRA also found, after a review of accident investigation reports, that from 1972 to 1983 "the nation's railroads experienced at least 21 significant train accidents involving alcohol or drug use as a probable cause or contributing factor," and that these accidents "resulted in 25 fatalities, 61 non-fatal injuries, and property damage estimated at $19 million (approximately $27 million in 1982 dollars)." <span class="citation no-link">48 Fed. Reg. 30726</span> (1983). The FRA further identified "an additional 17 fatalities to operating employees working on or around rail rolling stock that involved alcohol or drugs as a contributing factor." <i><span class="citation no-link">Ibid.</span></i> In light of these problems, the FRA solicited comments from interested parties on a various regulatory approaches to the problems of alcohol and drug abuse throughout the Nation's railroad system.</p>
<p>Comments submitted in response to this request indicated that railroads were able to detect a relatively small number of Rule G violations, owing, primarily, to their practice of <span class="star-pagination">*608</span> relying on observation by supervisors and co-workers to enforce the rule. <span class="citation no-link">49 Fed. Reg. 24266</span>-24267 (1984). At the same time, "industry participants . . . confirmed that alcohol and drug use [did] occur on the railroads with unacceptable frequency," and available information from all sources "suggest[ed] that the problem includ[ed] `pockets' of drinking and drug use involving multiple crew members (before and during work), sporadic cases of individuals reporting to work impaired, and repeated drinking and drug use by individual employees who are chemically or psychologically dependent on those substances." <i>Id.,</i> at 24253-24254. "Even without the benefit of regular post-accident testing," the FRA "identified 34 fatalities, 66 injuries and over $28 million in property damage (in 1983 dollars) that resulted from the errors of alcohol and drug-impaired employees in 45 train accidents and train incidents during the period 1975 through 1983." <i>Id.,</i> at 24254. Some of these accidents resulted in the release of hazardous materials and, in one case, the ensuing pollution required the evacuation of an entire Louisiana community. <i>Id.,</i> at 24254, 24259. In view of the obvious safety hazards of drug and alcohol use by railroad employees, the FRA announced in June 1984 its intention to promulgate federal regulations on the subject.</p>
<p></p>
<h2>B</h2>
<p>After reviewing further comments from representatives of the railroad industry, labor groups, and the general public, the FRA, in 1985, promulgated regulations addressing the problem of alcohol and drugs on the railroads. The final regulations apply to employees assigned to perform service subject to the Hours of Service Act, ch. 2939, <span class="citation no-link">34 Stat. 1415</span>, as amended, <span class="citation no-link">45 U. S. C. § 61</span> <i>et seq.</i> The regulations prohibit covered employees from using or possessing alcohol or any controlled substance. <span class="citation no-link">49 CFR § 219.101</span>(a)(1) (1987). The regulations further prohibit those employees from reporting for covered service while under the influence of, or <span class="star-pagination">*609</span> impaired by, alcohol, while having a blood alcohol concentration of 0.04 or more, or while under the influence of, or impaired by, any controlled substance. § 219.101(a)(2). The regulations do not restrict, however, a railroad's authority to impose an absolute prohibition on the presence of alcohol or any drug in the body fluids of persons in its employ, § 219.101(c), and, accordingly, they do not "replace Rule G or render it unenforceable." <span class="citation no-link">50 Fed. Reg. 31538</span> (1985).</p>
<p>To the extent pertinent here, two subparts of the regulations relate to testing. Subpart C, which is entitled "Post-Accident Toxicological Testing," is mandatory. It provides that railroads "shall take all practicable steps to assure that all covered employees of the railroad directly involved . . . provide blood and urine samples for toxicological testing by FRA," § 219.203(a), upon the occurrence of certain specified events. Toxicological testing is required following a "major train accident," which is defined as any train accident that involves (i) a fatality, (ii) the release of hazardous material accompanied by an evacuation or a reportable injury, or (iii) damage to railroad property of $500,000 or more. § 219.201 (a)(1). The railroad has the further duty of collecting blood and urine samples for testing after an "impact accident," which is defined as a collision that results in a reportable injury, or in damage to railroad property of $50,000 or more. § 219.201(a)(2). Finally, the railroad is also obligated to test after "[a]ny train incident that involves a fatality to any on-duty railroad employee." § 219.201(a)(3).</p>
<p>After occurrence of an event which activates its duty to test, the railroad must transport all crew members and other covered employees directly involved in the accident or incident to an independent medical facility, where both blood and urine samples must be obtained from each employee.<sup>[2]</sup> After <span class="star-pagination">*610</span> the samples have been collected, the railroad is required to ship them by prepaid air freight to the FRA laboratory for analysis. § 219.205(d). There, the samples are analyzed using "state-of-the-art equipment and techniques" to detect and measure alcohol and drugs.<sup>[3]</sup> The FRA proposes to place primary reliance on analysis of blood samples, as blood is "the only available body fluid . . . that can provide a clear indication not only of the presence of alcohol and drugs but also their current impairment effects." <span class="citation no-link">49 Fed. Reg. 24291</span> (1984). Urine samples are also necessary, however, because drug traces remain in the urine longer than in blood, and in some cases it will not be possible to transport employees to a medical facility before the time it takes for certain drugs to be eliminated from the bloodstream. In those instances, a "positive urine test, taken with specific information on the pattern of elimination for the particular drug and other information on the behavior of the employee and the circumstances of the accident, may be crucial to the determination of" the cause of an accident. <i><span class="citation no-link">Ibid.</span></i></p>
<p>The regulations require that the FRA notify employees of the results of the tests and afford them an opportunity to respond in writing before preparation of any final investigative report. See § 219.211(a)(2). Employees who refuse to provide required blood or urine samples may not perform covered <span class="star-pagination">*611</span> service for nine months, but they are entitled to a hearing concerning their refusal to take the test. § 219.213.</p>
<p>Subpart D of the regulations, which is entitled "Authorization to Test for Cause," is permissive. It authorizes railroads to require covered employees to submit to breath or urine tests in certain circumstances not addressed by Subpart C. Breath or urine tests, or both, may be ordered (1) after a reportable accident or incident, where a supervisor has a "reasonable suspicion" that an employee's acts or omissions contributed to the occurrence or severity of the accident or incident, § 219.301(b)(2); or (2) in the event of certain specific rule violations, including noncompliance with a signal and excessive speeding, § 219.301(b)(3). A railroad also may require breath tests where a supervisor has a "reasonable suspicion" that an employee is under the influence of alcohol, based upon specific, personal observations concerning the appearance, behavior, speech, or body odors of the employee. § 219.301(b)(1). Where impairment is suspected, a railroad, in addition, may require urine tests, but only if two supervisors make the appropriate determination, § 219.301(c)(2)(i), and, where the supervisors suspect impairment due to a substance other than alcohol, at least one of those supervisors must have received specialized training in detecting the signs of drug intoxication, § 219.301(c)(2)(ii).</p>
<p>Subpart D further provides that whenever the results of either breath or urine tests are intended for use in a disciplinary proceeding, the employee must be given the opportunity to provide a blood sample for analysis at an independent medical facility. § 219.303(c). If an employee declines to give a blood sample, the railroad may presume impairment, absent persuasive evidence to the contrary, from a positive showing of controlled substance residues in the urine. The railroad must, however, provide detailed notice of this presumption to its employees, and advise them of their right to provide a contemporaneous blood sample. As in the case of samples procured under Subpart C, the regulations set forth <span class="star-pagination">*612</span> procedures for the collection of samples, and require that samples "be analyzed by a method that is reliable within known tolerances." § 219.307(b).</p>
<p></p>
<h2>C</h2>
<p>Respondents, the Railway Labor Executives' Association and various of its member labor organizations, brought the instant suit in the United States District Court for the Northern District of California, seeking to enjoin the FRA's regulations on various statutory and constitutional grounds. In a ruling from the bench, the District Court granted summary judgment in petitioners' favor. The court concluded that railroad employees "have a valid interest in the integrity of their own bodies" that deserved protection under the Fourth Amendment. App. to Pet. for Cert. 53a. The court held, however, that this interest was outweighed by the competing "public and governmental interest in the . . . promotion of. . . railway safety, safety for employees, and safety for the general public that is involved with the transportation." <i>Id.,</i> at 52a. The District Court found respondents' other constitutional and statutory arguments meritless.</p>
<p>A divided panel of the Court of Appeals for the Ninth Circuit reversed. <i>Railway Labor Executives' Assn.</i> v. <i>Burnley,</i> <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d 575</a></span> (1988). The court held, first, that tests mandated by a railroad in reliance on the authority conferred by Subpart D involve sufficient Government action to implicate the Fourth Amendment, and that the breath, blood, and urine tests contemplated by the FRA regulations are Fourth Amendment searches. The court also "agre[ed] that the exigencies of testing for the presence of alcohol and drugs in blood, urine or breath require prompt action which precludes obtaining a warrant." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#583" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 583</a></span>. The court further held that "accommodation of railroad employees' privacy interest with the significant safety concerns of the government does not require adherence to a probable cause requirement," and, accordingly, that the legality of the searches contemplated by <span class="star-pagination">*613</span> the FRA regulations depends on their reasonableness under all the circumstances. <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#587" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 587</a></span>.</p>
<p>The court concluded, however, that particularized suspicion is essential to a finding that toxicological testing of railroad employees is reasonable. <i><span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">Ibid.</a></span></i> A requirement of individualized suspicion, the court stated, would impose "no insuperable burden on the government," <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#588" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>id.,</i> at 588</a></span>, and would ensure that the tests are confined to the detection of current impairment, rather than to the discovery of "the metabolites of various drugs, which are not evidence of current intoxication and may remain in the body for days or weeks after the ingestion of the drug." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#588" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 588-589</a></span>. Except for the provisions authorizing breath and urine tests on a "reasonable suspicion" of drug or alcohol impairment, <span class="citation no-link">49 CFR §§ 219.301</span>(b)(1) and (c)(2) (1987), the FRA regulations did not require a showing of individualized suspicion, and, accordingly, the court invalidated them.</p>
<p>Judge Alarcon dissented. He criticized the majority for "fail[ing] to engage in [a] balancing of interests" and for focusing instead "solely on the degree of impairment of the workers' privacy interests." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#597" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d, at 597</a></span>. The dissent would have held that "the government's compelling need to assure railroad safety by controlling drug use among railway personnel outweighs the need to protect privacy interests." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#596" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 596</a></span>.</p>
<p>We granted the federal parties' petition for a writ of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./486/1042/">486 U. S. 1042</a></span> (1988), to consider whether the regulations invalidated by the Court of Appeals violate the Fourth Amendment. We now reverse.</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment provides that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . ." The Amendment guarantees the privacy, dignity, and security of persons against certain arbitrary <span class="star-pagination">*614</span> and invasive acts by officers of the Government or those acting at their direction. <i>Camara</i> v. <i>Municipal Court of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967). See also <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653-654</a></span> (1979); <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span> (1976). Before we consider whether the tests in question are reasonable under the Fourth Amendment, we must inquire whether the tests are attributable to the Government or its agents, and whether they amount to searches or seizures. We turn to those matters.</p>
<p></p>
<h2>A</h2>
<p>Although the Fourth Amendment does not apply to a search or seizure, even an arbitrary one, effected by a private party on his own initiative, the Amendment protects against such intrusions if the private party acted as an instrument or agent of the Government. See <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113-114</a></span> (1984); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487</a></span> (1971). See also <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#475" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 475</a></span> (1921). A railroad that complies with the provisions of Subpart C of the regulations does so by compulsion of sovereign authority, and the lawfulness of its acts is controlled by the Fourth Amendment. Petitioners contend, however, that the Fourth Amendment is not implicated by Subpart D of the regulations, as nothing in Subpart D compels any testing by private railroads.</p>
<p>We are unwilling to conclude, in the context of this facial challenge, that breath and urine tests required by private railroads in reliance on Subpart D will not implicate the Fourth Amendment. Whether a private party should be deemed an agent or instrument of the Government for Fourth Amendment purposes necessarily turns on the degree of the Government's participation in the private party's activities, cf. <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/#78" aria-description="Citation for case: Lustig v. United States">338 U. S. 74, 78-79</a></span> (1949) (plurality opinion); <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#32" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 32-33</a></span> (1927), a question that can only be resolved "in light of all the circumstances," <i>Coolidge</i> v. <i>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra,</a></span></i> <span class="star-pagination">*615</span> at 487. The fact that the Government has not compelled a private party to perform a search does not, by itself, establish that the search is a private one. Here, specific features of the regulations combine to convince us that the Government did more than adopt a passive position toward the underlying private conduct.</p>
<p>The regulations, including those in Subpart D, pre-empt state laws, rules, or regulations covering the same subject matter, <span class="citation no-link">49 CFR § 219.13</span>(a) (1987), and are intended to supersede "any provision of a collective bargaining agreement, or arbitration award construing such an agreement," <span class="citation no-link">50 Fed. Reg. 31552</span> (1985). They also confer upon the FRA the right to receive certain biological samples and test results procured by railroads pursuant to Subpart D. § 219.11(c). In addition, a railroad may not divest itself of, or otherwise compromise by contract, the authority conferred by Subpart D. As the FRA explained, such "authority . . . is conferred for the purpose of promoting the public safety, and a railroad may not shackle itself in a way inconsistent with its duty to promote the public safety." <span class="citation no-link">50 Fed. Reg. 31552</span> (1985). Nor is a covered employee free to decline his employer's request to submit to breath or urine tests under the conditions set forth in Subpart D. See § 219.11(b). An employee who refuses to submit to the tests must be withdrawn from covered service. See 4 App. to Field Manual 18.</p>
<p>In light of these provisions, we are unwilling to accept petitioners' submission that tests conducted by private railroads in reliance on Subpart D will be primarily the result of private initiative. The Government has removed all legal barriers to the testing authorized by Subpart D, and indeed has made plain not only its strong preference for testing, but also its desire to share the fruits of such intrusions. In addition, it has mandated that the railroads not bargain away the authority to perform tests granted by Subpart D. These are clear indices of the Government's encouragement, endorsement, <span class="star-pagination">*616</span> and participation, and suffice to implicate the Fourth Amendment.</p>
<p></p>
<h2>B</h2>
<p>Our precedents teach that where, as here, the Government seeks to obtain physical evidence from a person, the Fourth Amendment may be relevant at several levels. See, <i>e. g., </i><i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#8" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 8</a></span> (1973). The initial detention necessary to procure the evidence may be a seizure of the person, <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#294" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 294-295</a></span> (1973); <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span> (1969), if the detention amounts to a meaningful interference with his freedom of movement. <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984); <i>United States</i> v. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen"><i>Jacobsen, supra,</i> at 113, n. 5</a></span>. Obtaining and examining the evidence may also be a search, see <i>Cupp</i> v. <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#295" aria-description="Citation for case: Cupp v. Murphy"><i>Murphy, supra,</i> at 295</a></span>; <i>United States</i> v. <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#8" aria-description="Citation for case: United States v. Dionisio"><i>Dionisio, supra,</i> at 8, 13-14</a></span>, if doing so infringes an expectation of privacy that society is prepared to recognize as reasonable, see, <i>e. g., </i><i>California</i> v. <i>Greenwood,</i> <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/#43" aria-description="Citation for case: California v. Greenwood">486 U. S. 35, 43</a></span> (1988); <i>United States</i> v. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen"><i>Jacobsen, supra,</i> at 113</a></span>.</p>
<p>We have long recognized that a "compelled intrusio[n] into the body for blood to be analyzed for alcohol content" must be deemed a Fourth Amendment search. See <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 767-768</a></span> (1966). See also <i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#760" aria-description="Citation for case: Winston v. Lee">470 U. S. 753, 760</a></span> (1985). In light of our society's concern for the security of one's person, see, <i>e. g., </i><i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968), it is obvious that this physical intrusion, penetrating beneath the skin, infringes an expectation of privacy that society is prepared to recognize as reasonable. The ensuing chemical analysis of the sample to obtain physiological data is a further invasion of the tested employee's privacy interests. Cf. <i>Arizona</i> v. <i>Hicks,</i> <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#324" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 324-325</a></span> (1987). Much the same is true of the breath-testing procedures required under Subpart D of the regulations. Subjecting a person to a breathalyzer test, which generally requires the production of alveolar or "deep lung" breath for chemical analysis, see, <i>e. g., </i><i>California</i> v. <span class="star-pagination">*617</span> <i>Trombetta,</i> <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#481" aria-description="Citation for case: California v. Trombetta">467 U. S. 479, 481</a></span> (1984), implicates similar concerns about bodily integrity and, like the blood-alcohol test we considered in <i>Schmerber,</i> should also be deemed a search, see 1 W. LaFave, Search and Seizure § 2.6(a), p. 463 (1987). See also <i>Burnett</i> v. <i>Anchorage,</i> <span class="citation" data-id="480401"><a href="/opinion/480401/peter-burnett-and-daniel-c-ryan-v-municipality-of-anchorage-raymond-roop/#1449" aria-description="Citation for case: Peter Burnett and Daniel C. Ryan v. Municipality of...">806 F. 2d 1447, 1449</a></span> (CA9 1986); <i>Shoemaker</i> v. <i>Handel,</i> <span class="citation" data-id="473627"><a href="/opinion/473627/shoemaker-v-handel/#1141" aria-description="Citation for case: Shoemaker v. Handel">795 F. 2d 1136, 1141</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./479/986/">479 U. S. 986</a></span> (1986).</p>
<p>Unlike the blood-testing procedure at issue in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>,</i> the procedures prescribed by the FRA regulations for collecting and testing urine samples do not entail a surgical intrusion into the body. It is not disputed, however, that chemical analysis of urine, like that of blood, can reveal a host of private medical facts about an employee, including whether he or she is epileptic, pregnant, or diabetic. Nor can it be disputed that the process of collecting the sample to be tested, which may in some cases involve visual or aural monitoring of the act of urination, itself implicates privacy interests. As the Court of Appeals for the Fifth Circuit has stated:</p>
<blockquote>"There are few activities in our society more personal or private than the passing of urine. Most people describe it by euphemisms if they talk about it at all. It is a function traditionally performed without public observation; indeed, its performance in public is generally prohibited by law as well as social custom." <i>National Treasury Employees Union</i> v. <i>Von Raab,</i> <span class="citation" data-id="486563"><a href="/opinion/486563/national-treasury-employees-union-v-raab/#175" aria-description="Citation for case: National Treasury Employees Union v. Raab">816 F. 2d 170, 175</a></span> (1987).</blockquote>
<p>Because it is clear that the collection and testing of urine intrudes upon expectations of privacy that society has long recognized as reasonable, the Federal Courts of Appeals have concluded unanimously, and we agree, that these intrusions must be deemed searches under the Fourth Amendment.<sup>[4]</sup></p>
<p><span class="star-pagination">*618</span> In view of our conclusion that the collection and subsequent analysis of the requisite biological samples must be deemed Fourth Amendment searches, we need not characterize the employer's antecedent interference with the employee's freedom of movement as an independent Fourth Amendment seizure. As our precedents indicate, not every governmental interference with an individual's freedom of movement raises such constitutional concerns that there is a seizure of the person. See <i>United States</i> v. <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#9" aria-description="Citation for case: United States v. Dionisio"><i>Dionisio, supra,</i> at 9-11</a></span> (grand jury subpoena, though enforceable by contempt, does not effect a seizure of the person); <i>United States</i> v. <i>Mara,</i> <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#21" aria-description="Citation for case: United States v. Mara">410 U. S. 19, 21</a></span> (1973) (same). For present purposes, it suffices to note that any limitation on an employee's freedom of movement that is necessary to obtain the blood, urine, or breath samples contemplated by the regulations must be considered in assessing the intrusiveness of the searches effected by the Government's testing program. Cf. <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707-709</a></span> (1983).</p>
<p></p>
<h2>III</h2>
<p></p>
<h2>A</h2>
<p>To hold that the Fourth Amendment is applicable to the drug and alcohol testing prescribed by the FRA regulations <span class="star-pagination">*619</span> is only to begin the inquiry into the standards governing such intrusions. <i>O'Connor</i> v. <i>Ortega,</i> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#719" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 719</a></span> (1987) (plurality opinion); <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 337</a></span> (1985). For the Fourth Amendment does not proscribe all searches and seizures, but only those that are unreasonable. <i>United States</i> v. <i>Sharpe,</i> <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#682" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 682</a></span> (1985); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#768" aria-description="Citation for case: Schmerber v. California">384 U. S., at 768</a></span>. What is reasonable, of course, "depends on all of the circumstances surrounding the search or seizure and the nature of the search or seizure itself." <i>United States</i> v. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#537" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 537</a></span> (1985). Thus, the permissibility of a particular practice "is judged by balancing its intrusion on the individual's Fourth Amendment interests against its promotion of legitimate governmental interests." <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 654</a></span>; <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976).</p>
<p>In most criminal cases, we strike this balance in favor of the procedures described by the Warrant Clause of the Fourth Amendment. See <i>United States</i> v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 701</a></span>, and n. 2; <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#315" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 315</a></span> (1972). Except in certain well-defined circumstances, a search or seizure in such a case is not reasonable unless it is accomplished pursuant to a judicial warrant issued upon probable cause. See, <i>e. g., </i><i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980); <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> (1978). We have recognized exceptions to this rule, however, "when `special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.' " <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987), quoting <i>New Jersey</i> v. <i>T. L. O., supra,</i> at 351 (BLACKMUN, J., concurring in judgment). When faced with such special needs, we have not hesitated to balance the governmental and privacy interests to assess the practicality of the warrant and probable-cause requirements in the particular context. See, <i>e. g., </i><i>Griffin</i> v. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin"><i>Wisconsin, supra,</i> at 873</a></span> (search of probationer's home); <i>New York</i> v. <span class="star-pagination">*620</span> <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#699" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 699-703</a></span> (1987) (search of premises of certain highly regulated businesses); <i>O'Connor</i> v. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#721" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><i>Ortega, supra,</i> at 721-725</a></span> (work-related searches of employees' desks and offices); <i>New Jersey</i> v. <i>T. L. O., supra,</i> at 337-342 (search of student's property by school officials); <i>Bell</i> v. <i>Wolfish,</i> <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#558" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 558-560</a></span> (1979) (body cavity searches of prison inmates).</p>
<p>The Government's interest in regulating the conduct of railroad employees to ensure safety, like its supervision of probationers or regulated industries, or its operation of a government office, school, or prison, "likewise presents `special needs' beyond normal law enforcement that may justify departures from the usual warrant and probable-cause requirements." <i>Griffin</i> v. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin"><i>Wisconsin, supra,</i> at 873-874</a></span>. The hours of service employees covered by the FRA regulations include persons engaged in handling orders concerning train movements, operating crews, and those engaged in the maintenance and repair of signal systems. <span class="citation no-link">50 Fed. Reg. 31511</span> (1985). It is undisputed that these and other covered employees are engaged in safety-sensitive tasks. The FRA so found, and respondents conceded the point at oral argument. Tr. of Oral Arg. 46-47. As we have recognized, the whole premise of the Hours of Service Act is that "[t]he length of hours of service has direct relation to the efficiency of the human agencies upon which protection [of] life and property necessarily depends." <i>Baltimore &amp; Ohio R. Co.</i> v. <i>ICC,</i> <span class="citation" data-id="8142539"><a href="/opinion/8180620/baltimore-ohio-railroad-v-interstate-commerce-commission/#619" aria-description="Citation for case: Baltimore &amp; Ohio Railroad v. Interstate Commerce Commission">221 U. S. 612, 619</a></span> (1911). See also <i>Atchison, T. &amp; S. F. R. Co.</i> v. <i>United States,</i> <span class="citation" data-id="98973"><a href="/opinion/98973/atchison-topeka-santa-fe-railway-co-v-united-states/#342" aria-description="Citation for case: Atchison, Topeka &amp; Santa Fe Railway Co. v. United States">244 U. S. 336, 342</a></span> (1917) ("[I]t must be remembered that the purpose of the act was to prevent the dangers which must necessarily arise to the employee and to the public from continuing men in a dangerous and hazardous business for periods so long as to render them unfit to give that service which is essential to the protection of themselves and those entrusted to their care").</p>
<p>The FRA has prescribed toxicological tests, not to assist in the prosecution of employees, but rather "to prevent accidents <span class="star-pagination">*621</span> and casualties in railroad operations that result from impairment of employees by alcohol or drugs." <span class="citation no-link">49 CFR § 219.1</span>(a) (1987).<sup>[5]</sup> This governmental interest in ensuring the safety of the traveling public and of the employees themselves plainly justifies prohibiting covered employees from using alcohol or drugs on duty, or while subject to being called for duty. This interest also "require[s] and justif[ies] the exercise of supervision to assure that the restrictions are in fact observed." <i>Griffin</i> v. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#875" aria-description="Citation for case: Griffin v. Wisconsin"><i>Wisconsin, supra,</i> at 875</a></span>. The question that remains, then, is whether the Government's need to monitor compliance with these restrictions justifies the privacy intrusions at issue absent a warrant or individualized suspicion.</p>
<p></p>
<h2>B</h2>
<p>An essential purpose of a warrant requirement is to protect privacy interests by assuring citizens subject to a search <span class="star-pagination">*622</span> or seizure that such intrusions are not the random or arbitrary acts of government agents. A warrant assures the citizen that the intrusion is authorized by law, and that it is narrowly limited in its objectives and scope. See, <i>e. g., </i><i>New York</i> v. <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#703" aria-description="Citation for case: New York v. Burger"><i>Burger, supra,</i> at 703</a></span>; <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977); <i>Camara</i> v. <i>Municipal Court of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532</a></span>. A warrant also provides the detached scrutiny of a neutral magistrate, and thus ensures an objective determination whether an intrusion is justified in any given case. See <i>United States</i> v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick"><i>Chadwick, supra,</i> at 9</a></span>. In the present context, however, a warrant would do little to further these aims. Both the circumstances justifying toxicological testing and the permissible limits of such intrusions are defined narrowly and specifically in the regulations that authorize them, and doubtless are well known to covered employees. Cf. <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 316</a></span> (1972). Indeed, in light of the standardized nature of the tests and the minimal discretion vested in those charged with administering the program, there are virtually no facts for a neutral magistrate to evaluate. Cf. <i>Colorado</i> v. <i>Bertine,</i> <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#376" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 376</a></span> (1987) (BLACKMUN, J., concurring).<sup>[6]</sup></p>
<p><span class="star-pagination">*623</span> We have recognized, moreover, that the government's interest in dispensing with the warrant requirement is at its strongest when, as here, "the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search." <i>Camara</i> v. <i>Municipal Court of San Francisco, supra,</i> at 533. See also <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 340</a></span>; <i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 603</a></span> (1981). As the FRA recognized, alcohol and other drugs are eliminated from the bloodstream at a constant rate, see <span class="citation no-link">49 Fed. Reg. 24291</span> (1984), and blood and breath samples taken to measure whether these substances were in the bloodstream when a triggering event occurred must be obtained as soon as possible. See <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S., at 770-771</a></span>. Although the metabolites of some drugs remain in the urine for longer periods of time and may enable the FRA to estimate whether the employee was impaired by those drugs at the time of a covered accident, incident, or rule violation, <span class="citation no-link">49 Fed. Reg. 24291</span> (1984), the delay necessary to procure a warrant nevertheless may result in the destruction of valuable evidence.</p>
<p>The Government's need to rely on private railroads to set the testing process in motion also indicates that insistence on a warrant requirement would impede the achievement of the Government's objective. Railroad supervisors, like school officials, see <i>New Jersey</i> v. <i>T. L. O., supra,</i> at 339-340, and hospital administrators, see <i>O'Connor</i> v. <i>Ortega,</i> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#722" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S., at 722</a></span>, are not in the business of investigating violations of the criminal laws or enforcing administrative codes, and otherwise have little occasion to become familiar with the intricacies of this Court's Fourth Amendment jurisprudence. "Imposing unwieldy warrant procedures . . . upon supervisors, <span class="star-pagination">*624</span> who would otherwise have no reason to be familiar with such procedures, is simply unreasonable." <i><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">Ibid.</a></span></i></p>
<p>In sum, imposing a warrant requirement in the present context would add little to the assurances of certainty and regularity already afforded by the regulations, while significantly hindering, and in many cases frustrating, the objectives of the Government's testing program. We do not believe that a warrant is essential to render the intrusions here at issue reasonable under the Fourth Amendment.</p>
<p></p>
<h2>C</h2>
<p>Our cases indicate that even a search that may be performed without a warrant must be based, as a general matter, on probable cause to believe that the person to be searched has violated the law. See <i>New Jersey</i> v. <i>T. L. O., supra,</i> at 340. When the balance of interests precludes insistence on a showing of probable cause, we have usually required "some quantum of individualized suspicion" before concluding that a search is reasonable. See, <i>e. g., </i><i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 560</a></span>. We made it clear, however, that a showing of individualized suspicion is not a constitutional floor, below which a search must be presumed unreasonable. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 561</a></span>. In limited circumstances, where the privacy interests implicated by the search are minimal, and where an important governmental interest furthered by the intrusion would be placed in jeopardy by a requirement of individualized suspicion, a search may be reasonable despite the absence of such suspicion. We believe this is true of the intrusions in question here.</p>
<p>By and large, intrusions on privacy under the FRA regulations are limited. To the extent transportation and like restrictions are necessary to procure the requisite blood, breath, and urine samples for testing, this interference alone is minimal given the employment context in which it takes place. Ordinarily, an employee consents to significant restrictions in his freedom of movement where necessary for <span class="star-pagination">*625</span> his employment, and few are free to come and go as they please during working hours. See, <i>e. g., </i><i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#218" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S., at 218</a></span>. Any additional interference with a railroad employee's freedom of movement that occurs in the time it takes to procure a blood, breath, or urine sample for testing cannot, by itself, be said to infringe significant privacy interests.</p>
<p>Our decision in <i>Schmerber</i> v. <i>California, supra</i><i>,</i> indicates that the same is true of the blood tests required by the FRA regulations. In that case, we held that a State could direct that a blood sample be withdrawn from a motorist suspected of driving while intoxicated, despite his refusal to consent to the intrusion. We noted that the test was performed in a reasonable manner, as the motorist's "blood was taken by a physician in a hospital environment according to accepted medical practices." <i>Id.,</i> at 771. We said also that the intrusion occasioned by a blood test is not significant, since such "tests are a commonplace in these days of periodic physical examinations and experience with them teaches that the quantity of blood extracted is minimal, and that for most people the procedure involves virtually no risk, trauma, or pain." <i>Ibid. Schmerber</i> thus confirmed "society's judgment that blood tests do not constitute an unduly extensive imposition on an individual's privacy and bodily integrity." <i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#762" aria-description="Citation for case: Winston v. Lee">470 U. S., at 762</a></span>. See also <i>South Dakota</i> v. <i>Neville,</i> <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#563" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 563</a></span> (1983) ("The simple blood-alcohol test is . . . safe, painless, and commonplace"); <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#436" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 436</a></span> (1957) ("The blood test procedure has become routine in our everyday life").</p>
<p>The breath tests authorized by Subpart D of the regulations are even less intrusive than the blood tests prescribed by Subpart C. Unlike blood tests, breath tests do not require piercing the skin and may be conducted safely outside a hospital environment and with a minimum of inconvenience or embarrassment. Further, breath tests reveal the level of alcohol in the employee's bloodstream and nothing more. <span class="star-pagination">*626</span> Like the blood-testing procedures mandated by Subpart C, which can be used only to ascertain the presence of alcohol or controlled substances in the bloodstream, breath tests reveal no other facts in which the employee has a substantial privacy interest. Cf. <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#123" aria-description="Citation for case: United States v. Jacobsen">466 U. S., at 123</a></span>; <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S., at 707</a></span>. In all the circumstances, we cannot conclude that the administration of a breath test implicates significant privacy concerns.</p>
<p>A more difficult question is presented by urine tests. Like breath tests, urine tests are not invasive of the body and, under the regulations, may not be used as an occasion for inquiring into private facts unrelated to alcohol or drug use.<sup>[7]</sup> We recognize, however, that the procedures for collecting the necessary samples, which require employees to perform an excretory function traditionally shielded by great privacy, raise concerns not implicated by blood or breath tests. While we would not characterize these additional privacy concerns as minimal in most contexts, we note that the regulations endeavor to reduce the intrusiveness of the collection process. The regulations do not require that samples be furnished under the direct observation of a monitor, despite the desirability of such a procedure to ensure the integrity of the sample. See <span class="citation no-link">50 Fed. Reg. 31555</span> (1985). See also Field Manual B-15, D-1. The sample is also collected in a medical environment, by personnel unrelated to the railroad <span class="star-pagination">*627</span> employer, and is thus not unlike similar procedures encountered often in the context of a regular physical examination.</p>
<p>More importantly, the expectations of privacy of covered employees are diminished by reason of their participation in an industry that is regulated pervasively to ensure safety, a goal dependent, in substantial part, on the health and fitness of covered employees. This relation between safety and employee fitness was recognized by Congress when it enacted the Hours of Service Act in 1907, <i>Baltimore &amp; Ohio R. Co.</i> v. <i>ICC,</i> <span class="citation" data-id="8142539"><a href="/opinion/8180620/baltimore-ohio-railroad-v-interstate-commerce-commission/#619" aria-description="Citation for case: Baltimore &amp; Ohio Railroad v. Interstate Commerce Commission">221 U. S., at 619</a></span>, and also when it authorized the Secretary to "test . . . railroad facilities, equipment, rolling stock, operations, <i>or persons,</i> as he deems necessary to carry out the provisions" of the Federal Railroad Safety Act of 1970. <span class="citation no-link">45 U. S. C. § 437</span>(a) (emphasis added). It has also been recognized by state governments,<sup>[8]</sup> and has long been reflected in industry practice, as evidenced by the industry's promulgation and enforcement of Rule G. Indeed, the FRA found, and the Court of Appeals acknowledged, see <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#585" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d, at 585</a></span>, that "most railroads require periodic physical examinations for train and engine employees and certain other employees." <span class="citation no-link">49 Fed. Reg. 24278</span> (1984). See also <i>Railway Labor Executives Assn.</i> v. <i>Norfolk &amp; Western R. Co.,</i> <span class="citation" data-id="497335"><a href="/opinion/497335/railway-labor-executives-association-v-norfolk-and-western-railway-company/#705" aria-description="Citation for case: Railway Labor Executives Association v. Norfolk and...">833 F. 2d 700, 705-706</a></span> (CA7 1987); <i>Brotherhood of Maintenance of</i> <span class="star-pagination">*628</span> <i>Way Employees, Lodge 16</i> v. <i>Burlington Northern R. Co.,</i> <span class="citation" data-id="477827"><a href="/opinion/477827/brotherhood-of-maintenance-of-way-employees-lodge-16-v-burlington/#1024" aria-description="Citation for case: Brotherhood Of Maintenance Of Way Employees, Lodge 16 v....">802 F. 2d 1016, 1024</a></span> (CA8 1986).</p>
<p>We do not suggest, of course, that the interest in bodily security enjoyed by those employed in a regulated industry must always be considered minimal. Here, however, the covered employees have long been a principal focus of regulatory concern. As the dissenting judge below noted: "The reason is obvious. An idle locomotive, sitting in the round-house, is harmless. It becomes lethal when operated negligently by persons who are under the influence of alcohol or drugs." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#593" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d, at 593</a></span>. Though some of the privacy interests implicated by the toxicological testing at issue reasonably might be viewed as significant in other contexts, logic and history show that a diminished expectation of privacy attaches to information relating to the physical condition of covered employees and to this reasonable means of procuring such information. We conclude, therefore, that the testing procedures contemplated by Subparts C and D pose only limited threats to the justifiable expectations of privacy of covered employees.</p>
<p>By contrast, the Government interest in testing without a showing of individualized suspicion is compelling. Employees subject to the tests discharge duties fraught with such risks of injury to others that even a momentary lapse of attention can have disastrous consequences. Much like persons who have routine access to dangerous nuclear power facilities, see, <i>e. g., </i><i>Rushton</i> v. <i>Nebraska Public Power Dist.,</i> <span class="citation" data-id="504461"><a href="/opinion/504461/warren-h-rushton-and-david-l-lostroh-v-nebraska-public-power-district/#566" aria-description="Citation for case: Warren H. Rushton and David L. Lostroh v. Nebraska Public...">844 F. 2d 562, 566</a></span> (CA8 1988); <i>Alverado</i> v. <i>Washington Public Power Supply System,</i> <span class="citation" data-id="1215534"><a href="/opinion/1215534/alverado-v-washington-public-power-supply-system/#436" aria-description="Citation for case: Alverado v. Washington Public Power Supply System">111 Wash. 2d 424, 436</a></span>, <span class="citation" data-id="1215534"><a href="/opinion/1215534/alverado-v-washington-public-power-supply-system/#433" aria-description="Citation for case: Alverado v. Washington Public Power Supply System">759 P. 2d 427, 433-434</a></span> (1988), cert. pending, No. 88-645, employees who are subject to testing under the FRA regulations can cause great human loss before any signs of impairment become noticeable to supervisors or others. An impaired employee, the FRA found, will seldom display any outward "signs detectable by the lay person or, in many cases, even the physician." <span class="citation no-link">50 Fed. Reg. 31526</span> (1985). This view finds <span class="star-pagination">*629</span> ample support in the railroad industry's experience with Rule G, and in the judgment of the courts that have examined analogous testing schemes. See, <i>e. g., </i><i>Brotherhood of Maintenance Way Employees, Lodge 16</i> v. <i>Burlington Northern R. Co., supra,</i> at 1020. Indeed, while respondents posit that impaired employees might be detected without alcohol or drug testing,<sup>[9]</sup> the premise of respondents' lawsuit is that even the occurrence of a major calamity will not give rise to a suspicion of impairment with respect to any particular employee.</p>
<p>While no procedure can identify all impaired employees with ease and perfect accuracy, the FRA regulations supply an effective means of deterring employees engaged in safety-sensitive tasks from using controlled substances or alcohol in the first place. <span class="citation no-link">50 Fed. Reg. 31541</span> (1985). The railroad industry's experience with Rule G persuasively shows, and common sense confirms, that the customary dismissal sanction <span class="star-pagination">*630</span> that threatens employees who use drugs or alcohol while on duty cannot serve as an effective deterrent unless violators know that they are likely to be discovered. By ensuring that employees in safety-sensitive positions know they will be tested upon the occurrence of a triggering event, the timing of which no employee can predict with certainty, the regulations significantly increase the deterrent effect of the administrative penalties associated with the prohibited conduct, cf. <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#876" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 876</a></span>, concomitantly increasing the likelihood that employees will forgo using drugs or alcohol while subject to being called for duty.</p>
<p>The testing procedures contemplated by Subpart C also help railroads obtain invaluable information about the causes of major accidents, see <span class="citation no-link">50 Fed. Reg. 31541</span> (1985), and to take appropriate measures to safeguard the general public. Cf. <i>Michigan</i> v. <i>Tyler,</i> <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#510" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 510</a></span> (1978) (noting that prompt investigation of the causes of a fire may uncover continuing dangers and thereby prevent the fire's recurrence); <i>Michigan</i> v. <i>Clifford,</i> <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#308" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287, 308</a></span> (1984) (REHNQUIST, J., dissenting) (same). Positive test results would point toward drug or alcohol impairment on the part of members of the crew as a possible cause of an accident, and may help to establish whether a particular accident, otherwise not drug related, was made worse by the inability of impaired employees to respond appropriately. Negative test results would likewise furnish invaluable clues, for eliminating drug impairment as a potential cause or contributing factor would help establish the significance of equipment failure, inadequate training, or other potential causes, and suggest a more thorough examination of these alternatives. Tests performed following the rule violations specified in Subpart D likewise can provide valuable information respecting the causes of those transgressions, which the FRA found to involve "the potential for a serious train accident or grave personal injury, or both." <span class="citation no-link">50 Fed. Reg. 31553</span> (1985).</p>
<p><span class="star-pagination">*631</span> A requirement of particularized suspicion of drug or alcohol use would seriously impede an employer's ability to obtain this information, despite its obvious importance. Experience confirms the FRA's judgment that the scene of a serious rail accident is chaotic. Investigators who arrive at the scene shortly after a major accident has occurred may find it difficult to determine which members of a train crew contributed to its occurrence. Obtaining evidence that might give rise to the suspicion that a particular employee is impaired, a difficult endeavor in the best of circumstances, is most impracticable in the aftermath of a serious accident. While events following the rule violations that activate the testing authority of Subpart D may be less chaotic, objective indicia of impairment are absent in these instances as well. Indeed, any attempt to gather evidence relating to the possible impairment of particular employees likely would result in the loss or deterioration of the evidence furnished by the tests. Cf. <i>Michigan</i> v. <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#293" aria-description="Citation for case: Michigan v. Clifford"><i>Clifford, supra,</i> at 293, n. 4</a></span> (plurality opinion); <i>Michigan</i> v. <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#510" aria-description="Citation for case: Michigan v. Tyler"><i>Tyler, supra,</i> at 510</a></span>. It would be unrealistic, and inimical to the Government's goal of ensuring safety in rail transportation, to require a showing of individualized suspicion in these circumstances.</p>
<p>Without quarreling with the importance of these governmental interests, the Court of Appeals concluded that the postaccident testing regulations were unreasonable because "[b]lood and urine tests intended to establish drug use other than alcohol . . . cannot measure current drug intoxication or degree of impairment." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#588" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d, at 588</a></span>. The court based its conclusion on its reading of certain academic journals that indicate that the testing of urine can disclose only drug metabolites, which "may remain in the body for days or weeks after the ingestion of the drug." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#589" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 589</a></span>. We find this analysis flawed for several reasons.</p>
<p>As we emphasized in <i>New Jersey</i> v. <i>T. L. O</i><i>.,</i> "it is universally recognized that evidence, to be relevant to an inquiry, need not conclusively prove the ultimate fact in issue, but <span class="star-pagination">*632</span> only have `any tendency to make the existence of any fact that is of consequence to the determination [of the point in issue] more probable or less probable than it would be without the evidence.' " <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#345" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 345</a></span>, quoting Fed. Rule Evid. 401. Even if urine test results disclosed nothing more specific than the recent use of controlled substances by a covered employee, this information would provide the basis for further investigative work designed to determine whether the employee used drugs at the relevant times. See Field Manual B-4. The record makes clear, for example, that a positive test result, coupled with known information concerning the pattern of elimination for the particular drug and information that may be gathered from other sources about the employee's activities, may allow the FRA to reach an informed judgment as to how a particular accident occurred. See <i>supra,</i> at 609-610.</p>
<p>More importantly, the Court of Appeals overlooked the FRA's policy of placing principal reliance on the results of blood tests, which unquestionably can identify very recent drug use, see, <i>e. g.,</i> <span class="citation no-link">49 Fed. Reg. 24291</span> (1984), while relying on urine tests as a secondary source of information designed to guard against the possibility that certain drugs will be eliminated from the bloodstream before a blood sample can be obtained. The court also failed to recognize that the FRA regulations are designed not only to discern impairment but also to deter it. Because the record indicates that blood and urine tests, taken together, are highly effective means of ascertaining on-the-job impairment and of deterring the use of drugs by railroad employees, we believe the Court of Appeals erred in concluding that the postaccident testing regulations are not reasonably related to the Government objectives that support them.<sup>[10]</sup></p>
<p><span class="star-pagination">*633</span> We conclude that the compelling Government interests served by the FRA's regulations would be significantly hindered if railroads were required to point to specific facts giving rise to a reasonable suspicion of impairment before testing a given employee. In view of our conclusion that, on the present record, the toxicological testing contemplated by the regulations is not an undue infringement on the justifiable expectations of privacy of covered employees, the Government's compelling interests outweigh privacy concerns.</p>
<p></p>
<h2>IV</h2>
<p>The possession of unlawful drugs is a criminal offense that the Government may punish, but it is a separate and far more dangerous wrong to perform certain sensitive tasks while under the influence of those substances. Performing those tasks while impaired by alcohol is, of course, equally dangerous, though consumption of alcohol is legal in most other contexts. The Government may take all necessary and reasonable regulatory steps to prevent or deter that hazardous conduct, and since the gravamen of the evil is performing certain functions while concealing the substance in the body, it may be necessary, as in the case before us, to examine the body or its fluids to accomplish the regulatory purpose. The necessity to perform that regulatory function with respect to railroad employees engaged in safety-sensitive tasks, and the reasonableness of the system for doing so, have been established in this case.</p>
<p>Alcohol and drug tests conducted in reliance on the authority of Subpart D cannot be viewed as private action outside the reach of the Fourth Amendment. Because the testing procedures mandated or authorized by Subparts C and D effect <span class="star-pagination">*634A</span> searches of the person, they must meet the Fourth Amendment's reasonableness requirement. In light of the limited discretion exercised by the railroad employers under the regulations, the surpassing safety interests served by toxicological tests in this context, and the diminished expectation of privacy that attaches to information pertaining to the fitness of covered employees, we believe that it is reasonable to conduct such tests in the absence of a warrant or reasonable suspicion that any particular employee may be impaired. We hold that the alcohol and drug tests contemplated by Subparts C and D of the FRA's regulations are reasonable within the meaning of the Fourth Amendment. The judgment of the Court of Appeals is accordingly reversed.</p>
<p><i>It is so ordered.</i></p>
<p><span class="star-pagination">*634B</span> JUSTICE STEVENS, concurring in part and concurring in the judgment.</p>
<p>In my opinion the public interest in determining the causes of serious railroad accidents adequately supports the validity of the challenged regulations. I am not persuaded, however, that the interest in deterring the use of alcohol or drugs is either necessary or sufficient to justify the searches authorized by these regulations.</p>
<p>I think it a dubious proposition that the regulations significantly deter the use of alcohol and drugs by hours of service employees. Most people  and I would think most railroad employees as well  do not go to work with the expectation that they may be involved in a major accident, particularly one causing such catastrophic results as loss of life or the release of hazardous material requiring an evacuation. Moreover, even if they are conscious of the possibilities that such an accident might occur and that alcohol or drug use might be a contributing factor, if the risk of serious personal injury does not deter their use of these substances, it seems highly unlikely that the additional threat of loss of employment would have any effect on their behavior.</p>
<p><span class="star-pagination">*635</span> For this reason, I do not join the portions of Part III of the Court's opinion that rely on a deterrence rationale; I do, however, join the balance of the opinion and the Court's judgment.</p>
<p>JUSTICE MARSHALL, with whom JUSTICE BRENNAN joins, dissenting.</p>
<p>The issue in this case is not whether declaring a war on illegal drugs is good public policy. The importance of ridding our society of such drugs is, by now, apparent to all. Rather, the issue here is whether the Government's deployment in that war of a particularly Draconian weapon  the compulsory collection and chemical testing of railroad workers' blood and urine  comports with the Fourth Amendment. Precisely because the need for action against the drug scourge is manifest, the need for vigilance against unconstitutional excess is great. History teaches that grave threats to liberty often come in times of urgency, when constitutional rights seem too extravagant to endure. The World War II relocation-camp cases, <i>Hirabayashi</i> v. <i>United States,</i> <span class="citation" data-id="9419386"><a href="/opinion/103875/hirabayashi-v-united-states/" aria-description="Citation for case: Hirabayashi v. United States">320 U. S. 81</a></span> (1943); <i>Korematsu</i> v. <i>United States,</i> <span class="citation" data-id="9419548"><a href="/opinion/104040/korematsu-v-united-states/" aria-description="Citation for case: Korematsu v. United States">323 U. S. 214</a></span> (1944), and the Red scare and McCarthy-era internal subversion cases, <i>Schenck</i> v. <i>United States,</i> <span class="citation" data-id="99296"><a href="/opinion/99296/schenck-v-united-states/" aria-description="Citation for case: Schenck v. United States">249 U. S. 47</a></span> (1919); <i>Dennis</i> v. <i>United States,</i> <span class="citation" data-id="9420605"><a href="/opinion/104914/dennis-v-united-states/" aria-description="Citation for case: Dennis v. United States">341 U. S. 494</a></span> (1951), are only the most extreme reminders that when we allow fundamental freedoms to be sacrificed in the name of real or perceived exigency, we invariably come to regret it.</p>
<p>In permitting the Government to force entire railroad crews to submit to invasive blood and urine tests, even when it lacks any evidence of drug or alcohol use or other wrongdoing, the majority today joins those shortsighted courts which have allowed basic constitutional rights to fall prey to momentary emergencies. The majority holds that the need of the Federal Railroad Administration (FRA) to deter and diagnose train accidents outweighs any "minimal" intrusions on personal dignity and privacy posed by mass toxicological testing of persons who have given no indication whatsoever of <span class="star-pagination">*636</span> impairment. <i>Ante,</i> at 624. In reaching this result, the majority ignores the text and doctrinal history of the Fourth Amendment, which require that highly intrusive searches of this type be based on probable cause, not on the evanescent cost-benefit calculations of agencies or judges. But the majority errs even under its own utilitarian standards, trivializing the raw intrusiveness of, and overlooking serious conceptual and operational flaws in, the FRA's testing program. These flaws cast grave doubts on whether that program, though born of good intentions, will do more than ineffectually symbolize the Government's opposition to drug use.</p>
<p>The majority purports to limit its decision to postaccident testing of workers in "safety-sensitive" jobs, <i>ante,</i> at 620, much as it limits its holding in the companion case to the testing of transferees to jobs involving drug interdiction or the use of firearms. <i>Treasury Employees</i> v. <i>Von Raab, post,</i> at 664. But the damage done to the Fourth Amendment is not so easily cabined. The majority's acceptance of dragnet blood and urine testing ensures that the first, and worst, casualty of the war on drugs will be the precious liberties of our citizens. I therefore dissent.</p>
<p></p>
<h2>I</h2>
<p>The Court today takes its longest step yet toward reading the probable-cause requirement out of the Fourth Amendment. For the fourth time in as many years, a majority holds that a " `special nee[d], beyond the normal need for law enforcement,' " makes the " `requirement' " of probable cause " `impracticable.' " <i>Ante,</i> at 619 (citations omitted). With the recognition of "[t]he Government's interest in regulating the conduct of railroad employees to ensure safety" as such a need, <i>ante,</i> at 620, the Court has now permitted "special needs" to displace constitutional text in each of the four categories of searches enumerated in the Fourth Amendment: searches of "persons," <i>ante,</i> at 613-614; "houses," <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868</a></span> (1987); "papers," <i>O'Connor</i> v. <i>Ortega,</i> <span class="star-pagination">*637</span> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987); and "effects," <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325</a></span> (1985).</p>
<p>The process by which a constitutional "requirement" can be dispensed with as "impracticable" is an elusive one to me. The Fourth Amendment provides that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated; and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." The majority's recitation of the Amendment, remarkably, leaves off after the word "violated," <i>ante,</i> at 613, but the remainder of the Amendment  the Warrant Clause  is not so easily excised. As this Court has long recognized, the Framers intended the provisions of that Clause  a warrant and probable cause  to "provide the yardstick against which official searches and seizures are to be measured." <i>T. L. O., supra,</i> at 359-360 (opinion of BRENNAN, J.). Without the content which those provisions give to the Fourth Amendment's overarching command that searches and seizures be "reasonable," the Amendment lies virtually devoid of meaning, subject to whatever content shifting judicial majorities, concerned about the problems of the day, choose to give to that supple term. See <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213</a></span> (1979) ("[T]he protections intended by the Framers could all too easily disappear in the consideration and balancing of the multifarious circumstances presented by different cases"). Constitutional requirements like probable cause are not fair-weather friends, present when advantageous, conveniently absent when "special needs" make them seem not.</p>
<p>Until recently, an unbroken line of cases had recognized probable cause as an indispensable prerequisite for a full-scale search, regardless of whether such a search was conducted pursuant to a warrant or under one of the recognized exceptions to the warrant requirement. <i>T. L. O., supra,</i> at 358 <span class="star-pagination">*638</span> and 359, n. 3 (opinion of BRENNAN, J.); see also <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 51</a></span> (1970). Only where the government action in question had a "substantially less intrusive" impact on privacy, <i>Dunaway,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#210" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 210</a></span>, and thus clearly fell short of a full-scale search, did we relax the probable-cause standard. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#214" aria-description="Citation for case: Dunaway v. New York"><i>Id.,</i> at 214</a></span> ("For all but those narrowly defined intrusions, the requisite `balancing' . . . is embodied in the principle that seizures are `reasonable' only if supported by probable cause"); see also <i>T. L. O., supra,</i> at 360 (opinion of BRENNAN, J.). Even in this class of cases, we almost always required the government to show some individualized suspicion to justify the search.<sup>[1]</sup> The few searches which we upheld in the absence of individualized justification were routinized, fleeting, and nonintrusive encounters conducted pursuant to regulatory programs which entailed no contact with the person.<sup>[2]</sup></p>
<p><span class="star-pagination">*639</span> In the four years since this Court, in <i>T. L. O.,</i> first began recognizing "special needs" exceptions to the Fourth Amendment, the clarity of Fourth Amendment doctrine has been badly distorted, as the Court has eclipsed the probable-cause requirement in a patchwork quilt of settings: public school principals' searches of students' belongings, <i>T. L. O.;</i> public employers' searches of employees' desks, <i><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O'Connor</a></span>;</i> and probation officers' searches of probationers' homes, <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span>.</i><sup>[3]</sup> Tellingly, each time the Court has found that "special needs" counseled ignoring the literal requirements of the Fourth Amendment for such full-scale searches in favor of a formless and unguided "reasonableness" balancing inquiry, it has concluded that the search in question satisfied that test. I have joined dissenting opinions in each of these cases, protesting the "jettison[ing of] . . . the only standard that finds support in the text of the Fourth Amendment" and predicting that the majority's "Rohrschach-like `balancing test' " portended "a dangerous weakening of the purpose of the Fourth Amendment to protect the privacy and security of our citizens." <i>T. L. O., supra,</i> at 357-358 (opinion of BRENNAN, J.).</p>
<p>The majority's decision today bears out that prophecy. After determining that the Fourth Amendment applies to the FRA's testing regime, the majority embarks on an extended inquiry into whether that regime is "reasonable," an inquiry in which it balances " `all of the circumstances surrounding the search or seizure and the nature of the search or seizure itself.' " <i>Ante,</i> at 619, quoting <i>United States</i> v. <i>Montoya de</i> <span class="star-pagination">*640</span> <i>Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#537" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 537</a></span> (1985). The result is "special needs" balancing analysis' deepest incursion yet into the core protections of the Fourth Amendment. Until today, it was conceivable that, when a government search was aimed at a person and not simply the person's possessions, balancing analysis had no place. No longer: with nary a word of explanation or acknowledgment of the novelty of its approach, the majority extends the "special needs" framework to a regulation involving compulsory blood withdrawal and urinary excretion, and chemical testing of the bodily fluids collected through these procedures. And until today, it was conceivable that a prerequisite for surviving "special needs" analysis was the existence of individualized suspicion. No longer: in contrast to the searches in <i>T. L. O., O'Connor,</i> and <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span>,</i> which were supported by individualized evidence suggesting the culpability of the persons whose property was searched,<sup>[4]</sup> the regulatory regime upheld today requires the postaccident collection and testing of the blood and urine of <i>all</i> covered employees  even if every member of this group gives every indication of sobriety and attentiveness.</p>
<p>In widening the "special needs" exception to probable cause to authorize searches of the human body unsupported by <i>any</i> evidence of wrongdoing, the majority today completes the process begun in <i>T. L. O.</i> of eliminating altogether the probable-cause requirement for civil searches  those undertaken for reasons "beyond the normal need for law enforcement." <i>Ante,</i> at 619 (citations omitted). In its place, the majority substitutes a manipulable balancing inquiry under which, upon the mere assertion of a "special need," even the deepest dignitary and privacy interests become vulnerable <span class="star-pagination">*641</span> to governmental incursion. See <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">ibid.</a></span></i> (distinguishing criminal from civil searches). By its terms, however, the Fourth Amendment  unlike the Fifth and Sixth  does not confine its protections to either criminal or civil actions. Instead, it protects generally "[t]he right of the people to be secure."<sup>[5]</sup></p>
<p>The fact is that the malleable "special needs" balancing approach can be justified only on the basis of the policy results it allows the majority to reach. The majority's concern with the railroad safety problems caused by drug and alcohol abuse is laudable; its cavalier disregard for the text of the Constitution is not. There is no drug exception to the Constitution, any more than there is a communism exception or an exception for other real or imagined sources of domestic unrest. <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#455" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 455</a></span> (1971). Because abandoning the explicit protections of the Fourth Amendment seriously imperils "the right to be let alone  the most comprehensive of rights and the right most valued by civilized men," <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 478</a></span> (1928) (Brandeis, J., dissenting), I reject the majority's "special needs" rationale as unprincipled and dangerous.</p>
<p></p>
<h2>II</h2>
<p>The proper way to evaluate the FRA's testing regime is to use the same analytic framework which we have traditionally used to appraise Fourth Amendment claims involving fullscale searches, at least until the recent "special needs" cases. Under that framework, we inquire, serially, whether a <span class="star-pagination">*642</span> search has taken place, see, <i>e. g., </i><i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 350-353</a></span> (1967); whether the search was based on a valid warrant or undertaken pursuant to a recognized exception to the warrant requirement, see, <i>e. g., </i><i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#748" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 748-750</a></span> (1984); whether the search was based on probable cause or validly based on lesser suspicion because it was minimally intrusive, see, <i>e. g., </i><i>Dunaway,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#208" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 208-210</a></span>; and, finally, whether the search was conducted in a reasonable manner, see, <i>e. g., </i><i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#763" aria-description="Citation for case: Winston v. Lee">470 U. S. 753, 763-766</a></span> (1985). See also <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#354" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 354-355</a></span> (opinion of BRENNAN, J.) (summarizing analytic framework).</p>
<p>The majority's threshold determination that "covered" railroad employees have been searched under the FRA's testing program is certainly correct. <i>Ante,</i> at 616-618. Who among us is not prepared to consider reasonable a person's expectation of privacy with respect to the extraction of his blood, the collection of his urine, or the chemical testing of these fluids? <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984).<sup>[6]</sup> The majority's ensuing conclusion that the warrant requirement may be dispensed with, however, conveniently overlooks the fact that there are three distinct searches at issue. Although the importance of collecting blood and urine samples before drug or alcohol metabolites disappear justifies waiving the warrant requirement for those two searches under the narrow "exigent circumstances" exception, see <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770</a></span> (1966) ("[T]he delay necessary to obtain a warrant . . . threaten[s] `the destruction of evidence' "), no such exigency prevents railroad officials from securing a warrant before chemically testing the samples they obtain. Blood and urine do not spoil if <span class="star-pagination">*643</span> properly collected and preserved, and there is no reason to doubt the ability of railroad officials to grasp the relatively simple procedure of obtaining a warrant authorizing, where appropriate, chemical analysis of the extracted fluids. It is therefore wholly unjustified to dispense with the warrant requirement for this final search. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#761" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 761-764</a></span> (1969) (exigency exception permits warrantless searches only to the extent that exigency exists).</p>
<p>It is the probable-cause requirement, however, that the FRA's testing regime most egregiously violates, a fact which explains the majority's ready acceptance and expansion of the countertextual "special needs" exception. By any measure, the FRA's highly intrusive collection and testing procedures qualify as full-scale personal searches. Under our precedents, a showing of probable cause is therefore clearly required. But even if these searches were viewed as entailing only minimal intrusions on the order, say, of a police stop-and-frisk, the FRA's program would still fail to pass constitutional muster, for we have, without exception, demanded that even minimally intrusive searches of the person be founded on individualized suspicion. See <i>supra,</i> at 638, and n. 1. The federal parties concede it does not satisfy this standard. Brief for Federal Parties 18. Only if one construes the FRA's collection and testing procedures as akin to the routinized and fleeting regulatory interactions which we have permitted in the absence of individualized suspicion, see n. 2, <i>supra,</i> might these procedures survive constitutional scrutiny. Presumably for this reason, the majority likens this case to <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), which upheld brief automobile stops at the border to ascertain the validity of motorists' residence in the United States. <i>Ante,</i> at 624. Case law and common sense reveal both the bankruptcy of this absurd analogy and the constitutional imperative of adhering to the textual standard of probable cause to evaluate the FRA's multifarious full-scale searches.</p>
<p><span class="star-pagination">*644</span> Compelling a person to submit to the piercing of his skin by a hypodermic needle so that his blood may be extracted significantly intrudes on the "personal privacy and dignity against unwarranted intrusion by the State" against which the Fourth Amendment protects. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California"><i>Schmerber, supra,</i> at 767</a></span>. As we emphasized in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 24-25</a></span> (1968), "Even a limited search of the outer clothing . . . constitutes a severe, though brief, intrusion upon cherished personal security, and it must surely be an annoying, frightening, and perhaps humiliating experience." We have similarly described the taking of a suspect's fingernail scrapings as a " `severe, though brief, intrusion upon cherished personal security.' " <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#295" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 295</a></span> (1973) (quoting <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 24-25</a></span>, and upholding this procedure upon a showing of probable cause). The government-compelled withdrawal of blood, involving as it does the added aspect of physical invasion, is surely no less an intrusion. The surrender of blood on demand is, furthermore, hardly a quotidian occurrence. Cf. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 557</a></span> (routine stops involve "quite limited" intrusion).</p>
<p>In recognition of the intrusiveness of this procedure, we specifically required in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> that police have evidence of a drunken-driving suspect's impairment before forcing him to endure a blood test:</p>
<blockquote>"The interests in human dignity and privacy which the Fourth Amendment protects forbid any such intrusions on the mere chance that desired evidence might be obtained. In the absence of a clear indication that in fact such evidence will be found, these fundamental human interests require law officers to suffer the risk that such evidence may disappear . . . ." <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#769" aria-description="Citation for case: Schmerber v. California">384 U. S., at 769-770</a></span>.</blockquote>
<p><i>Schmerber</i> strongly suggested that the "clear indication" needed to justify a compulsory blood test amounted to a showing of probable cause, which "plainly" existed in that case. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#768" aria-description="Citation for case: Schmerber v. California"><i>Id.,</i> at 768</a></span>. Although subsequent cases interpreting <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> have differed over whether a showing of individualized <span class="star-pagination">*645</span> suspicion would have sufficed, compare <i>Winston,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#760" aria-description="Citation for case: Winston v. Lee">470 U. S., at 760</a></span> (<span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California"><i>Schmerber</i></a></span> "noted the importance of probable cause"), with <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#540" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S., at 540</a></span> (<span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California"><i>Schmerber</i></a></span> "indicate[d] the necessity for particularized suspicion"), by any reading, <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> clearly forbade compulsory blood tests on any lesser showing than individualized suspicion. Exactly why a blood test which, if conducted on one person, requires a showing of at least individualized suspicion may, if conducted on many persons, be based on no showing whatsoever, the majority does not  and cannot  explain.<sup>[7]</sup></p>
<p>Compelling a person to produce a urine sample on demand also intrudes deeply on privacy and bodily integrity. Urination is among the most private of activities. It is generally forbidden in public, eschewed as a matter of conversation, and performed in places designed to preserve this tradition of <span class="star-pagination">*646</span> personal seclusion. Cf. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 560</a></span> (border-stop questioning involves no more than "some annoyance" and is neither "frightening" nor "offensive"). The FRA, however, gives scant regard to personal privacy, for its Field Manual instructs supervisors monitoring urination that railroad workers must provide urine samples "<i>under direct observation</i> by the physician/technician." Federal Railroad Administration, United States Dept. of Transportation, Field Manual: Control of Alcohol and Drug Use in Railroad Operations D-5 (1986) (emphasis added).<sup>[8]</sup> That the privacy interests offended by compulsory and supervised urine collection are profound is the overwhelming judgment of the lower courts and commentators. As Professor  later Solicitor General  Charles Fried has written:</p>
<blockquote>"[I]n our culture the excretory functions are shielded by more or less absolute privacy, so much so that situations in which this privacy is violated are experienced as extremely distressing, as detracting from one's dignity and self esteem." Privacy, 77 Yale L. J. 475, 487 (1968).<sup>[9]</sup></blockquote>
<p>The majority's characterization of the privacy interests implicated by urine collection as "minimal," <i>ante,</i> at 624, is nothing <span class="star-pagination">*647</span> short of startling. This characterization is, furthermore, belied by the majority's own prior explanation of why compulsory urination constitutes a search for the purposes of the Fourth Amendment:</p>
<blockquote>" `There are few activities in our society more personal or private than the passing of urine. Most people describe it by euphemisms if they talk about it at all. It is a function traditionally performed without public observation; indeed, its performance in public is generally prohibited by law as well as social custom.' " <i>Ante,</i> at 617, quoting <i>National Treasury Employees Union</i> v. <i>Von Raab,</i> <span class="citation" data-id="486563"><a href="/opinion/486563/national-treasury-employees-union-v-raab/#175" aria-description="Citation for case: National Treasury Employees Union v. Raab">816 F. 2d 170, 175</a></span> (CA5 1987).</blockquote>
<p>The fact that the majority can invoke this powerful passage in the context of deciding that a search has occurred, and then ignore it in deciding that the privacy interests this search implicates are "minimal," underscores the shameless manipulability of its balancing approach.</p>
<p>Finally, the chemical analysis the FRA performs upon the blood and urine samples implicates strong privacy interests apart from those intruded upon by the collection of bodily fluids. Technological advances have made it possible to uncover, through analysis of chemical compounds in these fluids, not only drug or alcohol use, but also medical disorders such as epilepsy, diabetes, and clinical depression. Cf. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 558</a></span>, quoting <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 880</a></span> (1975) (checkpoint inquiry involves only " `a brief question or two' " about motorist's residence). As the Court of Appeals for the District of Columbia Circuit has observed: "[S]uch tests may provide Government officials with a periscope through which they can peer into an individual's behavior in her private life, even in her own home." <i>Jones</i> v. <i>McKenzie,</i> 266 U. S. App. D. C. 85, 89, <span class="citation" data-id="497255"><a href="/opinion/497255/juanita-m-jones-v-floretta-dukes-mckenzie-superintendent-of-schools/#339" aria-description="Citation for case: Juanita M. Jones v. Floretta Dukes McKenzie...">833 F. 2d 335, 339</a></span> (1987); see also <i>Capua</i> v. <i>Plainfield,</i> <span class="citation" data-id="1908384"><a href="/opinion/1908384/capua-v-city-of-plainfield/#1511" aria-description="Citation for case: Capua v. City of Plainfield">643 F. Supp. 1507, 1511</a></span> (NJ 1986) (urine testing is "form of surveillance" which "reports on a person's off-duty activities just as surely as someone had been present and <span class="star-pagination">*648</span> watching"). The FRA's requirement that workers disclose the medications they have taken during the 30 days prior to chemical testing further impinges upon the confidentiality customarily attending personal health secrets.</p>
<p>By any reading of our precedents, the intrusiveness of these three searches demands that they  like other full-scale searches  be justified by probable cause. It is no answer to suggest, as does the majority, that railroad workers have relinquished the protection afforded them by this Fourth Amendment requirement, either by "participat[ing] in an industry that is regulated pervasively to ensure safety" or by undergoing periodic fitness tests pursuant to state law or to collective-bargaining agreements. <i>Ante,</i> at 627.</p>
<p>Our decisions in the regulatory search area refute the suggestion that the heavy regulation of the railroad industry eclipses workers' rights under the Fourth Amendment to insist upon a showing of probable cause when their bodily fluids are being extracted. This line of cases has exclusively involved searches of employer <i>property,</i> with respect to which "[c]ertain industries have such a history of government oversight that no reasonable expectation of privacy could exist for a <i>proprietor</i> over the <i>stock</i> of such an enterprise." <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 313</a></span> (1978) (emphasis added; citation omitted), quoted in <i>New York</i> v. <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#700" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 700</a></span> (1987). Never have we intimated that regulatory searches reduce employees' right of privacy in their <i>persons.</i> See <i>Camara</i> v. <i>Municipal Court of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 537</a></span> (1967) ("[T]he inspections are [not] personal in nature"); cf. <i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#598" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 598-599</a></span> (1981); <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>Marshall, supra,</i> at 313</a></span>. As the Court pointed out in <i><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O'Connor</a></span>,</i> individuals do not lose Fourth Amendment rights at the workplace gate, 480 U. S., at 716-718; see also <i>Oliver</i> v. <i>United States,</i> <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 178, n. 8</a></span> (1984), any more than they relinquish these rights at the schoolhouse door, <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#333" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 333</a></span>, or the hotel room threshold, <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#301" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 301</a></span> (1966). These rights mean <span class="star-pagination">*649</span> little indeed if, having passed through these portals, an individual may remain subject to a suspicionless search of his person justified solely on the grounds that the government already is permitted to conduct a search of the inanimate contents of the surrounding area. In holding that searches of persons may fall within the category of regulatory searches permitted in the absence of probable cause or even individualized suspicion, the majority sets a dangerous and ill-conceived precedent.</p>
<p>The majority's suggestion that railroad workers' privacy is only minimally invaded by the collection and testing of their bodily fluids because they undergo periodic fitness tests, <i>ante,</i> at 624-625, is equally baseless. As an initial matter, even if participation in these fitness tests did render "minimal" an employee's "interest in bodily security," <i>ante,</i> at 628, such minimally intrusive searches of the person require, under our precedents, a justificatory showing of individualized suspicion. See <i>supra,</i> at 637. More fundamentally, railroad employees are <i>not</i> routinely required to submit to blood or urine tests to gain or to maintain employment, and railroad employers do not ordinarily have access to employees' blood or urine, and certainly not for the purpose of ascertaining drug or alcohol usage. That railroad employees sometimes undergo tests of eyesight, hearing, skill, intelligence, and agility, <i>ante,</i> at 627, n. 8, hardly prepares them for Government demands to submit to the extraction of blood, to excrete under supervision, or to have these bodily fluids tested for the physiological and psychological secrets they may contain. Surely employees who release basic information about their financial and personal history so that employers may ascertain their "ethical fitness" do not, by so doing, relinquish their expectations of privacy with respect to their personal letters and diaries, revealing though these papers may be of their character.</p>
<p>I recognize that invalidating the full-scale searches involved in the FRA's testing regime for failure to comport with the Fourth Amendment's command of probable cause <span class="star-pagination">*650</span> may hinder the Government's attempts to make rail transit as safe as humanly possible. But constitutional rights have their consequences, and one is that efforts to maximize the public welfare, no matter how well intentioned, must always be pursued within constitutional boundaries. Were the police freed from the constraints of the Fourth Amendment for just one day to seek out evidence of criminal wrongdoing, the resulting convictions and incarcerations would probably prevent thousands of fatalities. Our refusal to tolerate this specter reflects our shared belief that even beneficent governmental power  whether exercised to save money, save lives, or make the trains run on time  must always yield to "a resolute loyalty to constitutional safeguards." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#273" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 273</a></span> (1973). The Constitution demands no less loyalty here.</p>
<p></p>
<h2>III</h2>
<p>Even accepting the majority's view that the FRA's collection and testing program is appropriately analyzed under a multifactor balancing test, and not under the literal terms of the Fourth Amendment, I would still find the program invalid. The benefits of suspicionless blood and urine testing are far outstripped by the costs imposed on personal liberty by such sweeping searches. Only by erroneously deriding as "minimal" the privacy and dignity interests at stake, and by uncritically inflating the likely efficacy of the FRA's testing program, does the majority strike a different balance.</p>
<p>For the reasons stated above, I find nothing minimal about the intrusion on individual liberty that occurs whenever the Government forcibly draws and analyzes a person's blood and urine. Several aspects of the FRA's testing program exacerbate the intrusiveness of these procedures. Most strikingly, the agency's regulations not only do not forbid, but, in fact, appear to invite criminal prosecutors to obtain the blood and urine samples drawn by the FRA and use them as the basis of criminal investigations and trials. See 49 CFR <span class="star-pagination">*651</span> § 219.211(d) (1987) ("Each sample . . . may be made available to . . . a party in litigation upon service of appropriate compulsory process on the custodian of the sample . . ."). This is an unprecedented invitation, leaving open the possibility of criminal prosecutions based on suspicionless searches of the human body. Cf. <i>Treasury Employees, post,</i> at 666 (Customs Service drug-testing program prohibits use of test results in criminal prosecutions); <i>Camara,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 537</a></span>.</p>
<p>To be sure, the majority acknowledges, in passing, the possibility of criminal prosecutions, <i>ante,</i> at 621, n. 5, but it refuses to factor this possibility into its Fourth Amendment balancing process, stating that "the record does not disclose that [<span class="citation no-link">49 CFR § 219.211</span>(d) (1987)] was intended to be, or actually has been, so used." <i><span class="citation no-link">Ibid.</span></i> This demurrer is highly disingenuous. The federal parties concede that they find "no prohibition on the release of FRA testing results to prosecutors." Brief for Federal Parties 10, n. 15. The absence of prosecutions to date  which is likely due to the fact that the FRA's regulations have been held invalid for much of their brief history  hardly proves that prosecutors will not avail themselves of the FRA's invitation in the future. If the majority really views the impact of FRA testing on privacy interests as minimal even if these tests generate criminal prosecutions, it should say so. If the prospect of prosecutions would lead the majority to reassess the validity of the testing program with prosecutions as part of the balance, it should say so, too, or condition its approval of that program on the nonrelease of test results to prosecutors. In ducking this important issue, the majority gravely disserves both the values served by the Fourth Amendment and the rights of those persons whom the FRA searches. Furthermore, the majority's refusal to restrict the release of test results casts considerable doubt on the conceptual basis of its decision  that the "special need" of railway safety is one "beyond the <span class="star-pagination">*652</span> normal need for law enforcement." <i>Ante,</i> at 619 (citations omitted).<sup>[10]</sup></p>
<p>The majority also overlooks needlessly intrusive aspects of the testing process itself. Although the FRA requires the collection and testing of both blood and urine, the agency concedes that mandatory urine tests  unlike blood tests  do not measure current impairment and therefore cannot differentiate on-duty impairment from prior drug or alcohol use which has ceased to affect the user's behavior. See <span class="citation no-link">49 CFR § 219.309</span>(2) (1987) (urine test may reveal use of drugs or alcohol as much as 60 days prior to sampling). Given that the FRA's stated goal is to ascertain current impairment, and not to identify persons who have used substances in their spare time sufficiently in advance of their railroad duties to pose no risk of on-duty impairment, § 219.101(a), mandatory urine testing seems wholly excessive. At the very least, the FRA could limit its use of urinalysis to confirming findings of current impairment suggested by a person's blood tests. The additional invasion caused by automatically testing urine as well as blood hardly ensures that privacy interests "will be invaded no more than is necessary." <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#343" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 343</a></span>.</p>
<p>The majority's trivialization of the intrusions on worker privacy posed by the FRA's testing program is matched at the other extreme by its blind acceptance of the Government's assertion that testing will "dete[r] employees engaged in safety-sensitive tasks from using controlled substances or alcohol," and "help railroads obtain invaluable information <span class="star-pagination">*653</span> about the causes of major accidents." <i>Ante,</i> at 629, 630. With respect, first, to deterrence, it is simply implausible that testing employees <i>after</i> major accidents occur, <span class="citation no-link">49 CFR § 219.201</span>(a)(1) (1987), will appreciably discourage them from using drugs or alcohol. As JUSTICE STEVENS observes in his concurring opinion:</p>
<blockquote>"Most people  and I would think most railroad employees as well  do not go to work with the expectation that they may be involved in a major accident, particularly one causing such catastrophic results as loss of life or the release of hazardous material requiring an evacuation. Moreover, even if they are conscious of the possibilities that such an accident might occur and that alcohol or drug use might be a contributing factor, if the risk of serious personal injury does not deter their use of these substances, it seems highly unlikely that the additional threat of loss of employment would have any effect on their behavior." <i>Ante,</i> at 634.</blockquote>
<p>Under the majority's deterrence rationale, people who skip school or work to spend a sunny day at the zoo will not taunt the lions because their truancy or absenteeism might be discovered in the event they are mauled. It is, of course, the fear of the accident, not the fear of a postaccident revelation, that deters. The majority's credulous acceptance of the FRA's deterrence rationale is made all the more suspect by the agency's failure to introduce, in an otherwise ample administrative record, <i>any</i> studies explaining or supporting its theory of accident deterrence.</p>
<p>The poverty of the majority's deterrence rationale leaves the Government's interest in diagnosing the causes of major accidents as the sole remaining justification for the FRA's testing program. I do not denigrate this interest, but it seems a slender thread from which to hang such an intrusive program, particularly given that the knowledge that one or more workers were impaired at the time of

[...TRUNCATED 32430 of 152430 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Smith v. Maryland.md  (`case`, 5 assertions)

### content_page

```
---
title: "Smith v. Maryland"
type: case
citation: "442 U.S. 735 (1979)"
parallel_cite: "99 S. Ct. 2577; 61 L. Ed. 2d 220"
neutral_cite: 1979 U.S. LEXIS 134
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-20
docket: 78-5374
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Smith v. Maryland
  varies_by_point: false
  scope_note: "Foundational third-party-doctrine case; remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Smith."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110118/smith-v-maryland/"
  cluster_id: 110118
  opinion_id: 110118
  identity_checked: true
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Key — Anchor"
related: ["[[United States v. Miller]]", "[[Carpenter v. United States]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "third-party-doctrine", "pen-register", "surveillance"]
holding: "No reasonable expectation of privacy in phone numbers voluntarily conveyed to the phone company; installing and using a pen register is not a Fourth Amendment search (third-party doctrine)."
lake:
  record_id: Smith v. Maryland
  status: verified
  projected_at: 2026-07-06
---

# Smith v. Maryland

*442 U.S. 735 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a robbery victim received threatening and obscene phone calls, police identified Smith as a suspect and, without a warrant, asked the telephone company to install a pen register at its central office to record the numbers dialed from Smith's home phone. The register showed a call placed to the victim. That information helped secure a search warrant for Smith's home, and he moved to suppress the fruits, arguing the pen register was an unconstitutional warrantless search.

## Issue
Whether the installation and use of a pen register — a device that records the telephone numbers dialed from a particular line — constitutes a "search" within the meaning of the Fourth Amendment.

## Rule
No. A caller has no legitimate expectation of privacy in the numbers he dials, because he voluntarily conveys them to the phone company. "This Court consistently has held that a person has no legitimate expectation of privacy in information he voluntarily turns over to third parties." — 442 U.S. at 743–744. ^pin-743

Applied to dialed numbers: "When he used his phone, petitioner voluntarily conveyed numerical information to the telephone company and 'exposed' that information to its equipment in the ordinary course of business. In so doing, petitioner assumed the risk that the company would reveal to police the numbers he dialed." — *Id.* at 744. ^pin-744

## Application
Smith voluntarily conveyed the numbers he dialed to the telephone company, whose switching equipment routed his calls and routinely recorded such numbers for billing and other legitimate business purposes. Having exposed that information to a third party, he assumed the risk it would be turned over to the government, so he had no legitimate expectation of privacy in it. The pen register therefore worked no Fourth Amendment search, and no warrant was required to install or use it.

## Conclusion
Installation and use of the pen register was not a search; the Fourth Amendment imposed no warrant requirement. With [[United States v. Miller]] (bank records), *Smith* is a foundation of the third-party doctrine the Court later confronted for digital cell-site data in [[Carpenter v. United States]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Smith* remains good law. [[Carpenter v. United States]] (2018) held the third-party doctrine does **not** extend to historical cell-site location information given its uniquely revealing, comprehensive nature, but **expressly declined to overrule** *Smith* or [[United States v. Miller]]; the pen-register/short-term-conveyance holding stands.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Key — Anchor*

## Sources
- *Smith v. Maryland*, 442 U.S. 735 (1979) — https://www.courtlistener.com/opinion/110118/smith-v-maryland/ — pinpoints: 743–744.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d4f36cea2ac052e5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "442 U.S. 735 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 134", "official_citation_present": true, "parallel_cite": "99 S. Ct. 2577; 61 L. Ed. 2d 220", "title": "Smith v. Maryland", "year": "1979"}}
{"assertion_id": "a363a26c7c5d3b33", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Key — Anchor", "title": "Smith v. Maryland"}}
{"assertion_id": "e5d1da30bd725b75", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "No reasonable expectation of privacy in phone numbers voluntarily conveyed to the phone company; installing and using a pen register is not a Fourth Amendment search (third-party doctrine).", "title": "Smith v. Maryland"}}
{"assertion_id": "1091e2093ff01e34", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-06-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Smith v. Maryland", "field_i_validity": "good_law", "scope_note": "Foundational third-party-doctrine case; remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Smith.", "title": "Smith v. Maryland", "varies_by_point": "false"}}
{"assertion_id": "5b31b17731dfe047", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Smith v. Maryland"}}
```

### lake record — Smith v. Maryland

```json
{
  "schema_version": "s2.v1",
  "record_id": "Smith v. Maryland",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Smith v. Maryland",
    "case_name_short": "",
    "case_name_full": "Smith v. Maryland",
    "input_case_name": "Smith v. Maryland",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-20",
    "year": 1979,
    "docket": "78-5374",
    "cluster_id": 110118,
    "lead_opinion_id": 110118,
    "sibling_ids": [
      110118,
      9427638,
      9427639,
      9427640
    ],
    "absolute_url": "/opinion/110118/smith-v-maryland/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "442 U.S. 735",
      "volume": "442",
      "reporter": "U.S.",
      "page": "735",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2577",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2577",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 220",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "220",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 134",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "134",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "442 U.S. 735",
        "volume": "442",
        "reporter": "U.S.",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2577",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2577",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 220",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "220",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 134",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "134",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "442 U.S. 735",
    "official_selection": {
      "court_class": "scotus",
      "selected": "442 U.S. 735",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-743",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule No. A caller has no legitimate expectation of privacy in the numbers he dials, because he voluntarily conveys them to the phone company.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-744",
      "page": null,
      "quote": "When he used his phone, petitioner voluntarily conveyed numerical information to the telephone company and 'exposed' that information to its equipment in the ordinary course of business. In so doing, petitioner assumed the risk that the company would reveal to police the numbers he dialed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Smith v. Maryland",
    "varies_by_point": false,
    "scope_note": "Foundational third-party-doctrine case; remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Smith.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Von Harris",
          "cluster_id": 10324088,
          "cite": [
            "2025 Ohio 279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Lepage",
          "cluster_id": 9503197,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hoffman",
          "cluster_id": 10135310,
          "cite": [
            "321 Or. App. 330",
            "515 P.3d 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ajemian v. Yahoo!, Inc.",
          "cluster_id": 4434746,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hudson v. Palmer",
          "cluster_id": 111252,
          "cite": [
            "82 L. Ed. 2d 393",
            "104 S. Ct. 3194",
            "468 U.S. 517",
            "1984 U.S. LEXIS 143",
            "52 U.S.L.W. 5052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Chadha",
          "cluster_id": 110985,
          "cite": [
            "77 L. Ed. 2d 317",
            "103 S. Ct. 2764",
            "462 U.S. 919",
            "1983 U.S. LEXIS 80",
            "51 U.S.L.W. 4907",
            "13 Envtl. L. Rep. (Envtl. Law Inst.) 20663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dunn",
          "cluster_id": 111833,
          "cite": [
            "94 L. Ed. 2d 326",
            "107 S. Ct. 1134",
            "480 U.S. 294",
            "1987 U.S. LEXIS 1057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knotts",
          "cluster_id": 110882,
          "cite": [
            "75 L. Ed. 2d 55",
            "103 S. Ct. 1081",
            "460 U.S. 276",
            "1983 U.S. LEXIS 135",
            "51 U.S.L.W. 4232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1762668,
          "cite": [
            "993 S.W.2d 103",
            "1999 Tex. Crim. App. LEXIS 53",
            "1999 WL 330266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. National Collegiate Athletic Assn.",
          "cluster_id": 1235436,
          "cite": [
            "865 P.2d 633",
            "7 Cal. 4th 1",
            "26 Cal. Rptr. 2d 834",
            "94 Cal. Daily Op. Serv. 681",
            "94 Daily Journal DAR 1141",
            "9 I.E.R. Cas. (BNA) 716",
            "1994 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110118 OR 9427638 OR 9427639 OR 9427640) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTA1ODY1NjAwMDAwJnM9NDQyNzcyNSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110118+OR+9427638+OR+9427639+OR+9427640%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110118 OR 9427638 OR 9427639 OR 9427640)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMTAmcz0xNjI1MDY5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110118+OR+9427638+OR+9427639+OR+9427640%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110118 OR 9427638 OR 9427639 OR 9427640)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 2,
        "triage_snippet_classified": 67
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110118 OR 9427638 OR 9427639 OR 9427640)",
    "indexed_citing_opinions": 1450,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110118,
        "count": 1224,
        "count_source": "search"
      },
      {
        "opinion_id": 9427638,
        "count": 267,
        "count_source": "search"
      },
      {
        "opinion_id": 9427639,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427640,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2307,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/smith-v-maryland.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyODU0OTMmcz0xMDM3MzQ1NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110118+OR+9427638+OR+9427639+OR+9427640%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110118,
        "cited_id": 105746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 324659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 337714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 345476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 1416762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 2073770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 2140967,
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
    "date_created": "2026-07-05T19:59:02Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:59:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:59:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:02:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:59:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Smith v. Maryland

```
<div>
<center><b><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U.S. 735</a></span> (1979)</b></center>
<center><h1>SMITH<br>
v.<br>
MARYLAND.</h1></center>
<center>No. 78-5374.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 28, 1979.</center>
<center>Decided June 20, 1979.</center>
CERTIORARI TO THE COURT OF APPEALS OF MARYLAND.
<p><span class="star-pagination">*736</span> <i>Howard L. Cardin</i> argued the cause for petitioner. With him on the brief was <i>James J. Gitomer.</i></p>
<p><i>Stephen H. Sachs,</i> Attorney General of Maryland, argued the cause for respondent. With him on the brief were <i>George A. Nilson,</i> Deputy Attorney General, and <i>Deborah K. Handel</i> and <i>Stephen B. Caplis,</i> Assistant Attorneys General.</p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents the question whether the installation and use of a pen register<sup>[1]</sup> constitutes a "search" within the meaning of the Fourth Amendment,<sup>[2]</sup> made applicable to the States through the Fourteenth Amendment. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
<p></p>
<h2>
<span class="star-pagination">*737</span> I</h2>
<p>On March 5, 1976, in Baltimore, Md., Patricia McDonough was robbed. She gave the police a description of the robber and of a 1975 Monte Carlo automobile she had observed near the scene of the crime. Tr. 66-68. After the robbery, McDonough began receiving threatening and obscene phone calls from a man identifying himself as the robber. On one occasion, the caller asked that she step out on her front porch; she did so, and saw the 1975 Monte Carlo she had earlier described to police moving slowly past her home. <i>Id.,</i> at 70. On March 16, police spotted a man who met McDonough's description driving a 1975 Monte Carlo in her neighborhood. <i>Id.,</i> at 71-72. By tracing the license plate number, police learned that the car was registered in the name of petitioner, Michael Lee Smith. <i>Id.,</i> at 72.</p>
<p>The next day, the telephone company, at police request, installed a pen register at its central offices to record the numbers dialed from the telephone at petitioner's home. <i>Id.,</i> at 73, 75. The police did not get a warrant or court order before having the pen register installed. The register revealed that on March 17 a call was placed from petitioner's home to McDonough's phone. <i>Id.,</i> at 74. On the basis of this and other evidence, the police obtained a warrant to search petitioner's residence. <i>Id.,</i> at 75. The search revealed that a page in petitioner's phone book was turned down to the name and number of Patricia McDonough; the phone book was seized. <i>Ibid.</i> Petitioner was arrested, and a six-man lineup was held on March 19. McDonough identified petitioner as the man who had robbed her. <i>Id.,</i> at 70-71.</p>
<p>Petitioner was indicted in the Criminal Court of Baltimore for robbery. By pretrial motion, he sought to suppress "all fruits derived from the pen register" on the ground that the police had failed to secure a warrant prior to its installation. Record 14; Tr. 54-56. The trial court denied the suppression motion, holding that the warrantless installation of the pen <span class="star-pagination">*738</span> register did not violate the Fourth Amendment. <i>Id.,</i> at 63. Petitioner then waived a jury, and the case was submitted to the court on an agreed statement of facts. <i>Id.,</i> at 65-66. The pen register tape (evidencing the fact that a phone call had been made from petitioner's phone to McDonough's phone) and the phone book seized in the search of petitioner's residence were admitted into evidence against him. <i>Id.,</i> at 74-76. Petitioner was convicted, <i>id.,</i> at 78, and was sentenced to six years. He appealed to the Maryland Court of Special Appeals, but the Court of Appeals of Maryland issued a writ of certiorari to the intermediate court in advance of its decision in order to consider whether the pen register evidence had been properly admitted at petitioner's trial. <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#160" aria-description="Citation for case: Smith v. State">283 Md. 156, 160</a></span>, <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#860" aria-description="Citation for case: Smith v. State">389 A. 2d 858, 860</a></span> (1978).</p>
<p>The Court of Appeals affirmed the judgment of conviction, holding that "there is no constitutionally protected reasonable expectation of privacy in the numbers dialed into a telephone system and hence no search within the fourth amendment is implicated by the use of a pen register installed at the central offices of the telephone company." <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#173" aria-description="Citation for case: Smith v. State"><i>Id.,</i> at 173</a></span>, <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#867" aria-description="Citation for case: Smith v. State">389 A. 2d, at 867</a></span>. Because there was no "search," the court concluded, no warrant was needed. Three judges dissented, expressing the view that individuals do have a legitimate expectation of privacy regarding the phone numbers they dial from their homes; that the installation of a pen register thus constitutes a "search"; and that, in the absence of exigent circumstances, the failure of police to secure a warrant mandated that the pen register evidence here be excluded. <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#174" aria-description="Citation for case: Smith v. State"><i>Id.,</i> at 174, 178</a></span>, <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#868" aria-description="Citation for case: Smith v. State">389 A. 2d, at 868, 870</a></span>. Certiorari was granted in order to resolve indications of conflict in the decided cases as to the restrictions imposed by the Fourth Amendment on the use of pen registers.<sup>[3]</sup> <span class="citation multiple-matches"><a href="/c/U.%20S./439/1001/">439 U. S. 1001</a></span> (1978).</p>
<p></p>
<h2>
<span class="star-pagination">*739</span> II</h2>
<p></p>
<h2>A</h2>
<p>The Fourth Amendment guarantees "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." In determining whether a particular form of government-initiated electronic surveillance is a "search" within the meaning of the Fourth Amendment,<sup>[4]</sup> our lodestar is <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). In <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> Government agents had intercepted the contents of a telephone conversation by attaching an electronic listening device to the outside of a public phone booth. The Court rejected the argument that a "search" can occur only when there has been a "physical intrusion" into a "constitutionally protected area," noting that the Fourth Amendment "protects people, not places." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 351-353</a></span>. Because the Government's monitoring of Katz' conversation "violated the privacy upon which he justifiably relied while using the telephone booth," the Court held that <span class="star-pagination">*740</span> it "constituted a `search and seizure' within the meaning of the Fourth Amendment." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353</a></span>.</p>
<p>Consistently with <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> this Court uniformly has held that the application of the Fourth Amendment depends on whether the person invoking its protection can claim a "justifiable," a "reasonable," or a "legitimate expectation of privacy" that has been invaded by government action. <i>E. g., </i><i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143</a></span>, and n. 12 (1978); <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#150" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 150, 151</a></span> (concurring opinion); <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#164" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 164</a></span> (dissenting opinion); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7</a></span> (1977); <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 442</a></span> (1976); <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#14" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 14</a></span> (1973); <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#335" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 335-336</a></span> (1973); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S. 745, 752</a></span> (1971) (plurality opinion); <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#368" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 368</a></span> (1968); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968). This inquiry, as Mr. Justice Harlan aptly noted in his <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> concurrence, normally embraces two discrete questions. The first is whether the individual, by his conduct, has "exhibited an actual (subjective) expectation of privacy," 389 U. S., at 361whether, in the words of the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> majority, the individual has shown that "he seeks to preserve [something] as private." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 351</a></span>. The second question is whether the individual's subjective expectation of privacy is "one that society is prepared to recognize as 'reasonable,'" <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">id.,</a></span></i> at 361 whether, in the words of the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> majority, the individual's expectation, viewed objectively, is "justifiable" under the circumstances. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353</a></span>.<sup>[5]</sup> See <i>Rakas</i> v. <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Illinois</a></span>,</i> 439 U. S., <span class="star-pagination">*741</span> at 143-144, n. 12; <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#151" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 151</a></span> (concurring opinion); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S., at 752</a></span> (plurality opinion).</p>
<p></p>
<h2>B</h2>
<p>In applying the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> analysis to this case, it is important to begin by specifying precisely the nature of the state activity that is challenged. The activity here took the form of installing and using a pen register. Since the pen register was installed on telephone company property at the telephone company's central offices, petitioner obviously cannot claim that his "property"' was invaded or that police intruded into a "constitutionally protected area." Petitioner's claim, rather, is that, notwithstanding the absence of a trespass, the State, as did the Government in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> infringed a "legitimate expectation of privacy" that petitioner held. Yet a pen register differs significantly from the listening device employed in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> for pen registers do not acquire the <i>contents</i> of communications. This Court recently noted:</p>
<blockquote>"Indeed, a law enforcement official could not even determine from the use of a pen register whether a communication existed. These devices do not hear sound. They disclose only the telephone numbers that have been dialeda means of establishing communication. Neither the purport of any communication between the caller and the recipient of the call, their identities, nor whether the call was even completed is disclosed by pen registers." <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#167" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159, 167</a></span> (1977).</blockquote>
<p><span class="star-pagination">*742</span> Given a pen register's limited capabilities, therefore, petitioner's argument that its installation and use constituted a "search" necessarily rests upon a claim that he had a "legitimate expectation of privacy" regarding the numbers he dialed on his phone.</p>
<p>This claim must be rejected. First, we doubt that people in general entertain any actual expectation of privacy in the numbers they dial. All telephone users realize that they must "convey" phone numbers to the telephone company, since it is through telephone company switching equipment that their calls are completed. All subscribers realize, moreover, that the phone company has facilities for making permanent records of the numbers they dial, for they see a list of their long-distance (toll) calls on their monthly bills. In fact, pen registers and similar devices are routinely used by telephone companies "for the purposes of checking billing operations, detecting fraud, and preventing violations of law." <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#174" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 174-175</a></span>. Electronic equipment is used not only to keep billing records of toll calls, but also "to keep a record of all calls dialed from a telephone which is subject to a special rate structure." <i>Hodge</i> v. <i>Mountain States Tel. &amp; Tel. Co.,</i> <span class="citation" data-id="9463842"><a href="/opinion/345476/james-l-hodge-v-the-mountain-states-telephone-and-telegraph-company-a/#266" aria-description="Citation for case: James L. Hodge v. The Mountain States Telephone and...">555 F. 2d 254, 266</a></span> (CA9 1977) (concurring opinion). Pen registers are regularly employed "to determine whether a home phone is being used to conduct a business, to check for a defective dial, or to check for overbilling." Note, The Legal Constraints upon the Use of the Pen Register as a Law Enforcement Tool, <span class="citation no-link">60 Cornell L. Rev. 1028</span>, 1029 (1975) (footnotes omitted). Although most people may be oblivious to a pen register's esoteric functions, they presumably have some awareness of one common use: to aid in the identification of persons making annoying or obscene calls. See, <i>e. g., </i><i>Von Lusch</i> v. <i>C &amp; P Telephone Co.,</i> <span class="citation" data-id="2347338"><a href="/opinion/2347338/von-lusch-v-c-p-telephone-co/#816" aria-description="Citation for case: Von Lusch v. C &amp; P Telephone Co.">457 F. Supp. 814, 816</a></span> (Md. 1978); Note, 60 Cornell L. Rev., at 1029-1030, n. 11; Claerhout, The Pen Register, <span class="citation no-link">20 Drake L. Rev. 108</span>, 110-111 (1970). Most phone books tell <span class="star-pagination">*743</span> subscribers, on a page entitled "Consumer Information," that the company "can frequently help in identifying to the authorities the origin of unwelcome and troublesome calls." <i>E. g.,</i> Baltimore Telephone Directory 21 (1978); District of Columbia Telephone Directory 13 (1978). Telephone users, in sum, typically know that they must convey numerical information to the phone company; that the phone company has facilities for recording this information; and that the phone company does in fact record this information for a variety of legitimate business purposes. Although subjective expectations cannot be scientifically gauged, it is too much to believe that telephone subscribers, under these circumstances, harbor any general expectation that the numbers they dial will remain secret.</p>
<p>Petitioner argues, however, that, whatever the expectations of telephone users in general, he demonstrated an expectation of privacy by his own conduct here, since he "us[ed] the telephone <i>in his house</i> to the exclusion of all others." Brief for Petitioner 6 (emphasis added). But the site of the call is immaterial for purposes of analysis in this case. Although petitioner's conduct may have been calculated to keep the <i>contents</i> of his conversation private, his conduct was not and could not have been calculated to preserve the privacy of the number he dialed. Regardless of his location, petitioner had to convey that number to the telephone company in precisely the same way if he wished to complete his call. The fact that he dialed the number on his home phone rather than on some other phone could make no conceivable difference, nor could any subscriber rationally think that it would.</p>
<p>Second, even if petitioner did harbor some subjective expectation that the phone numbers he dialed would remain private, this expectation is not "one that society is prepared to recognize as 'reasonable.'" <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span>. This Court consistently has held that a person has no legitimate expectation of privacy in information he <span class="star-pagination">*744</span> voluntarily turns over to third parties. <i>E. g., </i><i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller">425 U. S., at 442-444</a></span>; <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#335" aria-description="Citation for case: Couch v. United States">409 U. S., at 335-336</a></span>; <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S., at 752</a></span> (plurality opinion); <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#302" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 302</a></span> (1966); <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span> (1963). In <i><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span>,</i> for example, the Court held that a bank depositor has no "legitimate `expectation of privacy'" in financial information "voluntarily conveyed to . . . banks and exposed to their employees in the ordinary course of business." <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller">425 U. S., at 442</a></span>. The Court explained:</p>
<blockquote>"The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government. . . . This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed." <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#443" aria-description="Citation for case: United States v. Miller"><i>Id.,</i> at 443</a></span>.</blockquote>
<p>Because the depositor "assumed the risk" of disclosure, the Court held that it would be unreasonable for him to expect his financial records to remain private.</p>
<p>This analysis dictates that petitioner can claim no legitimate expectation of privacy here. When he used his phone, petitioner voluntarily conveyed numerical information to the telephone company and "exposed" that information to its equipment in the ordinary course of business. In so doing, petitioner assumed the risk that the company would reveal to police the numbers he dialed. The switching equipment that processed those numbers is merely the modern counterpart of the operator who, in an earlier day, personally completed calls for the subscriber. Petitioner concedes that if he had placed his calls through an operator, he could claim no legitimate expectation of privacy. Tr. of Oral Arg. 3-5, 11-12, 32. We <span class="star-pagination">*745</span> are not inclined to hold that a different constitutional result is required because the telephone company has decided to automate.</p>
<p>Petitioner argues, however, that automatic switching equipment differs from a live operator in one pertinent respect. An operator, in theory at least, is capable of remembering every number that is conveyed to him by callers. Electronic equipment, by contrast, can "remember" only those numbers it is programmed to record, and telephone companies, in view of their present billing practices, usually do not record local calls. Since petitioner, in calling McDonough, was making a local call, his expectation of privacy as to her number, on this theory, would be "legitimate."</p>
<p>This argument does not withstand scrutiny. The fortuity of whether or not the phone company in fact elects to make a quasi-permanent record of a particular number dialed does not, in our view, make any constitutional difference. Regardless of the phone company's election, petitioner voluntarily conveyed to it information that it had facilities for recording and that it was free to record. In these circumstances, petitioner assumed the risk that the information would be divulged to police. Under petitioner's theory, Fourth Amendment protection would exist, or not, depending on how the telephone company chose to define local-dialing zones, and depending on how it chose to bill its customers for local calls. Calls placed across town, or dialed directly, would be protected; calls placed across the river, or dialed with operator assistance, might not be. We are not inclined to make a crazy quilt of the Fourth Amendment, especially in circumstances where (as here) the pattern of protection would be dictated by billing practices of a private corporation.</p>
<p>We therefore conclude that petitioner in all probability entertained no actual expectation of privacy in the phone numbers he dialed, and that, even if he did, his expectation was not "legitimate." The installation and use of a pen register, <span class="star-pagination">*746</span> consequently, was not a "search," and no warrant was required. The judgment of the Maryland Court of Appeals is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>Mr. JUSTICE POWELL took no part in the consideration or decision of this case.</p>
<p>Mr. JUSTICE STEWART, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>I am not persuaded that the numbers dialed from a private telephone fall outside the constitutional protection of the Fourth and Fourteenth Amendments.</p>
<p>In <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352</a></span>, the Court acknowledged the "vital role that the public telephone has come to play in private communication[s]." The role played by a private telephone is even more vital, and since <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> it has been abundantly clear that telephone conversations carried on by people in their homes or offices are fully protected by the Fourth and Fourteenth Amendments. As the Court said in <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span>, "the broad and unsuspected governmental incursions into conversational privacy which electronic surveillance entails necessitate the application of Fourth Amendment safeguards." (Footnote omitted.)</p>
<p>Nevertheless, the Court today says that those safeguards do not extend to the numbers dialed from a private telephone, apparently because when a caller dials a number the digits may be recorded by the telephone company for billing purposes. But that observation no more than describes the basic nature of telephone calls. A telephone call simply cannot be made without the use of telephone company property and without payment to the company for the service. The telephone conversation itself must be electronically transmitted by telephone company equipment, and may be recorded or overheard by the use of other company equipment. Yet we <span class="star-pagination">*747</span> have squarely held that the user of even a public telephone is entitled "to assume that the words he utters into the mouthpiece will not be broadcast to the world." <i>Katz</i> v. <i>United States, supra,</i> at 352.</p>
<p>The central question in this case is whether a person who makes telephone calls from his home is entitled to make a similar assumption about the numbers he dials. What the telephone company does or might do with those numbers is no more relevant to this inquiry than it would be in a case involving the conversation itself. It is simply not enough to say, after <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> that there is no legitimate expectation of privacy in the numbers dialed because the caller assumes the risk that the telephone company will disclose them to the police.</p>
<p>I think that the numbers dialed from a private telephone like the conversations that occur during a callare within the constitutional protection recognized in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>.</i><sup>[1]</sup> It seems clear to me that information obtained by pen register surveillance of a private telephone is information in which the telephone subscriber has a legitimate expectation of privacy.<sup>[2]</sup> The information captured by such surveillance emanates from private conduct within a person's home or officelocations that without question are entitled to Fourth and Fourteenth Amendment protection. Further, that information is an integral part of the telephonic communication that under <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> <span class="star-pagination">*748</span> is entitled to constitutional protection, whether or not it is captured by a trespass into such an area.</p>
<p>The numbers dialed from a private telephonealthough certainly more prosaic than the conversation itselfare not without "content." Most private telephone subscribers may have their own numbers listed in a publicly distributed directory, but I doubt there are any who would be happy to have broadcast to the world a list of the local or long distance numbers they have called. This is not because such a list might in some sense be incriminating, but because it easily could reveal the identities of the persons and the places called, and thus reveal the most intimate details of a person's life.</p>
<p>I respectfully dissent.</p>
<p>Mr. JUSTICE MARSHALL, with whom Mr. JUSTICE BRENNAN joins, dissenting.</p>
<p>The Court concludes that because individuals have no actual or legitimate expectation of privacy in information they voluntarily relinquish to telephone companies, the use of pen registers by government agents is immune from Fourth Amendment scrutiny. Since I remain convinced that constitutional protections are not abrogated whenever a person apprises another of facts valuable in criminal investigations, see, <i>e. g., </i><i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#786" aria-description="Citation for case: United States v. White">401 U. S. 745, 786-790</a></span> (1971) (Harlan, J., dissenting); <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#795" aria-description="Citation for case: United States v. White"><i>id.,</i> at 795-796</a></span> (MARSHALL, J., dissenting); <i>California Bankers Assn.</i> v. <i>Shultz,</i> <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#95" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 95-96</a></span> (1974) (MARSHALL, J., dissenting); <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#455" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 455-456</a></span> (1976) (MARSHALL, J., dissenting), I respectfully dissent.</p>
<p>Applying the standards set forth in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring), the Court first determines that telephone subscribers have no subjective expectations of privacy concerning the numbers they dial. To reach this conclusion, the Court posits that individuals somehow infer from the long-distance listings on their phone bills, and from the cryptic assurances of "help" in tracing obscene <span class="star-pagination">*749</span> calls included in "most" phone books, that pen registers are regularly used for recording local calls. See <i>ante,</i> at 742-743. But even assuming, as I do not, that individuals "typically know" that a phone company monitors calls for internal reasons, <i>ante,</i> at 743,<sup>[1]</sup> it does not follow that they expect this information to be made available to the public in general or the government in particular. Privacy is not a discrete commodity, possessed absolutely or not at all. Those who disclose certain facts to a bank or phone company for a limited business purpose need not assume that this information will be released to other persons for other purposes. See <i>California Bankers Assn.</i> v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#95" aria-description="Citation for case: California Bankers Assn. v. Shultz"><i>Shultz, supra,</i> at 95-96</a></span> (MARSHALL, J., dissenting).</p>
<p>The crux of the Court's holding, however, is that whatever expectation of privacy petitioner may in fact have entertained regarding his calls, it is not one "society is prepared to recognize as `reasonable.'" <i>Ante,</i> at 743. In so ruling, the Court determines that individuals who convey information to third parties have "assumed the risk" of disclosure to the government. <i>Ante,</i> at 744, 745. This analysis is misconceived in two critical respects.</p>
<p>Implicit in the concept of assumption of risk is some notion of choice. At least in the third-party consensual surveillance cases, which first incorporated risk analysis into Fourth Amendment doctrine, the defendant presumably had exercised some discretion in deciding who should enjoy his confidential communications. See, <i>e. g., </i><i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#439" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 439</a></span> (1963); <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#302" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 302-303</a></span> (1966); <i>United States</i> v. <i><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">White, supra,</a></span></i> at 751-752 <span class="star-pagination">*750</span> (plurality opinion). By contrast here, unless a person is prepared to forgo use of what for many has become a personal or professional necessity, he cannot help but accept the risk of surveillance. Cf. <i>Lopez</i> v. <i>United States, supra,</i> at 465-466 (BRENNAN, J., dissenting). It is idle to speak of "assuming" risks in contexts where, as a practical mater, individuals have no realistic alternative.</p>
<p>More fundamentally, to make risk analysis dispositive in assessing the reasonableness of privacy expectations would allow the government to define the scope of Fourth Amendment protections. For example, law enforcement officials, simply by announcing their intent to monitor the content of random samples of first-class mail or private phone conversations, could put the public on notice of the risks they would thereafter assume in such communications. See Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 384, 407 (1974). Yet, although acknowledging this implication of its analysis, the Court is willing to concede only that, in some circumstances, a further "normative inquiry would be proper." <i>Ante,</i> at 740-741, n. 5. No meaningful effort is made to explain what those circumstances might be, or why this case is not among them.</p>
<p>In my view, whether privacy expectations are legitimate within the meaning of <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> depends not on the risks an individual can be presumed to accept when imparting information to third parties, but on the risks he should be forced to assume in a free and open society. By its terms, the constitutional prohibition of unreasonable searches and seizures assigns to the judiciary some prescriptive responsibility. As Mr. Justice Harlan, who formulated the standard the Court applies today, himself recognized: "[s]ince it is the task of the law to form and project, as well as mirror and reflect, we should not . . . merely recite . . . risks without examining the desirability of saddling them upon society." <i>United States</i> v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#786" aria-description="Citation for case: United States v. White"><i>White, supra,</i> at 786</a></span> (dissenting opinion). In making this <span class="star-pagination">*751</span> assessment, courts must evaluate the "intrinsic character" of investigative practices with reference to the basic values underlying the Fourth Amendment. <i>California Bankers Assn.</i> v. <i>Shultz,</i> <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#95" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S., at 95</a></span> (MARSHALL, J., dissenting). And for those "extensive intrusions that significantly jeopardize [individuals'] sense of security . . . , more than self-restraint by law enforcement officials is required." <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#786" aria-description="Citation for case: United States v. White">401 U. S., at 786</a></span> (Harlan, J., dissenting).</p>
<p>The use of pen registers, I believe, constitutes such an extensive intrusion. To hold otherwise ignores the vital role telephonic communication plays in our personal and professional relationships, see <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S., at 352</a></span>, as well as the First and Fourth Amendment interests implicated by unfettered official surveillance. Privacy in placing calls is of value not only to those engaged in criminal activity. The prospect of unregulated governmental monitoring will undoubtedly prove disturbing even to those with nothing illicit to hide. Many individuals, including members of unpopular political organizations or journalists with confidential sources, may legitimately wish to avoid disclosure of their personal contacts. See <i>NAACP</i> v. <i>Alabama,</i> <span class="citation" data-id="105746"><a href="/opinion/105746/national-assn-for-the-advancement-of-colored-people-v-alabama-ex-rel/#463" aria-description="Citation for case: National Ass&#x27;n for the Advancement of Colored People v....">357 U. S. 449, 463</a></span> (1958); <i>Branzburg</i> v. <i>Hayes,</i> <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#695" aria-description="Citation for case: Branzburg v. Hayes">408 U. S. 665, 695</a></span> (1972); <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#728" aria-description="Citation for case: Branzburg v. Hayes"><i>id.,</i> at 728-734</a></span> (STEWART, J., dissenting). Permitting governmental access to telephone records on less than probable cause may thus impede certain forms of political affiliation and journalistic endeavor that are the hallmark of a truly free society. Particularly given the Government's previous reliance on warrantless telephonic surveillance to trace reporters' sources and monitor protected political activity,<sup>[2]</sup> I am unwilling to insulate use of pen registers from independent judicial review.</p>
<p><span class="star-pagination">*752</span> Just as one who enters a public telephone booth is "entitled to assume that the words he utters into the mouthpiece will not be broadcast to the world," <i>Katz</i> v. <i>United States, supra,</i> at 352, so too, he should be entitled to assume that the numbers he dials in the privacy of his home will be recorded, if at all, solely for the phone company's business purposes. Accordingly, I would require law enforcement officials to obtain a warrant before they enlist telephone companies to secure information otherwise beyond the government's reach.</p>
<h2>NOTES</h2>
<p>[1]  "A pen register is a mechanical device that records the numbers dialed on a telephone by monitoring the electrical impulses caused when the dial on the telephone is released. It does not overhear oral communications and does not indicate whether calls are actually completed." <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159</a></span>, 161 n. 1 (1977). A pen register is "usually installed at a central telephone facility [and] records on a paper tape all numbers dialed from [the] line" to which it is attached. <i>United States</i> v. <i>Giordano,</i> <span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">416 U. S. 505</a></span>, 549 n. 1 (1974) (opinion concurring in part and dissenting in part). See also <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#162" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 162</a></span>.</p>
<p>[2]  "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." U. S. Const., Amdt. 4.</p>
<p>[3]  See <i>Application of United States for Order,</i> <span class="citation" data-id="8900411"><a href="/opinion/8912555/united-states-v-southwestern-bell-telephone-co/#245" aria-description="Citation for case: United States v. Southwestern Bell Telephone Co.">546 F. 2d 243, 245</a></span> (CA8 1976), cert. denied <i>sub nom. </i><i>Southwestern Bell Tel. Co.</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./434/1008/">434 U. S. 1008</a></span> (1978); <i>Application of United States in Matter of Order,</i> <span class="citation" data-id="9462905"><a href="/opinion/337714/application-of-the-united-states-of-america-in-the-matter-of-an-order/#959" aria-description="Citation for case: Application of the United States of America in the Matter...">538 F. 2d 956, 959-960</a></span> (CA2 1976), rev'd on other grounds <i>sub nom. </i><i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159</a></span> (1977); <i>United States</i> v. <i>Falcone,</i> <span class="citation" data-id="9461166"><a href="/opinion/322631/united-states-v-pasquale-falcone-appeal-of-pasquale-falconio-in-no/#482" aria-description="Citation for case: United States v. Pasquale Falcone Appeal of Pasquale...">505 F. 2d 478, 482</a></span>, and n. 21 (CA3 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/955/">420 U. S. 955</a></span> (1975); <i>Hodge</i> v. <i>Mountain States Tel. &amp; Tel. Co.,</i> <span class="citation" data-id="9463842"><a href="/opinion/345476/james-l-hodge-v-the-mountain-states-telephone-and-telegraph-company-a/#256" aria-description="Citation for case: James L. Hodge v. The Mountain States Telephone and...">555 F. 2d 254, 256</a></span> (CA9 1977); <span class="citation" data-id="9463842"><a href="/opinion/345476/james-l-hodge-v-the-mountain-states-telephone-and-telegraph-company-a/#266" aria-description="Citation for case: James L. Hodge v. The Mountain States Telephone and..."><i>id.,</i> at 266</a></span> (concurring opinion); and <i>United States</i> v. <i>Clegg,</i> <span class="citation" data-id="324659"><a href="/opinion/324659/united-states-v-michael-william-clegg/#610" aria-description="Citation for case: United States v. Michael William Clegg">509 F. 2d 605, 610</a></span> (CA5 1975). In previous decisions, this Court has not found it necessary to consider whether "pen register surveillance [is] subject to the requirements of the Fourth Amendment." <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 165</a></span> n. 7. See <i>United States</i> v. <i>Giordano,</i> <span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">416 U. S., at 554</a></span> n. 4 (opinion concurring in part and dissenting in part).</p>
<p>[4]  In this case, the pen register was installed, and the numbers dialed were recorded, by the telephone company. Tr. 73-74. The telephone company, however, acted at police request. <i>Id.,</i> at 73, 75. In view of this, respondent appears to concede that the company is to be deemed an "agent" of the police for purposes of this case, so as to render the installation and use of the pen register "state action" under the Fourth and Fourteenth Amendments. We may assume that "state action" was present here.</p>
<p>[5]  Situations can be imagined, of course, in which <i>Katz'</i> two-pronged inquiry would provide an inadequate index of Fourth Amendment protection. For example, if the Government were suddenly to announce on nationwide television that all homes henceforth would be subject to warrantless entry, individuals thereafter might not in fact entertain any actual expectation of privacy regarding their homes, papers, and effects. Similarly, if a refugee from a totalitarian country, unaware of this Nation's traditions, erroneously assumed that police were continuously monitoring his telephone conversations, a subjective expectation of privacy regarding the contents of his calls might be lacking as well. In such circumstances, where an individual's subjective expectations had been "conditioned" by influences alien to well-recognized Fourth Amendment freedoms, those subjective expectations obviously could play no meaningful role in ascertaining what the scope of Fourth Amendment protection was. In determining whether a "legitimate expectation of privacy" existed in such cases, a normative inquiry would be proper.</p>
<p>[1]  It is true, as the Court pointed out in <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#166" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159, 166-167</a></span>, that under Title III of the Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">18 U. S. C. §§ 2510-2520</span>, pen registers are not considered "interceptions" because "they do not acquire the `contents' of communications," as that term is defined by Congress. We are concerned in this case, however, not with the technical definitions of a statute, but with the requirements of the Constitution.</p>
<p>[2]  The question whether a defendant who is not a member of the subscriber's household has "standing" to object to pen register surveillance of a private telephone is, of course, distinct. Cf. <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span>.</p>
<p>[1]  Lacking the Court's apparently exhaustive knowledge of this Nation's telephone books and the reading habits of telephone subscribers, see <i>ante,</i> at 742-743, I decline to assume general public awareness of how obscene phone calls are traced. Nor am I persuaded that the scope of Fourth Amendment protection should turn on the concededly "esoteric functions" of pen registers in corporate billing, <i>ante,</i> at 742, functions with which subscribers are unlikely to have intimate familiarity.</p>
<p>[2]  See, <i>e. g., </i><i>Reporters Committee For Freedom of Press</i> v. <i>American Tel. &amp; Tel. Co.,</i> 192 U. S. App. D. C. 376, <span class="citation" data-id="9465568"><a href="/opinion/363949/reporters-committee-for-freedom-of-the-press-v-american-telephone/" aria-description="Citation for case: Reporters Committee for Freedom of the Press v. American...">593 F. 2d 1030</a></span> (1978), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./440/949/">440 U. S. 949</a></span> (1979); <i>Halperin</i> v. <i>Kissinger,</i> <span class="citation" data-id="1416762"><a href="/opinion/1416762/halperin-v-kissinger/" aria-description="Citation for case: Halperin v. Kissinger">434 F. Supp. 1193</a></span> (DC 1977); <i>Socialist Workers Party</i> v. <i>Attorney General,</i> <span class="citation" data-id="2140967"><a href="/opinion/2140967/socialist-workers-party-v-attorney-general-of-the-united-states/" aria-description="Citation for case: Socialist Workers Party v. Attorney General of the United...">463 F. Supp. 515</a></span> (SDNY 1978).</p>

</div>
```

---

## GROUP: content/cases/Soldal v. Cook County.md  (`case`, 7 assertions)

### content_page

```
---
title: "Soldal v. Cook County"
type: case
citation: ""
parallel_cite: "506 U.S. 56; 113 S. Ct. 538; 121 L. Ed. 2d 450; 92 Daily Journal DAR 16378; 61 U.S.L.W. 4019; 6 Fla. L. Weekly Fed. S 769"
neutral_cite: "1992 U.S. LEXIS 7835; 92 Cal. Daily Op. Serv. 9794"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1992
date_decided: 1992-12-08
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1992-12-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Soldal v. Cook County
  varies_by_point: false
  scope_note: "Good law; the holding that the Fourth Amendment protects possessory interests independent of privacy and liberty remains controlling."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112795/soldal-v-cook-county/"
  cluster_id: 112795
  opinion_id: 112795
  identity_checked: true
homes:
  - page: "[[Seizure of Property]]"
    role: "Key — Anchor (seizure of property)"
  - page: "[[Trespass]]"
    role: "Related (cross-doctrine)"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Jacobsen]]", "[[Horton v. California]]", "[[Oliver v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "possessory-interest", "property", "section-1983"]
holding: "A 'seizure' of property occurs whenever there is meaningful interference with possessory interests; the Fourth Amendment protects property interests independent of privacy or liberty."
lake:
  record_id: Soldal v. Cook County
  status: verified
  projected_at: 2026-07-09
---

# Soldal v. Cook County

*506 U.S. 56 (1992)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A trailer-park owner, without an eviction order, forcibly towed the Soldals' mobile home off its lot two weeks before the scheduled eviction hearing. Cook County sheriff's deputies stood by to prevent Soldal from interfering and declined to take his trespass complaint, knowing the eviction was unlawful. Soldal sued under § 1983, claiming an unreasonable seizure. The Seventh Circuit held there was no Fourth Amendment "seizure" because only possessory (not privacy or liberty) interests were affected.

## Issue
Whether a meaningful interference with a person's possessory interest in property — here, the towing of a home — is a "seizure" under the Fourth Amendment even though no privacy or liberty interest was invaded.

## Rule
Yes. "A 'seizure' of property, we have explained, occurs when 'there is some meaningful interference with an individual's possessory interests in that property.'" — 506 U.S. at 61 (quoting [[United States v. Jacobsen]]). ^pin-61

The Fourth Amendment is not limited to privacy: "our cases unmistakably hold that the Amendment protects property as well as privacy." — [*Id.* at 62](https://www.courtlistener.com/opinion/112795/soldal-v-cook-county/#:~:text=our%20cases%20unmistakably%20hold%20that). ^pin-62

## Application
The deputies' participation in physically wrenching the Soldals' trailer from its moorings and towing it away was a quintessential meaningful interference with the family's possessory interest — indeed, the home "literally was carried away." That the action invaded no privacy or liberty interest did not remove it from the Fourth Amendment, because the Amendment independently protects possessory interests in "effects" and "houses." The seizure therefore had to be reasonable, a question [[Reading and Citing Cases#on-remand|remanded]] for resolution.

## Conclusion
The towing of the Soldals' home was a Fourth Amendment seizure; the Seventh Circuit's contrary holding was reversed. *Soldal* establishes that property seizures are governed by the Fourth Amendment whether or not any privacy or liberty interest is also implicated.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Applies the seizure definition of [[United States v. Jacobsen]] to possessory interests and complements the plain-view seizure analysis of [[Horton v. California]]; the Court cautioned the Amendment does not protect possessory interests in *all* property (cf. [[Oliver v. United States]], open fields).

## Appears on
- [[Trespass]] — *Key — Anchor (seizure of property)*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Soldal v. Cook County*, 506 U.S. 56 (1992) — https://www.courtlistener.com/opinion/112795/soldal-v-cook-county/ — pinpoints: 61, 62.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "715404f38868d24c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "1992 U.S. LEXIS 7835; 92 Cal. Daily Op. Serv. 9794", "official_citation_present": false, "parallel_cite": "506 U.S. 56; 113 S. Ct. 538; 121 L. Ed. 2d 450; 92 Daily Journal DAR 16378; 61 U.S.L.W. 4019; 6 Fla. L. Weekly Fed. S 769", "title": "Soldal v. Cook County", "year": "1992"}}
{"assertion_id": "7ae4c56dc58e29a4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A 'seizure' of property occurs whenever there is meaningful interference with possessory interests; the Fourth Amendment protects property interests independent of privacy or liberty.", "title": "Soldal v. Cook County"}}
{"assertion_id": "9bafc61cc36a307e", "dimension": "support", "kind": "home_role", "locator": {"home": "Trespass"}, "payload": {"home": "Trespass", "role": "Related (cross-doctrine)", "title": "Soldal v. Cook County"}}
{"assertion_id": "d5ad74d939e8553d", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Related (cross-doctrine)", "title": "Soldal v. Cook County"}}
{"assertion_id": "fceab006d65c8d72", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of Property"}, "payload": {"home": "Seizure of Property", "role": "Key — Anchor (seizure of property)", "title": "Soldal v. Cook County"}}
{"assertion_id": "a258bf9a4734bec2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1992-12-08", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Soldal v. Cook County", "field_i_validity": "good_law", "scope_note": "Good law; the holding that the Fourth Amendment protects possessory interests independent of privacy and liberty remains controlling.", "title": "Soldal v. Cook County", "varies_by_point": "false"}}
{"assertion_id": "bf823f51f976659d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Soldal v. Cook County"}}
```

### lake record — Soldal v. Cook County

```json
{
  "schema_version": "s2.v1",
  "record_id": "Soldal v. Cook County",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Soldal v. Cook County",
    "case_name_short": "Soldal",
    "case_name_full": "SOLDAL Et Ux. v. COOK COUNTY, ILLINOIS, Et Al.",
    "input_case_name": "Soldal v. Cook County",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1992-12-08",
    "year": 1992,
    "docket": null,
    "cluster_id": 112795,
    "lead_opinion_id": 112795,
    "sibling_ids": [
      112795
    ],
    "absolute_url": "/opinion/112795/soldal-v-cook-county/",
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
        "cite": "506 U.S. 56",
        "volume": "506",
        "reporter": "U.S.",
        "page": "56",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 538",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "538",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 L. Ed. 2d 450",
        "volume": "121",
        "reporter": "L. Ed. 2d",
        "page": "450",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 Daily Journal DAR 16378",
        "volume": "92",
        "reporter": "Daily Journal DAR",
        "page": "16378",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 U.S.L.W. 4019",
        "volume": "61",
        "reporter": "U.S.L.W.",
        "page": "4019",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 Fla. L. Weekly Fed. S 769",
        "volume": "6",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1992 U.S. LEXIS 7835",
        "volume": "1992",
        "reporter": "U.S. LEXIS",
        "page": "7835",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 Cal. Daily Op. Serv. 9794",
        "volume": "92",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9794",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "506 U.S. 56",
        "volume": "506",
        "reporter": "U.S.",
        "page": "56",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 538",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "538",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 L. Ed. 2d 450",
        "volume": "121",
        "reporter": "L. Ed. 2d",
        "page": "450",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 U.S. LEXIS 7835",
        "volume": "1992",
        "reporter": "U.S. LEXIS",
        "page": "7835",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 Daily Journal DAR 16378",
        "volume": "92",
        "reporter": "Daily Journal DAR",
        "page": "16378",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 U.S.L.W. 4019",
        "volume": "61",
        "reporter": "U.S.L.W.",
        "page": "4019",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 Fla. L. Weekly Fed. S 769",
        "volume": "6",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 Cal. Daily Op. Serv. 9794",
        "volume": "92",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9794",
        "type": 6,
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
      "id": "pin-61",
      "page": null,
      "quote": "under the Fourth Amendment even though no privacy or liberty interest was invaded. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-62",
      "page": null,
      "quote": "our cases unmistakably hold that the Amendment protects property as well as privacy.",
      "star_marker": "62",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10477,
      "fragment": "#:~:text=our%20cases%20unmistakably%20hold%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1992-12-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Soldal v. Cook County",
    "varies_by_point": false,
    "scope_note": "Good law; the holding that the Fourth Amendment protects possessory interests independent of privacy and liberty remains controlling.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
      },
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
        "journal_ref": "Soldal v. Cook County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Sullivan",
          "cluster_id": 2821420,
          "cite": [
            "797 F.3d 623",
            "2015 U.S. App. LEXIS 13702",
            "2015 WL 4547498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tony Lavan v. City of Los Angeles",
          "cluster_id": 807915,
          "cite": [
            "693 F.3d 1022",
            "2012 WL 3834659",
            "2012 U.S. App. LEXIS 18639"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Poteet v. Sullivan",
          "cluster_id": 2332316,
          "cite": [
            "218 S.W.3d 780",
            "2007 WL 289871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Daniel Good Real Property",
          "cluster_id": 112914,
          "cite": [
            "126 L. Ed. 2d 490",
            "114 S. Ct. 492",
            "510 U.S. 43",
            "1993 U.S. LEXIS 7941",
            "7 Fla. L. Weekly Fed. S 665",
            "93 Daily Journal DAR 15706",
            "93 Cal. Daily Op. Serv. 9143",
            "62 U.S.L.W. 4013",
            "1993 WL 505539"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Edward Hoefling, Jr. v. City of Miami",
          "cluster_id": 3171918,
          "cite": [
            "811 F.3d 1271",
            "93 Fed. R. Serv. 3d 1022",
            "2016 U.S. App. LEXIS 1177",
            "2016 WL 285358"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Outboard Marine Corp.",
          "cluster_id": 762789,
          "cite": [
            "172 F.3d 531",
            "1999 U.S. App. LEXIS 5444",
            "1999 WL 164061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byron Halsey v. Frank Pfeiffer",
          "cluster_id": 2671183,
          "cite": [
            "750 F.3d 273",
            "2014 WL 1622769",
            "2014 U.S. App. LEXIS 7696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Geoffrey M. Radvansky v. City of Olmsted Falls",
          "cluster_id": 788941,
          "cite": [
            "395 F.3d 291",
            "2005 U.S. App. LEXIS 739",
            "2005 WL 77154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Kimball",
          "cluster_id": 1906975,
          "cite": [
            "724 A.2d 326",
            "555 Pa. 299",
            "1999 Pa. LEXIS 134"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brian Sheppard v. Leon Beerman, as an Individual and in His Official Capacity as Justice of the Supreme Court of the State of New York",
          "cluster_id": 664638,
          "cite": [
            "18 F.3d 147",
            "1994 U.S. App. LEXIS 3985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark A. Lee v. City of Chicago",
          "cluster_id": 782110,
          "cite": [
            "330 F.3d 456",
            "2003 U.S. App. LEXIS 10254",
            "2003 WL 21196550"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muriel D. Black v. Michael P. Lane, Michael Neal, P.A. Severs, Captain",
          "cluster_id": 669084,
          "cite": [
            "22 F.3d 1395"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan v. Gardner",
          "cluster_id": 601474,
          "cite": [
            "986 F.2d 1521",
            "93 Cal. Daily Op. Serv. 1354",
            "1993 U.S. App. LEXIS 3065",
            "1993 WL 46630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freeman v. City of Santa Ana",
          "cluster_id": 7034204,
          "cite": [
            "68 F.3d 1180",
            "96 Cal. Daily Op. Serv. 25",
            "96 Daily Journal DAR 29",
            "1995 U.S. App. LEXIS 37134",
            "1995 WL 611554"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peggy Poe v. John Leonard, Defendant-Third Party-Plaintiff-Appellant, Douglas Pearl, State of Connecticut, Third-Party-Defendant",
          "cluster_id": 776746,
          "cite": [
            "282 F.3d 123",
            "2002 WL 237411"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Armendariz v. Penman",
          "cluster_id": 7035099,
          "cite": [
            "75 F.3d 1311",
            "96 Cal. Daily Op. Serv. 839",
            "1996 U.S. App. LEXIS 1613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delores Henry v. Melody Hulett",
          "cluster_id": 4774392,
          "cite": [
            "969 F.3d 769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sheila Hensley v. Ronald Gassman",
          "cluster_id": 808240,
          "cite": [
            "693 F.3d 681",
            "2012 WL 3932043",
            "2012 U.S. App. LEXIS 19025"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112795) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQ5NTUyMDAwMDAwJnM9MjQyODA5MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112795%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112795)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkmcz04MTk4NjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112795%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112795)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 1,
        "triage_snippet_classified": 39
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112795)",
    "indexed_citing_opinions": 560,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112795,
        "count": 560,
        "count_source": "search"
      }
    ],
    "citation_count": 1158,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/soldal-v-cook-county.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2Njg3MjEmcz05NDc1MjIwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112795%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112795,
        "cited_id": 87010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 108568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 509655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 567219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 2159763,
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
    "date_created": "2026-07-05T20:02:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:02:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:02:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:05:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:02:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Soldal v. Cook County

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b195-13">
  Justice White
 </author>
<p id="AA-">
  delivered the opinion of the Court.
 </p>
<p id="b195-14">
  HH
 </p>
<p id="b195-3">
  Edward Soldal and his family resided in their trailer home, which was located on a rented lot in the Willoway Terrace
  <span citation-index="1" class="star-pagination" label="58"> 
   *58
   </span>
  mobile home park in Elk Grove, Illinois. In May 1987, Terrace Properties, the owner of the park, and Margaret Hale, its manager, filed an eviction proceeding against the Soldáis in an Illinois state court. Under the Illinois Forcible Entry and Detainer Act, Ill. Rev. Stat., ch.. 110, ¶ 9-101
  <em>
   et seq.
  </em>
  (1991), a tenant cannot be dispossessed absent a judgment of eviction. The suit was dismissed on June 2, 1987. A few months later, in August 1987, the owner brought a second proceeding of eviction, claiming nonpayment of rent. The case was set for trial on September 22, 1987.
 </p>
<p id="b196-5">
  Rather than await judgment in their favor, Terrace Properties and Hale, contrary to Illinois law, chose to evict the Soldáis forcibly two weeks prior to the scheduled hearing. On September 4, Hale notified the Cook County’s Sheriff’s Department that she was going to remove the trailer home from the park, and requested the presence of sheriff deputies to forestall any possible resistance. Later that day, two Terrace Properties employees arrived at the Soldáis’ home accompanied by Cook County Deputy Sheriff O’Neil. The employees proceeded to wrench the sewer and water connections off the side of the trailer home, disconnect the phone, tear off the trailer’s canopy and skirting, and hook the home to a tractor. Meanwhile, O’Neil explained to Edward Soldal that “ ‘he was there to see that [Soldal] didn’t interfere with [Willoway’s] work.’” Brief for Petitioner 6.
 </p>
<p id="b196-6">
  By this time, two more deputy sheriffs had arrived at the scene and Soldal told them that he wished to file a complaint for criminal trespass. They referred him to Deputy Lieutenant Jones, who was in Hale’s office. Jones asked Soldal to wait outside while he remained closeted with Hale and other Terrace Properties employees for over 20 minutes. After talking to a district attorney and making Soldal wait another half hour, Jones told Soldal that he would not accept a complaint because “ ‘it was between the landlord and the tenant . . . [and] they were going to go ahead and continue to move
  <span citation-index="1" class="star-pagination" label="59"> 
   *59
   </span>
  out the trailer.’”
  <em>
   Id.,
  </em>
  at 8.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Throughout this period, the deputy sheriffs knew that Terrace Properties did not have an eviction order and that its actions were unlawful. Eventually, and in the presence of an additional two deputy sheriffs, the Willoway workers pulled the trailer free of its moorings and towed it onto the street. Later, it was hauled to a neighboring property.
 </p>
<p id="b197-5">
  On September 9, the state judge assigned to the pending eviction proceedings ruled that the eviction had been unauthorized and ordered Terrace Properties to return the Sol-dais’ home to the lot. The home, however, was badly damaged.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  The Soldáis brought this action under <span class="citation no-link">42 U. S. C. § 1983</span>, alleging a violation of their rights under the Fourth and Fourteenth Amendments. They claimed that Terrace Properties and Hale had conspired with Cook County deputy sheriffs to unreasonably seize and remove the Soldáis’ trailer home. The District Judge granted defendants’ motion for summary judgment on the grounds that the Soldáis had failed to adduce any evidence to support their conspiracy theory and, therefore, the existence of state action necessary under § 1983.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b197-6">
  The Court of Appeals for the Seventh Circuit, construing the facts in petitioners’ favor, accepted their contention that there was state action. However, it went on to hold that
  <span citation-index="1" class="star-pagination" label="60"> 
   *60
   </span>
  the removal of the Soldáis’ trailer did not constitute a seizure for purposes of the Fourth Amendment or a deprivation of due process for purposes of the Fourteenth.
 </p>
<p id="b198-5">
  On rehearing, a majority of the Seventh Circuit, sitting en banc, reaffirmed the panel decision.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Acknowledging that what had occurred was a “seizure” in the literal sense of the word, the court reasoned that, because it was not made in the course of public law enforcement and because it did not invade the Soldáis’ privacy, it was not a seizure as contemplated by the Fourth Amendment. <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1076" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d 1073, 1076</a></span> (1991). Interpreting prior cases of this Court, the Seventh Circuit concluded that, absent interference with privacy or liberty, a “pure deprivation of property” is not cognizable under the Fourth Amendment.
  <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1078" aria-description="Citation for case: Edward Soldal v. County of Cook"><em>
   Id.,
  </em>
  at 1078-1079</a></span>. Rather, petitioners’ property interests were protected only by the Due Process Clauses of the Fifth and Fourteenth Amendments.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b198-6">
  We granted certiorari to consider whether the seizure and removal of the Soldáis’ trailer home implicated their Fourth Amendment rights, <span class="citation no-link">603 U. S. 918</span> (1992), and now reverse.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b199-4">
<span citation-index="1" class="star-pagination" label="61"> 
   *61
   </span>
  II
 </p>
<p id="b199-5">
  The Fourth Amendment, made applicable to the States by the Fourteenth,
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#30" aria-description="Citation for case: Ker v. California">374 U. S. 23, 30</a></span> (1963), provides in pertinent part that the “right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . .
 </p>
<p id="b199-6">
  A “seizure” of property, we have explained, occurs when “there is some meaningful interference with an individual’s possessory interests in that property.”
  <em>
   United States
  </em>
  v.
  <em>
   Jacobsen,
  </em>
  <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984). In addition, we have emphasized that “at the very core” of the Fourth Amendment “stands the right of a man to retreat into his own home.”
  <em>
   Silverman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.%20S./366/605/">366 U. S. 605</a></span>, 611 (1961). See also. Oliver v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 178-179</a></span> (1984);
  <em>
   Wyman
  </em>
  v.
  <em>
   James,
  </em>
  <span class="citation" data-id="9424375"><a href="/opinion/108223/wyman-v-james/#316" aria-description="Citation for case: Wyman v. James">400 U. S. 309, 316</a></span> (1971);
  <em>
   Payton
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.%20S./446/573/">446 U. S. 573</a></span>, 601 (1980).
 </p>
<p id="b199-7">
  As a result of the state action in this case, the Soldáis’ domicile was not only seized, it literally was carried away, giving new meaning to the term “mobile home.” We fail to see how being unceremoniously dispossessed of one’s home in the manner alleged to have occurred here can be viewed as anything but a seizure invoking the protection of the Fourth Amendment. Whether the Amendment was in fact
  <span citation-index="1" class="star-pagination" label="62"> 
   *62
   </span>
  violated is, of course, a different question that requires determining if the seizure was reasonable. That inquiry entails the weighing of various factors and is not before us. •
 </p>
<p id="b200-5">
  The Court of Appeals recognized that there had been a seizure, but concluded that it was a seizure only in a “technical” sense, not within the meaning of the Fourth Amendment. This conclusion followed from a narrow reading of the Amendment, which the court construed to safeguard only privacy and liberty interests while leaving unprotected possessory interests where neither privacy nor liberty was at stake. Otherwise, the court said,
 </p>
<blockquote id="b200-6">
  “a constitutional provision enacted two centuries ago [would] make every repossession and eviction with police assistance actionable under — of all things — the Fourth Amendments which] would both trivialize the amendment and gratuitously shift a large body of routine commercial litigation from the state courts to the federal courts. That trivializing, this shift, can be prevented by recognizing the difference between posses-sory and privacy interests.” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1077" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1077</a></span>.
 </blockquote>
<p id="b200-7">
  Because the officers had not entered Soldal’s house, rummaged through his possessions, or, in the Court of Appeals’ view, interfered with his liberty in the course of the eviction, the Fourth Amendment offered no protection against the “grave deprivation” of property that had occurred.
  <em>
   <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/" aria-description="Citation for case: Edward Soldal v. County of Cook">Ibid.</a></span>
  </em>
</p>
<p id="b200-8">
  We do not agree with this interpretation of the Fourth Amendment. The Amendment protects the people from unreasonable searches and seizures of “their persons, houses, papers, and effects.” This language surely cuts.against the novel holding below, and our cases unmistakably hold that the Amendment protects property as well as privacy.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  This
  <span citation-index="1" class="star-pagination" label="63"> 
   *63
   </span>
  much was made clear in
  <em>
   <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen, supra,</a></span>
  </em>
  where we explained that the first Clause of the Fourth Amendment
 </p>
<blockquote id="b201-5">
  “protects two types of expectations, one involving ‘searches,’ the other ‘seizures.’ A ‘search’ occurs when an expectation of privacy that society is prepared to consider reasonable is infringed. A ‘seizure’ of property occurs where there is some meaningful interference with an individual’s possessory interests in that property.” 466 U. S., at 113 (footnote omitted).
 </blockquote>
<p id="b201-6">
  See also
  <em>
   id.,
  </em>
  at 120;
  <em>
   Horton
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#183" aria-description="Citation for case: Horton v. California">496 U. S. 128, 183</a></span> (1990);
  <em>
   Arizona
  </em>
  v.
  <em>
   Hicks,
  </em>
  <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#328" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 328</a></span> (1987);
  <em>
   Maryland
  </em>
  v.
  <em>
   Macon,
  </em>
  <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#469" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463, 469</a></span> (1985);
  <em>
   Texas
  </em>
  v.
  <em>
   Brown,
  </em>
  <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 747-748</a></span> (1983) (Stevens, J., concurring in judgment);
  <em>
   United States
  </em>
  v.
  <em>
   Salvucci,
  </em>
  <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/#91" aria-description="Citation for case: United States v. Salvucci">448 U. S. 83, 91, n. 6</a></span> (1980). Thus, having concluded that chemical testing of powder found in a package did not compromise its owner’s privacy, the Court in
  <em>
   <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span>
  </em>
  did not put an end to its inquiry, as would be required under the view adopted by the Court of Appeals and advocated by respondents. Instead, adhering to the teachings of
  <em>
   United States
  </em>
  v.
  <em>
   Place,
  </em>
  <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), it went on to determine whether the invasion of the owners’ “possessory interests” occasioned by the destruction of the powder was reasonable under the Fourth Amendment.
  <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#124" aria-description="Citation for case: United States v. Jacobsen"><em>
   Jacobsen, supra,
  </em>
  at 124-125</a></span>. In
  <em>
   <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,
  </em>
  although we found that subjecting luggage to a “dog sniff” did not constitute a search for Fourth Amendment purposes because it did not compromise any privacy interest, taking custody of Place’s suitcase was deemed an unlawful seizure for it unreasonably infringed “the suspect’s possessory interest in his luggage.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#708" aria-description="Citation for case: United States v. Place">462 U. S., at 708</a></span>.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  Although lacking a privacy component, the property rights in both instances nonetheless were not
  <span citation-index="1" class="star-pagination" label="64"> 
   *64
   </span>
  disregarded, but rather were afforded Fourth Amendment protection.
 </p>
<p id="b202-5">
  Respondents rely principally on precedents such as
  <em>
   Katz
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967),
  <em>
   Warden, Maryland Penitentiary
  </em>
  v.
  <em>
   Hayden,
  </em>
  <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), and
  <em>
   Cardwell
  </em>
  v.
  <em>
   Lewis,
  </em>
  <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583</a></span> (1974), to demonstrate that the Fourth Amendment is only marginally concerned with property rights. But the message of those cases is that property rights are not the sole measure of Fourth Amendment violations. The
  <em>
   Warden
  </em>
  opinion thus observed, citing
  <em>
   Jones
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), and
  <em>
   Silverman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), that the “principal” object of the Amendment is the protection of privacy rather than property and that “this shift in emphasis from property to privacy has come about through a subtle interplay of substantive and procedural reform.” <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 304</a></span>. There was no suggestion that this shift in emphasis had snuffed out the previously recognized protection for property under the Fourth Amendment.
  <em>
   <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,
  </em>
  in declaring violative of the Fourth Amendment the unwarranted overhearing of a telephone booth conversation, effectively ended any lingering notions that the protection of privacy depended on trespass into a protected area. In the course of its decision, the
  <em>
   <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>
  </em>
  Court stated that the Fourth Amendment can neither be translated into a provision dealing with constitutionally protected areas nor. into a general constitutional right to privacy. The Amendment, the Court said, protects individual privacy against certain kinds of governmental intrusion, “but its protections go further, and often have nothing to do with privacy at all.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S., at 350</a></span>.
 </p>
<p id="b202-6">
  As for
  <em>
   <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">Cardwell</a></span>,
  </em>
  a plurality of this Court held in that case that the Fourth Amendment did not bar the use in evidence of paint scrapings taken from and tire treads observed on the defendant’s automobile, which had been seized in a parking lot and towed to a police lockup. Gathering this evidence was not deemed to be a search, for nothing from the
  <span citation-index="1" class="star-pagination" label="65"> 
   *65
   </span>
  interior of the car and “no personal effects, which the Fourth Amendment traditionally has been deemed to protect” were searched or seized. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#591" aria-description="Citation for case: Cardwell v. Lewis">417 U. S., at 591</a></span> (opinion of Blackmun, J.). No meaningful privacy rights were invaded. But this left the argument, pressed by the dissent, that the evidence gathered was the product of a warrantless and hence illegal seizure of the car from the parking lot where the defendant had left it. However, the plurality was of the view that, because under the circumstances of the case there was probable cause to seize the car as an instrumentality of the crime, Fourth Amendment precedent permitted the seizure without a warrant.
  <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#593" aria-description="Citation for case: Cardwell v. Lewis"><em>
   Id.,
  </em>
  at 593</a></span>. Thus, both the plurality and dissenting Justices considered the defendant’s auto deserving of Fourth Amendment protection even though privacy interests were not at stake. They differed only in the degree of protection that the Amendment demanded.
 </p>
<p id="b203-5">
  The Court of Appeals appeared to find more specific support for confining the protection of the Fourth Amendment to privacy interests in our decision in
  <em>
   Hudson
  </em>
  v.
  <em>
   Palmer,
  </em>
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/" aria-description="Citation for case: Hudson v. Palmer">468 U. S. 517</a></span> (1984). There, a state prison inmate sued, claiming that prison guards had entered his cell without consent and had seized and destroyed some of his personal effects. We ruled that an inmate, because of his status, enjoyed neither a right to privacy in his cell nor protection against unreasonable seizures of his personal effects.
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#526" aria-description="Citation for case: Hudson v. Palmer"><em>
   Id.,
  </em>
  at 526-528</a></span>, and n. 8;
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#538" aria-description="Citation for case: Hudson v. Palmer"><em>
   id.,
  </em>
  at 538</a></span> (O’Connor, J., concurring). Whatever else the case held, it is of limited usefulness outside the prison context with respect to the coverage of the Fourth Amendment.
 </p>
<p id="b203-6">
  We thus are unconvinced that any of the Court’s prior cases supports the view that the Fourth Amendment protects against unreasonable seizures of property only where privacy or liberty is also implicated. What is more, our “plain view” decisions make untenable such a construction of the Amendment. Suppose, for example, that police officers lawfully enter a house, by either complying with the warrant requirement or satisfying one of its recognized exceptions—
  <span citation-index="1" class="star-pagination" label="66"> 
   *66
   </span>
<em>
   e. g.,
  </em>
  through a valid consent or a showing of exigent circumstances. If they come across some item in plain view and seize it, no invasion of personal privacy has occurred.
  <em>
   Horton,
  </em>
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#133" aria-description="Citation for case: Horton v. California">496 U. S., at 133-134</a></span>;
  <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown"><em>
   Brown, supra,
  </em>
  at 739</a></span> (opinion of Rehnquist, J.). If the boundaries of the Fourth Amendment were defined exclusively by rights of privacy, “plain view” seizures would not implicate that constitutional provision at all. Yet, far from being automatically upheld, “plain view” seizures have been scrupulously subjected to Fourth Amendment inquiry. Thus, in the absence of consent or a warrant permitting the seizure of the items in question, such seizures can be justified only if they meet the probable-cause standard,
  <em>
   Arizona
  </em>
  v.
  <em>
   Hicks,
  </em>
  <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#326" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 326-327</a></span> (1987),
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  and if they are unaccompanied by unlawful trespass,
  <em>
   Horton,
  </em>
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California">496 U. S., at 136-137</a></span>.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  That is because, the absence of a privacy interest notwithstanding, “[a] seizure of the article ... would obviously invade the owner’s possessory interest.”
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#134" aria-description="Citation for case: Horton v. California"><em>
   Id.,
  </em>
  at 134</a></span>; see also
  <em>
   Brown,
  </em>
  <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown">460 U. S., at 739</a></span> (opinion of Rehnquist, J.). The plain-view doctrine “merely reflects an application of the Fourth Amendment’s central requirement of reasonableness to the law governing seizures of property.”
  <em>
   Ibid.; Coolidge
  </em>
  v.
  <em>
   New Hampshire,
  </em>
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 468</a></span> (1971);
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#516" aria-description="Citation for case: Coolidge v. New Hampshire"><em>
   id.,
  </em>
  at 516</a></span> (White, J., concurring and dissenting).
 </p>
<p id="b204-5">
  The Court of Appeals understandably found it necessary to reconcile its holding with our recognition in the plain-view cases that the Fourth Amendment protects property as such. In so doing, the court did not distinguish this case on the ground that the seizure of the Soldáis’ home took place in a
  <span citation-index="1" class="star-pagination" label="67"> 
   *67
   </span>
  noncriminal context. Indeed, it acknowledged what is evident from our precedents — that the Amendment’s protection applies in the civil context as well. See
  <em>
   O’Connor
  </em>
  v.
  <em>
   Ortega,
  </em>
  <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987);
  <em>
   New Jersey
  </em>
  v.
  <em>
   T. L. O.,
  </em>
  <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#334" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 334-335</a></span> (1985);
  <em>
   Michigan
  </em>
  v.
  <em>
   Tyler,
  </em>
  <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#504" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 504-506</a></span> (1978);
  <em>
   Marshall
  </em>
  v.
  <em>
   Barlow’s, Inc.,
  </em>
  <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312-313</a></span> (1978);
  <em>
   Camara
  </em>
  v.
  <em>
   Municipal Court of San Francisco,
  </em>
  <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967).
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
</p>
<p id="b205-5">
  Nor did the Court of Appeals suggest that the Fourth Amendment applied exclusively to law enforcement activities. It observed, for example, that the Amendment’s protection would be triggered “by a search or other entry into the home incident to an eviction or repossession,” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1077" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1077</a></span>.
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  Instead, the court sought to explain why the Fourth Amendment protects against seizures of property in the plain-view context, but not in this case, as follows:
 </p>
<blockquote id="b205-6">
  “[S]eizures made in the course of investigations by police or other law enforcement officers are almost always, as' in the plain view cases, the culmination of searches. The police search in order to seize, and it is the search
  <span citation-index="1" class="star-pagination" label="68"> 
   *68
   </span>
<em>
   and ensuing seizure
  </em>
  that the Fourth Amendment by its reference to ‘searches and seizures’ seeks to regulate. Seizure means one thing when it is the outcome of a search; it may mean something else when it stands apart from a search or any other investigative activity. The Fourth Amendment may still nominally apply, but, precisely because there is no invasion of privacy, the usual rules do not apply.”
  <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1079" aria-description="Citation for case: Edward Soldal v. County of Cook"><em>
   Id.,
  </em>
  at 1079</a></span> (emphasis in original).
 </blockquote>
<p id="b206-5">
  We have difficulty with this passage. The court seemingly construes the Amendment to protect only against seizures that are the outcome of a search. But our cases are to the contrary and hold that seizures of property are subject to Fourth Amendment scrutiny even though no search within the meaning of the Amendment has taken place. See,
  <em>
   e. g., Jacobsen,
  </em>
  466 U. S., at 120-125; Place, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U. S., at 706-707</a></span>;
  <em>
   Cardwell,
  </em>
  <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#588" aria-description="Citation for case: Cardwell v. Lewis">417 U. S., at 588-589</a></span>.
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
  More generally, an officer who happens to come across an individual’s property in a public area could seize it only if Fourth Amendment standards are satisfied — for example, if the items are evidence of a crime or contraband. Cf.
  <em>
   Payton
  </em>
  v.
  <em>
   New York,
  </em>
<span citation-index="1" class="star-pagination" label="69"> 
   *69
   </span>
  445 U. S., at 587. We are also puzzled by the last sentence of the excerpt, where the court announces that the “usual rules” of the Fourth Amendment are inapplicable if the seizure is not the result of a search or any other investigative activity “precisely because there is no invasion of privacy.” For the plain-view cases clearly state that, notwithstanding the absence of any interference with privacy, seizures of effects that are not authorized by a warrant are reasonable only because there is probable cause to associate the property with criminal activity. The seizure of the weapons in
  <em>
   <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/" aria-description="Citation for case: Horton v. California">Horton</a></span>,
  </em>
  for example, occurred in the midst of a search, yet we emphasized that it did not “involve any invasion of privacy.” <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#133" aria-description="Citation for case: Horton v. California">496 U. S., at 133</a></span>. In short, our statement that such seizures must satisfy the Fourth Amendment and will be deemed reasonable only if the item’s incriminating character is “immediately apparent,”
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California"><em>
   id.,
  </em>
  at 136-137</a></span>, is at odds with the Court of Appeals’ approach.
 </p>
<p id="b207-5">
  The Court of Appeals’ effort is both interesting and creative, but at bottom it simply reasserts the earlier thesis that the Fourth Amendment protects privacy but not property. We remain unconvinced and see no justification for departing from our prior cases. In our view, the reason why an officer might enter a house or effectuate a seizure is wholly irrelevant to the threshold question whether the Amendment applies. What matters is the intrusion on the people’s security from governmental interference. Therefore, the right against unreasonable seizures would be no less transgressed if the seizure of the house was undertaken to collect evidence, verify compliance with a housing regulation, effect an eviction by the police, or on a whim, for no reason at all. As we have observed on more than one occasion, it would be “anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior.”
  <em>
   Camara,
  </em>
  <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 530</a></span>; see also
  <em>
   O’Connor,
  </em>
  480 U. S., at 715;
  <em>
   T. L. O.,
  </em>
  <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#335" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 335</a></span>.
 </p>
<p id="b208-4">
<span citation-index="1" class="star-pagination" label="70"> 
   *70
   </span>
  The Court of Appeals also stated that even if, contrary to its previous rulings, “there is some element or tincture of a Fourth Amendment seizure, it cannot carry the day for the Soldáis.” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1080" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1080</a></span>. Relying on our decision in
  <em>
   Graham
  </em>
  v.
  <em>
   Connor,
  </em>
  <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989), the court reasoned that it should look at the “dominant character of the conduct challenged in a section 1983 case [to] determine the constitutional standard under which it is evaluated.” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1080" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1080</a></span>. Believing that the Soldáis' claim was more akin to a challenge against the deprivation of property without due process of law than against an unreasonable seizure, the court concluded that they should not be allowed to bring their suit under the guise of the Fourth Amendment.
 </p>
<p id="b208-5">
  But we see no basis for doling out constitutional protections in such fashion. Certain wrongs affect more than a single right and, accordingly, can implicate more than one of the Constitution’s commands. Where such multiple violations are alleged, we are not in the habit of identifying as a preliminary matter the claim’s “dominant” character. Rather, we examine each constitutional provision in turn. See,
  <em>
   e. g., Hudson
  </em>
  v.
  <em>
   Palmer,
  </em>
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/" aria-description="Citation for case: Hudson v. Palmer">468 U. S. 517</a></span> (1984) (Fourth Amendment and Fourteenth Amendment Due Process Clause);
  <em>
   Ingraham
  </em>
  v.
  <em>
   Wright,
  </em>
  <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span> (1977) (Eighth Amendment and Fourteenth Amendment Due Process Clause).
  <em>
   <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>
  </em>
  is not to the contrary. Its holding was that claims of excessive use of force should be analyzed under the Fourth Amendment’s reasonableness standard, rather than the Fourteenth Amendment’s substantive due process test. We were guided by the fact that, in that case, both provisions targeted the same sort of governmental conduct and, as a result, we chose the more “explicit textual source of constitutional protection” over the “more generalized notion of ‘substantive due process.’” <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor">490 U. S., at 394-395</a></span>. Surely,
  <em>
   <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>
  </em>
  does not bar resort in this case to the Fourth Amendment’s specific protection for “houses, papers,
  <span citation-index="1" class="star-pagination" label="71"> 
   *71
   </span>
  and effects” rather than the general protection of property in the Due Process Clause.
 </p>
<p id="pAC6">
  III
 </p>
<p id="b209-3">
  Respondents are fearful, as was the Court of Appeals, that applying the Fourth Amendment in this context inevitably will carry it into territory unknown and unforeseen: routine repossessions, negligent actions of public employees that interfere with individuals’ right to enjoy their homes, and the like, thereby federalizing areas of law traditionally the concern of the States. For several reasons, we think the risk is exaggerated. To begin, our decision will have no impact on activities such as repossessions or attachments if they involve entry into the home, intrusion on individuals’ privacy, or interference with their liberty, because they would implicate the Fourth Amendment even on the Court of Appeals’ own terms. This was true of the Tenth Circuit’s decision in
  <em>
   Specht
  </em>
  with which, as we previously noted, the Court of Appeals expressed agreement.
 </p>
<p id="b209-4">
  More significantly, “reasonableness is still the ultimate standard” under the Fourth Amendment,
  <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>
   Camara, supra,
  </em>
  at 539</a></span>, which means that numerous seizures of this type will survive constitutional scrutiny. As is true in other circumstances, the reasonableness determination will reflect a “careful balancing of governmental and private interests.”
  <em>
   T. L. O., supra,
  </em>
  at 341. Assuming, for example, that the officers were acting pursuant to a court order, as in
  <em>
   Specht
  </em>
  v.
  <em>
   Jensen,
  </em>
  <span class="citation" data-id="8955392"><a href="/opinion/8964119/specht-v-jensen/" aria-description="Citation for case: Specht v. Jensen">832 F. 2d 1516</a></span> (CA10 1987), or
  <em>
   Fuentes
  </em>
  v.
  <em>
   Shevin,
  </em>
  <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972), and as often would be the case, a showing of unreasonableness on these facts would be a laborious task indeed. Cf.
  <em>
   Simms
  </em>
  v.
  <em>
   Slacum,
  </em>
  <span class="citation" data-id="9416257"><a href="/opinion/84818/simms-v-slacum/#301" aria-description="Citation for case: Simms v. Slacum">3 Cranch 300, 301</a></span> (1806). Hence, while there is no guarantee against the filing of frivolous suits, had the ejection in this case properly awaited the state court’s judgment it is quite unlikely that the federal court would have been bothered with a § 1983 action alleging a Fourth Amendment violation.
 </p>
<p id="b210-5">
<span citation-index="1" class="star-pagination" label="72"> 
   *72
   </span>
  Moreover, we doubt that the police will often choose to further an enterprise knowing that it is contrary to the law, or proceed to seize property in the absence of objectively reasonable grounds for doing so. In short, our reaffirmance of Fourth Amendment principles today should not foment a wave of new litigation in the federal courts.
 </p>
<p id="b210-6">
<em>
   &gt;
  </em>
</p>
<p id="b210-3">
  The complaint here alleges that respondents, acting under color of state law, dispossessed the Soldáis of their trailer home by physically tearing it from its foundation and towing it to another lot. Taking these allegations as true, this was no “garden-variety” landlord-tenant or commercial dispute. The facts alleged suffice to constitute a “seizure” within the meaning of the . Fourth Amendment, for they plainly implicate the interests protected by that provision. The judgment of the Court of Appeals is, accordingly, reversed, and the case is remanded for further proceedings consistent with this opinion.
 </p>
<p id="b210-8">
<em>
   So ordered.
  </em>
</p>













<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b197-7">
   Jones’ statement was prompted by a district attorney’s advice that no criminal charges could be brought because, under Illinois law, a criminal action cannot be used to determine the right of possession. See Ill. Rev. Stat., ch. 110, ¶ 9-101
   <em>
    et seq.
   </em>
   (1991);
   <em>
    People
   </em>
   v.
   <em>
    Evans,
   </em>
   <span class="citation" data-id="2159763"><a href="/opinion/2159763/people-v-evans/" aria-description="Citation for case: People v. Evans">163 Ill. App. 3d 561</a></span>, <span class="citation" data-id="2159763"><a href="/opinion/2159763/people-v-evans/" aria-description="Citation for case: People v. Evans">516 N. E. 2d 817</a></span> (1st Dist. 1987).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b197-8">
   The Soldáis ultimately were evicted per court order in December 1987.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b197-9">
   Title <span class="citation no-link">42 U. S. C. § 1983</span> provides that:
  </p>
<blockquote id="b197-10">
   “Every person who, under color of any statute, ordinance, regulation, custom or usage, of any State . . . subjects, or causes to be subjected, any citizen of the United States ... to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b198-7">
   The court reiterated the panel’s conclusion that a conspiracy must be assumed on the state of the record and, therefore, that the case must be treated in its current posture “as if the deputy sheriffs themselves seized the trailer, disconnected it from the utilities, and towed it away.” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1076" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d 1073, 1076</a></span> (1991).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b198-8">
   The court noted that, in light of the existence of adequate judicial remedies under state law, a claim for deprivation of property without due process of law was unlikely to succeed.
   <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1075" aria-description="Citation for case: Edward Soldal v. County of Cook"><em>
    Id.,
   </em>
   at 1075-1076</a></span>. See
   <em>
    Parratt
   </em>
   v.
   <em>
    Taylor,
   </em>
   <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">451 U. S. 527</a></span> (1981). In any event, the Soldáis did not claim a violation of their procedural rights. As noted, the Seventh Circuit also held that respondents had not violated the Soldáis’ substantive due process rights under the Fourteenth Amendment. Petitioners assert that this was error, but in view of our disposition of the case we need not address the question at this time.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b198-9">
   Under <span class="citation no-link">42 U. S. C. § 1983</span>, the Soldáis were required to establish that the respondents, acting under color of state law, deprived them of a constitutional right, in this instance, their Fourth and Fourteenth Amendment freedom from unreasonable seizures by the State. See
   <em>
    Monroe
   </em>
   v.
   <em>
    Pape,
   </em>
<span citation-index="1" class="star-pagination" label="61"> 
    *61
    </span>
   <span class="citation" data-id="106225"><a href="/opinion/106225/lush-v-commissioner-of-education-of-new-york/#184" aria-description="Citation for case: Lush v. Commissioner of Education of New York">366 U. S. 167, 184</a></span> (1961). Respondents request that we affirm on the ground that the Court of Appeals erred in holding that there was sufficient state action to support a § 1983 action. The alleged injury to the Soldáis, it is urged, was inflicted by private parties for whom the county is not responsible. Although respondents did not cross-petition, they are entitled to ask us to affirm on that ground if such action would not enlarge the judgment of the Court of Appeals in their favor. The Court of Appeals found that because the police prevented Soldal from using reasonable force to protect his home from private action that the officers knew was illegal, there was sufficient evidence of conspiracy between the private parties and the officers to foreclose summary judgment for respondents. We are not inclined to review that holding. See
   <em>
    Adickes
   </em>
   v.
   <em>
    S. H. Kress &amp; Co.,
   </em>
   <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#152" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 152-161</a></span> (1970).
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b200-9">
   In holding that the Fourth Amendment’s reach extends to property as such, we are mindful that the Amendment does not protect possessory interests in all kinds of property. See,
   <em>
    e. g., Oliver
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#176" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 176-177</a></span> (1984). This case, however, concerns a house, which the Amendment’s language explicitly includes, as it does a person’s effects.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b201-7">
<em>
    <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>
   </em>
   also found that to detain luggage for 90 minutes was an unreasonable deprivation of the individual’s “liberty interest in proceeding with his itinerary,” which also is protected by the Fourth Amendment. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#708" aria-description="Citation for case: United States v. Place">462 U. S., at 708-710</a></span>.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b204-6">
   When “operational necessities” exist, seizures can be justified on less than probable cause. 480 U. S., at 327. That in no way affects our analysis, for even then it is clear that the Fourth Amendment applies.
   <em>
    Ibid.;
   </em>
   see also
   <em>
    United States
   </em>
   v.
   <em>
    Place,
   </em>
   <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983).
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b204-7">
   Of course, if the police officers’ presence in the home itself entailed a violation of the Fourth Amendment, no amount of probable cause to believe that an item in plain view constitutes incriminating evidence will justify its seizure.
   <em>
    Horton,
   </em>
   <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California">496 U. S., at 136-137</a></span>.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b205-7">
   It is true that
   <em>
    Murray’s Lessee
   </em>
   v.
   <em>
    Hoboken Land &amp; Improvement Co.,
   </em>
   <span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">18 How. 272</a></span> (1856), cast some doubt on the applicability of the Amendment to noncriminal encounters such as this.
   <span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/#285" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co."><em>
    Id.,
   </em>
   at 285</a></span>. But cases since that time have shed a different light, making clear that Fourth Amendment guarantees are triggered by governmental searches and seizures “without regard to the use to which [houses, papers, and effects] are applied.”
   <em>
    Warden, Maryland Penitentiary
   </em>
   v.
   <em>
    Hayden,
   </em>
   <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#301" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 301</a></span> (1967).
   <em>
    Murray’s Lessee’s
   </em>
   broad statement that the Fourth Amendment “has no reference to civil proceedings for the recovery of debt” arguably only meant that the warrant requirement did not apply, as was suggested in
   <em>
    G. M. Leasing Corp.
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#352" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 352</a></span> (1977). Whatever its proper reading, we reaffirm today our basic understanding that the protection against unreasonable searches and seizures fully applies in the civil context.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b205-8">
   This was the view expressed by the Court of Appeals for the Tenth Circuit in
   <em>
    Specht
   </em>
   v.
   <em>
    Jensen,
   </em>
   <span class="citation" data-id="8955392"><a href="/opinion/8964119/specht-v-jensen/" aria-description="Citation for case: Specht v. Jensen">832 F. 2d 1516</a></span> (1987), remanded on unrelated grounds, <span class="citation multiple-matches"><a href="/c/F.%202d/853/805/">853 F. 2d 805</a></span> (1988) (en banc), with which the Seventh Circuit expressly agreed. <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1076" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1076</a></span>.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b206-6">
   The officers in these cases were engaged in law enforcement and were ■looking for something that was found and seized. In this broad sense the seizures were the result of “searches,” but not in the Fourth Amendment sense. That the Court of Appeals might have been suggesting that the plain-view cases are explainable because they almost always occur in the course of law enforcement activities receives some support from the penultimate sentence of the quoted passage, where the court states that the word “seizure” might lose its usual meaning “when it stands apart from a search or
   <em>
    any other investigative activity.” Id.,
   </em>
   at 1079 (emphasis added). And, in the following paragraph, it observes that “[ojutside of the law enforcement area the Fourth Amendment retains its force as a protection against searches, because they invade privacy. That is why we decline to confine the amendment to the law enforcement setting.”
   <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1079" aria-description="Citation for case: Edward Soldal v. County of Cook"><em>
    Id.,
   </em>
   at 1079-1080</a></span>. Even if the court meant that seizures of property in the course of law enforcement activities, whether civil or criminal, implicate interests safeguarded by the Fourth Amendment, but that pure property interests are unprotected in the non-law-enforcement setting, we are not in accord, as indicated in the body of this opinion.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Sorrells v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Sorrells v. United States"
type: case
citation: "287 U.S. 435 (1932)"
parallel_cite: "53 S. Ct. 210; 77 L. Ed. 413; 86 A.L.R. 249"
neutral_cite: 1932 U.S. LEXIS 30
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1932
date_decided: 1932-12-19
docket: 100
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1932-12-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Sorrells v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/101997/sorrells-v-united-states/"
  cluster_id: 101997
  opinion_id: 101997
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Anchor"
related: ["[[Sherman v. United States]]", "[[Hampton v. United States]]", "[[Jacobson v. United States]]", "[[Mathews v. United States]]"]
aliases: []
tags: ["case", "entrapment", "predisposition", "prohibition"]
holding: "Entrapment is a valid defense; it arises when government officials implant the criminal design in the mind of a person who had no…"
lake:
  record_id: Sorrells v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Sorrells v. United States

*287 U.S. 435 (1932)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Prohibition agent, posing as a fellow World War I veteran, visited Sorrells's home and—after bonding over their shared war service—repeatedly asked Sorrells to obtain liquor. Sorrells twice refused, then eventually procured a half-gallon of whiskey. He was convicted of possessing and selling liquor and asserted entrapment.

## Issue
Whether entrapment is a valid defense, and on what basis, when government agents induce an otherwise law-abiding person to commit a crime.

## Rule
Government inducement of an otherwise innocent person can defeat conviction. "Entrapment is the conception and planning of an offense by an officer, and his procurement of its commission by one who would not have perpetrated it except for the trickery, persuasion, or fraud of the officer." — 287 U.S. at 454. ^pin-454

The Court grounded the defense in statutory construction: Congress is not presumed to have intended its penal statutes to reach a person whose criminal design originated with the government rather than with himself.

## Application
The agent exploited a shared-veteran rapport and persistent entreaties to overcome Sorrells's repeated refusals; because the evidence permitted a finding that the criminal design originated with the government and that Sorrells was not otherwise disposed to the offense, the entrapment issue should have gone to the jury, and the Court reversed.

## Conclusion
Entrapment is a valid defense resting on the inference that Congress did not intend to punish persons lured into crime by its own officers; the conviction was reversed and [[Reading and Citing Cases#on-remand|remanded]] for the jury to decide entrapment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The origin of the federal entrapment defense and its subjective (predisposition) test, applied in [[Sherman v. United States]] and reaffirmed in [[Jacobson v. United States]] and [[Mathews v. United States]]; the due-process outer boundary was addressed in [[Hampton v. United States]].

## Appears on
- [[Entrapment]] — *Key — Anchor*

## Sources
- *Sorrells v. United States*, 287 U.S. 435 (1932) — https://www.courtlistener.com/opinion/101997/sorrells-v-united-states/ — pinpoint: 454.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6e53e1e79434b362", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "287 U.S. 435 (1932)", "court": "U.S. Supreme Court", "neutral_cite": "1932 U.S. LEXIS 30", "official_citation_present": true, "parallel_cite": "53 S. Ct. 210; 77 L. Ed. 413; 86 A.L.R. 249", "title": "Sorrells v. United States", "year": "1932"}}
{"assertion_id": "19f48537a6221381", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Entrapment is a valid defense; it arises when government officials implant the criminal design in the mind of a person who had no…", "title": "Sorrells v. United States"}}
{"assertion_id": "2b315f3ec5a1b453", "dimension": "support", "kind": "home_role", "locator": {"home": "Entrapment"}, "payload": {"home": "Entrapment", "role": "Key — Anchor", "title": "Sorrells v. United States"}}
{"assertion_id": "5acb2948192959ae", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1932-12-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Sorrells v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Sorrells v. United States", "varies_by_point": "false"}}
{"assertion_id": "fa374b3335e89900", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Sorrells v. United States"}}
```

### lake record — Sorrells v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Sorrells v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Sorrells v. United States",
    "case_name_short": "Sorrells",
    "case_name_full": "Sorrells v. United States",
    "input_case_name": "Sorrells v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1932-12-19",
    "year": 1932,
    "docket": "100",
    "cluster_id": 101997,
    "lead_opinion_id": 101997,
    "sibling_ids": [
      101997
    ],
    "absolute_url": "/opinion/101997/sorrells-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "287 U.S. 435",
      "volume": "287",
      "reporter": "U.S.",
      "page": "435",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "53 S. Ct. 210",
        "volume": "53",
        "reporter": "S. Ct.",
        "page": "210",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 413",
        "volume": "77",
        "reporter": "L. Ed.",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 A.L.R. 249",
        "volume": "86",
        "reporter": "A.L.R.",
        "page": "249",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1932 U.S. LEXIS 30",
        "volume": "1932",
        "reporter": "U.S. LEXIS",
        "page": "30",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "287 U.S. 435",
        "volume": "287",
        "reporter": "U.S.",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 S. Ct. 210",
        "volume": "53",
        "reporter": "S. Ct.",
        "page": "210",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 413",
        "volume": "77",
        "reporter": "L. Ed.",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1932 U.S. LEXIS 30",
        "volume": "1932",
        "reporter": "U.S. LEXIS",
        "page": "30",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 A.L.R. 249",
        "volume": "86",
        "reporter": "A.L.R.",
        "page": "249",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "287 U.S. 435",
    "official_selection": {
      "court_class": "scotus",
      "selected": "287 U.S. 435",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-454",
      "page": null,
      "quote": "--- # Sorrells v. United States *287 U.S. 435 (1932)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Prohibition agent, posing as a fellow World War I veteran, visited Sorrells's home and\u2014after bonding over their shared war service\u2014repeatedly asked Sorrells to obtain liquor. Sorrells twice refused, then eventually procured a half-gallon of whiskey. He was convicted of possessing and selling liquor and asserted entrapment. ## Issue Whether entrapment is a valid defense, and on what basis, when government agents induce an otherwise law-abiding person to commit a crime. ## Rule Government inducement of an otherwise innocent person can defeat conviction.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1932-12-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Sorrells v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Delgado-Marrero",
          "cluster_id": 2652872,
          "cite": [
            "744 F.3d 167",
            "2014 WL 522462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cordae Black",
          "cluster_id": 1086588,
          "cite": [
            "733 F.3d 294"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gutierrez",
          "cluster_id": 32172,
          "cite": [
            "343 F.3d 415",
            "2003 U.S. App. LEXIS 16694",
            "2003 WL 21940783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maffett",
          "cluster_id": 1986216,
          "cite": [
            "633 N.W.2d 339",
            "464 Mich. 878"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald Dodd",
          "cluster_id": 770267,
          "cite": [
            "225 F.3d 340",
            "2000 U.S. App. LEXIS 21423"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terry Lee Brooks",
          "cluster_id": 769099,
          "cite": [
            "215 F.3d 842",
            "2000 U.S. App. LEXIS 13688",
            "2000 WL 764784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard D. Barnett Virgil R. Drake",
          "cluster_id": 766842,
          "cite": [
            "197 F.3d 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vazquez v. State",
          "cluster_id": 1799192,
          "cite": [
            "700 So. 2d 5",
            "1997 WL 361832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opn. No.",
          "cluster_id": 3594829,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Sandoval",
          "cluster_id": 603895,
          "cite": [
            "990 F.2d 481",
            "93 Daily Journal DAR 4205",
            "93 Cal. Daily Op. Serv. 2475",
            "1993 U.S. App. LEXIS 6759",
            "1993 WL 94342"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellant/cross-Appellee v. Jack Pardue, Michel Pardue, Appellee/cross-Appellant",
          "cluster_id": 597867,
          "cite": [
            "983 F.2d 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. American Trucking Associations",
          "cluster_id": 103369,
          "cite": [
            "310 U.S. 534",
            "60 S. Ct. 1059",
            "84 L. Ed. 1345",
            "1940 U.S. LEXIS 1049"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell",
          "cluster_id": 108768,
          "cite": [
            "36 L. Ed. 2d 366",
            "93 S. Ct. 1637",
            "411 U.S. 423",
            "1973 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richmond Newspapers, Inc. v. Virginia",
          "cluster_id": 110339,
          "cite": [
            "65 L. Ed. 2d 973",
            "100 S. Ct. 2814",
            "448 U.S. 555",
            "1980 U.S. LEXIS 18",
            "6 Media L. Rep. (BNA) 1833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee Valley Authority v. Hill",
          "cluster_id": 109897,
          "cite": [
            "57 L. Ed. 2d 117",
            "98 S. Ct. 2279",
            "437 U.S. 153",
            "1978 U.S. LEXIS 33",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20513",
            "11 ERC (BNA) 1705"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maine v. Thiboutot",
          "cluster_id": 110322,
          "cite": [
            "65 L. Ed. 2d 555",
            "100 S. Ct. 2502",
            "448 U.S. 1",
            "1980 U.S. LEXIS 51"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sherman v. United States",
          "cluster_id": 105681,
          "cite": [
            "2 L. Ed. 2d 848",
            "78 S. Ct. 819",
            "356 U.S. 369",
            "1958 U.S. LEXIS 1024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mathews v. United States",
          "cluster_id": 112012,
          "cite": [
            "99 L. Ed. 2d 54",
            "108 S. Ct. 883",
            "485 U.S. 58",
            "1988 U.S. LEXIS 943"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez v. United States",
          "cluster_id": 106622,
          "cite": [
            "10 L. Ed. 2d 462",
            "83 S. Ct. 1381",
            "373 U.S. 427",
            "1963 U.S. LEXIS 2618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hampton v. United States",
          "cluster_id": 109437,
          "cite": [
            "48 L. Ed. 2d 113",
            "96 S. Ct. 1646",
            "425 U.S. 484",
            "1976 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gore v. United States",
          "cluster_id": 105742,
          "cite": [
            "2 L. Ed. 2d 1405",
            "78 S. Ct. 1280",
            "357 U.S. 386",
            "1958 U.S. LEXIS 1801"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lewis v. United States",
          "cluster_id": 107312,
          "cite": [
            "17 L. Ed. 2d 312",
            "87 S. Ct. 424",
            "385 U.S. 206",
            "1966 U.S. LEXIS 3"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jacobson v. United States",
          "cluster_id": 112720,
          "cite": [
            "118 L. Ed. 2d 174",
            "112 S. Ct. 1535",
            "503 U.S. 540",
            "1992 U.S. LEXIS 2117"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cahan",
          "cluster_id": 1237532,
          "cite": [
            "282 P.2d 905",
            "44 Cal. 2d 434",
            "50 A.L.R. 2d 513",
            "1955 Cal. LEXIS 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Avery W. Vial, Movant",
          "cluster_id": 741872,
          "cite": [
            "115 F.3d 1192",
            "1997 U.S. App. LEXIS 14166",
            "1997 WL 324385"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evans v. Jeff D. Ex Rel. Johnson",
          "cluster_id": 111627,
          "cite": [
            "89 L. Ed. 2d 747",
            "106 S. Ct. 1531",
            "475 U.S. 717",
            "1986 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corbitt v. New Jersey",
          "cluster_id": 109956,
          "cite": [
            "58 L. Ed. 2d 466",
            "99 S. Ct. 492",
            "439 U.S. 212",
            "1978 U.S. LEXIS 144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Armstrong Paint & Varnish Works v. Nu-Enamel Corp.",
          "cluster_id": 103108,
          "cite": [
            "305 U.S. 315",
            "59 S. Ct. 191",
            "83 L. Ed. 195",
            "1938 U.S. LEXIS 1174",
            "39 U.S.P.Q. (BNA) 402"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Shuck",
          "cluster_id": 1060967,
          "cite": [
            "953 S.W.2d 662",
            "70 A.L.R. 5th 743",
            "1997 Tenn. LEXIS 487",
            "1997 WL 610824"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raley v. Ohio",
          "cluster_id": 105925,
          "cite": [
            "3 L. Ed. 2d 1344",
            "79 S. Ct. 1257",
            "360 U.S. 423",
            "1959 U.S. LEXIS 754"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Christopher Twigg, Iii, United States of America v. Henry Alfred Neville",
          "cluster_id": 361264,
          "cite": [
            "588 F.2d 373"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Burnet v. Guggenheim",
          "cluster_id": 102035,
          "cite": [
            "288 U.S. 280",
            "53 S. Ct. 369",
            "77 L. Ed. 748",
            "1933 U.S. LEXIS 40",
            "1 C.B. 374",
            "11 A.F.T.R. (P-H) 1392",
            "3 U.S. Tax Cas. (CCH) 1043"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haggar Co. v. Helvering, Com'r of Internal Revenue",
          "cluster_id": 103266,
          "cite": [
            "308 U.S. 389",
            "60 S. Ct. 337",
            "84 L. Ed. 340",
            "1940 U.S. LEXIS 1218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis",
          "cluster_id": 225410,
          "cite": [
            "183 F.2d 201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mohamed Kamara v. Attorney General of the United States",
          "cluster_id": 791578,
          "cite": [
            "420 F.3d 202",
            "2005 U.S. App. LEXIS 18576",
            "2005 WL 2063873"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(101997) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDI1MTg0MDAwMDAmcz0yMzEwMjY2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28101997%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(101997)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTQmcz00NDMyNDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28101997%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(101997)",
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
    "complete_query": "cites:(101997)",
    "indexed_citing_opinions": 1231,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 101997,
        "count": 1231,
        "count_source": "search"
      }
    ],
    "citation_count": 1793,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/sorrells-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU5NTQ5NTEmcz00NTI1NDk5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28101997%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 101997,
        "cited_id": 85646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 85698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 88029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 88397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 88664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 89421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 90036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 91233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 93280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 93298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 95894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 96230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 96460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 96682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 97368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 98638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 98755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 98794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 99608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 99734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 100892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 100923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 101251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3415789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3581964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3672124,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3673731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3884966,
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
    "date_created": "2026-07-05T20:05:23Z",
    "date_modified": "2026-07-06T08:51:01Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:05:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:05:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:10:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:05:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Sorrells v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b504-6">
<span citation-index="1" class="star-pagination" label="438"> 
   *438
   </span>
  Mr. Chief Justice Hughes
 </author>
<p id="AGLB">
  delivered the opinion of the Court.
 </p>
<p id="b504-7">
  Defendant was indicted on two counts (1) for possessing and (2) for selling, on July 13, 1930, one-half gallon of whiskey in violation of the National Prohibition Act. He pleaded not guilty. Upon the trial he relied upon the defense of entrapment. The court refused to sustain the defense, denying a motion to direct a verdict in favor of defendant and also refusing to submit the issue of entrapment to the jury. The court ruled that “ as a matter of law ” there was no entrapment. Verdict of guilty followed, motions in arrest, and to set aside the verdict as contrary to the law and the evidence,' were denied, and defendant was sentenced to imprisonment for eighteen
  <span citation-index="1" class="star-pagination" label="439"> 
   *439
   </span>
  months. The Circuit Court of Appeals affirmed the judgment, 57 F. (2d) 973, and this Court granted a writ of certiorari limited to the question whether the evidence was sufficient to go to the jury upon the issue of entrapment.
 </p>
<p id="b505-5">
  The Government, while supporting the conclusion of the court below, also urges that the defense, if available, should have been pleaded in bar to further proceedings under the indictment and could not be raised under the plea of not guilty. This question of pleading appropriately awaits the consideration of the nature and grounds of the defense.
 </p>
<p id="b505-6">
  The substance of the testimony at the trial as to entrapment was as follows: For the Government, one Martin, a prohibition agent, testified that having resided for a time in Haywood County, North Carolina, where he posed as a tourist, he visited defendant’s home near Canton, on Sunday, July 13, 1930, accompanied by three residents of the county who knew the defendant well. He was introduced as a resident of Charlotte who was stopping for a time at Clyde. The witness ascertained that defendant was a veteran of the World War and a former member of the 30th Division A. E. F. Witness informed defendant that he was also an ex-service man and a former member of the same Division, which was true. Witness' asked defendant if he could get the witness some liquor and defendant stated that he did not have any. Later, there was a second request without result. One of those present, one Jones, was also an ex-service man and a former member of the 30th Division, and the conversation turned to the war experiences of the three. After this, witness asked defendant for a third time to get him some liquor, whereupon defendant left his home and after a few minutes came back with a half gallon of liquor for which the witness paid defendant five dollars. Martin also testified that he was “ the first and only person among those pres
  <span citation-index="1" class="star-pagination" label="440"> 
   *440
   </span>
  ent at the time who said anything about securing some liquor,” and that his purpose was to prosecute the defendant for procuring and selling it. The Government rested its case on Martin’s testimony.
 </p>
<p id="b506-6">
  Defendant called as witnesses the three persons who had accompanied the prohibition agent. In substance, they corroborated the latter’s story but with some additions. Jones, a railroad employee, testified that he had introduced the agent to the defendant “as a furniture dealer of Charlotte,” because the agent had so represented himself; that witness told defendant that the agent was “an old 30th Division man ” and the agent thereupon said to defendant that he “would like to get a half gallon of whiskey to take back to Charlotte to a friend of his that was in the furniture business with him,” and that defendant replied that he “ did not fool with whiskey ”; that the agent and his companions were at defendant’s home “ for probably an hour or an hour and a half and that during such time the agent asked the defendant three or four or probably five times to get him, the agent, some liquor.” Defendant said “ he would go and see if he could get a half gallon of liquor ” and he returned with it after an absence of “ between twenty and thirty minutes.” Jones added that at that time he had never heard of defendant being in the liquor business, that he and the defendant were “ two old buddies,” and that he believed “ one former war buddy would get liquor for another.”
 </p>
<p id="b506-7">
  Another witness, the timekeeper and assistant paymaster of the Champion Fibre Company at Canton, testified that defendant was an employee of that company and had been “ on his job continuously without missing a pay day since March, 1924.” Witness identified the time sheet showing this employment. This witness and three others who were neighbors of the defendant and had known him for many years testified to his good character.
 </p>
<p id="b507-5">
<span citation-index="1" class="star-pagination" label="441"> 
   *441
   </span>
  To rebut this testimony, the Government called three witnesses who testified that the defendant had the general reputation of a rum-runner. There was no evidence that the defendant had ever possessed or sold any intoxicating liquor prior to the transaction in question.
 </p>
<p id="b507-6">
  It is clear that the evidence was sufficient to warrant a finding that the act for which defendant was prosecuted was instigated by the prohibition agent, that it was the creature of his purpose, that defendant had no previous disposition to commit it but was an industrious, law-abiding citizen, and that the agent lured defendant, otherwise innocent, to its commission by repeated and persistent solicitation in which he succeeded by taking advantage of the sentiment aroused by reminiscences of their experiences as companions in arms in the World War. Such a gross abuse of authority given for the purpose of detecting and punishing crime, and not for the making of criminals, deserves the severest condemnation, but the question whether it precludes prosecution or affords a ground of defense, and, if so, upon what theory, has given rise to conflicting opinions.
 </p>
<p id="b507-7">
  It is well settled that the fact that officers or employees of the Government merely afford opportunities or facilities for the commission of the offense does not defeat the prosecution. Artifice and stratagem may be employed to catch those engaged in criminal enterprises.
  <em>
   Grimm
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94127"><a href="/opinion/94127/grimm-v-united-states/#610" aria-description="Citation for case: Grimm v. United States">156 U. S. 604, 610</a></span>;
  <em>
   Goode
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94294"><a href="/opinion/94294/goode-v-united-states/#669" aria-description="Citation for case: Goode v. United States">159 U. S. 663, 669</a></span>;
  <em>
   Rosen
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417701"><a href="/opinion/94359/rosen-v-united-states/#42" aria-description="Citation for case: Rosen v. United States">161 U. S. 29, 42</a></span>;
  <em>
   Andrews v. United States,
  </em>
  <span class="citation" data-id="94440"><a href="/opinion/94440/andrews-v-united-states/#423" aria-description="Citation for case: Andrews v. United States">162 U. S. 420, 423</a></span>;
  <em>
   Price
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94604"><a href="/opinion/94604/price-v-united-states/#315" aria-description="Citation for case: Price v. United States">165 U. S. 311, 315</a></span>;
  <em>
   Bates
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8122456"><a href="/opinion/8160801/bates-v-united-states/#94" aria-description="Citation for case: Bates v. United States">10 Fed. 92, 94</a></span>, note, p. 97.
  <em>
   United States
  </em>
  v.
  <em>
   Reisenweber,
  </em>
  <span class="citation" data-id="8829953"><a href="/opinion/8844712/united-states-v-reisenweber/#526" aria-description="Citation for case: United States v. Reisenweber">288 Fed. 520, 526</a></span>;
  <em>
   Aultman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8830418"><a href="/opinion/8845169/aultman-v-united-states/" aria-description="Citation for case: Aultman v. United States">289 Fed. 251</a></span>.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The appropriate object of this permitted activity, frequently essential to the enforcement of the law, is to
  <span citation-index="1" class="star-pagination" label="442"> 
   *442
   </span>
  reveal the criminal design; to expose the illicit traffic, the prohibited publication, the fraudulent use of the mails, the illegal conspiracy, or other offenses, and thus to disclose the would-be violators of the law. A different question is presented when the criminal design originates with the officials of the Government, and they implant in the mind of an innocent person the disposition to commit the alleged offense and induce its commission in order that they may prosecute.
 </p>
<p id="b508-5">
  The Circuit Court of Appeals reached the conclusion that the defense of entrapment can be maintained only where, as a result of inducement, the accused is placed in the attitude of having committed ,a crime which he did not intend to commit, or where, by reason of the consent implied in the inducement, no crime has in fact been committed. 57 F. (2d) p. 974. As illustrating the first class, reference is made to the case of a sale of liquor to an Indian who was disguised so as to mislead the accused as to his identity.
  <em>
   United States
  </em>
  v.
  <em>
   Healy,
  </em>
  <span class="citation" data-id="8786735"><a href="/opinion/8802548/united-states-v-healy/" aria-description="Citation for case: United States v. Healy">202 Fed. 349</a></span>;
  <em>
   Voves
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8807195"><a href="/opinion/8822500/voves-v-united-states/" aria-description="Citation for case: Voves v. United States">249 Fed. 191</a></span>. In the second class are found cases such as those of larceny or rape where want of consent is an element of the crime.
  <em>
   Regina
  </em>
  v.
  <em>
   Fletcher,
  </em>
  8 Cox C. C. 131;
  <em>
   Rex
  </em>
  v.
  <em>
   McDaniel,
  </em>
  Fost. 121, 127, 128;
  <em>
   Connor
  </em>
  v.
  <em>
   People,
  </em>
  <span class="citation" data-id="6562355"><a href="/opinion/6683158/connor-v-people/" aria-description="Citation for case: Connor v. People">18 Colo. 373</a></span> ; <span class="citation no-link">33 Pac. 159</span>;
  <em>
   Williams
  </em>
  v.
  <em>
   Georgia,
  </em>
  <span class="citation" data-id="5557787"><a href="/opinion/5707869/williams-v-state/" aria-description="Citation for case: Williams v. State">55 Ga. 391</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Whittier,
  </em>
  <span class="citation" data-id="8687089"><a href="/opinion/8703909/united-states-v-whittier/" aria-description="Citation for case: United States v. Whittier">5 Dill. 35</a></span>;
  <em>
   State
  </em>
  v.
  <em>
   Adams,
  </em>
  <span class="citation" data-id="3672124"><a href="/opinion/3925541/state-v-adams/" aria-description="Citation for case: State v. . Adams">115 N. C. 775</a></span>; <span class="citation" data-id="3672124"><a href="/opinion/3925541/state-v-adams/" aria-description="Citation for case: State v. . Adams">20 S. E. 722</a></span>. There may also be.physical conditions which are essential to the offense and which do not exist in the case of a trap, as, for example, in the case of a prosecution for burglary where it appears that by reason of the trap there is no breaking.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
<em>
   Rex
  </em>
  v.
  <em>
   Egginton,
  </em>
  2 Leach C. C. 913;
  <em>
   Regina
  </em>
  v.
  <em>
   Johnson,
  </em>
  Car. &amp; Mar. 218;
  <em>
   Saunders
  </em>
  v.
  <em>
   People,
  </em>
  <span class="citation" data-id="7928801"><a href="/opinion/7976263/saunders-v-people/" aria-description="Citation for case: Saunders v. People">38 Mich 218</a></span>;
  <em>
   People
  </em>
  v.
  <em>
   McCord,
  </em>
  <span class="citation" data-id="7934195"><a href="/opinion/7981425/people-v-mccord/" aria-description="Citation for case: People v. McCord">76 Mich. 200</a></span>; <span class="citation" data-id="7934195"><a href="/opinion/7981425/people-v-mccord/" aria-description="Citation for case: People v. McCord">42 N. W. 1106</a></span>;
  <em>
   Allen
  </em>
  v.
  <em>
   State,
  </em>
  <span class="citation" data-id="6507278"><a href="/opinion/6630823/allen-v-state/" aria-description="Citation for case: Allen v. State">40 Ala. 334</a></span>;
  <em>
   Love
  </em>
  v.
  <em>
   People,
  </em>
  160 Ill.
  <span citation-index="1" class="star-pagination" label="443"> 
   *443
   </span>
  501; <span class="citation" data-id="6966669"><a href="/opinion/7062620/love-v-people/" aria-description="Citation for case: Love v. People">43 N. E. 710</a></span>. But these decisions .applying accepted principles to particular offenses, do not reach, much less determine, the present question. Neither in reasoning nor in effect do they prescribe limits for the doctrine of entrapment.
 </p>
<p id="ACZY">
  While this Court has not spoken on the precise question (see
  <em>
   Casey
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418615"><a href="/opinion/101251/casey-v-united-states/#419" aria-description="Citation for case: Casey v. United States">276 U. S. 413, 419</a></span>, 423
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  ), the weight of authority in the lower federal courts is decidedly in favor of the view that in such case as the one before us the defense of entrapment is available. The Government concedes that its contention, in supporting the ruling of the Circuit Court of Appeals, is opposed by decisions in all the other Circuits except the Tenth Circuit, and no decision in that Circuit suggesting a different view has been brought to Our attention. See
  <em>
   Capuano
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 1st), 9 F. (2d) 41, 42;
  <em>
   United States
  </em>
  v.
  <em>
   Lynch
  </em>
  (S. D. N. Y., Hough, J.), <span class="citation" data-id="8811194"><a href="/opinion/8826376/united-states-v-lynch/#984" aria-description="Citation for case: United States v. Lynch">256 Fed. 983, 984</a></span>;
  <em>
   Lucadamo
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 2d), <span class="citation" data-id="8825386"><a href="/opinion/8840238/lucadamo-v-united-states/#657" aria-description="Citation for case: Lucadamo v. United States">280 Fed. 653, 657, 658</a></span>;
  <em>
   Zucker
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 3d), <span class="citation" data-id="8829829"><a href="/opinion/8844592/zucker-v-united-states/#15" aria-description="Citation for case: Zucker v. United States">288 Fed. 12, 15</a></span>;
  <em>
   Gargano
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 5th), 24 F. (2d) 625, 626;
  <em>
   Cermak
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 6th), 4 F. (2d) 99;
  <em>
   O’Brien
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 7th), 51 F. (2d) 674, 679, 680;
  <em>
   Butts
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 8th), <span class="citation" data-id="8820799"><a href="/opinion/8835759/butts-v-united-states/#38" aria-description="Citation for case: Butts v. United States">273 Fed. 35, 38</a></span>;
  <em>
   Woo Wai
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 9th), <span class="citation" data-id="8795796"><a href="/opinion/8811409/woo-wai-v-united-states/" aria-description="Citation for case: Woo Wai v. United States">223 Fed. 412</a></span>. And the Circuit Court of Appeals of the Fourth Circuit, in the instant case, was able to reach its conclusion only by declining to follow the rule which it had laid down in its earlier decision in
  <em>
   Newman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9335893"><a href="/opinion/9340549/newman-v-states/#131" aria-description="Citation for case: Newman v. States">299 Fed. 128, 131</a></span>.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  It
  <span citation-index="1" class="star-pagination" label="444"> 
   *444
   </span>
  should be added that in many cases in.which the evidence has been found insufficient to support the defense of entrapment the availability of that defense, on a showing of such facts as are present here, has been recognized.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  The federal courts have generally approved the statement of Circuit Judge Sanborn in the leading case of
  <em>
   Butts
  </em>
  v.
  <em>
   United States, supra,
  </em>
  as follows: “ The first duties of the officers of the law are to prevent, not to punish crime. It is not their duty to incite to and create crime for the sole purpose of prosecuting and punishing it. Here the evidence strongly tends to prove, if it does not conclusively do so, that their first and chief endeavor was to cause, to create, crime in order to punish it, and it is unconscionable, contrary to public policy, and to the established law of the land to punish a man for the Commission of an offense of the like of which he had never been guilty, either in thought or in deed, and evidently never would have been guilty of if the officers .¡of the law had not inspired, incited, persuaded, and lured him to attempt to com
  <span citation-index="1" class="star-pagination" label="445"> 
   *445
   </span>
  xnit it.” The judgment in that case was reversed because of the * fatal error ’ of the trial court in refusing to instruct the jury to that effect. In
  <em>
   Newman
  </em>
  v.
  <em>
   United States, supra,
  </em>
  the applicable principle was thus stated by Circuit Judge Woods: “It is well settled that decoys may be used to entrap criminals, and to present opportunity to one intending or willing to commit crime. But decoys are not permissible to ensnare the innocent and law-abiding into the commission of crime. When the criminal design originates, not with the accused, but is conceived in the mind of the government officers, and the accused is by persuasion, deceitful representation, or inducement lured into the commission of a criminal act, the government is estopped by sound public policy from prosecution therefor.” These quotations sufficiently indicate the grounds of the decisions above cited.
 </p>
<p id="b511-6">
  The validity of the principle as thus stated and applied is challenged both upon theoretical and practical grounds. The argument, from the standpoint of principle, is that the court is called upon to try the accused for a particular offense which is defined by statute and that, if the evidence shows that this offense has knowingly been committed, it matters not that its commission was induced by officers of the Government in the manner and circumstances assumed. It is said that where one intentionally does an act in circumstances known to him, and the particular conduct is forbidden by the law in those circumstances, he intentionally breaks the law in the only sense in which the law considers intent.
  <em>
   Ellis
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418092"><a href="/opinion/96682/ellis-v-united-states/#257" aria-description="Citation for case: Ellis v. United States">206 U. S. 246, 257</a></span>. Moreover, that as the statute is designed to redress ,a public wrong, and not a private injury, there is no ground for holding the Government estopped by the conduct of its officers from prosecuting the offender. To the suggestion of public policy the objectors answer that the legislature, acting within its constitutional au
  <span citation-index="1" class="star-pagination" label="446"> 
   *446
   </span>
  thority, is the arbiter of public
  <em>
   policy
  </em>
<a class="footnote" href="#fn6" id="fn6_ref">
<em>
    6
   </em>
</a>
<em>
</em>
  and that, where conduct is expressly forbidden and penalized by a valid statute, the courts are not at liberty to disregard the law and to bar a prosecution for its violation because they are of the opinion that the crime has been instigated by government officials.
 </p>
<p id="b512-5">
  It is manifest that these arguments rest entirely upon the letter of the statute. They take no account of the fact that its application in the circumstances under consideration is foreign to its purpose; that such an application is so shocking to the sense of justice that it has been urged that it is the duty of the court to stop the prosecution in the interest of the Government itself, to protect it from the illegal conduct of its officers and to preserve the purity of its courts.
  <em>
   Casey
  </em>
  v.
  <em>
   United States, supra.
  </em>
  But can an application of the statute having such an effect— creating a situation so contrary to the purpose of the law and so inconsistent with its proper enforcement as to invoke such a challenge — fairly be deemed to be within its intendment?
 </p>
<p id="b512-6">
  Literal interpretation of statutes at the expense of the reason of the law and producing absurd consequences or flagrant injustice has frequently been condemned. In
  <em>
   United States
  </em>
  v.
  <em>
   Palmer,
  </em>
  <span class="citation" data-id="8373757"><a href="/opinion/8403414/united-states-v-palmer/#631" aria-description="Citation for case: United States v. Palmer">3 Wheat. 610, 631</a></span>, Chief Justice Marshall, in construing the Act of' Congress of April 30, 1790, §8(1 Stat. 113) relating to robbery on the high seas, found that the words “ any person or persons ” were “ broad enough to comprehend every human being,” but he concluded that “ general words must not only be limited to- cases within the jurisdiction of the state, but also to those objects to which the legislature intended to apply them.” In
  <em>
   United States
  </em>
  v.
  <em>
   Kirby,
  </em>
  <span class="citation" data-id="88029"><a href="/opinion/88029/united-states-v-kirby/" aria-description="Citation for case: United States v. Kirby">7 Wall. 482</a></span>, the case arose under the Act of Congress of March 3, 1825
  <span citation-index="1" class="star-pagination" label="447"> 
   *447
   </span>
  (<span class="citation no-link">4 Stat. 104</span>) providing for the conviction of any person who “ shall knowingly and willfully obstruct or retard the passage of the mail, or of any driver or carrier . . . carrying the same.” Considering the purpose of the statute, the Court held that it had no application to the obstruction or retarding of the passage of the mail or of its carrier by reason of the arrest of the carrier upon a warrant issued by a state court. The Court said: “All laws should receive a sensible construction. General terms should be so limited in their application as not to lead to injustice, oppression, or an absurd consequence. It will always, therefore, be presumed that the legislature intended exceptions to its language which would avoid results of this character. The reason of the law in such cases should prevail over its letter.” And the Court supported this conclusion by reference to the classical illustrations found in Puffendorf and Plowden.
  <em>
   Id.,
  </em>
  pp. 486, 487.
 </p>
<p id="b513-4">
  Applying this principle in
  <em>
   Lau Ow Bew
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="93298"><a href="/opinion/93298/lau-ow-bew-v-united-states/" aria-description="Citation for case: Lau Ow Bew v. United States">144 U. S. 47</a></span>, the Court decided that a statute requiring the permission of the Chinese government, and identification by certificate, of “ every Chinese person other than a laborer,” entitled by treaty or the act of Congress to come within the United States, did not apply to Chinese merchants already domiciled in the United States, who had left the country for temporary purposes,
  <em>
   animo revertendi,
  </em>
  and sought to reenter it on their return to their business and their homes. And in
  <em>
   United States
  </em>
  v.
  <em>
   Katz,
  </em>
  <span class="citation" data-id="100892"><a href="/opinion/100892/united-states-v-katz/#362" aria-description="Citation for case: United States v. Katz">271 U. S. 354, 362</a></span>, construing § 10 of the National Prohibition Act so as to avoid an unreasonable application of its words, if taken literally, the Court again declared that “ general terms descriptive of a class of persons made subject to a criminal statute may and should be limited where the literal application of the statute would lead to extreme or absurd results, and where the legislative pur
  <span citation-index="1" class="star-pagination" label="448"> 
   *448
   </span>
  pose gathered from the whole Act would be satisfied by a more limited interpretation.”
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  See, to the same effect,
  <em>
   Heydenfeldt
  </em>
  v.
  <em>
   Daney Gold Mining Co.,
  </em>
  <span class="citation" data-id="89421"><a href="/opinion/89421/heydenfeldt-v-daney-gold-and-silver-mining-co/#638" aria-description="Citation for case: Heydenfeldt v. Daney Gold and Silver Mining Co.">93 U. S. 634, 638</a></span>;
  <em>
   Carlisle
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="88664"><a href="/opinion/88664/carlisle-v-united-states/#153" aria-description="Citation for case: Carlisle v. United States">16 Wall. 147, 153</a></span>;
  <em>
   Oates
  </em>
  v.
  <em>
   National Bank,
  </em>
  <span class="citation" data-id="90036"><a href="/opinion/90036/oates-v-national-bank/" aria-description="Citation for case: Oates v. National Bank">100 U. S. 239</a></span>;
  <em>
   Chew Heong
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417392"><a href="/opinion/91233/chew-heong-v-united-states/#555" aria-description="Citation for case: Chew Heong v. United States">112 U. S. 536, 555</a></span>;
  <em>
   Holy Trinity Church
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="93280"><a href="/opinion/93280/church-of-the-holy-trinity-v-united-states/#459" aria-description="Citation for case: Church of the Holy Trinity v. United States">143 U. S. 457, 459-462</a></span>;
  <em>
   Hawaii
  </em>
  v.
  <em>
   Mankichi,
  </em>
  <span class="citation" data-id="9417915"><a href="/opinion/95894/hawaii-v-mankichi/#212" aria-description="Citation for case: Hawaii v. Mankichi">190 U. S. 197, 212-214</a></span>;
  <em>
   Jacobson
  </em>
  v.
  <em>
   Massachusetts,
  </em>
  <span class="citation" data-id="96230"><a href="/opinion/96230/jacobson-v-massachusetts/#39" aria-description="Citation for case: Jacobson v. Massachusetts">197 U. S. 11, 39</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Jin Fuey Moy,
  </em>
  <span class="citation" data-id="98755"><a href="/opinion/98755/united-states-v-jin-fuey-moy/#402" aria-description="Citation for case: United States v. Jin Fuey Moy">241 U. S. 394, 402</a></span>;
  <em>
   Baender
  </em>
  v.
  <em>
   Barnett,
  </em>
  <span class="citation" data-id="99734"><a href="/opinion/99734/baender-v-barnett/#226" aria-description="Citation for case: Baender v. Barnett">255 U. S. 224, 226</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Chemical Foundation,
  </em>
  <span class="citation" data-id="100923"><a href="/opinion/100923/united-states-v-chemical-foundation-inc/#18" aria-description="Citation for case: United States v. Chemical Foundation, Inc.">272 U. S. 1, 18</a></span>.
 </p>
<p id="b514-6">
  We think that this established principle of construction is applicable here. We are unable to conclude that it was the intention of the Congress in enacting this statute that its processes of detection and enforcement should be abused by the instigation by government officials of an act on the part of persons otherwise innocent in order to lure them to its commission and to punish them. We are not forced by the letter to do violence to the spirit and purpose of the statute. This, we think, has been the underlying and controlling thought in the suggestions in judicial opinions that the Government in such a case is estopped to prosecute or that the courts should bar the prosecution. If the requirements of the highest public policy in the maintenance of the integrity
  <span citation-index="1" class="star-pagination" label="449"> 
   *449
   </span>
  of administration would preclude the enforcement of the statute in such circumstances as are present here, the same considerations justify the conclusion that the case lies outside the purview of the Act and that its general words should not be construed to demand a proceeding at once inconsistent with that policy and abhorrent to the sense of justice. This view does not derogate from the authority of the court to deal appropriately with abuses of its process and it obviates the objection to the exercise by the court of a dispensing power in forbidding the prosecution of one who is charged with conduct assumed to fall within the statute.
 </p>
<p id="b515-6">
  We are unable to approve the view that the court, although treating the statute as applicable despite the entrapment, and the defendant as guilty, has authority to grant immunity, .or to adopt a procedure to that end. It is the function of the court to construe the statute, not to defeat it as construed. Clemency is the function of the Executive.
  <em>
   Ex parte United States,
  </em>
  <span class="citation" data-id="98794"><a href="/opinion/98794/ex-parte-united-states/#42" aria-description="Citation for case: Ex Parte United States">242 U. S. 27, 42</a></span>. In that case, this Court decisively denied such authority to free guilty defendants, in holding that the court had no power to suspend sentences indefinitely. The Court, speaking by Chief Justice White, said — “ if it be that the plain legislative command fixing a specific punishment for crime is subject to be permanently set aside by an implied judicial power upon considerations extraneous to the legality of the conviction, it would seem necessarily to follow that there could be likewise implied a discretionary authority to permanently refuse to try a criminal charge because of the conclusion that a particular act made criminal by law ought not to be treated as criminal. And thus it would come to pass that the possession by the judicial department of power to permanently refuse to enforce a law would result in the destruction of the conceded powers of the other departments and hence leave no law to be enforced.” And while recognizing the hu
  <span citation-index="1" class="star-pagination" label="450"> 
   *450
   </span>
  mane considerations which had led judges to adopt the practice of suspending sentences indefinitely in certain cases, the Court found no ground for approving the practice “ since its exercise in the very ^nature of things amounts to a refusal by the judicial power to perform a duty resting upon it and, as a consequence thereof, to an interference with both the legislative and executive authority as fixed by the Constitution.”
  <em>
   Id.
  </em>
  pp. 51, 52. Where defendant has been duly indicted for an offense found to be within the statute, and the proper authorities seek to proceed with the prosecution, the court cannot refuse to try the case in the constitutional method because it desires to let the defendant go free.
 </p>
<p id="b516-5">
  Suggested analogies from procedure in civil cases are not helpful. When courts of law refuse to sustain alleged causes of action which grow out of illegal schemes, the applicable law itself denies the right to recover. Where courts of equity refuse equitable relief because complainants come with unclean hands, they are administering the principles of equitable jurisprudence governing equitable rights. But in a criminal prosecution, the statute defining the offense is necessarily the law of the case.
 </p>
<p id="b516-6">
  To construe statutes so as to .avoid absurd or glaringly unjust results, foreign to the legislative purpose, is, as we have seen, a traditional and appropriate function of the courts. Judicial nullification of statutes, admittedly valid and applicable, has, happily, no place in our system. The Congress by legislation can always, if it desires, alter the effect of judicial construction of statutes. We conceive it to be our duty to construe the statute here in question reasonably, and we hold that it is beyond our prerogative to give the statute an unreasonable construction, confessedly contrary to public policy, and then to decline to enforce it.
 </p>
<p id="b516-7">
  The conclusion we have reached upon these grounds carries its own limitation. We are dealing with a statu
  <span citation-index="1" class="star-pagination" label="451"> 
   *451
   </span>
  tory prohibition and we are simply concerned to ascertain whether in the light of a plain public policy and of the proper administration of justice, conduct induced as stated should be deemed to be within that prohibition. We have no occasion to consider hypothetical cases of crimes so heinous or revolting that the applicable law would admit of no exceptions. No such situation is presented here. The question in each case must be determined by the scope of the law considered in the light of what may fairly be deemed to be its object.
 </p>
<p id="b517-4">
  Objections to the defense of entrapment are also urged upon practical grounds. But considerations of mere convenience must yield to the essential demands of justice. The argument is pressed that if the defense is available it will lead to the introduction of issues of a collateral character relating to the activities of the officials of the- Government and to the conduct and purposes of the defendant previous to the alleged offense. For the defense of entrapment is not simply that the particular act was committed at the instance of government officials. That is often the case where the proper action of these officials leads to the revelation of criminal enterprises.
  <em>
   Grimm
  </em>
  v.
  <em>
   United States, supra.
  </em>
  The predisposition and criminal design of the defendant are relevant. But the issues raised and the evidence adduced must be pertinent to the controlling question whether the defendant is a person otherwise innocent whom the Government is seeking to punish for an alleged offense which is the product of the creative activity of its own officials. If that is the fact, common justice requires that the accused be permitted to prove it. The Government in such a case is in no position to object to evidence of the activities of its representatives in relation to the accused, and if the defendant seeks acquittal by reason of entrapment he cannot complain of an appropriate and searching inquiry into his own conduct and predisposition as bearing upon that issue. If in con
  <span citation-index="1" class="star-pagination" label="452"> 
   *452
   </span>
  sequence he suffers a disadvantage, he has brought it upon himself by reason of the nature of the defense.
 </p>
<p id="b518-5">
  What has been said indicates the answer to the contention of the Government that the defense of entrapment must be pleaded in bar to further proceedings under the indictment and cannot be raised under the plea of not guilty. This contention presupposes that the defense is available to the accused and relates only to the manner in which it shall be presented. The Government considers the defense as analogous to a plea of pardon or of
  <em>
   autrefois convict
  </em>
  or
  <em>
   autrefois acquit.
  </em>
  It is assumed that the accused is not denying his guilt but is setting up special facts in bar upon which he relies regardless of his guilt or innocence of the crime charged. This, as we have seen, is a misconception. The defense is available, not in the view that the accused though guilty may go free, but that the Government cannot be permitted to contend that he is guilty of a crime where the government officials are the instigators of his conduct. The federal courts in sustaining the defense in such circumstances have proceeded in the view that the defendant is not guilty. The practice of requiring a plea in bar has not obtained. Fundamentally, the question is whether the defense, if the facts bear it otit, takes the case out of the purview of the statute because it cannot be supposed that the Congress intended that the letter of its enactment should be used to support such a gross perversion of its purpose.
 </p>
<p id="b518-6">
  We are of the opinion that upon the evidence produced in the instant case the defense of entrapment was available and that the trial court was in error in holding that as a matter of law there was no entrapment and in refusing to submit the issue to the jury.
 </p>
<p id="b518-7">
  The judgment is reversed and the cause is remanded for further proceedings in conformity with this opinion.
 </p>
<p id="b518-8">
<em>
   Judgment reversed.
  </em>
</p>
<author id="b519-3">
<span citation-index="1" class="star-pagination" label="453"> 
   *453
   </span>
  Mr. Justice McReynolds
 </author>
<p id="AsVD">
  is of the opinion that the judgment below should be affirmed.
 </p>
<p id="b519-4">
  Separate opinion of
 </p>
<author id="AUGg">
  Mr. Justice Roberts.
 </author>
<p id="b519-5">
  The facts set forth in the court’s opinion establish that a prohibition enforcement officer instigated the commission of the crime charged. The courts below held that the showing was insufficient, as matter of law, to sustain the claim of entrapment, and that the jury were properly instructed to ignore that defense in their consideration of the case. A conviction resulted. The Government maintains that the issue of entrapment is not triable under the plea of not guilty, but should be raised by plea in bar or be adjudicated in some manner by the court rather than by the jury, and as the trial court properly decided the question, the record presents ho reversible error. I think, however, the judgment should be reversed, but for reasons and upon grounds other than those stated in the opinion of the court.
 </p>
<p id="b519-6">
  Of late the term “ entrapment ” has been adopted by the courts to signify instigation of crime by officers of government. The cases in which such incitement has been recognized as a defense have grown to an amazing total.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The increasing frequency of the assertion that the defendant was entrapped is doubtless due to the creation by statute of many new crimes, (e. g., sale and transportation of liquor and narcotics) and the correlative establishment of special enforcement bodies for the detection and punishment of offenders. The efforts of members of these forces to obtain arrests and convictions have too often been marked by reprehensible methods.
 </p>
<p id="b519-7">
  Society is at war with the criminal classes, and courts have uniformly held that in waging this warfare the forces of prevention and detection may use traps, decoys, and
  <span citation-index="1" class="star-pagination" label="454"> 
   *454
   </span>
  deception to obtain evidence of the commission of crime. Resort to such means does not render an indictment thereafter found a nullity nor call for the exclusion of evidence so procured.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  3But the defense here asserted involves more than obtaining evidence by artifice or deception. Entrapment is the conception and planning of an offense by an officer, and his procurement of its commission by one who would not have perpetrated it except for the trickery, persuasion, or fraud of the officer. Federal and state courts have held that substantial proof of entrapment as thus defined calls for the submission of the issue to the jury and warrants an acquittal. The reasons assigned in support of this procedure have not been uniform. Thus it has been held that the acts of its officers estop the government to prove the offense. The result has also been justified by the mere statement of the rule that where entrapment is proved the defendant is not guilty of the crime charged. Often the defense has been permitted upon grounds of public policy, which the courts formulate by saying they will not permit their process to be used in aid of a scheme for the actual creation of a crime by those whose duty is to deter its commission.
 </p>
<p id="b520-5">
  This court has adverted to the doctrine,
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  but has not heretofore had occasion to determine its validity, the basis on which it should rest, or the procedure to be followed when it is involved. The present case affords the opportunity to settle these matters as respects the administration of the federal criminal law.
 </p>
<p id="b520-6">
  There is common agreement that where a law officer envisages a crime, plans it, and activates its commission by one not theretofore intending its perpetration, for the sole purpose of obtaining a victim through indictment, conviction and sentence, the consummation of so revolting a plan
  <span citation-index="1" class="star-pagination" label="455"> 
   *455
   </span>
  ought not to be permitted by any self-respecting tribunal. Equally true is this whether the offense is one at common law or merely a creature of statute. Public policy forbids such sacrifice of decency. The enforcement of this policy calls upon the court, in every instance where alleged entrapment of a defendant is brought to its notice, to ascertain the facts, to appraise their effect upon the administration of justice, and to make such order with respect to the further prosecution of the cause as the circumstances require.
 </p>
<p id="b521-6">
  This view calls for no distinction between crimes
  <em>
   mala in se
  </em>
  and statutory offenses of lesser gravity; requires no statutory construction, and attributes no merit to ,a guilty defendant; but frankly recognizes the true foundation of the doctrine in the public policy which protects the purity of government and its processes. Always the courts refuse their aid in civil cases to the perpetration and consummation of an illegal scheme. Invariably they hold a civil action must be abated if its basis is violation of the decencies of life, disregard of the rules, statutory or common law, which formulate the ethics of men’s relations to each other. Neither courts of equity nor those administering legal remedies tolerate the use of their process to consummate a wrong.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  The doctrine of entrapment in criminal law is the analogue of the same rule applied in civil proceedings. And this is the real basis of the decisions approving the defense of entrapment, though in statement the rule is cloaked under a declaration that the government is estopped or the defendant has not been proved guilty.
 </p>
<p id="b521-7">
  A new method of rationalizing the defense is now asserted. ' This is to construe the act creating the offense by
  <span citation-index="1" class="star-pagination" label="456"> 
   *456
   </span>
  reading in a condition or proviso that if the offender shall have been entrapped into crime the law shall not apply to him. So, it is said, the true intent of the legislature will be effectuated. This seems a strained and unwarranted construction of the statute; and amounts, in fact, to judicial amendment. It is not merely broad construction, but addition of an element not contained in the legislation. The constituents of the offense are enumerated by the statute. If we assume the defendant to have been a person of upright purposes, law abiding, and not prone to crime, — induced against his own will and better judgment to become the instrument of the criminal purpose of another, — his action, so induced, none the less falls within the letter of the law and renders him amenable to its penalties.- Viewed in its true light entrapment is not a defense to him; his act, coupled with his intent to do the act, brings him within the definition of the law; he has no rights or equities by reason of his entrapment. It cannot truly be said that entrapment excuses him or contradicts the obvious fact of his commission of the offense. We cannot escape this conclusion by saying that where need arises the statute will be read as containing an implicit condition that it shall not apply in the case of entrapment. The effect of such construction is to add to the words of the statute a proviso which gives to the defendant a double defense under his plea of not guilty, namely, (a) that what he did does not fall within the definition of the statute, and (b) entrapment. This amounts to saying that one who with full intent commits the act defined by law as an offense, is nevertheless by virtue of the unspoken and implied mandate of the statute to be adjudged not guilty by reason of someone's else improper conduct. It is merely to adopt a form of words to justify action which ought to be based on the inherent right of the court not to be made the instrument of wrong.
 </p>
<p id="b522-5">
  It is said that this case warrants such a construction of the applicable act, but that the question whether a similar
  <span citation-index="1" class="star-pagination" label="457"> 
   *457
   </span>
  construction will be required in the case of other or more serious crimes is not before the court. Thus no guide or rule is announced as to when a statute shall be read as excluding a case of entrapment; and no principle of statutory construction is suggested which would enable us to say that it is excluded by some statutes and not by others.
 </p>
<p id="b523-6">
  The doctrine rests, rather, on a fundamental rule of public policy. The protection of its own functions and the preservation of the purity of its own temple belongs only to the court. It is the province of the court and of the court alone to protect itself and the government from such prostitution of the criminal law. The violation of the principles of justice by the entrapment of the unwary into crime should be dealt with by the court no matter by whom or at what stage of the proceedings the facts are brought to its attention.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  Quite properly it may discharge the prisoner upon a writ of
  <em>
   habeas
  </em>
  corpus.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  Equally well may it quash the indictment or entertain and try a plea in bar.6
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  But its powers do not end there. Proof of entrapment, at any stage of the case, requires the court to stop the prosecution, direct that the indictment be quashed, and the defendant set at liberty.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  If in doubt as to the facts it may submit the issue of entrapment to a jury for advice. But whatever may be the finding upon such submission the power and the duty to act remain with the court and not with the jury.
 </p>
<p id="b524-4">
<span citation-index="1" class="star-pagination" label="458"> 
   *458
   </span>
  Such action does not grant immunity to a guilty defendant. But to afford him as his right a defense founded not on the statute, but on the court’s view of what the legislature is assumed to have meant, is to grant him unwarranted immunity. If the court may construe an act of Congress so as to create a defense for one whose guilt the act pronounces, no reason is apparent why the same statute may not be modified by a similar process of construction as to the penalty prescribed. But it is settled that this may not be done.
  <em>
   Ex parte United States,
  </em>
  <span class="citation" data-id="98794"><a href="/opinion/98794/ex-parte-united-states/" aria-description="Citation for case: Ex Parte United States">242 U. S. 27</a></span>. The broad distinction between the refusal to lend the aid of the court’s own processes to the consummation of a wrong and the attempt to modify by judicial legislation the mandate of the statute as to the punishment to be imposed after trial and conviction is so obvious as not to need discussion.
 </p>
<p id="b524-5">
  Recognition of the defense of entrapment as belonging to the defendant and as raising an issue for decision by the jury called to try him upon plea of the general issue, results in the trial of a false issue wholly outside the true rule which should be applied by the courts. It has been generally held, where the defendant has proved an entrapment, it is permissible for the government to show in rebuttal that the officer guilty of incitement of the crime had reasonable cause to believe the defendant was a person disposed to commit the offense. This procedure is approved by the opinion of the court. The proof received in rebuttal usually amounts to no more than that the defendant had a bad reputation, or that he had been previously convicted. Is the statute upon which the indictment is based to be further construed as removing the defense of entrapment from such a defendant?
 </p>
<p id="b524-6">
  Whatever may be the demerits of the defendant or his previous infractions of law these will not justify the instigation and creation of a new crime, as a means to reach him and punish him for his past misdemeanors. He has committed the crime in question, but, by supposition,
  <span citation-index="1" class="star-pagination" label="459"> 
   *459
   </span>
  only because of instigation and inducement by a government officer. To say that such conduct by an official of government is condoned and rendered innocuous by the fact that the defendant had a bad reputation or had previously transgressed is wholly to disregard the reason for refusing the processes of the court to consummate an abhorrent transaction. It is to discard the basis of the doctrine and in effect to weigh the equities as between the government and the defendant when there are in truth no equities belonging to the latter, and when the rule of action cannot rest on any estimate of the good which may come of the conviction of the offender by foul means. The accepted procedure, in effect, pivots conviction in such cases, not on the commission of the crime charged, but on the prior reputation or some former act or acts of the defendant not mentioned in the indictment.
 </p>
<p id="b525-4">
  The applicable principle is that courts must be closed to the trial of a crime instigated by the government’s own agents. No other issue, no comparison of equities as between the guilty official and the guilty defendant, has any place in the enforcement of this overruling principle of public policy.
 </p>
<p id="b525-5">
  The judgment should be reversed and the cause remanded to the District Court with instructions to quash the indictment and discharge the defendant.
 </p>
<judges id="b525-6">
  Mr. Justice Brandéis and Mr. Justice Stone concur in this opinion.
 </judges>















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b507-8">
   See, also,
   <em>
    Regina
   </em>
   v.
   <em>
    <span class="citation" data-id="5557787"><a href="/opinion/5707869/williams-v-state/" aria-description="Citation for case: Williams v. State">Williams</a></span>,
   </em>
   1 Car. &amp; K. 195;
   <em>
    People
   </em>
   v.
   <em>
    Mills,
   </em>
   178 N Y. 274; <span class="citation" data-id="3581964"><a href="/opinion/3600589/people-v-mills/" aria-description="Citation for case: People v. . Mills">70 N. E. 786</a></span>;
   <em>
    People
   </em>
   v.
   <em>
    Ficke,
   </em>
   <span class="citation" data-id="3415789"><a href="/opinion/3419370/the-people-v-ficke/" aria-description="Citation for case: The People v. Ficke">343 Ill. 367</a></span>; <span class="citation" data-id="3415789"><a href="/opinion/3419370/the-people-v-ficke/" aria-description="Citation for case: The People v. Ficke">175 N. E. 543</a></span>.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b508-6">
   See note of Francis Wharton to
   <em>
    Bates
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8122456"><a href="/opinion/8160801/bates-v-united-states/" aria-description="Citation for case: Bates v. United States">10 Fed. 97</a></span>-99.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b509-7">
   Compare
   <em>
    Olmstead
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b509-8">
   See, also,
   <em>
    United States
   </em>
   v.
   <em>
    Adams,
   </em>
   <span class="citation" data-id="8848571"><a href="/opinion/8863027/united-states-v-adams/" aria-description="Citation for case: United States v. Adams">59 Fed. 674</a></span>;
   <em>
    Sam Yick
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8802472"><a href="/opinion/8817917/yick-v-united-states/#65" aria-description="Citation for case: Yick v. United States">240 Fed. 60, 65</a></span>;
   <em>
    United States
   </em>
   v.
   <em>
    Echols,
   </em>
   <span class="citation" data-id="8809555"><a href="/opinion/8824775/united-states-v-echols/" aria-description="Citation for case: United States v. Echols">253 Fed. 862</a></span>;
   <em>
    Peterson
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8810455"><a href="/opinion/8825662/peterson-v-united-states/" aria-description="Citation for case: Peterson v. United States">255 Fed. 433</a></span>;
   <em>
    Billingsley
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8821314"><a href="/opinion/8836257/billingsley-v-united-states/#89" aria-description="Citation for case: Billingsley v. United States">274 Fed. 86, 89</a></span>;
   <em>
    Luterman
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8826008"><a href="/opinion/8840847/luterman-v-united-states/#377" aria-description="Citation for case: Luterman v. United States">281 Fed. 374, 377</a></span>;
   <em>
    United States
   </em>
   v.
   <em>
    Pappagoda,
   </em>
   <span class="citation" data-id="8829885"><a href="/opinion/8844647/united-states-v-pappagoda/" aria-description="Citation for case: United States v. Pappagoda">288 Fed. 214</a></span>;
   <em>
    Ritter
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8832845"><a href="/opinion/8847543/ritter-v-united-states/" aria-description="Citation for case: Ritter v. United States">293 Fed. 187</a></span>;
   <em>
    Di Salvo
   </em>
   v.
   <em>
    United States,
   </em>
   2 F. (2d) 222;
   <em>
    Silk
   </em>
   v.
   <span citation-index="1" class="star-pagination" label="444"> 
    *444
    </span>
<em>
    United States,
   </em>
   16 F. (2d) 568;
   <em>
    Jarl
   </em>
   v.
   <em>
    United States,
   </em>
   19 F. (2d) 891;
   <em>
    Corcoran
   </em>
   v.
   <em>
    United States,
   </em>
   19 F. (2d) 901;
   <em>
    United States
   </em>
   v.
   <em>
    Washington,
   </em>
   20 F. (2d) 160;
   <em>
    Cline
   </em>
   v.
   <em>
    United States,
   </em>
   20 F. (2d) 494;
   <em>
    United States ex rel. Hassel
   </em>
   v.
   <em>
    Mathues,
   </em>
   22 F. (2d) 979;
   <em>
    Driskill
   </em>
   v.
   <em>
    United States,
   </em>
   24 F. (2d) 525;
   <em>
    Ybor
   </em>
   v.
   <em>
    United States,
   </em>
   31 F. (2d) 42;
   <em>
    Robinson
   </em>
   v.
   <em>
    United States,
   </em>
   32 F. (2d) 505;
   <em>
    Vaccaro
   </em>
   v.
   <em>
    Collier,
   </em>
   38 F. (2d) 862;
   <em>
    Patton
   </em>
   v.
   <em>
    United States,
   </em>
   42 F. (2d) 68; and cases collected in note in
   <em>
    O’Brien
   </em>
   v.
   <em>
    United States,
   </em>
   51 F. (2d) 674, 678, including decisions of state courts. Compare
   <em>
    Rex
   </em>
   v.
   <em>
    Titley,
   </em>
   14 Cox C. C. 502;
   <em>
    Blaikie
   </em>
   v.
   <em>
    Linton,
   </em>
   18 Scottish Law Rep. 583; London Law Times, July 30, 1881, p. 223;
   <em>
    People
   </em>
   v.
   <em>
    Mills,
   </em>
   <span class="citation" data-id="3581964"><a href="/opinion/3600589/people-v-mills/" aria-description="Citation for case: People v. . Mills">178 N. Y. 274</a></span>; <span class="citation" data-id="3581964"><a href="/opinion/3600589/people-v-mills/" aria-description="Citation for case: People v. . Mills">70 N. E. 786</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Smith,
   </em>
   <span class="citation" data-id="3673731"><a href="/opinion/3927128/state-v-smith/" aria-description="Citation for case: State v. . Smith">152 N. C. 798</a></span>; <span class="citation" data-id="3673731"><a href="/opinion/3927128/state-v-smith/" aria-description="Citation for case: State v. . Smith">67 S. E. 508</a></span>;
   <em>
    Bauer
   </em>
   v.
   <em>
    Commonwealth,
   </em>
   <span class="citation" data-id="6815072"><a href="/opinion/6919457/bauer-v-commonwealth/" aria-description="Citation for case: Bauer v. Commonwealth">135 Va. 463</a></span>; <span class="citation" data-id="6815072"><a href="/opinion/6919457/bauer-v-commonwealth/" aria-description="Citation for case: Bauer v. Commonwealth">115 S. E. 514</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Gibbs,
   </em>
   <span class="citation" data-id="7975122"><a href="/opinion/8019675/state-v-gibbs/" aria-description="Citation for case: State v. Gibbs">109 Minn. 247</a></span>; <span class="citation" data-id="7975122"><a href="/opinion/8019675/state-v-gibbs/" aria-description="Citation for case: State v. Gibbs">123 N. W. 810</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Rippey,
   </em>
   127 S. C. 550; <span class="citation" data-id="3884966"><a href="/opinion/4123323/state-v-rippey/" aria-description="Citation for case: State v. Rippey">122 S. E. 397</a></span>. See, also, 18 A. L. R. Ann. 146; 28 Col. L. Rev. 1067; <span class="citation no-link">44 Harv. L. Rev. 109</span>; 2 So. Cal. L. Rev. 283 ; 41 Yale L. J. 1249; <span class="citation no-link">10 Va. L. Rev. 316</span>; <span class="citation no-link">9 Tex. L. Rev. 276</span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b510-6">
   See cases cited in note 4.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b512-7">
   See
   <em>
    Chicago B. &amp; Q. R. Co.
   </em>
   v.
   <em>
    McGuire,
   </em>
   <span class="citation" data-id="97368"><a href="/opinion/97368/chicago-burlington-quincy-railroad-v-mcguire/#565" aria-description="Citation for case: Chicago, Burlington &amp; Quincy Railroad v. McGuire">219 U. S. 549, 565</a></span>;
   <em>
    Green
   </em>
   v.
   <em>
    Frazier,
   </em>
   <span class="citation" data-id="99608"><a href="/opinion/99608/green-v-frazier/#240" aria-description="Citation for case: Green v. Frazier">253 U. S. 233, 240</a></span>.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b514-7">
   In
   <em>
    Hawaii
   </em>
   v.
   <em>
    Mankichi,
   </em>
   <span class="citation" data-id="9417915"><a href="/opinion/95894/hawaii-v-mankichi/#214" aria-description="Citation for case: Hawaii v. Mankichi">190 U. S. 197, 214</a></span>, the Court referred with approval to the following language of the Master of the Rolls (after-wards Lord Esher) in
   <em>
    Plumstead Board of Works
   </em>
   v.
   <em>
    Spackman,
   </em>
   L. R.
   <em>
    13 Q. B.
   </em>
   D. 878, 887: “If there are no means of avoiding such an interpretation of the statute,” (as will amount to a great hardship,) “ a judge must come to the conclusion that the legislature by inadvertence haa committed an act of legislative injustice; but to my mind a judge ought to struggle with all the intellect that he has, and with all the vigor of mind that he has, against such an interpretation of an act of Parliament; and, unless he is forced to come to a contrary conclusion, he ought to assume that it is impossible that the legislature could have so intended.”
  </p>
</div><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b519-8">
   See
   <em>
    O’Brien
   </em>
   v.
   <em>
    United States,
   </em>
   51 F. (2d) 674, footnote 1, p. 678.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b520-7">
   Compare
   <em>
    Olmstead
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b520-8">
<em>
    Casey
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9418615"><a href="/opinion/101251/casey-v-united-states/" aria-description="Citation for case: Casey v. United States">276 U. S. 413</a></span>.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b521-8">
   See
   <em>
    Hannay
   </em>
   v.
   <em>
    Eve,
   </em>
   <span class="citation" data-id="84810"><a href="/opinion/84810/hannay-v-eve/#247" aria-description="Citation for case: Hannay v. Eve">3 Cranch 242, 247</a></span>;
   <em>
    Bank of United States
   </em>
   v.
   <em>
    Owens,
   </em>
   <span class="citation" data-id="85646"><a href="/opinion/85646/president-of-the-bank-of-the-united-states-v-owens/#538" aria-description="Citation for case: President of the Bank of the United States v. Owens">2 Pet. 527, 538</a></span>;
   <em>
    Bartle
   </em>
   v.
   <em>
    Nutt,
   </em>
   <span class="citation" data-id="85698"><a href="/opinion/85698/bartle-v-nutt/#188" aria-description="Citation for case: Bartle v. Nutt">4 Pet. 184, 188</a></span>;
   <em>
    Hanauer
   </em>
   v.
   <em>
    Doane,
   </em>
   <span class="citation" data-id="88397"><a href="/opinion/88397/hanauer-v-doane/#349" aria-description="Citation for case: Hanauer v. Doane">12 Wall. 342, 349</a></span>;
   <em>
    Trist
   </em>
   v.
   <em>
    Child,
   </em>
   <span class="citation" data-id="89027"><a href="/opinion/89027/trist-v-child/#448" aria-description="Citation for case: Trist v. Child">21 Wall. 441, 448</a></span>;
   <em>
    Hazelton
   </em>
   v.
   <em>
    Sheckells,
   </em>
   <span class="citation" data-id="96460"><a href="/opinion/96460/hazelton-v-sheckells/" aria-description="Citation for case: Hazelton v. Sheckells">202 U. S. 71</a></span>;
   <em>
    Crocker
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="98638"><a href="/opinion/98638/crocker-v-united-states/#78" aria-description="Citation for case: Crocker v. United States">240 U. S. 74, 78</a></span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b523-7">
   Compare
   <em>
    Gambino
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/#319" aria-description="Citation for case: Gambino v. United States">275 U. S. 310, 319</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b523-8">
   See
   <em>
    United States ex rel. Hassell
   </em>
   v.
   <em>
    Mathues,
   </em>
   22 F. (2d) 979.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b523-9">
   Compare
   <em>
    United States
   </em>
   v.
   <em>
    Pappagoda,
   </em>
   <span class="citation" data-id="8829885"><a href="/opinion/8844647/united-states-v-pappagoda/" aria-description="Citation for case: United States v. Pappagoda">288 Fed. 214</a></span>;
   <em>
    Spring Drug Co.
   </em>
   v.
   <em>
    United States,
   </em>
   12 F. (2d) 852.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b523-10">
   In
   <em>
    United States
   </em>
   v.
   <em>
    Echols,
   </em>
   <span class="citation" data-id="8809555"><a href="/opinion/8824775/united-states-v-echols/" aria-description="Citation for case: United States v. Echols">253 Fed. 862</a></span>, upon the tender of a plea of guilty, the court of its own motion examined the prisoner and the officers concerned in his arrest; and being satisfied that these officers had instigated the crime, declared that public policy required that the plea be refused and the case dismissed. In
   <em>
    United States
   </em>
   v.
   <em>
    Healy,
   </em>
   <span class="citation" data-id="8786735"><a href="/opinion/8802548/united-states-v-healy/" aria-description="Citation for case: United States v. Healy">202 Fed. 349</a></span>, a judgment and sentence were set aside and the defendant discharged upon the court’s ascertaining that the conviction was procured by entrapment.
  </p>
</div></div></opinion>
```

---
