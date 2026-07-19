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

## GROUP: content/cases/Monell v. Department of Social Services.md  (`case`, 5 assertions)

### content_page

```
---
title: "Monell v. Department of Social Services"
type: case
citation: "436 U.S. 658 (1978)"
parallel_cite: "98 S. Ct. 2018; 56 L. Ed. 2d 611; 16 Empl. Prac. Dec. (CCH) 8345; 17 Fair Empl. Prac. Cas. (BNA) 873"
neutral_cite: 1978 U.S. LEXIS 100
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-06-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-06-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Monell v. Department of Social Services
  varies_by_point: false
  scope_note: "Overruled Monroe v. Pape in part (municipal immunity from § 1983 suit)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109881/monell-v-new-york-city-dept-of-social-servs/"
  cluster_id: 109881
  opinion_id: 109881
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Monroe v. Pape]]", "[[City of Canton v. Harris]]", "[[Pembaur v. City of Cincinnati]]"]
aliases: ["Monell v. New York City Dept. of Social Servs.", "Monell v. Department of Social Services of the City of New York"]
tags: ["case", "section-1983", "municipal-liability", "policy-or-custom", "respondeat-superior"]
holding: "Local governments ARE 'persons' suable under § 1983, but ONLY when the constitutional injury is caused by the execution of an official…"
lake:
  record_id: Monell v. Department of Social Services
  status: verified
  projected_at: 2026-07-06
---

# Monell v. Department of Social Services

*436 U.S. 658 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New York City employees challenged an official policy that compelled pregnant employees to take unpaid leave before it was medically necessary, suing the city and its officials under § 1983. The lower courts held the municipal defendants immune under *[[Monroe v. Pape]]*.

## Issue
Whether local governments are "persons" subject to suit under § 1983, and on what basis they may be held liable.

## Rule
Local governments are suable "persons" under § 1983, but only for their own official policies or customs — not vicariously. "the touchstone of the § 1983 action against a government body is an allegation that official policy is responsible for a deprivation of rights protected by the Constitution"; "local governments, like every other § 1983 'person,' by the very terms of the statute, may be sued for constitutional deprivations visited pursuant to governmental 'custom' even though such a custom has not received formal approval through the body's official decisionmaking channels." — 436 U.S. at 690-691. ^pin-690

At the same time, "a municipality cannot be held liable ... under § 1983 on a *respondeat superior* theory." — *Id.* at 691. ^pin-691

## Application
The challenged compulsory-leave rule was an official municipal policy "officially adopted and promulgated by that body's officers," not merely the act of an individual employee. Because the constitutional injury was inflicted through execution of the city's own policy, the city was a suable "person" under § 1983 and could be held liable for that policy — though not for an employee's tort on a vicarious-liability theory.

## Conclusion
Reversed in relevant part; municipalities are § 1983 "persons" liable for their official policies or customs, and *[[Monroe v. Pape]]* was overruled insofar as it held otherwise.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Monell* **overruled** [[Monroe v. Pape]] in part — its holding that municipalities are wholly immune from § 1983 suit. *Monell*'s policy-or-custom requirement was later elaborated by cases such as [[Pembaur v. City of Cincinnati]] and [[City of Canton v. Harris]].

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Monell v. Department of Social Services*, 436 U.S. 658 (1978) — https://www.courtlistener.com/opinion/109881/monell-v-new-york-city-dept-of-social-servs/ — pinpoints: 690, 691.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d288f2efab77f626", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "436 U.S. 658 (1978)", "court": "U.S. Supreme Court", "neutral_cite": "1978 U.S. LEXIS 100", "official_citation_present": true, "parallel_cite": "98 S. Ct. 2018; 56 L. Ed. 2d 611; 16 Empl. Prac. Dec. (CCH) 8345; 17 Fair Empl. Prac. Cas. (BNA) 873", "title": "Monell v. Department of Social Services", "year": "1978"}}
{"assertion_id": "7dfa85160005c693", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Local governments ARE 'persons' suable under § 1983, but ONLY when the constitutional injury is caused by the execution of an official…", "title": "Monell v. Department of Social Services"}}
{"assertion_id": "80fa75bb3b859a3b", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Monell v. Department of Social Services"}}
{"assertion_id": "86b5e61a944c994e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Monell v. Department of Social Services"}}
{"assertion_id": "8ed148260c6cc45d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1978-06-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Monell v. Department of Social Services", "field_i_validity": "good_law", "scope_note": "Overruled Monroe v. Pape in part (municipal immunity from § 1983 suit).", "title": "Monell v. Department of Social Services", "varies_by_point": "false"}}
```

### lake record — Monell v. Department of Social Services

```json
{
  "schema_version": "s2.v1",
  "record_id": "Monell v. Department of Social Services",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Monell v. New York City Dept. of Social Servs.",
    "case_name_short": "Monell",
    "case_name_full": "MONELL Et Al. v. DEPARTMENT OF SOCIAL SERVICES OF THE CITY OF NEW YORK Et Al.",
    "input_case_name": "Monell v. Department of Social Services",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-06-06",
    "year": 1978,
    "docket": null,
    "cluster_id": 109881,
    "lead_opinion_id": 109881,
    "sibling_ids": [
      109881,
      9427232,
      9427233,
      9427234,
      9427235
    ],
    "absolute_url": "/opinion/109881/monell-v-new-york-city-dept-of-social-servs/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9018437,
        "score": 20,
        "case_name": "Vinson v. Richmond Police Department"
      },
      {
        "cluster_id": 109930,
        "score": 20,
        "case_name": "Regents of the University of California v. Bakke"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "436 U.S. 658",
      "volume": "436",
      "reporter": "U.S.",
      "page": "658",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 2018",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2018",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 611",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "611",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 Empl. Prac. Dec. (CCH) 8345",
        "volume": "16",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "8345",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fair Empl. Prac. Cas. (BNA) 873",
        "volume": "17",
        "reporter": "Fair Empl. Prac. Cas. (BNA)",
        "page": "873",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 100",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "436 U.S. 658",
        "volume": "436",
        "reporter": "U.S.",
        "page": "658",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 2018",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2018",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 611",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "611",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 100",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 Empl. Prac. Dec. (CCH) 8345",
        "volume": "16",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "8345",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fair Empl. Prac. Cas. (BNA) 873",
        "volume": "17",
        "reporter": "Fair Empl. Prac. Cas. (BNA)",
        "page": "873",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "436 U.S. 658",
    "official_selection": {
      "court_class": "scotus",
      "selected": "436 U.S. 658",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-690",
      "page": null,
      "quote": "subject to suit under \u00a7 1983, and on what basis they may be held liable. ## Rule Local governments are suable",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-691",
      "page": null,
      "quote": "a municipality cannot be held liable ... under \u00a7 1983 on a *respondeat superior* theory.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-06-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Monell v. Department of Social Services",
    "varies_by_point": false,
    "scope_note": "Overruled Monroe v. Pape in part (municipal immunity from \u00a7 1983 suit).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "West v. Atkins",
          "cluster_id": 112116,
          "cite": [
            "101 L. Ed. 2d 40",
            "108 S. Ct. 2250",
            "487 U.S. 42",
            "1988 U.S. LEXIS 2744",
            "56 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heck v. Humphrey",
          "cluster_id": 117864,
          "cite": [
            "129 L. Ed. 2d 383",
            "114 S. Ct. 2364",
            "512 U.S. 477",
            "1994 U.S. LEXIS 4824"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Will v. Michigan Department of State Police",
          "cluster_id": 112293,
          "cite": [
            "105 L. Ed. 2d 45",
            "109 S. Ct. 2304",
            "491 U.S. 58",
            "1989 U.S. LEXIS 2975",
            "57 U.S.L.W. 4677",
            "50 Empl. Prac. Dec. (CCH) 39,067",
            "49 Fair Empl. Prac. Cas. (BNA) 1664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. Graham",
          "cluster_id": 111500,
          "cite": [
            "87 L. Ed. 2d 114",
            "105 S. Ct. 3099",
            "473 U.S. 159",
            "1985 U.S. LEXIS 86",
            "53 U.S.L.W. 4966"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Canton v. Harris",
          "cluster_id": 112209,
          "cite": [
            "103 L. Ed. 2d 412",
            "109 S. Ct. 1197",
            "489 U.S. 378",
            "1989 U.S. LEXIS 1200",
            "57 U.S.L.W. 4270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillips v. County of Allegheny",
          "cluster_id": 1387268,
          "cite": [
            "515 F.3d 224",
            "2008 U.S. App. LEXIS 2513",
            "2008 WL 305025"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of the County Commissioners of Bryan County v. Brown",
          "cluster_id": 118104,
          "cite": [
            "137 L. Ed. 2d 626",
            "117 S. Ct. 1382",
            "520 U.S. 397",
            "1997 U.S. LEXIS 2793",
            "65 U.S.L.W. 4286",
            "10 Fla. L. Weekly Fed. S 405",
            "12 I.E.R. Cas. (BNA) 1217",
            "97 Cal. Daily Op. Serv. 3033",
            "97 Daily Journal DAR 5311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parratt v. Taylor",
          "cluster_id": 110478,
          "cite": [
            "68 L. Ed. 2d 420",
            "101 S. Ct. 1908",
            "451 U.S. 527",
            "1981 U.S. LEXIS 99",
            "49 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pembaur v. City of Cincinnati",
          "cluster_id": 111615,
          "cite": [
            "89 L. Ed. 2d 452",
            "106 S. Ct. 1292",
            "475 U.S. 469",
            "1986 U.S. LEXIS 33",
            "54 U.S.L.W. 4289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Los Angeles v. Lyons",
          "cluster_id": 110916,
          "cite": [
            "75 L. Ed. 2d 675",
            "103 S. Ct. 1660",
            "461 U.S. 95",
            "1983 U.S. LEXIS 152",
            "51 U.S.L.W. 4424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Polk County v. Dodson",
          "cluster_id": 110589,
          "cite": [
            "70 L. Ed. 2d 509",
            "102 S. Ct. 445",
            "454 U.S. 312",
            "1981 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen v. McCurry",
          "cluster_id": 110360,
          "cite": [
            "66 L. Ed. 2d 308",
            "101 S. Ct. 411",
            "449 U.S. 90",
            "1980 U.S. LEXIS 156",
            "49 U.S.L.W. 4015"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DeShaney v. Winnebago County Department of Social Services",
          "cluster_id": 112202,
          "cite": [
            "103 L. Ed. 2d 249",
            "109 S. Ct. 998",
            "489 U.S. 189",
            "1989 U.S. LEXIS 1039",
            "57 U.S.L.W. 4218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
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
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Quern v. Jordan",
          "cluster_id": 110031,
          "cite": [
            "59 L. Ed. 2d 358",
            "99 S. Ct. 1139",
            "440 U.S. 332",
            "1979 U.S. LEXIS 67"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hafer v. Melo",
          "cluster_id": 112657,
          "cite": [
            "116 L. Ed. 2d 301",
            "112 S. Ct. 358",
            "502 U.S. 21",
            "1991 U.S. LEXIS 6502",
            "57 Empl. Prac. Dec. (CCH) 41,059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Oklahoma v. Tuttle",
          "cluster_id": 111441,
          "cite": [
            "85 L. Ed. 2d 791",
            "105 S. Ct. 2427",
            "471 U.S. 808",
            "1985 U.S. LEXIS 26"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of St. Louis v. Praprotnik",
          "cluster_id": 112017,
          "cite": [
            "99 L. Ed. 2d 107",
            "108 S. Ct. 915",
            "485 U.S. 112",
            "1988 U.S. LEXIS 1069"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monell v. Department of Social Services:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109881 OR 9427232 OR 9427233 OR 9427234 OR 9427235) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzE0MzQ4ODAwMDAwJnM9OTQ5Nzc2MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109881+OR+9427232+OR+9427233+OR+9427234+OR+9427235%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      },
      "lane2_top_cited": {
        "query": "cites:(109881 OR 9427232 OR 9427233 OR 9427234 OR 9427235)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjUxJnM9NDI0NzA4MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109881+OR+9427232+OR+9427233+OR+9427234+OR+9427235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109881 OR 9427232 OR 9427233 OR 9427234 OR 9427235)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzM5OTIzMjAwMDAwJnM9MTAzMzU1MTkmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109881+OR+9427232+OR+9427233+OR+9427234+OR+9427235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109881 OR 9427232 OR 9427233 OR 9427234 OR 9427235)",
    "indexed_citing_opinions": 11909,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109881,
        "count": 10324,
        "count_source": "search"
      },
      {
        "opinion_id": 9427232,
        "count": 1585,
        "count_source": "search"
      },
      {
        "opinion_id": 9427233,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427234,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427235,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 42009,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/monell-v-department-of-social-services.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zLjA1MzIyNjImcz03MzIzNjg4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109881+OR+9427232+OR+9427233+OR+9427234+OR+9427235%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9427233,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 96537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 104614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 107705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 108990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 109823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 249412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 334135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427233,
        "cited_id": 1460310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 84894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 86231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 86293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 87995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 88010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 88079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 88174,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 88308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 90262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 92688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 96537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 103172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 103360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 105221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 106658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 107993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108316,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 108990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 109823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 249412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 282871,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 334135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 1415269,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 1460310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 1480162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 1490664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 3876939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 6507289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 6599360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 6607492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 6633878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 7036523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 7037170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 7652067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8632804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8639091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8822445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8903338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 8939977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9004895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9299595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9300237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9301445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109881,
        "cited_id": 9427232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 84894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 86231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 86293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 87995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 88010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 88174,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 88308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 90262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 92688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 103172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 103360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 105221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 106658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 107993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108316,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 108990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 109728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 334135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 1415269,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 1480162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 1490664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 6507289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 6599360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 6633878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 7036523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 7037170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 7652067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 8639091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 8939977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 9004895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 9299595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 9300237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427232,
        "cited_id": 9301445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 84894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 86293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 87989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 88079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 104135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 108782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 108813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 108987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 108990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 109503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 109509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 109520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 109574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 282871,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 334135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 3876939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 6607492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 8632804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 8822445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9427235,
        "cited_id": 8903338,
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
    "date_created": "2026-07-05T14:24:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:24:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:24:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:27:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:24:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Monell v. Department of Social Services (truncated)

```
<div>
<center><b><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S. 658</a></span> (1978)</b></center>
<center><h1>MONELL ET AL.<br>
v.<br>
DEPARTMENT OF SOCIAL SERVICES OF THE CITY OF NEW YORK ET AL.</h1></center>
<center>No. 75-1914.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued November 2, 1977.</center>
<center>Decided June 6, 1978.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT
<p><span class="star-pagination">*660</span> <i>Oscar Chase</i> argued the cause for petitioners. With him on the briefs were <i>Nancy Stearns, Jack Greenberg,</i> and <i>Eric Schnapper.</i></p>
<p><i>L. Kevin Sheridan</i> argued the cause for respondents. With him on the brief was <i>W. Bernard Richland.</i><sup>[*]</sup></p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>Petitioners, a class of female employees of the Department of Social Services and of the Board of Education of the city of New York, commenced this action under <span class="citation no-link">42 U. S. C. § 1983</span> in July 1971.<sup>[1]</sup> The gravamen of the complaint was that the <span class="star-pagination">*661</span> Board and the Department had as a matter of official policy compelled pregnant employees to take unpaid leaves of absence before such leaves were required for medical reasons.<sup>[2]</sup> Cf. <i>Cleveland Board of Education</i> v. <i>LaFleur,</i> <span class="citation" data-id="9425515"><a href="/opinion/108913/cleveland-board-of-education-v-lafleur/" aria-description="Citation for case: Cleveland Board of Education v. LaFleur">414 U. S. 632</a></span> (1974). The suit sought injunctive relief and backpay for periods of unlawful forced leave. Named as defendants in the action were the Department and its Commissioner, the Board and its Chancellor, and the city of New York and its Mayor. In each case, the individual defendants were sued solely in their official capacities.<sup>[3]</sup></p>
<p>On cross-motions for summary judgment, the District Court for the Southern District of New York held moot petitioners' claims for injunctive and declaratory relief since the city of New York and the Board, after the filing of the complaint, had changed their policies relating to maternity leaves so that no pregnant employee would have to take leave unless she was medically unable to continue to perform her job. <span class="citation" data-id="1415269"><a href="/opinion/1415269/monell-v-deptartment-of-social-services-of-new-york/#855" aria-description="Citation for case: Monell v. Deptartment of Social Services of New York">394 F. Supp. 853, 855</a></span> (1975). No one now challenges this conclusion. <span class="star-pagination">*662</span> The court did conclude, however, that the acts complained of were unconstitutional under <i><span class="citation" data-id="9425515"><a href="/opinion/108913/cleveland-board-of-education-v-lafleur/" aria-description="Citation for case: Cleveland Board of Education v. LaFleur">LaFleur, supra.</a></span></i> <span class="citation" data-id="1415269"><a href="/opinion/1415269/monell-v-deptartment-of-social-services-of-new-york/#855" aria-description="Citation for case: Monell v. Deptartment of Social Services of New York">394 F. Supp., at 855</a></span>. Nonetheless plaintiffs' prayers for backpay were denied because any such damages would come ultimately from the city of New York and, therefore, to hold otherwise would be to "circumven[t]" the immunity conferred on municipalities by <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961). See <span class="citation" data-id="1415269"><a href="/opinion/1415269/monell-v-deptartment-of-social-services-of-new-york/#855" aria-description="Citation for case: Monell v. Deptartment of Social Services of New York">394 F. Supp., at 855</a></span>.</p>
<p>On appeal, petitioners renewed their arguments that the Board of Education<sup>[4]</sup> was not a "municipality" within the meaning of <i>Monroe</i> v. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Pape, supra</a></span></i><i>,</i> and that, in any event, the District Court had erred in barring a damages award against the individual defendants. The Court of Appeals for the Second Circuit rejected both contentions. The court first held that the Board of Education was not a "person" under § 1983 because "it performs a vital governmental function . . ., and, significantly, while it has the right to determine how the funds appropriated to it shall be spent . . ., it has no final say in deciding what its appropriations shall be." <span class="citation" data-id="334135"><a href="/opinion/334135/12-fair-emplpraccas-836-11-empl-prac-dec-p-10755-jane-monell-v/#263" aria-description="Citation for case: 12 Fair empl.prac.cas. 836, 11 Empl. Prac. Dec. P 10,755...">532 F. 2d 259, 263</a></span> (1976). The individual defendants, however, were "persons" under § 1983, even when sued solely in their official capacities. <span class="citation" data-id="334135"><a href="/opinion/334135/12-fair-emplpraccas-836-11-empl-prac-dec-p-10755-jane-monell-v/#264" aria-description="Citation for case: 12 Fair empl.prac.cas. 836, 11 Empl. Prac. Dec. P 10,755...">532 F. 2d, at 264</a></span>. Yet, because a damages award would "have to be paid by a city that was held not to be amenable to such an action in <i>Monroe</i> v. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Pape</a></span></i><i>,</i>" a damages action against officials sued in their official capacities could not proceed. <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#265" aria-description="Citation for case: Monroe v. Pape"><i>Id.,</i> at 265</a></span>.</p>
<p>We granted certiorari in this case, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1071/">429 U. S. 1071</a></span>, to consider</p>
<blockquote>"Whether local governmental officials and/or local independent school boards are `persons' within the meaning of <span class="citation no-link">42 U. S. C. § 1983</span> when equitable relief in the nature of back pay is sought against them in their official capacities?" Pet. for Cert. 8. <span class="star-pagination">*663</span> Although, after plenary consideration, we have decided the merits of over a score of cases brought under § 1983 in which the principal defendant was a school board<sup>[5]</sup>and, indeed, in some of which § 1983 and its jurisdictional counterpart, <span class="citation no-link">28 U. S. C. § 1343</span>, provided the only basis for jurisdiction<sup>[6]</sup>we indicated in <i>Mt. Healthy City Board of Education</i> v. <i>Doyle,</i> <span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/#279" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U. S. 274, 279</a></span> (1977), last Term that the question presented here was open and would be decided "another day." That other day has come and we now overrule <i>Monroe</i> v. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Pape, supra</a></span></i><i>,</i> insofar as it holds that local governments are wholly immune from suit under § 1983.<sup>[7]</sup></blockquote>
<p></p>
<h2>
<span class="star-pagination">*664</span> I</h2>
<p>In <i>Monroe</i> v. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Pape</a></span></i><i>,</i> we held that "Congress did not undertake to bring municipal corporations within the ambit of [§ 1983]." <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#187" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 187</a></span>. The sole basis for this conclusion was an inference drawn from Congress' rejection of the "Sherman amendment" to the bill which became the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, the precursor of § 1983. The amendment would have held a municipal corporation liable for damage done to the person or property of its inhabitants by <i>private</i> persons "riotously and tumultuously assembled."<sup>[8]</sup> Cong. Globe, 42d Cong., 1st Sess., 749 (1871) (hereinafter Globe). Although the Sherman amendment did not seek to amend § 1 of the Act, which is now § 1983, and although the nature of the obligation created by that amendment was vastly different from that created by § 1, the Court nonetheless concluded in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> that Congress must have meant to exclude municipal corporations from the coverage of § 1 because "`the House [in voting against the Sherman amendment] had solemnly decided that in their judgment Congress had no constitutional power to impose any <i>obligation</i> upon county and town organizations, the mere instrumentality for the administration of state law.'" <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#190" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 190</a></span> (emphasis added), quoting Globe 804 (Rep. Poland). This statement, we thought, showed that Congress doubted its "constitutional power . . . to impose <i>civil liability</i> on municipalities," <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#190" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 190</a></span> (emphasis added), and that such doubt would have extended to any type of civil liability.<sup>[9]</sup></p>
<p><span class="star-pagination">*665</span> A fresh analysis of the debate on the Civil Rights Act of 1871, and particularly of the case law which each side mustered in its support, shows, however, that <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> incorrectly equated the "obligation" of which Representative Poland spoke with "civil liability."</p>
<p></p>
<h2>A. An Overview</h2>
<p>There are three distinct stages in the legislative consideration of the bill which became the Civil Rights Act of 1871. On March 28, 1871, Representative Shellabarger, acting for a House select committee, reported H. R. 320, a bill "to enforce the provisions of the fourteenth amendment to the Constitution of the United States, and for other purposes." H. R. 320 contained four sections. Section 1, now codified as <span class="citation no-link">42 U. S. C. § 1983</span>, was the subject of only limited debate and was passed without amendment.<sup>[10]</sup> Sections 2 through 4 dealt primarily with the "other purpose" of suppressing Ku Klux Klan violence in the Southern States.<sup>[11]</sup> The wisdom and constitutionality of these sectionsnot § 1, now § 1983were the subject of almost all congressional debate and each of these sections was amended. The House finished its initial debates on H. R. 320 on April 7, 1871, and one week later the Senate also voted out a bill.<sup>[12]</sup> Again, debate on § 1 of the bill was limited and that section was passed as introduced.</p>
<p><span class="star-pagination">*666</span> Immediately prior to the vote on H. R. 320 in the Senate, Senator Sherman introduced his amendment.<sup>[13]</sup> This was <i>not</i> an amendment to § 1 of the bill, but was to be added as § 7 at the end of the bill. Under the Senate rules, no discussion of the amendment was allowed and, although attempts were made to amend the amendment, it was passed as introduced. In this form, the amendment did <i>not</i> place liability on municipal corporations, but made any inhabitant of a municipality liable for damage inflicted by persons "riotously and tumultuously assembled."<sup>[14]</sup></p>
<p>The House refused to acquiesce in a number of amendments made by the Senate, including the Sherman amendment, and the respective versions of H. R. 320 were therefore sent to a conference committee. Section 1 of the bill, however, was not a subject of this conference since, as noted, it was passed verbatim as introduced in both Houses of Congress.</p>
<p>On April 18, 1871, the first conference committee completed its work on H. R. 320. The main features of the conference committee draft of the Sherman amendment were these:<sup>[15]</sup> First, a cause of action was given to persons injured by</p>
<blockquote>"any persons riotously and tumultuously assembled together . . . with intent to deprive any person of any right conferred upon him by the Constitution and laws of the United States, or to deter him or punish him for exercising such right, or by reason of his race, color, or previous condition of servitude . . . ." <span class="star-pagination">*667</span> Second, the bill provided that the action would be against the county, city, or parish in which the riot had occurred and that it could be maintained by either the person injured or his legal representative. Third, unlike the amendment as proposed, the conference substitute made the government defendant liable on the judgment if it was not satisfied against individual defendants who had committed the violence. If a municipality were liable, the judgment against it could be collected</blockquote>
<blockquote>"by execution, attachment, mandamus, garnishment, or any other proceeding in aid of execution or applicable to the enforcement of judgments against municipal corporations; and such judgment [would become] a lien as well upon all moneys in the treasury of such county, city, or parish, as upon the other property thereof."</blockquote>
<p>In the ensuing debate on the first conference report, which was the first debate of any kind on the Sherman amendment, Senator Sherman explained that the purpose of his amendment was to enlist the aid of persons of property in the enforcement of the civil rights laws by making their property "responsible" for Ku Klux Klan damage.<sup>[16]</sup> Statutes drafted on a similar theory, he stated, had long been in force in England and were in force in 1871 in a number of States.<sup>[17]</sup><span class="star-pagination">*668</span> Nonetheless there were critical differences between the conference substitute and extant state and English statutes: The conference substitute, unlike most state riot statutes, lacked a short statute of limitations and imposed liability on the government defendant whether or not it had notice of the impending riot, whether or not the municipality was authorized to exercise a police power, whether or not it exerted all reasonable efforts to stop the riot, and whether or not the rioters were caught and punished.<sup>[18]</sup></p>
<p>The first conference substitute passed the Senate but was rejected by the House. House opponents, within whose ranks were some who had supported § 1, thought the Federal Government could not, consistent with the Constitution, obligate municipal corporations to keep the peace if those corporations were neither so obligated nor so authorized by their state charters. And, because of this constitutional objection, opponents of the Sherman amendment were unwilling to impose damages liability for nonperformance of a duty which Congress could not require municipalities to perform. This position is reflected in Representative Poland's statement that is quoted in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>.</i><sup>[19]</sup></p>
<p>Because the House rejected the first conference report a second conference was called and it duly issued its report. The second conference substitute for the Sherman amendment abandoned municipal liability and, instead, made "any person <span class="star-pagination">*669</span> or persons having knowledge [that a conspiracy to violate civil rights was afoot], and having power to prevent or aid in preventing the same," who did not attempt to stop the same, liable to any person injured by the conspiracy.<sup>[20]</sup> The amendment in this form was adopted by both Houses of Congress and is now codified as <span class="citation no-link">42 U. S. C. § 1986</span>.</p>
<p>The meaning of the legislative history sketched above can most readily be developed by first considering the debate on the report of the first conference committee. This debate shows conclusively that the constitutional objections raised against the Sherman amendmenton which our holding in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> was based, see <i>supra,</i> at 664would not have prohibited congressional creation of a civil remedy against state municipal corporations that infringed federal rights. Because § 1 of the Civil Rights Act does not state expressly that municipal corporations come within its ambit, it is finally necessary to interpret § 1 to confirm that such corporations were indeed intended to be included within the "persons" to whom that section applies.</p>
<p></p>
<h2>B. Debate on the First Conference Report</h2>
<p>The style of argument adopted by both proponents and opponents of the Sherman amendment in both Houses of Congress was largely legal, with frequent references to cases decided by this Court and the Supreme Courts of the several States. Proponents of the Sherman amendment did not, however, discuss in detail the argument in favor of its constitutionality. Nonetheless, it is possible to piece together such an argument from the debates on the first conference report and those on § 2 of the civil rights bill, which, because it allowed the Federal Government to prosecute crimes "in the States," had also raised questions of federal power. The account of Representative Shellabarger, the House sponsor of H. R. 320, is the most complete.</p>
<p><span class="star-pagination">*670</span> Shellabarger began his discussion of H. R. 320 by stating that "there is a domain of constitutional law involved in the right consideration of this measure which is wholly unexplored." Globe App. 67. There were analogies, however. With respect to the meaning of § 1 of the Fourteenth Amendment, and particularly its Privileges or Immunities Clause, Shellabarger relied on the statement of Mr. Justice Washington in <i>Corfield</i> v. <i>Coryell,</i> <span class="citation" data-id="9301445"><a href="/opinion/9306338/corfield-v-coryell/" aria-description="Citation for case: Corfield v. Coryell">4 Wash. C. C. 371</a></span> (CC ED Pa. 1825), which defined the privileges protected by Art. IV:</p>
<blockquote>"`What these fundamental privileges are[,] it would perhaps be more tedious than difficult to enumerate. They may, however, be all comprehended under the following general heads: protection by the Government;'</blockquote>
<blockquote>
<i>"Mark that</i></blockquote>
<blockquote>"`<i>protection by the Government;</i> the enjoyment of life and liberty, with the right to acquire and possess property of every kind, and to pursue and obtain happiness and safety . . . .'" Globe App. 69 (emphasis added), quoting <span class="citation" data-id="9301445"><a href="/opinion/9306338/corfield-v-coryell/#380" aria-description="Citation for case: Corfield v. Coryell">4 Wash. C. C., at 380-381</a></span>.</blockquote>
<p>Building on his conclusion that citizens were owed protectiona conclusion not disputed by opponents of the Sherman amendment<sup>[21]</sup>Shellabarger then considered Congress' role in providing that protection. Here again there were precedents:</p>
<blockquote>"[Congress has always] assumed to enforce, as against <span class="star-pagination">*671</span> the States, and also persons, every one of the provisions of the Constitution. Most of the provisions of the Constitution which restrain and directly relate to the States, such as those in [Art. I, § 10,] relate to the divisions of the political powers of the State and General Governments.. . . These prohibitions upon political powers of the States are all of such nature that they can be, and even have been, . . . enforced by the courts of the United States declaring void all State acts of encroachment on Federal powers. Thus, and thus sufficiently, has the United States `enforced' these provisions of the Constitution. But there are some that are not of this class. These are where the court secures the rights or the liabilities of persons within the States, as between such persons and the States.</blockquote>
<blockquote>"These three are: first, that as to fugitives from justice;<sup>[22]</sup> second, that as to fugitives from service, (or slaves;)<sup>[23]</sup> third, that declaring that the `citizens of each State shall be entitled to all the privileges and immunities of citizens in the several States.'<sup>[24]</sup></blockquote>
<blockquote>
<span class="star-pagination">*672</span> "And, sir, every one of thesethe only provisions where it was deemed that legislation was required to enforce the constitutional provisionsthe only three where the rights or liabilities of persons in the States, as between these persons and the States, are directly provided for, Congress has by legislation affirmatively interfered to protect . . . such persons." Globe App. 69-70.</blockquote>
<p>Of legislation mentioned by Shellabarger, the closest analog of the Sherman amendment, ironically, was the statute implementing the fugitives from justice and fugitive slave provisions of Art. IVthe Act of Feb. 12, 1793, 1 Stat. 302the constitutionality of which had been sustained in 1842, in <i>Prigg</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">16 Pet. 539</a></span>. There, Mr. Justice Story, writing for the Court, held that Art. IV gave slaveowners a federal right to the unhindered possession of their slaves in whatever State such slaves might be found. <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#612" aria-description="Citation for case: Prigg v. Pennsylvania">16 Pet., at 612</a></span>. Because state process for recovering runaway slaves might be inadequate or even hostile to the rights of the slaveowner, the right intended to be conferred could be negated if left to state implementation. <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#614" aria-description="Citation for case: Prigg v. Pennsylvania"><i>Id.,</i> at 614</a></span>. Thus, since the Constitution guaranteed the right and this in turn required a remedy, Story held it to be a "natural inference" that Congress had the power itself to ensure an appropriate (in the Necessary and Proper Clause sense) remedy for the right. <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#615" aria-description="Citation for case: Prigg v. Pennsylvania"><i>Id.,</i> at 615</a></span>.</p>
<p>Building on <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Prigg</a></span>,</i> Shellabarger argued that a remedy against municipalities and counties was an appropriateand hence constitutionalmethod for ensuring the protection which the Fourteenth Amendment made every citizen's federal right.<sup>[25]</sup> This much was clear from the adoption of such statutes by the several States as devices for suppressing riot.<sup>[26]</sup> Thus, said Shellabarger, the only serious question remaining <span class="star-pagination">*673</span> was "whether, since a county is an integer or part of a State, the United States can impose upon it, as such, <i>any obligations to keep the peace</i> in obedience to United States laws."<sup>[27]</sup> This he answered affirmatively, citing <i>Board of Comm'rs</i> v. <i>Aspinwall,</i> <span class="citation" data-id="87413"><a href="/opinion/87413/the-board-of-commrs-of-knox-county-v-aspinwall/" aria-description="Citation for case: The Board of Commr&#x27;s of Knox County v. Aspinwall">24 How. 376</a></span> (1861), the first of many cases<sup>[28]</sup> upholding the power of federal courts to enforce the Contract Clause against municipalities.<sup>[29]</sup></p>
<p>House opponents of the Sherman amendmentwhose views are particularly important since only the House voted down the amendmentdid not dispute Shellabarger's claim that the Fourteenth Amendment created a federal right to protection, see n. 21, <i>supra,</i> but they argued that the local units of government upon which the amendment fastened liability were not obligated to keep the peace at state law and further that the Federal Government could not constitutionally require local governments to create police forces, whether this requirement was levied directly, or indirectly by imposing damages for breach of the peace on municipalities. The most complete statement of this position is that of Representative Blair:<sup>[30]</sup></p>
<blockquote>"The proposition known as the Sherman amendment <span class="star-pagination">*674</span>. . . is entirely new. It is altogether without a precedent in this country. . . . That amendment claims the power in the General Government to go into the States of this Union and lay such obligations as it may please upon the municipalities, which are the creations of the States alone. . . .</blockquote>
<blockquote>". . . [H]ere it is proposed, not to carry into effect an obligation which rests upon the municipality, but to <span class="star-pagination">*675</span> create that obligation, and that is the provision I am unable to assent to. The parallel of the hundred does not in the least meet the case. The power that laid the obligation upon the hundred first put the duty upon the hundred that it should perform in that regard, and failing to meet the obligation which had been laid upon it, it was very proper that it should suffer damage for its neglect. . . .</blockquote>
<blockquote>"... [T]here are certain rights and duties that belong to the States, . . . there are certain powers that inhere in the State governments. They create these municipalities, they say what their powers shall be and what their obligations shall be. If the Government of the United States can step in and add to those obligations, may it not utterly destroy the municipality? If it can say that it shall be liable for damages occurring from a riot, . . . where [will] its power . . . stop and what obligations . . . might [it] not lay upon a municipality. . . .</blockquote>
<blockquote>"Now, only the other day, the Supreme Court . . . decided [in <i>Collector</i> v. <i>Day,</i> <span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">11 Wall. 113</a></span> (1871)] that there is no power in the Government of the United States, under its authority to tax, to tax the salary of a State officer. Why? Simply because the power to tax involves the power to destroy, and it was not the intent to give the Government of the United States power to destroy the government of the States in any respect. It was held also in the case of Prigg <i>vs.</i> Pennsylvania [<span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">16 Pet. 539</a></span> (1842)] that it is not within the power of the Congress of the United States to lay duties upon a State officer; that we cannot command a State officer to do any duty whatever, as such; and I ask . . . the difference between that and commanding a municipality, which is equally the creature of the State, to perform a duty." Globe 795.</blockquote>
<p>Any attempt to impute a unitary constitutional theory to opponents of the Sherman amendment is, of course, fraught <span class="star-pagination">*676</span> with difficulties, not the least of which is that most Members of Congress did not speak to the issue of the constitutionality of the amendment. Nonetheless, two considerations lead us to conclude that opponents of the Sherman amendment found it unconstitutional substantially because of the reasons stated by Representative Blair: First, Blair's analysis is precisely that of Poland, whose views were quoted as authoritative in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> see <i>supra,</i> at 664, and that analysis was shared in large part by all House opponents who addressed the constitutionality of the Sherman amendment.<sup>[31]</sup> Second, Blair's exegesis of the reigning constitutional theory of his day, as we shall explain, was clearly supported by precedentalbeit precedent that has not survived, see <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#347" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 347-348</a></span> (1880); <i>Graves</i> v. <i>New York ex rel. O'Keefe,</i> <span class="citation" data-id="9419020"><a href="/opinion/103172/graves-v-new-york-ex-rel-okeefe/#486" aria-description="Citation for case: Graves v. New York Ex Rel. O&#x27;Keefe">306 U. S. 466, 486</a></span> (1939)and no other constitutional formula was advanced by participants in the House debates.</p>
<p><i>Collector</i> v. <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i><i>,</i> cited by Blair, was the clearest and, at the time of the debates, the most recent pronouncement of a doctrine of coordinate sovereignty that, as Blair stated, placed limits on even the enumerated powers of the National Government in favor of protecting state prerogatives. There, the Court held that the United States could not tax the income of Day, a Massachusetts state judge, because the independence of the States within their legitimate spheres would be imperiled if the instrumentalities through which States executed their powers were "subject to the control of another and distinct government." <span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/#127" aria-description="Citation for case: Collector v. Day">11 Wall., at 127</a></span>. Although the Court in <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i> apparently rested this holding in part on the proposition that the taxing "power acknowledges no limits but the will of the legislative body imposing the tax," <span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/#125" aria-description="Citation for case: Collector v. Day"><i>id.,</i> at 125-126</a></span>; cf. <i>McCulloch</i> v. <i>Maryland,</i> <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316</a></span> (1819), the Court had in other cases limited other national powers in order to avoid interference with the States.<sup>[32]</sup></p>
<p><span class="star-pagination">*677</span> In <i>Prigg</i> v. <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Pennsylvania</a></span></i><i>,</i> for example, Mr. Justice Story, in addition to confirming a broad national power to legislate under the Fugitive Slave Clause, see <i>supra,</i> at 672, held that Congress could not "insist that states . . . provide means to carry into effect the duties of the national government." <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#615" aria-description="Citation for case: Prigg v. Pennsylvania">16 Pet., at 615-616</a></span>.<sup>[33]</sup> And Mr. Justice McLean agreed that, "[a]s a general principle," it was true "that Congress had no power to impose duties on state officers, as provided in the [Act of Feb. 12, 1793]." Nonetheless he wondered whether Congress might not impose "positive" duties on state officers where a clause of the Constitution, like the Fugitive Slave Clause, seemed to require affirmative government assistance, rather than restraint of government, to secure federal rights. See <span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/#664" aria-description="Citation for case: Prigg v. Pennsylvania"><i>id.,</i> at 664-665</a></span>.</p>
<p>Had Mr. Justice McLean been correct in his suggestion that, where the Constitution envisioned affirmative government assistance, the States or their officers or instrumentalities could be required to provide it, there would have been little doubt that Congress could have insisted that municipalities afford by "positive" action the protection<sup>[34]</sup> owed individuals under § 1 of the Fourteenth Amendment whether or not municipalities were obligated by state law to keep the peace. However, any such argument, largely foreclosed by <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Prigg</a></span>,</i> was made <span class="star-pagination">*678</span> impossible by the Court's holding in <i>Kentucky</i> v. <i>Dennison,</i> <span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">24 How. 66</a></span> (1861). There, the Court was asked to require Dennison, the Governor of Ohio, to hand over Lago, a fugitive from justice wanted in Kentucky, as required by § 1 of the Act of Feb. 12, 1793,<sup>[35]</sup> which implemented Art. IV, § 2, cl. 2, of the Constitution. Mr. Chief Justice Taney, writing for a unanimous Court, refused to enforce that section of the Act:</p>
<blockquote>"[W]e think it clear, that the Federal Government, under the Constitution, has no power to impose on a State officer, as such, any duty whatever, and compel him to perform it; for if it possessed this power, it might overload the officer with duties which would fill up all his time, and disable him from performing his obligations to the State, and might impose on him duties of a character incompatible with the rank and dignity to which he was elevated by the State." 24 How., at 107-108.</blockquote>
<p>The rationale of <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i>that the Nation could not impose duties on state officers since that might impede States in their legitimate activitiesis obviously identical to that which animated the decision in <i>Collector</i> v. <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i><i>.</i> See <i>supra,</i> at 676. And, as Blair indicated, municipalities as instrumentalities through which States executed their policies could be equally disabled from carrying out state policies if they were also obligated to carry out federally imposed duties. Although no one cited <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i> by name, the principle for which it <span class="star-pagination">*679</span> stands was well known to Members of Congress,<sup>[36]</sup> many of whom discussed <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i><sup>[37]</sup> as well as a series of State Supreme Court cases<sup>[38]</sup> in the mid-1860's which had invalidated a federal tax on the process of state courts on the ground that the tax threatened the independence of a vital state function.<sup>[39]</sup> Thus, there was ample support for Blair's view that the Sherman amendment, by putting municipalities to the Hobson's choice of keeping the peace or paying civil damages, attempted to impose obligations on municipalities by indirection that could not be imposed directly, thereby threatening to "destroy the government of the States." Globe 795.</p>
<p>If municipal liability under § 1 of the Civil Rights Act of 1871 created a similar Hobson's choice, we might conclude, as <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> did, that Congress could not have intended municipalities to be among the "persons" to which that section applied. But this is not the case.</p>
<p>First, opponents expressly distinguished between imposing an obligation to keep the peace and merely imposing civil liability for damages on a municipality that was obligated by state law to keep the peace, but which had not in violation of the Fourteenth Amendment. Representative Poland, for example, reasoning from Contract Clause precedents, indicated that Congress could constitutionally confer jurisdiction on the federal courts to entertain suits seeking to hold municipalities <span class="star-pagination">*680</span> liable for using their authorized powers in violation of the Constitutionwhich is as far as § 1 of the Civil Rights Act went:</p>
<blockquote>"I presume . . . that where a State had imposed a duty [to keep the peace] upon [a] municipality . . . an action would be allowed to be maintained against them in the courts of the United States under the ordinary restrictions as to jurisdiction. But the enforcing a liability, existing by their own contract, or by a State law, in the courts, is a very widely different thing from devolving a new duty or liability upon them by the national Government, which has no power either to create or destroy them, and no power or control over them whatever." Globe 794.</blockquote>
<p>Representative Burchard agreed:</p>
<blockquote>"[T]here is no duty imposed by the Constitution of the United States, or usually by State laws, upon a county to protect the people of that county against the commission of the offenses herein enumerated, such as the burning of buildings or any other injury to property or injury to person. Police powers are not conferred upon counties as corporations; they are conferred upon cities that have qualified legislative power. And so far as cities are concerned, where the equal protection required to be afforded by a State is imposed upon a city by State laws, perhaps the United States courts could enforce its performance. But counties . . . do not have any control of the police . . . ." <i>Id.,</i> at 795.</blockquote>
<p>See also the views of Rep. Willard, discussed at n. 30, <i>supra.</i></p>
<p>Second, the doctrine of dual sovereignty apparently put no limit on the power of federal courts to enforce the Constitution against municipalities that violated it. Under the theory of dual sovereignty set out in <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Prigg</a></span>,</i> this is quite understandable. So long as federal courts were vindicating the Federal Constitution, they were providing the "positive" government action <span class="star-pagination">*681</span> required to protect federal constitutional rights and no question was raised of enlisting the States in "positive" action. The limits of the principles announced in <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i> and <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i> are not so well defined in logic, but are clear as a matter of history. It must be remembered that the same Court which rendered <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span></i> also vigorously enforced the Contract Clause against municipalitiesan enforcement effort which included various forms of "positive" relief, such as ordering that taxes be levied and collected to discharge federal-court judgments, once a constitutional infraction was found.<sup>[40]</sup> Thus, federal judicial enforcement of the Constitution's express limits on state power, since it was done so frequently, must, notwithstanding anything said in <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i> or <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span>,</i> have been permissible, at least so long as the interpretation of the Constitution was left in the hands of the judiciary. Since § 1 of the Civil Rights Act simply conferred jurisdiction on the federal courts to enforce § 1 of the Fourteenth Amendmenta situation precisely analogous to the grant of diversity jurisdiction under which the Contract Clause was enforced against municipalitiesthere <span class="star-pagination">*682</span> is no reason to suppose that opponents of the Sherman amendment would have found any constitutional barrier to § 1 suits against municipalities.</p>
<p>Finally, the very votes of those Members of Congress, who opposed the Sherman amendment but who had voted for § 1, confirm that the liability imposed by § 1 was something very different from that imposed by the amendment. Section 1 without question could be used to obtain a damages judgment against state or municipal <i>officials</i> who violated federal constitutional rights while acting under color of law.<sup>[41]</sup> However, for <i>Prigg-Dennison-Day</i> purposes, as Blair and others recognized,<sup>[42]</sup> there was no distinction of constitutional magnitude between officers and agentsincluding corporate agentsof the State: Both were state instrumentalities and the State could be impeded no matter over which sort of instrumentality the Federal Government sought to assert its power. <i><span class="citation" data-id="87371"><a href="/opinion/87371/commonwealth-of-ky-v-dennison-governor-c/" aria-description="Citation for case: Commonwealth of Ky. v. DENNISON, GOVERNOR, &amp;C.">Dennison</a></span></i> and <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span>,</i> after all, were not suits against municipalities but against <i>officers,</i> and Blair was quite conscious that he was extending these cases by applying them to municipal corporations.<sup>[43]</sup> Nonetheless, Senator Thurman, who gave the most exhaustive critique of § 1<i>inter alia,</i> complaining that it would be applied to state officers, see Globe App. 217and who opposed both § 1 and the Sherman amendment, the latter on <i><span class="citation" data-id="9883019"><a href="/opinion/86231/prigg-v-pennsylvania/" aria-description="Citation for case: Prigg v. Pennsylvania">Prigg</a></span></i> grounds, agreed unequivocally that § 1 was constitutional.<sup>[44]</sup><span class="star-pagination">*683</span> Those who voted for § 1 must similarly have believed in its constitutionality despite <i>Prigg, Dennison,</i> and <i><span class="citation" data-id="9416804"><a href="/opinion/88308/collector-v-day/" aria-description="Citation for case: Collector v. Day">Day</a></span>.</i></p>
<p></p>
<h2>C. Debate on § 1 of the Civil Rights Bill</h2>
<p>From the foregoing discussion, it is readily apparent that nothing said in debate on the Sherman amendment would have prevented holding a municipality liable under § 1 of the Civil Rights Act for its own violations of the Fourteenth Amendment. The question remains, however, whether the general language describing those to be liable under § 1"any person"covers more than natural persons. An examination of the debate on § 1 and application of appropriate rules of construction show unequivocally that § 1 was intended to cover legal as well as natural persons.</p>
<p>Representative Shellabarger was the first to explain the function of § 1:</p>
<blockquote>"[Section 1] not only provides a civil remedy for persons whose former condition may have been that of slaves, but also to all people where, under color of State law, they or any of them may be deprived of rights to which they are entitled under the Constitution by reason and virtue of their national citizenship." Globe App. 68.</blockquote>
<p>By extending a remedy to all people, including whites, § 1 went beyond the mischief to which the remaining sections of the 1871 Act were addressed. Representative Shellabarger also stated without reservation that the constitutionality of § 2 of the Civil Rights Act of 1866 controlled the constitutionality of § 1 of the 1871 Act, and that the former had been <span class="star-pagination">*684</span> approved by "the supreme courts of at least three States of this Union" and by Mr. Justice Swayne, sitting on circuit, who had concluded: "`We have no doubt of the constitutionality of every provision of this act.'" Globe App. 68. Representative Shellabarger then went on to describe how the courts would and should interpret § 1:</p>
<blockquote>"This act is remedial, and in aid of the preservation of human liberty and human rights. All statutes and constitutional provisions authorizing such statutes are liberally and beneficently construed. It would be most strange and, in civilized law, monstrous were this not the rule of interpretation. As has been again and again decided by your own Supreme Court of the United States, and everywhere else where there is wise judicial interpretation, the largest latitude consistent with the words employed is uniformly given in construing such statutes and constitutional provisions as are meant to protect and defend and give remedies for their wrongs to all the people. . . . Chief Justice Jay and also Story say:</blockquote>
<blockquote>"`Where a power is remedial in its nature there is much reason to contend that it ought to be construed liberally, and it is generally adopted in the interpretation of laws.'1 <i>Story on Constitution,</i> sec. 429." Globe App., at 68.</blockquote>
<p>The sentiments expressed in Representative Shellabarger's opening speech were echoed by Senator Edmunds, the manager of H. R. 320 in the Senate:</p>
<blockquote>"The first section is one that I believe nobody objects to, as defining the rights secured by the Constitution of the United States when they are assailed by any State law or under color of any State law, and it is merely carrying out the principles of the civil rights bill [of 1866], which have since become a part of the Constitution." Globe 568.</blockquote>
<blockquote>
<span class="star-pagination">*685</span> "[Section 1 is] so very simple and really reënact[s] the Constitution." <i>Id.,</i> at 569.</blockquote>
<p>And he agreed that the bill "secure[d] the rights of white men as much as of colored men." <i>Id.,</i> at 696.</p>
<p>In both Houses, statements of the supporters of § 1 corroborated that Congress, in enacting § 1, intended to give a broad remedy for violations of federally protected civil rights.<sup>[45]</sup> Moreover, since municipalities through their official <span class="star-pagination">*686</span> acts could, equally with natural persons, create the harms intended to be remedied by § 1, and, further, since Congress intended § 1 to be broadly construed, there is no reason to suppose that municipal corporations would have been excluded from the sweep of § 1. Cf., <i>e. g., </i><i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 346-347</a></span> (1880); <i>Home Tel. &amp; Tel. Co.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/#286" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">227 U. S. 278, 286-287, 294-296</a></span> (1913). One need not rely on this inference alone, however, for the debates show that Members of Congress understood "persons" to include municipal corporations.</p>
<p>Representative Bingham, for example, in discussing § 1 of the bill, explained that he had drafted § 1 of the Fourteenth Amendment with the case of <i>Barron</i> v. <i>Mayor of Baltimore,</i> <span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">7 Pet. 243</a></span> (1833), especially in mind. "In [that] case the <span class="star-pagination">*687</span> <i>city</i> had taken private property for public use, without compensation. . ., and there was no redress for the wrong . . . ." Globe App. 84 (emphasis added). Bingham's further remarks clearly indicate his view that such takings by cities, as had occurred in <i><span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">Barron</a></span>,</i> would be redressable under § 1 of the bill. See Globe App. 85. More generally, and as Bingham's remarks confirm, § 1 of the bill would logically be the vehicle by which Congress provided redress for takings, since that section provided the only civil remedy for Fourteenth Amendment violations and that Amendment unequivocally prohibited uncompensated takings.<sup>[46]</sup> Given this purpose, it beggars reason to suppose that Congress would have exempted municipalities from suit, insisting instead that compensation for a taking come from an officer in his individual capacity rather than from the government unit that had the benefit of the property taken.<sup>[47]</sup></p>
<p>In addition, by 1871, it was well understood that corporations should be treated as natural persons for virtually all purposes of constitutional and statutory analysis. This had not always been so. When this Court first considered the question of the status of corporations, Mr. Chief Justice Marshall, writing for the Court, denied that corporations "as such" were persons as that term was used in Art. III and the Judiciary Act of 1789. See <i>Bank of the </i><i>United States</i> v. <i>Deveaux,</i> <span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/#86" aria-description="Citation for case: Bank of the United States v. Deveaux">5 Cranch 61, 86</a></span> (1809).<sup>[48]</sup> By 1844, however, the <i><span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/" aria-description="Citation for case: Bank of the United States v. Deveaux">Deveaux</a></span></i> doctrine was unhesitatingly abandoned:</p>
<blockquote>"[A] corporation created by and doing business in a particular <span class="star-pagination">*688</span> state, is to be deemed <i>to all intents and purposes as a person,</i> although an artificial person, . . . capable of being treated as a citizen of that state, as much as a natural person." <i>Louisville R. Co.</i> v. <i>Letson,</i> <span class="citation" data-id="86293"><a href="/opinion/86293/louisville-cincinnati-charleston-rail-road-v-letson/#558" aria-description="Citation for case: Louisville, Cincinnati, &amp; Charleston Rail-Road v. Letson">2 How. 497, 558</a></span> (1844) (emphasis added), discussed in Globe 752.</blockquote>
<p>And only two years before the debates on the Civil Rights Act, in <i>Cowles</i> v. <i>Mercer County,</i> <span class="citation" data-id="87989"><a href="/opinion/87989/cowles-v-mercer-county/#121" aria-description="Citation for case: Cowles v. Mercer County">7 Wall. 118, 121</a></span> (1869), the <i><span class="citation" data-id="86293"><a href="/opinion/86293/louisville-cincinnati-charleston-rail-road-v-letson/" aria-description="Citation for case: Louisville, Cincinnati, &amp; Charleston Rail-Road v. Letson">Letson</a></span></i> principle was automatically and without discussion extended to municipal corporations. Under this doctrine, municipal corporations were routinely sued in the federal courts<sup>[49]</sup> and this fact was well known to Members of Congress.<sup>[50]</sup></p>
<p>That the "usual" meaning of the word "person" would extend to municipal corporations is also evidenced by an Act of Congress which had been passed only months before the Civil Rights Act was passed. This Act provided that</p>
<blockquote>"in all acts hereafter passed . . . the word `person' may extend and be applied to bodies politic and corporate. . . unless the context shows that such words were intended to be used in a more limited sense." Act of Feb. 25, 1871, § 2, <span class="citation no-link">16 Stat. 431</span>.</blockquote>
<p>Municipal corporations in 1871 were included within the phrase "bodies politic and corporate"<sup>[51]</sup> and, accordingly, the <span class="star-pagination">*689</span> "plain meaning" of § 1 is that local government bodies were to be included within the ambit of the persons who could be sued under § 1 of the Civil Rights Act. Indeed, a Circuit Judge, writing in 1873 in what is apparently the first reported case under § 1, read the Dictionary Act in precisely this way in a case involving a corporate plaintiff and a municipal defendant.<sup>[52]</sup> See <i>Northwestern Fertilizing Co.</i> v. <i>Hyde Park,</i> <span class="citation" data-id="9299595"><a href="/opinion/9304502/northwestern-fertilizing-co-v-park/#394" aria-description="Citation for case: Northwestern Fertilizing Co. v. Park">18 F. Cas. 393, 394</a></span> (No. 10,336) (CC ND Ill. 1873).<sup>[53]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*690</span> II</h2>
<p>Our analysis of the legislative history of the Civil Rights Act of 1871 compels the conclusion that Congress <i>did</i> intend municipalities and other local government units to be included among those persons to whom § 1983 applies.<sup>[54]</sup> Local governing bodies,<sup>[55]</sup> therefore, can be sued directly under § 1983 for monetary, declaratory, or injunctive relief where, as here, the action that is alleged to be unconstitutional implements or executes a policy statement, ordinance, regulation, or decision officially adopted and promulgated by that body's officers. Moreover, although the touchstone of the § 1983 action against a government body is an allegation that official policy is responsible for a deprivation of rights protected by the Constitution, local governments, like every other § 1983 "person," by the very terms of the statute, may be sued for constitutional <span class="star-pagination">*691</span> deprivations visited pursuant to governmental "custom" even though such a custom has not received formal approval through the body's official decisionmaking channels. As Mr. Justice Harlan, writing for the Court, said in <i>Adickes</i> v. <i>S. H. Kress &amp; Co.,</i> <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#167" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 167-168</a></span> (1970): "Congress included customs and usages [in § 1983] because of the persistent and widespread discriminatory practices of state officials . . . . Although not authorized by written law, such practices of state officials could well be so permanent and well settled as to constitute a `custom or usage' with the force of law."<sup>[56]</sup></p>
<p>On the other hand, the language of § 1983, read against the background of the same legislative history, compels the conclusion that Congress did not intend municipalities to be held liable unless action pursuant to official municipal policy of some nature caused a constitutional tort. In particular, we conclude that a municipality cannot be held liable <i>solely</i> because it employs a tortfeasoror, in other words, a municipality cannot be held liable under § 1983 on a <i>respondeat superior</i> theory.</p>
<p>We begin with the language of § 1983 as originally passed:</p>
<blockquote>"[<i>A</i>]<i>ny person who,</i> under color of any law, statute, ordinance, regulation, custom, or usage of any State, <i>shall subject, or cause to be subjected,</i> any person . . . to the deprivation of any rights, privileges, or immunities secured by the Constitution of the United States, shall, any such <span class="star-pagination">*692</span> law, statute, ordinance, regulation, custom, or usage of the State to the contrary notwithstanding, be liable to the party injured in any action at law, suit in equity, or other proper proceeding for redress . . . ." <span class="citation no-link">17 Stat. 13</span> (emphasis added).</blockquote>
<p>The italicized language plainly imposes liability on a government that, under color of some official policy, "causes" an employee to violate another's constitutional rights. At the same time, that language cannot be easily read to impose liability vicariously on governing bodies solely on the basis of the existence of an employer-employee relationship with a tortfeasor. Indeed, the fact that Congress did specifically provide that A's tort became B's liability if B "caused" A to subject another to a tort suggests that Congress did not intend § 1983 liability to attach where such causation was absent.<sup>[57]</sup> See <i>Rizzo</i> v. <i>Goode,</i> <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#370" aria-description="Citation for case: Rizzo v. Goode">423 U. S. 362, 370-371</a></span> (1976).</p>
<p><span class="star-pagination">*693</span> Equally important, creation of a federal law of <i>respondeat superior</i> would have raised all the constitutional problems associated with the obligation to keep the peace, an obligation Congress chose not to impose because it thought imposition of such an obligation unconstitutional. To this day, there is disagreement about the basis for imposing liability on an employer for the torts of an employee when the sole nexus between the employer and the tort is the fact of the employer-employee relationship. See W. Prosser, Law of Torts § 69, p. 459 (4th ed. 1971). Nonetheless, two justifications tend to stand out. First is the common-sense notion that no matter how blameless an employer appears to be in an individual case, accidents might nonetheless be reduced if employers had to bear the cost of accidents. See, <i>e. g., ibid.;</i> 2 F. Harper &amp; F. James, Law of Torts, § 26.3, pp. 1368-1369 (1956). Second is the argument that the cost of accidents should be <span class="star-pagination">*694</span> spread to the community as a whole on an insurance theory. See, <i>e. g., id.,</i> § 26.5; Prosser, <i>supra,</i> at 459.<sup>[58]</sup></p>
<p>The first justification is of the same sort that was offered for statutes like the Sherman amendment: "The obligation to make compensation for injury resulting from riot is, by arbitrary enactment of statutes, affirmatory law, and the reason of passing the statute is to secure a more perfect police regulation." Globe 777 (Sen. Frelinghuysen). This justification was obviously insufficient to sustain the amendment against perceived constitutional difficulties and there is no reason to suppose that a more general liability imposed for a similar reason would have been thought less constitutionally objectionable. The second justification was similarly put forward as a justification for the Sherman amendment: "we do not look upon [the Sherman amendment] as a punishment. . . . It is a mutual insurance." <i>Id.,</i> at 792 (Rep. Butler). Again, this justification was insufficient to sustain the amendment.</p>
<p>We conclude, therefore, that a local government may not be sued under § 1983 for an injury inflicted solely by its employees or agents. Instead, it is when execution of a government's policy or custom, whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy, inflicts the injury that the government as an entity is responsible under § 1983. Since this case unquestionably involves official policy as the moving force of the constitutional violation found by the District Court, see <i>supra,</i> at <span class="star-pagination">*695</span> 660-662, and n. 2, we must reverse the judgment below. In so doing, we have no occasion to address, and do not address, what the full contours of municipal liability under § 1983 may be. We have attempted only to sketch so much of the § 1983 cause of action against a local government as is apparent from the history of the 1871 Act and our prior cases, and we expressly leave further development of this action to another day.</p>
<p></p>
<h2>III</h2>
<p>Although we have stated that <i>stare decisis</i> has more force in statutory analysis than in constitutional adjudication because, in the former situation, Congress can correct our mistakes through legislation, see, <i>e. g., </i><i>Edelman</i> v. <i>Jordan,</i> <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/#671" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651, 671</a></span>, and n. 14 (1974), we have never applied <i>stare decisis</i> mechanically to prohibit overruling our earlier decisions determining the meaning of statutes. See, <i>e. g., </i><i>Continental T. V., Inc.</i> v. <i>GTE Sylvania Inc.,</i> <span class="citation" data-id="9426918"><a href="/opinion/109716/continental-t-v-inc-v-gte-sylvania-inc/#47" aria-description="Citation for case: Continental T. v.  Inc. v. GTE Sylvania Inc.">433 U. S. 36, 47-49</a></span> (1977); <i>Burnet v. Coronado Oil &amp; Gas Co.,</i> <span class="citation" data-id="8148759"><a href="/opinion/8186832/burnet-v-coronado-oil-gas-co/" aria-description="Citation for case: Burnet v. Coronado Oil &amp; Gas Co.">285 U. S. 393</a></span>, 406 n. 1 (1932) (Brandeis, J., dissenting) (collecting cases). Nor is this a case where we should "place on the shoulders of Congress the burden of the Court's own error." <i>Girouard</i> v. <i>United States,</i> <span class="citation" data-id="9419823"><a href="/opinion/104285/girouard-v-united-states/#70" aria-description="Citation for case: Girouard v. United States">328 U. S. 61, 70</a></span> (1946).</p>
<p>First, <i>Monroe</i> v. <i>Pape</i><i>,</i> insofar as it completely immunizes municipalities from suit under § 1983, was a departure from prior practice. See, <i>e. g., </i><i>Northwestern Fertilizing Co.</i> v. <i>Hyde Park,</i> <span class="citation" data-id="9299595"><a href="/opinion/9304502/northwestern-fertilizing-co-v-park/" aria-description="Citation for case: Northwestern Fertilizing Co. v. Park">18 F. Cas. 393</a></span> (No. 10,336) (CC ND Ill. 1873); <i>City of Manchester</i> v. <i>Leiby,</i> <span class="citation" data-id="1480162"><a href="/opinion/1480162/city-of-manchester-v-leiby/" aria-description="Citation for case: City of Manchester v. Leiby">117 F. 2d 661</a></span> (CA1 1941); <i>Hannan</i> v. <i>City of Haverhill,</i> <span class="citation" data-id="1490664"><a href="/opinion/1490664/hannan-v-city-of-haverhill/" aria-description="Citation for case: Hannan v. City of Haverhill">120 F. 2d 87</a></span> (CA1 1941); <i>Douglas</i> v. <i>City of Jeannette,</i> <span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157</a></span> (1943); <i>Holmes</i> v. <i>Atlanta,</i> <span class="citation" data-id="8928384"><a href="/opinion/8938007/holmes-v-city-of-atlanta/" aria-description="Citation for case: Holmes v. City of Atlanta">350 U. S. 879</a></span> (1955), in each of which municipalities were defendants in § 1983 suits.<sup>[59]</sup> Moreover, the constitutional defect <span class="star-pagination">*696</span> that led to the rejection of the Sherman amendment would not have distinguished between municipalities and school boards, each of which is an instrumentality of state administration. See <i>supra,</i> at 673-682. For this reason, our casesdecided both before and after <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> see n. <span class="citation" data-id="334135"><a href="/opinion/334135/12-fair-emplpraccas-836-11-empl-prac-dec-p-10755-jane-monell-v/" aria-description="Citation for case: 12 Fair empl.prac.cas. 836, 11 Empl. Prac. Dec. P 10,755...">5, <i>supra</i></a></span> holding school boards liable in § 1983 actions are inconsistent with <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> especially as <i>Monroe's</i> immunizing principle was extended to suits for injunctive relief in <i>City of Kenosha</i> v. <i>Bruno,</i> <span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507</a></span> (1973).<sup>[60]</sup> And although in many of these cases jurisdiction was not questioned, we ought not "disregard the implications of an exercise of judicial authority assumed to be proper for [100] years." <i>Brown Shoe Co.</i> v. <i>United States,</i> <span class="citation" data-id="9422445"><a href="/opinion/106440/brown-shoe-co-v-united-states/#307" aria-description="Citation for case: Brown Shoe Co. v. United States">370 U. S. 294, 307</a></span> (1962); see <i>Bank of the </i><i>United States</i> v. <i>Deveaux,</i> <span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/#88" aria-description="Citation for case: Bank of the United States v. Deveaux">5 Cranch, at 88</a></span> (Marshall, C. J.) ("Those decisions are not cited as authority . . . but they have much weight, as they show that this point neither occurred to the bar or the bench"). Thus, while we have reaffirmed <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> without further examination on three occasions,<sup>[61]</sup> it can scarcely be said that <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> is so consistent with the warp and woof of civil rights law as to be beyond question.</p>
<p>Second, the principle of blanket immunity established in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> cannot be cabined short of school boards. Yet such an extension would itself be inconsistent with recent expressions of congressional intent. In the wake of our decisions, Congress not only has shown no hostility to federal-court decisions against school boards, but it has indeed rejected efforts to strip the federal courts of jurisdiction over school boards.<sup>[62]</sup> Moreover, recognizing that school boards are often <span class="star-pagination">*697</span> defendants in school desegregation suits, which have almost without exception been § 1983 suits, Congress has twice passed legislation authorizing grants to school boards to assist them in complying with federal-court decrees.<sup>[63]</sup> Finally, in <span class="star-pagination">*698</span> regard to the Civil Rights Attorney's Fees Awards Act of 1976, <span class="citation no-link">90 Stat. 2641</span>, <span class="citation no-link">42 U. S. C. § 1988</span> (1976 ed.), which allows prevailing parties (in the discretion of the court) in § 1983 suits <span class="star-pagination">*699</span> to obtain attorney's fees from the losing parties, the Senate stated:</p>
<blockquote>"[D]efendants in these cases are often State or local <i>bodies</i> or State or local officials. In such cases it is intended that the attorneys' fees, like other items of costs, will be collected either directly from the official, <i>in his official capacity,</i> from funds of his agency or under his control, or <i>from the State or local government (whether or not the agency or government is a named party)."</i> S. Rep. No. 94-1011, p. 5 (1976) (emphasis added; footnotes omitted).</blockquote>
<p>Far from showing that Congress has relied on <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> therefore, events since 1961 show that Congress has refused to extend the benefits of <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> to school boards and has attempted to allow awards of attorney's fees against local governments even though <i>Monroe, City of Kenosha</i> v. <i><span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">Bruno</a></span>,</i> and <i>Aldinger</i> v. <i>Howard,</i> <span class="citation" data-id="9426488"><a href="/opinion/109503/aldinger-v-howard/" aria-description="Citation for case: Aldinger v. Howard">427 U. S. 1</a></span> (1976), have made the joinder of such governments impossible.<sup>[64]</sup></p>
<p>Third, municipalities can assert no reliance claim which can <span class="star-pagination">*700</span> support an absolute immunity. As Mr. Justice Frankfurter said in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> "[t]his is not an area of commercial law in which, presumably, individuals may have arranged their affairs in reliance on the expected stability of decision." <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#221" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 221-222</a></span> (dissenting in part). Indeed, municipalities simply cannot "arrange their affairs" on an assumption that they can violate constitutional rights indefinitely since injunctive suits against local officials under § 1983 would prohibit any such arrangement. And it scarcely need be mentioned that nothing in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> encourages municipalities to violate constitutional rights or even suggests that such violations are anything other than completely wrong.</p>
<p>Finally, even under the most stringent test for the propriety of overruling a statutory decision proposed by Mr. Justice Harlan in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i><sup>[65]</sup>"that it appear beyond doubt from the legislative history of the 1871 statute that <i>[Monroe]</i> misapprehended the meaning of the [section]," <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#192" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 192</a></span> (concurring opinion)the overruling of <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> insofar as it holds that local governments are not "persons" who may be defendants in § 1983 suits is clearly proper. It is simply beyond doubt that, under the 1871 Congress' view of the law, were § 1983 liability unconstitutional as to local governments, it would have been equally unconstitutional as to state officers. Yet everyoneproponents and opponents alikeknew § 1983 would be applied to state officers and nonetheless stated that § 1983 was constitutional. See <i>supra,</i> at 680-682. And, moreover, there can be no doubt that § 1 of the Civil Rights Act was intended to provide a remedy, to be broadly construed, against all forms of official violation of federally protected <span class="star-pagination">*701</span> rights. Therefore, absent a clear statement in the legislative history supporting the conclusion that § 1 was not to apply to the official acts of a municipal corporationwhich simply is not presentthere is no justification for excluding municipalities from the "persons" covered by § 1.</p>
<p>For the reasons stated above, therefore, we hold that <i>stare decisis</i> does not bar our overruling of <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> insofar as it is inconsistent with Parts I and II of this opinion.<sup>[66]</sup></p>
<p></p>
<h2>IV</h2>
<p>Since the question whether local government bodies should be afforded some form of official immunity was not presented as a question to be decided on this petition and was not briefed by the parties or addressed by the courts below, we express no views on the scope of any municipal immunity beyond holding that municipal bodies sued under § 1983 cannot be entitled to an absolute immunity, lest our decision that such bodies are subject to suit under § 1983 "be drained of meaning," <i>Scheuer</i> v. <i>Rhodes,</i> <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#248" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 248</a></span> (1974). Cf. <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#397" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 397-398</a></span> (1971).</p>
<p></p>
<h2>
<span class="star-pagination">*702</span> V</h2>
<p>For the reasons stated above, the judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT</h2>
<p>As proposed, the Sherman amendment was as follows:</p>
<blockquote>"That if any house, tenement, cabin, shop, building, barn, or granary shall be unlawfully or feloniously demolished, pulled down, burned, or destroyed, wholly or in part, by any persons riotously and tumultuously assembled together; or if any person shall unlawfully and with force and violence be whipped, scourged, wounded, or killed by any persons riotously and tumultuously assembled together; and if such offense was committed to deprive any person of any right conferred upon him by the Constitution and laws of the United States, or to deter him or punish him for exercising such right, or by reason of his race, color, or previous condition of servitude, in every such case the inhabitants of the county, city, or parish in which any of the said offenses shall be committed shall be liable to pay full compensation to the person or persons damnified by such offense if living, or to his widow or legal representative if dead; and such compensation may be recovered by such person or his representative by a suit in any court of the United States of competent jurisdiction in the district in which the offense was committed, to be in the name of the person injured, or his legal representative, and against said county, city, or parish. And execution may be issued on a judgment rendered in such suit and may be levied upon any property, real or personal, of any person in said county, city, or parish, and the said county, city, or parish may recover the full amount of such judgment, costs and interest, <span class="star-pagination">*703</span> from any person or persons engaged as principal or accessory in such riot in an action in any court of competent jurisdiction." Globe 663.</blockquote>
<p>The complete text of the first conference substitute for the Sherman amendment is:</p>
<blockquote>"That if any house, tenement, cabin, shop, building, barn, or granary shall be unlawfully or feloniously demolished, pulled down, burned, or destroyed, wholly or in part, by any persons riotously and tumultuously assembled together; or if any person shall unlawfully and with force and violence be whipped, scourged, wounded, or killed by any persons riotously and tumultuously assembled together, with intent to deprive any person of any right conferred upon him by the Constitution and laws of the United States, or to deter him or punish him for exercising such right, or by reason of his race, color, or previous condition of servitude, in every such case the county, city, or parish in which any of the said offenses shall be committed shall be liable to pay full compensation to the person or persons damnified by such offense, if living, or to his widow or legal representative if dead; and such compensation may be recovered in an action on the case by such person or his representative in any court of the United States of competent jurisdiction in the district in which the offense was committed, such action to be in the name of the person injured, or his legal representative, and against said county, city, or parish, and in which action any of the parties committing such acts may be joined as defendants. And any payment of any judgment, or part thereof unsatisfied, recovered by the plaintiff in such action, may, if not satisfied by the individual defendant therein within two months next after the recovery of such judgment upon execution duly issued against such individual defendant in such judgment, and returned unsatisfied, in whole or in part, be enforced <span class="star-pagination">*704</span> against such county, city, or parish, by execution, attachment, mandamus, garnishment, or any other proceeding in aid of execution or applicable to the enforcement of judgments against municipal corporations; and such judgment shall be a lien as well upon all moneys in the treasury of such county, city, or parish, as upon the other property thereof. And the court in any such action may on motion cause additional parties to be made therein prior to issue joined, to the end that justice may be done. And the said county, city, or parish may recover the full amount of such judgment, by it paid, with costs and interest, from any person or persons engaged as principal or accessory in such riot, in an action in any court of competent jurisdiction. And such county, city, or parish, so paying, shall also be subrogated to all the plaintiff's rights under such judgment." <i>Id.,</i> at 749, 755.</blockquote>
<p>The relevant text of the second conference substitute for the Sherman amendment is as follows:</p>
<blockquote>"[A]ny person or persons having knowledge that any of the wrongs conspired to be done and mentioned in the second section of this act are about to be committed, and having power to prevent or aid in preventing the same, <i>shall neglect or refuse so to do,</i> and such wrongful act shall be committed, such person or persons shall be liable to the person injured, or his legal representatives." <i>Id.,</i> at 804 (emphasis added).</blockquote>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>I join the opinion of the Court, and express these additional views.</p>
<p>Few cases in the history of the Court have been cited more frequently than <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), decided less than two decades ago. Focusing new light on <span class="citation no-link">42 U. S. C. § 1983</span>, that decision widened access to the federal courts and permitted expansive interpretations of the reach of <span class="star-pagination">*705</span> the 1871 measure. But <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> exempted local governments from liability at the same time it opened wide the courthouse door to suits against officers and employees of those entitieseven when they act pursuant to express authorization. The oddness of this result, and the weakness of the historical evidence relied on by the <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> Court in support of it, are well demonstrated by the Court's opinion today. Yet the gravity of overruling a part of so important a decision prompts me to write.</p>
<p></p>
<h2>I</h2>
<p>In addressing a complaint alleging unconstitutional police conduct that probably was unauthorized and actionable under state law,<sup>[1]</sup> the <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> Court treated the 42d Congress' rejection of the Sherman amendment as conclusive evidence of an intention to immunize local governments from all liability under the statute for constitutional injury. That reading, in light of today's thorough canvass of the legislative history, clearly "misapprehended the meaning of the controlling provision," <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#192" aria-description="Citation for case: Monroe v. Pape"><i>Monroe, supra,</i> at 192</a></span> (Harlan, J., concurring). In this case, involving formal, written policies of the Department of Social Services and the Board of Education of the city of New York that are alleged to conflict <span class="star-pagination">*706</span> with the command of the Due Process Clause, cf. <i>Cleveland Board of Education</i> v. <i>LaFleur,</i> <span class="citation" data-id="9425515"><a href="/opinion/108913/cleveland-board-of-education-v-lafleur/" aria-description="Citation for case: Cleveland Board of Education v. LaFleur">414 U. S. 632</a></span> (1974), the Court decides "not to reject [wisdom] merely because it comes late," <i>Henslee</i> v. <i>Union Planters Bank,</i> <span class="citation" data-id="9420257"><a href="/opinion/104614/henslee-v-union-planters-national-bank-trust-co/#600" aria-description="Citation for case: Henslee v. Union Planters National Bank &amp; Trust Co.">335 U. S. 595, 600</a></span> (1949) (Frankfurter, J., dissenting).</p>
<p>As the Court demonstrates, the Sherman amendment presented an extreme example of "riot act" legislation that sought to impose vicarious liability on government subdivisions for the consequences of private lawlessness. As such, it implicated concerns that are of marginal pertinence to the operative principle of § 1 of the 1871 legislationnow § 1983that "any person" acting "under color of" state law may be held liable for affirmative conduct that "subjects, or causes to be subjected, any person . . . to the deprivation of any" federal constitutional or statutory right. Of the many reasons for the defeat of the Sherman proposal, none supports <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i>'s observation that the 42d Congress was fundamentally "antagonistic," <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#191" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 191</a></span>, to the proposition that government entities and natural persons alike should be held accountable for the consequences of conduct directly working a constitutional violation. Opponents in the Senate appear to have been troubled primarily by the proposal's unprecedented lien provision, which would have exposed even property held for public purposes to the demands of § 1983 judgment lienors. <i>Ante,</i> at 673-674, n. 30. The opposition in the House of Representatives focused largely on the Sherman amendment's attempt to impose a peacekeeping obligation on municipalities when the Constitution itself imposed no such affirmative duty and when many municipalities were not even empowered under state law to maintain police forces. <i>Ante,</i> at 673-675, 679-682.<sup>[2]</sup></p>
<p><span class="star-pagination">*707</span> The Court correctly rejects a view of the legislative history that would produce the anomalous result of immunizing local government units from monetary liability for action directly causing a constitutional deprivation, even though such actions may be fully consistent with, and thus not remediable under, state law. No conduct of government comes more clearly within the "under color of" state law language of § 1983. It is most unlikely that Congress intended public officials acting under the command or the specific authorization of the government employer to be <i>exclusively</i> liable for resulting constitutional injury.<sup>[3]</sup></p>
<p>As elaborated in Part II of today's opinion, the rejection of the Sherman amendment can best be understood not as evidence of Congress' acceptance of a rule of absolute municipal immunity but as a limitation of the statutory ambit to actual wrongdoers, <i>i. e.,</i> a rejection of <i>respondeat superior</i> or any other principle of vicarious liability. Cf. Levin, The Section 1983 Municipal Immunity Doctrine, 65 Geo. L. J. 1483, 1531-1535 (1977). Thus, it has been clear that a public official may be held liable in damages when his actions are found to violate a constitutional right and there is no qualified immunity, see <i>Wood</i> v. <i>Strickland,</i> <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975); <i>Procunier</i> v. <i>Navarette,</i> <span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555</a></span> (1978). Today the Court recognizes <span class="star-pagination">*708</span> that this principle also applies to a local government when implementation of its official policies or established customs inflicts the constitutional injury.</p>
<p></p>
<h2>II</h2>
<p>This Court traditionally has been hesitant to overrule prior constructions of statutes or interpretations of common-law rules. "<i>Stare decisis</i> is usually the wise policy," <i>Burnet</i> v. <i>Coronado Oil &amp; Gas Co.,</i> <span class="citation" data-id="8148759"><a href="/opinion/8186832/burnet-v-coronado-oil-gas-co/#406" aria-description="Citation for case: Burnet v. Coronado Oil &amp; Gas Co.">285 U. S. 393, 406</a></span> (1932) (Brandeis, J., dissenting), but this cautionary principle must give way to countervailing considerations in appropriate circumstances.<sup>[4]</sup> I concur in the Court's view that this is not a case where we should "place on the shoulders of Congress the burden of the Court's own error." <i>Girouard</i> v. <i>United States,</i> <span class="citation" data-id="9419823"><a href="/opinion/104285/girouard-v-united-states/#70" aria-description="Citation for case: Girouard v. United States">328 U. S. 61, 70</a></span> (1946).</p>
<p>Nor is this the usual case in which the Court is asked to overrule a precedent. Here considerations of <i>stare decisis</i> cut in both directions. On the one hand, we have a series of rulings that municipalities and counties are not "persons" for purposes of § 1983. On the other hand, many decisions of this Court have been premised on the amenability of school boards and similar entities to § 1983 suits.</p>
<p>In <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> and its progeny, we have answered a question that was never actually briefed or argued in this Court whether a municipality is liable in damages for injuries that are the direct result of its official policies. "The theory of the complaint [in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> was] that under the circumstances [t]here alleged the City [was] liable for the acts of its police officers, by virtue of <i>respondeat superior.</i>" Brief for Petitioners, <span class="star-pagination">*709</span> O. T. 1960, No. 39, p. 21.<sup>[5]</sup> Respondents answered that adoption of petitioners' position would expose "Chicago and every other municipality in the United States . . . to Civil Rights Act liability through no action of its own and based on action contrary to its own ordinances and the laws of the state it is a part of." Brief for Respondents, O. T. 1960, No. 39, p. 26. Thus the ground of decision in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> was not advanced by either party and was broader than necessary to resolve the contentions made in that case.<sup>[6]</sup></p>
<p><span class="star-pagination">*710</span> Similarly, in <i>Moor</i> v. <i>County of Alameda,</i> <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/" aria-description="Citation for case: Moor v. County of Alameda">411 U. S. 693</a></span> (1973), petitioners asserted that "the County was vicariously liable for the acts of its deputies and sheriff," <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/#696" aria-description="Citation for case: Moor v. County of Alameda"><i>id.,</i> at 696</a></span>, under <span class="citation no-link">42 U. S. C. § 1988</span>. In rejecting this vicarious-liability claim, <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/#710" aria-description="Citation for case: Moor v. County of Alameda">411 U. S., at 710</a></span>, and n. 27, we reaffirmed <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i>'s reading of the statute, but there was no challenge in that case to "the holding in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> concerning the status under § 1983 of public entities such as the County," <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/#700" aria-description="Citation for case: Moor v. County of Alameda">411 U. S., at 700</a></span>; Brief for Petitioners, O. T. 1972, No. 72-10, p. 9.</p>
<p>Only in <i>City of Kenosha</i> v. <i>Bruno,</i> <span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507</a></span> (1973), did the Court confront a § 1983 claim based on conduct that was both authorized under state law and the direct cause of the claimed constitutional injury. In <i>Kenosha,</i> however, we raised the issue of the city's amenability to suit under § 1983 on our own initiative.<sup>[7]</sup></p>
<p>This line of casesfrom <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> to <i>Kenosha</i>is difficult to reconcile on a principled basis with a parallel series of cases <span class="star-pagination">*711</span> in which the Court has assumed <i>sub silentio</i> that some local government entities could be sued under § 1983. If now, after full consideration of the question, we continued to adhere to <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> grave doubt would be cast upon the Court's exercise of § 1983 jurisdiction over school boards. See <i>ante,</i> at 663 n. 5. Since "the principle of blanket immunity established in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> cannot be cabined short of school boards," <i>ante,</i> at 696, the conflict is squarely presented. Although there was an independent basis of jurisdiction in many of the school board cases because of the inclusion of individual public officials as nominal parties, the opinions of this Court make explicit reference to the school board party, particularly in discussions of the relief to be awarded, see, <i>e. g., </i><i>Green</i> v. <i>County School Board,</i> <span class="citation" data-id="107705"><a href="/opinion/107705/green-v-county-school-board-of-new-kent-county/#437" aria-description="Citation for case: Green v. County School Board of New Kent County">391 U. S. 430, 437-439, 441-442</a></span> (1968); <i>Milliken</i> v. <i>Bradley,</i> <span class="citation" data-id="9426944"><a href="/opinion/109723/milliken-v-bradley/#292" aria-description="Citation for case: Milliken v. Bradley">433 U. S. 267, 292-293</a></span> (1977) (POWELL, J., concurring in judgment). And, as the Court points out, <i>ante,</i> at 696-697, and nn. 62, 63, Congress has focused specifically on this Court's school board decisions in several statutes. Thus the exercise of § 1983 jurisdiction over school boards, while perhaps not premised on considered holdings, has been longstanding. Indeed, it predated <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>.</i></p>
<p>Even if one attempts to explain away the school board decisions as involving suits which "may be maintained against board members in their official capacities for injunctive relief under either § 1983 or <i>Ex parte Young,</i> <span class="citation" data-id="9418117"><a href="/opinion/96819/ex-parte-young/" aria-description="Citation for case: Ex Parte Young">209 U. S. 123</a></span> (1908)," <i>post,</i> at 716-717, n. 2, some difficulty remains in rationalizing the relevant body of precedents. At least two of the school board cases involved claims for monetary relief. <i>Cohen</i> v. <i>Chesterfield County School Board,</i> <span class="citation" data-id="1460310"><a href="/opinion/1460310/cohen-v-chesterfield-county-school-board/#1161" aria-description="Citation for case: Cohen v. Chesterfield County School Board">326 F. Supp. 1159, 1161</a></span> (ED Va. 1971), rev'd, <span class="citation multiple-matches"><a href="/c/F.%202d/474/395/">474 F. 2d 395</a></span> (CA4 1973), rev'd and remanded, <span class="citation" data-id="9425515"><a href="/opinion/108913/cleveland-board-of-education-v-lafleur/" aria-description="Citation for case: Cleveland Board of Education v. LaFleur">414 U. S. 632</a></span> (1974); <i>Tinker</i> v. <i>Des Moines Independent School Dist.,</i> <span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#504" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 504</a></span> (1969). See also <i>Vlandis</i> v. <i>Kline,</i> <span class="citation" data-id="9425336"><a href="/opinion/108810/vlandis-v-kline/#445" aria-description="Citation for case: Vlandis v. Kline">412 U. S. 441, 445</a></span> (1973). Although the point was not squarely presented in this Court, these claims <span class="star-pagination">*712</span> for damages could not have been maintained in official-capacity suits if the government entity were not itself suable. Cf. <i>Edelman</i> v. <i>Jordan,</i> <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651</a></span> (1974).<sup>[8]</sup> Moreover, the rationale of <i>Kenosha</i> would have to be disturbed to avoid closing all avenues under § 1983 to injunctive relief against constitutional violations by local government. The Court of Appeals in this case suggested that we import, by analogy, the Eleventh Amendment fiction of <i>Ex parte Young</i> into § 1983, <span class="citation" data-id="334135"><a href="/opinion/334135/12-fair-emplpraccas-836-11-empl-prac-dec-p-10755-jane-monell-v/#264" aria-description="Citation for case: 12 Fair empl.prac.cas. 836, 11 Empl. Prac. Dec. P 10,755...">532 F. 2d 259, 264-266</a></span> (CA2 1976). That approach, however, would create tension with <i>Kenosha</i> because it would require "a bifurcated application" of "the generic word `person' in § 1983" to public officials "depending on the nature of the relief sought against them." 412 U. S., at 513. A public official sued in his official capacity for carrying out official policy would be a "person" for purposes of injunctive relief, but a non-"person" in an action for damages. The Court's holding avoids this difficulty. See <i>ante,</i> at 690 n. 55.</p>
<p>Finally, if we continued to adhere to a rule of absolute municipal immunity under § 1983, we could not long avoid the question whether "we should, by analogy to our decision in <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971), imply a cause of action directly from the Fourteenth Amendment which would not be subject to the limitations contained in § 1983 . . . ." <i>Mt. Healthy City Board of Ed.</i> v. <i>Doyle,</i> <span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/#278" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U. S. 274, 278</a></span> (1977). One aspect of that inquiry would be whether there are any "special factors counselling hesitation in the absence of affirmative action by Congress," <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#396" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 396</a></span> (1971), such as an "explicit congressional declaration <span class="star-pagination">*713</span> that persons injured by a [municipality] may not recover money damages . . ., but must instead be remitted to another remedy, equally effective in the view of Congress," <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#397" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of..."><i>id.,</i> at 397</a></span>. In light of the Court's persuasive re-examination in today's decision of the 1871 debates, I would have difficulty inferring from § 1983 "an explicit congressional declaration" against municipal liability for the implementation of official policies in violation of the Constitution. Rather than constitutionalize a cause of action against local government that Congress intended to create in 1871, the better course is to confess error and set the record straight, as the Court does today.<sup>[9]</sup></p>
<p></p>
<h2>III</h2>
<p>Difficult questions nevertheless remain for another day. There are substantial line-drawing problems in determining "when execution of a government's policy or custom" can be said to inflict constitutional injury such that "government as an entity is responsible under § 1983." <i>Ante,</i> at 694. This case, however, involves formal, written policies of a municipal department and school board; it is the clear case. The Court also reserves decision on the availability of a qualified municipal immunity. <i>Ante,</i> at 701. Initial resolution of the question whether the protection available at common law for municipal corporations, see <i>post,</i> at 720-721, or other principles support a <span class="star-pagination">*714</span> qualified municipal immunity in the context of the § 1983 damages action, is left to the lower federal courts.</p>
<p>MR. JUSTICE STEVENS, concurring in part.</p>
<p>Since Parts II and IV of the opinion of the Court are merely advisory and are not necessary to explain the Court's decision, I join only Parts I, III, and V.</p>
<p>MR. JUSTICE REHNQUIST, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>Seventeen years ago, in <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), this Court held that the 42d Congress did not intend to subject a municipal corporation to liability as a "person" within the meaning of <span class="citation no-link">42 U. S. C. § 1983</span>. Since then, the Congress has remained silent, but this Court has reaffirmed that holding on at least three separate occasions. <i>Aldinger</i> v. <i>Howard,</i> <span class="citation" data-id="9426488"><a href="/opinion/109503/aldinger-v-howard/" aria-description="Citation for case: Aldinger v. Howard">427 U. S. 1</a></span> (1976); <i>City of Kenosha</i> v. <i>Bruno,</i> <span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507</a></span> (1973); <i>Moor</i> v. <i>County of Alameda,</i> <span class="citation" data-id="9425281"><a href="/opinion/108782/moor-v-county-of-alameda/" aria-description="Citation for case: Moor v. County of Alameda">411 U. S. 693</a></span> (1973). See also <i>Mt. Healthy City Board of Ed.</i> v. <i>Doyle,</i> <span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/#277" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U. S. 274, 277-279</a></span> (1977). Today, the Court abandons this long and consistent line of precedents, offering in justification only an elaborate canvass of the same legislative history which was before the Court in 1961. Because I cannot agree that this Court is "free to disregard these precedents," which have been "considered maturely and recently" by this Court, <i>Runyon</i> v. <i>McCrary,</i> <span class="citation" data-id="9426505"><a href="/opinion/109509/runyon-v-mccrary/#186" aria-description="Citation for case: Runyon v. McCrary">427 U. S. 160, 186</a></span> (1976) (POWELL, J., concurring), I am compelled to dissent.</p>
<p></p>
<h2>I</h2>
<p>As this Court has repeatedly recognized, <i><span class="citation" data-id="9426505"><a href="/opinion/109509/runyon-v-mccrary/" aria-description="Citation for case: Runyon v. McCrary">id.,</a></span></i> at 175 n. 12; <i>Edelman</i> v. <i>Jordan,</i> <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651</a></span>, 671 n. 14 (1974), considerations of <i>stare decisis</i> are at their strongest when this Court confronts its previous constructions of legislation. In all cases, private parties shape their conduct according to this Court's settled construction of the law, but the Congress is at <span class="star-pagination">*715</span> liberty to correct our mistakes of statutory construction, unlike our constitutional interpretations, whenever it sees fit. The controlling principles were best stated by Mr. Justice Brandeis:</p>
<blockquote>"<i>Stare decisis</i> is usually the wise policy, because in most matters it is more important that the applicable rule of law be settled than that it be settled right. . . . This is commonly true even where the error is a matter of serious concern, provided correction can be had by legislation. But in cases involving the Federal Constitution, where correction through legislative action is practically impossible, this Court has often overruled its earlier decisions." <i>Burnet</i> v. <i>Coronado Oil &amp; Gas Co.,</i> <span class="citation" data-id="8148759"><a href="/opinion/8186832/burnet-v-coronado-oil-gas-co/#406" aria-description="Citation for case: Burnet v. Coronado Oil &amp; Gas Co.">285 U. S. 393, 406-407</a></span> (1932) (dissenting opinion) (footnotes omitted).</blockquote>
<p>Only the most compelling circumstances can justify this Court's abandonment of such firmly established statutory precedents. The best exposition of the proper burden of persuasion was delivered by Mr. Justice Harlan in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> itself:</p>
<blockquote>"From my point of view, the policy of <i>stare decisis,</i> as it should be applied in matters of statutory construction, and, to a lesser extent, the indications of congressional acceptance of this Court's earlier interpretation, require that it appear <i>beyond doubt</i> from the legislative history of the 1871 statute that [<i>United States</i> v.] <i>Classic,</i> [<span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U. S. 299</a></span> (1941)] and <i>Screws</i> [v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span> (1945)] misapprehended the meaning of the controlling provision, before a departure from what was decided in those cases would be justified." <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#192" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 192</a></span> (concurring opinion) (footnote omitted; emphasis added).</blockquote>
<p>The Court does not demonstrate that any exception to this general rule is properly applicable here. The Court's first assertion, that <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> "was a departure from prior practice," <i>ante,</i> at 695, is patently erroneous. Neither in <i>Douglas</i> v. <i>City of Jeannette,</i> <span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157</a></span> (1943), nor in <i>Holmes</i> v. <i>Atlanta,</i> <span class="star-pagination">*716</span> <span class="citation" data-id="8928384"><a href="/opinion/8938007/holmes-v-city-of-atlanta/" aria-description="Citation for case: Holmes v. City of Atlanta">350 U. S. 879</a></span> (1955), nor in any of the school board cases cited by the Court, <i>ante,</i> at 663 n. 5, was the question now before us raised by any of the litigants or addressed by this Court. As recently as four Terms ago, we said in <i>Hagans</i> v. <i>Lavine,</i> <span class="citation" data-id="9425636"><a href="/opinion/108987/hagans-v-lavine/" aria-description="Citation for case: Hagans v. Lavine">415 U. S. 528</a></span>, 535 n. 5 (1974):</p>
<blockquote>"Moreover, when questions of jurisdiction have been passed on in prior decisions <i>sub silentio,</i> this Court has never considered itself bound when a subsequent case finally brings the jurisdictional issue before us."</blockquote>
<p>The source of this doctrine that jurisdictional issues decided <i>sub silentio</i> are not binding in other cases seems to be Mr. Chief Justice Marshall's remark in <i>United States</i> v. <i>More,</i> <span class="citation" data-id="6607492"><a href="/opinion/6726239/united-states-v-more/#172" aria-description="Citation for case: United States v. More">3 Cranch 159, 172</a></span> (1805).<sup>[1]</sup> While the Chief Justice also said that such decisions may "have much weight, as they show that this point neither occurred to the bar or the bench," <i>Bank of the </i><i>United States</i> v. <i>Deveaux,</i> <span class="citation" data-id="84894"><a href="/opinion/84894/bank-of-the-united-states-v-deveaux/#88" aria-description="Citation for case: Bank of the United States v. Deveaux">5 Cranch 61, 88</a></span> (1809), unconsidered assumptions of jurisdiction simply cannot outweigh four consistent decisions of this Court, explicitly considering and rejecting that jurisdiction.</p>
<p>Nor is there any indication that any later Congress has ever approved suit against any municipal corporation under § 1983. Of all its recent enactments, only the Civil Rights Attorney's Fees Awards Act of 1976, § 2, <span class="citation no-link">90 Stat. 2641</span>, <span class="citation no-link">42 U. S. C. § 1988</span> (1976 ed.), explicitly deals with the Civil Rights Act of 1871.<sup>[2]</sup> The 1976 Act provides that attorney's fees may be awarded <span class="star-pagination">*717</span> to the prevailing party "[i]n any action or proceeding to enforce a provision of sections 1981, 1982, 1983, 1985, and 1986 of this title." There is plainly no language in the 1976 Act which would enlarge the parties suable under those substantive sections; it simply provides that parties who are already suable may be made liable for attorney's fees. As the Court admits, <i>ante,</i> at 699, the language in the Senate Report stating that liability may be imposed "whether or not the agency or government is a named party," S. Rep. No. 94-1011, p. 5 (1976), suggests that Congress did not view its purpose as being in any way inconsistent with the well-known holding of <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>.</i></p>
<p>The Court's assertion that municipalities have no right to act "on an assumption that they can violate constitutional rights indefinitely," <i>ante,</i> at 700, is simply beside the point. Since <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> municipalities <i>have</i> had the right to expect that they would not be held liable retroactively for their officers' failure to predict this Court's recognition of new constitutional rights. No doubt innumerable municipal insurance policies and indemnity ordinances have been founded on this assumption, which is wholly justifiable under established principles of <i>stare decisis.</i> To obliterate those legitimate expectations without more compelling justifications than those advanced by the Court is a significant departure from our prior practice.</p>
<p>I cannot agree with MR. JUSTICE POWELL's view that "[w]e owe somewhat less deference to a decision that was rendered without benefit of a full airing of all the relevant considerations." <i>Ante,</i> at 709 n. 6. Private parties must be able to rely upon explicitly stated holdings of this Court without being <span class="star-pagination">*718</span> obliged to peruse the briefs of the litigants to predict the likelihood that this Court might change its mind. To cast such doubt upon each of our cases, from <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137</a></span> (1803), forward, in which the explicit ground of decision "was never actually briefed or argued," <i>ante,</i> at 708 (POWELL, J., concurring), would introduce intolerable uncertainty into the law. Indeed, in <i><span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">Marbury</a></span></i> itself, the argument of Charles Lee on behalf of the applicantswhich, unlike the arguments in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> is reproduced in the Reports of this Court where anyone can see itdevotes not a word to the question of whether this Court has the power to invalidate a statute duly enacted by the Congress. Neither this ground of decision nor any other was advanced by Secretary of State Madison, who evidently made no appearance. <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/#153" aria-description="Citation for case: Marbury v. Madison">1 Cranch, at 153-154</a></span>. More recent landmark decisions of this Court would appear to be likewise vulnerable under my Brother POWELL'S analysis. In <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), none of the parties requested the Court to overrule <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949); it did so only at the request of an <i>amicus curiae.</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 646</a></span> n. 3. That <i>Marbury, Mapp,</i> and countless other decisions retain their vitality despite their obvious flaws is a necessary byproduct of the adversary system, in which both judges and the general public rely upon litigants to present "all the relevant considerations." <i>Ante,</i> at 709 n. 6 (POWELL, J., concurring). While it undoubtedly has more latitude in the field of constitutional interpretation, this Court is surely not free to abandon settled statutory interpretation at any time a new thought seems appealing.<sup>[3]</sup></p>
<p>Thus, our only task is to discern the intent of the 42d Congress. That intent was first expounded in <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>,</i> and it <span class="star-pagination">*719</span> has been followed consistently ever since. This is not some esoteric branch of the law in which congressional silence might reasonably be equated with congressional indifference. Indeed, this very year, the Senate has been holding hearings on a bill, S. 35, 95th Cong., 1st Sess. (1977), which would remove the municipal immunity recognized by <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>.</i> 124 Cong. Rec. D117 (daily ed. Feb. 8, 1978). In these circumstances, it cannot be disputed that established principles of <i>stare decisis</i> require this Court to pay the highest degree of deference to its prior holdings. <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span></i> may not be overruled unless it has been demonstrated "beyond doubt from the legislative history of the 1871 statute that [<span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape"><i>Monroe</i></a></span>] misapprehended the meaning of the controlling provision." <i>Monroe,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#192" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 192</a></span> (Harlan, J., concurring). The Court must show not only that Congress, in rejecting the Sherman amendment, concluded that municipal liability was not unconstitutional, but also that, in enacting § 1, it intended to impose that liability. I am satisfied that no such showing has been made.</p>
<p></p>
<h2>II</h2>
<p>Any analysis of the meaning of the word "person" in § 1983, which was originally enacted as § 1 of the Ku Klux Klan Act of April 20, 1871, <span class="citation no-link">17 Stat. 13</span>, must begin, not with the Sherman amendment, but with the Dictionary Act. The latter Act, which supplied rules of construction for all legislation, provided:</p>
<blockquote>"That in all acts hereafter passed . . . the word `person' may extend and be applied to bodies politic and corporate. . . unless the context shows that such words were intended to be used in a more limited sense . . . ." Act of Feb. 25, 1871, § 2, <span class="citation no-link">16 Stat. 431</span>.</blockquote>
<p>The Act expressly provided that corporations need not be included within the scope of the word "person" where the context suggests a more limited reach. Not a word in the legislative history of the Act gives any indication of the contexts <span class="star-pagination">*720</span> in which Congress felt it appropriate to include a corporation as a person. Indeed, the chief cause of concern was that the Act's provision that "words importing the masculine gender may be applied to females," might lead to an inadvertent extension of the suffrage to women. Cong. Globe, 41st Cong., 3d Sess., 777 (1871) (remarks of Sen. Sawyer).</p>
<p>There are other factors, however, which suggest that the Congress which enacted § 1983 may well have intended the word "person" "to be used in a more limited sense," as <i><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for ca

[...TRUNCATED 83639 of 203639 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Montejo v. Louisiana.md  (`case`, 5 assertions)

### content_page

```
---
title: "Montejo v. Louisiana"
type: case
citation: "556 U.S. 778 (2009)"
parallel_cite: "129 S. Ct. 2079; 173 L. Ed. 2d 955"
neutral_cite: 2009 U.S. LEXIS 3973
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-05-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-05-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Montejo v. Louisiana
  varies_by_point: false
  scope_note: "Montejo itself overruled Michigan v. Jackson; Montejo is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145873/montejo-v-louisiana/"
  cluster_id: 145873
  opinion_id: 145873
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Michigan v. Jackson]]", "[[Edwards v. Arizona]]", "[[McNeil v. Wisconsin]]", "[[Maryland v. Shatzer]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "waiver", "interrogation"]
holding: "A defendant may validly waive his Sixth Amendment right to counsel during police-initiated interrogation even after counsel has been…"
lake:
  record_id: Montejo v. Louisiana
  status: verified
  projected_at: 2026-07-06
---

# Montejo v. Louisiana

*556 U.S. 778 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Montejo was arrested for murder. At a preliminary "72-hour hearing," the court ordered the appointment of counsel. Before Montejo met his appointed lawyer, detectives read him his *[[Miranda v. Arizona|Miranda]]* rights; he agreed to accompany them to locate the murder weapon and, during the trip, wrote an inculpatory letter of apology to the victim's widow. He sought to suppress the letter under *[[Michigan v. Jackson]]* because police had initiated interrogation after counsel was appointed.

## Issue
Whether, once the Sixth Amendment right to counsel has attached and counsel has been appointed, a waiver of counsel during police-initiated interrogation is presumed invalid under *[[Michigan v. Jackson]]*.

## Rule
No — police are not categorically barred from initiating interrogation. The Court overruled the *[[Michigan v. Jackson]]* presumption and held that a defendant may waive the Sixth Amendment right to counsel during police-initiated interrogation even after counsel has been requested or appointed, provided the waiver is voluntary, knowing, and intelligent. A standard set of *[[Miranda v. Arizona|Miranda]]* warnings and waiver ordinarily suffices to relinquish the Sixth Amendment right, because the *Miranda–Edwards–Minnick* line already protects a defendant who does not wish to be questioned without counsel. "Michigan v. Jackson should be and now is overruled." — 556 U.S. at 797. ^pin-797

## Application
Because the *[[Michigan v. Jackson|Jackson]]* presumption no longer applies, the fact that counsel had been appointed at Montejo's 72-hour hearing did not by itself render his later waiver invalid. The Court did not decide admissibility itself; it [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] so that Montejo could argue — under *[[Edwards v. Arizona]]*, a theory he had not raised below — that he had earlier invoked his right to counsel and that his letter of apology should therefore be suppressed.

## Conclusion
The Louisiana Supreme Court correctly rejected Montejo's *[[Michigan v. Jackson|Jackson]]* claim, but the judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]] to allow Montejo to pursue an *[[Edwards v. Arizona|Edwards]]*-based suppression argument.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Montejo **overruled** [[Michigan v. Jackson]], eliminating the Sixth Amendment presumption against police-initiated interrogation after the right to counsel attaches; a defendant who does not wish to be questioned without counsel is now protected through the Fifth Amendment *[[Edwards v. Arizona|Edwards]]*/*[[Miranda v. Arizona|Miranda]]* regime.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Montejo v. Louisiana*, 556 U.S. 778 (2009) — https://www.courtlistener.com/opinion/145873/montejo-v-louisiana/ — pinpoint: 797 (CL opinion in slip-opinion format; U.S. Reports page per official citation).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f78b6f0b2c896587", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "556 U.S. 778 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 3973", "official_citation_present": true, "parallel_cite": "129 S. Ct. 2079; 173 L. Ed. 2d 955", "title": "Montejo v. Louisiana", "year": "2009"}}
{"assertion_id": "9a1f8e02b365d92c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A defendant may validly waive his Sixth Amendment right to counsel during police-initiated interrogation even after counsel has been…", "title": "Montejo v. Louisiana"}}
{"assertion_id": "9a2835d834003244", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "Montejo v. Louisiana"}}
{"assertion_id": "5dbf2a8bbbcfaa20", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-05-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Montejo v. Louisiana", "field_i_validity": "good_law", "scope_note": "Montejo itself overruled Michigan v. Jackson; Montejo is good law.", "title": "Montejo v. Louisiana", "varies_by_point": "false"}}
{"assertion_id": "e7721649038d0429", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Montejo v. Louisiana"}}
```

### lake record — Montejo v. Louisiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Montejo v. Louisiana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Montejo v. Louisiana",
    "case_name_short": "Montejo",
    "case_name_full": "Montejo v. Louisiana",
    "input_case_name": "Montejo v. Louisiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-05-26",
    "year": 2009,
    "docket": null,
    "cluster_id": 145873,
    "lead_opinion_id": 145873,
    "sibling_ids": [
      145873,
      9435335,
      9435336
    ],
    "absolute_url": "/opinion/145873/montejo-v-louisiana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 778",
      "volume": "556",
      "reporter": "U.S.",
      "page": "778",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 2079",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "2079",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 955",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "955",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 3973",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3973",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 778",
        "volume": "556",
        "reporter": "U.S.",
        "page": "778",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 2079",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "2079",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 955",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "955",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 3973",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3973",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 778",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 778",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-797",
      "page": null,
      "quote": "the court ordered the appointment of counsel. Before Montejo met his appointed lawyer, detectives read him his *Miranda* rights; he agreed to accompany them to locate the murder weapon and, during the trip, wrote an inculpatory letter of apology to the victim's widow. He sought to suppress the letter under *Michigan v. Jackson* because police had initiated interrogation after counsel was appointed. ## Issue Whether, once the Sixth Amendment right to counsel has attached and counsel has been appointed, a waiver of counsel during police-initiated interrogation is presumed invalid under *Michigan v. Jackson*. ## Rule No \u2014 police are not categorically barred from initiating interrogation. The Court overruled the *Michigan v. Jackson* presumption and held that a defendant may waive the Sixth Amendment right to counsel during police-initiated interrogation even after counsel has been requested or appointed, provided the waiver is voluntary, knowing, and intelligent. A standard set of *Miranda* warnings and waiver ordinarily suffices to relinquish the Sixth Amendment right, because the *Miranda\u2013Edwards\u2013Minnick* line already protects a defendant who does not wish to be questioned without counsel.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-05-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Montejo v. Louisiana",
    "varies_by_point": false,
    "scope_note": "Montejo itself overruled Michigan v. Jackson; Montejo is good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "the State of Texas v. Kevin Castanedanieto",
          "cluster_id": 7857287,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cook v. State",
          "cluster_id": 10679925,
          "cite": [
            "870 S.E.2d 758",
            "313 Ga. 471"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 9231323,
          "cite": [
            "140 S. Ct. 1390",
            "206 L. Ed. 2d 583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dwight Smith",
          "cluster_id": 4452817,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4348984,
          "cite": [
            "848 F.3d 767",
            "2017 FED App. 0034P",
            "2017 WL 603848",
            "2017 U.S. App. LEXIS 2629"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gustavo Andres Vasquez v. State",
          "cluster_id": 4252017,
          "cite": [
            "501 S.W.3d 691",
            "2016 Tex. App. LEXIS 9349",
            "2016 WL 4483462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Neary-French",
          "cluster_id": 4247088,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Francis",
          "cluster_id": 4243552,
          "cite": [
            "140 A.3d 927",
            "322 Conn. 247",
            "2016 Conn. LEXIS 231"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Bergeron",
          "cluster_id": 3207734,
          "cite": [
            "824 F.3d 148",
            "2016 U.S. App. LEXIS 9732",
            "2016 WL 3031089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martinez v. Ryan",
          "cluster_id": 625711,
          "cite": [
            "182 L. Ed. 2d 272",
            "132 S. Ct. 1309",
            "566 U.S. 1",
            "2012 U.S. LEXIS 2317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Frye",
          "cluster_id": 626055,
          "cite": [
            "182 L. Ed. 2d 379",
            "132 S. Ct. 1399",
            "566 U.S. 134",
            "2012 U.S. LEXIS 2321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Citizens United v. Federal Election Commission",
          "cluster_id": 1741,
          "cite": [
            "175 L. Ed. 2d 753",
            "130 S. Ct. 876",
            "558 U.S. 310",
            "2010 U.S. LEXIS 766",
            "22 Fla. L. Weekly Fed. S 73",
            "78 U.S.L.W. 4078",
            "187 L.R.R.M. (BNA) 2961",
            "159 Lab. Cas. (CCH) 10,166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jae Lee v. United States",
          "cluster_id": 4403800,
          "cite": [
            "582 U.S. 357",
            "2017 U.S. LEXIS 4045",
            "137 S. Ct. 1958",
            "198 L. Ed. 2d 476",
            "26 Fla. L. Weekly Fed. S 733",
            "85 U.S.L.W. 4412",
            "2017 WL 2694701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Morrow v. Barry Balaski",
          "cluster_id": 891221,
          "cite": [
            "719 F.3d 160",
            "98 A.L.R. 6th 777",
            "2013 WL 2466892",
            "2013 U.S. App. LEXIS 11246"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janus v. State, County, and Municipal Employees",
          "cluster_id": 4511640,
          "cite": [
            "585 U.S. 878",
            "138 S. Ct. 2448",
            "201 L. Ed. 2d 924",
            "2018 U.S. LEXIS 4028"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loper Bright Enterprises v. Raimondo",
          "cluster_id": 10600041,
          "cite": [
            "603 U.S. 369"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loper Bright Enterprises v. Raimondo",
          "cluster_id": 9986254,
          "cite": [
            "603 U.S. 369"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cox",
          "cluster_id": 2345288,
          "cite": [
            "983 A.2d 666",
            "603 Pa. 223",
            "2009 Pa. LEXIS 2423"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bobby v. Dixon",
          "cluster_id": 616807,
          "cite": [
            "181 L. Ed. 2d 328",
            "132 S. Ct. 26",
            "565 U.S. 23",
            "2011 U.S. LEXIS 7926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lansing Schools Education Ass'n v. Lansing Board of Education",
          "cluster_id": 830370,
          "cite": [
            "487 Mich. 349"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hooks v. Workman",
          "cluster_id": 805977,
          "cite": [
            "689 F.3d 1148",
            "2012 WL 3140916",
            "2012 U.S. App. LEXIS 16150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 4746633,
          "cite": [
            "590 U.S. 83"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gamble v. United States",
          "cluster_id": 4630267,
          "cite": [
            "587 U.S. 678",
            "139 S. Ct. 1960",
            "204 L. Ed. 2d 322",
            "2019 U.S. LEXIS 4173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bonilla-Barraza",
          "cluster_id": 2625609,
          "cite": [
            "209 P.3d 1090",
            "2009 WL 1741945"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 1346679,
          "cite": [
            "697 S.E.2d 757",
            "287 Ga. 646",
            "2010 Fulton County D. Rep. 2574",
            "2010 Ga. LEXIS 484"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Tekoh",
          "cluster_id": 6480695,
          "cite": [
            "597 U.S. 134",
            "213 L. Ed. 2d 479",
            "142 S. Ct. 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eldridge v. Johndrow",
          "cluster_id": 2775233,
          "cite": [
            "2015 UT 21",
            "345 P.3d 553",
            "2015 Utah LEXIS 67",
            "779 Utah Adv. Rep. 112",
            "2015 WL 404491"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ayers v. Hudson",
          "cluster_id": 176545,
          "cite": [
            "623 F.3d 301",
            "2010 U.S. App. LEXIS 20487",
            "2010 WL 3894463"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pecina, Alfredo Leyva",
          "cluster_id": 2947167,
          "cite": [
            "361 S.W.3d 68",
            "2012 WL 204293",
            "2012 Tex. Crim. App. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Howard Hawk Willis",
          "cluster_id": 4236316,
          "cite": [
            "496 S.W.3d 653",
            "2016 Tenn. LEXIS 405"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145873 OR 9435335 OR 9435336) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDM4NzMyODAwMDAwJnM9MjgyNjA1MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145873+OR+9435335+OR+9435336%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(145873 OR 9435335 OR 9435336)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MyZzPTgwNTkxMyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145873+OR+9435335+OR+9435336%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145873 OR 9435335 OR 9435336)",
        "reviewed": 49,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 49,
        "triage_read": 0,
        "triage_snippet_classified": 49
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145873 OR 9435335 OR 9435336)",
    "indexed_citing_opinions": 391,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145873,
        "count": 307,
        "count_source": "search"
      },
      {
        "opinion_id": 9435335,
        "count": 93,
        "count_source": "search"
      },
      {
        "opinion_id": 9435336,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 669,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/montejo-v-louisiana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTMwNDMmcz0xMDAxNzc3NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145873+OR+9435335+OR+9435336%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145873,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 117863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 118417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 134725,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 142900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 577034,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 1793654,
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
    "date_created": "2026-07-05T14:30:21Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:30:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:30:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:36:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:30:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Montejo v. Louisiana

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

                       MONTEJO v. LOUISIANA

      CERTIORARI TO THE SUPREME COURT OF LOUISIANA

    No. 07–1529. Argued January 13, 2009—Decided May 26, 2009
At a preliminary hearing required by Louisiana law, petitioner Montejo
  was charged with first-degree murder, and the court ordered the ap
  pointment of counsel. Later that day, the police read Montejo his
  rights under Miranda v. Arizona, 384 U. S. 436, and he agreed to go
  along on a trip to locate the murder weapon. During the excursion,
  he wrote an inculpatory letter of apology to the victim’s widow. Upon
  returning, he finally met his court-appointed attorney. At trial, his
  letter was admitted over defense objection, and he was convicted and
  sentenced to death. Affirming, the State Supreme Court rejected his
  claim that the letter should have been suppressed under the rule of
  Michigan v. Jackson, 475 U. S. 625, which forbids police to initiate
  interrogation of a criminal defendant once he has invoked his right to
  counsel at an arraignment or similar proceeding. The court reasoned
  that Jackson’s prophylactic protection is not triggered unless the de
  fendant has actually requested a lawyer or has otherwise asserted
  his Sixth Amendment right to counsel; and that, since Montejo stood
  mute at his hearing while the judge ordered the appointment of
  counsel, he had made no such request or assertion.
Held:
    1. Michigan v. Jackson should be and now is overruled. Pp. 3–18.
       (a) The State Supreme Court’s interpretation of Jackson would
 lead to practical problems. Requiring an initial “invocation” of the
 right to counsel in order to trigger the Jackson presumption, as the
 court below did, might work in States that require an indigent defen
 dant formally to request counsel before an appointment is made, but
 not in more than half the States, which appoint counsel without re
 quest from the defendant. Pp. 3–6.
       (b) On the other hand, Montejo’s solution is untenable as a theo
 retical and doctrinal matter. Eliminating the invocation requirement
2                       MONTEJO v. LOUISIANA

                                  Syllabus

    entirely would depart fundamentally from the rationale of Jackson,
    whose presumption was created by analogy to a similar prophylactic
    rule established in Edwards v. Arizona, 451 U. S. 477, to protect the
    Fifth Amendment-based Miranda right. Both Edwards and Jackson
    are meant to prevent police from badgering defendants into changing
    their minds about the right to counsel once they have invoked it, but
    a defendant who never asked for counsel has not yet made up his
    mind in the first instance. Pp. 6–13.
          (c) Stare decisis does not require the Court to expand signifi
    cantly the holding of a prior decision in order to cure its practical de
    ficiencies. To the contrary, the fact that a decision has proved “un
    workable” is a traditional ground for overruling it. Payne v.
    Tennessee, 501 U. S. 808, 827. Beyond workability, the relevant fac
    tors include the precedent’s antiquity, the reliance interests at stake,
    and whether the decision was well reasoned. Pearson v. Callahan,
    555 U. S. ___, ___. The first two cut in favor of jettisoning Jackson:
    the opinion is only two decades old, and eliminating it would not up
    set expectations, since any criminal defendant learned enough to or
    der his affairs based on Jackson’s rule would also be perfectly capable
    of interacting with the police on his own. As for the strength of Jack
    son’s reasoning, when this Court creates a prophylactic rule to pro
    tect a constitutional right, the relevant “reasoning” is the weighing of
    the rule’s benefits against its costs. Jackson’s marginal benefits are
    dwarfed by its substantial costs. Even without Jackson, few badger
    ing-induced waivers, if any, would be admitted at trial because the
    Court has taken substantial other, overlapping measures to exclude
    them. Under Miranda, any suspect subject to custodial interrogation
    must be advised of his right to have a lawyer present. 384 U. S., at
    474. Under Edwards, once such a defendant “has invoked his
    [Miranda] right,” interrogation must stop. 451 U. S., at 484. And
    under Minnick v. Mississippi, 498 U. S. 146, no subsequent interro
    gation may take place until counsel is present. Id., at 153. These
    three layers of prophylaxis are sufficient. On the other side of the
    equation, the principal cost of applying Jackson’s rule is that crimes
    can go unsolved and criminals unpunished when uncoerced confes
    sions are excluded and when officers are deterred from even trying to
    obtain confessions. The Court concludes that the Jackson rule does
    not “pay its way,” United States v. Leon, 468 U. S. 897, 907–908, n. 6,
    and thus the case should be overruled. Pp. 13–18.
       2. Montejo should nonetheless be given an opportunity to contend
    that his letter of apology should have been suppressed under the Ed
    wards rule. He understandably did not pursue an Edwards objec
    tion, because Jackson offered broader protections, but the decision
    here changes the legal landscape. Pp. 18–19.
                     Cite as: 556 U. S. ____ (2009)                    3

                                Syllabus

06–1807 (La.), 974 So. 2d 1238, vacated and remanded.

  SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, THOMAS, and ALITO, JJ., joined. ALITO, J., filed a
concurring opinion, in which KENNEDY, J., joined. STEVENS, J., filed a
dissenting opinion, in which SOUTER and GINSBURG, JJ., joined, and in
which BREYER, J., joined, except for n. 5. BREYER, J., filed a dissenting
opinion.
                        Cite as: 556 U. S. ____ (2009)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 07–1529
                                   _________________


          JESSE JAY MONTEJO, PETITIONER v. 

                     LOUISIANA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      LOUISIANA

                                 [May 26, 2009] 


   JUSTICE SCALIA delivered the opinion of the Court.
   We consider in this case the scope and continued viabil
ity of the rule announced by this Court in Michigan v.
Jackson, 475 U. S. 625 (1986), forbidding police to initiate
interrogation of a criminal defendant once he has re
quested counsel at an arraignment or similar proceeding.
                              I
  Petitioner Jesse Montejo was arrested on September 6,
2002, in connection with the robbery and murder of Lewis
Ferrari, who had been found dead in his own home one
day earlier. Suspicion quickly focused on Jerry Moore, a
disgruntled former employee of Ferrari’s dry cleaning
business. Police sought to question Montejo, who was a
known associate of Moore.
  Montejo waived his rights under Miranda v. Arizona,
384 U. S. 436 (1966), and was interrogated at the sheriff’s
office by police detectives through the late afternoon and
evening of September 6 and the early morning of Septem
ber 7. During the interrogation, Montejo repeatedly
changed his account of the crime, at first claiming that he
2                     MONTEJO v. LOUISIANA

                          Opinion of the Court

had only driven Moore to the victim’s home, and ulti
mately admitting that he had shot and killed Ferrari in
the course of a botched burglary. These police interroga
tions were videotaped.
   On September 10, Montejo was brought before a judge
for what is known in Louisiana as a “72-hour hearing”—a
preliminary hearing required under state law.1 Although
the proceedings were not transcribed, the minute record
indicates what transpired: “The defendant being charged
with First Degree Murder, Court ordered N[o] Bond set in
this matter. Further, Court ordered the Office of Indigent
Defender be appointed to represent the defendant.” App.
to Pet. for Cert. 63a.
   Later that same day, two police detectives visited Mon
tejo back at the prison and requested that he accompany
them on an excursion to locate the murder weapon (which
Montejo had earlier indicated he had thrown into a lake).
After some back-and-forth, the substance of which re
mains in dispute, Montejo was again read his Miranda
rights and agreed to go along; during the excursion, he
wrote an inculpatory letter of apology to the victim’s
widow. Only upon their return did Montejo finally meet
his court-appointed attorney, who was quite upset that the
detectives had interrogated his client in his absence.
   At trial, the letter of apology was admitted over defense
objection. The jury convicted Montejo of first-degree mur
der, and he was sentenced to death.
   The Louisiana Supreme Court affirmed the conviction
and sentence. 06–1807 (1/16/08), 974 So. 2d 1238 (2008).
As relevant here, the court rejected Montejo’s argument
that under the rule of Jackson, supra, the letter should
——————
  1 “The sheriff or law enforcement officer having custody of an arrested

person shall bring him promptly, and in any case within seventy-two
hours from the time of the arrest, before a judge for the purpose of
appointment of counsel.” La. Code Crim. Proc. Ann., Art. 230.1(A)
(West Supp. 2009).
                 Cite as: 556 U. S. ____ (2009)            3

                     Opinion of the Court

have been suppressed. 974 So. 2d, at 1261. Jackson held
that “if police initiate interrogation after a defendant’s
assertion, at an arraignment or similar proceeding, of his
right to counsel, any waiver of the defendant’s right to
counsel for that police-initiated interrogation is invalid.”
475 U. S., at 636.
  Citing a decision of the United States Court of Appeals
for the Fifth Circuit, Montoya v. Collins, 955 F. 2d 279
(1992), the Louisiana Supreme Court reasoned that the
prophylactic protection of Jackson is not triggered unless
and until the defendant has actually requested a lawyer or
has otherwise asserted his Sixth Amendment right to
counsel. 974 So. 2d, at 1260–1261, and n. 68. Because
Montejo simply stood mute at his 72-hour hearing while
the judge ordered the appointment of counsel, he had
made no such request or assertion. So the proper inquiry,
the court ruled, was only whether he had knowingly,
intelligently, and voluntarily waived his right to have
counsel present during the interaction with the police. Id.,
at 1261. And because Montejo had been read his Miranda
rights and agreed to waive them, the Court answered that
question in the affirmative, 974 So. 2d, at 1262, and up
held the conviction.
  We granted certiorari. 554 U. S. ___ (2008).
                            II
   Montejo and his amici raise a number of pragmatic
objections to the Louisiana Supreme Court’s interpreta
tion of Jackson. We agree that the approach taken below
would lead either to an unworkable standard, or to arbi
trary and anomalous distinctions between defendants in
different States. Neither would be acceptable.
   Under the rule adopted by the Louisiana Supreme
Court, a criminal defendant must request counsel, or
otherwise “assert” his Sixth Amendment right at the
preliminary hearing, before the Jackson protections are
4                 MONTEJO v. LOUISIANA

                     Opinion of the Court

triggered. If he does so, the police may not initiate further
interrogation in the absence of counsel. But if the court on
its own appoints counsel, with the defendant taking no
affirmative action to invoke his right to counsel, then
police are free to initiate further interrogations provided
that they first obtain an otherwise valid waiver by the
defendant of his right to have counsel present.
   This rule would apply well enough in States that require
the indigent defendant formally to request counsel before
any appointment is made, which usually occurs after the
court has informed him that he will receive counsel if he
asks for it. That is how the system works in Michigan, for
example, Mich. Ct. Rule 6.005(A) (2009), whose scheme
produced the factual background for this Court’s decision
in Michigan v. Jackson. Jackson, like all other repre
sented indigent defendants in the State, had requested
counsel in accordance with the applicable state law.
   But many States follow other practices. In some two
dozen, the appointment of counsel is automatic upon a
finding of indigency, e.g., Kan. Stat. Ann. §22–4503(c)
(2007); and in a number of others, appointment can be
made either upon the defendant’s request or sua sponte by
the court, e.g., Del. Code Ann., Tit. 29, §4602(a) (2003).
See App. to Brief for National Legal Aid & Defender Assn.
et al. as Amici Curiae 1a–21a. Nothing in our Jackson
opinion indicates whether we were then aware that not all
States require that a defendant affirmatively request
counsel before one is appointed; and of course we had no
occasion there to decide how the rule we announced would
apply to these other States.
   The Louisiana Supreme Court’s answer to that unre
solved question is troublesome. The central distinction it
draws—between defendants who “assert” their right to
counsel and those who do not—is exceedingly hazy when
applied to States that appoint counsel absent request from
the defendant. How to categorize a defendant who merely
                 Cite as: 556 U. S. ____ (2009)            5

                     Opinion of the Court

asks, prior to appointment, whether he will be appointed
counsel? Or who inquires, after the fact, whether he has
been? What treatment for one who thanks the court after
the appointment is made? And if the court asks a defen
dant whether he would object to appointment, will a quick
shake of his head count as an assertion of his right?
  To the extent that the Louisiana Supreme Court’s rule
also permits a defendant to trigger Jackson through the
“acceptance” of counsel, that notion is even more mysteri
ous: How does one affirmatively accept counsel appointed
by court order? An indigent defendant has no right to
choose his counsel, United States v. Gonzalez-Lopez, 548
U. S. 140, 151 (2006), so it is hard to imagine what his
“acceptance” would look like, beyond the passive silence
that Montejo exhibited.
  In practice, judicial application of the Louisiana rule in
States that do not require a defendant to make a request
for counsel could take either of two paths. Courts might
ask on a case-by-case basis whether a defendant has
somehow invoked his right to counsel, looking to his con
duct at the preliminary hearing—his statements and
gestures—and the totality of the circumstances. Or,
courts might simply determine as a categorical matter
that defendants in these States—over half of those in the
Union—simply have no opportunity to assert their right to
counsel at the hearing and are therefore out of luck.
  Neither approach is desirable. The former would be
particularly impractical in light of the fact that, as amici
describe, preliminary hearings are often rushed, and are
frequently not recorded or transcribed. Brief for National
Legal Aid & Defender Assn. et al. 25–30. The sheer vol
ume of indigent defendants, see id., at 29, would render
the monitoring of each particular defendant’s reaction to
the appointment of counsel almost impossible. And some
times the defendant is not even present. E.g., La. Code
Crim. Proc. Ann., Art. 230.1(A) (West Supp. 2009) (allow
6                 MONTEJO v. LOUISIANA

                     Opinion of the Court

ing court to appoint counsel if defendant is “unable to
appear”). Police who did not attend the hearing would
have no way to know whether they could approach a par
ticular defendant; and for a court to adjudicate that ques
tion ex post would be a fact-intensive and burdensome
task, even if monitoring were possible and transcription
available. Because “clarity of . . . command” and “cer
tainty of . . . application” are crucial in rules that govern
law enforcement, Minnick v. Mississippi, 498 U. S. 146,
151 (1990), this would be an unfortunate way to proceed.
See also Moran v. Burbine, 475 U. S. 412, 425–426 (1986).
   The second possible course fares no better, for it would
achieve clarity and certainty only at the expense of intro
ducing arbitrary distinctions: Defendants in States that
automatically appoint counsel would have no opportunity
to invoke their rights and trigger Jackson, while those in
other States, effectively instructed by the court to request
counsel, would be lucky winners. That sort of hollow
formalism is out of place in a doctrine that purports to
serve as a practical safeguard for defendants’ rights.
                             III
  But if the Louisiana Supreme Court’s application of
Jackson is unsound as a practical matter, then Montejo’s
solution is untenable as a theoretical and doctrinal matter.
Under his approach, once a defendant is represented by
counsel, police may not initiate any further interrogation.
Such a rule would be entirely untethered from the original
rationale of Jackson.
                                A
  It is worth emphasizing first what is not in dispute or at
stake here. Under our precedents, once the adversary
judicial process has been initiated, the Sixth Amendment
guarantees a defendant the right to have counsel present
at all “critical” stages of the criminal proceedings. United
                 Cite as: 556 U. S. ____ (2009)           7

                     Opinion of the Court

States v. Wade, 388 U. S. 218, 227–228 (1967); Powell v.
Alabama, 287 U. S. 45, 57 (1932). Interrogation by the
State is such a stage. Massiah v. United States, 377 U. S.
201, 204–205 (1964); see also United States v. Henry, 447
U. S. 264, 274 (1980).
  Our precedents also place beyond doubt that the Sixth
Amendment right to counsel may be waived by a defen
dant, so long as relinquishment of the right is voluntary,
knowing, and intelligent. Patterson v. Illinois, 487 U. S.
285, 292, n. 4 (1988); Brewer v. Williams, 430 U. S. 387,
404 (1977); Johnson v. Zerbst, 304 U. S. 458, 464 (1938).
The defendant may waive the right whether or not he is
already represented by counsel; the decision to waive need
not itself be counseled. Michigan v. Harvey, 494 U. S. 344,
352–353 (1990). And when a defendant is read his
Miranda rights (which include the right to have counsel
present during interrogation) and agrees to waive those
rights, that typically does the trick, even though the
Miranda rights purportedly have their source in the Fifth
Amendment:
    “As a general matter . . . an accused who is admon
    ished with the warnings prescribed by this Court in
    Miranda . . . has been sufficiently apprised of the na
    ture of his Sixth Amendment rights, and of the conse
    quences of abandoning those rights, so that his waiver
    on this basis will be considered a knowing and intelli
    gent one.” Patterson, supra, at 296.
   The only question raised by this case, and the only one
addressed by the Jackson rule, is whether courts must
presume that such a waiver is invalid under certain cir
cumstances. 475 U. S., at 630, 633. We created such a
presumption in Jackson by analogy to a similar prophylac
tic rule established to protect the Fifth Amendment based
Miranda right to have counsel present at any custodial
interrogation. Edwards v. Arizona, 451 U. S. 477 (1981),
8                 MONTEJO v. LOUISIANA

                     Opinion of the Court

decided that once “an accused has invoked his right to
have counsel present during custodial interrogation . . .
[he] is not subject to further interrogation by the authori
ties until counsel has been made available,” unless he
initiates the contact. Id., at 484–485.
   The Edwards rule is “designed to prevent police from
badgering a defendant into waiving his previously as
serted Miranda rights,” Harvey, supra, at 350. It does this
by presuming his postassertion statements to be involun
tary, “even where the suspect executes a waiver and his
statements would be considered voluntary under tradi
tional standards.” McNeil v. Wisconsin, 501 U. S. 171, 177
(1991). This prophylactic rule thus “protect[s] a suspect’s
voluntary choice not to speak outside his lawyer’s pres
ence.” Texas v. Cobb, 532 U. S. 162, 175 (2001) (KENNEDY,
J., concurring).
   Jackson represented a “wholesale importation of the
Edwards rule into the Sixth Amendment.” Cobb, supra, at
175. The Jackson Court decided that a request for counsel
at an arraignment should be treated as an invocation of
the Sixth Amendment right to counsel “at every critical
stage of the prosecution,” 475 U. S., at 633, despite doubt
that defendants “actually inten[d] their request for counsel
to encompass representation during any further question
ing,” id., at 632–633, because doubts must be “resolved in
favor of protecting the constitutional claim,” id., at 633.
Citing Edwards, the Court held that any subsequent
waiver would thus be “insufficient to justify police
initiated interrogation.” 475 U. S., at 635. In other words,
we presume such waivers involuntary “based on the sup
position that suspects who assert their right to counsel are
unlikely to waive that right voluntarily” in subsequent
interactions with police. Harvey, supra, at 350.
   The dissent presents us with a revisionist view of Jack
son. The defendants’ request for counsel, it contends, was
important only because it proved that counsel had been
                     Cite as: 556 U. S. ____ (2009)                    9

                          Opinion of the Court

appointed. Such a non sequitur (nowhere alluded to in the
case) hardly needs rebuttal. Proceeding from this fanciful
premise, the dissent claims that the decision actually
established “a rule designed to safeguard a defendant’s
right to rely on the assistance of counsel,” post, at 6–7
(opinion of STEVENS, J.), not one “designed to prevent
police badgering,” post, at 7. To safeguard the right to
assistance of counsel from what? From a knowing and
voluntary waiver by the defendant himself? Unless the
dissent seeks to prevent a defendant altogether from
waiving his Sixth Amendment rights, i.e., to “imprison a
man in his privileges and call it the Constitution,” Adams
v. United States ex rel. McCann, 317 U. S. 269, 280
(1942)—a view with zero support in reason, history or case
law—the answer must be: from police pressure, i.e., badg
ering. The antibadgering rationale is the only way to
make sense of Jackson’s repeated citations of Edwards,
and the only way to reconcile the opinion with our waiver
jurisprudence.2
                            B
  With this understanding of what Jackson stands for and
whence it came, it should be clear that Montejo’s interpre
tation of that decision—that no represented defendant can
ever be approached by the State and asked to consent to
interrogation—is off the mark. When a court appoints
counsel for an indigent defendant in the absence of any
request on his part, there is no basis for a presumption
——————
   2 The dissent responds that Jackson also ensures that the defendant’s

counsel receives notice of any interrogation, post, at 6, n. 2.
But notice to what end? Surely not in order to protect some constitu
tional right to receive counsel’s advice regarding waiver of the right to
have counsel present. Contrary to the dissent’s intimations, neither the
advice nor the presence of counsel is needed in order to effectuate a
knowing waiver of the Sixth Amendment right. Our cases make clear
that the Miranda waivers typically suffice; indeed, even an unrepre
sented defendant can waive his right to counsel. See supra, at 7.
10                MONTEJO v. LOUISIANA

                     Opinion of the Court

that any subsequent waiver of the right to counsel will be
involuntary. There is no “initial election” to exercise the
right, Patterson, 487 U. S., at 291, that must be preserved
through a prophylactic rule against later waivers. No
reason exists to assume that a defendant like Montejo,
who has done nothing at all to express his intentions with
respect to his Sixth Amendment rights, would not be
perfectly amenable to speaking with the police without
having counsel present. And no reason exists to prohibit
the police from inquiring. Edwards and Jackson are
meant to prevent police from badgering defendants into
changing their minds about their rights, but a defendant
who never asked for counsel has not yet made up his mind
in the first instance.
  The dissent’s argument to the contrary rests on a flawed
a fortiori: “If a defendant is entitled to protection from
police-initiated interrogation under the Sixth Amendment
when he merely requests a lawyer, he is even more obvi
ously entitled to such protection when he has secured a
lawyer.” Post, at 3. The question in Jackson, however,
was not whether respondents were entitled to counsel
(they unquestionably were), but “whether respondents
validly waived their right to counsel,” 475 U. S., at 630;
and even if it is reasonable to presume from a defendant’s
request for counsel that any subsequent waiver of the right
was coerced, no such presumption can seriously be enter
tained when a lawyer was merely “secured” on the defen
dant’s behalf, by the State itself, as a matter of course. Of
course, reading the dissent’s analysis, one would have no
idea that Montejo executed any waiver at all.
  In practice, Montejo’s rule would prevent police-initiated
interrogation entirely once the Sixth Amendment right
attaches, at least in those States that appoint counsel
promptly without request from the defendant. As the
dissent in Jackson pointed out, with no expressed dis
agreement from the majority, the opinion “most assuredly
                 Cite as: 556 U. S. ____ (2009)          11

                     Opinion of the Court

[did] not hold that the Edwards per se rule prohibiting all
police-initiated interrogations applies from the moment
the defendant’s Sixth Amendment right to counsel at
taches, with or without a request for counsel by the defen
dant.” 475 U. S., at 640 (opinion of Rehnquist, J.). That
would have constituted a “shockingly dramatic restructur
ing of the balance this Court has traditionally struck
between the rights of the defendant and those of the larger
society.” Ibid.
  Montejo’s rule appears to have its theoretical roots in
codes of legal ethics, not the Sixth Amendment. The
American Bar Association’s Model Rules of Professional
Conduct (which nearly all States have adopted into law in
whole or in part) mandate that “a lawyer shall not com
municate about the subject of [a] representation with a
party the lawyer knows to be represented by another
lawyer in the matter, unless the lawyer has the consent of
the other lawyer or is authorized to do so by law or a court
order.” Model Rule 4.2 (2008). But the Constitution does
not codify the ABA’s Model Rules, and does not make
investigating police officers lawyers. Montejo’s proposed
rule is both broader and narrower than the Model Rule.
Broader, because Montejo would apply it to all agents of
the State, including the detectives who interrogated him,
while the ethical rule governs only lawyers. And nar
rower, because he agrees that if a defendant initiates
contact with the police, they may talk freely—whereas a
lawyer could be sanctioned for interviewing a represented
party even if that party “initiates” the communication and
consents to the interview. Model Rule 4.2, Comment 3.
  Montejo contends that our decisions support his inter
pretation of the Jackson rule. We think not. Many of the
cases he cites concern the substantive scope of the Sixth
Amendment—e.g., whether a particular interaction with
the State constitutes a “critical” stage at which counsel is
entitled to be present—not the validity of a Sixth Amend
12                     MONTEJO v. LOUISIANA

                          Opinion of the Court

ment waiver. See Maine v. Moulton, 474 U. S. 159 (1985);
Henry, 447 U. S. 264; Massiah, 377 U. S. 201; see also
Moran, 475 U. S. 412. Since everyone agrees that absent a
valid waiver, Montejo was entitled to a lawyer during the
interrogation, those cases do not advance his argument.
   Montejo also points to descriptions of the Jackson hold
ing in two later cases. In one, we noted that “analysis of
the waiver issue changes” once a defendant “obtains or
even requests counsel.” Harvey, 494 U. S., at 352. But
elsewhere in the same opinion, we explained that Jackson
applies “after a defendant requests assistance of counsel,”
494 U. S., at 349; “when a suspect charged with a crime
requests counsel outside the context of interrogation,” id.,
at 350; and to “suspects who assert their right to counsel,”
ibid. The accuracy of the “obtains” language is thus ques
tionable. Anyway, since Harvey held that evidence ob
tained in violation of the Jackson rule could be admitted
to impeach the defendant’s trial testimony, 494 U. S., at
346, the Court’s varying descriptions of when the rule was
violated were dicta. The dictum from the other decision,
Patterson, supra, at 290, n. 3, is no more probative.3
   The upshot is that even on Jackson’s own terms, it

——————
  3 In the cited passage, the Court noted that “[o]nce an accused has a

lawyer, a distinct set of constitutional safeguards aimed at preserving
the sanctity of attorney-client relationship takes effect.” Patterson, 487
U. S., at 290, n. 3. To support that proposition, the Court cited Maine
v. Moulton, 474 U. S. 159 (1985), which was not a case about waiver.
The passage went on to observe that “the analysis changes markedly
once an accused even requests the assistance of counsel,” 487 U. S., at
290, n. 3 (emphasis in original), this time citing Jackson. Montejo
infers from the “even requests” that having counsel is more conclusive of
the invalidity of uncounseled waiver than the mere requesting of
counsel. But the Patterson footnote did not suggest that the analysis
“changes” in both these scenarios (having a lawyer, versus requesting
one) with specific reference to the validity of waivers under the Sixth
Amendment. The citation of Moulton (a nonwaiver case) for the first
scenario suggests just the opposite.
                 Cite as: 556 U. S. ____ (2009)          13

                     Opinion of the Court

would be completely unjustified to presume that a defen
dant’s consent to police-initiated interrogation was invol
untary or coerced simply because he had previously been
appointed a lawyer.
                             IV
   So on the one hand, requiring an initial “invocation” of
the right to counsel in order to trigger the Jackson pre
sumption is consistent with the theory of that decision, but
(as Montejo and his amici argue, see Part II, supra) would
be unworkable in more than half the States of the Union.
On the other hand, eliminating the invocation require
ment would render the rule easy to apply but depart fun
damentally from the Jackson rationale.
   We do not think that stare decisis requires us to expand
significantly the holding of a prior decision—
fundamentally revising its theoretical basis in the proc
ess—in order to cure its practical deficiencies. To the
contrary, the fact that a decision has proved “unworkable”
is a traditional ground for overruling it. Payne v. Tennes
see, 501 U. S. 808, 827 (1991). Accordingly, we called for
supplemental briefing addressed to the question whether
Michigan v. Jackson should be overruled.
   Beyond workability, the relevant factors in deciding
whether to adhere to the principle of stare decisis include
the antiquity of the precedent, the reliance interests at
stake, and of course whether the decision was well rea
soned. Pearson v. Callahan, 555 U. S. ___, ___ (2009) (slip
op., at 8). The first two cut in favor of abandoning Jack
son: the opinion is only two decades old, and eliminating it
would not upset expectations. Any criminal defendant
learned enough to order his affairs based on the rule
announced in Jackson would also be perfectly capable of
interacting with the police on his own. Of course it is
likely true that police and prosecutors have been trained
to comply with Jackson, see generally Supplemental Brief
14                     MONTEJO v. LOUISIANA

                           Opinion of the Court

for Larry D. Thompson et al. as Amici Curiae, but that is
hardly a basis for retaining it as a constitutional require
ment. If a State wishes to abstain from requesting inter
views with represented defendants when counsel is not
present, it obviously may continue to do so.4
  Which brings us to the strength of Jackson’s reasoning.
When this Court creates a prophylactic rule in order to
protect a constitutional right, the relevant “reasoning” is
the weighing of the rule’s benefits against its costs. “The
value of any prophylactic rule . . . must be assessed not
only on the basis of what is gained, but also on the basis of
what is lost.” Minnick, 498 U. S., at 161 (SCALIA, J., dis
senting). We think that the marginal benefits of Jackson
(viz., the number of confessions obtained coercively that
are suppressed by its bright-line rule and would otherwise
have been admitted) are dwarfed by its substantial costs
(viz., hindering “society’s compelling interest in finding,
convicting, and punishing those who violate the law,”
Moran, supra, at 426).
  What does the Jackson rule actually achieve by way of
preventing unconstitutional conduct? Recall that the
purpose of the rule is to preclude the State from badgering
defendants into waiving their previously asserted rights.
See Harvey, supra, at 350; see also McNeil, 501 U. S., at
177. The effect of this badgering might be to coerce a
waiver, which would render the subsequent interrogation
a violation of the Sixth Amendment. See Massiah, supra,
at 204. Even though involuntary waivers are invalid even
——————
  4 The dissent posits a different reliance interest: “the public’s interest
in knowing that counsel, once secured, may be reasonably relied upon
as a medium between the accused and the power of the State,” post, at
9. We suspect the public would be surprised to learn that a criminal
can freely sign away his right to a lawyer, confess his crimes, and then
ask the courts to assume that the confession was coerced—on the
ground that he had, at some earlier point in time, made a pro forma
statement requesting that counsel be appointed on his behalf.
                 Cite as: 556 U. S. ____ (2009)           15

                     Opinion of the Court

apart from Jackson, see Patterson, 487 U. S., at 292, n. 4,
mistakes are of course possible when courts conduct case
by-case voluntariness review. A bright-line rule like that
adopted in Jackson ensures that no fruits of interrogations
made possible by badgering-induced involuntary waivers
are ever erroneously admitted at trial.
   But without Jackson, how many would be? The answer
is few if any. The principal reason is that the Court has
already taken substantial other, overlapping measures
toward the same end. Under Miranda’s prophylactic
protection of the right against compelled self
incrimination, any suspect subject to custodial interroga
tion has the right to have a lawyer present if he so re
quests, and to be advised of that right. 384 U. S., at 474.
Under Edwards’ prophylactic protection of the Miranda
right, once such a defendant “has invoked his right to have
counsel present,” interrogation must stop. 451 U. S., at
484. And under Minnick’s prophylactic protection of the
Edwards right, no subsequent interrogation may take
place until counsel is present, “whether or not the accused
has consulted with his attorney.” 498 U. S., at 153.
   These three layers of prophylaxis are sufficient. Under
the Miranda-Edwards-Minnick line of cases (which is not
in doubt), a defendant who does not want to speak to the
police without counsel present need only say as much
when he is first approached and given the Miranda warn
ings. At that point, not only must the immediate contact
end, but “badgering” by later requests is prohibited. If
that regime suffices to protect the integrity of “a suspect’s
voluntary choice not to speak outside his lawyer’s pres
ence” before his arraignment, Cobb, 532 U. S., at 175
(KENNEDY, J., concurring), it is hard to see why it would
not also suffice to protect that same choice after arraign
ment, when Sixth Amendment rights have attached. And
if so, then Jackson is simply superfluous.
   It is true, as Montejo points out in his supplemental
16                MONTEJO v. LOUISIANA

                     Opinion of the Court

brief, that the doctrine established by Miranda and Ed
wards is designed to protect Fifth Amendment, not Sixth
Amendment, rights. But that is irrelevant. What matters
is that these cases, like Jackson, protect the right to have
counsel during custodial interrogation—which right hap
pens to be guaranteed (once the adversary judicial process
has begun) by two sources of law. Since the right under
both sources is waived using the same procedure, Patter
son, supra, at 296, doctrines ensuring voluntariness of the
Fifth Amendment waiver simultaneously ensure the
voluntariness of the Sixth Amendment waiver.
   Montejo also correctly observes that the Miranda-
Edwards regime is narrower than Jackson in one respect:
The former applies only in the context of custodial interro
gation. If the defendant is not in custody then those deci
sions do not apply; nor do they govern other, noninterroga
tive types of interactions between the defendant and the
State (like pretrial lineups). However, those uncovered
situations are the least likely to pose a risk of coerced
waivers. When a defendant is not in custody, he is in
control, and need only shut his door or walk away to avoid
police badgering. And noninterrogative interactions with
the State do not involve the “inherently compelling pres
sures,” Miranda, supra, at 467, that one might reasonably
fear could lead to involuntary waivers.
   Jackson was policy driven, and if that policy is being
adequately served through other means, there is no reason
to retain its rule. Miranda and the cases that elaborate
upon it already guarantee not simply noncoercion in the
traditional sense, but what Justice Harlan referred to as
“voluntariness with a vengeance,” 384 U. S., at 505 (dis
senting opinion). There is no need to take Jackson’s fur
ther step of requiring voluntariness on stilts.
   On the other side of the equation are the costs of adding
the bright-line Jackson rule on top of Edwards and other
extant protections. The principal cost of applying any
                     Cite as: 556 U. S. ____ (2009)                   17

                          Opinion of the Court

exclusionary rule “is, of course, letting guilty and possibly
dangerous criminals go free . . . .” Herring v. United
States, 555 U. S. ___, ___ (2009) (slip op., at 6). Jackson
not only “operates to invalidate a confession given by the
free choice of suspects who have received proper advice of
their Miranda rights but waived them nonetheless,” Cobb,
supra, at 174–175 (KENNEDY, J., concurring), but also
deters law enforcement officers from even trying to obtain
voluntary confessions. The “ready ability to obtain unco
erced confessions is not an evil but an unmitigated good.”
McNeil, 501 U. S., at 181. Without these confessions,
crimes go unsolved and criminals unpunished. These are
not negligible costs, and in our view the Jackson Court
gave them too short shrift.5
   Notwithstanding this calculus, Montejo and his amici
urge the retention of Jackson. Their principal objection to
its elimination is that the Edwards regime which remains
will not provide an administrable rule. But this Court has
praised Edwards precisely because it provides “ ‘clear and
unequivocal’ guidelines to the law enforcement profes
sion,” Arizona v. Roberson, 486 U. S. 675, 682 (1988). Our
cases make clear which sorts of statements trigger its
protections, see Davis v. United States, 512 U. S. 452, 459
(1994), and once triggered, the rule operates as a bright
line. Montejo expresses concern that courts will have to
determine whether statements made at preliminary hear
ings constitute Edwards invocations—thus implicating all
the practical problems of the Louisiana rule we discussed
above, see Part II, supra. That concern is misguided. “We
——————
  5 The dissent claims that, in fact, few confessions have been sup

pressed by federal courts applying Jackson. Post, at 8. If so, that is
because, as the dissent boasts, “generations of police officers have been
trained to refrain from approaching represented defendants,” post, at 9,
n. 4. Anyway, if the rule truly does not hinder law enforcement or
make much practical difference, see post, at 7–9, and nn. 3–4, then
there is no reason to be particularly exercised about its demise.
18                 MONTEJO v. LOUISIANA

                      Opinion of the Court

have in fact never held that a person can invoke his
Miranda rights anticipatorily, in a context other than
‘custodial interrogation’. . . .” McNeil, supra, at 182, n. 3.
What matters for Miranda and Edwards is what happens
when the defendant is approached for interrogation, and
(if he consents) what happens during the interrogation—
not what happened at any preliminary hearing.
   In sum, when the marginal benefits of the Jackson rule
are weighed against its substantial costs to the truth
seeking process and the criminal justice system, we read
ily conclude that the rule does not “pay its way,” United
States v. Leon, 468 U. S. 897, 907–908, n. 6 (1984). Michi
gan v. Jackson should be and now is overruled.
                            V
   Although our holding means that the Louisiana Su
preme Court correctly rejected Montejo’s claim under
Jackson, we think that Montejo should be given an oppor
tunity to contend that his letter of apology should still
have been suppressed under the rule of Edwards. If Mon
tejo made a clear assertion of the right to counsel when
the officers approached him about accompanying them on
the excursion for the murder weapon, then no interroga
tion should have taken place unless Montejo initiated it.
Davis, supra, at 459. Even if Montejo subsequently agreed
to waive his rights, that waiver would have been invalid
had it followed an “unequivocal election of the right,”
Cobb, 532 U. S., at 176 (KENNEDY, J., concurring).
   Montejo understandably did not pursue an Edwards
objection, because Jackson served as the Sixth Amend
ment analogy to Edwards and offered broader protections.
Our decision today, overruling Jackson, changes the legal
landscape and does so in part based on the protections
already provided by Edwards. Thus we think that a re
mand is appropriate so that Montejo can pursue this
alternative avenue for relief. Montejo may also seek on
                 Cite as: 556 U. S. ____ (2009)          19

                     Opinion of the Court

remand to press any claim he might have that his Sixth
Amendment waiver was not knowing and voluntary, e.g.,
his argument that the waiver was invalid because it was
based on misrepresentations by police as to whether he
had been appointed a lawyer, cf. Moran, 475 U. S., at 428–
429. These matters have heightened importance in light
of our opinion today.
   We do not venture to resolve these issues ourselves, not
only because we are a court of final review, “not of first
view,” Cutter v. Wilkinson, 544 U. S. 709, 718, n. 7 (2005),
but also because the relevant facts remain unclear. Mon
tejo and the police gave inconsistent testimony about
exactly what took place on the afternoon of September 10,
2002, and the Louisiana Supreme Court did not make an
explicit credibility determination. Moreover, Montejo’s
testimony came not at the suppression hearing, but rather
only at trial, and we are unsure whether under state law
that testimony came too late to affect the propriety of the
admission of the evidence. These matters are best left for
resolution on remand.
   We do reject, however, the dissent’s revisionist legal
analysis of the “knowing and voluntary” issue. Post, at
10–14. In determining whether a Sixth Amendment
waiver was knowing and voluntary, there is no reason
categorically to distinguish an unrepresented defendant
from a represented one. It is equally true for each that, as
we held in Patterson, the Miranda warnings adequately
inform him “of his right to have counsel present during the
questioning,” and make him “aware of the consequences of
a decision by him to waive his Sixth Amendment rights,”
487 U. S., at 293. Somewhat surprisingly for an opinion
that extols the virtues of stare decisis, the dissent com
plains that our “treatment of the waiver question rests
entirely on the dubious decision in Patterson,” post, at 12.
The Court in Patterson did not consider the result dubious,
nor does the Court today.
20                MONTEJO v. LOUISIANA

                     Opinion of the Court

                        *     *     *
   This case is an exemplar of Justice Jackson’s oft quoted
warning that this Court “is forever adding new stories to
the temples of constitutional law, and the temples have a
way of collapsing when one story too many is added.”
Douglas v. City of Jeannette, 319 U. S. 157, 181 (1943)
(opinion concurring in result). We today remove Michigan
v. Jackson’s fourth story of prophylaxis.
   The judgment of the Louisiana Supreme Court is va
cated, and the case is remanded for further proceedings
not inconsistent with this opinion.
                                           It is so ordered.
                  Cite as: 556 U. S. ____ (2009)             1

                      ALITO, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 07–1529
                          _________________


         JESSE JAY MONTEJO, PETITIONER v. 

                    LOUISIANA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      LOUISIANA

                         [May 26, 2009] 


   JUSTICE ALITO, with whom JUSTICE KENNEDY joins,
concurring.
   Earlier this Term, in Arizona v. Gant, 556 U. S. ___
(2009), the Court overruled New York v. Belton, 453 U. S.
454 (1981), even though that case had been on the books
for 28 years, had not been undermined by subsequent
decisions, had been recently reaffirmed and extended, had
proven to be eminently workable (indeed, had been
adopted for precisely that reason), and had engendered
substantial law enforcement reliance. See Gant, supra, at
___ (slip op., at 4) (ALITO, J., dissenting). The Court took
this step even though we were not asked to overrule Bel
ton and this new rule is almost certain to lead to a host of
problems. See Gant, supra, at ___ (slip op., at 10) (ALITO,
J., dissenting); Megginson v. United States, post, p. ___;
Grooms v. United States, post, p. ___.
   JUSTICE SCALIA, who cast the deciding vote to overrule
Belton, dismissed stare decisis concerns with the following
observation: “[I]t seems to me ample reason that the
precedent was badly reasoned and produces erroneous . . .
results.” Gant, supra, at ___ (slip op., at 3) (concurring
opinion). This narrow view of stare decisis provides
the only principle on which the decision in Gant can be
justified.
   In light of Gant, the discussion of stare decisis in today’s
2                    MONTEJO v. LOUISIANA

                        ALITO, J., concurring

dissent* is surprising. The dissent in the case at hand
criticizes the Court for “[a]cting on its own” in reconsider
ing Michigan v. Jackson, 475 U. S. 625 (1986). Post, at 4
(opinion of STEVENS, J.). But the same was true in Gant,
and in this case, the Court gave the parties and interested
amici the opportunity to submit supplemental briefs on
the issue, a step not taken in Gant.
  The dissent faults the Court for “cast[ing] aside the
reliance interests of law enforcement,” post, at 8–9, but in
Gant, there were real and important law enforcement
interests at stake. See 556 U. S., at ___ (slip op., at 5–6)
(ALITO, J., dissenting). Even the Court conceded that the
Belton rule had “been widely taught in police academies
and that law enforcement officers ha[d] relied on the rule
in conducting vehicle searches during the past 28 years.”
556 U. S., at ___ (slip op., at 16). And whatever else might
be said about Belton, it surely provided a bright-line rule.
  A month ago, none of this counted for much, but today
the dissent writes:
    “Jackson’s bright-line rule has provided law enforce
    ment officers with clear guidance, allowed prosecutors
    to quickly and easily assess whether confessions will
    be admissible in court, and assisted judges in deter
    mining whether a defendant’s Sixth Amendment
    rights have been violated by police interrogation.”
    Post, at 8.
 It is striking that precisely the same points were true in
Gant:
    “[Belton’s] bright-line rule ha[d] provided law en
    forcement officers with clear guidance, allowed prose

——————
  * One of the dissenters in the present case, JUSTICE BREYER, also
dissented in Gant and would have followed Belton on stare decisis
grounds. See 556 U. S., at ___ (slip op., at 1). Thus, he would not
overrule either Belton or Michigan v. Jackson, 475 U. S. 625 (1986).
                 Cite as: 556 U. S. ____ (2009)            3

                     ALITO, J., concurring

    cutors to quickly and easily assess whether [evidence
    obtained in a vehicle search] w[ould] be admissible in
    court, and assisted judges in determining whether a
    defendant’s [Fourth] Amendment rights ha[d] been
    violated by police interrogation.” Post, at 8.
  The dissent, finally, invokes Jackson’s antiquity, stating
that “the 23-year existence of a simple bright-line rule”
should weigh in favor of its retention. Post, at 9. But in
Gant, the Court had no compunction about casting aside a
28-year-old bright-line rule. I can only assume that the
dissent thinks that our constitutional precedents are like
certain wines, which are most treasured when they are
neither too young nor too old, and that Jackson, at 23, is
in its prime, whereas Belton, at 28, had turned brownish
and vinegary.
  I agree with the dissent that stare decisis should pro
mote “ ‘the evenhanded . . . development of legal princi
ples,’ ” post, at 6 (quoting Payne v. Tennessee, 501 U. S.
808, 827–828 (1991)). The treatment of stare decisis in
Gant fully supports the decision in the present case.
                  Cite as: 556 U. S. ____ (2009)            1

                     STEVENS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 07–1529
                          _________________


         JESSE JAY MONTEJO, PETITIONER v. 

                    LOUISIANA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      LOUISIANA

                         [May 26, 2009] 


   JUSTICE STEVENS, with whom JUSTICE SOUTER and
JUSTICE GINSBURG join, and with whom JUSTICE BREYER
joins, except for footnote 5, dissenting.
   Today the Court properly concludes that the Louisiana
Supreme Court’s parsimonious reading of our decision in
Michigan v. Jackson, 475 U. S. 625 (1986), is indefensible.
Yet the Court does not reverse. Rather, on its own initia
tive and without any evidence that the longstanding Sixth
Amendment protections established in Jackson have
caused any harm to the workings of the criminal justice
system, the Court rejects Jackson outright on the ground
that it is “untenable as a theoretical and doctrinal mat
ter.” Ante, at 6. That conclusion rests on a misinterpreta
tion of Jackson’s rationale and a gross undervaluation of
the rule of stare decisis. The police interrogation in this
case clearly violated petitioner’s Sixth Amendment right
to counsel.
                               I
  The Sixth Amendment provides that “[i]n all criminal
prosecutions, the accused shall enjoy the right . . . to have
the Assistance of Counsel for his defence.” The right to
counsel attaches during “the initiation of adversary judi
cial criminal proceedings,” Rothgery v. Gillespie County,
554 U. S. ___, ___ (2008) (slip op., at 5) (internal quotation
2                  MONTEJO v. LOUISIANA

                     STEVENS, J., dissenting

marks omitted), and it guarantees the assistance of coun
sel not only during in-court proceedings but during all
critical stages, including postarraignment interviews with
law enforcement officers, see Patterson v. Illinois, 487
U. S. 285, 290 (1988).
   In Jackson, this Court considered whether the Sixth
Amendment bars police from interrogating defendants
who have requested the appointment of counsel at ar
raignment. Applying the presumption that such a request
constitutes an invocation of the right to counsel “at every
critical stage of the prosecution,” 475 U. S., at 633, we held
that “a defendant who has been formally charged with a
crime and who has requested appointment of counsel at
his arraignment” cannot be subject to uncounseled inter
rogation unless he initiates “exchanges or conversations
with the police,” id., at 626.
   In this case, petitioner Jesse Montejo contends that
police violated his Sixth Amendment right to counsel by
interrogating him following his “72-hour hearing” outside
the presence of, and without prior notice to, his lawyer.
The Louisiana Supreme Court rejected Montejo’s claim.
Relying on the fact that the defendants in Jackson had
“requested” counsel at arraignment, the state court held
that Jackson’s protections did not apply to Montejo be
cause his counsel was appointed automatically; Montejo
had not explicitly requested counsel or affirmatively ac
cepted the counsel appointed to represent him before he
submitted to police interrogation. 06–1807, pp. 28–29
(1/16/08), 974 So. 2d 1238, 1261.
   I agree with the majority’s conclusion that the Louisiana
Supreme Court’s decision, if allowed to stand, “would lead
either to an unworkable standard, or to arbitrary and
anomalous distinctions between defendants in different
States,” ante, at 3. Neither option is tolerable, and neither
is compelled by Jackson itself.
   Our decision in Jackson involved two consolidated cases,
                  Cite as: 556 U. S. ____ (2009)            3

                     STEVENS, J., dissenting

both arising in the State of Michigan. Under Michigan
law in effect at that time, when a defendant appeared for
arraignment the court was required to inform him that
counsel would be provided if he was financially needy and
he requested representation. Mich. Gen. Ct. Rule 785.4(1)
(1976). It was undisputed that the Jackson defendants
made such a “request” at their arraignment: one by com
pleting an affidavit of indigency, and the other by respond
ing affirmatively to a question posed to him by the court.
See App. in Michigan v. Jackson, O. T. 1984, No. 84–1531,
p. 168; App. in Michigan v. Bladel, O. T. 1984, No. 84–
1539, pp. 3a–4a. In neither case, however, was it clear
that counsel had actually been appointed at the arraign
ment. Thus, the defendants’ requests for counsel were
significant as a matter of state law because they served as
evidence that the appointment of counsel had been effec
tuated even in the absence of proof that defense counsel
had actual notice of the appointments.
   Unlike Michigan, Louisiana does not require a defen
dant to make a request in order to receive court-appointed
counsel. Consequently, there is no reason to place consti
tutional significance on the fact that Montejo neither
voiced a request for counsel nor affirmatively embraced
that appointment post hoc. Certainly our decision in
Jackson did not mandate such an odd rule. See ante, at 4
(acknowledging that we had no occasion to decide in Jack
son how its rule would apply in States that do not make
appointment of counsel contingent on affirmative request).
If a defendant is entitled to protection from police-initiated
interrogation under the Sixth Amendment when he
merely requests a lawyer, he is even more obviously enti
tled to such protection when he has secured a lawyer.
Indeed, we have already recognized as much. See Michi
gan v. Harvey, 494 U. S. 344, 352 (1990) (acknowledging
that “once a defendant obtains or even requests counsel,”
Jackson alters the waiver analysis); Patterson, 487 U. S.,
4                      MONTEJO v. LOUISIANA

                         STEVENS, J., dissenting

at 290, n. 3 (noting “as a matter of some significance” to
the constitutional analysis that defendant had “not re
tained, or accepted by appointment, a lawyer to represent
him at the time he was questioned by authorities” (em
phasis added)).1 Once an attorney-client relationship has
been established through the appointment or retention of
counsel, as a matter of federal law the method by which
the relationship was created is irrelevant: The existence of
a valid attorney-client relationship provides a defendant
with the full constitutional protection afforded by the
Sixth Amendment.
                             II
  Today the Court correctly concludes that the Louisiana
Supreme Court’s holding is “troublesome,” ante, at 4,
“impractical,” ante, at 5, and “unsound,” ante, at 6. In
stead of reversing the decision of the state court by simply
answering the question on which we granted certiorari in
a unanimous opinion, however, the majority has decided to
change the law. Acting on its own initiative, the majority
overrules Jackson to correct a “theoretical and doctrinal”
problem of its own imagining, see ante, at 6. A more
careful reading of Jackson and the Sixth Amendment
cases upon which it relied reveals that the rule announced
in Jackson protects a fundamental right that the Court
now dishonors.
  The majority’s decision to overrule Jackson rests on its
assumption that Jackson’s protective rule was intended to
“prevent police from badgering defendants into changing
their minds about their rights,” ante, at 10; see also ante,
——————
  1 In Patterson v. Illinois, we further explained, “[o]nce an accused has

a lawyer,” “a distinct set of constitutional safeguards aimed at preserv
ing the sanctity of the attorney-client relationship takes effect.” 487
U. S., at 290, n. 3 (citing Maine v. Moulton, 474 U. S. 159, 176 (1985)).
“Indeed,” we emphasized, “the analysis changes markedly once an
accused even requests the assistance of counsel.” 487 U. S., at 290, n. 3.
                 Cite as: 556 U. S. ____ (2009)            5

                    STEVENS, J., dissenting

at 13, just as the rule adopted in Edwards v. Arizona, 451
U. S. 477 (1981), was designed to prevent police from
coercing unindicted suspects into revoking their requests
for counsel at interrogation. Operating on that limited
understanding of the purpose behind Jackson’s protective
rule, the Court concludes that Jackson provides no safe
guard not already secured by this Court’s Fifth Amend
ment jurisprudence. See Miranda v. Arizona, 384 U. S.
436 (1966) (requiring defendants to be admonished of their
right to counsel prior to custodial interrogation); Edwards,
451 U. S. 477 (prohibiting police-initiated interrogation
following defendant’s invocation of the right to counsel).
   The majority’s analysis flagrantly misrepresents Jack
son’s underlying rationale and the constitutional interests
the decision sought to protect. While it is true that the
rule adopted in Jackson was patterned after the rule in
Edwards, 451 U. S., at 484–485, the Jackson opinion does
not even mention the anti-badgering considerations that
provide the basis for the Court’s decision today. Instead,
Jackson relied primarily on cases discussing the broad
protections guaranteed by the Sixth Amendment right to
counsel—not its Fifth Amendment counterpart. Jackson
emphasized that the purpose of the Sixth Amendment is
to “ ‘protec[t] the unaided layman at critical confrontations
with his adversary,’ ” 475 U. S., at 631 (quoting United
States v. Gouveia, 467 U. S. 180, 189 (1984)), by giving
him “ ‘the right to rely on counsel as a ‘medium’ between
him[self] and the State,’ ” 475 U. S., at 632 (quoting Maine
v. Moulton, 474 U. S. 159, 176 (1985)). Underscoring that
the commencement of criminal proceedings is a decisive
event that transforms a suspect into an accused within the
meaning of the Sixth Amendment, we concluded that
arraigned defendants are entitled to “at least as much
protection” during interrogation as the Fifth Amendment
affords unindicted suspects. See, e.g., 475 U. S., at 632
(“[T]he difference between the legal basis for the rule
6                      MONTEJO v. LOUISIANA

                         STEVENS, J., dissenting

applied in Edwards and the Sixth Amendment claim
asserted in these cases actually provides additional sup
port for the application of the rule in these circumstances”
(emphasis added)). Thus, although the rules adopted in
Edwards and Jackson are similar, Jackson did not rely on
the reasoning of Edwards but remained firmly rooted in
the unique protections afforded to the attorney-client
relationship by the Sixth Amendment.2
  Once Jackson is placed in its proper Sixth Amendment
context, the majority’s justifications for overruling the
decision crumble. Ordinarily, this Court is hesitant to
disturb past precedent and will do so only when a rule has
proven “outdated, ill-founded, unworkable, or otherwise
legitimately vulnerable to serious reconsideration.”
Vasquez v. Hillery, 474 U. S. 254, 266 (1986). While stare
decisis is not “an inexorable command,” we adhere to it as
“the preferred course because it promotes the evenhanded,
predictable, and consistent development of legal princi
ples, fosters reliance on judicial decisions, and contributes
to the actual and perceived integrity of the judicial proc
——————
    2 Themajority insists that protection from police badgering is the
only purpose the Jackson rule can plausibly serve. After all, it asks,
from what other evil would the rule guard? See ante, at 9. There are
two obvious answers. First, most narrowly, it protects the defendant
from any police-initiated interrogation without notice to his counsel, not
just from “badgering” which is not necessarily a part of police question
ing. Second, and of prime importance, it assures that any waiver of
counsel will be valid. The assistance offered by counsel protects a
defendant from surrendering his rights with an insufficient apprecia
tion of what those rights are and how the decision to respond to inter
rogation might advance or compromise his exercise of those rights
throughout the course of criminal proceedings. A lawyer can provide
her client with advice regarding the legal and practical options avail
able to him; the potential consequences, both good and bad, of choosing
to discuss his case with police; the likely effect of such a conversation on
the resolution of the charges against him; and an informed assessment
of the best course of action under the circumstances. Such assistance
goes far beyond mere protection against police badgering.
                     Cite as: 556 U. S. ____ (2009)                    7

                        STEVENS, J., dissenting

ess.” Payne v. Tennessee, 501 U. S. 808, 827–828 (1991).
   Paying lip service to the rule of stare decisis, the major
ity acknowledges that the Court must consider many
factors before taking the dramatic step of overruling a
past decision. See ante, at 12. Specifically, the majority
focuses on four considerations: the reasoning of the deci
sion, the workability of the rule, the reliance interests at
stake, and the antiquity of the precedent. The Court
exaggerates the considerations favoring reversal, however,
and gives short shrift to the valid considerations favoring
retention of the Jackson rule.
   First, and most central to the Court’s decision to over
rule Jackson, is its assertion that Jackson’s “ ‘reason
ing’ ”—which the Court defines as “the weighing of the
[protective] rule’s benefits against its costs,” ante, at 14—
does not justify continued application of the rule it cre
ated. The balancing test the Court performs, however,
depends entirely on its misunderstanding of Jackson as a
rule designed to prevent police badgering, rather than a
rule designed to safeguard a defendant’s right to rely on
the assistance of counsel.3
   Next, in order to reach the conclusion that the Jackson

——————
   3 Even accepting the majority’s improper framing of Jackson’s foun

dation, the Court fails to show that the costs of the rule are more than
negligible or differ from any other protection afforded by the right to
counsel. The majority assumes, without citing any empirical or even
anecdotal support, that any marginal benefits of the Jackson rule are
“dwarfed by its substantial costs,” which it describes as harm to “ ‘soci
ety’s compelling interest in finding, convicting, and punishing those
who violate the law.’ ” Ante, at 14 (quoting Moran v. Burbine, 475 U. S.
412, 426 (1986)). That assumption is highly dubious, particularly in
light of the fact that several amici with interest in law enforcement
have conceded that the application of Jackson’s protective rule rarely
impedes prosecution. See Supplemental Brief for Larry D. Thompson
et al. as Amici Curiae 6 (hereinafter Thompson Supplemental Brief);
Brief for United States as Amicus Curiae 12 (hereinafter United States
Brief).
8                    MONTEJO v. LOUISIANA

                       STEVENS, J., dissenting

rule is unworkable, the Court reframes the relevant in
quiry, asking not whether the Jackson rule as applied for
the past quarter century has proved easily administrable,
but instead whether the Louisiana Supreme Court’s
cramped interpretation of that rule is practically worka
ble. The answer to that question, of course, is no. When
framed more broadly, however, the evidence is overwhelm
ing that Jackson’s simple, bright-line rule has done more
to advance effective law enforcement than to undermine it.
  In a supplemental brief submitted by lawyers and
judges with extensive experience in law enforcement and
prosecution, amici Larry D. Thompson et al. argue per
suasively that Jackson’s bright-line rule has provided law
enforcement officers with clear guidance, allowed prosecu
tors to quickly and easily assess whether confessions will
be admissible in court, and assisted judges in determining
whether a defendant’s Sixth Amendment rights have been
violated by police interrogation. See generally Thompson
Supplemental Brief 6. While amici acknowledge that
“Jackson reduces opportunities to interrogate defendants”
and “may require exclusion of evidence that could support
a criminal conviction,” they maintain that “it is a rare case
where this rule lets a guilty defendant go free.” Ibid.
Notably, these representations are not contradicted by the
State of Louisiana or other amici, including the United
States. See United States Brief 12 (conceding that the
Jackson rule has not “resulted in the suppression of sig
nificant numbers of statements in federal prosecutions in
the past”).4 In short, there is substantial evidence sug
——————
  4 Further supporting the workability of the Jackson rule is the fact

that it aligns with the professional standards and norms that already
govern the behavior of police and prosecutors. Rules of Professional
Conduct endorsed by the American Bar Association (ABA) and by every
State Bar Association in the country prohibit prosecutors from making
direct contact with represented defendants in all but the most limited
of circumstances, see App. to Supplemental Brief for Public Defender
                     Cite as: 556 U. S. ____ (2009)                   9

                        STEVENS, J., dissenting

gesting that Jackson’s rule is not only workable, but also
desirable from the perspective of law enforcement.
   Turning to the reliance interests at stake in the case,
the Court rejects the interests of criminal defendants with
the flippant observation that any who are knowledgeable
enough to rely on Jackson are too savvy to need its protec
tions, and casts aside the reliance interests of law en
forcement on the ground that police and prosecutors re
main free to employ the Jackson rule if it suits them. See
ante, at 12. Again as a result of its mistaken understand
ing of the purpose behind Jackson’s protective rule, the
Court fails to identify the real reliance interest at issue in
this case: the public’s interest in knowing that counsel,
once secured, may be reasonably relied upon as a medium
between the accused and the power of the State. That
interest lies at the heart of the Sixth Amendment’s guar
antee, and is surely worthy of greater consideration than
it is given by today’s decision.
   Finally, although the Court acknowledges that “antiq
uity” is a factor that counsels in favor of retaining prece
dent, it concludes that the fact Jackson is “only two dec
ades old” cuts “in favor of abandoning” the rule it
established. Ante, at 13. I would have thought that the
——————
Service for the District of Columbia et al. as Amici Curiae 1a–15a
(setting forth state rules governing contact with represented persons);
ABA Model Rule of Professional Conduct 4.2 (2008); 28 U. S. C.
§530B(a) (making state rules of professional conduct applicable to
federal attorneys), and generations of police officers have been trained
to refrain from approaching represented defendants, both because
Jackson requires it and because, absent direction from prosecutors,
officers are reticent to interrogate represented defendants. See United
States Brief 11–12; see also Thompson Supplemental Brief 13 (citing
Federal Bureau of Investigation, Legal Handbook for Special Agents
§7–4.1(7) (2003)). Indeed, the United States concedes that a decision to
overrule the case “likely w[ill] not significantly alter the manner in
which federal law enforcement agents investigate indicted defendants.”
United States Brief 11–12.
10                    MONTEJO v. LOUISIANA

                        STEVENS, J., dissenting

23-year existence of a simple bright-line rule would be a
factor that cuts in the other direction.
  Despite the fact that the rule established in Jackson
remains relevant, well grounded in constitutional prece
dent, and easily administrable, the Court today rejects it
sua sponte. Such a decision can only diminish the public’s
confidence in the reliability and fairness of our system of
justice.5
                            III
   Even if Jackson had never been decided, it would be
clear that Montejo’s Sixth Amendment rights were vio
lated. Today’s decision eliminates the rule that “any
waiver of Sixth Amendment rights given in a discussion
initiated by police is presumed invalid” once a defendant
has invoked his right to counsel. Harvey, 494 U. S., at 349
(citing Jackson, 475 U. S., at 636). Nevertheless, under
the undisputed facts of this case, there is no sound basis
for concluding that Montejo made a knowing and valid
waiver of his Sixth Amendment right to counsel before
acquiescing in police interrogation following his 72-hour
hearing.    Because police questioned Montejo without
notice to, and outside the presence of, his lawyer, the
——————
  5 In his concurrence, JUSTICE ALITO assumes that my consideration of

the rule of stare decisis in this case is at odds with the Court’s recent
rejection of his reliance on that doctrine in his dissent in Arizona v.
Gant, 556 U. S. ___ (2009). While I agree that the reasoning in his
dissent supports my position in this case, I do not agree with his
characterization of our opinion in Gant. Contrary to his representation,
the Court did not overrule our precedent in New York v. Belton, 453
U. S. 454 (1981). Rather, we affirmed the narrow interpretation of
Belton’s holding adopted by the Arizona Supreme Court, rejecting the
broader interpretation adopted by other lower courts that had been
roundly criticized by judges and scholars alike. By contrast, in this
case the Court flatly overrules Jackson—a rule that has drawn virtu
ally no criticism—on its own initiative. The two cases are hardly
comparable. If they were, and if JUSTICE ALITO meant what he said in
Gant, I would expect him to join this opinion.
                 Cite as: 556 U. S. ____ (2009)          11

                    STEVENS, J., dissenting

interrogation violated Montejo’s right to counsel even
under pre-Jackson precedent.
   Our pre-Jackson case law makes clear that “the Sixth
Amendment is violated when the State obtains incriminat
ing statements by knowingly circumventing the accused’s
right to have counsel present in a confrontation between
the accused and a state agent.” Moulton, 474 U. S., at
176. The Sixth Amendment entitles indicted defendants
to have counsel notified of and present during critical
confrontations with the state throughout the pretrial
process. Given the realities of modern criminal prosecu
tion, the critical proceedings at which counsel’s assistance
is required more and more often occur outside the court
room in pretrial proceedings “where the results might well
settle the accused’s fate and reduce the trial itself to a
mere formality.” United States v. Wade, 388 U. S. 218,
224 (1967).
   In Wade, for instance, we held that because a post
indictment lineup conducted for identification purposes is
a critical stage of the criminal proceedings, a defendant
and his counsel are constitutionally entitled to notice of
the impending lineup. Accordingly, counsel’s presence is a
“requisite to conduct of the lineup, absent an intelligent
waiver.” Id., at 237 (internal quotation marks omitted).
The same reasoning applies to police decisions to interro
gate represented defendants. For if the Sixth Amendment
entitles an accused to such robust protection during a
lineup, surely it entitles him to such protection during a
custodial interrogation, when the stakes are as high or
higher. Cf. Spano v. New York, 360 U. S. 315, 326 (1959)
(Douglas, J., concurring) (“[W]hat use is a defendant’s
right to effective counsel at every stage of a criminal case
if, while he is held awaiting trial, he can be questioned in
the absence of counsel until he confesses?”).
   The Court avoids confronting the serious Sixth Amend
ment concerns raised by the police interrogation in this
12                    MONTEJO v. LOUISIANA

                        STEVENS, J., dissenting

case by assuming that Montejo validly waived his Sixth
Amendment rights before submitting to interrogation.6 It
does so by summarily concluding that “doctrines ensuring
voluntariness of the Fifth Amendment waiver simultane
ously ensure the voluntariness of the Sixth Amendment
waiver,” ante, at 15–16; thus, because Montejo was given
Miranda warnings prior to interrogation, his waiver was
presumptively valid. Ironically, while the Court faults
Jackson for blurring the line between this Court’s Fifth
and Sixth Amendment jurisprudence, it commits the same
error by assuming that the Miranda warnings given in
this case, designed purely to safeguard the Fifth Amend
ment right against self-incrimination, were somehow
adequate to protect Montejo’s more robust Sixth Amend
ment right to counsel.
    The majority’s cursory treatment of the waiver question
rests entirely on the dubious decision in Patterson, in
which we addressed whether, by providing Miranda warn
ings, police had adequately advised an indicted but unrep
resented defendant of his Sixth Amendment right to coun
sel. The majority held that “[a]s a general matter . . . an
accused who is admonished with the warnings prescribed
. . . in Miranda, . . . has been sufficiently apprised of the
nature of his Sixth Amendment rights, and of the conse
quences of abandoning those rights.” 487 U. S., at 296.
The Court recognized, however, that “because the Sixth
Amendment’s protection of the attorney-client relationship

——————
  6 The majority leaves open the possibility that, on remand, Montejo

may argue that his waiver was invalid because police falsely told him
he had not been appointed counsel. See ante, at 18. While such police
deception would obviously invalidate any otherwise valid waiver of
Montejo’s Sixth Amendment rights, Montejo has a strong argument
that, given his status as a represented criminal defendant, the Miranda
warnings given to him by police were insufficient to permit him to
make a knowing waiver of his Sixth Amendment rights even absent
police deception.
                     Cite as: 556 U. S. ____ (2009)                  13

                        STEVENS, J., dissenting

. . . extends beyond Miranda’s protection of the Fifth
Amendment right to counsel, . . . there will be cases where
a waiver which would be valid under Miranda will not
suffice for Sixth Amendment purposes.” Id., at 297, n. 9.
This is such a case.
    As I observed in Patterson, the conclusion that Miranda
warnings ordinarily provide a sufficient basis for a know
ing waiver of the right to counsel rests on the questionable
assumption that those warnings make clear to defendants
the assistance a lawyer can render during post-indictment
interrogation. See 487 U. S., at 307 (dissenting opinion).
Because Miranda warnings do not hint at the ways in
which a lawyer might assist her client during conversa
tions with the police, I remain convinced that the warn
ings prescribed in Miranda,7 while sufficient to apprise a
defendant of his Fifth Amendment right to remain silent,
are inadequate to inform an unrepresented, indicted de
fendant of his Sixth Amendment right to have a lawyer
present at all critical stages of a criminal prosecution. The
inadequacy of those warnings is even more obvious in the
case of a represented defendant. While it can be argued
that informing an indicted but unrepresented defendant of
his right to counsel at least alerts him to the fact that he is
entitled to obtain something he does not already possess,
providing that same warning to a defendant who has
already secured counsel is more likely to confound than
enlighten.8 By glibly assuming that that the Miranda
——————
  7 Under Miranda, a suspect must be “warned prior to any questioning

that he has the right to remain silent, that anything he says may be
used against him in court of law, that he has the right to the presence
of any attorney, and that if he cannot afford an attorney, one will be
appointed for him prior to any questioning if he so desires.” 384 U. S.,
at 479.
  8 With respect to vulnerable defendants, such as juveniles and those

with mental impairments of various kinds, amici National Association
of Criminal Defense Lawyers et al. assert that “[o]verruling Jackson
would be particularly detrimental . . . because of the confusing instruc
14                    MONTEJO v. LOUISIANA

                        STEVENS, J., dissenting

warnings given in this case were sufficient to ensure
Montejo’s waiver was both knowing and voluntary, the
Court conveniently avoids any comment on the actual
advice Montejo received, which did not adequately inform
him of his relevant Sixth Amendment rights or alert him
to the possible consequences of waiving those rights.
  A defendant’s decision to forgo counsel’s assistance and
speak openly with police is a momentous one. Given the
high stakes of making such a choice and the potential
value of counsel’s advice and mediation at that critical
stage of the criminal proceedings, it is imperative that a
defendant possess “a full awareness of both the nature of
the right being abandoned and the consequences of the
decision to abandon it,” Moran v. Burbine, 475 U. S. 412,
421 (1986), before his waiver is deemed valid. See Iowa v.
Tovar, 541 U. S. 77, 81 (2004); Johnson v. Zerbst, 304
U. S. 458, 464 (1938). Because the administration of
Miranda warnings was insufficient to ensure Montejo
understood the Sixth Amendment right he was being
asked to surrender, the record in this case provides no
basis for concluding that Montejo validly waived his right
to counsel, even in the absence of Jackson’s enhanced
protections.
                            IV
  The Court’s decision to overrule Jackson is unwar
ranted. Not only does it rests on a flawed doctrinal prem
——————
tions regarding counsel that they would receive. At the initial hearing,
they would likely learn that an attorney was being appointed for them,
In a later custodial interrogation, however, they would be informed in
the traditional manner of ‘their right to counsel’ and right to have
counsel ‘appointed’ if they are indigent, notwithstanding that counsel
had already been appointed in open court. These conflicting statements
would be confusing to anyone, but would be especially baffling to
defendants with mental disabilities or other impairments.” Supple
mental Brief for National Association of Criminal Defense Lawyers
et al. as Amici Curiae 7–8.
                Cite as: 556 U. S. ____ (2009)         15

                   STEVENS, J., dissenting

ise, but the dubious benefits it hopes to achieve are far
outweighed by the damage it does to the rule of law and
the integrity of the Sixth Amendment right to counsel.
Moreover, even apart from the protections afforded by
Jackson, the police interrogation in this case violated
Jesse Montejo’s Sixth Amendment right to counsel.
  I respectfully dissent.
                  Cite as: 556 U. S. ____ (2009)            1

                     BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 07–1529
                          _________________


         JESSE JAY MONTEJO, PETITIONER v. 

                    LOUISIANA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      LOUISIANA

                         [May 26, 2009] 


   JUSTICE BREYER, dissenting.
   I join JUSTICE STEVENS’ dissent except for footnote 5.
Although the principles of stare decisis are not inflexible, I
believe they bind the Court here. I reached a similar
conclusion in Arizona v. Gant, 556 U. S. ___, ___–___
(2009) (slip op., at 1–2) (BREYER, J., dissenting), and in
several other recent cases. See, e.g., Leegin Creative
Leather Products, Inc. v. PSKS, Inc., 551 U. S. 877, ___–
___ (2007) (slip op., at 17–19) (BREYER, J., dissenting);
Parents Involved in Community Schools v. Seattle School
Dist. No. 1, 551 U. S. 701, ___–___ (2007) (slip op., at 65–
66) (BREYER, J., dissenting); Federal Election Comm’n v.
Wisconsin Right to Life, Inc., 551 U. S. 449, ___–___ (2007)
(slip op., at 31–32) (SOUTER, J., dissenting); Bowles v.
Russell, 551 U. S. 205, 219–220 (2007) (SOUTER, J., dis
senting); Gonzales v. Carhart, 550 U. S. 124, 190–191
(2007) (GINSBURG, J., dissenting); District of Columbia v.
Heller, 554 U. S. ___, ___–___ (2008) (slip op. at 41–45)
(STEVENS, J., dissenting).

```

---

## GROUP: content/cases/Moran v. Burbine.md  (`case`, 5 assertions)

### content_page

```
---
title: "Moran v. Burbine"
type: case
citation: "475 U.S. 412 (1986)"
parallel_cite: "106 S. Ct. 1135; 89 L. Ed. 2d 410; 54 U.S.L.W. 4265"
neutral_cite: 1986 U.S. LEXIS 32
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-03-10
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-03-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Moran v. Burbine
  varies_by_point: false
  scope_note: "Canonical statement of the two-dimensional Miranda-waiver standard; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111614/moran-v-burbine/"
  cluster_id: 111614
  opinion_id: 111614
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[North Carolina v. Butler]]", "[[Edwards v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "waiver"]
holding: "A Miranda waiver is valid even though police failed to tell the suspect that an attorney was trying to reach him; events outside the…"
lake:
  record_id: Moran v. Burbine
  status: verified
  projected_at: 2026-07-09
---

# Moran v. Burbine

*475 U.S. 412 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Burbine was arrested for a burglary; police then connected him to a murder. While he was in custody, his sister obtained a public defender, who telephoned the station and was told Burbine would not be questioned until the next day. Unaware of the call and never told of it, Burbine was given *[[Miranda v. Arizona|Miranda]]* warnings, waived his rights, and confessed to the murder.

## Issue
Whether a *[[Miranda v. Arizona|Miranda]]* waiver is invalid because police failed to inform the suspect that an attorney was trying to reach him, or because police misled the attorney about whether questioning would occur.

## Rule
No. A waiver is valid if it is voluntary, knowing, and intelligent, judged by a two-part inquiry: "First, the relinquishment of the right must have been voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion, or deception. Second, the waiver must have been made with a full awareness of both the nature of the right being abandoned and the consequences of the decision to abandon it." — 475 U.S. at 421. ^pin-421

Information withheld from the suspect cannot bear on that inquiry: "Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right." — [*Id.* at 422](https://www.courtlistener.com/opinion/111614/moran-v-burbine/#:~:text=Events%20occurring%20outside%20of%20the). ^pin-422

## Application
Burbine's waiver was voluntary — there was no coercion — and knowing and intelligent, because he was repeatedly advised of and understood his rights. The police failure to tell him of the attorney's call, and any deception of the attorney, occurred outside his presence and were unknown to him, so they could not undermine his comprehension or the validity of his waiver. The Court also held that the Sixth Amendment had not attached because adversary judicial proceedings had not begun, and the police conduct did not violate due process on these facts. The confession was admissible.

## Conclusion
The waiver was valid and the confession admissible; the First Circuit's grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Moran* supplies the canonical two-dimensional (voluntary + knowing/intelligent) standard for a valid *[[Miranda v. Arizona|Miranda]]* waiver, applied in cases such as [[North Carolina v. Butler]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Moran v. Burbine*, 475 U.S. 412 (1986) — https://www.courtlistener.com/opinion/111614/moran-v-burbine/ — pinpoints: 421, 422.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5739df5473493a53", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "475 U.S. 412 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 32", "official_citation_present": true, "parallel_cite": "106 S. Ct. 1135; 89 L. Ed. 2d 410; 54 U.S.L.W. 4265", "title": "Moran v. Burbine", "year": "1986"}}
{"assertion_id": "1d4a8363ae8284ec", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A Miranda waiver is valid even though police failed to tell the suspect that an attorney was trying to reach him; events outside the…", "title": "Moran v. Burbine"}}
{"assertion_id": "355e50ad65c19b1a", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "Moran v. Burbine"}}
{"assertion_id": "9962f9070f18389a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Moran v. Burbine"}}
{"assertion_id": "c639857ce0d8a3d9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-03-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Moran v. Burbine", "field_i_validity": "good_law", "scope_note": "Canonical statement of the two-dimensional Miranda-waiver standard; no negative treatment.", "title": "Moran v. Burbine", "varies_by_point": "false"}}
```

### lake record — Moran v. Burbine

```json
{
  "schema_version": "s2.v1",
  "record_id": "Moran v. Burbine",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Moran v. Burbine",
    "case_name_short": "Moran",
    "case_name_full": "Moran, Superintendent, Rhode Island Department of Corrections v. Burbine",
    "input_case_name": "Moran v. Burbine",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-03-10",
    "year": 1986,
    "docket": null,
    "cluster_id": 111614,
    "lead_opinion_id": 111614,
    "sibling_ids": [
      111614,
      9842071,
      9842072
    ],
    "absolute_url": "/opinion/111614/moran-v-burbine/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "475 U.S. 412",
      "volume": "475",
      "reporter": "U.S.",
      "page": "412",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1135",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1135",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 410",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4265",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4265",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 32",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "32",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 412",
        "volume": "475",
        "reporter": "U.S.",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1135",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1135",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 410",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 32",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "32",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4265",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4265",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "475 U.S. 412",
    "official_selection": {
      "court_class": "scotus",
      "selected": "475 U.S. 412",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-421",
      "page": null,
      "quote": "--- # Moran v. Burbine *475 U.S. 412 (1986)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Burbine was arrested for a burglary; police then connected him to a murder. While he was in custody, his sister obtained a public defender, who telephoned the station and was told Burbine would not be questioned until the next day. Unaware of the call and never told of it, Burbine was given *Miranda* warnings, waived his rights, and confessed to the murder. ## Issue Whether a *Miranda* waiver is invalid because police failed to inform the suspect that an attorney was trying to reach him, or because police misled the attorney about whether questioning would occur. ## Rule No. A waiver is valid if it is voluntary, knowing, and intelligent, judged by a two-part inquiry:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-422",
      "page": null,
      "quote": "Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right.",
      "star_marker": "422",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 20840,
      "fragment": "#:~:text=Events%20occurring%20outside%20of%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-03-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Moran v. Burbine",
    "varies_by_point": false,
    "scope_note": "Canonical statement of the two-dimensional Miranda-waiver standard; no negative treatment.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Moran v. Burbine:lane1_negative"
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
        "journal_ref": "Moran v. Burbine:lane1_negative"
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
        "journal_ref": "Moran v. Burbine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Simpkins",
          "cluster_id": 10018645,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Simpkins",
          "cluster_id": 4731163,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Vasquez-Santiago",
          "cluster_id": 10133179,
          "cite": [
            "301 Or. App. 90",
            "456 P.3d 270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane1_negative"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Padilla v. Kentucky",
          "cluster_id": 1723,
          "cite": [
            "176 L. Ed. 2d 284",
            "130 S. Ct. 1473",
            "559 U.S. 356",
            "2010 U.S. LEXIS 2928"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richardson v. Marsh",
          "cluster_id": 111865,
          "cite": [
            "95 L. Ed. 2d 176",
            "107 S. Ct. 1702",
            "481 U.S. 200",
            "1987 U.S. LEXIS 1812",
            "55 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "in Int. of B.H",
          "cluster_id": 4889275,
          "cite": [
            "2021 CO 39"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Murray",
          "cluster_id": 111728,
          "cite": [
            "91 L. Ed. 2d 434",
            "106 S. Ct. 2661",
            "477 U.S. 527",
            "1986 U.S. LEXIS 67",
            "54 U.S.L.W. 4833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Male Juvenile (95-Cr-1074)",
          "cluster_id": 744606,
          "cite": [
            "121 F.3d 34",
            "1997 U.S. App. LEXIS 19219",
            "1997 WL 416548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richardson v. State",
          "cluster_id": 853754,
          "cite": [
            "717 N.E.2d 32",
            "1999 Ind. LEXIS 918",
            "1999 WL 784001"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert L. Wilson v. Edward Murray, Director of the Virginia Department of Corrections",
          "cluster_id": 480360,
          "cite": [
            "806 F.2d 1232",
            "1986 U.S. App. LEXIS 34712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gray v. Maryland",
          "cluster_id": 118184,
          "cite": [
            "140 L. Ed. 2d 294",
            "118 S. Ct. 1151",
            "523 U.S. 185",
            "1998 U.S. LEXIS 1605"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Penry v. State",
          "cluster_id": 2372264,
          "cite": [
            "903 S.W.2d 715",
            "1995 WL 68622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. District Court in & for First Judicial District, Jefferson County",
          "cluster_id": 1138536,
          "cite": [
            "785 P.2d 141",
            "14 Brief Times Rptr. 75",
            "1990 Colo. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111614 OR 9842071 OR 9842072) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTYyMjg0ODAwMDAwJnM9NDYzNzA0NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111614+OR+9842071+OR+9842072%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111614 OR 9842071 OR 9842072)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NTMmcz0xNDU2MjgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111614+OR+9842071+OR+9842072%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111614 OR 9842071 OR 9842072)",
        "reviewed": 109,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 109,
        "triage_read": 0,
        "triage_snippet_classified": 109
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111614 OR 9842071 OR 9842072)",
    "indexed_citing_opinions": 1991,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111614,
        "count": 1730,
        "count_source": "search"
      },
      {
        "opinion_id": 9842071,
        "count": 297,
        "count_source": "search"
      },
      {
        "opinion_id": 9842072,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3340,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/moran-v-burbine.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNjk1Mzcmcz0xMDU5Njc4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111614+OR+9842071+OR+9842072%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111614,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109825,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 303738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 436102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 446925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1169436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1174756,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1320570,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1345918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1467753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1525657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1688778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1715629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1843028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1847051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1869337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1955294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1996598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2055814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2238115,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2267415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2314564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T14:39:18Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:39:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:39:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:43:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:39:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Moran v. Burbine (truncated)

```
<div>
<center><b><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">475 U.S. 412</a></span> (1986)</b></center>
<center><h1>MORAN, SUPERINTENDENT, RHODE ISLAND DEPARTMENT OF CORRECTIONS<br>
v.<br>
BURBINE</h1></center>
<center>No. 84-1485.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 13, 1985</center>
<center>Decided March 10, 1986</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIRST CIRCUIT
<p><span class="star-pagination">*414</span> <i>Constance L. Messore,</i> Special Assistant Attorney General of Rhode Island, argued the cause for petitioner. With her on the briefs was <i>Arlene Violet,</i> Attorney General.</p>
<p><i>Deputy Solicitor General Frey</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Acting Solicitor General Fried, Assistant Attorney General Trott, Andrew J. Pincus,</i> and <i>Sara Criscitelli.</i></p>
<p><i>Robert B. Mann</i> argued the cause for respondent. With him on the brief was <i>William F. Reilly.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*415</span> JUSTICE O'CONNOR delivered the opinion of the Court.</p>
<p>After being informed of his rights pursuant to <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and after executing a series of written waivers, respondent confessed to the murder of a young woman. At no point during the course of the interrogation, which occurred prior to arraignment, did he request an attorney. While he was in police custody, his sister attempted to retain a lawyer to represent him. The attorney telephoned the police station and received assurances that respondent would not be questioned further until the next day. In fact, the interrogation session that yielded the inculpatory statements began later that evening. The question presented is whether either the conduct of the police or respondent's <span class="star-pagination">*416</span> ignorance of the attorney's efforts to reach him taints the validity of the waivers and therefore requires exclusion of the confessions.</p>
<p></p>
<h2>I</h2> <p>On the morning of March 3, 1977, Mary Jo Hickey was found unconscious in a factory parking lot in Providence, Rhode Island. Suffering from injuries to her skull apparently inflicted by a metal pipe found at the scene, she was rushed to a nearby hospital. Three weeks later she died from her wounds.</p>
<p>Several months after her death, the Cranston, Rhode Island, police arrested respondent and two others in connection with a local burglary. Shortly before the arrest, Detective Ferranti of the Cranston police force had learned from a confidential informant that the man responsible for Ms. Hickey's death lived at a certain address and went by the name of "Butch." Upon discovering that respondent lived at that address and was known by that name, Detective Ferranti informed respondent of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. When respondent refused to execute a written waiver, Detective Ferranti spoke separately with the two other suspects arrested on the breaking and entering charge and obtained statements further implicating respondent in Ms. Hickey's murder. At approximately 6 p.m., Detective Ferranti telephoned the police in Providence to convey the information he had uncovered. An hour later, three officers from that department arrived at the Cranston headquarters for the purpose of questioning respondent about the murder.</p>
<p>That same evening, at about 7:45 p.m., respondent's sister telephoned the Public Defender's Office to obtain legal assistance for her brother. Her sole concern was the breaking and entering charge, as she was unaware that respondent was then under suspicion for murder. She asked for Richard Casparian who had been scheduled to meet with respondent earlier that afternoon to discuss another charge unrelated to either the break-in or the murder. As soon as the conversation <span class="star-pagination">*417</span> ended, the attorney who took the call attempted to reach Mr. Casparian. When those efforts were unsuccessful, she telephoned Allegra Munson, another Assistant Public Defender, and told her about respondent's arrest and his sister's subsequent request that the office represent him.</p>
<p>At 8:15 p.m., Ms. Munson telephoned the Cranston police station and asked that her call be transferred to the detective division. In the words of the Supreme Court of Rhode Island, whose factual findings we treat as presumptively correct, <span class="citation no-link">28 U. S. C. § 2254</span>(d), the conversation proceeded as follows:</p>
<blockquote>"A male voice responded with the word `Detectives.' Ms. Munson identified herself and asked if Brian Burbine was being held; the person responded affirmatively. Ms. Munson explained to the person that Burbine was represented by attorney Casparian who was not available; she further stated that she would act as Burbine's legal counsel in the event that the police intended to place him in a lineup or question him. The unidentified person told Ms. Munson that the police would not be questioning Burbine or putting him in a lineup and that they were through with him for the night. Ms. Munson was not informed that the Providence Police were at the Cranston police station or that Burbine was a suspect in Mary's murder." <i>State</i> v. <i>Burbine,</i> <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#23" aria-description="Citation for case: State v. Burbine">451 A. 2d 22, 23-24</a></span> (1982).</blockquote>
<p>At all relevant times, respondent was unaware of his sister's efforts to retain counsel and of the fact and contents of Ms. Munson's telephone conversation.</p>
<p>Less than an hour later, the police brought respondent to an interrogation room and conducted the first of a series of interviews concerning the murder. Prior to each session, respondent was informed of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and on three separate occasions he signed a written form acknowledging that he understood his right to the presence of an attorney and explicitly indicating that he "[did] not want an attorney <span class="star-pagination">*418</span> called or appointed for [him]" before he gave a statement. App. to Pet. for Cert. 94, 103, 107. Uncontradicted evidence at the suppression hearing indicated that at least twice during the course of the evening, respondent was left in a room where he had access to a telephone, which he apparently declined to use. Tr. of Suppression Hearing 23, 85. Eventually, respondent signed three written statements fully admitting to the murder.</p>
<p>Prior to trial, respondent moved to suppress the statements. The court denied the motion, finding that respondent had received the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and had "knowingly, intelligently, and voluntarily waived his privilege against self-incrimination [and] his right to counsel." App. to Pet. for Cert. 116. Rejecting the contrary testimony of the police, the court found that Ms. Munson did telephone the detective bureau on the evening in question, but concluded that "there was no . . . conspiracy or collusion on the part of the Cranston Police Department to secrete this defendant from his attorney." <i>Id.,</i> at 114. In any event, the court held, the constitutional right to request the presence of an attorney belongs solely to the defendant and may not be asserted by his lawyer. Because the evidence was clear that respondent never asked for the services of an attorney, the telephone call had no relevance to the validity of the waiver or the admissibility of the statements.</p>
<p>The jury found respondent guilty of murder in the first degree, and he appealed to the Supreme Court of Rhode Island. A divided court rejected his contention that the Fifth and Fourteenth Amendments to the Constitution required the suppression of the inculpatory statements and affirmed the conviction. Failure to inform respondent of Ms. Munson's efforts to represent him, the court held, did not undermine the validity of the waivers. "It hardly seems conceivable that the additional information that an attorney whom he did not know had called the police station would have added significantly to the quantum of information necessary for the <span class="star-pagination">*419</span> accused to make an informed decision as to waiver." <i>State</i> v. <i>Burbine</i> <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#29" aria-description="Citation for case: State v. Burbine">451 A. 2d 22, 29</a></span> (1982). Nor, the court concluded, did <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i> or any other decision of this Court independently require the police to honor Ms. Munson's request that interrogation not proceed in her absence. In reaching that conclusion, the court noted that because two different police departments were operating in the Cranston station house on the evening in question, the record supported the trial court's finding that there was no "conspiracy or collusion" to prevent Ms. Munson from seeing respondent. <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#30" aria-description="Citation for case: State v. Burbine">451 A. 2d, at 30, n. 5</a></span>. In any case, the court held, the right to the presence of counsel belongs solely to the accused and may not be asserted by "benign third parties, whether or not they happen to be attorneys." <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#28" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 28</a></span>.</p>
<p>After unsuccessfully petitioning the United States District Court for the District of Rhode Island for a writ of habeas corpus, <span class="citation" data-id="1869337"><a href="/opinion/1869337/burbine-v-moran/" aria-description="Citation for case: Burbine v. Moran">589 F. Supp. 1245</a></span> (1984), respondent appealed to the Court of Appeals for the First Circuit. That court reversed. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d 178</a></span> (1985). Finding it unnecessary to reach any arguments under the Sixth and Fourteenth Amendments, the court held that the police's conduct had fatally tainted respondent's "otherwise valid" waiver of his Fifth Amendment privilege against self-incrimination and right to counsel. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#184" aria-description="Citation for case: Brian K. Burbine v. John Moran"><i>Id.,</i> at 184</a></span>. The court reasoned that by failing to inform respondent that an attorney had called and that she had been assured that no questioning would take place until the next day, the police had deprived respondent of information crucial to his ability to waive his rights knowingly and intelligently. The court also found that the record would support "no other explanation for the refusal to tell Burbine of Attorney Munson's call than . . . deliberate or reckless irresponsibility." <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#185" aria-description="Citation for case: Brian K. Burbine v. John Moran"><i>Id.,</i> at 185</a></span>. This kind of "blameworthy action by the police," the court concluded, together with respondent's ignorance of the telephone call, "vitiate[d] any claim that [the] waiver of counsel was knowing and voluntary." <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#185" aria-description="Citation for case: Brian K. Burbine v. John Moran"><i>Id.,</i> at 185, 187</a></span>.</p>
<p><span class="star-pagination">*420</span> We granted certiorari to decide whether a prearraignment confession preceded by an otherwise valid waiver must be suppressed either because the police misinformed an inquiring attorney about their plans concerning the suspect or because they failed to inform the suspect of the attorney's efforts to reach him. <span class="citation multiple-matches"><a href="/c/U.%20S./471/1098/">471 U. S. 1098</a></span> (1985). We now reverse.</p>
<p></p>
<h2>II</h2>
<p>In <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i> the Court recognized that custodial interrogations, by their very nature, generate "compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. To combat this inherent compulsion, and thereby protect the Fifth Amendment privilege against self-incrimination, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> imposed on the police an obligation to follow certain procedures in their dealings with the accused. In particular, prior to the initiation of questioning, they must fully apprise the suspect of the State's intention to use his statements to secure a conviction, and must inform him of his rights to remain silent and to "have counsel present . . . if [he] so desires." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 468-470</a></span>. Beyond this duty to inform, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires that the police respect the accused's decision to exercise the rights outlined in the warnings. "If the individual indicates in any manner, at any time prior to or during questioning, that he wishes to remain silent, [or if he] states that he wants an attorney, the interrogation must cease." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#473" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 473-474</a></span>. See also <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981).</p>
<p>Respondent does not dispute that the Providence police followed these procedures with precision. The record amply supports the state-court findings that the police administered the required warnings, sought to assure that respondent understood his rights, and obtained an express written waiver prior to eliciting each of the three statements. Nor does respondent contest the Rhode Island courts' determination that he at no point requested the presence of a lawyer. <span class="star-pagination">*421</span> He contends instead that the confessions must be suppressed because the police's failure to inform him of the attorney's telephone call deprived him of information essential to his ability to knowingly waive his Fifth Amendment rights. In the alternative, he suggests that to fully protect the Fifth Amendment values served by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> we should extend that decision to condemn the conduct of the Providence police. We address each contention in turn.</p>
<p></p>
<h2>A</h2>
<p>Echoing the standard first articulated in <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938), <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> holds that "[t]he defendant may waive effectuation" of the rights conveyed in the warnings "provided the waiver is made voluntarily, knowingly and intelligently." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444, 475</a></span>. The inquiry has two distinct dimensions. <i>Edwards</i> v. <i>Arizona, supra,</i> at 482; <i>Brewer</i> v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#404" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 404</a></span> (1977). First, the relinquishment of the right must have been voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion, or deception. Second, the waiver must have been made with a full awareness of both the nature of the right being abandoned and the consequences of the decision to abandon it. Only if the "totality of the circumstances surrounding the interrogation" reveals both an uncoerced choice and the requisite level of comprehension may a court properly conclude that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights have been waived. <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#725" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 725</a></span> (1979). See also <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#374" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 374-375</a></span> (1979).</p>
<p>Under this standard, we have no doubt that respondent validly waived his right to remain silent and to the presence of counsel. The voluntariness of the waiver is not at issue. As the Court of Appeals correctly acknowledged, the record is devoid of any suggestion that police resorted to physical or psychological pressure to elicit the statements. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#184" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d, at 184</a></span>. Indeed it appears that it was respondent, and not the <span class="star-pagination">*422</span> police, who spontaneously initiated the conversation that led to the first and most damaging confession. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#180" aria-description="Citation for case: Brian K. Burbine v. John Moran"><i>Id.,</i> at 180</a></span>. Cf. <i>Edwards</i> v. <i>Arizona, supra</i><i>.</i> Nor is there any question about respondent's comprehension of the full panoply of rights set out in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and of the potential consequences of a decision to relinquish them. Nonetheless, the Court of Appeals believed that the "[d]eliberate or reckless" conduct of the police, in particular their failure to inform respondent of the telephone call, fatally undermined the validity of the otherwise proper waiver. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#187" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d, at 187</a></span>. We find this conclusion untenable as a matter of both logic and precedent.</p>
<p>Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right. Under the analysis of the Court of Appeals, the same defendant, armed with the same information and confronted with precisely the same police conduct, would have knowingly waived his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights had a lawyer not telephoned the police station to inquire about his status. Nothing in any of our waiver decisions or in our understanding of the essential components of a valid waiver requires so incongruous a result. No doubt the additional information would have been useful to respondent; perhaps even it might have affected his decision to confess. But we have never read the Constitution to require that the police supply a suspect with a flow of information to help him calibrate his self-interest in deciding whether to speak or stand by his rights. See, <i>e. g., </i><i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 316-317</a></span> (1985); <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span> (1977). Cf. <i>Hill</i> v. <i>Lockhart,</i> <span class="citation" data-id="9430227"><a href="/opinion/111539/hill-v-lockhart/#56" aria-description="Citation for case: Hill v. Lockhart">474 U. S. 52, 56</a></span> (1985); <i>McMann</i> v. <i>Richardson,</i> <span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/#769" aria-description="Citation for case: McMann v. Richardson">397 U. S. 759, 769</a></span> (1970). Once it is determined that a suspect's decision not to rely on his rights was uncoerced, that he at all times knew he could stand mute and request a lawyer, and that he was aware of the State's intention to use his statements to secure a conviction, the analysis <span class="star-pagination">*423</span> is complete and the waiver is valid as a matter of law.<sup>[1]</sup> The Court of Appeals' conclusion to the contrary was in error.</p>
<p>Nor do we believe that the level of the police's culpability in failing to inform respondent of the telephone call has any bearing on the validity of the waivers. In light of the state-court findings that there was no "conspiracy or collusion" on the part of the police, <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#30" aria-description="Citation for case: State v. Burbine">451 A. 2d, at 30, n. 5</a></span>, we have serious doubts about whether the Court of Appeals was free to conclude that their conduct constituted "deliberate or reckless irresponsibility." <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#185" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d, at 185</a></span>; see <span class="citation no-link">28 U. S. C. § 2254</span>(d). But whether intentional or inadvertent, the state of mind of the police is irrelevant to the question of the intelligence and voluntariness of respondent's election to abandon his rights. Although highly inappropriate, even deliberate deception of an attorney could not possibly affect a suspect's decision to waive his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights unless he were at least aware of the incident. Compare <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#481" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 481</a></span> (1964) (excluding confession where police incorrectly told the <i>suspect</i> that his lawyer " `didn't want to see' him"). Nor was the failure to inform respondent of the telephone call the kind of "trick[ery]" that can vitiate the validity of a waiver. <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span>. Granting that the "deliberate or reckless" withholding of information is objectionable as a <span class="star-pagination">*424</span> matter of ethics, such conduct is only relevant to the constitutional validity of a waiver if it deprives a defendant of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them. Because respondent's voluntary decision to speak was made with full awareness and comprehension of all the information <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires the police to convey, the waivers were valid.</p>
<p></p>
<h2>B</h2>
<p>At oral argument respondent acknowledged that a constitutional rule requiring the police to inform a suspect of an attorney's efforts to reach him would represent a significant extension of our precedents. Tr. of Oral Arg. 32-33. He contends, however, that the conduct of the Providence police was so inimical to the Fifth Amendment values <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> seeks to protect that we should read that decision to condemn their behavior. Regardless of any issue of waiver, he urges, the Fifth Amendment requires the reversal of a conviction if the police are less than forthright in their dealings with an attorney or if they fail to tell a suspect of a lawyer's unilateral efforts to contact him. Because the proposed modification ignores the underlying purposes of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rules and because we think that the decision as written strikes the proper balance between society's legitimate law enforcement interests and the protection of the defendant's Fifth Amendment rights, we decline the invitation to further extend <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s reach.</p>
<p>At the outset, while we share respondent's distaste for the deliberate misleading of an officer of the court, reading <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to forbid police deception of an <i>attorney</i> "would cut [the decision] completely loose from its own explicitly stated rationale." <i>Beckwith</i> v. <i>United States,</i> <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#345" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 345</a></span> (1976). As is now well established, "[t]he . . . <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are `not themselves rights protected by the Constitution but [are] instead measures to insure that the [suspect's] right against compulsory self-incrimination [is] protected.' " <span class="star-pagination">*425</span> <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984), quoting <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974). Their objective is not to mold police conduct for its own sake. Nothing in the Constitution vests in us the authority to mandate a code of behavior for state officials wholly unconnected to any federal right or privilege. The purpose of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings instead is to dissipate the compulsion inherent in custodial interrogation and, in so doing, guard against abridgment of the suspect's Fifth Amendment rights. Clearly, a rule that focuses on how the police treat an attorney  conduct that has no relevance at all to the degree of compulsion experienced by the defendant during interrogation  would ignore both <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s mission and its only source of legitimacy.</p>
<p>Nor are we prepared to adopt a rule requiring that the police inform a suspect of an attorney's efforts to reach him. While such a rule might add marginally to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s goal of dispelling the compulsion inherent in custodial interrogation, overriding practical considerations counsel against its adoption. As we have stressed on numerous occasions, "[o]ne of the principal advantages" of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is the ease and clarity of its application. <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 430</a></span> (1984); see also <i>New York</i> v. <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#662" aria-description="Citation for case: New York v. Quarles"><i>Quarles, supra,</i> at 662-664</a></span> (concurring opinion); <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S., at 718</a></span>. We have little doubt that the approach urged by respondent and endorsed by the Court of Appeals would have the inevitable consequence of muddying <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s otherwise relatively clear waters. The legal questions it would spawn are legion: To what extent should the police be held accountable for knowing that the accused has counsel? Is it enough that someone in the station house knows, or must the interrogating officer himself know of counsel's efforts to contact the suspect? Do counsel's efforts to talk to the suspect concerning one criminal investigation trigger the obligation to inform the defendant before interrogation may proceed on a wholly separate matter? We are unwilling to modify <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in a <span class="star-pagination">*426</span> manner that would so clearly undermine the decision's central "virtue of informing police and prosecutors with specificity. . . what they may do in conducting [a] custodial interrogation, and of informing courts under what circumstances statements obtained during such interrogation are not admissible." <i>Fare</i> v. <i>Michael C., supra,</i> at 718.</p>
<p>Moreover, problems of clarity to one side, reading <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to require the police in each instance to inform a suspect of an attorney's efforts to reach him would work a substantial and, we think, inappropriate shift in the subtle balance struck in that decision. Custodial interrogations implicate two competing concerns. On the one hand, "the need for police questioning as a tool for effective enforcement of criminal laws" cannot be doubted. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#225" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 225</a></span> (1973). Admissions of guilt are more than merely "desirable," <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#186" aria-description="Citation for case: United States v. Washington">431 U. S., at 186</a></span>; they are essential to society's compelling interest in finding, convicting, and punishing those who violate the law. On the other hand, the Court has recognized that the interrogation process is "inherently coercive" and that, as a consequence, there exists a substantial risk that the police will inadvertently traverse the fine line between legitimate efforts to elicit admissions and constitutionally impermissible compulsion. <i>New York</i> v. <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#656" aria-description="Citation for case: New York v. Quarles"><i>Quarles, supra,</i> at 656</a></span>. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> attempted to reconcile these opposing concerns by giving the <i>defendant</i> the power to exert some control over the course of the interrogation. Declining to adopt the more extreme position that the actual presence of a lawyer was necessary to dispel the coercion inherent in custodial interrogation, see Brief for American Civil Liberties Union as <i>Amicus Curiae</i> in <i>Miranda</i> v. <i>Arizona</i><i>,</i> O. T. 1965, No. 759, pp. 22-31, the Court found that the suspect's Fifth Amendment rights could be adequately protected by less intrusive means. Police questioning, often an essential part of the investigatory process, could continue in its traditional form, the Court held, but only if the suspect clearly understood <span class="star-pagination">*427</span> that, at any time, he could bring the proceeding to a halt or, short of that, call in an attorney to give advice and monitor the conduct of his interrogators.</p>
<p>The position urged by respondent would upset this carefully drawn approach in a manner that is both unnecessary for the protection of the Fifth Amendment privilege and injurious to legitimate law enforcement. Because, as <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> holds, full comprehension of the rights to remain silent and request an attorney are sufficient to dispel whatever coercion is inherent in the interrogation process, a rule requiring the police to inform the suspect of an attorney's efforts to contact him would contribute to the protection of the Fifth Amendment privilege only incidentally, if at all. This minimal benefit, however, would come at a substantial cost to society's legitimate and substantial interest in securing admissions of guilt. Indeed, the very premise of the Court of Appeals was not that awareness of Ms. Munson's phone call would have dissipated the coercion of the interrogation room, but that it might have convinced respondent not to speak at all. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#185" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d, at 185</a></span>. Because neither the letter nor purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> require this additional handicap on otherwise permissible investigatory efforts, we are unwilling to expand the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rules to require the police to keep the suspect abreast of the status of his legal representation.</p>
<p>We acknowledge that a number of state courts have reached a contrary conclusion. Compare <i>State</i> v. <i>Jones,</i> <span class="citation" data-id="1174756"><a href="/opinion/1174756/state-v-jones/" aria-description="Citation for case: State v. Jones">19 Wash. App. 850</a></span>, <span class="citation" data-id="1174756"><a href="/opinion/1174756/state-v-jones/" aria-description="Citation for case: State v. Jones">578 P. 2d 71</a></span> (1978), with <i>State</i> v. <i>Beck,</i> <span class="citation" data-id="9647546"><a href="/opinion/1525657/state-v-beck/" aria-description="Citation for case: State v. Beck">687 S. W. 2d 155</a></span> (Mo. 1985) (en banc). We recognize also that our interpretation of the Federal Constitution, if given the dissent's expansive gloss, is at odds with the policy recommendations embodied in the American Bar Association Standards of Criminal Justice. Cf. ABA Standards for Criminal Justice 5-7.1 (2d ed. 1980). Notwithstanding the dissent's protestations, however, our interpretive duties go well beyond deferring to the numerical preponderance of lower court decisions or to the subconstitutional recommendations <span class="star-pagination">*428</span> of even so esteemed a body as the American Bar Association. See <i>Nix</i> v. <i>Whiteside, ante,</i> at 189 (BLACKMUN, J., concurring in judgment). Nothing we say today disables the States from adopting different requirements for the conduct of its employees and officials as a matter of state law. We hold only that the Court of Appeals erred in construing the Fifth Amendment to the Federal Constitution to require the exclusion of respondent's three confessions.</p>
<p></p>
<h2>III</h2>
<p>Respondent also contends that the Sixth Amendment requires exclusion of his three confessions.<sup>[2]</sup> It is clear, of course, that, absent a valid waiver, the defendant has the right to the presence of an attorney during any interrogation occurring after the first formal charging proceeding, the point at which the Sixth Amendment right to counsel initially attaches. <i>United States</i> v. <i>Gouveia,</i> <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#187" aria-description="Citation for case: United States v. Gouveia">467 U. S. 180, 187</a></span> (1984); <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 689</a></span> (1972) (opinion of Stewart, J.). See <i>Brewer</i> v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#400" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 400-401</a></span>. And we readily agree that once the right <i>has</i> attached, it follows that the police may not interfere with the efforts of a defendant's attorney to act as a " `medium' between [the suspect] and the State" during the interrogation. <i>Maine</i> v. <i>Moulton,</i> <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 176</a></span> (1985); see <i>Brewer</i> v. <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#401" aria-description="Citation for case: Brewer v. Williams"><i>Williams, supra,</i> at 401, n. 8</a></span>. The difficulty for respondent is that the interrogation sessions that yielded the inculpatory statements took place <i>before</i> the initiation of "adversary judicial proceedings." <i>United States</i> v. <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#192" aria-description="Citation for case: United States v. Gouveia"><i>Gouveia, supra,</i> at 192</a></span>. He contends, however, that this circumstance is not fatal to his Sixth Amendment claim. At least in some situations, he argues, the Sixth Amendment protects the integrity of the <span class="star-pagination">*429</span> attorney-client relationship<sup>[3]</sup> regardless of whether the prosecution has in fact commenced "by way of formal charge, preliminary hearing, indictment, information or arraignment." 467 U. S., at 188. Placing principal reliance on a footnote in <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#465" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 465, n. 35</a></span>, and on <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), he maintains that <i>Gouveia, Kirby,</i> and our other "critical stage" cases, concern only the narrow question of when the right <i>to</i> counsel  that is, to the appointment or presence of counsel  attaches. The right to non-interference with an attorney's dealings with a criminal suspect, he asserts, arises the moment that the relationship is formed, or, at the very least, once the defendant is placed in custodial interrogation.</p>
<p>We are not persuaded. At the outset, subsequent decisions foreclose any reliance on <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> and <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> for the proposition that the Sixth Amendment right, in any of its manifestations, applies prior to the initiation of adversary judicial proceedings. Although <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> was originally decided as a Sixth Amendment case, "the Court in retrospect perceived that the `prime purpose' of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> was not to vindicate the constitutional right to counsel as such, but, like <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> `to guarantee full effectuation of the privilege against self-incrimination . . . .' " <i>Kirby</i> v. <i>Illinois, supra,</i> <span class="star-pagination">*430</span> at 689, quoting <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#729" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719, 729</a></span> (1966). Clearly then, <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> provides no support for respondent's argument. Nor, of course, does <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the holding of which rested exclusively on the Fifth Amendment. Thus, the decision's brief observation about the reach of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i>'s Sixth Amendment analysis is not only dictum, but reflects an understanding of the case that the Court has expressly disavowed. See also, <i>United States</i> v. <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#188" aria-description="Citation for case: United States v. Gouveia"><i>Gouveia, supra,</i> at 188, n. 5</a></span>; Y. Kamisar, Police Interrogation and Confessions 217-218, n. 94 (1980).</p>
<p>Questions of precedent to one side, we find respondent's understanding of the Sixth Amendment both practically and theoretically unsound. As a practical matter, it makes little sense to say that the Sixth Amendment right to counsel attaches at different times depending on the fortuity of whether the suspect or his family happens to have retained counsel prior to interrogation. Cf. <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#220" aria-description="Citation for case: United States v. Gouveia"><i>id.,</i> at 220-221</a></span>. More importantly, the suggestion that the existence of an attorney-client relationship itself triggers the protections of the Sixth Amendment misconceives the underlying purposes of the right to counsel. The Sixth Amendment's intended function is not to wrap a protective cloak around the attorney-client relationship for its own sake any more than it is to protect a suspect from the consequences of his own candor. Its purpose, rather, is to assure that in any "criminal prosecutio[n]," U. S. Const., Amdt. 6, the accused shall not be left to his own devices in facing the " `prosecutorial forces of organized society.' " <i>Maine</i> v. <i><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton, supra,</a></span></i> at 170 (quoting <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>). By its very terms, it becomes applicable only when the government's role shifts from investigation to accusation. For it is only then that the assistance of one versed in the "intricacies . . . of law," <i>ibid.,</i> is needed to assure that the prosecution's case encounters "the crucible of meaningful adversarial testing." <i>United States</i> v. <i>Cronic,</i> <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#656" aria-description="Citation for case: United States v. Cronic">466 U. S. 648, 656</a></span> (1984).</p>
<p><span class="star-pagination">*431</span> Indeed, in <i>Maine</i> v. <i><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton</a></span></i><i>,</i> decided this Term, the Court again confirmed that looking to the initiation of adversary judicial proceedings, far from being mere formalism, is fundamental to the proper application of the Sixth Amendment right to counsel. There, we considered the constitutional implications of a surreptitious investigation that yielded evidence pertaining to two crimes. For one, the defendant had been indicated; for the other, he had not. Concerning the former, the Court reaffirmed that after the first charging proceeding the government may not deliberately elicit incriminating statements from an accused out of the presence of counsel. See also <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964). The Court made clear, however, that the evidence concerning the crime for which the defendant had not been indicted  evidence obtained in precisely the same manner from the identical suspect  would be admissible at a trial limited to those charges. <i>Maine</i> v. <i>Moulton,</i> <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#180" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 180</a></span>, and n. 16. The clear implication of the holding, and one that confirms the teaching of <i><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/" aria-description="Citation for case: United States v. Gouveia">Gouveia</a></span>,</i> is that the Sixth Amendment right to counsel does not attach until after the initiation of formal charges. Moreover, because Moulton already had legal representation, the decision all but forecloses respondent's argument that the attorney-client relationship itself triggers the Sixth Amendment right.</p>
<p>Respondent contends, however, that custodial interrogations require a different rule. Because confessions elicited during the course of police questioning often seal a suspect's fate, he argues, the need for an advocate  and the concomitant right to noninterference with the attorney-client relationship  is at its zenith, regardless of whether the State has initiated the first adversary judicial proceeding. We do not doubt that a lawyer's presence could be of value to the suspect; and we readily agree that if a suspect confesses, his attorney's case at trial will be that much more difficult. But these concerns are no more decisive in this context than they were for the equally damaging preindictment lineup <span class="star-pagination">*432</span> at issue in <i><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span>,</i> or the statements pertaining to the unindicted crime elicted from the defendant in <i>Maine</i> v. <i><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton</a></span></i><i>.</i> Compare <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#226" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 226-227</a></span> (1967) (Sixth Amendment attaches at postindictment lineup); <i>Massiah</i> v. <i>United States, supra</i> (after indictment, police may not elicit statements from suspect out of the presence of counsel). For an interrogation, no more or less than for any other "critical" pretrial event, the possibility that the encounter may have important consequences at trial, standing alone, is insufficient to trigger the Sixth Amendment right to counsel. As <i><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/" aria-description="Citation for case: United States v. Gouveia">Gouveia</a></span></i> made clear, until such time as the " `government has committed itself to prosecute, and . . . the adverse positions of government and defendant have solidified' " the Sixth Amendment right to counsel does not attach. 467 U. S., at 189 (quoting <i>Kirby</i> v. <i>Illinois, supra,</i> at 689).</p>
<p>Because, as respondent acknowledges, the events that led to the inculpatory statements preceded the formal initiation of adversary judicial proceedings, we reject the contention that the conduct of the police violated his rights under the Sixth Amendment.</p>
<p></p>
<h2>IV</h2>
<p>Finally, respondent contends that the conduct of the police was so offensive as to deprive him of the fundamental fairness guaranteed by the Due Process Clause of the Fourteenth Amendment. Focusing primarily on the impropriety of conveying false information to an attorney, he invites us to declare that such behavior should be condemned as violative of canons fundamental to the " `traditions and conscience of our people.' " <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#169" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 169</a></span> (1952), quoting <i>Snyder</i> v. <i>Massachusetts,</i> <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span> (1934). We do not question that on facts more egregious than those presented here police deception might rise to a level of a due process violation. Accordingly, JUSTICE STEVENS' <span class="star-pagination">*433</span> apocalyptic suggestion that we have approved any and all forms of police misconduct is demonstrably incorrect.<sup>[4]</sup> We hold only that, on these facts, the challenged conduct falls short of the kind of misbehavior that so shocks the sensibilities <span class="star-pagination">*434A</span> of civilized society as to warrant a federal intrusion into the criminal processes of the States.</p>
<p>We hold therefore that the Court of Appeals erred in finding that the Federal Constitution required the exclusion of the three inculpatory statements. Accordingly, we reverse and remand for proceedings consistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p><span class="star-pagination">*434B</span> JUSTICE STEVENS, with whom JUSTICE BRENNAN and JUSTICE MARSHALL join, dissenting.</p>
<p>This case poses fundamental questions about our system of justice. As this Court has long recognized, and reaffirmed only weeks ago, "ours is an accusatorial and not an inquisitorial system." <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#110" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 110</a></span> (1985).<sup>[1]</sup> The Court's opinion today represents a startling departure from that basic insight.</p>
<p><span class="star-pagination">*435</span> The Court concludes that the police may deceive an attorney by giving her false information about whether her client will be questioned, and that the police may deceive a suspect by failing to inform him of his attorney's communications and efforts to represent him.<sup>[2]</sup> For the majority, this conclusion, though "distaste[ful]," <i>ante,</i> at 424, is not even debatable. The deception of the attorney is irrelevant because the attorney has no right to information, accuracy, honesty, or fairness in the police response to her questions about her client. The deception of the client is acceptable, because, although the information would affect the client's assertion of his rights, the client's actions in ignorance of the availability of his attorney are voluntary, knowing, and intelligent; additionally, society's interest in apprehending, prosecuting, and punishing criminals outweighs the suspect's interest in information regarding his attorney's efforts to communicate with him. Finally, even mendacious police interference in the communications between a suspect and his lawyer does not violate any notion of fundamental fairness because it does not shock the conscience of the majority.</p>
<p>The case began in March 1977 with the discovery of Mary Jo Hickey, unconscious and disheveled in a deserted parking lot, lying in a pool of blood, with semen on her clothes, her dentures broken, and a piece of heavy, bloodstained metal nearby. Days later, Brian Burbine, then 20 years old, went to Maine and stayed with friends. According to the friends' testimony at trial, he was upset, and described a night out with Hickey, who was then 35. After several drinks, <span class="star-pagination">*436</span> Burbine told them, a ride home turned into a violent encounter; he hit Hickey several times and threw her out of the car. Three weeks after she was discovered in the parking lot, Hickey died. Three months later, after the 21-hour period of detention by the Cranston and Providence, Rhode Island, police that is the focus of this dispute, Burbine was charged with her murder, and ultimately found guilty of it.</p>
<p>The murder of Mary Jo Hickey was a vicious crime, fully meriting a sense of outrage and a desire to find and prosecute the perpetrator swiftly and effectively. Indeed, by the time Burbine was arrested on an unrelated breaking-and-entering charge, the Hickey murder had been the subject of a local television special.<sup>[3]</sup> Not surprisingly, Detective Ferranti, the Cranston Detective who "broke" the case, was rewarded with a special commendation for his efforts.<sup>[4]</sup></p>
<p>The recognition that ours is an accusatorial, and not an inquisitorial system nevertheless requires that the government's actions, even in responding to this brutal crime, respect those liberties and rights that distinguish this society from most others. As Justice Jackson observed shortly after his return from Nuremberg, cases of this kind present "a real dilemma in a free society . . . for the defendant is shielded by such safeguards as no system of law except the Anglo-American concedes to him."<sup>[5]</sup> Justice Frankfurter similarly <span class="star-pagination">*437</span> emphasized that it is "a fair summary of history to say that the safeguards of liberty have been forged in controversies involving not very nice people."<sup>[6]</sup> And, almost a century and a half ago, Macaulay observed that the guilt of Titus Oates could not justify his conviction by improper methods: "That Oates was a bad man is not a sufficient excuse; for the guilty are almost always the first to suffer those hardships which are afterwards used as precedents against the innocent."<sup>[7]</sup></p>
<p>The Court's holding focuses on the period after a suspect has been taken into custody and before he has been charged with an offense. The core of the Court's holding is that police interference with an attorney's access to her client during that period is not unconstitutional. The Court reasons that a State has a compelling interest, not simply in custodial interrogation, but in lawyer-free, incommunicado custodial interrogation. Such incommunicado interrogation is so important that a lawyer may be given false information that prevents her presence and representation; it is so important that police may refuse to inform a suspect of his attorney's <span class="star-pagination">*438</span> communications and immediate availability.<sup>[8]</sup> This conclusion flies in the face of this Court's repeated expressions of deep concern about incommunicado questioning.<sup>[9]</sup> Until <span class="star-pagination">*439</span> today, incommunicado questioning has been viewed with the strictest scrutiny by this Court; today, incommunicado questioning is embraced as a societal goal of the highest order that justifies police deception of the shabbiest kind.</p>
<p>It is not only the Court's ultimate conclusion that is deeply disturbing; it is also its manner of reaching that conclusion. The Court completely rejects an entire body of law on the subject  the many carefully reasoned state decisions that have come to precisely the opposite conclusion.<sup>[10]</sup> The Court <span class="star-pagination">*440</span> similarly dismisses the fact that the police deception which it sanctions quite clearly violates the American Bar Association's Standards for Criminal Justice<sup>[11]</sup>  Standards which <span class="star-pagination">*441</span> THE CHIEF JUSTICE has described as "the single most comprehensive and probably the most monumental undertaking in the field of criminal justice ever attempted by the American legal profession in our national history,"<sup>[12]</sup> and which this Court frequently finds helpful.<sup>[13]</sup> And, of course, the Court dismisses the fact that the American Bar Association has emphatically endorsed the prevailing state-court position and expressed its serious concern about the effect that a contrary view  a view, such as the Court's, that exalts incommunicado interrogation, sanctions police deception, and demeans the right to consult with an attorney  will have in police stations and courtrooms throughout this Nation.<sup>[14]</sup> Of greatest importance, the Court misapprehends or rejects the central principles that have, for several decades, animated this Court's decisions concerning incommunicado interrogation.<sup>[15]</sup></p>
<p>Police interference with communications between an attorney and his client is a recurrent problem. The factual variations in the many state-court opinions condemning this interference as a violation of the Federal Constitution suggest the <span class="star-pagination">*442</span> variety of contexts in which the problem emerges. In Oklahoma, police led a lawyer to several different locations while they interrogated the suspect;<sup>[16]</sup> in Oregon, police moved a suspect to a new location when they learned that his lawyer was on his way;<sup>[17]</sup> in Illinois, authorities failed to tell a suspect that his lawyer had arrived at the jail and asked to see him;<sup>[18]</sup> in Massachusetts, police did not tell suspects that their lawyers were at or near the police station.<sup>[19]</sup> In all these cases, the police not only failed to inform the suspect, but also misled the attorneys. The scenarios vary, but the core problem of police interference remains. "Its recurrence suggests that it has roots in some condition fundamental and general to our criminal system." <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#57" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 57</a></span> (1949) (Jackson, J., concurring in result).</p>
<p>The near-consensus of state courts and the legal profession's Standards about this recurrent problem lends powerful support to the conclusion that police may not interfere with communications between an attorney and the client whom they are questioning. Indeed, at least two opinions from this Court seemed to express precisely that view.<sup>[20]</sup> The Court today flatly rejects that widely held view and responds to this recurrent problem by adopting the most restrictive interpretation of the federal constitutional restraints on police <span class="star-pagination">*443</span> deception, misinformation, and interference in attorney-client communications.</p>
<p>The exact reach of the Court's opinion is not entirely clear because, on the one hand, it indicates that more egregious forms of police deception might violate the Constitution, <i>ante,</i> at 432, while, on the other hand, it endeavors to make its disposition of this case palatable by making findings of fact concerning the voluntariness of Burbine's confessions that the trial judge who heard the evidence declined to make.<sup>[21]</sup> Before addressing the legal issues, it therefore seems appropriate to make certain additional comments about what the record discloses concerning the incriminating statements made by Burbine during the 21-hour period that he was detained by the Cranston and Providence police on June 29 and June 30, 1977.</p>
<p></p>
<h2>I</h2>
<p>As the majority points out, with respect to attorney Munson's telephone call, the Rhode Island Supreme Court's summary of factual findings provides the common ground for analysis:</p>
<blockquote>"At approximately 8:15 [on June 29, 1977], Ms. Munson called the Cranston police station and asked that her call be transferred to the detective division. A male voice responded with the word `Detectives.' Ms. Munson identified herself and asked if Brian Burbine was being held; the person responded affirmatively. Ms. Munson explained to the person that Burbine was represented by attorney Casparian who was not available; she further stated that she would act as Burbine's legal counsel in the event that the police intended to place him in a lineup or question him. The unidentified person told Ms. Munson that the police would not be questioning Burbine or putting him in a lineup and that they were <span class="star-pagination">*444</span> through with him for the night. Ms. Munson was not informed that the Providence police were at the Cranston police station or that Burbine was a suspect in Mary's murder. The trial justice found as a fact that Ms. Munson did make the call, but further found that there was no collusion or conspiracy on the part of the police `to secrete [Burbine] from his attorney . . . .' " <i>State</i> v. <i>Burbine,</i> <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#23" aria-description="Citation for case: State v. Burbine">451 A. 2d 22, 23-24</a></span> (1982).<sup>[22]</sup></blockquote>
<p>Although this paragraph accurately describes attorney Munson's 8:15 call, the significance of the false response to her inquiry is best understood in the context of the events that were then proceeding in the police station. The difficulty in reconstructing some of those events illustrates the need for strict presumptions regarding the consequences of custodial interrogation  a need this Court has repeatedly recognized.<sup>[23]</sup></p>
<p><span class="star-pagination">*445</span> On June 27, 1977, an unidentified person advised Detective Ferranti that a man known as "Butch," who lived at 306 New York Avenue in Providence, was responsible for the death of Mary Jo Hickey. The record does not explain why Ferranti, who was a member of the Cranston Police Force, was informed about a crime that occurred in Providence.</p>
<p>At about 3 p.m. on June 29, 1977, Cranston police officers apprehended respondent Burbine and two other men (DiOrio and Sparks) in "a burned out building in the Cranston area." S. H. 6, 180. The three men were taken to the Cranston police station, charged with "breaking and entering," and placed in separate rooms. After noticing that DiOrio and Burbine lived at 306 New York Avenue in Providence, Detective Ferranti talked to DiOrio and was told that Burbine was the only "Butch" at that address. <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#146" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 146-147</a></span>.</p>
<p>At approximately 4:30, Ferranti "went in the room where Burbine was" and asked him "if there was anybody that he knew by the name of Butch on the street, and he said he was the only Butch." <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#148" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 148</a></span>.<sup>[24]</sup> After the brief questioning about the identity of "Butch," Detective Ferranti left Burbine in the interrogation room  where he remained until about 9 p.m.<sup>[25]</sup>  and interrogated DiOrio and Sparks. They both "made damaging statements relative to Burbine being involved in the murder in Providence"; Ferranti therefore "immediately contacted Providence Police." <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#149" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 149-150</a></span>. The Providence officers  Captain Wilson (the Chief of Detectives), Lieutenant Gannon, and Detective Trafford  responded promptly, and arrived at the Cranston station between <span class="star-pagination">*446</span> 6 and 7 p.m. Lieutenant Gannon testified that, as he drove to the Cranston police station, he knew that he might not be able to question Burbine "[i]f for some reason he didn't want to give me a statement, if for some reason he chose to get an attorney and the attorney informed us that he didn't want him to give a statement." Trial Tr. 407.</p>
<p>After arriving at the station, the three Providence officers, as well as Ferranti and a second Cranston officer (Lieutenant Ricard), either remained in the large central room in the basement of the Cranston police station, or participated in the questioning of DiOrio and Sparks in interrogation rooms adjacent to that large central room.</p>
<p>It was at this point  with Burbine alone in another adjacent room, with Providence police on hand, with police from two Departments questioning Sparks and DiOrio about Burbine's involvement in the Hickey homicide  that attorney Munson telephoned. Her call arrived at 8:15; she asked for "Detectives," and was told that the police "would not be questioning Burbine" and that they were "through" with him for the night. These statements were false. Moreover, she was not told that Burbine would be questioned about a homicide rather than the breaking-and-entering charge on which he had been arrested, and she was not told that Providence police were at the Cranston police station preparing to question Burbine about a Providence crime.</p>
<p>At about 9, some 45 minutes after Munson received the assurance that the police were "through" with Burbine, the officers completed their questioning of DiOrio and Sparks and were prepared to question Burbine. There is no dispute about the fact that Burbine was brought into the central room at about 9, that all five police officers were then present, and that Burbine appeared somewhat upset and professed that he " `didn't do anything wrong.' " S. H. 21. Detective Ferranti testified that this statement was in response to questions from the Providence police about the Hickey <span class="star-pagination">*447</span> homicide;<sup>[26]</sup> Lieutenant Gannon of the Providence police testified that the statement was about the Hickey homicide, but that Providence police did not question Burbine and that they merely saw Burbine being escorted by Ferranti.<sup>[27]</sup> Burbine was not told that attorney Munson had called and had asked about him; nor was he told that Munson had been informed that the police were through with him for the night. After his protestations, Burbine was taken into another interrogation room.</p>
<p>Detective Ferranti then went into that room and, according to the testimony of the Providence officers, spent either "ten minutes" or from "five to ten minutes" alone with Burbine.<sup>[28]</sup> The record does not tell us whether he told Burbine that Sparks and DiOrio had just given statements implicating him in the Hickey homicide. Nor does it resolve the question whether Burbine's decision to confess was made <i>before</i> his session with Ferranti or <i>as a result</i> of that session. The Court evidently makes the former assumption, for it asserts that Burbine "initiated" this encounter. <i>Ante,</i> at 421-422. However, the state courts made no finding about this <span class="star-pagination">*448</span> "initiation" by Burbine. Detective Ferranti testified that Burbine banged and kicked on the door, S. H. 153-154; Lieutenant Gannon testified that he "believed" there was a knocking or some communication from Burbine, <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#22" aria-description="Citation for case: State v. Burbine"><i>id.,</i> at 22</a></span>, but he was "not sure." <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#66" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 66</a></span>.<sup>[29]</sup> None of the other officers, who were apparently in the large room adjacent to Burbine's, corroborated this testimony by mentioning any "banging," "kicking," or other noise from Burbine's direction. In all events, some minutes later, Detective Ferranti came back out of the room and indicated that Burbine wanted to talk.</p>
<p>Lieutenant Gannon and Detective Trafford of the Providence police accompanied Detective Ferranti "back into the room." During the period between 9:30 and 10:20 p.m., they administered <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and typed out a four-page statement which Burbine signed, waiving his constitutional rights, acknowledging his responsibility for the death of Hickey, and reciting his version of that event. Ferranti alternately testified that Burbine was "coherent" and "incoherent" at the time of this questioning. <i>Id.,</i> at 157-158; Trial Tr. 198, 208-209. Apparently for the first time since his arrival at the station in the afternoon, the police then brought Burbine some food. S. H. 160, Trial Tr. 205.</p>
<p>After obtaining Burbine's signature on the first written statement at 10:20 p.m., the police were still not "through" with Burbine. Burbine's first statement included no mention of the clothes that he had been wearing, or of a glass that was found with Hickey's purse a few blocks from the homicide. Soon after the completion of the first statement, and after the Providence and Cranston officers had discussed the first statement and expressed pleasure with their success,<sup>[30]</sup><span class="star-pagination">*449</span> Gannon, Trafford, and Ferranti again questioned Burbine. They ascertained that he was wearing his "red toke" and "black windbreaker" at the time, and that Hickey had left the bar with a glass in hand.<sup>[31]</sup> At 11:20 p.m., Burbine signed the second statement.</p>
<p>The following morning, the officers obtained a warrant, conducted a search of Burbine's residence, and seized the clothing that he had described in the second statement. In the meantime, Burbine was arraigned in Cranston court on the charge for which he had been arrested. Still without counsel, Burbine pleaded guilty to malicious damage. After the Cranston proceeding, Providence officers instantly arrested him for the Hickey homicide. Trial Tr. 501. Burbine was taken to the Providence police station, where he executed a third waiver of rights and identified the coat and jacket that the officers had seized. Shortly after noon, Major Leyden called the Public Defender's Office and requested counsel for Burbine because he would be placed in a lineup. <i>Id.,</i> at 423.</p>
<p>Thus, although there are a number of ambiguities in the record, the state-court findings established (1) that attorney Munson made her call at about 8:15 p.m.; (2) that she was given false information; (3) that Burbine was not told of her <span class="star-pagination">*450</span> call; and (4) that he was thereafter given the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, waived his rights, and signed three incriminating statements without receiving any advice from an attorney. The remainder of the record underscores two points. The first is the context of the call  a context in which two Police Departments were on the verge of resolving a highly publicized, hauntingly brutal homicide and in which, as Lieutenant Gannon testified, the police were aware that counsel's advice to remain silent might be an obstacle to obtaining a confession. The second is the extent of the uncertainty about the events that motivated Burbine's decision to waive his rights. The lawyer-free privacy of the interrogation room, so exalted by the majority, provides great difficulties in determining what actually transpired. It is not simply the ambiguity that is troublesome; if so, the problem would be not unlike other difficult evidentiary problems. Rather, the particularly troublesome aspect is that the ambiguity arises in the very situation  incommunicado interrogation  for which this Court has developed strict presumptions and for which this Court has, in the past, imposed the heaviest burden of justification on the government. It is in this context, and the larger context of our accusatorial system, that the deceptive conduct of the police must be evaluated.</p>
<p></p>
<h2>II</h2>
<p>Well-settled principles of law lead inexorably to the conclusion that the failure to inform Burbine of the call from his attorney makes the subsequent waiver of his constitutional rights invalid. Analysis should begin with an acknowledgment that the burden of proving the validity of a waiver of constitutional rights is always on the <i>government.</i><sup>[32]</sup> When <span class="star-pagination">*451</span> such a waiver occurs in a custodial setting, that burden is an especially heavy one because custodial interrogation is inherently coercive,<sup>[33]</sup> because disinterested witnesses are seldom available to describe what actually happened,<sup>[34]</sup> and because history has taught us that the danger of overreaching during incommunicado interrogation is so real.<sup>[35]</sup></p>
<p>In applying this heavy presumption against the validity of waivers, this Court has sometimes relied on a case-by-case totality of the circumstances analysis.<sup>[36]</sup> We have found, however, that some custodial interrogation situations require strict presumptions against the validity of a waiver. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> established that a waiver is not valid in the absence of certain warnings. <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), similarly established that a waiver is not valid if police <span class="star-pagination">*452</span> initiate questioning after the defendant has invoked his right to counsel. In these circumstances, the waiver is invalid as a matter of law even if the evidence overwhelmingly establishes, as a matter of fact, that "a suspect's decision not to rely on his rights was uncoerced, that he at all times knew that he could stand mute and request a lawyer, and that he was aware of the State's intention to use his statements to secure a conviction," see <i>ante,</i> at 422. In light of our decision in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> the Court is simply wrong in stating that "the analysis is complete and the waiver is valid as a matter of law" when these facts have been established. <i>Ante,</i> at 422-423.<sup>[37]</sup> Like the failure to give warnings and like police initiation of interrogation after a request for counsel, police deception of a suspect through omission of information regarding attorney communications greatly exacerbates the inherent problems of incommunicado interrogation and requires a clear principle to safeguard the presumption against the waiver of constitutional rights. As in those situations, the police deception should render a subsequent waiver invalid.</p>
<p>Indeed, as <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> itself makes clear, proof that the required warnings have been given is a necessary, but by no means sufficient, condition for establishing a valid waiver. As the Court plainly stated in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> "any evidence that the accused was threatened, tricked, or cajoled into a waiver will, of course, show that the defendant did not voluntarily waive his privilege. The requirement of warnings and waiver of rights is a fundamental with respect to the Fifth <span class="star-pagination">*453</span> Amendment privilege and not simply a preliminary ritual to existing methods of interrogation." 384 U. S., at 476.</p>
<p>In this case it would be perfectly clear that Burbine's waiver was invalid if, for example, Detective Ferranti had "threatened, tricked, or cajoled" Burbine in their private preconfession meeting  perhaps by misdescribing the statements obtained from DiOrio and Sparks  even though, under the Court's truncated analysis of the issue, Burbine fully understood his rights. For <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> clearly condemns threats or trickery that cause a suspect to make an unwise waiver of his rights even though he fully understands those rights. In my opinion there can be no constitutional distinction  as the Court appears to draw, <i>ante,</i> at 423-424  between a deceptive misstatement and the concealment by the police of the critical fact that an attorney retained by the accused or his family has offered assistance, either by telephone or in person.<sup>[38]</sup></p>
<p>Thus, the Court's truncated analysis, which relies in part on a distinction between deception accomplished by means of an omission of a critically important fact and deception by means of a misleading statement, is simply untenable. If, as the Court asserts, "the analysis is at an end" as soon as the suspect is provided with enough information to have the <i>capacity</i> to understand and exercise his rights, I see no reason why the police should not be permitted to make the same kind of misstatements to the suspect that they are apparently allowed to make to his lawyer. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> however, clearly <span class="star-pagination">*454</span> establishes that both kinds of deception vitiate the suspect's waiver of his right to counsel.<sup>[39]</sup></p>
<p>As the Court notes, the question is whether the deceptive police conduct "deprives a defendant of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them." <i>Ante,</i> at 424. This question has been resoundingly answered time and time again by the state courts that, with rare exceptions,<sup>[40]</sup> have correctly understood the meaning of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion.<sup>[41]</sup> The majority's <span class="star-pagination">*455</span> blithe assertion of "no doubt" about the outcome of this case, <i>ante,</i> at 421, simply ignores the prevailing view of the state courts that have considered this issue. Particularly in an opinion that relies on a desire to avoid "a federal intrusion into the criminal processes of the States," <i>ante,</i> at 434, one would expect at least some indication why, in the majority's view, so many state courts have been so profoundly wrong on this precise issue. Unlike the majority, the state courts have realized that attorney communication to the police <span class="star-pagination">*456</span> about the client is an event that has a direct "bearing" on the knowing and intelligent waiver of constitutional rights. As the Oregon Supreme Court has explained: "To pass up an abstract offer to call some unknown lawyer is very different from refusing to talk with an identified attorney actually available to provide at least initial assistance and advice, whatever might be arranged in the long run. A suspect indifferent to the first offer may well react quite differently to the second." <i>State</i> v. <i>Haynes,</i> <span class="citation" data-id="9578898"><a href="/opinion/1320570/state-v-haynes/#72" aria-description="Citation for case: State v. Haynes">288 Ore. 59, 72</a></span>, <span class="citation" data-id="9578898"><a href="/opinion/1320570/state-v-haynes/#278" aria-description="Citation for case: State v. Haynes">602 P. 2d 272, 278</a></span> (1979), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./446/945/">446 U. S. 945</a></span> (1980).<sup>[42]</sup></p>
<p>In short, settled principles about construing waivers of constitutional rights and about the need for strict presumptions in custodial interrogations, as well as a plain reading of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion itself, overwhelmingly support the conclusion reached by almost every state court that has considered the matter  a suspect's waiver of his right to counsel is invalid if police refuse to inform the suspect of his counsel's communications.</p>
<p></p>
<h2>III</h2>
<p>The Court makes the alternative argument that requiring police to inform a suspect of his attorney's communications to <span class="star-pagination">*457</span> and about him is not required because it would upset the careful "balance" of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> Despite its earlier notion that the attorney's call is an "outside event" that has "no bearing" on a knowing and intelligent waiver, the majority does acknowledge that information of attorney Munson's call "would have been useful to respondent" and "might have affected his decision to confess." <i>Ante,</i> at 422.<sup>[43]</sup> Thus, a rule requiring the police to inform a suspect of an attorney's call would have two predictable effects. It would serve "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span>'s goal of dispelling the compulsion inherent in custodial interrogation," <i>ante,</i> at 425, and it would disserve the goal of custodial interrogation because it would result in fewer confessions. By a process of balancing these two concerns, the Court finds the benefit to the individual outweighed by the "substantial cost to society's legitimate and substantial interest in securing admissions of guilt." <i>Ante,</i> at 427.</p>
<p>The Court's balancing approach is profoundly misguided. The cost of suppressing evidence of guilt will always make the value of a procedural safeguard appear "minimal," "marginal," or "incremental." Indeed, the value of any trial at all seems like a "procedural technicality" when balanced against the interest in administering prompt justice to a murderer or a rapist caught redhanded. The individual interest in procedural safeguards that minimize the risk of error is easily discounted when the fact of guilt appears certain beyond doubt.</p>
<p>What is the cost of requiring the police to inform a suspect of his attorney's call? It would decrease the likelihood that custodial interrogation will enable the police to obtain a confession. This is certainly a real cost, but it is the same cost that this Court has repeatedly found necessary to preserve <span class="star-pagination">*458</span> the character of our free society and our rejection of an inquisitorial system. Three examples illustrate the point.</p>
<p>In <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), we excluded a confession by a defendant who had not been permitted to consult with his lawyer, and whose lawyer had not been permitted to see him. We emphasized the "lesson of history" that our system of justice is not founded on a fear that a suspect will exercise his rights. "If the exercise of constitutional rights will thwart the effectiveness of a system of law enforcement, then there is something very wrong with that system." <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#490" aria-description="Citation for case: Escobedo v. Illinois"><i>Id.,</i> at 490</a></span>. In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), we similarly stressed this character of our system, despite its "cost," by unequivocally holding that an individual has an absolute right to refuse to respond to police interrogation and to have the assistance of counsel during any questioning.<sup>[44]</sup> Thus, as a matter of law, the assumed right of the police to interrogate a suspect is no right at all; at best, it is a mere privilege terminable at the will of the suspect. And, more recently in <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), the Court corrected the long-held but mistaken view of the police that they have some sort of right to take any suspect <span class="star-pagination">*459</span> into custody for the purpose of questioning him even though they may not have probable cause to arrest.<sup>[45]</sup></p>
<p>Just as the "cost" does not justify taking a suspect into custody or interrogating him without giving him warnings simply because police desire to question him, so too the "cost" does not justify permitting police to withhold from a suspect knowledge of an attorney's communication, even though that communication would have an unquestionable effect on the suspect's exercise of his rights. The "cost" that concerns the Court amounts to nothing more than an acknowledgement that the law enforcement interest in obtaining convictions suffers whenever a suspect exercises the rights that are afforded by our system of criminal justice. In other words, it is the fear that an individual may exercise his rights that tips the scales of justice for the Court today. The principle that ours is an accusatorial, not an inquisitorial, system, however, has repeatedly led the Court to reject that fear as a valid reason for inhibiting the invocation of rights.</p>
<p>If the Court's cost-benefit analysis were sound, it would justify a repudiation of the right to a warning about counsel itself. There is only a difference in degree between a presumption that advice about the immediate availability of a lawyer would not affect the voluntariness of a decision to confess, and a presumption that every citizen knows that he has a right to remain silent and therefore no warnings of any kind are needed. In either case, the withholding of information serves precisely the same law enforcement interests. And in both cases, the cost can be described as nothing more than <span class="star-pagination">*460</span> an incremental increase in the risk that an individual will make an unintelligent waiver of his rights.</p>
<p>In cases like <i>Escobedo, Miranda,</i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> the Court has viewed the balance from a much broader perspective. In all these cases  indeed, whenever the distinction between an inquisitorial and an accusatorial system of justice is implicated  the law enforcement interest served by incommunicado interrogation has been weighed against the interest in individual liberty that is threatened by such practices. The balance has never been struck by an evaluation of empirical data of the kind submitted to legislative decisionmakers  indeed, the Court relies on no such data today. Rather, the Court has evaluated the quality of the conflicting rights and interests. In the past, that kind of balancing process has led to the conclusion that the police have <i>no right</i> to compel an individual to respond to custodial interrogation, and that the interest in liberty that is threatened by incommunicado interrogation is so precious that special procedures must be followed to protect it. The Court's contrary conclusion today can only be explained by its failure to appreciate the value of the liberty that an accusatorial system seeks to protect.</p>
<p></p>
<h2>IV</h2>
<p>The Court also argues that a rule requiring the police to inform a suspect of an attorney's efforts to reach him would have an additional cost: it would undermine the "clarity" of the rule of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case. <i>Ante,</i> at 425-426. This argument is not supported by any reference to the experience in the States that have adopted such a rule. The Court merely professes concern about its ability to answer three quite simple questions.<sup>[46]</sup></p>
<p><span class="star-pagination">*461</span> Moreover, the Court's evaluation of the interest in "clarity" is rather one-sided. For a police officer with a printed card containing the exact text he is supposed to recite, perhaps the rule is clear. But the interest in clarity that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision was intended to serve is not merely for the benefit of the police. Rather, the decision was also, and primarily, intended to provide adequate guidance to the person in custody who is being asked to waive the protections afforded by the Constitution.<sup>[47]</sup> Inevitably, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision also serves the judicial interest in clarifying the inquiry <span class="star-pagination">*462</span> into what actually transpired during a custodial interrogation.<sup>[48]</sup> Under the Court's conception of the interest in clarity, however, the police would presumably prevail whenever they could convince the trier of fact that a required ritual was performed before the confession was obtained.</p>
<p></p>
<h2>V</h2>
<p>At the time attorney Munson made her call to the Cranston police station, she was acting as Burbine's attorney. Under ordinary principles of agency law the deliberate deception of Munson was tantamount to deliberate deception of her client.<sup>[49]</sup> If an attorney makes a mistake in the course of her representation of her client, the client must accept the consequences of that mistake.<sup>[50]</sup> It is equally clear that when an attorney makes an inquiry on behalf of her client, the client is entitled to a truthful answer. Surely the client must have the same remedy for a false representation to his lawyer that he would have if he were acting <i>pro se</i> and had propounded the question himself.</p>
<p>The majority brushes aside the police deception involved in the misinformation of attorney Munson. It is irrelevant to the Fifth Amendment analysis, concludes the majority, because that right is personal; it is irrelevant to the Sixth <span class="star-pagination">*463</span> Amendment analysis, continues the majority, because the Sixth Amendment does not apply until formal adversary proceedings have begun.</p>
<p>In my view, as a matter of law, the police deception of Munson was tantamount to deception of Burbine himself. It constituted a violation of Burbine's right to have an attorney present during the questioning that began shortly thereafter. The existence of that right is undisputed.<sup>[51]</sup> Whether the source of that right is the Sixth Amendment, the Fifth Amendment, or a combination of the two is of no special importance, for I do not understand the Court to deny the existence of the right.</p>
<p>The pertinent question is whether police deception of the attorney is utterly irrelevant to that right. In my judgment, it blinks at reality to suggest that misinformation which prevented the presence of an attorney has no bearing on the protection and effectuation of the right to counsel in custodial interrogation. The majority parses the role of attorney and suspect so narrowly that the deception of the attorney is of no <span class="star-pagination">*464</span> constitutional significance. In other contexts, however, the Court does not hesitate to recognize an identity between the interest of attorney and accused.<sup>[52]</sup> The character of the attorney-client relationship requires rejection of the Court's notion that the attorney is some entirely distinct, completely severable entity and that deception of the attorney is irrelevant to the right of counsel in custodial interrogation.<sup>[53]</sup></p>
<p><span class="star-pagination">*465</span> The possible reach of the Court's opinion is stunning. For the majority seems to suggest that police may deny counsel all access to a client who is being held. At least since <i>Escobedo</i> v. <i>Illinois</i><i>,</i> it has been widely accepted that police may not simply deny attorneys access to their clients who are in custody. This view has survived the recasting of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> from a Sixth Amendment to a Fifth Amendment case that the majority finds so critically important. That this prevailing view is shared <i>by the police</i> can be seen in the state-court opinions detailing various forms of police deception of attorneys.<sup>[54]</sup> For, if there were no obligation to give attorneys access, there would be no need to take elaborate steps to avoid access, such as shuttling the suspect to a different location,<sup>[55]</sup> or taking the lawyer to different locations;<sup>[56]</sup> police could simply refuse to allow the attorneys to see the suspects. But the law enforcement profession has apparently believed, quite rightly in my view, that denying lawyers access to their clients is impermissible. The Court today seems to assume that this view was error  that, from the federal constitutional perspective, the lawyer's access is, as a question from the Court put it in oral argument, merely "a matter of prosecutorial grace." Tr. of Oral Arg. 32. Certainly, nothing in the Court's Fifth and Sixth Amendment analysis acknowledges that there is <i>any</i> federal constitutional bar to an absolute denial of lawyer access to a suspect who is in police custody.</p>
<p>In sharp contrast to the majority, I firmly believe that the right to counsel at custodial interrogation is infringed by police treatment of an attorney that prevents or impedes the attorney's representation of the suspect at that interrogation.</p>
<p></p>
<h2>
<span class="star-pagination">*466</span> VI</h2>
<p>The Court devotes precisely five sentences to its conclusion that the police interference in the attorney's representation of Burbine did not violate the Due Process Clause. In the majority's view, the due process analysis is a simple "shock the conscience" test. Finding its conscience troubled,<sup>[57]</sup> but not shocked, the majority rejects the due process challenge.</p>
<p>In a variety of circumstances, however, the Court has given a more thoughtful consideration to the requirements of due process. For instance, we have concluded that use of a suspect's post-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings silence against him violates the due process requirement of fundamental fairness because such use breaches an implicit promise that "silence will carry no penalty."<sup>[58]</sup> Similarly, we have concluded that "the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment."<sup>[59]</sup> We have also concluded that vindictive prosecution violates due process;<sup>[60]</sup> so too does vindictive sentencing.<sup>[61]</sup> Indeed, we have emphasized that analysis of the "voluntariness" of a confession is frequently a "convenient shorthand" for reviewing objectionable police methods under the rubric of the due process requirement of fundamental fairness.<sup>[62]</sup> What emerges from <span class="star-pagination">*467</span> these cases is not the majority's simple "shock the conscience" test, but the principle that due process requires fairness, integrity, and honor in the operation of the criminal justice system, and in its treatment of the citizen's cardinal constitutional protections.</p>
<p>In my judgment, police interference in the attorney-client relationship is the type of governmental misconduct on a matter of central importance to the administration of justice that the Due Process Clause prohibits. Just as the police cannot impliedly promise a suspect that his silence will not be used against him and then proceed to break that promise, so too police cannot tell a suspect's attorney that they will not question the suspect and then proceed to question him. Just as the government cannot conceal from a suspect material and exculpatory evidence, so too the government cannot conceal from a suspect the material fact of his attorney's communication.</p>
<p><span class="star-pagination">*468</span> Police interference with communications between an attorney and his client violates the due process requirement of fundamental fairness. Burbine's attorney was given completely false information about the lack of questioning; moreover, she was not told that her client would be questioned regarding a murder charge about which she was unaware. Burbine, in turn, was not told that his attorney had phoned and that she had been informed that he would not be questioned. Quite simply, the Rhode Island police effectively drove a wedge between an attorney and a suspect through misinformation and omissions.</p>
<p>The majority does not "question that on facts more egregious than those presented here police deception might rise to a level of a due process violation." <i>Ante,</i> at 432. In my view, the police deception disclosed by this record plainly does rise to that level.</p>
<p></p>
<h2>VII</h2>
<p>This case turns on a proper appraisal of the role of the lawyer in our society. If a lawyer is seen as a nettlesome obstacle to the pursuit of wrongdoers  as in an inquisitorial society  then the Court's decision today makes a good deal of sense. If a lawyer is seen as an aid to the understanding and protection of constitutional rights  as in an accusatorial society  then today's decision makes no sense at all.</p>
<p>Like the conduct of the police in the Cranston station on the evening of June 29, 1977, the Court's opinion today serves the goal of insuring that the perpetrator of a vile crime is punished. Like the police on that June night as well, however, the Court has trampled on well-established legal principles and flouted the spirit of our accusatorial system of justice.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the State of California et al. by <i>John K. Van de Kamp,</i> Attorney General of California, <i>Steve White,</i> Chief Assistant Attorney General, <i>Karl S. Mayer,</i> Assistant Attorney General, and <i>Ann K. Jensen</i> and <i>Dane R. Gillette,</i> Deputy Attorneys General, <i>Charles A. Graddick,</i> Attorney General of Alabama, <i>Norman C. Gorsuch,</i> Attorney General of Alaska, <i>Robert K. Corbin,</i> Attorney General of Arizona, <i>Duane Woodard,</i> Attorney General of Colorado, <i>Austin J. McGuigan,</i> Chief State's Attorney of Connecticut, <i>Charles M. Oberly III,</i> Attorney General of Delaware, <i>Neil F. Hartigan,</i> Attorney General of Illinois, <i>Linley E. Pearson,</i> Attorney General of Indiana, <i>Robert T. Stephan,</i> Attorney General of Kansas, <i>William J. Guste, Jr.,</i> Attorney General of Louisiana, <i>James E. Tierney,</i> Attorney General of Maine, <i>Stephen H. Sachs,</i> Attorney General of Maryland, <i>Stanley D. Steinborn,</i> Attorney General of Michigan, <i>William L. Webster,</i> Attorney General of Missouri, <i>Mike Greeley,</i> Attorney General of Montana, <i>Stephen E. Merrill,</i> Attorney General of New Hampshire, <i>Irwin I. Kimmelman,</i> Attorney General of New Jersey, <i>Lacy H. Thornburg,</i> Attorney General of North Carolina, <i>Nicholas J. Spaeth,</i> Attorney General of North Dakota, <i>Leroy S. Zimmerman,</i> Attorney General of Pennsylvania, <i>Travis Medlock,</i> Attorney General of South Carolina, <i>Mark V. Meierhenry,</i> Attorney General of South Dakota, <i>W. J. Michael Cody,</i> Attorney General of Tennessee, <i>Jim Mattox,</i> Attorney General of Texas, <i>Gerald L. Baliles,</i> Attorney General of Virginia, <i>Jeffrey L. Amestoy,</i> Attorney General of Vermont, <i>Charlie Brown,</i> Attorney General of West Virginia, <i>Bronson C. La Follette,</i> Attorney General of Wisconsin, <i>A. G. McClintock,</i> Attorney General of Wyoming, <i>Richard G. Opper,</i> Attorney General of Guam, <i>J'Ada M. Finch-Sheen,</i> Attorney General of the Virgin Islands, and <i>Jack E. Yelverton;</i> and for Americans for Effective Law Enforcement, Inc., by <i>David Crump, Daniel B. Hales, Fred E. Inbau, Wayne W. Schmidt,</i> and <i>James P. Manak.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the American Bar Association by <i>William W. Falsgraf, Steven H. Goldblatt,</i> and <i>Charles G. Cole;</i> for the National Association of Criminal Defense Lawyers et al. by <i>Judith H. Mizner, Nancy Gertner,</i> and <i>Scott Baldwin;</i> and for the National Legal Aid and Defender Association et al. by <i>Kim R. Fawcett, James R. Neuhard, Jack D. Novik,</i> and <i>John A. MacFadyen.</i></p>
<p>[1]  The dissent incorrectly reads our analysis of the components of a valid waiver to be inconsistent with the Court's holding in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). <i>Post,</i> at 452. When a suspect <i>has</i> requested counsel, the interrogation must cease, regardless of any question of waiver, unless the suspect himself initiates the conversation. In the course of its lengthy exposition, however, the dissent never comes to grips with the crucial distinguishing feature of this case  that Burbine at no point requested the presence of counsel, as was his right under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to do. We do not quarrel with the dissent's characterization of police interrogation as a "privilege terminable at the will of the suspect." <i>Post,</i> at 458. We reject, however, the dissent's entirely undefended suggestion that the Fifth Amendment "right to counsel" requires anything more than that the police inform the suspect of his right to representation and honor his request that the interrogation cease until his attorney is present. See, <i>e. g., </i><i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#104" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 104, n. 10</a></span> (1975).</p>
<p>[2]  Petitioner does not argue that respondent's valid waiver of his Fifth Amendment right to counsel necessarily served to waive his parallel rights under the Sixth Amendment. Accordingly, we have no occasion to consider whether a waiver for one purpose necessarily operates as a general waiver of the right to counsel for all purposes.</p>
<p>[3]  Notwithstanding the Rhode Island Supreme Court's finding that, as a matter of state law, no attorney-client relationship existed between respondent and Ms. Munson, the Sixth Amendment issue is properly before us. <i>State</i> v. <i>Burbine,</i> <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#29" aria-description="Citation for case: State v. Burbine">451 A. 2d 22, 29</a></span> (1982). Petitioner now concedes that such a relationship existed and invites us to decide the Sixth Amendment question based on that concession. Of course, a litigant's concession cannot be used to circumvent the rule that this Court may not disregard a state court's interpretation of state law. Respondent's argument, however, does not focus on whether an attorney-client relationship actually existed as a formal matter of state law. He argues instead that, on the particular facts of this case, the Sixth Amendment right to counsel has been violated. In any event, even if the existence of an attorney-client relationship could somehow independently trigger the Sixth Amendment right to counsel, a position we reject, the type of circumstances that would give rise to the right would certainly have a federal definition.</p>
<p>[4]  Among its other failings, the dissent declines to follow <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), a decision that categorically forecloses JUSTICE STEVENS' major premise  that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires the police to inform a suspect of any and all information that would be useful to a decision whether to remain silent or speak with the police. See also <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span> (1977). The dissent also launches a novel "agency" theory of the Fifth Amendment under which any perceived deception of a lawyer is automatically treated as deception of his or her client. This argument entirely disregards the elemental and established proposition that the privilege against compulsory self-incrimination is, by hypothesis, a personal one that can only be invoked by the individual whose testimony is being compelled.
</p>
<p>Most importantly, the dissent's misreading of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> itself is breathtaking in its scope. For example, it reads <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as creating an undifferentiated right to the presence of an attorney that is triggered automatically by the initiation of the interrogation itself. <i>Post,</i> at 463. Yet, as both <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and subsequent decisions construing <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> make clear beyond refute, " `the interrogation must cease until an attorney is present' <i>only</i> `[i]f the individual states that he wants an attorney.' " <i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#104" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 104, n. 10</a></span> (1975) (emphasis added), quoting <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>. The dissent condemns us for embracing "incommunicado questioning . . . as a societal goal of the highest order that justifies police deception of the shabbiest kind." <i>Post,</i> at 439. We, of course, do nothing of the kind. As any reading of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> reveals, the decision, rather than proceeding from the premise that the rights and needs of the defendant are paramount to all others, embodies a carefully crafted balance designed to fully protect <i>both</i> the defendant's and society's interests. The dissent may not share our view that the Fifth Amendment rights of the defendant are amply protected by application of <i>Miranda as written.</i> But the dissent is "simply wrong," <i>post,</i> at 452, in suggesting that exclusion of Burbine's three confessions follows perfunctorily from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s mandate. Y. Kamisar, Police Interrogation and Confessions 217-218, n. 94 (1980).</p>
<p>Quite understandably, the dissent is outraged by the very idea of police deception of a lawyer. Significantly less understandable is its willingness to misconstrue this Court's constitutional holdings in order to implement its subjective notions of sound policy.</p>
<p>[1]  Justice Frankfurter succinctly explained the character of that distinction in his opinion in <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#54" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 54</a></span> (1949):
</p>
<p>"Ours is the accusatorial as opposed to the inquisitorial system. Such has been the characteristic of Anglo-American criminal justice since it freed itself from practices borrowed by the Star Chamber from the Continent whereby an accused was interrogated in secret for hours on end. See Ploscowe, <i>The Development of Present-Day Criminal Procedures in Europe and America,</i> <span class="citation no-link">48 Harv. L. Rev. 433</span>, 457-458, 467-473 (1935). Under our system society carries the burden of proving its charge against the accused not out of his own mouth. It must establish its case, not by interrogation of the accused even under judicial safeguards, but by evidence independently secured through skillful investigation. `The law will not suffer a prisoner to be made the deluded instrument of his own conviction.' 2 Hawkins, Pleas of the Crown, c. 46, § 34 (8th ed. 1824). The requirement of specific charges, their proof beyond a reasonable doubt, the protection of the accused from confessions extorted through whatever form of police pressures, the right to a prompt hearing before a magistrate, the right to assistance of counsel, to be supplied by government when circumstances make it necessary, the duty to advise an accused of his constitutional rights  these are all characteristics of the accusatorial system and manifestations of its demands. Protracted, systematic and uncontrolled subjection of an accused to interrogation by the police for the purpose of eliciting disclosures or confession is subversive of the accusatorial system."</p>
<p>See generally <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7-8</a></span> (1964); <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 540-541</a></span> (1961); <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#543" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 543-545</a></span> (1897).</p>
<p>[2]  I agree with the majority that, in considering "the type of circumstances" that give rise to constitutional rights in this area, the relationship between an attorney and suspect has "a federal definition." <i>Ante,</i> at 429, n. 3. In my view, for federal constitutional purposes, members of a suspect's family may provide a lawyer with authority to act on a suspect's behalf while the suspect is in custody.</p>
<p>[3]  Tr. of Suppression Hearing 167 (S. H.).</p>
<p>[4]  <i>Id.,</i> at 168.</p>
<p>[5]  "Amid much that is irrelevant or trivial, one serious situation seems to me to stand out in these cases. The suspect neither had nor was advised of his right to get counsel. This presents a real dilemma in a free society. To subject one without counsel to questioning which may and is intended to convict him is a real peril to individual freedom. To bring in a lawyer means a real peril to solution of the crime, because, under our adversary system, he deems that his sole duty is to protect his client  guilty or innocent  and that in such a capacity he owes no duty whatever to help society solve its crime problem. Under this conception of criminal procedure, any lawyer worth his salt will tell the suspect in no uncertain terms to make no statement to police under any circumstances.
</p>
<p>"If the State may arrest on suspicion and interrogate without counsel, there is no denying the fact that it largely negates the benefits of the constitutional guaranty of the right to assistance of counsel. Any lawyer who has ever been called into a case after his client has `told all' and turned any evidence he has over to the Government, knows how helpless he is to protect his client against the facts thus disclosed.</p>
<p>"I suppose the view one takes will turn on what one thinks should be the right of an accused person against the State. Is it his right to have the judgment on the facts? Or is it his right to have a judgment based on only such evidence as he cannot conceal from the authorities, who cannot compel him to testify in court and also cannot question him before? Our system comes close to the latter by any interpretation, for the defendant is shielded by such safeguards as no system of law

[...TRUNCATED 60237 of 180237 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Muehler v. Mena.md  (`case`, 6 assertions)

### content_page

```
---
title: "Muehler v. Mena"
type: case
citation: "544 U.S. 93 (2005)"
parallel_cite: "125 S. Ct. 1465; 161 L. Ed. 2d 299"
neutral_cite: 2005 U.S. LEXIS 2755
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2005
date_decided: 2005-03-22
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2005-03-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Muehler v. Mena
  varies_by_point: false
  scope_note: "Applies Michigan v. Summers detention authority; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/142878/muehler-v-mena/"
  cluster_id: 142878
  opinion_id: 142878
  identity_checked: true
homes:
  - page: "[[Detention and Search of Persons at the Scene]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Securing the Scene]]"
    role: "Related (scene-securing overlap)"
related: ["[[Michigan v. Summers]]", "[[Bailey v. United States]]", "[[Los Angeles County v. Rettele]]"]
aliases: []
tags: ["case", "fourth-amendment", "detention", "search-warrant", "handcuffs"]
holding: "Officers executing a search warrant for weapons at a gang house may detain occupants in handcuffs for the entire duration of the search…"
lake:
  record_id: Muehler v. Mena
  status: verified
  projected_at: 2026-07-09
---

# Muehler v. Mena

*544 U.S. 93 (2005)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers executing a search warrant for weapons and evidence of gang membership at a suspected gang house detained Mena and other occupants in handcuffs in a garage for the two-to-three-hour duration of the search, guarded by officers. During the detention, and with an INS agent present, officers questioned Mena about her immigration status. She sued the officers under § 1983.

## Issue
Whether handcuffing and detaining an occupant for the entire duration of a search-warrant execution was reasonable, and whether officers needed independent reasonable suspicion to ask the detainee about her immigration status.

## Rule
The detention authority is categorical, and incidental questioning needs no separate justification. "An officer's authority to detain incident to a search is categorical; it does not depend on the 'quantum of proof justifying detention or the extent of the intrusion to be imposed by the seizure.'" — 544 U.S. at 98. ^pin-98

Using reasonable force such as handcuffs to effectuate a *[[Michigan v. Summers|Summers]]* detention is permissible where justified by officer-safety and orderly-completion interests. Because mere questioning that does not prolong a detention is not a separate seizure, "the officers did not need reasonable suspicion to ask Mena for her name, date and place of birth, or immigration status." — [*Id.* at 101](https://www.courtlistener.com/opinion/142878/muehler-v-mena/#:~:text=the%20officers%20did%20not%20need). ^pin-101

## Application
Mena's detention in handcuffs for the duration of the search was permissible under *[[Michigan v. Summers]]* because the warrant authorized a search for weapons and evidence of a violent gang — circumstances posing special dangers that justified both the detention and the use of handcuffs. The questioning about her immigration status required no separate reasonable suspicion because it did not extend the time she was already lawfully detained.

## Conclusion
The detention and the questioning were reasonable under the Fourth Amendment; the Ninth Circuit's judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Mena* applies and extends [[Michigan v. Summers]]' categorical authority to detain occupants during a warranted search, confirming that reasonable force and incidental questioning fall within it.

## Appears on
- [[Securing the Scene]] — *Key — Progeny / Refinement*

## Sources
- *Muehler v. Mena*, 544 U.S. 93 (2005) — https://www.courtlistener.com/opinion/142878/muehler-v-mena/ — pinpoints: 98, 101.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f687cf8d3adfa0a5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "544 U.S. 93 (2005)", "court": "U.S. Supreme Court", "neutral_cite": "2005 U.S. LEXIS 2755", "official_citation_present": true, "parallel_cite": "125 S. Ct. 1465; 161 L. Ed. 2d 299", "title": "Muehler v. Mena", "year": "2005"}}
{"assertion_id": "3c6fa88636bb21b2", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Related (scene-securing overlap)", "title": "Muehler v. Mena"}}
{"assertion_id": "58e535d30ba16dc6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Officers executing a search warrant for weapons at a gang house may detain occupants in handcuffs for the entire duration of the search…", "title": "Muehler v. Mena"}}
{"assertion_id": "80b3119f5dff7f4e", "dimension": "support", "kind": "home_role", "locator": {"home": "Detention and Search of Persons at the Scene"}, "payload": {"home": "Detention and Search of Persons at the Scene", "role": "Key — Progeny / Refinement", "title": "Muehler v. Mena"}}
{"assertion_id": "442c2724fdafee8e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2005-03-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Muehler v. Mena", "field_i_validity": "good_law", "scope_note": "Applies Michigan v. Summers detention authority; good law.", "title": "Muehler v. Mena", "varies_by_point": "false"}}
{"assertion_id": "98fbef74a08826ed", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Muehler v. Mena"}}
```

### lake record — Muehler v. Mena

```json
{
  "schema_version": "s2.v1",
  "record_id": "Muehler v. Mena",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Muehler v. Mena",
    "case_name_short": "Muehler",
    "case_name_full": "MUEHLER Et Al. v. MENA",
    "input_case_name": "Muehler v. Mena",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2005-03-22",
    "year": 2005,
    "docket": null,
    "cluster_id": 142878,
    "lead_opinion_id": 142878,
    "sibling_ids": [
      142878,
      9434759,
      9434760,
      9434761
    ],
    "absolute_url": "/opinion/142878/muehler-v-mena/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "544 U.S. 93",
      "volume": "544",
      "reporter": "U.S.",
      "page": "93",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "125 S. Ct. 1465",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "1465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "161 L. Ed. 2d 299",
        "volume": "161",
        "reporter": "L. Ed. 2d",
        "page": "299",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2005 U.S. LEXIS 2755",
        "volume": "2005",
        "reporter": "U.S. LEXIS",
        "page": "2755",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "544 U.S. 93",
        "volume": "544",
        "reporter": "U.S.",
        "page": "93",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 S. Ct. 1465",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "1465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "161 L. Ed. 2d 299",
        "volume": "161",
        "reporter": "L. Ed. 2d",
        "page": "299",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 U.S. LEXIS 2755",
        "volume": "2005",
        "reporter": "U.S. LEXIS",
        "page": "2755",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "544 U.S. 93",
    "official_selection": {
      "court_class": "scotus",
      "selected": "544 U.S. 93",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-98",
      "page": null,
      "quote": "--- # Muehler v. Mena *544 U.S. 93 (2005)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers executing a search warrant for weapons and evidence of gang membership at a suspected gang house detained Mena and other occupants in handcuffs in a garage for the two-to-three-hour duration of the search, guarded by officers. During the detention, and with an INS agent present, officers questioned Mena about her immigration status. She sued the officers under \u00a7 1983. ## Issue Whether handcuffing and detaining an occupant for the entire duration of a search-warrant execution was reasonable, and whether officers needed independent reasonable suspicion to ask the detainee about her immigration status. ## Rule The detention authority is categorical, and incidental questioning needs no separate justification.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-101",
      "page": null,
      "quote": "the officers did not need reasonable suspicion to ask Mena for her name, date and place of birth, or immigration status.",
      "star_marker": "101",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17404,
      "fragment": "#:~:text=the%20officers%20did%20not%20need",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2005-03-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Muehler v. Mena",
    "varies_by_point": false,
    "scope_note": "Applies Michigan v. Summers detention authority; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane1_negative"
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
        "journal_ref": "Muehler v. Mena:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Phyllis J. May v. City of Nahunta, Georgia",
          "cluster_id": 4339893,
          "cite": [
            "846 F.3d 1320",
            "2017 WL 218838",
            "2017 U.S. App. LEXIS 985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bernard West v. United States",
          "cluster_id": 2735560,
          "cite": [
            "100 A.3d 1076",
            "2014 D.C. App. LEXIS 382",
            "2014 WL 4636023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane1_negative"
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
        "journal_ref": "Muehler v. Mena:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kareen Rasul Griffin",
          "cluster_id": 809546,
          "cite": [
            "696 F.3d 1354",
            "2012 WL 4496817",
            "2012 U.S. App. LEXIS 20543"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jenkins",
          "cluster_id": 2444991,
          "cite": [
            "3 A.3d 806",
            "298 Conn. 209",
            "2010 Conn. LEXIS 304"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane1_negative"
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
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. United States",
          "cluster_id": 803270,
          "cite": [
            "183 L. Ed. 2d 351",
            "132 S. Ct. 2492",
            "567 U.S. 387",
            "2012 U.S. LEXIS 4872",
            "80 U.S.L.W. 4539",
            "23 Fla. L. Weekly Fed. S 437",
            "2012 WL 2368661",
            "95 Empl. Prac. Dec. (CCH) 44,539",
            "115 Fair Empl. Prac. Cas. (BNA) 353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
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
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez-Barragan",
          "cluster_id": 4260741,
          "cite": [
            "2016 CO 66",
            "379 P.3d 330",
            "2016 WL 5375502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
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
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Bennett v. City of Eastpointe",
          "cluster_id": 790530,
          "cite": [
            "410 F.3d 810",
            "2005 U.S. App. LEXIS 10587",
            "2005 WL 1384366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
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
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Binay v. Bettendorf",
          "cluster_id": 2092,
          "cite": [
            "601 F.3d 640",
            "2010 U.S. App. LEXIS 8084",
            "2010 WL 1541295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amy Corbitt v. Michael Vickers",
          "cluster_id": 4638184,
          "cite": [
            "929 F.3d 1304"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A.M. Ex Rel. F.M. v. Holmes",
          "cluster_id": 4241340,
          "cite": [
            "830 F.3d 1123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Russell Marcilis, II v. Township of Redford",
          "cluster_id": 807964,
          "cite": [
            "693 F.3d 589",
            "2012 WL 3854793",
            "2012 U.S. App. LEXIS 18707"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Randall Lee Pals",
          "cluster_id": 4472392,
          "cite": [
            "805 N.W.2d 767",
            "2011 Iowa Sup. LEXIS 87"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Los Angeles County, California v. Rettele",
          "cluster_id": 145728,
          "cite": [
            "167 L. Ed. 2d 974",
            "127 S. Ct. 1989",
            "550 U.S. 609",
            "2007 U.S. LEXIS 5900",
            "75 U.S.L.W. 3619",
            "20 Fla. L. Weekly Fed. S 281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bew",
          "cluster_id": 2231907,
          "cite": [
            "886 N.E.2d 1002",
            "228 Ill. 2d 122",
            "319 Ill. Dec. 878",
            "2008 Ill. LEXIS 291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
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
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cosby",
          "cluster_id": 2105166,
          "cite": [
            "898 N.E.2d 603",
            "231 Ill. 2d 262",
            "325 Ill. Dec. 556",
            "2008 Ill. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leyva",
          "cluster_id": 891705,
          "cite": [
            "2011 NMSC 9",
            "250 P.3d 861",
            "149 N.M. 435",
            "2011 NMSC 009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bletz v. Gribble",
          "cluster_id": 217605,
          "cite": [
            "641 F.3d 743",
            "2011 U.S. App. LEXIS 10683",
            "2011 WL 2080332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santos",
          "cluster_id": 165698,
          "cite": [
            "403 F.3d 1120",
            "2005 U.S. App. LEXIS 5444",
            "2005 WL 768771"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reyes Fabian Olivera-Mendez",
          "cluster_id": 797553,
          "cite": [
            "484 F.3d 505",
            "2007 U.S. App. LEXIS 10492",
            "2007 WL 1296781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Basher",
          "cluster_id": 183144,
          "cite": [
            "629 F.3d 1161",
            "2011 U.S. App. LEXIS 1064",
            "2011 WL 167045"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alcaraz-Arellano",
          "cluster_id": 167269,
          "cite": [
            "441 F.3d 1252",
            "2006 U.S. App. LEXIS 7797",
            "2006 WL 805323"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Muehler v. Mena:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(142878 OR 9434759 OR 9434760 OR 9434761) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgzODE3NjAwMDAwJnM9MjQ0NDk5MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28142878+OR+9434759+OR+9434760+OR+9434761%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(142878 OR 9434759 OR 9434760 OR 9434761)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDEmcz0xMzcyNzcxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28142878+OR+9434759+OR+9434760+OR+9434761%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(142878 OR 9434759 OR 9434760 OR 9434761)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 0,
        "triage_snippet_classified": 18
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(142878 OR 9434759 OR 9434760 OR 9434761)",
    "indexed_citing_opinions": 519,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 142878,
        "count": 458,
        "count_source": "search"
      },
      {
        "opinion_id": 9434759,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9434760,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434761,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 938,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/muehler-v-mena.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5NjM3Njgmcz05MzY3NzA0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28142878+OR+9434759+OR+9434760+OR+9434761%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 142878,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 112725,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 118263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 122252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 137742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 770457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 782383,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 142878,
        "cited_id": 2018459,
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
    "date_created": "2026-07-05T14:43:30Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:43:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:43:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:46:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:43:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Muehler v. Mena

```
<div>
<center><b><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">544 U.S. 93</a></span> (2005)</b></center>
<center><h1>MUEHLER ET AL.<br>
v.<br>
MENA.</h1></center>
<center>No. 03-1423.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 8, 2004.</center>
<center>Decided March 22, 2005.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*94</span> REHNQUIST, C. J., delivered the opinion of the Court, in which O'CONNOR, SCALIA, KENNEDY, and THOMAS, JJ., joined. KENNEDY, J., filed a concurring opinion, <i>post,</i> p. 102. STEVENS, J., filed an opinion concurring in the judgment, in which SOUTER, GINSBURG, and BREYER, JJ., joined, <i>post,</i> p. 104.</p>
<p><i>Carter G. Phillips</i> argued the cause for petitioners. With him on the briefs were <i>Joseph R. Guerra</i> and <i>David H. Hirsch.</i></p>
<p><i>Kannon K. Shanmugam</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Acting Solicitor General Clement, Assistant Attorney General Wray,</i> and <i>Deputy Solicitor General Dreeben.</i></p>
<p><i>Paul L. Hoffman</i> argued the cause for respondent. With him on the brief were <i>Benjamin Schonbrun, Michael S. Morrison,</i> and <i>Erwin Chemerinsky.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*95</span> CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Respondent Iris Mena was detained in handcuffs during a search of the premises that she and several others occupied. Petitioners were lead members of a police detachment executing a search warrant of these premises. She sued the officers under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, and the District Court found in her favor. The Court of Appeals affirmed the judgment, holding that the use of handcuffs to detain Mena during the search violated the Fourth Amendment and that the officers' questioning of Mena about her immigration status during the detention constituted an independent Fourth Amendment violation. <i>Mena</i> v. <i>Simi Valley,</i> <span class="citation multiple-matches"><a href="/c/F.3d/332/1255/">332 F.3d 1255</a></span> (CA9 2003). We hold that Mena's detention in handcuffs for the length of the search was consistent with our opinion in <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U.S. 692</a></span> (1981), and that the officers' questioning during that detention did not violate her Fourth Amendment rights.</p>
<p></p>
<h2>* * *</h2>
<p>Based on information gleaned from the investigation of a gang-related, driveby shooting, petitioners Muehler and Brill had reason to believe at least one member of a gang  the West Side Locos  lived at 1363 Patricia Avenue. They also suspected that the individual was armed and dangerous, since he had recently been involved in the driveby shooting. As a result, Muehler obtained a search warrant for 1363 Patricia Avenue that authorized a broad search of the house and premises for, among other things, deadly weapons and <span class="star-pagination">*96</span> evidence of gang membership. In light of the high degree of risk involved in searching a house suspected of housing at least one, and perhaps multiple, armed gang members, a Special Weapons and Tactics (SWAT) team was used to secure the residence and grounds before the search.</p>
<p>At 7 a.m. on February 3, 1998, petitioners, along with the SWAT team and other officers, executed the warrant. Mena was asleep in her bed when the SWAT team, clad in helmets and black vests adorned with badges and the word "POLICE," entered her bedroom and placed her in handcuffs at gunpoint. The SWAT team also handcuffed three other individuals found on the property. The SWAT team then took those individuals and Mena into a converted garage, which contained several beds and some other bedroom furniture. While the search proceeded, one or two officers guarded the four detainees, who were allowed to move around the garage but remained in handcuffs.</p>
<p>Aware that the West Side Locos gang was composed primarily of illegal immigrants, the officers had notified the Immigration and Naturalization Service (INS) that they would be conducting the search, and an INS officer accompanied the officers executing the warrant. During their detention in the garage, an officer asked for each detainee's name, date of birth, place of birth, and immigration status. The INS officer later asked the detainees for their immigration documentation. Mena's status as a permanent resident was confirmed by her papers.</p>
<p>The search of the premises yielded a .22 caliber handgun with .22 caliber ammunition, a box of .25 caliber ammunition, several baseball bats with gang writing, various additional gang paraphernalia, and a bag of marijuana. Before the officers left the area, Mena was released.</p>
<p>In her § 1983 suit against the officers she alleged that she was detained "for an unreasonable time and in an unreasonable manner" in violation of the Fourth Amendment. App. <span class="star-pagination">*97</span> 19. In addition, she claimed that the warrant and its execution were overbroad, that the officers failed to comply with the "knock and announce" rule, and that the officers had needlessly destroyed property during the search. The officers moved for summary judgment, asserting that they were entitled to qualified immunity, but the District Court denied their motion. The Court of Appeals affirmed that denial, <i>except</i> for Mena's claim that the warrant was overbroad; on this claim the Court of Appeals held that the officers were entitled to qualified immunity. <i>Mena</i> v. <i>Simi Valley,</i> <span class="citation multiple-matches"><a href="/c/F.%203d/226/1031/">226 F. 3d 1031</a></span> (CA9 2000). After a trial, a jury, pursuant to a special verdict form, found that Officers Muehler and Brill violated Mena's Fourth Amendment right to be free from unreasonable seizures by detaining her both with force greater than that which was reasonable and for a longer period than that which was reasonable. The jury awarded Mena $10,000 in actual damages and $20,000 in punitive damages against each petitioner for a total of $60,000.</p>
<p>The Court of Appeals affirmed the judgment on two grounds. <span class="citation multiple-matches"><a href="/c/F.%203d/332/1255/">332 F. 3d 1255</a></span> (CA9 2003). Reviewing the denial of qualified immunity <i>de novo, id.,</i> at 1261, n. 2, it first held that the officers' detention of Mena violated the Fourth Amendment because it was objectively unreasonable to confine her in the converted garage and keep her in handcuffs during the search, <i>id.,</i> at 1263-1264. In the Court of Appeals' view, the officers should have released Mena as soon as it became clear that she posed no immediate threat. <i>Id.,</i> at 1263. The court additionally held that the questioning of Mena about her immigration status constituted an independent Fourth Amendment violation. <i>Id.,</i> at 1264-1266. The Court of Appeals went on to hold that those rights were clearly established at the time of Mena's questioning, and thus the officers were not entitled to qualified immunity. <i>Id.,</i> at 1266-1267. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.S./542/903/">542 U.S. 903</a></span> (2004), and now vacate and remand.</p>
<p></p>
<h2>
<span class="star-pagination">*98</span> * * *</h2>
<p>In <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U.S. 692</a></span> (1981), we held that officers executing a search warrant for contraband have the authority "to detain the occupants of the premises while a proper search is conducted." <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#705" aria-description="Citation for case: Michigan v. Summers"><i>Id.,</i> at 705</a></span>. Such detentions are appropriate, we explained, because the character of the additional intrusion caused by detention is slight and because the justifications for detention are substantial. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#701" aria-description="Citation for case: Michigan v. Summers"><i>Id.,</i> at 701-705</a></span>. We made clear that the detention of an occupant is "surely less intrusive than the search itself," and the presence of a warrant assures that a neutral magistrate has determined that probable cause exists to search the home. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#701" aria-description="Citation for case: Michigan v. Summers"><i>Id.,</i> at 701</a></span>. Against this incremental intrusion, we posited three legitimate law enforcement interests that provide substantial justification for detaining an occupant: "preventing flight in the event that incriminating evidence is found"; "minimizing the risk of harm to the officers"; and facilitating "the orderly completion of the search," as detainees' "self-interest may induce them to open locked doors or locked containers to avoid the use of force." <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><i>Id.,</i> at 702-703</a></span>.</p>
<p>Mena's detention was, under <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>,</i> plainly permissible.<sup>[1]</sup> An officer's authority to detain incident to a search is categorical; it does not depend on the "quantum of proof justifying detention or the extent of the intrusion to be imposed by the seizure." <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#705" aria-description="Citation for case: Michigan v. Summers"><i>Id.,</i> at 705, n. 19</a></span>. Thus, Mena's detention for the duration of the search was reasonable under <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> because a warrant existed to search 1363 Patricia Avenue and she was an occupant of that address at the time of the search.</p>
<p>Inherent in <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i>' authorization to detain an occupant of the place to be searched is the authority to use reasonable <span class="star-pagination">*99</span> force to effectuate the detention. See <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U.S. 386, 396</a></span> (1989) ("Fourth Amendment jurisprudence has long recognized that the right to make an arrest or investigatory stop necessarily carries with it the right to use some degree of physical coercion or threat thereof to effect it"). Indeed, <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> itself stressed that the risk of harm to officers and occupants is minimized "if the officers routinely exercise unquestioned command of the situation." <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers">452 U.S., at 703</a></span>.</p>
<p>The officers' use of force in the form of handcuffs to effectuate Mena's detention in the garage, as well as the detention of the three other occupants, was reasonable because the governmental interests outweigh the marginal intrusion. See <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor"><i>Graham, supra,</i> at 396-397</a></span>. The imposition of correctly applied handcuffs on Mena, who was already being lawfully detained during a search of the house, was undoubtedly a separate intrusion in addition to detention in the converted garage.<sup>[2]</sup> The detention was thus more intrusive than that which we upheld in <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>.</i> See <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#701" aria-description="Citation for case: Michigan v. Summers">452 U.S., at 701-702</a></span> (concluding that the additional intrusion in the form of a detention was less than that of the warrant-sanctioned search); <i>Maryland</i> v. <i>Wilson,</i> <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#413" aria-description="Citation for case: Maryland v. Wilson">519 U.S. 408, 413-414</a></span> (1997) (concluding <span class="star-pagination">*100</span> that the additional intrusion from ordering passengers out of a car, which was already stopped, was minimal).</p>
<p>But this was no ordinary search. The governmental interests in not only detaining, but using handcuffs, are at their maximum when, as here, a warrant authorizes a search for weapons and a wanted gang member resides on the premises. In such inherently dangerous situations, the use of handcuffs minimizes the risk of harm to both officers and occupants. Cf. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><i>Summers, supra,</i> at 702-703</a></span> (recognizing the execution of a warrant to search for drugs "may give rise to sudden violence or frantic efforts to conceal or destroy evidence"). Though this safety risk inherent in executing a search warrant for weapons was sufficient to justify the use of handcuffs, the need to detain multiple occupants made the use of handcuffs all the more reasonable. Cf. <i>Maryland</i> v. <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson"><i>Wilson, supra,</i> at 414</a></span> (noting that "danger to an officer from a traffic stop is likely to be greater when there are passengers in addition to the driver in the stopped car").</p>
<p>Mena argues that, even if the use of handcuffs to detain her in the garage was reasonable as an initial matter, the duration of the use of handcuffs made the detention unreasonable. The duration of a detention can, of course, affect the balance of interests under <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>.</i> However, the 2- to 3-hour detention in handcuffs in this case does not outweigh the government's continuing safety interests. As we have noted, this case involved the detention of four detainees by two officers during a search of a gang house for dangerous weapons. We conclude that the detention of Mena in handcuffs during the search was reasonable.</p>
<p>The Court of Appeals also determined that the officers violated Mena's Fourth Amendment rights by questioning her about her immigration status during the detention. 332 F.3d, at 1264-1266. This holding, it appears, was premised on the assumption that the officers were required to have independent reasonable suspicion in order to question Mena concerning her immigration status because the questioning <span class="star-pagination">*101</span> constituted a discrete Fourth Amendment event. But the premise is faulty. We have "held repeatedly that mere police questioning does not constitute a seizure." <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#434" aria-description="Citation for case: Florida v. Bostick">501 U.S. 429, 434</a></span> (1991); see also <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#212" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U.S. 210, 212</a></span> (1984). "[E]ven when officers have no basis for suspecting a particular individual, they may generally ask questions of that individual; ask to examine the individual's identification; and request consent to search his or her luggage." <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#434" aria-description="Citation for case: Florida v. Bostick"><i>Bostick, supra,</i> at 434-435</a></span> (citations omitted). As the Court of Appeals did not hold that the detention was prolonged by the questioning, there was no additional seizure within the meaning of the Fourth Amendment. Hence, the officers did not need reasonable suspicion to ask Mena for her name, date and place of birth, or immigration status.</p>
<p>Our recent opinion in <i>Illinois</i> v. <i>Caballes,</i> <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405</a></span> (2005), is instructive. There, we held that a dog sniff performed during a traffic stop does not violate the Fourth Amendment. We noted that a lawful seizure "can become unlawful if it is prolonged beyond the time reasonably required to complete that mission," but accepted the state court's determination that the duration of the stop was not extended by the dog sniff. <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#407" aria-description="Citation for case: Illinois v. Caballes"><i>Id.,</i> at 407</a></span>. Because we held that a dog sniff was not a search subject to the Fourth Amendment, we rejected the notion that "the shift in purpose" "from a lawful traffic stop into a drug investigation" was unlawful because it "was not supported by any reasonable suspicion." <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#408" aria-description="Citation for case: Illinois v. Caballes"><i>Id.,</i> at 408</a></span>. Likewise here, the initial <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> detention was lawful; the Court of Appeals did not find that the questioning extended the time Mena was detained. Thus no additional Fourth Amendment justification for inquiring about Mena's immigration status was required.<sup>[3]</sup></p>
<p><span class="star-pagination">*102</span> In summary, the officers' detention of Mena in handcuffs during the execution of the search warrant was reasonable and did not violate the Fourth Amendment. Additionally, the officers' questioning of Mena did not constitute an independent Fourth Amendment violation. Mena has advanced in this Court, as she did before the Court of Appeals, an alternative argument for affirming the judgment below. She asserts that her detention extended beyond the time the police completed the tasks incident to the search. Because the Court of Appeals did not address this contention, we too decline to address it. See <i>Pierce County</i> v. <i>Guillen,</i> <span class="citation" data-id="122252"><a href="/opinion/122252/pierce-county-v-guillen/#148" aria-description="Citation for case: Pierce County v. Guillen">537 U.S. 129, 148, n. 10</a></span> (2003); <i>National Collegiate Athletic Assn.</i> v. <i>Smith,</i> <span class="citation" data-id="118263"><a href="/opinion/118263/national-collegiate-athletic-assn-v-smith/#469" aria-description="Citation for case: National Collegiate Athletic Assn. v. Smith">525 U.S. 459, 469-470</a></span> (1999).</p>
<p>The judgment of the Court of Appeals is therefore vacated, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE KENNEDY, concurring.</p>
<p>I concur in the judgment and in the opinion of the Court. It does seem important to add this brief statement to help ensure that police handcuffing during searches becomes neither routine nor unduly prolonged.</p>
<p>The safety of the officers and the efficacy of the search are matters of first concern, but so too is it a matter of first concern that excessive force is not used on the persons detained, especially when these persons, though lawfully detained under <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U.S. 692</a></span> (1981), are not themselves suspected of any involvement in criminal <span class="star-pagination">*103</span> activity. The use of handcuffs is the use of force, and such force must be objectively reasonable under the circumstances, <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span> (1989).</p>
<p>The reasonableness calculation under <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> is in part a function of the expected and actual duration of the search. If the search extends to the point when the handcuffs can cause real pain or serious discomfort, provision must be made to alter the conditions of detention at least long enough to attend to the needs of the detainee. This is so even if there is no question that the initial handcuffing was objectively reasonable. The restraint should also be removed if, at any point during the search, it would be readily apparent to any objectively reasonable officer that removing the handcuffs would not compromise the officers' safety or risk interference or substantial delay in the execution of the search. The time spent in the search here, some two to three hours, certainly approaches, and may well exceed, the time beyond which a detainee's Fourth Amendment interests require revisiting the necessity of handcuffing in order to ensure the restraint, even if permissible as an initial matter, has not become excessive.</p>
<p>That said, under these circumstances I do not think handcuffing the detainees for the duration of the search was objectively unreasonable. As I understand the record, during much of this search 2 armed officers were available to watch over the 4 unarmed detainees, while the other 16 officers on the scene conducted an extensive search of a suspected gang safe house. Even if we accept as true  as we must  the factual assertions that these detainees posed no readily apparent danger and that keeping them handcuffed deviated from standard police procedure, it does not follow that the handcuffs were unreasonable. Where the detainees outnumber those supervising them, and this situation could not be remedied without diverting officers from an extensive, complex, and time-consuming search, the continued use of handcuffs after the initial sweep may be justified, subject to <span class="star-pagination">*104</span> adjustments or temporary release under supervision to avoid pain or excessive physical discomfort. Because on this record it does not appear the restraints were excessive, I join the opinion of the Court.</p>
<p>JUSTICE STEVENS, with whom JUSTICE SOUTER, JUSTICE GINSBURG, and JUSTICE BREYER join, concurring in the judgment.</p>
<p>The jury in this case found that the two petitioners violated Iris Mena's Fourth Amendment right to be free from unreasonable seizure by detaining her with greater force and for a longer period of time than was reasonable under the circumstances. In their post-trial motion in the District Court, petitioners advanced three legal arguments: (1) They were entitled to qualified immunity because the unconstitutionality of their conduct was not clearly established;<sup>[1]</sup> (2) the judge's instruction to the jury was erroneous;<sup>[2]</sup> and (3) the evidence was not sufficient to support the jury's award of <span class="star-pagination">*105</span> punitive damages. The trial judge's thoughtful explanation of his reasons for denying the motion does not address either of the issues the Court discusses today.</p>
<p>In its opinion affirming the judgment, the Court of Appeals made two mistakes. First, as the Court explains, <i>ante,</i> at 100-101, it erroneously held that the immigration officers' questioning of Mena about her immigration status was an independent violation of the Fourth Amendment.<sup>[3]</sup> Second, instead of merely deciding whether there was sufficient evidence in the record to support the jury's verdict, the Court of Appeals appears to have ruled as a matter of law that the officers should have released her from the handcuffs sooner than they did. I agree that it is appropriate to remand the case to enable the Court of Appeals to consider whether the evidence supports Mena's contention that she was held longer than the search actually lasted. In doing so, the Court of Appeals must of course accord appropriate deference to the jury's reasonable factual findings, while applying the correct legal standard. See <i>Ornelas</i> v. <i>United States,</i> <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#699" aria-description="Citation for case: Ornelas v. United States">517 U.S. 690, 699</a></span> (1996).</p>
<p>In my judgment, however, the Court's discussion of the amount of force used to detain Mena pursuant to <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U.S. 692</a></span> (1981), is analytically unsound. Although the Court correctly purports to apply the "objective reasonableness" test announced in <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span> (1989), it misapplies that test. Given the facts of this case  and the presumption that a reviewing court must draw all reasonable inferences in favor of supporting the verdict  I think it clear that the jury could properly have found that this 5-foot-2-inch young lady posed no threat to the officers at the scene, and that they used excessive force in keeping her in handcuffs for up to three hours. Although <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> authorizes the detention of any individual <span class="star-pagination">*106</span> who is present when a valid search warrant is being executed, that case does not give officers <i>carte blanche</i> to keep individuals who pose no threat in handcuffs throughout a search, no matter how long it may last. On remand, I would therefore instruct the Court of Appeals to consider whether the evidence supports Mena's contention that the petitioners used excessive force in detaining her when it considers the length of the <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> detention.</p>
<p></p>
<h2>I</h2>
<p>As the Court notes, the warrant in this case authorized the police to enter the Mena home to search for a gun belonging to Raymond Romero that may have been used in a gang, related driveby shooting. Romero, a known member of the West Side Locos gang, rented a room from the Mena family. The house, described as a "`poor house,'" was home to several unrelated individuals who rented from the Menas. Brief for Petitioners 4. Each resident had his or her own bedroom, which could be locked with a padlock on the outside, and each had access to the living room and kitchen. In addition, several individuals lived in trailers in the back yard and also had access to the common spaces in the Mena home. <i>Id.,</i> at 5.</p>
<p>In addition to Romero, police had reason to believe that at least one other West Side Locos gang member had lived at the residence, although Romero's brother told police that the individual had returned to Mexico. The officers in charge of the search, petitioners Muehler and Brill, had been at the same residence a few months earlier on an unrelated domestic violence call, but did not see any other individuals they believed to be gang members inside the home on that occasion.</p>
<p>In light of the fact that the police believed that Romero possessed a gun and that there might be other gang members at the residence, petitioner Muehler decided to use a Special Weapons and Tactics (SWAT) team to execute the <span class="star-pagination">*107</span> warrant. As described in the majority opinion, eight members of the SWAT team forcefully entered the home at 7 a.m. In fact, Mena was the only occupant of the house, and she was asleep in her bedroom. The police woke her up at gunpoint, and immediately handcuffed her. At the same time, officers served another search warrant at the home of Romero's mother, where Romero was known to stay several nights each week. In part because Romero's mother had previously cooperated with police officers, they did not use a SWAT team to serve that warrant. Romero was found at his mother's house; after being cited for possession of a small amount of marijuana, he was released.</p>
<p>Meanwhile, after the SWAT team secured the Mena residence and gave the "all clear," police officers transferred Mena and three other individuals (who had been in trailers in the back yard) to a converted garage.<sup>[4]</sup> To get to the garage, Mena, who was still in her bedclothes, was forced to walk barefoot through the pouring rain. The officers kept her and the other three individuals in the garage for up to three hours while they searched the home. Although she requested them to remove the handcuffs, they refused to do so. For the duration of the search, two officers guarded Mena and the other three detainees. A .22-caliber handgun, ammunition, and gang-related paraphernalia were found in Romero's bedroom, and other gang-related paraphernalia was found in the living room. Officers found nothing of significance in Mena's bedroom.<sup>[5]</sup><i>Id.,</i> at 6-9.</p>
<p></p>
<h2>
<span class="star-pagination">*108</span> II</h2>
<p>In analyzing the quantum of force used to effectuate the <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> detention, the Court rightly employs the "objective reasonableness" test of <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>.</i> Under <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>,</i> the trier of fact must balance "`the nature and quality of the intrusion on the individual's Fourth Amendment interests' against the countervailing governmental interests at stake." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U.S., at 396</a></span>. The District Court correctly instructed the jury to take into consideration such factors as "`the severity of the suspected crime, whether the person being detained is the subject of the investigation, whether such person poses an immediate threat to the security of the police or others or to the ability of the police to conduct the search, and whether such person is actively resisting arrest or attempting to flee.'" See n. 2, <i>supra.</i> The District Court also correctly instructed the jury to consider whether the detention was prolonged and whether Mena was detained in handcuffs after the search had ended. <i>Ibid.</i> Many of these factors are taken from <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> itself, and the jury instruction reflects an entirely reasonable construction of the objective reasonableness test in the <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> context.</p>
<p>Considering those factors, it is clear that the SWAT team's initial actions were reasonable. When officers undertake a dangerous assignment to execute a warrant to search property that is presumably occupied by violence-prone gang members, it may well be appropriate to use both overwhelming force and surprise in order to secure the premises as promptly as possible. In this case the decision to use a SWAT team of eight heavily armed officers and to execute the warrant at 7 a.m. gave the officers maximum protection against the anticipated risk. As it turned out, there was only one person in the house  Mena  and she was sound asleep. Nevertheless, "[t]he `reasonableness' of a particular <span class="star-pagination">*109</span> use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight." <i>Graham,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U.S., at 396</a></span>. At the time they first encountered Mena, the officers had no way of knowing her relation to Romero, whether she was affiliated with the West Side Locos, or whether she had any weapons on her person. Further, the officers needed to use overwhelming force to immediately take command of the situation; by handcuffing Mena they could more quickly secure her room and join the other officers. It would be unreasonable to expect officers, who are entering what they believe to be a high risk situation, to spend the time necessary to determine whether Mena was a threat before they handcuffed her. To the extent that the Court of Appeals relied on the initial actions of the SWAT team to find that there was sufficient evidence to support the jury's verdict, it was in error.</p>
<p>Whether the well-founded fears that justified the extraordinary entry into the house should also justify a prolonged interruption of the morning routine of a presumptively innocent person, however, is a separate question and one that depends on the specific facts of the case. This is true with respect both to how the handcuffs were used, and to the totality of the circumstances surrounding the detention, including whether Mena was detained in handcuffs after the search had concluded. With regard to the handcuffs, police may use them in different ways.<sup>[6]</sup> Here, the cuffs kept Mena's arms behind her for two to three hours. She testified that they were "`real uncomfortable'" and that she had asked the officers to remove them, but that they had refused. App. 105. Moreover, she was continuously guarded by two <span class="star-pagination">*110</span> police officers who obviously made flight virtually impossible even if the cuffs had been removed.</p>
<p>A jury could reasonably have found a number of facts supporting a conclusion that the prolonged handcuffing was unreasonable. No contraband was found in Mena's room or on her person. There were no indications suggesting she was or ever had been a gang member, which was consistent with the fact that during the police officers' last visit to the home, no gang members were present. She fully cooperated with the officers and the INS agent, answering all their questions. She was unarmed, and given her small size, was clearly no match for either of the two armed officers who were guarding her. In sum, there was no evidence that Mena posed any threat to the officers or anyone else.</p>
<p>The justifications offered by the officers are not persuasive. They have argued that at least six armed officers were required to guard the four detainees, even though all of them had been searched for weapons. Since there were 18 officers at the scene, and since at least 1 officer who at one point guarded Mena and the other three residents was sent home after offering to assist in the search, it seems unlikely that lack of resources was really a problem. While a court should not ordinarily question the allocation of police officers or resources, a jury could have reasonably found that this is a case where ample resources were available.</p>
<p>The jury may also have been skeptical of testimony that the officers in fact feared for their safety given that the actual suspect of the shooting had been found at the other location and promptly released. Additionally, while the officers testified that as a general matter they would not release an individual from handcuffs while searching a residence, the SWAT team's tactical plan for this particular search arguably called for them to do just that, since it directed that "[a]ny subjects encountered will be handcuffed and detained until they can be patted down, their location noted, [field identified], <span class="star-pagination">*111</span> and released by Officer Muehler or Officer R. Brill." 2 Record 53. The tactical plan suggests that they can, and often do, release individuals who are not related to the search. The SWAT team leader testified that handcuffs are not always required when executing a search.</p>
<p>In short, under the factors listed in <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> and those validly presented to the jury in the jury instructions, a jury could have reasonably found from the evidence that there was no apparent need to handcuff Mena for the entire duration of the search and that she was detained for an unreasonably prolonged period. She posed no threat whatsoever to the officers at the scene. She was not suspected of any crime and was not a person targeted by the search warrant. She had no reason to flee the scene and gave no indication that she desired to do so. Viewing the facts in the light most favorable to the jury's verdict, as we are required to do, there is certainly no obvious factual basis for rejecting the jury's verdict that the officers acted unreasonably, and no obvious basis for rejecting the conclusion that, on these facts, the quantum of force used was unreasonable as a matter of law.</p>
<p></p>
<h2>III</h2>
<p>Police officers' legitimate concern for their own safety is always a factor that should weigh heavily in balancing the relevant <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> factors. But, as Officer Brill admitted at trial, if that justification were always sufficient, it would authorize the handcuffing of every occupant of the premises for the duration of every <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> detention. Nothing in either the <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> or the <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> opinion provides any support for such a result. Rather, the decision of what force to use must be made on a case-by-case basis. There is evidence in this record that may well support the conclusion that it was unreasonable to handcuff Mena throughout the search. On remand, therefore, I would instruct the Ninth Circuit to consider that evidence, as well as the possibility <span class="star-pagination">*112</span> that Mena was detained after the search was completed, when deciding whether the evidence in the record is sufficient to support the jury's verdict.</p>
<h2>NOTES</h2>
<p>[*]   <i>Richard Ruda</i> and <i>James I. Crowley</i> filed a brief for the National League of Cities et al. as <i>amici curiae</i> urging reversal.
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the American Civil Liberties Union et al. by <i>Mark D. Rosenbaum, Ahilan T. Arulanantham,</i> <i>Steven R. Shapiro, Lucas Guttentag,</i> and <i>Lee Gelernt;</i> and for the National Association of Criminal Defense Lawyers by <i>Henk Brands</i> and <i>Pamela Harris.</i></p>
<p>Briefs of <i>amici curiae</i> were filed for the National Latino Officers Association et al. by <i>Baher Azmy, Lawrence S. Lustberg,</i> and <i>Jonathan L. Hafetz;</i> and for the Police Officers Research Association of California Legal Defense Fund et al. by <i>Michael J. Hansen.</i></p>
<p>[1]  In determining whether a Fourth Amendment violation occurred we draw all reasonable factual inferences in favor of the jury verdict, but as we made clear in <i>Ornelas</i> v. <i>United States,</i> <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#697" aria-description="Citation for case: Ornelas v. United States">517 U.S. 690, 697-699</a></span> (1996), we do not defer to the jury's legal conclusion that those facts violate the Constitution.</p>
<p>[2]  In finding the officers should have released Mena from the handcuffs, the Court of Appeals improperly relied upon the fact that the warrant did not include Mena as a suspect. See <i>Mena</i> v. <i>Simi Valley,</i> <span class="citation multiple-matches"><a href="/c/F.3d/332/1255/">332 F.3d 1255</a></span>, 1263, n. 5 (CA9 2003). The warrant was concerned not with individuals but with locations and property. In particular, the warrant in this case authorized the search of 1363 Patricia Avenue and its surrounding grounds for, among other things, deadly weapons and evidence of street gang membership. In this respect, the warrant here resembles that at issue in <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U.S. 692</a></span> (1981), which allowed the search of a residence for drugs without mentioning any individual, including the owner of the home whom police ultimately arrested. See <i>People</i> v. <i>Summers,</i> <span class="citation" data-id="2018459"><a href="/opinion/2018459/people-v-summers/#440" aria-description="Citation for case: People v. Summers">407 Mich. 432, 440-443</a></span>, <span class="citation" data-id="2018459"><a href="/opinion/2018459/people-v-summers/#226" aria-description="Citation for case: People v. Summers">286 N.W.2d 226, 226-227</a></span> (1979), rev'd, <i>Michigan</i> v. <i>Summers, supra</i><i>. Summers</i> makes clear that when a neutral magistrate has determined police have probable cause to believe contraband exists, "[t]he connection of an occupant to [a] home" alone "justifies a detention of that occupant." <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers">452 U.S., at 703-704</a></span>.</p>
<p>[3]  The Court of Appeals' reliance on <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U.S. 873</a></span> (1975), is misplaced. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> held that stops by roving patrols near the border "may be justified on facts that do not amount to the probable cause require[ment] for an arrest." <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Id.,</i> at 880</a></span>. We considered only whether the patrols had the "authority to <i>stop</i> automobiles in areas near the Mexican border," <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#874" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>id.,</i> at 874</a></span> (emphasis added), and expressed no opinion as to the appropriateness of questioning when an individual was already seized. See <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543, 556-562</a></span> (1976). We certainly did not, as the Court of Appeals suggested, create a "requirement of particularized reasonable suspicion for purposes of inquiry into citizenship status." 332 F.3d, at 1267.</p>
<p>[1]  The Court of Appeals' conclusion that the officers were not entitled to qualified immunity was not challenged in the petition for certiorari and is therefore waived. See <i>Taylor</i> v. <i>Freeland &amp; Kronz,</i> <span class="citation" data-id="9432520"><a href="/opinion/112725/taylor-v-freeland-kronz/#645" aria-description="Citation for case: Taylor v. Freeland &amp; Kronz">503 U.S. 638, 645-646</a></span> (1992).</p>
<p>[2]  The trial judge instructed the jury as follows:
</p>
<p>"`Generally, a police officer carrying out a search authorized by a warrant may detain occupants of the residence during the search, so long as the detention is reasonable.</p>
<p>"`In determining the reasonableness of a detention conducted in connection with a search, you may look to all the circumstances, including the severity of the suspected crime, whether the person being detained is the subject of the investigation, whether such person poses an immediate threat to the security of the police or others or to the ability of the police to conduct the search, and whether such person is actively resisting arrest or attempting to flee. A detention may be unreasonable if it is unnecessarily painful, degrading, prolonged or if it involves an undue invasion of privacy. A police officer is required to release an individual detained in connection with a lawful search as soon as the officers' right to conduct the search ends or the search itself is concluded, whichever is sooner.'" <i>Mena</i> v. <i>Simi Valley,</i> <span class="citation multiple-matches"><a href="/c/F.3d/332/1255/">332 F.3d 1255</a></span>, 1267-1268 (CA9 2003) (alterations omitted; one paragraph break added).</p>
<p>[3]  While I agree with the Court's discussion of this issue, I note that the issue was not properly presented to the Ninth Circuit because it was not raised by either petitioners or respondent.</p>
<p>[4]  The other individuals were a 55-year-old Latina female, a 40-year-old Latino male who was removed from the scene by the Immigration and Naturalization Service (INS), and a white male who appears to be in his early 30's and who was cited for possession of a small amount of marijuana.</p>
<p>[5]  One of the justifications for our decision in <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U.S. 692</a></span> (1981), was the fact that the occupants may be willing to "open locked doors or locked containers to avoid the use of force that is not only damaging to property but may also delay the completion of the task at hand." <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers"><i>Id.,</i> at 703</a></span>. Mena, however, was never asked to assist the officers, although she testified that she was willing to do so. See 3 Tr. 42 (June 14, 2001). Instead, officers broke the locks on several cabinets and dressers to which Mena possessed the keys.</p>
<p>[6]  For instance, a suspect may be handcuffed to a fixed object, to a custodian, or her hands may simply be linked to one another. The cuffs may join the wrists either in the front or the back of the torso. They can be so tight that they are painful, particularly when applied for prolonged periods. While they restrict movement, they do not necessarily preclude flight if the prisoner is not kept under constant surveillance.</p>

</div>
```

---
