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

## GROUP: content/cases/National Treasury Employees Union v. Von Raab.md  (`case`, 5 assertions)

### content_page

```
---
title: "National Treasury Employees Union v. Von Raab"
type: case
citation: "489 U.S. 656 (1989)"
parallel_cite: "109 S. Ct. 1384; 103 L. Ed. 2d 685; 1989 CCH OSHD 28,589; 4 I.E.R. Cas. (BNA) 246; 57 U.S.L.W. 4338; 49 Empl. Prac. Dec. (CCH) 38,792"
neutral_cite: 1989 U.S. LEXIS 6033
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
  composite_basis_ref: National Treasury Employees Union v. Von Raab
  varies_by_point: false
  scope_note: "Special-needs suspicionless-testing precedent; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112220/national-treasury-employees-union-v-von-raab/"
  cluster_id: 112220
  opinion_id: 9431609
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Skinner v. Railway Labor Executives' Association]]", "[[New Jersey v. T.L.O.]]", "[[Vernonia School District 47J v. Acton]]", "[[Chandler v. Miller]]"]
aliases: ["Von Raab", "NTEU v. Von Raab"]
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "administrative-search"]
holding: "Suspicionless drug testing of Customs employees seeking drug-interdiction or firearm-carrying positions is reasonable under the…"
lake:
  record_id: National Treasury Employees Union v. Von Raab
  status: verified
  projected_at: 2026-07-09
---

# National Treasury Employees Union v. Von Raab

*489 U.S. 656 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The U.S. Customs Service adopted a drug-screening program requiring urinalysis for employees seeking transfer or promotion to positions involving drug interdiction, the carrying of firearms, or the handling of classified material. The employees' union challenged the suspicionless testing under the Fourth Amendment.

## Issue
Whether suspicionless drug testing of Customs employees who seek such positions is a reasonable search under the Fourth Amendment.

## Rule
Where a search serves a special governmental need beyond ordinary law enforcement, reasonableness is determined by balancing, and a warrant or individualized suspicion may be unnecessary: "where a Fourth Amendment intrusion serves special governmental needs, beyond the normal need for law enforcement, it is necessary to balance the individual's privacy expectations against the Government's interests to determine whether it is impractical to require a warrant or some level of individualized suspicion in the particular context." — 489 U.S. at 665–66. ^pin-665

Employees in such sensitive roles have a reduced privacy interest: "Customs employees who are directly involved in the interdiction of illegal drugs or who are required to carry firearms in the line of duty likewise have a diminished expectation of privacy in respect to the intrusions occasioned by a urine test." — [*Id.* at 672](https://www.courtlistener.com/opinion/112220/national-treasury-employees-union-v-von-raab/#:~:text=Customs%20employees%20who%20are%20directly). ^pin-672

## Application
The Customs program was not designed to serve ordinary law enforcement, and its results could not be used in a criminal prosecution without the employee's consent. Balancing the Government's compelling interest in the integrity of the borders and in keeping firearms out of the hands of drug users against the diminished privacy of employees who seek those specific positions, the testing of applicants for drug-interdiction and firearm-carrying positions was reasonable. The Court [[Reading and Citing Cases#on-remand|remanded]] as to the classified-materials category for clarification of which positions it actually covered.

## Conclusion
Suspicionless testing of applicants for drug-interdiction and firearms positions was upheld as reasonable; the case was [[Reading and Citing Cases#on-remand|remanded]] for further consideration of the classified-materials category.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. Decided with [[Skinner v. Railway Labor Executives' Association]], *Von Raab* is a leading special-needs precedent later applied in the school-testing context ([[Vernonia School District 47J v. Acton]]) and distinguished where the asserted need was not substantial ([[Chandler v. Miller]]).

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *National Treasury Employees Union v. Von Raab*, 489 U.S. 656 (1989) — https://www.courtlistener.com/opinion/112220/national-treasury-employees-union-v-von-raab/ — pinpoints: 665–66, 672.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3b9c47c09fe1d265", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "489 U.S. 656 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1989 U.S. LEXIS 6033", "official_citation_present": true, "parallel_cite": "109 S. Ct. 1384; 103 L. Ed. 2d 685; 1989 CCH OSHD 28,589; 4 I.E.R. Cas. (BNA) 246; 57 U.S.L.W. 4338; 49 Empl. Prac. Dec. (CCH) 38,792", "title": "National Treasury Employees Union v. Von Raab", "year": "1989"}}
{"assertion_id": "1106cd0cdcb84a3b", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "National Treasury Employees Union v. Von Raab"}}
{"assertion_id": "70ce840026dcae0f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Suspicionless drug testing of Customs employees seeking drug-interdiction or firearm-carrying positions is reasonable under the…", "title": "National Treasury Employees Union v. Von Raab"}}
{"assertion_id": "d6d7d970ffe1e22f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1989-03-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "National Treasury Employees Union v. Von Raab", "field_i_validity": "good_law", "scope_note": "Special-needs suspicionless-testing precedent; good law.", "title": "National Treasury Employees Union v. Von Raab", "varies_by_point": "false"}}
{"assertion_id": "ec4c5b8cee98118e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "National Treasury Employees Union v. Von Raab"}}
```

### lake record — National Treasury Employees Union v. Von Raab

```json
{
  "schema_version": "s2.v1",
  "record_id": "National Treasury Employees Union v. Von Raab",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "National Treasury Employees Union v. Von Raab",
    "case_name_short": "Von Raab",
    "case_name_full": "NATIONAL TREASURY EMPLOYEES UNION Et Al. v. VON RAAB, COMMISSIONER, UNITED STATES CUSTOMS SERVICE",
    "input_case_name": "National Treasury Employees Union v. Von Raab",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-03-21",
    "year": 1989,
    "docket": null,
    "cluster_id": 112220,
    "lead_opinion_id": 9431609,
    "sibling_ids": [
      112220,
      9431609,
      9431610,
      9431611
    ],
    "absolute_url": "/opinion/112220/national-treasury-employees-union-v-von-raab/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "489 U.S. 656",
      "volume": "489",
      "reporter": "U.S.",
      "page": "656",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1384",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1384",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 685",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "685",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 CCH OSHD 28,589",
        "volume": "1989",
        "reporter": "CCH OSHD",
        "page": "28,589",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 I.E.R. Cas. (BNA) 246",
        "volume": "4",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "246",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4338",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4338",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Empl. Prac. Dec. (CCH) 38,792",
        "volume": "49",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "38,792",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 6033",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "6033",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "489 U.S. 656",
        "volume": "489",
        "reporter": "U.S.",
        "page": "656",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1384",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1384",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 685",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "685",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 6033",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "6033",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 CCH OSHD 28,589",
        "volume": "1989",
        "reporter": "CCH OSHD",
        "page": "28,589",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 I.E.R. Cas. (BNA) 246",
        "volume": "4",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "246",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4338",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4338",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Empl. Prac. Dec. (CCH) 38,792",
        "volume": "49",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "38,792",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "489 U.S. 656",
    "official_selection": {
      "court_class": "scotus",
      "selected": "489 U.S. 656",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-665",
      "page": null,
      "quote": "--- # National Treasury Employees Union v. Von Raab *489 U.S. 656 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The U.S. Customs Service adopted a drug-screening program requiring urinalysis for employees seeking transfer or promotion to positions involving drug interdiction, the carrying of firearms, or the handling of classified material. The employees' union challenged the suspicionless testing under the Fourth Amendment. ## Issue Whether suspicionless drug testing of Customs employees who seek such positions is a reasonable search under the Fourth Amendment. ## Rule Where a search serves a special governmental need beyond ordinary law enforcement, reasonableness is determined by balancing, and a warrant or individualized suspicion may be unnecessary:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-672",
      "page": null,
      "quote": "Customs employees who are directly involved in the interdiction of illegal drugs or who are required to carry firearms in the line of duty likewise have a diminished expectation of privacy in respect to the intrusions occasioned by a urine test.",
      "star_marker": "672",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 31893,
      "fragment": "#:~:text=Customs%20employees%20who%20are%20directly",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "National Treasury Employees Union v. Von Raab",
    "varies_by_point": false,
    "scope_note": "Special-needs suspicionless-testing precedent; good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4381539,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Landgraf v. USI Film Products",
          "cluster_id": 117841,
          "cite": [
            "128 L. Ed. 2d 229",
            "114 S. Ct. 1483",
            "511 U.S. 244",
            "1994 U.S. LEXIS 3292"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmelin v. Michigan",
          "cluster_id": 112646,
          "cite": [
            "115 L. Ed. 2d 836",
            "111 S. Ct. 2680",
            "501 U.S. 957",
            "1991 U.S. LEXIS 3816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yates v. People",
          "cluster_id": 4675566,
          "cite": [
            "2019 CO 90"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Employment Div., Dept. of Human Resources of Ore. v. Smith",
          "cluster_id": 112404,
          "cite": [
            "108 L. Ed. 2d 876",
            "110 S. Ct. 1595",
            "494 U.S. 872",
            "1990 U.S. LEXIS 2021",
            "58 U.S.L.W. 4433",
            "53 Empl. Prac. Dec. (CCH) 39,826",
            "52 Fair Empl. Prac. Cas. (BNA) 855"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaiser Aluminum & Chemical Corp. v. Bonjorno",
          "cluster_id": 112403,
          "cite": [
            "108 L. Ed. 2d 842",
            "110 S. Ct. 1570",
            "494 U.S. 827",
            "1990 U.S. LEXIS 2024"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chandler v. Miller",
          "cluster_id": 118100,
          "cite": [
            "137 L. Ed. 2d 513",
            "117 S. Ct. 1295",
            "520 U.S. 305",
            "1997 U.S. LEXIS 2505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 118414,
          "cite": [
            "149 L. Ed. 2d 205",
            "121 S. Ct. 1281",
            "532 U.S. 67",
            "2001 U.S. LEXIS 2460",
            "2001 Daily Journal DAR 2839",
            "2001 Colo. J. C.A.R. 1427",
            "14 Fla. L. Weekly Fed. S 152",
            "69 U.S.L.W. 4184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
          "cluster_id": 121171,
          "cite": [
            "153 L. Ed. 2d 735",
            "122 S. Ct. 2559",
            "536 U.S. 822",
            "2002 U.S. LEXIS 4882",
            "2002 Cal. Daily Op. Serv. 5761",
            "2002 Daily Journal DAR 7275",
            "70 U.S.L.W. 4737",
            "15 Fla. L. Weekly Fed. S 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stein v. Davidson Hotel Co.",
          "cluster_id": 1060994,
          "cite": [
            "945 S.W.2d 714",
            "12 I.E.R. Cas. (BNA) 1636",
            "1997 Tenn. LEXIS 283",
            "1997 WL 257138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Reyes",
          "cluster_id": 1444172,
          "cite": [
            "968 P.2d 445",
            "80 Cal. Rptr. 2d 734",
            "19 Cal. 4th 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bevill v. State",
          "cluster_id": 1149417,
          "cite": [
            "556 So. 2d 699",
            "1990 WL 7305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112220 OR 9431609 OR 9431610 OR 9431611) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDczNjA2NDAwMDAwJnM9Mjk5NjgwNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112220+OR+9431609+OR+9431610+OR+9431611%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(112220 OR 9431609 OR 9431610 OR 9431611)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMmcz0yNjg3NTU4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112220+OR+9431609+OR+9431610+OR+9431611%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112220 OR 9431609 OR 9431610 OR 9431611)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 0,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112220 OR 9431609 OR 9431610 OR 9431611)",
    "indexed_citing_opinions": 760,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112220,
        "count": 703,
        "count_source": "search"
      },
      {
        "opinion_id": 9431609,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9431610,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431611,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1190,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/national-treasury-employees-union-v-von-raab.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc1NTUxODkmcz01MzExNzM2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112220+OR+9431609+OR+9431610+OR+9431611%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112220,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 107554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 107814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 312772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 312834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 319945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 328554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 486563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 504461,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 1631759,
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
    "date_created": "2026-07-05T15:04:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:05:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:05:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:09:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:05:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — National Treasury Employees Union v. Von Raab

```
<opinion type="majority">
<author id="b731-10">Justice Kennedy</author>
<p id="AURm">delivered the opinion of the Court.</p>
<p id="b731-11">We granted certiorari to decide whether it violates the Fourth Amendment for the United States Customs Service to require a urinalysis test from employees who seek transfer or promotion to certain positions.</p>
<p id="AEk">I</p>
<p id="b731-3">A</p>
<p id="b731-4">The United States Customs Service, a bureau of the Department of the Treasury, is the federal agency responsible for processing persons, carriers, cargo, and mail into the United States, collecting revenue from imports, and enforcing customs and related laws. See United States Customs Service, Customs U. S. A., Fiscal Year 1985, p. 4. An important responsibility of the Service is the interdiction and <page-number citation-index="1" label="660">*660</page-number>seizure of contraband, including illegal drugs. <em>Ibid. </em>In 1987 alone, Customs agents seized drugs with a retail value of nearly $9 billion. See United States Customs Service, Customs U. S. A., Fiscal Year 1987, p. 40. In the routine discharge of their duties, many Customs employees have direct contact with those who traffic in drugs for profit. Drug import operations, often directed by sophisticated criminal syndicates, <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#561" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 561-562</a></span> (1980) (Powell, J., concurring), may be effected by violence or its threat. As a necessary response, many Customs operatives carry and use firearms in connection with their official duties. App. 109.</p>
<p id="b732-5">In December 1985, respondent, the Commissioner of Customs, established a Drug Screening Task Force to explore the possibility of implementing a drug-screening program within the Service. <em>Id., </em>at 11. After extensive research and consultation with experts in the field, the task force concluded that “drug screening through urinalysis is technologically reliable, valid and accurate.” <em>Ibid. </em>Citing this conclusion, the Commissioner announced his intention to require drug tests of employees who applied for, or occupied, certain positions within the Service. <em>Id., </em>at 10-11. The Commissioner stated his belief that “Customs is largely drug-free,” but noted also that “unfortunately no segment of society is immune from the threat of illegal drug use.” <em>Id., </em>at 10. Drug interdiction has become the agency’s primary enforcement mission, and the Commissioner stressed that “there is no room in the Customs Service for those who break the laws prohibiting the possession and use of illegal drugs.” <em>Ibid.</em></p>
<p id="b732-6">In May 1986, the Commissioner announced implementation of the drug-testing program. Drug tests were made a condition of placement or employment for positions that meet one or more of three criteria. The first is direct involvement in drug interdiction or enforcement of related laws, an activity the Commissioner deemed fraught with obvious dangers to the mission of the agency and the lives of Customs <page-number citation-index="1" label="661">*661</page-number>agents. <em>Id., </em>at 17, 113. The second criterion is a requirement that the incumbent carry firearms, as the Commissioner concluded that “[pjublic safety demands that employees who carry deadly arms and are prepared to make instant life or death decisions be drug free.” <em>Id., </em>at 113. The third criterion is a requirement for the incumbent to handle “classified” material, which the Commissioner determined might fall into the hands of smugglers if accessible to employees who, by reason of their own illegal drug use, are susceptible to bribery or blackmail. <em>Id., </em>at 114.</p>
<p id="b733-5">After an employee qualifies for a position covered by the Customs testing program, the Service advises him by letter that his final selection is contingent upon successful completion of drug screening. An independent contractor contacts the employee to fix the time and place for collecting the sample. On reporting for the test, the employee must produce photographic identification and remove any outer garments, such as a coat or a jacket, and personal belongings. The employee may produce the sample behind a partition, or in the privacy of a bathroom stall if he so chooses. To ensure against adulteration of the specimen, or substitution of a sample from another person, a monitor of the same sex as the employee remains close at hand to listen for the normal sounds of urination. Dye is added to the toilet water to prevent the employee from using the water to adulterate the sample.</p>
<p id="b733-6">Upon receiving the specimen, the monitor inspects it to ensure its proper temperature and color, places a tamper-proof custody seal over the container, and affixes an identification label indicating the date and the individual’s specimen number. The employee signs a chain-of-custody form, which is initialed by the monitor, and the urine sample is placed in a plastic bag, sealed, and submitted to a laboratory.<footnotemark>1</footnotemark></p>
<p id="b734-4"><page-number citation-index="1" label="662">*662</page-number>The laboratory tests the sample for the presence of marijuana, cocaine, opiates, amphetamines, and phencyclidine. Two tests are used. An initial screening test uses the enzyme-multiplied-immunoassay technique (EMIT). Any specimen that is identified as positive on this initial test must then be confirmed using gas chromatography/mass spectrometry (GC/MS). Confirmed positive results are reported to a “Medical Review Officer,” “[a] licensed physician. . . who has knowledge of substance abuse disorders and has appropriate medical training to interpret and evaluate an individual’s positive test result together with his or her medical history and any other relevant biomedical information.” HHS Reg. § 1.2, <page-number citation-index="1" label="663">*663</page-number><span class="citation no-link">53 Fed. Reg. 11980</span> (1988); HHS Reg. §2.4(g), 53 Fed. Reg., at 11983. 'After verifying the positive result, the Medical Review Officer transmits it to the agency.</p>
<p id="b735-5">Customs employees.who test positive for drugs and who can offer no satisfactory explanation are subject to dismissal from the Service. Test results may not, however, be turned over to any other agency, including criminal prosecutors, without the employee’s written consent.</p>
<p id="b735-6">B</p>
<p id="b735-7">Petitioners, a union of federal employees and a union official, commenced this suit in the United States District Court for the Eastern District of Louisiana on behalf of current Customs Service employees who seek covered positions. Petitioners alleged that the Custom Service drug-testing program violated, <em>inter alia, </em>the Fourth Amendment. The District Court agreed. <span class="citation" data-id="1631759"><a href="/opinion/1631759/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">649 F. Supp. 380</a></span> (1986). The court acknowledged “the legitimate governmental interest in a drug-free work place and work force,” but concluded that “the drug testing plan constitutes an overly intrusive policy of searches and seizures without probable cause or reasonable suspicion, in violation of legitimate expectations of privacy.” <span class="citation" data-id="1631759"><a href="/opinion/1631759/national-treasury-employees-union-v-von-raab/#387" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Id., </em>at 387</a></span>. The court enjoined the drug-testing program, and ordered the Customs Service not to require drug tests of any applicants for covered positions.</p>
<p id="b735-8">A divided panel of the United States Court of Appeals for the Fifth Circuit vacated the injunction. <span class="citation multiple-matches"><a href="/c/F.%202d/816/170/">816 F. 2d 170</a></span> (1987). The court agreed with petitioners that the drug-screening program, by requiring an employee to produce a urine sample for chemical testing, effects a search within the meaning of the Fourth Amendment. The court held further that the searches required by the Commissioner’s directive are reasonable under the Fourth Amendment. It first noted that “[t]he Service has attempted to minimize the intrusiveness of the search” by not requiring visual observation of the act of urination and by affording notice to the employee that <page-number citation-index="1" label="664">*664</page-number>he will be tested. <em>Id., </em>at 177. The court also considered it significant that the program limits discretion in determining which employees are to be tested, <em>ibid., </em>and noted that the tests are an aspect of the employment relationship, <em>id., </em>at 178.</p>
<p id="b736-5">The court further found that the Government has a strong interest in detecting drug use among employees who meet the criteria of the Customs program. It reasoned that drug use by covered employees casts substantial doubt on their ability to discharge their duties honestly and vigorously, undermining public confidence in the integrity of the Service and concomitantly impairing the Service’s efforts to enforce the drug laws. <em>Ibid. </em>Illicit drug users, the court found, are susceptible to bribery and blackmail, may be tempted to divert for their own use portions of any drug shipments they interdict, and may, if required to carry firearms, “endanger the safety of their fellow agents, as well as their own, when their performance is impaired by drug use.” <em>Ibid. </em>“Considering the nature and responsibilities of the jobs for which applicants are being considered at Customs and the limited scope of the search,” the court stated, “the exaction of consent as a condition of assignment to the new job is not unreasonable.” <em>Id., </em>at 179.</p>
<p id="b736-6">The dissenting judge concluded that the Customs program is not an effective method for achieving the Service’s goals. He argued principally that an employee “given a five day notification of a test date need only abstain from drug use to prevent being identified as a user.” <em>Id., </em>at 184. He noted also that persons already employed in sensitive positions are not subject to the test. <em>Ibid. </em>Because he did not believe the Customs program can achieve its purposes, the dissenting judge found it unreasonable under the Fourth Amendment.</p>
<p id="b736-7">We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./485/903/">485 U. S. 903</a></span> (1988). We now affirm so much of the judgment of the Court of Appeals as upheld the testing of employees directly involved in drug interdiction or required to carry firearms. We vacate the <page-number citation-index="1" label="665">*665</page-number>judgment to the extent it upheld the testing of applicants for positions requiring the incumbent to handle classified materials, and remand for further proceedings. II</p>
<p id="b737-7">hH</p>
<p id="b737-3">In <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., ante, </em>at 616-618, decided today, we held that federal regulations requiring employees of private railroads to produce urine samples for chemical testing implicate the Fourth Amendment, as those tests invade reasonable expectations of privacy. Our earlier cases have settled that the Fourth Amendment protects individuals from unreasonable searches conducted by the Government, even when the Government acts as an employer, <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 717</a></span> (1987) (plurality opinion); see <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#731" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 731</a></span> (Scalia, J., concurring in judgment), and, in view of our holding in <em>Railway Labor Executives </em>that urine tests are searches, it follows that the Customs Service’s drug-testing program must meet the reasonableness requirement of the Fourth Amendment.</p>
<p id="b737-4">While we have often emphasized, and reiterate today, that a search must be supported, as a general matter, by a warrant issued upon probable cause, see, <em>e. g., Griffin </em>v. <em>Wisconsin, </em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987); <em>United States </em>v. <em>Karo, </em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#717" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 717</a></span> (1984), our decision in <em>Railway Labor Executives </em>reaffirms the longstanding principle that neither a <em>warrant nor probable cause, nor, indeed, any measure of </em>individualized suspicion, is an indispensable component of reasonableness in every circumstance. <em>Ante, </em>at 618-624. See also <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 342, n. 8</a></span> (1985); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 556-661</a></span> (1976). As we note in <em>Railway Labor Executives, </em>our cases establish that where a Fourth Amendment intrusion serves special governmental needs, beyond the normal need for law enforcement, it is necessary to balance the individual’s privacy expectations against the Government’s interests to determine whether it is impractical to require a warrant or <page-number citation-index="1" label="666">*666</page-number>some level of individualized suspicion in the particular context. <em>Ante, </em>at 619-620.</p>
<p id="b738-5">It is clear that the Customs Service’s drug-testing program is not designed to serve the ordinary needs of law enforcement. Test results may not be used in a criminal prosecution of the employee without the employee’s consent. The purposes of the program are to deter drug use among those eligible for promotion to sensitive positions within the Service and to prevent the promotion of drug users to those positions. These substantial interests, no less than the Government’s concern for safe rail transportation at issue in <em>Railway Labor Executives, </em>present a special need that may justify departure from the ordinary warrant and probable-cause requirements.</p>
<p id="b738-6">A</p>
<p id="b738-7">Petitioners do not contend that a warrant is required by the balance of privacy and governmental interests in this context, nor could any such contention withstand scrutiny. We have recognized before that requiring the Government to procure a warrant for every work-related intrusion “would conflict with ‘the common-sense realization that government offices could not function if every employment decision became a constitutional matter.’” <em>O’Connor </em>v. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#722" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Ortega, supra, </em>at 722</a></span>, quoting <em>Connick </em>v. <em>Myers, </em><span class="citation" data-id="9429164"><a href="/opinion/110917/connick-ex-rel-parish-of-orleans-v-myers/#143" aria-description="Citation for case: Connick Ex Rel. Parish of Orleans v. Myers">461 U. S. 138, 143</a></span> (1983). See also <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S., at 732</a></span> (Scalia, J., concurring in judgment); <em>New Jersey </em>v. <em>T. L. O., supra, </em>at 340 (noting that “[t]he warrant requirement ... is unsuited to the school environment: requiring a teacher to obtain a warrant before searching a child suspected of an infraction of school rules (or of the criminal law) would unduly interfere with the maintenance of the swift and informal disciplinary procedures needed in the schools”). Even if Customs Service employees are more likely to be familiar with the procedures required to obtain a warrant than most other Government workers, requiring a warrant in this context would serve only to divert valuable agency resources from the Service’s primary mis<page-number citation-index="1" label="667">*667</page-number>sion. The Customs Service has been entrusted with pressing responsibilities, and its mission would be compromised if it were required to seek search warrants in connection with routine, yet sensitive, employment decisions.</p>
<p id="b739-5">Furthermore, a warrant would provide little or nothing in the way of additional protection of personal privacy. A warrant serves primarily to advise the citizen that an intrusion is authorized by law and limited in its permissible scope and to interpose a neutral magistrate between the citizen and the law enforcement officer “engaged in the often competitive enterprise of ferreting out crime.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). But in the present context, “the circumstances justifying toxicological testing and the permissible limits of such intrusions are defined narrowly and specifically . . . , and doubtless are well known to covered employees.” <em>Ante, </em>at 622. Under the Customs program, every employee who seeks a transfer to a covered position knows that he must take a drug test, and is likewise aware of the procedures the Service must follow in administering the test. A covered employee is simply not subject “to the discretion of the official in the field.” <em>Camara </em>v. <em>Municipal Court of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 532</a></span> (1967). The process becomes automatic when the employee elects to apply for, and thereafter pursue, a covered position. Because the Service does not make a discretionary determination to search based on a judgment that certain conditions are present, there are simply “no special facts for a neutral magistrate to evaluate.” <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#383" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 383</a></span> (1976) (Powell, J., concurring).</p>
<p id="b739-6">B</p>
<p id="b739-7">Even where it is reasonable to dispense with the warrant requirement in the particular circumstances, a search ordinarily must be based on probable cause. <em>Ante, </em>at 624. Our cases teach, however, that the probable-cause standard “ ‘is peculiarly related to criminal investigations.’” <em>Colorado </em>v. <em>Bertine, </em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#371" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 371</a></span> (1987), quoting <em>South Dakota </em>v. <page-number citation-index="1" label="668">*668</page-number><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#370" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 370, n. 5</a></span>. In particular, the traditional probable-cause standard may be unhelpful in analyzing the reasonableness of routine administrative functions, <em>Colorado </em>v. <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#371" aria-description="Citation for case: Colorado v. Bertine"><em>Bertine, supra, </em>at 371</a></span>; see also <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#723" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S., at 723</a></span>, especially where the Government seeks to <em>prevent </em>the development of hazardous conditions or to detect violations that rarely generate articulable grounds for searching any particular place or person. Cf. <em>Camara </em>v. <em>Municipal Court of San Francisco, supra, </em>at 535-536 (noting that building code inspections, unlike searches conducted pursuant to a criminal investigation, are designed “to prevent even the unintentional development of conditions which are hazardous to public health and safety”); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 557</a></span> (noting that requiring particularized suspicion before routine stops on major highways near the Mexican border “would be impractical because the flow of traffic tends to be too heavy to allow the particularized study of a given car that would enable it to be identified as a possible carrier of illegal aliens”). Our precedents have settled that, in certain limited circumstances, the Government’s need to discover such latent or hidden conditions, or to prevent their development, is sufficiently compelling to justify the intrusion on privacy entailed by conducting such searches without any measure of individualized suspicion. <em>E. g., ante, </em>at 624. We think the Government’s need to conduct the suspicionless searches required by the Customs program outweighs the privacy interests of employees engaged directly in drug interdiction, and of those who otherwise are required to carry firearms.</p>
<p id="b740-5">The Customs Service is our Nation’s first line of defense against one of the greatest problems affecting the health and welfare of our population. We have adverted before to “the veritable national crisis in law enforcement caused by smuggling of illicit narcotics.” <em>United States </em>v. <em>Montoya de Hernandez, </em><span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#538" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 538</a></span> (1985). See also <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#513" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 513</a></span> (Blackmun, J., dissenting). Our <page-number citation-index="1" label="669">*669</page-number>cases also reflect the traffickers’ seemingly inexhaustible repertoire of deceptive practices and elaborate schemes for importing narcotics, <em>e. g., United States </em>v. <em>Montoya de Hernandez, supra, </em>at 538-539; <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#608" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 608-609</a></span> (1977). The record in this case confirms that, through the adroit selection of source locations, smuggling routes, and increasingly elaborate methods of concealment, drug traffickers have managed to bring into this country increasingly large quantities of illegal drugs. App. 111. The record also indicates, and it is well known, that drug smugglers do not hesitate to use violence to protect their lucrative trade and avoid apprehension. <em>Id., </em>at 109.</p>
<p id="b741-5">Many of the Service’s employees are often exposed to this criminal element and to the controlled substances it seeks to smuggle into the country. <em>Ibid. </em>Cf. <em>United States </em>v. <em>Montoya de Hernandez, supra, </em>at 543. The physical safety of these employees may be threatened, and many may be tempted not only by bribes from the traffickers with whom they deal, but also by their own access to vast sources of valuable contraband seized and controlled by the Service. The Commissioner indicated below that “Customs [officers have been shot, stabbed, run over, dragged by automobiles, and assaulted with blunt objects while performing their duties.” App. at 109-110. At least nine officers have died in the line of duty since 1974. He also noted that Customs officers have been the targets of bribery by drug smugglers on numerous occasions, and several have been removed from the Service for accepting bribes and for other integrity violations. <em>Id., </em>at 114. See also United States Customs Service, Customs U. S. A., Fiscal Year 1987, p. 31 (reporting internal investigations that resulted in the arrest of 24 employees and 54 civilians); United States Customs Service, Customs U. S. A., Fiscal Year 1986, p. 32 (reporting that 334 criminal and serious integrity investigations were conducted during the fiscal year, resulting in the arrest of 37 employees and 17 civilians); United States Customs Service, Customs <page-number citation-index="1" label="670">*670</page-number>U. S. A., Fiscal Year 1985, p. 32 (reporting that 284 criminal and serious integrity investigations were conducted during the 1985 fiscal year, resulting in the arrest of 15 employees and 51 civilians).</p>
<p id="b742-4">It is readily apparent that the Government has a compelling interest in ensuring that front-line interdiction personnel are physically fit, and have unimpeachable integrity and judgment. Indeed, the Government’s interest here is at least as important as its interest in searching travelers entering the country. We have long held that travelers seeking to enter the country may be stopped and required to submit to a routine search without probable cause, or even founded suspicion, “because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in.” <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925). See also <em>United States </em>v. <em>Montoya de Hernandez, supra, </em>at <em>538; United States </em>v. <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#617" aria-description="Citation for case: United States v. Ramsey"><em>Ramsey, supra, </em>at 617-619</a></span>. This national interest in self-protection could be irreparably damaged if those charged with safeguarding it were, because of their own drug use, unsympathetic to their mission of interdicting narcotics. A drug user’s indifference to the Service’s basic mission or, even worse, his active complicity with the malefactors, can facilitate importation of sizable drug shipments or block apprehension of dangerous criminals. The public interest demands effective measures to bar drug users from positions directly involving the interdiction of illegal drugs.</p>
<p id="b742-5">The public interest likewise demands effective measures to prevent the promotion of drug users to positions that require the incumbent to carry a firearm, even if the incumbent is not engaged directly in the interdiction of drugs. Customs employees who may use deadly force plainly “discharge duties fraught with such risks of injury to others that even a momentary lapse of attention can have disastrous consequences.” <em>Ante, </em>at 628. We agree with the Government <page-number citation-index="1" label="671">*671</page-number>that the public should not bear the risk that employees who may suffer from impaired perception and judgment will be promoted to positions where they may need to employ deadly force. Indeed, ensuring against the creation of this dangerous risk will itself further Fourth Amendment values, as the use of deadly force may violate the Fourth Amendment in certain circumstances. See <em>Tennessee </em>v. <em>Garner, </em><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1, 7-12</a></span> (1985).</p>
<p id="b743-5">Against these valid public interests we must weigh the interference with individual liberty that results from requiring these classes of employees to undergo a urine test. The interference with individual privacy that results from the collection of a urine sample for subsequent chemical analysis could be substantial in some circumstances. <em>Ante, </em>at 626. We have recognized, however, that the “operational realities of the workplace” may render entirely reasonable certain work-related intrusions by supervisors and co-workers that might be viewed as unreasonable in other contexts. See <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S., at 717</a></span>; <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 732</a></span> (Scalia, J., concurring in judgment). While these operational realities will rarely affect an employee’s expectations of privacy with respect to searches of his person, or of personal effects that the employee may bring to the workplace, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#716" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 716, 725</a></span>, it is plain that certain forms of public employment may diminish privacy expectations even with respect to such personal searches. Employees of the United States Mint, for example, should expect to be subject to certain routine personal searches when they leave the workplace every day. Similarly, those who join our military or intelligence services may not only be required to give what in other contexts might be viewed as extraordinary assurances of trustworthiness and probity, but also may expect intrusive inquiries into their physical fitness for those special positions. Cf. <em>Snepp </em>v. <em>United States, </em><span class="citation" data-id="9427761"><a href="/opinion/110183/snepp-v-united-states/#509" aria-description="Citation for case: Snepp v. United States">444 U. S. 507, 509, n. 3</a></span> (1980); <em>Parker </em>v. <em>Levy, </em><span class="citation" data-id="9425778"><a href="/opinion/109077/parker-v-levy/#758" aria-description="Citation for case: Parker v. Levy">417 U. S. 733, 758</a></span> (1974); <em>Committee for GI Rights </em>v. <page-number citation-index="1" label="672">*672</page-number><em>Callaway, </em>171 U. S. App. D. C. 73, 84, <span class="citation" data-id="328554"><a href="/opinion/328554/the-committee-for-gi-rights-v-honorable-howard-h-callaway-secretary-of/#477" aria-description="Citation for case: The Committee for Gi Rights v. Honorable Howard H....">518 F. 2d 466, 477</a></span> (1975).</p>
<p id="b744-5">We think Customs employees who are directly involved in the interdiction of illegal drugs or who are required to carry firearms in the line of duty likewise have a diminished expectation of privacy in respect to the intrusions occasioned by a urine test. Unlike most private citizens or government employees in general, employees involved in drug interdiction reasonably should expect effective inquiry into their fitness and probity. Much the same is true of employees who are required to carry firearms. Because successful performance of their duties depends uniquely on their judgment and dexterity, these employees cannot reasonably expect to keep from the Service personal information that bears directly on their fitness. Cf. <em>In re Caruso </em>v. <em>Ward, </em>72 N. Y. 2d 433, 441, <span class="citation" data-id="5538531"><a href="/opinion/5689297/caruso-v-ward/#854" aria-description="Citation for case: Caruso v. Ward">530 N. E. 2d 850, 854-855</a></span> (1988). While reasonable tests designed to elicit this information doubtless infringe some privacy expectations, we do not believe these expectations outweigh the Government’s compelling interests in safety and in the integrity of our borders.<footnotemark>2</footnotemark></p>
<p id="b745-4"><page-number citation-index="1" label="673">*673</page-number>Without disparaging the importance of the governmental interests that support the suspicionless searches of these employees, petitioners nevertheless contend that the Service’s drug-testing program is unreasonable in two particulars. First, petitioners argue that the program is unjustified because it is not based on a belief that testing will reveal any drug use by covered employees. In pressing this argument, petitioners point out that the Service’s testing scheme was not implemented in response to any perceived drug problem among Customs employees, and that the program actually has not led to the discovery of a significant number of drug users. Brief for Petitioners 37, 44; Tr. of Oral Arg. 11-12, 20-21. Counsel for petitioners informed us at oral argument that no more than 5 employees out of 3,600 have tested positive for drugs. <em>Id., </em>at 11. Second, petitioners contend that the Service’s scheme is not a “sufficiently productive mechanism to justify [its] intrusion upon Fourth Amendment interests,” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#658" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 658-659</a></span> (1979), because illegal drug users can avoid detection with ease by temporary abstinence or by surreptitious adulteration of their urine specimens. Brief for Petitioners 46-47. These contentions are unpersuasive.</p>
<p id="b746-4"><page-number citation-index="1" label="674">*674</page-number>Petitioners’ first contention evinces an unduly narrow view of the context in which the Service’s testing program was implemented. Petitioners do not dispute, nor can there be doubt, that drug abuse is one of the most serious problems confronting our society today. There is little reason to believe that American workplaces are immune from this pervasive social problem, as is amply illustrated by our decision in <em>Railway Labor Executives. </em>See also <em>Masino </em>v. <em>United States, </em><span class="citation" data-id="1418046"><a href="/opinion/1418046/state-v-frank/#1050" aria-description="Citation for case: State v. Frank">589 P. 2d 1048, 1050</a></span> (Ct. Cl. 1978) (describing marijuana use by two Customs inspectors). Detecting drug impairment on the part of employees can be a difficult task, especially where, as here, it is not feasible to subject employees and their work product to the kind of day-to-day scrutiny that is the norm in more traditional office environments. Indeed, the almost unique mission of the Service gives the Government a compelling interest in ensuring that many of these covered employees do not use drugs even off duty, for such use creates risks of bribery and blackmail against which the Government is entitled to guard. In light of the extraordinary safety and national security hazards that would attend the promotion of drug users to positions that require the carrying of firearms or the interdiction of controlled substances, the Service’s policy of deterring drug users from seeking such promotions cannot be deemed unreasonable.</p>
<p id="b746-5">The mere circumstance that all but a few of the employees tested are entirely innocent of wrongdoing does not impugn the program’s validity. The same is likely to be true of householders who are required to submit to suspicionless housing code inspections, see <em>Camara </em>v. <em>Municipal Court of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), and of motorists who are stopped at the checkpoints we approved in <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976). The Service’s program is designed to prevent the promotion of drug users to sensitive positions as much as it is designed to detect those employees who use drugs. Where, as here, the possible harm against which the Government seeks to guard is <page-number citation-index="1" label="675">*675</page-number>substantial, the need to prevent its occurrence furnishes an ample justification for reasonable searches calculated to advance the Government’s goal.<footnotemark>3</footnotemark></p>
<p id="b748-4"><page-number citation-index="1" label="676">*676</page-number>We think petitioners’ second argument — that the Service’s testing program is ineffective because employees may attempt to deceive the test by a brief abstention before the test date, or by adulterating their urine specimens — overstates the case. As the Court of Appeals noted, addicts may be unable to abstain even for a limited period of time, or may be unaware of the “fade-away effect” of certain drugs. 816 F. 2d, at 180. More importantly, the avoidance techniques suggested by petitioners are fraught with uncertainty and risks for those employees who venture to attempt them. A particular employee’s pattern of elimination for a given drug cannot be predicted with perfect accuracy, and, in any event, this information is not likely to be known or available to the employee. Petitioners’ own expert indicated below that the time it takes for particular drugs to become undetectable in urine can vary widely depending on the individual, and may extend for as long as 22 days. App. 66. See also <em>ante, </em>at 631 (noting Court of Appeals’ reliance on certain academic literature that indicates that the testing of urine can discover drug use “ ‘for. . . weeks after the ingestion of the drug’ ”). Thus, contrary to petitioners’ suggestion, no employee reasonably can expect to deceive the test by the simple expedient of abstaining after the test date is assigned. Nor can he expect attempts at adulteration to succeed, in view of the precautions taken by the sample collector to ensure the integrity of the sample. In all the circumstances, we are persuaded that the program bears a close and substantial relation to the Service’s goal of deterring drug users from seeking promotion to sensitive positions.<footnotemark>4</footnotemark></p>
<p id="b749-4"><page-number citation-index="1" label="677">*677</page-number>In sum, we believe the Government has demonstrated that its compelling interests in safeguarding our borders and the public safety outweigh the privacy expectations of employees who seek to be promoted to positions that directly involve the interdiction of illegal drugs or that require the incumbent to carry a firearm. We hold that the testing of these employees is reasonable under the Fourth Amendment.</p>
<p id="b749-5">C</p>
<p id="b749-6">We are unable, on the present record, to assess the reasonableness of the Government’s testing program insofar as it covers employees who are required “to handle classified material.” App. 17. We readily agree that the Government has a compelling interest in protecting truly sensitive information from those who, “under compulsion of circumstances or for other reasons, . . . might compromise [such] information.” <em>Department of Navy </em>v. <em>Egan, </em><span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/#528" aria-description="Citation for case: Department of the Navy v. Egan">484 U. S. 518, 528</a></span> (1988). See also <em>United States </em>v. <em>Robel, </em><span class="citation" data-id="9423541"><a href="/opinion/107554/united-states-v-robel/#267" aria-description="Citation for case: United States v. Robel">389 U. S. 258, 267</a></span> (1967) (“We have recognized that, while the Constitution protects against invasions of individual rights, it does not withdraw from the Government the power to safeguard its vital interests. . . . The Government can deny access to its secrets to those who would use such information to harm the Nation”). We also agree that employees who seek promotions to positions where they would handle sensitive information can be required to submit to a urine test under the Service’s screening program, especially if the positions covered under this category require background investigations, medical examinations, or other intrusions that may be expected to diminish their expectations of privacy in respect of a urinalysis test. Cf. <em>Department of Navy </em>v. <span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/#528" aria-description="Citation for case: Department of the Navy v. Egan"><em>Egan, supra, </em>at 528</a></span> (noting that the Executive Branch generally subjects those desir<page-number citation-index="1" label="678">*678</page-number>ing a security clearance to “a background investigation that varies according to the degree of adverse effect the applicant could have on the national security”).</p>
<p id="b750-5">It is not clear, however, whether the category defined by the Service’s testing directive encompasses only those Customs employees likely to gain access to sensitive information. Employees who are tested under the Service’s scheme include those holding such diverse positions as “Accountant,” “Accounting Technician,” “Animal Caretaker,” “Attorney (All),” “Baggage Clerk,” “Co-op Student (All),” “Electric Equipment Repairer,” “Mail Clerk/Assistant,” and “Messenger.” App. 42-43. We assume these positions were selected for coverage under the Service’s testing program by reason of the incumbent’s access to “classified” information, as it is not clear that they would fall under either of the two categories we have already considered. Yet it is not evident that those occupying these positions are likely to gain access to sensitive information, and this apparent discrepancy raises in our minds the question whether the Service has defined this category of employees more broadly than is necessary to meet the purposes of the Commissioner’s directive.</p>
<p id="b750-6">We cannot resolve this ambiguity on the basis of the record before us, and we think it is appropriate to remand the case to the Court of Appeals for such proceedings as may be necessary to clarify the scope of this category of employees subject to testing. Upon remand the Court of Appeals should examine the criteria used by the Service in determining what materials are classified and in deciding whom to test under this rubric. In assessing the reasonableness of requiring tests of these employees, the court should also consider pertinent information bearing upon the employees’ privacy expectations, as well as the supervision to which these employees are already subject.</p>
<p id="b750-7">Ill</p>
<p id="b750-8">Where the Government requires its employees to produce urine samples to be analyzed for evidence of illegal drug <page-number citation-index="1" label="679">*679</page-number>use, the collection and subsequent chemical analysis of such samples are searches that must meet the reasonableness requirement of the Fourth Amendment. Because the testing program adopted by the Customs Service is not designed to serve the ordinary' needs of law enforcement, we have balanced the public interest in the Service’s testing program against the privacy concerns implicated by the tests, without reference to our usual presumption in favor of the procedures specified in the Warrant Clause, to assess whether the tests required by Customs are reasonable.</p>
<p id="b751-5">We hold that the suspicionless testing of employees who apply for promotion to positions directly involving the interdiction of illegal drugs, or to positions that require the incumbent to carry a firearm, is reasonable. The Government’s compelling interests in preventing the promotion of drug users to positions where they might endanger the integrity of our Nation’s borders or the life of the citizenry outweigh the privacy interests of those who seek promotion to these positions, who enjoy a diminished expectation of privacy by virtue of the special, and obvious, physical and ethical demands of those positions. We do not decide whether testing those who apply for promotion to positions where they would handle “classified” information is reasonable because we find the record inadequate for this purpose.</p>
<p id="b751-6">The judgment of the Court of Appeals for the Fifth Circuit is affirmed in part and vacated in part, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b751-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b733-7"> After this case was decided by .the Court of Appeals, <span class="citation multiple-matches"><a href="/c/F.%202d/816/170/">816 F. 2d 170</a></span> (CA5 1987), the United States Department of Health and Human Services, in accordance with recently enacted legislation, <span class="citation no-link">Pub. L. 100-71, § 503</span>, <span class="citation no-link">101 <page-number citation-index="1" label="662">*662</page-number>Stat. 468</span>-471, promulgated regulations (hereinafter HHS Regulations or HHS Reg.) governing certain federal employee drug-testing programs. <span class="citation no-link">53 Fed. Reg. 11979</span> (1988). To the extent the HHS Regulations add to, or depart from, the procedures adopted as part of a federal drug-screening program covered by <span class="citation no-link">Pub. L. 100-71, </span>the HHS Regulations control. <span class="citation no-link">Pub. L. 100-71, § 503</span>(b)(2)(B), <span class="citation no-link">101 Stat. 470</span>. Both parties agree that the Customs Service’s drug-testing program must conform to the HHS Regulations. See Brief for Petitioners 6, n. 8; Brief for Respondent 4-5, and n. 4. We therefore consider the HHS Regulations to the extent they supplement or displace the Commissioner’s original directive. See <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#53" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 53</a></span> (1974); <em>Thorpe </em>v. <em>Housing Authority of Durham, </em><span class="citation" data-id="9423867"><a href="/opinion/107814/thorpe-v-housing-authority-of-durham/#281" aria-description="Citation for case: Thorpe v. Housing Authority of Durham">393 U. S. 268, 281-282</a></span> (1969).</p>
<p id="b734-6">One respect in which the original Customs directive differs from the now-prevailing regime concerns the extent to which the employee may be required to disclose personal medical information. Under the Service’s original plan, each tested employee was asked to disclose, at the time the urine sample was collected, any medications taken within the last 30 days, and to explain any circumstances under which he may have been in legitimate contact with illegal substances within the last 30 days. Failure to provide this information at this time could result in the agency not considering the effect of medications or other licit contacts with drugs on a positive test result. Under the HHS Regulations, an employee need not provide information concerning medications when he produces the sample for testing. He may instead present such information only, after he is notified that his specimen tested positive for illicit drugs, at which time the Medical Review Officer reviews all records made available by the employee to determine whether the positive indication could have been caused by lawful use of drugs. See HHS Reg. § 2.7, <span class="citation no-link">53 Fed. Reg. 11985</span>-11986 (1988).</p>
</footnote>
<footnote label="2">
<p id="b744-6"> The procedures prescribed by the Customs Service for the collection and analysis of the requisite samples do not carry the grave potential for “arbitrary and oppressive interference with the privacy and personal security of individuals,” <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span>, (1976), that the Fourth Amendment was designed to prevent. Indeed, these procedures significantly minimize the program’s intrusion on privacy interests. Only employees who have been tentatively accepted for promotion or transfer to one of the three categories of covered positions are tested, and applicants know at the outset that a drug test is a requirement of those positions. Employees are also notified in advance of the scheduled sample collection, thus reducing to a minimum any “unsettling show of authority,” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#657" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 657</a></span> (1979), that may be associated with unexpected intrusions on privacy. Cf. <em>United States </em>v. <em>Martinez-FueHe, supra, </em>at 559 (noting that the intrusion on privacy occasioned by routine highway checkpoints is minimized by the fact that motorists “are not taken by surprise as they know, or may obtain knowledge of, the location of the checkpoints and will not be stopped elsewhere”); <em>Wyman </em>v. <em>James, </em><span class="citation" data-id="9424375"><a href="/opinion/108223/wyman-v-james/#320" aria-description="Citation for case: Wyman v. James">400 U. S. 309, 320-321</a></span> (1971) (providing a welfare re-<page-number citation-index="1" label="673">*673</page-number>eipient with advance notice that she would be visited by a welfare caseworker minimized the intrusion on privacy occasioned by the visit). There is no direct observation of the act of urination, as the employee may provide a specimen in the privacy of a stall.</p>
<p id="b745-6">Further, urine samples may be examined only for the specified drugs. The use of samples to test for any other substances is prohibited. See HHS Reg. § 2.1(c), <span class="citation no-link">53 Fed. Reg. 11980</span> (1988). And, as the Court of Appeals noted, the combination of EMIT and GC/MS tests required by the Service is highly accurate, assuming proper storage, handling, and measurement techniques. 816 F. 2d, at 181. Finally, an employee need not disclose personal medical information to the Government unless his test result is positive, and even then any such information is reported to a licensed physician. Taken together, these procedures significantly minimize the intrusiveness of the Service’s drug-screening program.</p>
</footnote>
<footnote label="3">
<p id="b747-5"> The point is well illustrated also by the Federal Government’s practice of requiring the search of all passengers seeking to board commercial airliners, as well as the search of their carry-on luggage, without any basis for suspecting any particular passenger of an untoward motive. Applying our precedents dealing with administrative searches, see, <em>e. g., Camara </em>v. <em>Municipal Court of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), the lower courts that have considered the question have consistently concluded that such searches are reasonable under the Fourth Amendment. As Judge Friendly explained in a leading case upholding such searches:</p>
<p id="b747-6">“When the risk is the jeopardy to hundreds of human lives and millions of dollars of property inherent in the pirating or blowing up of a large airplane, that danger <em>alone </em>meets the test of reasonableness, so long as the search is conducted in good faith for the purpose of preventing hijacking or like damage and with reasonable scope and the passenger has been given advance notice of his liability to such a search so that he can avoid it by choosing not to travel by air.” <em>United States </em>v. <em>Edwards, </em><span class="citation" data-id="9460705"><a href="/opinion/319945/united-states-v-cynthia-edwards/#500" aria-description="Citation for case: United States v. Cynthia Edwards">498 F. 2d 496, 500</a></span> (CA2 1974) (emphasis in original).</p>
<p id="b747-7">See also <em>United States </em>v. <em>Skipwith, </em><span class="citation" data-id="9459727"><a href="/opinion/312834/united-states-v-lee-skipwith-iii/#1275" aria-description="Citation for case: United States v. Lee Skipwith, III">482 F. 2d 1272, 1275-1276</a></span> (CA5 1973); <em>United States </em>v. <em>Davis, </em><span class="citation" data-id="312772"><a href="/opinion/312772/united-states-v-charles-davis-aka-marcus-anderson/#907" aria-description="Citation for case: United States v. Charles Davis AKA Marcus Anderson">482 F. 2d 893, 907-912</a></span> (CA9 1973). It is true, as counsel for petitioners pointed out at oral argument, that these air piracy precautions were adopted in response to an observable national and international hijacking crisis. Tr. of Oral Arg. 13. Yet we would not suppose that, if the validity of these searches be conceded, the Government would be precluded from conducting them absent a demonstration of danger as to any particular airport or airline. It is sufficient that the Government have a compelling interest in preventing an otherwise pervasive societal problem from spreading to the particular context.</p>
<p id="b747-9">Nor would we think, in view of the obvious deterrent purpose of these searches, that the validity of the Government’s airport screening program necessarily turns on whether significant numbers of putative air pirates are actually discovered by the searches conducted under the program. In the 15 years the program has been in effect, more than 9.5 <em>billion </em>persons have been screened, and over 10 <em>billion </em>pieces of luggage have been inspected. See Federal Aviation Administration, Semiannual Report to Congress on the Effectiveness of The Civil Aviation Program (Nov. 1988) (Exhibit 6). By far the overwhelming majority of those persons who have been searched, like Customs employees who have been tested under the Service’s drug-screening scheme, have proved entirely innocent — only <page-number citation-index="1" label="676">*676</page-number>42,000 firearms have been detected during the same period. <em><span class="citation" data-id="312772"><a href="/opinion/312772/united-states-v-charles-davis-aka-marcus-anderson/" aria-description="Citation for case: United States v. Charles Davis AKA Marcus Anderson">Ibid.</a></span> </em>When the Government’s interest lies in deterring highly hazardous conduct, a low incidence of such conduct, far from impugning the validity of the scheme for implementing this interest, is more logically viewed as a hallmark of success. See <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#559" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 559</a></span> (1979).</p>
</footnote>
<footnote label="4">
<p id="b748-6"> Indeed, petitioners’ objection is based on those features of the Service's program — the provision of advance notice and the failure of the sample collector to observe directly the act of urination — that contribute sig-<page-number citation-index="1" label="677">*677</page-number>nifieantly to diminish the program’s intrusion on privacy. See <em>supra, </em>at 672-673, n. 2. Thus, under petitioners’ view, “the testing program would be more likely to be constitutional if it were more pervasive and more invasive of privacy.” 816 F. 2d, at 180.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Navarette v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Navarette v. California"
type: case
citation: ""
parallel_cite: "134 S. Ct. 1683; 188 L. Ed. 2d 680; 82 U.S.L.W. 4282; 572 U.S. 393; 24 Fla. L. Weekly Fed. S 690"
neutral_cite: "2014 U.S. LEXIS 2930; 2014 WL 1577513"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-04-22
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2014-04-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Navarette v. California
  varies_by_point: false
  scope_note: Good law on anonymous-tip reliability for reasonable suspicion.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2670795/prado-navarette-v-california/"
  cluster_id: 2670795
  opinion_id: 2670795
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Alabama v. White]]", "[[Florida v. J.L.]]", "[[Illinois v. Gates]]", "[[Terry v. Ohio]]"]
aliases: ["Prado Navarette v. California"]
tags: ["case", "fourth-amendment", "reasonable-suspicion", "anonymous-tip", "traffic-stop"]
holding: "A 911 call reporting dangerous/reckless driving can supply reasonable suspicion for a stop when it bears adequate indicia of reliability…"
lake:
  record_id: Navarette v. California
  status: verified
  projected_at: 2026-07-06
---

# Navarette v. California

*572 U.S. 393 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A 911 caller reported that a specific silver Ford pickup truck had just run her off the road, giving the truck's license plate and location. Officers located the truck and stopped it without independently observing any traffic violation; as they approached they smelled marijuana and found 30 pounds of it. The occupants moved to suppress, arguing the anonymous tip did not supply reasonable suspicion.

## Issue
Whether an anonymous 911 tip reporting dangerous driving can supply reasonable suspicion for an investigatory traffic stop.

## Rule
Under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], an anonymous tip may supply reasonable suspicion when it bears adequate indicia of reliability. Here, "we conclude that the call bore adequate indicia of reliability for the officer to credit the caller's account." — 572 U.S. at 398. ^pin-398

The Court found the 911 call reliable because the caller claimed eyewitness knowledge of dangerous driving, reported it contemporaneously, and used the 911 system, which has features that allow tracing callers and deter false reports.

## Application
The caller's report that the truck had run her off the road described conduct supporting reasonable suspicion of drunk driving; the caller's eyewitness basis of knowledge, near-contemporaneous report, and use of the 911 system gave the tip sufficient reliability. The officers were therefore justified in stopping the identified truck even though they had not personally witnessed erratic driving.

## Conclusion
The traffic stop complied with the Fourth Amendment; the judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Navarette* applies the anonymous-tip framework of [[Alabama v. White]] and distinguishes [[Florida v. J.L.]], holding that a contemporaneous, eyewitness 911 report of dangerous driving can carry enough indicia of reliability to justify a stop.

## Appears on
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *Navarette v. California*, 572 U.S. 393 (2014) — https://www.courtlistener.com/opinion/2670795/prado-navarette-v-california/ — pinpoint: 398.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "59de07152b2c41e0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2014 U.S. LEXIS 2930; 2014 WL 1577513", "official_citation_present": false, "parallel_cite": "134 S. Ct. 1683; 188 L. Ed. 2d 680; 82 U.S.L.W. 4282; 572 U.S. 393; 24 Fla. L. Weekly Fed. S 690", "title": "Navarette v. California", "year": "2014"}}
{"assertion_id": "1872c3fa16eabed4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A 911 call reporting dangerous/reckless driving can supply reasonable suspicion for a stop when it bears adequate indicia of reliability…", "title": "Navarette v. California"}}
{"assertion_id": "231fea006d6a3aa9", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Key — Progeny / Refinement", "title": "Navarette v. California"}}
{"assertion_id": "06b2e894489571ba", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Navarette v. California"}}
{"assertion_id": "a9e6d9dfdf51bfc8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2014-04-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Navarette v. California", "field_i_validity": "good_law", "scope_note": "Good law on anonymous-tip reliability for reasonable suspicion.", "title": "Navarette v. California", "varies_by_point": "false"}}
```

### lake record — Navarette v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Navarette v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Prado Navarette v. California",
    "case_name_short": "Navarette",
    "case_name_full": "Lorenzo Prado NAVARETTE and Jos\u00e9 Prado Navarette, Petitioners, v. CALIFORNIA.",
    "input_case_name": "Navarette v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-04-22",
    "year": 2014,
    "docket": null,
    "cluster_id": 2670795,
    "lead_opinion_id": 2670795,
    "sibling_ids": [
      2670795
    ],
    "absolute_url": "/opinion/2670795/prado-navarette-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8414100,
        "score": 20,
        "case_name": "Navarette v. California"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "134 S. Ct. 1683",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "1683",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 680",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "680",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4282",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4282",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "572 U.S. 393",
        "volume": "572",
        "reporter": "U.S.",
        "page": "393",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 690",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. LEXIS 2930",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "2930",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 1577513",
        "volume": "2014",
        "reporter": "WL",
        "page": "1577513",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "134 S. Ct. 1683",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "1683",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 680",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "680",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. LEXIS 2930",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "2930",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4282",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4282",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "572 U.S. 393",
        "volume": "572",
        "reporter": "U.S.",
        "page": "393",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 690",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 1577513",
        "volume": "2014",
        "reporter": "WL",
        "page": "1577513",
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
      "id": "pin-398",
      "page": null,
      "quote": "--- # Navarette v. California *572 U.S. 393 (2014)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A 911 caller reported that a specific silver Ford pickup truck had just run her off the road, giving the truck's license plate and location. Officers located the truck and stopped it without independently observing any traffic violation; as they approached they smelled marijuana and found 30 pounds of it. The occupants moved to suppress, arguing the anonymous tip did not supply reasonable suspicion. ## Issue Whether an anonymous 911 tip reporting dangerous driving can supply reasonable suspicion for an investigatory traffic stop. ## Rule Under the totality of the circumstances, an anonymous tip may supply reasonable suspicion when it bears adequate indicia of reliability. Here,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2014-04-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Navarette v. California",
    "varies_by_point": false,
    "scope_note": "Good law on anonymous-tip reliability for reasonable suspicion.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Castillo-Martinez",
          "cluster_id": 9489871,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The State of Texas v. Martin Eduardo Velasquezreyes",
          "cluster_id": 9481403,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane1_negative"
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
        "journal_ref": "Navarette v. California:lane1_negative"
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
        "journal_ref": "Navarette v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kevin Gamble (071234)",
          "cluster_id": 2686119,
          "cite": [
            "218 N.J. 412",
            "95 A.3d 188",
            "2014 WL 3858497",
            "2014 N.J. LEXIS 801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
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
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Beal, Jr. v. James Beller",
          "cluster_id": 4348069,
          "cite": [
            "847 F.3d 897",
            "2017 WL 544599",
            "2017 U.S. App. LEXIS 2439"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeff Courtright v. City of Battle Creek",
          "cluster_id": 4312445,
          "cite": [
            "839 F.3d 513",
            "2016 FED App. 0256P",
            "2016 U.S. App. LEXIS 18502",
            "2016 WL 5956725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
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
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Barbeau",
          "cluster_id": 4543099,
          "cite": [
            "301 Neb. 293",
            "917 N.W.2d 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Halley v. Huckaby",
          "cluster_id": 4530346,
          "cite": [
            "902 F.3d 1136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthews, Cornelious L.",
          "cluster_id": 2949477,
          "cite": [
            "431 S.W.3d 596",
            "2014 WL 3029070",
            "2014 Tex. Crim. App. LEXIS 820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linda Brooks v. Avancez",
          "cluster_id": 6621840,
          "cite": [
            "39 F.4th 424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Silveria and Travis",
          "cluster_id": 4774990,
          "cite": [
            "267 Cal. Rptr. 3d 303",
            "471 P.3d 412",
            "10 Cal. 5th 195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
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
        "journal_ref": "Navarette v. California:lane2_top_cited"
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
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ezekiel Gardner",
          "cluster_id": 3204635,
          "cite": [
            "823 F.3d 793",
            "2016 U.S. App. LEXIS 9066",
            "2016 WL 2893881"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 2824888,
          "cite": [
            "61 Cal. 4th 968",
            "353 P.3d 305",
            "190 Cal. Rptr. 3d 583",
            "2015 Cal. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Carter",
          "cluster_id": 2756719,
          "cite": [
            "105 A.3d 765",
            "2014 Pa. Super. 265",
            "2014 Pa. Super. LEXIS 4539",
            "2014 WL 6756271"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mason v. Commonwealth",
          "cluster_id": 3200832,
          "cite": [
            "786 S.E.2d 148",
            "291 Va. 362",
            "2016 WL 2586178",
            "2016 Va. LEXIS 59"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gaytan",
          "cluster_id": 2812404,
          "cite": [
            "2015 IL 116223"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
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
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest D. Shields",
          "cluster_id": 2808513,
          "cite": [
            "789 F.3d 733",
            "2015 U.S. App. LEXIS 10058",
            "2015 WL 3654318"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hawkins (Slip Opinion)",
          "cluster_id": 4669773,
          "cite": [
            "2019 Ohio 4210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Correll Thomas v. C. Dillard",
          "cluster_id": 3191530,
          "cite": [
            "818 F.3d 864",
            "2016 U.S. App. LEXIS 6210",
            "2016 WL 1319765"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warren Green, IV",
          "cluster_id": 4520277,
          "cite": [
            "897 F.3d 173"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Williams",
          "cluster_id": 3007498,
          "cite": [
            "125 A.3d 425",
            "2015 Pa. Super. 216",
            "2015 Pa. Super. LEXIS 581",
            "2015 WL 5810631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Patrick I. Hogan",
          "cluster_id": 2816261,
          "cite": [
            "364 Wis. 2d 167",
            "2015 WI 76",
            "868 N.W.2d 124",
            "2015 Wisc. LEXIS 348"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hernandez",
          "cluster_id": 4347480,
          "cite": [
            "847 F.3d 1257",
            "2017 WL 526028",
            "2017 U.S. App. LEXIS 2324"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2670795) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTU0MTYzMjAwMDAwJnM9NDYwMzU4MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282670795%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(2670795)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNyZzPTMxMzMzMjUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282670795%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2670795)",
        "reviewed": 116,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 116,
        "triage_read": 2,
        "triage_snippet_classified": 114
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2670795)",
    "indexed_citing_opinions": 442,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2670795,
        "count": 442,
        "count_source": "search"
      }
    ],
    "citation_count": 1112,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/navarette-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjI2NDImcz0xMDM1NzU4NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282670795%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2670795,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 112454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 117921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 118352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 118474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 776340,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 1990652,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 2089507,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 2575791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 2629186,
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
    "date_created": "2026-07-05T15:09:29Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:14:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Navarette v. California

```
(Slip Opinion)              OCTOBER TERM, 2013                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

         PRADO NAVARETTE ET AL. v. CALIFORNIA

    CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA,

                FIRST APPELLATE DISTRICT


    No. 12–9490. Argued January 21, 2014—Decided April 22, 2014
A California Highway Patrol officer stopped the pickup truck occupied
  by petitioners because it matched the description of a vehicle that a
  911 caller had recently reported as having run her off the road. As he
  and a second officer approached the truck, they smelled marijuana.
  They searched the truck’s bed, found 30 pounds of marijuana, and ar-
  rested petitioners. Petitioners moved to suppress the evidence, argu-
  ing that the traffic stop violated the Fourth Amendment. Their mo-
  tion was denied, and they pleaded guilty to transporting marijuana.
  The California Court of Appeal affirmed, concluding that the officer
  had reasonable suspicion to conduct an investigative stop.
Held: The traffic stop complied with the Fourth Amendment because,
 under the totality of the circumstances, the officer had reasonable
 suspicion that the truck’s driver was intoxicated. Pp. 3–11.
    (a) The Fourth Amendment permits brief investigative stops when
 an officer has “a particularized and objective basis for suspecting the
 particular person stopped of . . . criminal activity.” United States v.
 Cortez, 449 U. S. 411, 417–418. Reasonable suspicion takes into ac-
 count “the totality of the circumstances,” id., at 417, and depends
 “upon both the content of information possessed by police and its de-
 gree of reliability,” Alabama v. White, 496 U. S. 325, 330. An anony-
 mous tip alone seldom demonstrates sufficient reliability, White, 496
 U. S., at 329, but may do so under appropriate circumstances, id., at
 327. Pp. 3–5.
    (b) The 911 call in this case bore adequate indicia of reliability for
 the officer to credit the caller’s account. By reporting that she had
 been run off the road by a specific vehicle, the caller necessarily
 claimed an eyewitness basis of knowledge. The apparently short
 time between the reported incident and the 911 call suggests that the
2                 PRADO NAVARETTE v. CALIFORNIA

                                  Syllabus

    caller had little time to fabricate the report. And a reasonable officer
    could conclude that a false tipster would think twice before using the
    911 system, which has several technological and regulatory features
    that safeguard against making false reports with immunity. Pp. 5–8.
      (c) Not only was the tip here reliable, but it also created reasonable
    suspicion of drunk driving. Running another car off the road sug-
    gests the sort of impairment that characterizes drunk driving. While
    that conduct might be explained by another cause such as driver dis-
    traction, reasonable suspicion “need not rule out the possibility of in-
    nocent conduct.” United States v. Arvizu, 534 U. S. 266, 277. Finally,
    the officer’s failure to observe additional suspicious conduct during
    the short period that he followed the truck did not dispel the reason-
    able suspicion of drunk driving, and the officer was not required to
    surveil the truck for a longer period. Pp. 8–10.
Affirmed.

   THOMAS, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, BREYER, and ALITO, JJ., joined. SCALIA, J., filed a
dissenting opinion, in which GINSBURG, SOTOMAYOR, and KAGAN, JJ.,
joined.
                        Cite as: 572 U. S. ____ (2014)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash­
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 12–9490
                                   _________________


  LORENZO PRADO NAVARETTE AND JOSE PRADO 

    NAVARETTE, PETITIONERS v. CALIFORNIA 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF 

        CALIFORNIA, FIRST APPELLATE DISTRICT

                                 [April 22, 2014]

  JUSTICE THOMAS delivered the opinion of the Court.
  After a 911 caller reported that a vehicle had run her off
the road, a police officer located the vehicle she identified
during the call and executed a traffic stop. We hold that
the stop complied with the Fourth Amendment because,
under the totality of the circumstances, the officer had
reasonable suspicion that the driver was intoxicated.
                             I
   On August 23, 2008, a Mendocino County 911 dispatch
team for the California Highway Patrol (CHP) received a
call from another CHP dispatcher in neighboring Hum­
boldt County. The Humboldt County dispatcher relayed a
tip from a 911 caller, which the Mendocino County team
recorded as follows: “ ‘Showing southbound Highway 1 at
mile marker 88, Silver Ford 150 pickup. Plate of 8-David­
94925. Ran the reporting party off the roadway and was
last seen approximately five [minutes] ago.’ ” App. 36a.
The Mendocino County team then broadcast that infor­
mation to CHP officers at 3:47 p.m.
   A CHP officer heading northbound toward the reported
vehicle responded to the broadcast. At 4:00 p.m., the
2               PRADO NAVARETTE v. CALIFORNIA

                         Opinion of the Court

officer passed the truck near mile marker 69. At about
4:05 p.m., after making a U-turn, he pulled the truck over.
A second officer, who had separately responded to the
broadcast, also arrived on the scene. As the two officers
approached the truck, they smelled marijuana. A search
of the truck bed revealed 30 pounds of marijuana. The
officers arrested the driver, petitioner Lorenzo Prado
Navarette, and the passenger, petitioner José Prado
Navarette.
  Petitioners moved to suppress the evidence, arguing
that the traffic stop violated the Fourth Amendment
because the officer lacked reasonable suspicion of criminal
activity. Both the magistrate who presided over the sup­
pression hearing and the Superior Court disagreed.1
Petitioners pleaded guilty to transporting marijuana and
were sentenced to 90 days in jail plus three years of
probation.
  The California Court of Appeal affirmed, concluding
that the officer had reasonable suspicion to conduct an
investigative stop. 2012 WL 4842651 (Oct. 12, 2012). The
court reasoned that the content of the tip indicated that it
came from an eyewitness victim of reckless driving, and
that the officer’s corroboration of the truck’s description,
location, and direction established that the tip was reliable
enough to justify a traffic stop. Id., at *7. Finally, the
court concluded that the caller reported driving that was
sufficiently dangerous to merit an investigative stop with­
out waiting for the officer to observe additional reckless
driving himself. Id., at *9. The California Supreme Court
——————
   1 At the suppression hearing, counsel for petitioners did not dispute

that the reporting party identified herself by name in the 911 call
recording. Because neither the caller nor the Humboldt County dis­
patcher who received the call was present at the hearing, however, the
prosecution did not introduce the recording into evidence. The prosecu­
tion proceeded to treat the tip as anonymous, and the lower courts
followed suit. See 2012 WL 4842651, *6 (Cal. Ct. App., Oct. 12, 2012).
                  Cite as: 572 U. S. ____ (2014)            3

                      Opinion of the Court

denied review. We granted certiorari, 570 U. S. ___
(2013), and now affirm.
                             II
  The Fourth Amendment permits brief investigative
stops—such as the traffic stop in this case—when a law
enforcement officer has “a particularized and objective
basis for suspecting the particular person stopped of crim­
inal activity.” United States v. Cortez, 449 U. S. 411, 417–
418 (1981); see also Terry v. Ohio, 392 U. S. 1, 21–22
(1968). The “reasonable suspicion” necessary to justify
such a stop “is dependent upon both the content of infor­
mation possessed by police and its degree of reliability.”
Alabama v. White, 496 U. S. 325, 330 (1990). The stand­
ard takes into account “the totality of the circumstances—
the whole picture.” Cortez, supra, at 417. Although a
mere “ ‘hunch’ ” does not create reasonable suspicion,
Terry, supra, at 27, the level of suspicion the standard
requires is “considerably less than proof of wrongdoing by
a preponderance of the evidence,” and “obviously less”
than is necessary for probable cause, United States v.
Sokolow, 490 U. S. 1, 7 (1989).
                              A
   These principles apply with full force to investigative
stops based on information from anonymous tips. We
have firmly rejected the argument “that reasonable cause
for a[n investigative stop] can only be based on the officer’s
personal observation, rather than on information supplied
by another person.” Adams v. Williams, 407 U. S. 143,
147 (1972). Of course, “an anonymous tip alone seldom
demonstrates the informant’s basis of knowledge or verac­
ity.” White, 496 U. S., at 329 (emphasis added). That is
because “ordinary citizens generally do not provide exten­
sive recitations of the basis of their everyday observa­
tions,” and an anonymous tipster’s veracity is “ ‘by hypoth­
4            PRADO NAVARETTE v. CALIFORNIA

                     Opinion of the Court

esis largely unknown, and unknowable.’ ” Ibid. But under
appropriate circumstances, an anonymous tip can demon­
strate “sufficient indicia of reliability to provide reasona­
ble suspicion to make [an] investigatory stop.” Id., at 327.
   Our decisions in Alabama v. White, 496 U. S. 325 (1990),
and Florida v. J. L., 529 U. S. 266 (2000), are useful
guides. In White, an anonymous tipster told the police
that a woman would drive from a particular apartment
building to a particular motel in a brown Plymouth station
wagon with a broken right tail light. The tipster further
asserted that the woman would be transporting cocaine.
496 U. S., at 327. After confirming the innocent details,
officers stopped the station wagon as it neared the motel
and found cocaine in the vehicle. Id., at 331. We held that
the officers’ corroboration of certain details made the
anonymous tip sufficiently reliable to create reasonable
suspicion of criminal activity. By accurately predicting
future behavior, the tipster demonstrated “a special famil­
iarity with respondent’s affairs,” which in turn implied
that the tipster had “access to reliable information about
that individual’s illegal activities.” Id., at 332. We also
recognized that an informant who is proved to tell the
truth about some things is more likely to tell the truth
about other things, “including the claim that the object of
the tip is engaged in criminal activity.” Id., at 331 (citing
Illinois v. Gates, 462 U. S. 213, 244 (1983)).
   In J. L., by contrast, we determined that no reasonable
suspicion arose from a bare-bones tip that a young black
male in a plaid shirt standing at a bus stop was carrying a
gun. 529 U. S., at 268. The tipster did not explain how he
knew about the gun, nor did he suggest that he had any
special familiarity with the young man’s affairs. Id., at
271. As a result, police had no basis for believing “that the
tipster ha[d] knowledge of concealed criminal activity.”
Id., at 272. Furthermore, the tip included no predictions
of future behavior that could be corroborated to assess the
                  Cite as: 572 U. S. ____ (2014)            5

                      Opinion of the Court

tipster’s credibility. Id., at 271. We accordingly concluded
that the tip was insufficiently reliable to justify a stop and
frisk.
                                B
   The initial question in this case is whether the 911 call
was sufficiently reliable to credit the allegation that peti­
tioners’ truck “ran the [caller] off the roadway.” Even
assuming for present purposes that the 911 call was anon­
ymous, see n. 1, supra, we conclude that the call bore
adequate indicia of reliability for the officer to credit the
caller’s account. The officer was therefore justified in
proceeding from the premise that the truck had, in fact,
caused the caller’s car to be dangerously diverted from the
highway.
   By reporting that she had been run off the road by a
specific vehicle—a silver Ford F-150 pickup, license plate
8D94925—the caller necessarily claimed eyewitness
knowledge of the alleged dangerous driving. That basis of
knowledge lends significant support to the tip’s reliability.
See Gates, supra, at 234 (“[An informant’s] explicit and
detailed description of alleged wrongdoing, along with a
statement that the event was observed firsthand, entitles
his tip to greater weight than might otherwise be the
case”); Spinelli v. United States, 393 U. S. 410, 416 (1969)
(a tip of illegal gambling is less reliable when “it is not
alleged that the informant personally observed [the de­
fendant] at work or that he had ever placed a bet with
him”). This is in contrast to J. L., where the tip provided
no basis for concluding that the tipster had actually seen
the gun. 529 U. S., at 271. Even in White, where we
upheld the stop, there was scant evidence that the tipster
had actually observed cocaine in the station wagon. We
called White a “ ‘close case’ ” because “[k]nowledge about a
person’s future movements indicates some familiarity with
that person’s affairs, but having such knowledge does not
6            PRADO NAVARETTE v. CALIFORNIA

                     Opinion of the Court

necessarily imply that the informant knows, in particular,
whether that person is carrying hidden contraband.” 529
U. S., at 271. A driver’s claim that another vehicle ran her
off the road, however, necessarily implies that the inform­
ant knows the other car was driven dangerously.
   There is also reason to think that the 911 caller in this
case was telling the truth. Police confirmed the truck’s
location near mile marker 69 (roughly 19 highway miles
south of the location reported in the 911 call) at 4:00 p.m.
(roughly 18 minutes after the 911 call). That timeline of
events suggests that the caller reported the incident soon
after she was run off the road. That sort of contemporane­
ous report has long been treated as especially reliable. In
evidence law, we generally credit the proposition that
statements about an event and made soon after perceiving
that event are especially trustworthy because “substantial
contemporaneity of event and statement negate the likeli­
hood of deliberate or conscious misrepresentation.” Advi­
sory Committee’s Notes on Fed. Rule Evid. 803(1), 28
U. S. C. App., p. 371 (describing the rationale for the
hearsay exception for “present sense impression[s]”). A
similar rationale applies to a “statement relating to a
startling event”—such as getting run off the road—“made
while the declarant was under the stress of excitement
that it caused.” Fed. Rule Evid. 803(2) (hearsay exception
for “excited utterances”). Unsurprisingly, 911 calls that
would otherwise be inadmissible hearsay have often been
admitted on those grounds. See D. Binder, Hearsay
Handbook §8.1, pp. 257–259 (4th ed. 2013–2014) (citing
cases admitting 911 calls as present sense impressions);
id., §9.1, at 274–275 (911 calls admitted as excited utter­
ances). There was no indication that the tip in J. L. (or
even in White) was contemporaneous with the observation
of criminal activity or made under the stress of excitement
caused by a startling event, but those considerations
weigh in favor of the caller’s veracity here.
                 Cite as: 572 U. S. ____ (2014)            7

                     Opinion of the Court

  Another indicator of veracity is the caller’s use of the
911 emergency system. See Brief for Respondent 40–41,
44; Brief for United States as Amicus Curiae 16–18. A 911
call has some features that allow for identifying and trac­
ing callers, and thus provide some safeguards against
making false reports with immunity. See J. L., supra, at
276 (KENNEDY, J., concurring). As this case illustrates,
see n. 1, supra, 911 calls can be recorded, which provides
victims with an opportunity to identify the false tipster’s
voice and subject him to prosecution, see, e.g., Cal. Penal
Code Ann. §653x (West 2010) (makes “telephon[ing] the
911 emergency line with the intent to annoy or harass”
punishable by imprisonment and fine); see also §148.3
(2014 West Cum. Supp.) (prohibits falsely reporting “that
an ‘emergency’ exists”); §148.5 (prohibits falsely reporting
“that a felony or misdemeanor has been committed”). The
911 system also permits law enforcement to verify im­
portant information about the caller. In 1998, the Federal
Communications Commission (FCC) began to require
cellular carriers to relay the caller’s phone number to 911
dispatchers. 47 CFR §20.18(d)(1) (2013) (FCC’s “Phase I
enhanced 911 services” requirements). Beginning in 2001,
carriers have been required to identify the caller’s geo­
graphic location with increasing specificity. §§20.18(e)–(h)
(“Phase II enhanced 911 service” requirements). And
although callers may ordinarily block call recipients from
obtaining their identifying information, FCC regulations
exempt 911 calls from that privilege.           §§64.1601(b),
(d)(4)(ii) (“911 emergency services” exemption from rule
that, when a caller so requests, “a carrier may not reveal
that caller’s number or name”). None of this is to suggest
that tips in 911 calls are per se reliable. Given the forego­
ing technological and regulatory developments, however, a
reasonable officer could conclude that a false tipster would
think twice before using such a system. The caller’s use of
the 911 system is therefore one of the relevant circum­
8               PRADO NAVARETTE v. CALIFORNIA

                          Opinion of the Court

stances that, taken together, justified the officer’s reliance
on the information reported in the 911 call.
                               C
   Even a reliable tip will justify an investigative stop only
if it creates reasonable suspicion that “criminal activity
may be afoot.” Terry, 392 U. S., at 30. We must therefore
determine whether the 911 caller’s report of being run off
the roadway created reasonable suspicion of an ongoing
crime such as drunk driving as opposed to an isolated
episode of past recklessness. See Cortez, 449 U. S., at 417
(“An investigatory stop must be justified by some objective
manifestation that the person stopped is, or is about to be,
engaged in criminal activity”). We conclude that the
behavior alleged by the 911 caller, “viewed from the
standpoint of an objectively reasonable police officer,
amount[s] to reasonable suspicion” of drunk driving.
Ornelas v. United States, 517 U. S. 690, 696 (1996). The
stop was therefore proper.2
   Reasonable suspicion depends on “ ‘ “the factual and
practical considerations of everyday life on which reason-
able and prudent men, not legal technicians, act.” ’ ” Id., at
695. Under that commonsense approach, we can appro­
priately recognize certain driving behaviors as sound
indicia of drunk driving. See, e.g., People v. Wells,
38 Cal. 4th 1078, 1081, 136 P. 3d 810, 811 (2006) (“ ‘weav­
ing all over the roadway’ ”); State v. Prendergast, 103 Haw.
451, 452–453, 83 P. 3d 714, 715–716 (2004) (“cross[ing]
over the center line” on a highway and “almost caus[ing]
several head-on collisions”); State v. Golotta, 178 N. J.
205, 209, 837 A. 2d 359, 361 (2003) (driving “ ‘all over
the road’ ” and “ ‘weaving back and forth’ ”); State v.
——————
    2 Becausewe conclude that the 911 call created reasonable suspicion
of an ongoing crime, we need not address under what circumstances a
stop is justified by the need to investigate completed criminal activity.
Cf. United States v. Hensley, 469 U. S. 221, 229 (1985).
                 Cite as: 572 U. S. ____ (2014)           9

                     Opinion of the Court

Walshire, 634 N. W. 2d 625, 626 (Iowa 2001) (“driving in
the median”). Indeed, the accumulated experience of
thousands of officers suggests that these sorts of erratic
behaviors are strongly correlated with drunk driving.
See Nat. Highway Traffic Safety Admin., The Visual
Detection of DWI Motorists 4–5 (Mar. 2010), online at
http://nhtsa.gov/staticfiles/nti/pdf/808677.pdf (as visited
Apr. 18, 2014, and available in Clerk of Court’s case file).
Of course, not all traffic infractions imply intoxication.
Unconfirmed reports of driving without a seatbelt or
slightly over the speed limit, for example, are so tenuously
connected to drunk driving that a stop on those grounds
alone would be constitutionally suspect. But a reliable tip
alleging the dangerous behaviors discussed above gener-
ally would justify a traffic stop on suspicion of drunk
driving.
   The 911 caller in this case reported more than a minor
traffic infraction and more than a conclusory allegation of
drunk or reckless driving. Instead, she alleged a specific
and dangerous result of the driver’s conduct: running
another car off the highway. That conduct bears too great
a resemblance to paradigmatic manifestations of drunk
driving to be dismissed as an isolated example of reckless­
ness. Running another vehicle off the road suggests lane­
positioning problems, decreased vigilance, impaired judg­
ment, or some combination of those recognized drunk
driving cues. See Visual Detection of DWI Motorists 4–5.
And the experience of many officers suggests that a driver
who almost strikes a vehicle or another object—the exact
scenario that ordinarily causes “running [another vehicle]
off the roadway”—is likely intoxicated. See id., at 5, 8.
As a result, we cannot say that the officer acted unreason­
ably under these circumstances in stopping a driver
whose alleged conduct was a significant indicator of drunk
driving.
   Petitioners’ attempts to second-guess the officer’s rea­
10           PRADO NAVARETTE v. CALIFORNIA

                      Opinion of the Court

sonable suspicion of drunk driving are unavailing. It is
true that the reported behavior might also be explained
by, for example, a driver responding to “an unruly child or
other distraction.” Brief for Petitioners 21. But we have
consistently recognized that reasonable suspicion “need
not rule out the possibility of innocent conduct.” United
States v. Arvizu, 534 U. S. 266, 277 (2002).
   Nor did the absence of additional suspicious conduct,
after the vehicle was first spotted by an officer, dispel the
reasonable suspicion of drunk driving. Brief for Petition­
ers 23–24. It is hardly surprising that the appearance of a
marked police car would inspire more careful driving for a
time. Cf. Arvizu, supra, at 275 (“ ‘[s]lowing down after
spotting a law enforcement vehicle’ ” does not dispel rea­
sonable suspicion of criminal activity). Extended observa­
tion of an allegedly drunk driver might eventually dispel a
reasonable suspicion of intoxication, but the 5-minute
period in this case hardly sufficed in that regard. Of
course, an officer who already has such a reasonable sus­
picion need not surveil a vehicle at length in order to
personally observe suspicious driving. See Adams v.
Williams, 407 U. S., at 147 (repudiating the argument
that “reasonable cause for a[n investigative stop] can only
be based on the officer’s personal observation”). Once
reasonable suspicion of drunk driving arises, “[t]he rea­
sonableness of the officer’s decision to stop a suspect does
not turn on the availability of less intrusive investigatory
techniques.” Sokolow, 490 U. S., at 11. This would be a
particularly inappropriate context to depart from that
settled rule, because allowing a drunk driver a second
chance for dangerous conduct could have disastrous
consequences.
                              III
  Like White, this is a “close case.” 496 U. S., at 332. As
in that case, the indicia of the 911 caller’s reliability here
                  Cite as: 572 U. S. ____ (2014)            11

                      Opinion of the Court

are stronger than those in J. L., where we held that a
bare-bones tip was unreliable. 529 U. S., at 271. Alt­
hough the indicia present here are different from those we
found sufficient in White, there is more than one way to
demonstrate “a particularized and objective basis for
suspecting the particular person stopped of criminal activ­
ity.” Cortez, 449 U. S., at 417–418. Under the totality of
the circumstances, we find the indicia of reliability in this
case sufficient to provide the officer with reasonable suspi­
cion that the driver of the reported vehicle had run another
vehicle off the road. That made it reasonable under the
circumstances for the officer to execute a traffic stop. We
accordingly affirm.
                                              It is so ordered.
                 Cite as: 572 U. S. ____ (2014)            1

                     SCALIA, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 12–9490
                         _________________


  LORENZO PRADO NAVARETTE AND JOSE PRADO 

    NAVARETTE, PETITIONERS v. CALIFORNIA 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF 

        CALIFORNIA, FIRST APPELLATE DISTRICT

                        [April 22, 2014]

   JUSTICE SCALIA, with whom JUSTICE GINSBURG,
JUSTICE SOTOMAYOR, and JUSTICE KAGAN join, dissenting.
   The California Court of Appeal in this case relied on
jurisprudence from the California Supreme Court (adopted
as well by other courts) to the effect that “an anonymous
and uncorroborated tip regarding a possibly intoxicated
highway driver” provides without more the reasonable
suspicion necessary to justify a stop. People v. Wells, 38
Cal. 4th l078, 1082, 136 P. 3d 810, 812, (2006). See also,
e.g., United States v. Wheat, 278 F. 3d 722, 729–730 (CA8
2001); State v. Walshire, 634 N. W. 2d 625, 626–627, 630
(Iowa 2001). Today’s opinion does not explicitly adopt
such a departure from our normal Fourth Amendment
requirement that anonymous tips must be corroborated; it
purports to adhere to our prior cases, such as Florida v.
J. L., 529 U. S. 266 (2000), and Alabama v. White, 496
U. S. 325 (1990). Be not deceived.
   Law enforcement agencies follow closely our judgments
on matters such as this, and they will identify at once our
new rule: So long as the caller identifies where the car is,
anonymous claims of a single instance of possibly careless
or reckless driving, called in to 911, will support a traffic
stop. This is not my concept, and I am sure would not be
the Framers’, of a people secure from unreasonable
searches and seizures. I would reverse the judgment of
2              PRADO NAVARETTE v. CALIFORNIA

                        SCALIA, J., dissenting

the Court of Appeal of California.
                                    I
    The California Highway Patrol in this case knew noth­
ing about the tipster on whose word—and that alone—
they seized Lorenzo and José Prado Navarette. They did
not know her name.1 They did not know her phone num­
ber or address. They did not even know where she called
from (she may have dialed in from a neighboring county,
App. 33a–34a).
    The tipster said the truck had “[run her] off the road­
way,” id., at 36a, but the police had no reason to credit
that charge and many reasons to doubt it, beginning with
the peculiar fact that the accusation was anonymous.
“[E]liminating accountability . . . is ordinarily the very
purpose of anonymity.”              McIntyre v. Ohio Elections
Comm’n, 514 U. S. 334, 385 (1995) (SCALIA, J., dissenting).
The unnamed tipster “can lie with impunity,” J. L., supra,
at 275 (KENNEDY, J., concurring). Anonymity is especially
suspicious with respect to the call that is the subject of the
present case. When does a victim complain to the police
about an arguably criminal act (running the victim off the
road) without giving his identity, so that he can accuse
and testify when the culprit is caught?
    The question before us, the Court agrees, ante, at 8, is
whether the “content of information possessed by police
and its degree of reliability,” White, 496 U. S., at 330, gave
the officers reasonable suspicion that the driver of the
truck (Lorenzo) was committing an ongoing crime. When
the only source of the government’s information is an
informant’s tip, we ask whether the tip bears sufficient
“ ‘indicia of reliability,’ ” id., at 328, to establish “a particu­
larized and objective basis for suspecting the particular
——————
  1 There was some indication below that the tipster was a woman. See

App. 18a. Beyond that detail, we must, as the Court notes, ante, at 2,
n. 1, assume that the identity of the tipster was unknown.
                 Cite as: 572 U. S. ____ (2014)            3

                     SCALIA, J., dissenting

person stopped of criminal activity,” United States v.
Cortez, 449 U. S. 411, 417–418 (1981).
   The most extreme case, before this one, in which an
anonymous tip was found to meet this standard was
White, supra. There the reliability of the tip was estab­
lished by the fact that it predicted the target’s behavior in
the finest detail—a detail that could be known only by
someone familiar with the target’s business: She would,
the tipster said, leave a particular apartment building, get
into a brown Plymouth station wagon with a broken right
tail light, and drive immediately to a particular motel.
Id., at 327. Very few persons would have such intimate
knowledge, and hence knowledge of the unobservable fact
that the woman was carrying unlawful drugs was plausi­
ble. Id., at 332. Here the Court makes a big deal of the
fact that the tipster was dead right about the fact that a
silver Ford F-150 truck (license plate 8D94925) was trav­
eling south on Highway 1 somewhere near mile marker
88. But everyone in the world who saw the car would have
that knowledge, and anyone who wanted the car stopped
would have to provide that information. Unlike the situa­
tion in White, that generally available knowledge in no
way makes it plausible that the tipster saw the car run
someone off the road.
   The Court says, ante, at 5, that “[b]y reporting that she
had been run off the road by a specific vehicle . . . the
caller necessarily claimed eyewitness knowledge.” So
what? The issue is not how she claimed to know, but
whether what she claimed to know was true. The claim to
“eyewitness knowledge” of being run off the road supports
not at all its veracity; nor does the amazing, mystifying
prediction (so far short of what existed in White) that the
petitioners’ truck would be heading south on Highway 1.
   The Court finds “reason to think” that the informant
“was telling the truth” in the fact that police observation
confirmed that the truck had been driving near the spot at
4             PRADO NAVARETTE v. CALIFORNIA

                      SCALIA, J., dissenting

which, and at the approximate time at which, the tipster
alleged she had been run off the road. Ante, at 6. Accord­
ing to the Court, the statement therefore qualifies as a
“ ‘present sense impression’ ” or “ ‘excited utterance,’ ” kinds
of hearsay that the law deems categorically admissible
given their low likelihood of reflecting “ ‘deliberate or
conscious misrepresentation.’ ” Ibid. (quoting Advisory
Committee’s Notes on Fed. Rule Evid. 803(1), 28 U. S. C.
App., p. 371). So, the Court says, we can fairly suppose
that the accusation was true.
   No, we cannot. To begin with, it is questionable whether
either the “present sense impression” or the “excited ut­
terance” exception to the hearsay rule applies here. The
classic “present sense impression” is the recounting of an
event that is occurring before the declarant’s eyes, as the
declarant is speaking (“I am watching the Hindenburg
explode!”). See 2 K. Broun, McCormick on Evidence 362
(7th ed. 2013) (hereinafter McCormick). And the classic
“excited utterance” is a statement elicited, almost involun­
tarily, by the shock of what the declarant is immediately
witnessing (“My God, those people will be killed!”). See
id., at 368–369. It is the immediacy that gives the state­
ment some credibility; the declarant has not had time to
dissemble or embellish. There is no such immediacy here.
The declarant had time to observe the license number of
the offending vehicle, 8D94925 (a difficult task if she was
forced off the road and the vehicle was speeding away), to
bring her car to a halt, to copy down the observed license
number (presumably), and (if she was using her own cell
phone) to dial a call to the police from the stopped car.
Plenty of time to dissemble or embellish.
   Moreover, even assuming that less than true immediacy
will suffice for these hearsay exceptions to apply, the
tipster’s statement would run into additional barriers to
admissibility and acceptance. According to the very Advi­
sory Committee’s Notes from which the Court quotes,
                 Cite as: 572 U. S. ____ (2014)            5

                     SCALIA, J., dissenting

cases addressing an unidentified declarant’s present sense
impression “indicate hesitancy in upholding the statement
alone as sufficient” proof of the reported event. 28 U. S. C.
App., at 371; see also 7 M. Graham, Handbook of Federal
Evidence 19–20 (7th ed. 2012). For excited utterances as
well, the “knotty theoretical” question of statement-alone
admissibility persists—seemingly even when the declarant
is known. 2 McCormick 368. “Some courts . . . have taken
the position that an excited utterance is admissible only if
other proof is presented which supports a finding of fact
that the exciting event did occur. The issue has not yet
been resolved under the Federal Rules.” Id., at 367–368
(footnote omitted). It is even unsettled whether excited
utterances of an unknown declarant are ever admissible.
A leading treatise reports that “the courts have been
reluctant to admit such statements, principally because of
uncertainty that foundational requirements, including the
impact of the event on the declarant, have been satisfied.”
Id., at 372. In sum, it is unlikely that the law of evidence
would deem the mystery caller in this case “especially
trustworthy,” ante, at 6.
   Finally, and least tenably, the Court says that another
“indicator of veracity” is the anonymous tipster’s mere
“use of the 911 emergency system,” ante, at 7. Because,
you see, recent “technological and regulatory develop­
ments” suggest that the identities of unnamed 911 callers
are increasingly less likely to remain unknown. Ibid.
Indeed, the systems are able to identify “the caller’s geo­
graphic location with increasing specificity.” Ibid. Amici
disagree with this, see Brief for National Association of
Criminal Defense Lawyers et al. 8–12, and the present
case surely suggests that amici are right—since we know
neither the identity of the tipster nor even the county from
which the call was made. But assuming the Court is right
about the ease of identifying 911 callers, it proves abso­
lutely nothing in the present case unless the anonymous
6               PRADO NAVARETTE v. CALIFORNIA

                          SCALIA, J., dissenting

caller was aware of that fact. “It is the tipster’s belief in
anonymity, not its reality, that will control his behavior.”
Id., at 10 (emphasis added). There is no reason to believe
that your average anonymous 911 tipster is aware that
911 callers are readily identifiable.2
                               II
   All that has been said up to now assumes that the anon­
ymous caller made, at least in effect, an accusation of
drunken driving. But in fact she did not. She said that
the petitioners’ truck “ ‘[r]an [me] off the roadway.’ ” App.
36a. That neither asserts that the driver was drunk nor
even raises the likelihood that the driver was drunk. The
most it conveys is that the truck did some apparently
nontypical thing that forced the tipster off the roadway,
whether partly or fully, temporarily or permanently. Who
really knows what (if anything) happened? The truck
might have swerved to avoid an animal, a pothole, or a
jaywalking pedestrian.
   But let us assume the worst of the many possibilities:
that it was a careless, reckless, or even intentional ma­
neuver that forced the tipster off the road. Lorenzo might
have been distracted by his use of a hands-free cell phone,
see Strayer, Drews, & Crouch, A Comparison of the Cell
Phone Driver and the Drunk Driver, 48 Human Factors 381,
388 (2006), or distracted by an intense sports argument with
José, see D. Strayer et al., AAA Foundation for Traffic
Safety, Measuring Cognitive Distraction in the Automobile
28 (June 2013), online at https://www.aaafoundation.org/
sites/default/files/MeasuringCognitiveDistractions.pdf as visited
Apr. 17, 2014, and available in Clerk of Court’s case file).
——————
   2 The Court’s discussion of reliable 911 traceability has so little rele­

vance to the present case that one must surmise it has been included
merely to assure officers in the future that anonymous 911 accusa­
tions—even untraced ones—are not as suspect (and hence as unrelia­
ble) as other anonymous accusations. That is unfortunate.
                     Cite as: 572 U. S. ____ (2014)                    7

                         SCALIA, J., dissenting

Or, indeed, he might have intentionally forced the tipster
off the road because of some personal animus, or hostility
to her “Make Love, Not War” bumper sticker. I fail to see
how reasonable suspicion of a discrete instance of irregular
or hazardous driving generates a reasonable suspicion of
ongoing intoxicated driving. What proportion of the hun­
dreds of thousands—perhaps millions—of careless, reck­
less, or intentional traffic violations committed each day is
attributable to drunken drivers? I say 0.1 percent. I have
no basis for that except my own guesswork. But unless
the Court has some basis in reality to believe that the
proportion is many orders of magnitude above that—say 1
in 10 or at least 1 in 20—it has no grounds for its unsup­
ported assertion that the tipster’s report in this case gave
rise to a reasonable suspicion of drunken driving.
   Bear in mind that that is the only basis for the stop that
has been asserted in this litigation.3 The stop required
suspicion of an ongoing crime, not merely suspicion of
having run someone off the road earlier. And driving
while being a careless or reckless person, unlike driving
while being a drunk person, is not an ongoing crime. In
other words, in order to stop the petitioners the officers
here not only had to assume without basis the accuracy of
the anonymous accusation but also had to posit an unlikely
reason (drunkenness) for the accused behavior.
   In sum, at the moment the police spotted the truck, it
was more than merely “possib[le]” that the petitioners
were not committing an ongoing traffic crime. United
States v. Arvizu, 534 U. S. 266, 277 (2002) (emphasis
——————
  3 The circumstances that may justify a stop under Terry v. Ohio, 392

U. S. 1 (1968), to investigate past criminal activity are far from clear,
see United States v. Hensley, 469 U. S. 221, 229 (1985), and have not
been discussed in this litigation. Hence, the Court says it “need not
address” that question. Ante, at 8, n. 2. I need not either. This case
has been litigated on the assumption that only suspicion of ongoing
intoxicated or reckless driving could have supported this stop.
8            PRADO NAVARETTE v. CALIFORNIA

                     SCALIA, J., dissenting

added). It was overwhelmingly likely that they were not.
                              III
   It gets worse. Not only, it turns out, did the police have
no good reason at first to believe that Lorenzo was driving
drunk, they had very good reason at last to know that he
was not. The Court concludes that the tip, plus confirma­
tion of the truck’s location, produced reasonable suspicion
that the truck not only had been but still was barreling
dangerously and drunkenly down Highway 1. Ante, at 8–
10. In fact, alas, it was not, and the officers knew it. They
followed the truck for five minutes, presumably to see if it
was being operated recklessly. And that was good police
work. While the anonymous tip was not enough to sup­
port a stop for drunken driving under Terry v. Ohio, 392
U. S. 1 (1968), it was surely enough to counsel observation
of the truck to see if it was driven by a drunken driver.
But the pesky little detail left out of the Court’s reason-
able-suspicion equation is that, for the five minutes that the
truck was being followed (five minutes is a long time),
Lorenzo’s driving was irreproachable. Had the officers
witnessed the petitioners violate a single traffic law, they
would have had cause to stop the truck, Whren v. United
States, 517 U. S. 806, 810 (1996), and this case would not
be before us. And not only was the driving irreproachable,
but the State offers no evidence to suggest that the peti­
tioners even did anything suspicious, such as suddenly
slowing down, pulling off to the side of the road, or turning
somewhere to see whether they were being followed. Cf.
Arvizu, supra, at 270–271, 277 (concluding that an officer’s
suspicion of criminality was enhanced when the driver,
upon seeing that he was being followed, “slowed dramati­
cally,” “appeared stiff,” and “seemed to be trying to pre­
tend” that the patrol car was not there). Consequently,
the tip’s suggestion of ongoing drunken driving (if it could
be deemed to suggest that) not only went uncorroborated;
                 Cite as: 572 U. S. ____ (2014)            9

                     SCALIA, J., dissenting

it was affirmatively undermined.
   A hypothetical variation on the facts of this case illus­
trates the point. Suppose an anonymous tipster reports
that, while following near mile marker 88 a silver Ford
F-150, license plate 8D949925, traveling southbound on
Highway 1, she saw in the truck’s open cab several five­
foot-tall stacks of what was unmistakably baled cannabis.
Two minutes later, a highway patrolman spots the truck
exactly where the tip suggested it would be, begins follow­
ing it, but sees nothing in the truck’s cab. It is not enough
to say that the officer’s observation merely failed to cor­
roborate the tipster’s accusation. It is more precise to say
that the officer’s observation discredited the informant’s
accusation: The crime was supposedly occurring (and
would continue to occur) in plain view, but the police saw
nothing. Similarly, here, the crime supposedly suggested
by the tip was ongoing intoxicated driving, the hallmarks
of which are many, readily identifiable, and difficult to
conceal. That the officers witnessed nary a minor traffic
violation nor any other “sound indici[um] of drunk driv­
ing,” ante, at 8, strongly suggests that the suspected crime
was not occurring after all. The tip’s implication of con­
tinuing criminality, already weak, grew even weaker.
   Resisting this line of reasoning, the Court curiously
asserts that, since drunk drivers who see marked squad
cars in their rearview mirrors may evade detection simply
by driving “more careful[ly],” the “absence of additional
suspicious conduct” is “hardly surprising” and thus largely
irrelevant. Ante, at 10. Whether a drunk driver drives
drunkenly, the Court seems to think, is up to him. That is
not how I understand the influence of alcohol. I subscribe
to the more traditional view that the dangers of intoxi-
cated driving are the intoxicant’s impairing effects on the
body—effects that no mere act of the will can resist. See,
e.g., A. Dasgupta, The Science of Drinking: How Alcohol
Affects Your Body and Mind 39 (explaining that the physi­
10           PRADO NAVARETTE v. CALIFORNIA

                     SCALIA, J., dissenting

ological effect of a blood alcohol content between 0.08 and
0.109, for example, is “sever[e] impair[ment]” of “[b]alance,
speech, hearing, and reaction time,” as well as one’s gen­
eral “ability to drive a motor vehicle”). Consistent with
this view, I take it as a fundamental premise of our intoxi­
cated-driving laws that a driver soused enough to swerve
once can be expected to swerve again—and soon. If he
does not, and if the only evidence of his first episode of
irregular driving is a mere inference from an uncorrobo­
rated, vague, and nameless tip, then the Fourth Amend­
ment requires that he be left alone.
                         *    *     *
  The Court’s opinion serves up a freedom-destroying
cocktail consisting of two parts patent falsity: (1) that
anonymous 911 reports of traffic violations are reliable so
long as they correctly identify a car and its location, and
(2) that a single instance of careless or reckless driving
necessarily supports a reasonable suspicion of drunken­
ness. All the malevolent 911 caller need do is assert a
traffic violation, and the targeted car will be stopped,
forcibly if necessary, by the police. If the driver turns out
not to be drunk (which will almost always be the case), the
caller need fear no consequences, even if 911 knows his
identity. After all, he never alleged drunkenness, but
merely called in a traffic violation—and on that point his
word is as good as his victim’s.
  Drunken driving is a serious matter, but so is the loss of
our freedom to come and go as we please without police
interference. To prevent and detect murder we do not
allow searches without probable cause or targeted Terry
stops without reasonable suspicion. We should not do so
for drunken driving either. After today’s opinion all of us
on the road, and not just drug dealers, are at risk of hav­
ing our freedom of movement curtailed on suspicion of
drunkenness, based upon a phone tip, true or false, of a
                  Cite as: 572 U. S. ____ (2014)           11

                      SCALIA, J., dissenting

single instance of careless driving. I respectfully dissent.

```

---

## GROUP: content/cases/Neil v. Biggers.md  (`case`, 5 assertions)

### content_page

```
---
title: "Neil v. Biggers"
type: case
citation: "409 U.S. 188 (1972)"
parallel_cite: "93 S. Ct. 375; 34 L. Ed. 2d 401"
neutral_cite: 1972 U.S. LEXIS 6
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-12-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-12-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Neil v. Biggers
  varies_by_point: false
  scope_note: "Source of the five reliability factors; carried forward in Manson v. Brathwaite; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108639/neil-v-biggers/"
  cluster_id: 108639
  opinion_id: 108639
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny / Refinement"
related: ["[[Manson v. Brathwaite]]", "[[Stovall v. Denno]]", "[[Perry v. New Hampshire]]", "[[United States v. Wade]]"]
aliases: []
tags: ["case", "due-process", "eyewitness-identification", "reliability", "showup"]
holding: "Even an unnecessarily suggestive identification is admissible if, under the totality of the circumstances, it is nonetheless reliable;…"
lake:
  record_id: Neil v. Biggers
  status: verified
  projected_at: 2026-07-06
---

# Neil v. Biggers

*409 U.S. 188 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A rape victim identified Biggers at a station-house showup seven months after the crime, after viewing him and hearing him repeat words spoken by her attacker. During the crime she had had a prolonged opportunity to observe the assailant under light from the moon and a kitchen light. Biggers challenged the identification as the product of an unnecessarily suggestive showup.

## Issue
Whether an identification produced by an unnecessarily suggestive procedure must be excluded, or whether it may be admitted if it is reliable under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Rule
Reliability, not suggestiveness alone, controls admissibility. "[T]he central question [is] whether under the 'totality of the circumstances' the identification was reliable even though the confrontation procedure was suggestive." — 409 U.S. at 199. ^pin-199

"[T]he factors to be considered in evaluating the likelihood of misidentification include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of the witness' prior description of the criminal, the level of certainty demonstrated by the witness at the confrontation, and the length of time between the crime and the confrontation." — *Id.* at 199–200. ^pin-199b

## Application
Applying those factors, the victim had had an extended opportunity to view her assailant, had paid close attention, had given an accurate prior description, and was certain in her identification; although seven months had passed, she had made no prior misidentification. Under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], her identification was sufficiently reliable to be admitted despite the suggestive showup.

## Conclusion
The identification was reliable and admissible; the judgment granting relief on the identification claim was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The five *Biggers* reliability factors were carried forward and made the governing test for suggestive identifications in [[Manson v. Brathwaite]].

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny / Refinement*

## Sources
- *Neil v. Biggers*, 409 U.S. 188 (1972) — https://www.courtlistener.com/opinion/108639/neil-v-biggers/ — pinpoints: 199, 199–200.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2532fe426052a941", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "409 U.S. 188 (1972)", "court": "U.S. Supreme Court", "neutral_cite": "1972 U.S. LEXIS 6", "official_citation_present": true, "parallel_cite": "93 S. Ct. 375; 34 L. Ed. 2d 401", "title": "Neil v. Biggers", "year": "1972"}}
{"assertion_id": "23791a56388ce430", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Progeny / Refinement", "title": "Neil v. Biggers"}}
{"assertion_id": "bcbcf45f56b4d9b5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Even an unnecessarily suggestive identification is admissible if, under the totality of the circumstances, it is nonetheless reliable;…", "title": "Neil v. Biggers"}}
{"assertion_id": "1739212335f3eeb5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1972-12-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Neil v. Biggers", "field_i_validity": "good_law", "scope_note": "Source of the five reliability factors; carried forward in Manson v. Brathwaite; good law.", "title": "Neil v. Biggers", "varies_by_point": "false"}}
{"assertion_id": "7fd3c9dabe985fff", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Neil v. Biggers"}}
```

### lake record — Neil v. Biggers

```json
{
  "schema_version": "s2.v1",
  "record_id": "Neil v. Biggers",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Neil v. Biggers",
    "case_name_short": "Neil",
    "case_name_full": "Neil, Warden v. Biggers",
    "input_case_name": "Neil v. Biggers",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-12-06",
    "year": 1972,
    "docket": null,
    "cluster_id": 108639,
    "lead_opinion_id": 108639,
    "sibling_ids": [
      108639,
      9425063,
      9425064
    ],
    "absolute_url": "/opinion/108639/neil-v-biggers/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8987110,
        "score": 20,
        "case_name": "Neil v. Biggers"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "409 U.S. 188",
      "volume": "409",
      "reporter": "U.S.",
      "page": "188",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 375",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "34 L. Ed. 2d 401",
        "volume": "34",
        "reporter": "L. Ed. 2d",
        "page": "401",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 6",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "409 U.S. 188",
        "volume": "409",
        "reporter": "U.S.",
        "page": "188",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 375",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "34 L. Ed. 2d 401",
        "volume": "34",
        "reporter": "L. Ed. 2d",
        "page": "401",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 6",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "409 U.S. 188",
    "official_selection": {
      "court_class": "scotus",
      "selected": "409 U.S. 188",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-199",
      "page": null,
      "quote": "--- # Neil v. Biggers *409 U.S. 188 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A rape victim identified Biggers at a station-house showup seven months after the crime, after viewing him and hearing him repeat words spoken by her attacker. During the crime she had had a prolonged opportunity to observe the assailant under light from the moon and a kitchen light. Biggers challenged the identification as the product of an unnecessarily suggestive showup. ## Issue Whether an identification produced by an unnecessarily suggestive procedure must be excluded, or whether it may be admitted if it is reliable under the totality of the circumstances. ## Rule Reliability, not suggestiveness alone, controls admissibility.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-199b",
      "page": null,
      "quote": "[T]he factors to be considered in evaluating the likelihood of misidentification include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of the witness' prior description of the criminal, the level of certainty demonstrated by the witness at the confrontation, and the length of time between the crime and the confrontation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-12-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Neil v. Biggers",
    "varies_by_point": false,
    "scope_note": "Source of the five reliability factors; carried forward in Manson v. Brathwaite; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tappia Green",
          "cluster_id": 9409950,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Traynham v. State",
          "cluster_id": 10021058,
          "cite": [
            "243 Md. App. 717"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Myers v. State",
          "cluster_id": 10021078,
          "cite": [
            "243 Md. App. 154"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tibbs v. Florida",
          "cluster_id": 110731,
          "cite": [
            "72 L. Ed. 2d 652",
            "102 S. Ct. 2211",
            "457 U.S. 31",
            "1982 U.S. LEXIS 116",
            "50 U.S.L.W. 4607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Williams",
          "cluster_id": 109438,
          "cite": [
            "48 L. Ed. 2d 126",
            "96 S. Ct. 1691",
            "425 U.S. 501",
            "1976 U.S. LEXIS 50"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sumner v. Mata",
          "cluster_id": 110382,
          "cite": [
            "66 L. Ed. 2d 722",
            "101 S. Ct. 764",
            "449 U.S. 539",
            "1981 U.S. LEXIS 62",
            "49 U.S.L.W. 4133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Piatkowski",
          "cluster_id": 2206245,
          "cite": [
            "870 N.E.2d 403",
            "225 Ill. 2d 551",
            "312 Ill. Dec. 338",
            "2007 Ill. LEXIS 857"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Exxon Shipping Co. v. Baker",
          "cluster_id": 145779,
          "cite": [
            "128 S. Ct. 2605",
            "554 U.S. 471"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Reid",
          "cluster_id": 1636806,
          "cite": [
            "91 S.W.3d 247"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
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
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Owens",
          "cluster_id": 111992,
          "cite": [
            "98 L. Ed. 2d 951",
            "108 S. Ct. 838",
            "484 U.S. 554",
            "1988 U.S. LEXIS 940",
            "56 U.S.L.W. 4160"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. State",
          "cluster_id": 1743700,
          "cite": [
            "937 S.W.2d 479",
            "1996 WL 724669"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trans World Airlines, Inc. v. Hardison",
          "cluster_id": 109692,
          "cite": [
            "53 L. Ed. 2d 113",
            "97 S. Ct. 2264",
            "432 U.S. 63",
            "1977 U.S. LEXIS 115",
            "14 Empl. Prac. Dec. (CCH) 7620",
            "14 Fair Empl. Prac. Cas. (BNA) 1697"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rutledge v. United States",
          "cluster_id": 118013,
          "cite": [
            "134 L. Ed. 2d 419",
            "116 S. Ct. 1241",
            "517 U.S. 292",
            "1996 U.S. LEXIS 2163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDaniel v. Brown",
          "cluster_id": 1750,
          "cite": [
            "175 L. Ed. 2d 582",
            "130 S. Ct. 665",
            "558 U.S. 120",
            "2010 U.S. LEXIS 3"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gimmy v. People",
          "cluster_id": 1231296,
          "cite": [
            "645 P.2d 262",
            "1982 Colo. LEXIS 568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sumner v. Mata",
          "cluster_id": 110667,
          "cite": [
            "71 L. Ed. 2d 480",
            "102 S. Ct. 1303",
            "455 U.S. 591",
            "1982 U.S. LEXIS 83",
            "50 U.S.L.W. 3760"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Malloy",
          "cluster_id": 5685415,
          "cite": [
            "55 N.Y.2d 296",
            "434 N.E.2d 237",
            "449 N.Y.S.2d 168",
            "1982 N.Y. LEXIS 3140"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schevers",
          "cluster_id": 1191968,
          "cite": [
            "979 P.2d 659",
            "132 Idaho 786",
            "1999 Ida. App. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 109757,
          "cite": [
            "54 L. Ed. 2d 424",
            "98 S. Ct. 458",
            "434 U.S. 220",
            "1977 U.S. LEXIS 163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Neil v. Biggers:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108639 OR 9425063 OR 9425064) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTY5NDU2MDAwMDAwJnM9NDY2NDc1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108639+OR+9425063+OR+9425064%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(108639 OR 9425063 OR 9425064)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MDImcz0yMDc3MTc4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108639+OR+9425063+OR+9425064%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108639 OR 9425063 OR 9425064)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 0,
        "triage_snippet_classified": 69
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108639 OR 9425063 OR 9425064)",
    "indexed_citing_opinions": 4347,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108639,
        "count": 3947,
        "count_source": "search"
      },
      {
        "opinion_id": 9425063,
        "count": 458,
        "count_source": "search"
      },
      {
        "opinion_id": 9425064,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7060,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/neil-v-biggers.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNTAzNTQmcz0xMDMwNzE1MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108639+OR+9425063+OR+9425064%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108639,
        "cited_id": 85455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 85481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 87987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 94988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 98883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 100433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 100923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 101908,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 104451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 104591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 104726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 106109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 106328,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 107893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 284140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 291028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 298978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 303254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108639,
        "cited_id": 1493381,
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
    "date_created": "2026-07-05T15:14:05Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:14:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:24:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:28:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:24:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Neil v. Biggers

```
<div>
<center><b><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188</a></span> (1972)</b></center>
<center><h1>NEIL, WARDEN<br>
v.<br>
BIGGERS.</h1></center>
<center>No. 71-586.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 18-19, 1972.</center>
<center>Decided December 6, 1972.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*189</span> <i>Bart C. Durham III,</i> Assistant Attorney General of Tennessee, argued the cause for petitioner. With him on the brief was <i>David M. Pack,</i> Attorney General.</p>
<p><i>Michael Meltsner</i> argued the cause for respondent. With him on the brief were <i>Jack Greenberg, Anthony G. Amsterdam, Avon N. Williams, Jr.,</i> and <i>Z. Alexander Looby.</i></p>
<p><i>Louis J. Lefkowitz,</i> Attorney General of New York, <i>pro se, Samuel A. Hirshowitz,</i> First Assistant Attorney General, and <i>Maria L. Marcus,</i> Assistant Attorney General, filed a brief for the Attorney General of New York as <i>amicus curiae</i> urging reversal.</p>
<p><i>Shirley Fingerhood, Richard G. Green, Burt Neuborne,</i> and <i>Melvin L. Wulf</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging affirmance.</p>
<p>MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>In 1965, after a jury trial in a Tennessee court, respondent was convicted of rape and was sentenced to 20 years' imprisonment. The State's evidence consisted in part of testimony concerning a station-house identification of respondent by the victim. The Tennessee Supreme Court affirmed. <i>Biggers</i> v. <i>State,</i> <span class="citation" data-id="1493381"><a href="/opinion/1493381/biggers-v-state/" aria-description="Citation for case: Biggers v. State">219 Tenn. 553</a></span>, <span class="citation" data-id="1493381"><a href="/opinion/1493381/biggers-v-state/" aria-description="Citation for case: Biggers v. State">411 S. W. 2d 696</a></span> (1967). On certiorari, the judgment of the Tennessee Supreme Court was affirmed by an equally divided Court. <i>Biggers</i> v. <i>Tennessee,</i> <span class="citation" data-id="9423641"><a href="/opinion/107638/biggers-v-tennessee/" aria-description="Citation for case: Biggers v. Tennessee">390 U. S. 404</a></span> (1968) (MARSHALL, J., not participating). Respondent then brought a federal habeas corpus action raising several claims. In reply, <span class="star-pagination">*190</span> petitioner contended that the claims were barred by <span class="citation no-link">28 U. S. C. § 2244</span> (c), which provides in pertinent part:</p>
<blockquote>"In a habeas corpus proceeding brought in behalf of a person in custody pursuant to the judgment of a State court, a prior judgment of the Supreme Court of the United States on an appeal or review by a writ of certiorari at the instance of the prisoner of the decision of such State court, shall be conclusive as to all issues of fact or law with respect to an asserted denial of a Federal right which constitutes ground for discharge in a habeas corpus proceeding, actually adjudicated by the Supreme Court therein. . . ."</blockquote>
<p>The District Court held that the claims were not barred and, after a hearing, held in an unreported opinion that the station-house identification procedure was so suggestive as to violate due process. The Court of Appeals affirmed. <span class="citation" data-id="9457324"><a href="/opinion/298978/archie-nathaniel-biggers-v-william-s-neil-warden-tennessee-state/" aria-description="Citation for case: Archie Nathaniel Biggers v. William S. Neil, Warden,...">448 F. 2d 91</a></span> (1971). We granted certiorari to decide whether an affirmance by an equally divided Court is an actual adjudication barring subsequent consideration on habeas corpus, and, if not, whether the identification procedure violated due process. <span class="citation multiple-matches"><a href="/c/U.%20S./405/954/">405 U. S. 954</a></span> (1972).</p>
<p></p>
<h2>I</h2>
<p>The intended scope of the phrase "actually adjudicated by the Supreme Court" must be determined by reference to the peculiarities of federal court jurisdiction and the context in which § 2244 (c) was enacted. Jurisdiction to hear state prisoner claims on habeas corpus was first expressly conferred on the federal courts by the Judiciary Act of 1867, c. 28, <span class="citation no-link">14 Stat. 385</span>. Thereafter, decisions of this Court established not only that <i>res judicata</i> was inapplicable, <i>e. g., </i><i>Salinger</i> v. <i>Loisel,</i> <span class="citation" data-id="100433"><a href="/opinion/100433/salinger-v-loisel/#230" aria-description="Citation for case: Salinger v. Loisel">265 U. S. 224, 230</a></span> (1924); <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">372 U. S. 391</a></span>, 423 <span class="star-pagination">*191</span> (1963), but also that federal courts were obliged in appropriate cases to redetermine issues of fact and federal law. By the same token, the Court developed a number of limiting principles to restrain open-ended relitigation, among them that a successive habeas corpus application raising grounds rejected in a previous application might be denied without reaching the merits. <i>Salinger</i> v. <span class="citation" data-id="100433"><a href="/opinion/100433/salinger-v-loisel/#231" aria-description="Citation for case: Salinger v. Loisel"><i>Loisel, supra,</i> at 231</a></span>.</p>
<p>In 1948, Congress codified a version of the <i><span class="citation" data-id="100433"><a href="/opinion/100433/salinger-v-loisel/" aria-description="Citation for case: Salinger v. Loisel">Salinger</a></span></i> rule in <span class="citation no-link">28 U. S. C. § 2244</span>. As redesignated and amended in 1966, § 2244 (b) shields against senseless repetition of claims by state prisoners without endangering the principle that each is entitled, other limitations aside, to a redetermination of his federal claims by a federal court on habeas corpus. With this in mind, the purpose of § 2244 (c), also enacted in 1966, becomes clear. This subsection embodies a recognition that if this Court has "actually adjudicated" a claim on direct appeal or certiorari, a state prisoner has had the federal redetermination to which he is entitled. A subsequent application for habeas corpus raising the same claims would serve no valid purpose and would add unnecessarily to an already overburdened system of criminal justice.<sup>[1]</sup></p>
<p>In this light, we review our cases explicating the disposition "affirmed by an equally divided Court." On what was apparently the first occasion of an equal division, <span class="star-pagination">*192</span> <i>The Antelope,</i> <span class="citation" data-id="85455"><a href="/opinion/85455/the-antelope/" aria-description="Citation for case: The Antelope">10 Wheat. 66</a></span> (1825), the Court simply affirmed on the point of division without much discussion. <span class="citation" data-id="85455"><a href="/opinion/85455/the-antelope/#126" aria-description="Citation for case: The Antelope"><i>Id.,</i> at 126-127</a></span>. Faced with a similar division during the next Term, the Court again affirmed, Chief Justice Marshall explaining that "the principles of law which have been argued, cannot be settled; but the judgment is affirmed, the court being divided in opinion upon it." <i>Etting</i> v. <i>Bank of the United States,</i> <span class="citation" data-id="85481"><a href="/opinion/85481/etting-v-bank-of-united-states/#78" aria-description="Citation for case: Etting v. Bank of United States">11 Wheat. 59, 78</a></span> (1826). As was later elaborated, in such cases it is the appellant or petitioner who asks the Court to overturn a lower court's decree.</p>
<blockquote>"If the judges are divided, the reversal cannot be had, for no order can be made. The judgment of the court below, therefore, stands in full force. It is, indeed, the settled practice in such case to enter a judgment of affirmance; but this is only the most convenient mode of expressing the fact that the cause is finally disposed of in conformity with the action of the court below, and that that court can proceed to enforce its judgment. The legal effect would be the same if the appeal, or writ of error, were dismissed." <i>Durant</i> v. <i>Essex Co.,</i> <span class="citation" data-id="87987"><a href="/opinion/87987/durant-v-essex-co/#112" aria-description="Citation for case: Durant v. Essex Co.">7 Wall. 107, 112</a></span> (1869).</blockquote>
<p>Nor is an affirmance by an equally divided Court entitled to precedential weight. <i>Ohio ex rel. Eaton</i> v. <i>Price,</i> <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/#264" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263, 264</a></span> (1960). We decline to construe § 2244 (c)'s bar as extending to claims on which the judgment of a state court stands because of the absence of a majority position in this Court, and accordingly conclude that the courts below properly reached the merits.<sup>[2]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*193</span> II</h2>
<p>We proceed, then, to consider respondent's due process claim.<sup>[3]</sup> As the claim turns upon the facts, we must first review the relevant testimony at the jury trial and at the habeas corpus hearing regarding the rape and the identification. The victim testified at trial that on the evening of January 22, 1965, a youth with a butcher knife grabbed her in the doorway to her kitchen:</p>
<blockquote>"A. [H]e grabbed me from behind, and grappled twisted me on the floor. Threw me down on the floor.</blockquote>
<blockquote>"Q. And there was no light in that kitchen?</blockquote>
<blockquote>
<span class="star-pagination">*194</span> "A. Not in the kitchen.</blockquote>
<blockquote>"Q. So you couldn't have seen him then?</blockquote>
<blockquote>"A. Yes, I could see him, when I looked up in his face.</blockquote>
<blockquote>"Q. In the dark?</blockquote>
<blockquote>"A. He was right in the doorwayit was enough light from the bedroom shining through. Yes, I could see who he was.</blockquote>
<blockquote>"Q. You could see? No light? And you could see him and know him then?</blockquote>
<blockquote>"A. Yes." Tr. of Rec. in No. 237, O. T. 1967, pp. 33-34.</blockquote>
<p>When the victim screamed, her 12-year-old daughter came out of her bedroom and also began to scream. The assailant directed the victim to "tell her [the daughter] to shut up, or I'll kill you both." She did so, and was then walked at knifepoint about two blocks along a railroad track, taken into a woods, and raped there. She testified that "the moon was shining brightly, full moon." After the rape, the assailant ran off, and she returned home, the whole incident having taken between 15 minutes and half an hour.</p>
<p>She then gave the police what the Federal District Court characterized as "only a very general description," describing him as "being fat and flabby with smooth skin, bushy hair and a youthful voice." Additionally, though not mentioned by the District Court, she testified at the habeas corpus hearing that she had described her assailant as being between 16 and 18 years old and between five feet ten inches and six feet tall, as weighing between 180 and 200 pounds, and as having a dark brown complexion. This testimony was substantially corroborated by that of a police officer who was testifying from his notes.</p>
<p>On several occasions over the course of the next seven months, she viewed suspects in her home or at the police <span class="star-pagination">*195</span> station, some in lineups and others in showups, and was shown between 30 and 40 photographs. She told the police that a man pictured in one of the photographs had features similar to those of her assailant, but identified none of the suspects. On August 17, the police called her to the station to view respondent, who was being detained on another charge. In an effort to construct a suitable lineup, the police checked the city jail and the city juvenile home. Finding no one at either place fitting respondent's unusual physical description, they conducted a showup instead.</p>
<p>The showup itself consisted of two detectives walking respondent past the victim. At the victim's request, the police directed respondent to say "shut up or I'll kill you." The testimony at trial was not altogether clear as to whether the victim first identified him and then asked that he repeat the words or made her identification after he had spoken.<sup>[4]</sup> In any event, the victim testified that she had "no doubt" about her identification. At the habeas corpus hearing, she elaborated in response to questioning.</p>
<blockquote>"A. That I have no doubt, I mean that I am sure that when Isee, when I first laid eyes on him, I <span class="star-pagination">*196</span> knew that it was the individual, because his face well, there was just something that I don't think I could ever forget. I believe_____</blockquote>
<blockquote>"Q. You say when you first laid eyes on him, which time are you referring to?</blockquote>
<blockquote>"A. When I identified himwhen I seen him in the courthouse when I was took up to view the suspect." App. 127.</blockquote>
<p>We must decide whether, as the courts below held, this identification and the circumstances surrounding it failed to comport with due process requirements.</p>
<p></p>
<h2>III</h2>
<p>We have considered on four occasions the scope of due process protection against the admission of evidence deriving from suggestive identification procedures. In <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967), the Court held that the defendant could claim that "the confrontation conducted . . . was so unnecessarily suggestive and conducive to irreparable mistaken identification that he was denied due process of law." <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#301" aria-description="Citation for case: Stovall v. Denno"><i>Id.,</i> at 301-302</a></span>. This, we held, must be determined "on the totality of the circumstances." We went on to find that on the facts of the case then before us, due process was not violated, emphasizing that the critical condition of the injured witness justified a showup in her hospital room. At trial, the witness, whose view of the suspect at the time of the crime was brief, testified to the out-of-court identification, as did several police officers present in her hospital room, and also made an in-court identification.</p>
<p>Subsequently, in a case where the witnesses made in-court identifications arguably stemming from previous exposure to a suggestive photographic array, the Court restated the governing test:</p>
<blockquote>"[W]e hold that each case must be considered on its own facts, and that convictions based on eyewitness <span class="star-pagination">*197</span> identification at trial following a pretrial identification by photograph will be set aside on that ground only if the photographic identification procedure was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification." <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 384</a></span> (1968).</blockquote>
<p>Again we found the identification procedure to be supportable, relying both on the need for prompt utilization of other investigative leads and on the likelihood that the photographic identifications were reliable, the witnesses having viewed the bank robbers for periods of up to five minutes under good lighting conditions at the time of the robbery.</p>
<p>The only case to date in which this Court has found identification procedures to be violative of due process is <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#442" aria-description="Citation for case: Foster v. California">394 U. S. 440, 442</a></span> (1969). There, the witness failed to identify Foster the first time he confronted him, despite a suggestive lineup. The police then arranged a showup, at which the witness could make only a tentative identification. Ultimately, at yet another confrontation, this time a lineup, the witness was able to muster a definite identification. We held all of the identifications inadmissible, observing that the identifications were "all but inevitable" under the circumstances. <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#443" aria-description="Citation for case: Foster v. California"><i>Id.,</i> at 443</a></span>.</p>
<p>In the most recent case of <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), we held admissible an in-court identification by a witness who had a fleeting but "real good look" at his assailant in the headlights of a passing car. The witness testified at a pretrial suppression hearing that he identified one of the petitioners among the participants in the lineup before the police placed the participants in a formal line. MR. JUSTICE BRENNAN for four members of the Court stated that this evidence could support a finding that the in-court identification was <span class="star-pagination">*198</span> "entirely based upon observations at the time of the assault and not at all induced by the conduct of the lineup." <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#5" aria-description="Citation for case: Coleman v. Alabama"><i>Id.,</i> at 5-6</a></span>.</p>
<p>Some general guidelines emerge from these cases as to the relationship between suggestiveness and misidentification. It is, first of all, apparent that the primary evil to be avoided is "a very substantial likelihood of irreparable misidentification." <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>. While the phrase was coined as a standard for determining whether an in-court identification would be admissible in the wake of a suggestive out-of-court identification, with the deletion of "irreparable" it serves equally well as a standard for the admissibility of testimony concerning the out-of-court identification itself.<sup>[5]</sup> It is the likelihood of misidentification which violates a defendant's right to due process, and it is this which was the basis of the exclusion of evidence in <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span>.</i> Suggestive confrontations are disapproved because they increase the likelihood of misidentification, and unnecessarily suggestive ones are condemned for the further reason that the increased chance of misidentification is gratuitous. But as <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> makes clear, the admission of evidence of a showup without more does not violate due process.</p>
<p>What is less clear from our cases is whether, as intimated by the District Court, unnecessary suggestiveness <span class="star-pagination">*199</span> alone requires the exclusion of evidence.<sup>[6]</sup> While we are inclined to agree with the courts below that the police did not exhaust all possibilities in seeking persons physically comparable to respondent, we do not think that the evidence must therefore be excluded. The purpose of a strict rule barring evidence of unnecessarily suggestive confrontations would be to deter the police from using a less reliable procedure where a more reliable one may be available, and would not be based on the assumption that in every instance the admission of evidence of such a confrontation offends due process. <i>Clemons</i> v. <i>United States,</i> 133 U. S. App. D. C. 27, 48, <span class="citation" data-id="9454404"><a href="/opinion/284140/malcus-t-clemons-v-united-states-of-america-david-e-clark-v-united/#1251" aria-description="Citation for case: Malcus T. Clemons v. United States of America, David E....">408 F. 2d 1230, 1251</a></span> (1968) (Leventhal, J., concurring); cf. <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 273</a></span> (1967); <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). Such a rule would have no place in the present case, since both the confrontation and the trial preceded <i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>,</i> when we first gave notice that the suggestiveness of confrontation procedures was anything other than a matter to be argued to the jury.</p>
<p>We turn, then, to the central question, whether under the "totality of the circumstances" the identification was reliable even though the confrontation procedure was suggestive. As indicated by our cases, the factors to be considered in evaluating the likelihood of misidentification include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of the witness' prior description of the criminal, the level of certainty demonstrated by the witness at the confrontation, and the length of time <span class="star-pagination">*200</span> between the crime and the confrontation. Applying these factors, we disagree with the District Court's conclusion.</p>
<p>In part, as discussed above, we think the District Court focused unduly on the relative reliability of a lineup as opposed to a showup, the issue on which expert testimony was taken at the evidentiary hearing. It must be kept in mind also that the trial was conducted before <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and that therefore the incentive was lacking for the parties to make a record at trial of facts corroborating or undermining the identification. The testimony was addressed to the jury, and the jury apparently found the identification reliable. Some of the State's testimony at the federal evidentiary hearing may well have been self-serving in that it too neatly fit the case law, but it surely does nothing to undermine the state record, which itself fully corroborated the identification.</p>
<p>We find that the District Court's conclusions on the critical facts are unsupported by the record and clearly erroneous. The victim spent a considerable period of time with her assailant, up to half an hour. She was with him under adequate artificial light in her house and under a full moon outdoors, and at least twice, once in the house and later in the woods, faced him directly and intimately. She was no casual observer, but rather the victim of one of the most personally humiliating of all crimes.<sup>[7]</sup> Her description to the police, which included the assailant's approximate age, height, weight, complexion, skin texture, build, and voice, might not have satisfied Proust but was more than ordinarily thorough. She had "no doubt" that respondent was the person who raped her. In the nature of the crime, there are rarely witnesses to a rape other than the victim, who often has a limited <span class="star-pagination">*201</span> opportunity of observation.<sup>[8]</sup> The victim here, a practical nurse by profession, had an unusual opportunity to observe and identify her assailant. She testified at the habeas corpus hearing that there was something about his face "I don't think I could ever forget." App. 127.</p>
<p>There was, to be sure, a lapse of seven months between the rape and the confrontation. This would be a seriously negative factor in most cases. Here, however, the testimony is undisputed that the victim made no previous identification at any of the showups, lineups, or photographic showings. Her record for reliability was thus a good one, as she had previously resisted whatever suggestiveness inheres in a showup. Weighing all the factors, we find no substantial likelihood of misidentification. The evidence was properly allowed to go to the jury.<sup>[9]</sup></p>
<p><i>Affirmed in part, reversed in part, and remanded.</i></p>
<p>MR. JUSTICE MARSHALL took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE STEWART concur, concurring in part and dissenting in part.</p>
<p>We granted certiorari in this case to determine whether our affirmance by an equally divided Court of respondent's state conviction constitutes an actual adjudication <span class="star-pagination">*202</span> within the meaning of <span class="citation no-link">28 U. S. C. § 2244</span> (c), and thus bars subsequent consideration of the same issues on federal habeas corpus. The Court holds today that such an affirmance does not bar further federal relief, and I fully concur in that aspect of the Court's opinion. Regrettably, however, the Court also addresses the merits and delves into the factual background of the case to reverse the District Court's finding, upheld by the Court of Appeals, that under the "totality of the circumstances," the pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> showup was so impermissibly suggestive as to give rise to a substantial likelihood of misidentification. This is an unjustified departure from our long-established practice not to reverse findings of fact concurred in by two lower courts unless shown to be clearly erroneous. See, <i>e. g., </i><i>Blau</i> v. <i>Lehman,</i> <span class="citation" data-id="9422327"><a href="/opinion/106328/blau-v-lehman/#408" aria-description="Citation for case: Blau v. Lehman">368 U. S. 403, 408-409</a></span> (1962); <i>Faulkner</i> v. <i>Gibbs,</i> <span class="citation" data-id="104726"><a href="/opinion/104726/faulkner-v-gibbs/#268" aria-description="Citation for case: Faulkner v. Gibbs">338 U. S. 267, 268</a></span> (1949); <i>United States</i> v. <i>Dickinson,</i> <span class="citation" data-id="104451"><a href="/opinion/104451/united-states-v-dickinson/#751" aria-description="Citation for case: United States v. Dickinson">331 U. S. 745, 751</a></span> (1947); <i>United States</i> v. <i>Commercial Credit Co.,</i> <span class="citation" data-id="101908"><a href="/opinion/101908/united-states-v-commercial-credit-co/#67" aria-description="Citation for case: United States v. Commercial Credit Co.">286 U. S. 63, 67</a></span> (1932); <i>United States</i> v. <i>Chemical Foundation,</i> <span class="citation" data-id="100923"><a href="/opinion/100923/united-states-v-chemical-foundation-inc/#14" aria-description="Citation for case: United States v. Chemical Foundation, Inc.">272 U. S. 1, 14</a></span> (1926); <i>Baker</i> v. <i>Schofield,</i> <span class="citation" data-id="98883"><a href="/opinion/98883/baker-v-schofield/#118" aria-description="Citation for case: Baker v. Schofield">243 U. S. 114, 118</a></span> (1917); <i>Towson</i> v. <i>Moore,</i> <span class="citation" data-id="94988"><a href="/opinion/94988/towson-v-moore/#24" aria-description="Citation for case: Towson v. Moore">173 U. S. 17, 24</a></span> (1899); cf. <i>Boulden</i> v. <i>Holman,</i> <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/#480" aria-description="Citation for case: Boulden v. Holman">394 U. S. 478, 480-481</a></span> (1969).</p>
<p>As the Court recognizes, a pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> identification obtained as a result of an unnecessarily suggestive showup may still be introduced in evidence if, under the "totality of the circumstances," the identification retains strong indicia of reliability. After an extensive hearing and careful review of the state court record, however, the District Court found that, under the circumstances of this case, there existed an intolerable risk of misidentification. Moreover, in making this determination, the court specifically found that "the complaining witness did not get an opportunity to obtain a good view of the suspect during the commission of the crime," "the show-up confrontation was not conducted near the time of the alleged crime, but, rather, some seven months after its commission," <span class="star-pagination">*203</span> and the complaining witness was unable to give "a good physical description of her assailant" to the police. App. 41-42. The Court of Appeals, which conducted its own review of the record, upheld the District Court's findings in their entirety. <span class="citation" data-id="9457324"><a href="/opinion/298978/archie-nathaniel-biggers-v-william-s-neil-warden-tennessee-state/#95" aria-description="Citation for case: Archie Nathaniel Biggers v. William S. Neil, Warden,...">448 F. 2d 91, 95</a></span> (CA6 1971).</p>
<p>Although this case would seem to fall squarely within the bounds of the "two-court" rule, the Court seems to suggest that the rule is "inapplicable here" because "this is a habeas corpus case in which the facts are contained primarily in the state court record (equally available to us as to the federal courts below) . . . ." <i>Ante,</i> at 193 n. 3. The "two-court" rule, however, rests upon more than mere deference to the trier of fact who has a firsthand opportunity to observe the testimony and to gauge the credibility of witnesses. For the rule also serves as an indispensable judicial "time-saver," making it unnecessary for this Court to waste scarce time and resources on minor factual questions which have already been accorded consideration by two federal courts and whose resolution is without significance except to the parties immediately involved. Thus, the "two-court" rule must logically apply even where, as here, the lower courts' findings of fact are based primarily upon the state court record.</p>
<p>The Court argues further, however, that the rule is irrelevant here because, in its view, "the dispute between the parties is not so much over the elemental facts as over the constitutional significance to be attached to them." <i>Ante,</i> at 193 n. 3. I cannot agree. Even a cursory examination of the Court's opinion reveals that its concern is not limited solely to the proper application of legal principles but, rather, extends to an essentially <i>de novo</i> inquiry into such "elemental facts" as the nature of the victim's opportunity to observe the assailant and the type of description the victim gave <span class="star-pagination">*204</span> the police at the time of the crime. And although we might reasonably disagree with the lower courts' findings as to such matters, the "two-court" rule wisely inhibits us from cavalierly substituting our own view of the facts simply because we might adopt a different construction of the evidence or resolve the ambiguities differently. On the contrary, these findings are "final here in the absence of very exceptional showing of error." <i>Comstock</i> v. <i>Group of Institutional Investors,</i> <span class="citation" data-id="9420225"><a href="/opinion/104591/comstock-v-group-of-institutional-investors/#214" aria-description="Citation for case: Comstock v. Group of Institutional Investors">335 U. S. 211, 214</a></span> (1948). The record before us is simply not susceptible of such a showing and, indeed, the petitioner does not argue otherwise. I would therefore dismiss the writ of certiorari as improvidently granted insofar as it relates to Question 2 of the Questions Presented.</p>
<h2>NOTES</h2>
<p>[1]  The legislative history adds little. The Senate Report states, cryptically, that "[t]his subsection is intended to give a conclusive presumption only to actual adjudications of Federal rights, by the Supreme Court, and not to give such a presumption to mere denials of writs of certiorari." S. Rep. No. 1797, 89th Cong., 2d Sess., 2 (1966). We conclude from this only that Congress did not expressly address itself to the effect of an affirmance by an equally divided Court. Nor is this surprising in view of the rarity of such divided affirmances in criminal cases.</p>
<p>[2]  We have been aided, and are confirmed in this view, by the thoughtful opinion of Judge Mansfield in <i>United States ex rel. Radich</i> v. <i>Criminal Ct. of City of New York,</i> <span class="citation" data-id="9458134"><a href="/opinion/303254/united-states-ex-rel-stephen-radich-v-the-criminal-court-of-the-city-of/" aria-description="Citation for case: United States Ex Rel. Stephen Radich v. The Criminal...">459 F. 2d 745</a></span> (CA2 1972), pet. for cert. pending <i>sub nom. Ross</i> v. <i>Radich,</i> No. 71-1510.</p>
<p>[3]  The dissent would have us decline to address the merits because the District Court, after an evidentiary hearing, found due process to have been violated, and the Court of Appealsafter reviewing the entire recordfound that "the conclusions of fact of the District Judge are [not] clearly erroneous." <span class="citation" data-id="9457324"><a href="/opinion/298978/archie-nathaniel-biggers-v-william-s-neil-warden-tennessee-state/#95" aria-description="Citation for case: Archie Nathaniel Biggers v. William S. Neil, Warden,...">448 F. 2d 91, 95</a></span>. It is said that we should not depart from "our long-established practice not to reverse findings of fact concurred in by two lower courts unless shown to be clearly erroneous." <i>Post,</i> at 202. This rule of practice, under which the Court does not lightly overturn the concurrent findings of fact of two lower federal courts, is a salutary one to be followed where applicable. We think it inapplicable here where the dispute between the parties is not so much over the elemental facts as over the constitutional significance to be attached to them. Moreover, this is a habeas corpus case in which the facts are contained primarily in the state court record (equally available to us as to the federal courts below) and where the evidentiary hearing in the District Court purported to be "confined" to two specific issues which we deem not controlling. Of the nine cases cited in the dissenting opinion in support of the rule of practice urged upon us, eight of them involved civil litigation in the federal system. Only one of the cases cited, <i>Boulden</i> v. <i>Holman,</i> <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/" aria-description="Citation for case: Boulden v. Holman">394 U. S. 478</a></span> (1969), involved a habeas corpus review and the Court simply heldon the basis of "an independent study of the entire record"that the conclusion reached by the District Court and the Court of Appeals "was justified." <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/#480" aria-description="Citation for case: Boulden v. Holman"><i>Id.,</i> at 480, 481</a></span>.</p>
<p>[4]  At trial, one of the police officers present at the identification testified explicitly that the words were spoken after the identification. The victim testified:
</p>
<p>"Q. What physical characteristics, if any, caused you to be able to identify him?</p>
<p>"A. First of all,uhhis size,next I could remember his voice.</p>
<p>"Q. What about his voice? Describe his voice to the Jury.</p>
<p>"A. Well, he has the voice of an immature youthI call it an immature youth. I have teen-age boys. And that was the first thing that made me think it was the boy." Tr. of Rec. in No. 237, O. T. 1967, p. 17.</p>
<p>The colloquy continued, with the victim describing the voice and other physical characteristics. At the habeas corpus hearing, the victim and all of the police witnesses testified that a visual identification preceded the voice identification. App. 80, 123, 134.</p>
<p>[5]  See <i>Clemons</i> v. <i>United States,</i> 133 U. S. App. D. C. 27, 47, <span class="citation" data-id="9454404"><a href="/opinion/284140/malcus-t-clemons-v-united-states-of-america-david-e-clark-v-united/#1250" aria-description="Citation for case: Malcus T. Clemons v. United States of America, David E....">408 F. 2d 1230, 1250</a></span> (1968) (McGowan, J., for the court <i>en banc</i>), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./394/964/">394 U. S. 964</a></span> (1969). In the present case, there has been controversy, in our view irrelevant, over whether, as she testified at the habeas corpus hearing, the victim actually made an in-court identification. While we think it evident from the many testimonial links between her out-of-court identification and "the defendant" before her in court that the answer is "yes," we recognize that if the testimony concerning the out-of-court identification was inadmissible, the conviction must be overturned.</p>
<p>[6]  The District Court stated:
</p>
<p>"In this case it appears to the Court that a line-up, which both sides admit is generally more reliable than a show-up, could have been arranged. The fact that this was not done tended needlessly to decrease the fairness of the identification process to which petitioner was subjected." App. 42.</p>
<p>[7]  See <i>United States ex rel. Phipps</i> v. <i>Follette,</i> <span class="citation" data-id="291028"><a href="/opinion/291028/united-states-of-america-ex-rel-robert-phipps-relator-appellant-v-harold/#915" aria-description="Citation for case: United States of America Ex Rel. Robert Phipps,...">428 F. 2d 912, 915-916</a></span> (CA2) (Friendly, J.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/908/">400 U. S. 908</a></span> (1970).</p>
<p>[8]  Respondent attaches some weight to the failure of the victim's daughter to identify him. Apart from the fact that this does not bear directly on the reliability of her mother's identification, the girl was only 12 years old and had, as best we can tell, only a very brief view of the assailant from across the room.</p>
<p>[9]  Respondent's habeas corpus petition raised a number of other claims, including one challenging the legality of his detention at the time he was viewed by the victim. The courts below did not address these claims, nor do we.</p>

</div>
```

---

## GROUP: content/cases/New York v. Burger.md  (`case`, 5 assertions)

### content_page

```
---
title: "New York v. Burger"
type: case
citation: "482 U.S. 691 (1987)"
parallel_cite: "107 S. Ct. 2636; 96 L. Ed. 2d 601; 55 U.S.L.W. 4890"
neutral_cite: 1987 U.S. LEXIS 2725
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-06-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-06-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New York v. Burger
  varies_by_point: false
  scope_note: "Three-part test for warrantless inspection of closely regulated businesses; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111927/new-york-v-burger/"
  cluster_id: 111927
  opinion_id: 9431050
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Donovan v. Dewey]]", "[[Marshall v. Barlow's, Inc.]]", "[[United States v. Biswell]]", "[[Camara v. Municipal Court]]"]
aliases: []
tags: ["case", "fourth-amendment", "administrative-search", "closely-regulated-business", "inspection"]
holding: "A warrantless administrative inspection of a closely (pervasively) regulated business — here, an automobile junkyard — is reasonable if…"
lake:
  record_id: New York v. Burger
  status: verified
  projected_at: 2026-07-06
---

# New York v. Burger

*482 U.S. 691 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police conducted a warrantless inspection of Burger's automobile junkyard under a New York statute authorizing inspection of vehicle-dismantling businesses. They found stolen vehicles and parts and charged him with possession of stolen property.

## Issue
Whether a warrantless administrative inspection of a closely (pervasively) regulated business is reasonable under the Fourth Amendment.

## Rule
A warrantless inspection of a pervasively regulated business is reasonable only if three criteria are met. "This warrantless inspection, however, even in the context of a pervasively regulated business, will be deemed to be reasonable only so long as three criteria are met. First, there must be a 'substantial' government interest that informs the regulatory scheme pursuant to which the inspection is made." — 482 U.S. at 702. ^pin-702

Second, the warrantless inspections must be necessary to further the regulatory scheme. "Finally, 'the statute's inspection program, in terms of the certainty and regularity of its application, [must] provid[e] a constitutionally adequate substitute for a warrant.'" — *Id.* at 703. ^pin-703

## Application
Junkyards/vehicle-dismantling businesses are closely regulated; New York had a substantial interest in combating automobile theft; warrantless, unannounced inspections were necessary because stolen cars and parts pass quickly through such businesses and surprise is essential to detection; and the statute provided a constitutionally adequate substitute for a warrant by notifying operators that inspections would occur on a regular basis and by limiting inspectors' discretion. The inspection of Burger's junkyard was therefore reasonable.

## Conclusion
The warrantless inspection was constitutional; the New York Court of Appeals' suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Burger* synthesizes the closely-regulated-business inspection line ([[United States v. Biswell]]; [[Donovan v. Dewey]]) into a three-part test, distinct from the warrant-based regime for ordinary commercial premises in [[Marshall v. Barlow's, Inc.]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *New York v. Burger*, 482 U.S. 691 (1987) — https://www.courtlistener.com/opinion/111927/new-york-v-burger/ — pinpoints: 702, 703.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a481cf1b341eeef4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "482 U.S. 691 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 2725", "official_citation_present": true, "parallel_cite": "107 S. Ct. 2636; 96 L. Ed. 2d 601; 55 U.S.L.W. 4890", "title": "New York v. Burger", "year": "1987"}}
{"assertion_id": "4d6896d55841bda1", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "New York v. Burger"}}
{"assertion_id": "fe8f58d3676bbf68", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless administrative inspection of a closely (pervasively) regulated business — here, an automobile junkyard — is reasonable if…", "title": "New York v. Burger"}}
{"assertion_id": "05095260dc0cb87d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-06-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "New York v. Burger", "field_i_validity": "good_law", "scope_note": "Three-part test for warrantless inspection of closely regulated businesses; good law.", "title": "New York v. Burger", "varies_by_point": "false"}}
{"assertion_id": "1a782e086b5ea685", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "New York v. Burger"}}
```

### lake record — New York v. Burger

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Burger",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Burger",
    "case_name_short": "Burger",
    "case_name_full": "New York v. Burger",
    "input_case_name": "New York v. Burger",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-06-19",
    "year": 1987,
    "docket": null,
    "cluster_id": 111927,
    "lead_opinion_id": 9431050,
    "sibling_ids": [
      111927,
      9431050,
      9431051
    ],
    "absolute_url": "/opinion/111927/new-york-v-burger/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "482 U.S. 691",
      "volume": "482",
      "reporter": "U.S.",
      "page": "691",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 2636",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "2636",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 L. Ed. 2d 601",
        "volume": "96",
        "reporter": "L. Ed. 2d",
        "page": "601",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4890",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4890",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 2725",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2725",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "482 U.S. 691",
        "volume": "482",
        "reporter": "U.S.",
        "page": "691",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 2636",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "2636",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 L. Ed. 2d 601",
        "volume": "96",
        "reporter": "L. Ed. 2d",
        "page": "601",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 2725",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2725",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4890",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4890",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "482 U.S. 691",
    "official_selection": {
      "court_class": "scotus",
      "selected": "482 U.S. 691",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-702",
      "page": null,
      "quote": "--- # New York v. Burger *482 U.S. 691 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police conducted a warrantless inspection of Burger's automobile junkyard under a New York statute authorizing inspection of vehicle-dismantling businesses. They found stolen vehicles and parts and charged him with possession of stolen property. ## Issue Whether a warrantless administrative inspection of a closely (pervasively) regulated business is reasonable under the Fourth Amendment. ## Rule A warrantless inspection of a pervasively regulated business is reasonable only if three criteria are met.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-703",
      "page": null,
      "quote": "Finally, 'the statute's inspection program, in terms of the certainty and regularity of its application, [must] provid[e] a constitutionally adequate substitute for a warrant.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-06-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New York v. Burger",
    "varies_by_point": false,
    "scope_note": "Three-part test for warrantless inspection of closely regulated businesses; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Gigliotti",
          "cluster_id": 7316853,
          "cite": [
            "145 F. Supp. 3d 203",
            "2015 WL 6830675"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathan Albert Leal v. State",
          "cluster_id": 2751234,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vivid Entertainment, LLC v. Fielding",
          "cluster_id": 8727579,
          "cite": [
            "965 F. Supp. 2d 1113",
            "2013 WL 4451068",
            "2013 U.S. Dist. LEXIS 116731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ortiz",
          "cluster_id": 8477550,
          "cite": [
            "507 F. App'x 339"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Al-Kidd v. Ashcroft",
          "cluster_id": 1204118,
          "cite": [
            "580 F.3d 949",
            "2009 U.S. App. LEXIS 20000",
            "2009 WL 2836448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waters v. Churchill",
          "cluster_id": 1087950,
          "cite": [
            "128 L. Ed. 2d 686",
            "114 S. Ct. 1878",
            "511 U.S. 661",
            "1994 U.S. LEXIS 4104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dolan v. City of Tigard",
          "cluster_id": 117861,
          "cite": [
            "129 L. Ed. 2d 304",
            "114 S. Ct. 2309",
            "512 U.S. 374",
            "1994 U.S. LEXIS 4826"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Verdugo-Urquidez",
          "cluster_id": 112382,
          "cite": [
            "108 L. Ed. 2d 222",
            "110 S. Ct. 1056",
            "494 U.S. 259",
            "1990 U.S. LEXIS 1175",
            "1990 WL 16772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2428168,
          "cite": [
            "827 S.W.2d 937",
            "1992 Tex. Crim. App. LEXIS 83",
            "1992 WL 61756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chandler v. Miller",
          "cluster_id": 118100,
          "cite": [
            "137 L. Ed. 2d 513",
            "117 S. Ct. 1295",
            "520 U.S. 305",
            "1997 U.S. LEXIS 2505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 118414,
          "cite": [
            "149 L. Ed. 2d 205",
            "121 S. Ct. 1281",
            "532 U.S. 67",
            "2001 U.S. LEXIS 2460",
            "2001 Daily Journal DAR 2839",
            "2001 Colo. J. C.A.R. 1427",
            "14 Fla. L. Weekly Fed. S 152",
            "69 U.S.L.W. 4184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carlos Botero-Ospina",
          "cluster_id": 709242,
          "cite": [
            "71 F.3d 783",
            "1995 U.S. App. LEXIS 34347",
            "1995 WL 723102"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cecil Ferguson",
          "cluster_id": 656143,
          "cite": [
            "8 F.3d 385",
            "1993 U.S. App. LEXIS 28306",
            "1993 WL 437691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segundo v. State",
          "cluster_id": 1590541,
          "cite": [
            "270 S.W.3d 79",
            "2008 Tex. Crim. App. LEXIS 1505",
            "2008 WL 4724093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mitchell",
          "cluster_id": 168153,
          "cite": [
            "518 F.3d 740",
            "69 Fed. R. Serv. 3d 1713",
            "2008 U.S. App. LEXIS 4505",
            "2008 WL 542130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. City of New York",
          "cluster_id": 2490,
          "cite": [
            "579 F.3d 160",
            "2009 U.S. App. LEXIS 17640",
            "2009 WL 2413929"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ronald Calzone v. Josh Hawley",
          "cluster_id": 4416575,
          "cite": [
            "866 F.3d 866",
            "2017 WL 3366519",
            "2017 U.S. App. LEXIS 14476"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Santikos v. State",
          "cluster_id": 1653416,
          "cite": [
            "836 S.W.2d 631",
            "1992 Tex. Crim. App. LEXIS 131",
            "1992 WL 116096"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of L. A. v. Patel",
          "cluster_id": 2811846,
          "cite": [
            "576 U.S. 409",
            "135 S. Ct. 2443",
            "192 L. Ed. 2d 435",
            "2015 U.S. LEXIS 4065",
            "83 U.S.L.W. 4520",
            "25 Fla. L. Weekly Fed. S 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111927 OR 9431050 OR 9431051) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU4NjI0MDAwMDAwJnM9Nzk1ODY3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111927+OR+9431050+OR+9431051%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111927 OR 9431050 OR 9431051)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzImcz0yODEwNTI0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111927+OR+9431050+OR+9431051%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111927 OR 9431050 OR 9431051)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111927 OR 9431050 OR 9431051)",
    "indexed_citing_opinions": 691,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111927,
        "count": 608,
        "count_source": "search"
      },
      {
        "opinion_id": 9431050,
        "count": 111,
        "count_source": "search"
      },
      {
        "opinion_id": 9431051,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1073,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-burger.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNjU0ODUmcz0xMDMxNDM4MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111927+OR+9431050+OR+9431051%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111927,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 317754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 427553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1108128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1244252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1382601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1557646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1601166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2024330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2102923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2123138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2123937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2583761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 3778084,
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
    "date_created": "2026-07-05T15:36:22Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:36:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:36:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:38:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:36:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Burger

```
<opinion type="majority">
<author id="b731-6">Justice Blackmun</author>
<p id="ANB">delivered the opinion of the Court.</p>
<p id="b731-7">This case presents the question whether the warrantless search of an automobile junkyard, conducted pursuant to a statute authorizing such a search, falls within the exception to the warrant requirement for administrative inspections of pervasively regulated industries. The case also presents the question whether an otherwise proper administrative inspection is unconstitutional because the ultimate purpose of the regulatory statute pursuant to which the search is done — the deterrence of criminal behavior — is the same as that of penal laws, with the result that the inspection may disclose violations not only of the regulatory statute but also of the penal statutes.</p>
<p id="b731-8">I</p>
<p id="b731-9">Respondent Joseph Burger is the owner of a junkyard in Brooklyn, N. Y. His business consists, in part, of the dismantling of automobiles and the selling of their parts. His junkyard is an open lot with no buildings. A high metal fence surrounds it, wherein are located, among other things, vehicles and parts of vehicles. At approximately noon on November 17, 1982, Officer Joseph Vega and four other plainclothes officers, all members of the Auto Crimes Division of the New York City Police Department, entered re<page-number citation-index="1" label="694">*694</page-number>spondent’s junkyard to conduct an inspection pursuant to N. Y. Veh. &amp; Traf. Law §415-a5 (McKinney 1986).<footnotemark>1</footnotemark> Tr. 6. On any given day, the Division conducts from 6 to 10 inspections of vehicle dismantlers, automobile junkyards, and related businesses.<footnotemark>2</footnotemark> <em>Id., </em>at 26.</p>
<p id="b732-5">Upon entering the junkyard, the officers asked to see Burger’s license<footnotemark>3</footnotemark> and his “police book” — the record of the auto<page-number citation-index="1" label="695">*695</page-number>mobiles and vehicle parts in his possession. Burger replied that he had neither a license nor a police book.<footnotemark>4</footnotemark> The officers then announced their intention to conduct a § 415-a5 inspection. Burger did not object. Tr. 6, 47. In accordance with their practice, the officers copied down the Vehicle Identification Numbers (VINs) of several vehicles and parts of vehicles that were in the junkyard. <em>Id., </em>at 7, 20, 44, 46. After checking these numbers against a police computer, the officers determined that respondent was in possession of stolen vehicles and parts.<footnotemark>5</footnotemark> Accordingly, Burger was arrested and charged with five counts of possession of stolen property<footnotemark>6</footnotemark> <page-number citation-index="1" label="696">*696</page-number>and one count of unregistered operation as a vehicle dismantle^ in violation of § 415-al.</p>
<p id="b734-5">In the Kings County Supreme Court, Burger moved to suppress the evidence obtained as a result of the inspection, primarily on the ground that § 415-a5 was unconstitutional. After a hearing, the court denied the motion. It reasoned that the junkyard business was a “pervasively regulated” industry in which warrantless administrative inspections were appropriate, that the statute was properly limited in “time, place and scope,” and that, once the officers had reasonable cause to believe that certain vehicles and parts were stolen, they could arrest Burger and seize the property without a warrant. App. to Pet. for Cert. 18a-19a. When respondent moved for reconsideration in light of a recent decision of the Appellate Division, <em>People </em>v. <em>Pace, </em>101 App. Div. 2d 336, 475 N. Y. S. 2d 443 (1984), aff’d, 65 N. Y. 2d 684, <span class="citation no-link">481 N. E. 2d 250</span> (1985),<footnotemark>7</footnotemark> the court granted reargument. Upon re<page-number citation-index="1" label="697">*697</page-number>consideration, the court distinguished the situation in <em>Pace </em>from that in the instant case. It observed that the Appellate Division in <em>Pace </em>did not apply § 415-a5 to the search in question, <span class="citation" data-id="6204687"><a href="/opinion/6336105/people-v-burger/#711" aria-description="Citation for case: People v. Burger">125 Misc. 2d 709, 711</a></span>, 479 N. Y. S. 2d 936, 938 (1984), and that, in any event, the police officers in that case were not conducting an administrative inspection, but were acting on the basis of recently discovered evidence that criminal activity was taking place at the automobile salvage yard. <span class="citation" data-id="6204687"><a href="/opinion/6336105/people-v-burger/#712" aria-description="Citation for case: People v. Burger"><em>Id., </em>at 712-714</a></span>, 479 N. Y. S. 2d, at 939-940. The court therefore reaffirmed its earlier determination in the instant case that § 415-a5 was constitutional.<footnotemark>8</footnotemark> For the same reasons, the Appellate Division affirmed. 112 App. Div. 2d 1046, 493 N. Y. S. 2d 34 (1985).</p>
<p id="b735-5">The New York Court of Appeals, however, reversed. 67 N. Y. 2d 338, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/" aria-description="Citation for case: People v. Burger">493 N. E. 2d 926</a></span> (1986). In its view, § 415-a5 violated the Fourth Amendment’s prohibition of unreasonable searches and seizures.<footnotemark>9</footnotemark> According to the Court of Ap<page-number citation-index="1" label="698">*698</page-number>peals, “[t]he fundamental defect [of § 415-a5] ... is that [it] authorize [s] searches undertaken solely to uncover evidence of criminality and not to enforce a comprehensive regulatory scheme. The asserted ‘administrative schem[e]’ here [is], in reality, designed simply to give the police an expedient means of enforcing penal sanctions for possession of stolen property.” <em>Id., </em>at 344, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929</a></span>. In contrast to the statutes authorizing warrantless inspections whose constitutionality this Court has upheld, §415-a5, it was said, “do[es] little more than authorize general searches, including those conducted by the police, of certain commercial premises.” <em>Ibid. </em>To be sure, with its license and recordkeeping requirements, and with its authorization for inspections of records, § 415-a appears to be administrative in character. “It fails to satisfy the constitutional requirements for a valid, comprehensive regulatory scheme, however, inasmuch as it permits searches, such as conducted here, of vehicles and vehicle parts notwithstanding the absence of any records against which the findings of such a search could be compared.” <em>Id., </em>at 344-345, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929-930</a></span>. Accordingly, the only purpose of such searches is to determine whether a junkyard owner is storing stolen property on business premises.<footnotemark>10</footnotemark></p>
<p id="b736-5">Because of the important state interest in administrative schemes designed to regulate the vehicle-dismantling or automobile-junkyard industry,<footnotemark>11</footnotemark> we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./479/812/">479 U. S. 812</a></span> (1986).</p>
<p id="Ai6G"><page-number citation-index="1" label="699">*699</page-number>l — l I</p>
<p id="Ank">A</p>
<p id="AAH">The Court long has recognized that the Fourth Amendment’s prohibition on unreasonable searches and seizures is applicable to commercial premises, as'well as to private homes. <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541, 543, 546</a></span> (1967). An owner or operator of a business thus has an expectation of privacy in commercial property, which society is prepared to consider to be reasonable, see <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). This expecta<page-number citation-index="1" label="700">*700</page-number>tion exists not only with respect to traditional police searches conducted for the gathering of criminal evidence but also with respect to administrative inspections designed to enforce regulatory statutes. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312-313</a></span> (1978). An expectation of privacy in commercial premises, however, is different from, and indeed less than, a similar expectation in an individual’s home. See <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#598" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 598-599</a></span> (1981). This expectation is particularly attenuated in commercial property employed in “closely regulated” industries. The Court observed in <em>Marshall </em>v. <em>Barlow’s, Inc.: </em>“Certain industries have such a history of government oversight that no reasonable expectation of privacy, see <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351-352</a></span> (1967), could exist for a proprietor over the stock of such an enterprise.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 313</a></span>.</p>
<p id="b738-5">The Court first examined the “unique” problem of inspections of “closely regulated” businesses in two enterprises that had “a long tradition of close government supervision.” <em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">Ibid.</a></span> </em>In <em>Colonnade Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970), it considered a warrantless search of a catering business pursuant to several federal revenue statutes authorizing the inspection of the premises of liquor dealers. Although the Court disapproved the search because the statute provided that a sanction be imposed when entry was refused, and because it did not authorize entry without a warrant as an alternative in this situation, it recognized that “the liquor industry [was] long subject to close supervision and inspection.” <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#77" aria-description="Citation for case: Colonnade Catering Corp. v. United States"><em>Id., </em>at 77</a></span>. We returned to this issue in <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972), which involved a warrantless inspection of the premises of a pawnshop operator, who was federally licensed to sell sporting , weapons pursuant to the Gun Control Act of 1968, <span class="citation no-link">18 U. S. C. § 921</span> <em>et seq. </em>While noting that “[fjederal regulation of the interstate' traffic in firearms is not as deeply rooted in history as is governmental control of the liquor industry,” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>, we nonetheless concluded that the warrantless inspec<page-number citation-index="1" label="701">*701</page-number>tions authorized by the Gun Control Act would “pose only limited threats to the dealer’s justifiable expectations of privacy.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 316</a></span>. We observed: “When a dealer chooses to engage in this pervasively regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection.” <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Ibid.</a></span></em></p>
<p id="b739-5">The “Colonnade-Biswell” doctrine, stating the reduced expectation of privacy by an owner of commercial premises in a “closely regulated” industry, has received renewed emphasis in more recent decisions. In <em>Marshall </em>v. <em>Barlow’s, Inc., </em>we noted its continued vitality but declined to find that war-rantless inspections, made pursuant to the Occupational Safety and Health Act of 1970, <span class="citation no-link">84 Stat. 1598</span>, <span class="citation no-link">29 U. S. C. § 657</span>(a), of <em>all </em>businesses engaged in interstate commerce fell within the narrow focus of this doctrine. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 313-314</a></span>. However, we found warrantless inspections made pursuant to the Federal Mine Safety and Health Act of 1977, <span class="citation no-link">91 Stat. 1290</span>, <span class="citation no-link">30 U. S. C. §801</span> <em>et seq., </em>proper because they were of a “closely regulated” industry. <em>Donovan </em>v. <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey, supra.</a></span></em></p>
<p id="b739-6">Indeed, in <em>Donovan </em>v. <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey</a></span>, </em>we declined to limit our consideration to the length of time during which the business in question — stone quarries — had been subject to federal regulation. <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#605" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 605-606</a></span>. We pointed out that the doctrine is essentially defined by “the pervasiveness and regularity of the federal regulation” and the effect of such regulation upon an owner’s expectation of privacy. See <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey"><em>id., </em>at 600, 606</a></span>. We observed, however, that “the duration of a particular regulatory scheme” would remain an “important factor” in deciding whether a warrantless inspection pursuant to the scheme is permissible. <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#606" aria-description="Citation for case: Donovan v. Dewey"><em>Id., </em>at 606</a></span>.<footnotemark>12</footnotemark></p>
<p id="b740-4"><page-number citation-index="1" label="702">*702</page-number>B</p>
<p id="b740-5">Because the owner or operator of commercial premises in a “closely regulated” industry has a reduced expectation of privacy, the warrant and probable-cause requirements, which fulfill the traditional Fourth Amendment standard of reasonableness for a government search, see <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#741" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 741</a></span> (1987) (dissenting opinion), have lessened application in this context. Rather, we conclude that, as in other situations of “special need,” see New <em>Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#353" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 353</a></span> (1985) (opinion concurring in judgment), where the privacy interests of the owner are weakened and the government interests in regulating particular businesses are concomitantly heightened, a warrant-less inspection of commercial premises may well be reasonable within the meaning of the Fourth Amendment.</p>
<p id="b740-7">This warrantless inspection, however, even in the context of a pervasively regulated business, will be deemed to be reasonable only so long as three criteria are met. First, there must be a “substantial” government interest that informs the regulatory scheme pursuant to which the inspection is made. See <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#602" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 602</a></span> (“substantial federal interest in improving the health and safety conditions in the Nation’s underground and surface mines”); <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span> (regulation of firearms is “of central importance to federal efforts to prevent violent crime and to assist the States in regulating the firearms traffic within their borders”); <em>Colonnade Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#75" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 75</a></span> (federal interest “in protecting the revenue against various types of fraud”).</p>
<p id="b740-8">Second, the warrantless inspections must be “necessary to further [the] regulatory scheme.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 600</a></span>. For example, in <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey</a></span> </em>we recognized that forcing mine inspectors to obtain a warrant before every in<page-number citation-index="1" label="703">*703</page-number>spection might alert mine owners or operators to the impending inspection, thereby frustrating the purposes of the Mine Safety and Health Act — to detect and thus to deter safety and health violations. <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">Id., at 603</a></span>.</p>
<p id="b741-8">Finally, “the statute’s inspection program, in terms of the certainty and regularity of its application, [must] provid[e] a constitutionally adequate substitute for a warrant.” <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Ibid.</a></span> </em>In other words, the regulatory statute must perform the two basic functions of a warrant: it must advise the owner of the commercial premises that the search is being made pursuant to the law and has a properly defined scope, and it must limit the discretion of the inspecting officers. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 323</a></span>; see also <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#332" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>id., </em>at 332</a></span> (Stevens, J., dissenting). To perform this first function, the statute must be “sufficiently comprehensive and defined that the owner of commercial property cannot help but be aware that his property will be subject to periodic inspections undertaken for specific purposes.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 600</a></span>. In addition, in defining how a statute limits the discretion of the inspectors, we have observed that it must be “carefully limited in time, place, and scope.” <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>.</p>
<p id="b741-9">hH I — I hH</p>
<p id="b741-3">A</p>
<p id="b741-4">Searches made pursuant to § 415-a5, in our view, clearly fall within this established exception to the warrant requirement for administrative inspections in “closely regulated” businesses.<footnotemark>13</footnotemark> First, the nature of the regulatory statute reveals that the operation of a junkyard, part of which is devoted to <page-number citation-index="1" label="704">*704</page-number>vehicle dismantling, is a “closely regulated” business in the State of New York.<footnotemark>14</footnotemark> The provisions regulating the activity of vehicle dismantling are extensive. An operator cannot engage in this industry without first obtaining a license, which means that he must meet the registration requirements and must pay a fee.<footnotemark>15</footnotemark> Under § 415-a5(a), the operator must maintain a police book recording the acquisition and disposition of motor vehicles and vehicle parts, and make such records and inventory available for inspection by the police or any agent of the Department of Motor Vehicles. The operator also must display his registration number prominently at his place of business, on business documentation, and on vehicles and parts that pass through his business. § 415-a5(b). Moreover, the person engaged in this activity is subject to criminal penalties, as well as to loss of license or civil fines, <page-number citation-index="1" label="705">*705</page-number>for failure to comply with these provisions. See §§ 415-al, 5, and 6.<footnotemark>16</footnotemark> That other States besides New York have imposed similarly extensive regulations on automobile junkyards further supports the “closely regulated” status of this industry. See n. 11, <em>supra.</em></p>
<p id="b743-5">In determining whether vehicle dismantlers constitute a “closely regulated” industry, the “duration of [this] particular regulatory scheme,” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#606" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 606</a></span>, has some relevancy. Section 415-a could be said to be of fairly recent vintage, see 1973 N. Y. Laws, ch. 225, § 1 (McKinney), and the inspection provision of § 415-a5 was added only in 1979, see 1979 N. Y. Laws, ch. 691, §2 (McKinney). But because the automobile is a relatively new phenomenon in our society and because its widespread use is even newer, automobile junkyards and vehicle dismantlers have not been in existence very long and thus do not have an ancient history of government oversight. Indeed, the indus<page-number citation-index="1" label="706">*706</page-number>try did not attract government attention until the 1950’s, when all used automobiles were no longer easily reabsorbed into the steel industry and attention then focused on the environmental and aesthetic problems associated with abandoned vehicles. See Landscape 1970: National Conference on the Abandoned Automobile 11; see also Report to the President from the Panel on Automobile Junkyards, White House Conference on Natural Beauty 1 (1965) (statement of Charles M. Haar, Chairman: “There are junkyards and abandoned cars in the streets and along the countryside that are making America ugly, not beautiful”).</p>
<p id="b744-4">The automobile-junkyard business, however, is simply a new branch of an industry that has existed, and has been closely regulated, for many years. The automobile junkyard is closely akin to the secondhand shop or the general junkyard. Both share the purpose of recycling salvageable articles and components of items no longer usable in their original form. As such, vehicle dismantlers represent a modern, specialized version of a traditional activity.<footnotemark>17</footnotemark> In New York, general junkyards and secondhand shops long have been subject to regulation. One New York court has explained:</p>
<blockquote id="b745-4"><page-number citation-index="1" label="707">*707</page-number>“Vehicle dismantlers are part of the junk industry as well as part of the auto industry. . . . Prior to the enactment of section 415-a of the Vehicle and Traffic Law, auto dismantlers were subject to regulatory provisions governing the licensing and operation of junkyards. These regulations included provisions mandating the keeping of detailed records of purchases and sales, and the making of such records available at reasonable times to designated officials including police officers, by junk dealers . . . and by dealers in secondhand articles ....</blockquote>
<blockquote id="b745-5">“These regulatory, record keeping and warrantless inspection provisions for junk shops have been a part of the law of the City of New York and of Brooklyn for at least 140 years.” <em>People </em>v. <em>Tinneny, </em><span class="citation" data-id="6199918"><a href="/opinion/6331361/people-v-tinneny/#969" aria-description="Citation for case: People v. Tinneny">99 Misc. 2d 962, 969</a></span>, 417 N. Y. S. 2d 840, 845 (Sup. 1979).</blockquote>
<p id="b745-6">See also N. Y. C. Charter and Admin. Code § B32-113.01 (1977) (“ ‘Junk dealer’. Any person engaged in the business of purchasing or selling junk”); §B32-126.0a (‘“dealer in second-hand articles’ shall mean any person who, in any way or as a principal broker or agent: 1. [d]eals in the purchase or sale of second-hand articles of whatever nature”).<footnotemark>18</footnotemark> The history of government regulation of junk-related activities argues strongly in favor of the “closely regulated” status of the automobile junkyard.</p>
<p id="b745-7">Accordingly, in light of the regulatory framework governing his business and the history of regulation of related industries, an operator of a junkyard engaging in vehicle dismantling has a reduced expectation of privacy in this “closely regulated” business.</p>
<p id="b746-3"><page-number citation-index="1" label="708">*708</page-number>B</p>
<p id="b746-4">The New York regulatory scheme satisfies the three criteria necessary to make reasonable warrantless inspections pursuant to § 415-a5. First, the State has a substantial interest in regulating the vehicle-dismantling and automobile-junkyard industry because motor vehicle theft has increased in the State and because the problem of theft is associated with this industry. In this day, automobile theft has become a significant social problem, placing enormous economic and personal burdens upon the citizens of different States. For example, when approving the 1979 amendment to § 415-a5, which added the provision for inspections of records and inventory of junkyards, the Governor of the State explained:</p>
<blockquote id="b746-5">“Motor vehicle theft in New York State has been rapidly increasing. It has become a multimillion dollar industry which has resulted in an intolerable economic burden on the citizens of New York. In 1976, over 130,000 automobiles were reported stolen in New York, resulting in losses in excess of $225 million. Because of the high rate of motor vehicle theft, the premiums for comprehensive motor vehicle insurance in New York are significantly above the national average. In addition, stolen automobiles are often used in the commission of other crimes and there is a high incidence of accidents resulting in property damage and bodily injury involving stolen automobiles.” Governor’s Message approving L. 1979, chs. 691 and 692,1979 N. Y. Laws 1826,1826-1827 (McKinney).</blockquote>
<p id="b746-6">See also 25 Legislative Newsletter, New York State Automobile Assn., p. 1 (May 10, 1978), reprinted in Governor’s Bill Jacket, L. 1979, ch. 691 (1979 Bill Jacket) (“Auto theft in New York State has become a low-risk, high-profit, multi<page-number citation-index="1" label="709">*709</page-number>million dollar growth industry that is imposing intolerable economic burdens on motorists”).<footnotemark>19</footnotemark> Because contemporary automobiles are made from standardized parts, the nationwide extent of vehicle theft and concern about it are understandable.</p>
<p id="b747-5">Second, regulation of the vehicle-dismantling industry reasonably serves the State’s substantial interest in eradicating automobile theft. It is well established that the theft problem can be addressed effectively by controlling the receiver of, or market in, stolen property. 2 W. LaFave &amp; A. Scott, Substantive Criminal Law §8.10(a), p. 422 (1986) (“Without [professional receivers of stolen property], theft ceases to be profitable”); 2 Encyclopedia of Crime and Justice 789 (Kadish ed. 1983) (“[The criminal receiver] . . . inspires 95 per cent or more of the theft in America”). Automobile junkyards and vehicle dismantlers provide the major market for stolen vehicles and vehicle parts. See Memorandum from Paul Goldman, Counsel, State Consumer Protection Board, to Richard A. Brown, Counsel to the Governor (June 29, 1979), 1979 Bill Jacket (“It is believed that a major source of stolen vehicles, parts and registration documentation may involve vehicles which pass through the hands of [junk vehicle] dealers”). Thus, the State rationally may believe that it will reduce car theft by regulations that prevent automobile junkyards from becoming markets for stolen vehicles and that help trace the origin and destination of vehicle parts.<footnotemark>20</footnotemark></p>
<p id="b748-3"><page-number citation-index="1" label="710">*710</page-number>Moreover, the warrantless administrative inspections pursuant to § 415-a5 “are necessary to further [the] regulatory scheme.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 600</a></span>. In this respect, we see no difference between these inspections and those approved by the Court in <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span> </em>and <em>Donovan </em>v. <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey</a></span>. </em>We explained in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>:</em></p>
<blockquote id="b748-4">“[I]f inspection is to be effective and serve as a credible deterrent, unannounced, even frequent, inspections are essential. In this context, the prerequisite of a warrant could easily frustrate inspection; and if the necessary flexibility as to time, scope, and frequency is to be preserved, the protections afforded by a warrant would be negligible.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</blockquote>
<p id="b748-5">See also <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 603</a></span>. Similarly, in the present case, a warrant requirement would interfere with the statute’s purpose of deterring automobile theft accomplished by identifying vehicles and parts as stolen and shutting down the market in such items. Because stolen cars and parts often pass quickly through an automobile junkyard, “frequent” and “unannounced” inspections are necessary in order to detect them. In sum, surprise is crucial if the regulatory scheme aimed at remedying this major social problem is to function at all.</p>
<p id="b749-4"><page-number citation-index="1" label="711">*711</page-number>Third, § 415-a5 provides a “constitutionally adequate substitute for a warrant.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 603</a></span>. The statute informs the operator of a vehicle dismantling business that inspections will be made on a regular basis. <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#605" aria-description="Citation for case: Donovan v. Dewey"><em>Id., </em>at 605</a></span>. Thus, the vehicle dismantler knows that the inspections to which he is subject do not constitute discretionary acts by a government official but are conducted pursuant to statute. See <em>Marshall </em>v. <em>Barlow's, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#332" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 332</a></span> (dissenting opinion). Section 415-a5 also sets forth the scope of the inspection and, accordingly, places the operator on notice as to how to comply with the statute. In addition, it notifies the operator as to who is authorized to conduct an inspection.</p>
<p id="b749-5">Finally, the “time, place, and scope” of the inspection is limited, <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>, to place appropriate restraints upon the discretion of the inspecting officers. See <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#605" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 605</a></span>. The officers are allowed to conduct an inspection only “during [the] regular and usual business hours.” §415-a5.<footnotemark>21</footnotemark> The inspections can be made only of vehicle-dismantling and related industries. And the permissible scope of these searches is narrowly defined: the inspectors may examine the records, as well as “any vehicles or parts of vehicles which are subject to <page-number citation-index="1" label="712">*712</page-number>the record keeping requirements of this section and which are on the premises.” Ibid.<footnotemark>22</footnotemark></p>
<p id="b750-5">IV</p>
<p id="b750-6">A search conducted pursuant to § 415-a5, therefore, clearly falls within the well-established exception to the warrant requirement for administrative inspections of “closely regulated” businesses. The Court of Appeals, nevertheless, struck down the statute as violative of the Fourth Amendment because, in its view, the statute had no truly administrative purpose but was “designed simply to give the police an expedient means of enforcing penal sanctions for possession of stolen property.” 67 N. Y. 2d, at 344, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929</a></span>. The court rested its conclusion that the administrative goal of the statute was pretextual and that § 415-a5 really “authorized searches undertaken solely to uncover evidence of criminality” particularly on the fact that, even if an operator failed to produce his police book, the inspecting officers could continue their inspection for stolen vehicles and parts. <em>Id., </em>at 344, 345, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929, 930</a></span>. The court also suggested that the identity of the inspectors — police officers — was significant in revealing the true nature of the statutory scheme. <em>Id., </em>at 344, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929</a></span>.</p>
<p id="b750-7">In arriving at this conclusion, the Court of Appeals failed to recognize that a State can address a major social problem <em>both </em>by way of an administrative scheme <em>and </em>through penal sanctions. Administrative statutes and penal laws may have the same <em>ultimate </em>purpose of remedying the social problem, but they have different subsidiary purposes and prescribe different methods of addressing the problem. An administrative statute establishes how a particular business in a <page-number citation-index="1" label="713">*713</page-number>“closely regulated” industry should be operated, setting forth rules to guide an operator’s conduct of the business and allowing government officials to ensure that those rules are followed. Such a regulatory approach contrasts with that of the penal laws, a major emphasis of which is the punishment of individuals for specific acts of behavior.</p>
<p id="b751-5">In <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>we recognized this fact that both administrative and penal schemes can serve the same purposes by observing that the ultimate purposes of the Gun Control Act were “to prevent violent crime and to assist the States in regulating the firearms traffic within their borders.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>. It is beyond dispute that certain state penal laws had these same purposes. Yet the regulatory goals of the Gun Control Act were narrower: the Act ensured that “weapons [were] distributed through regular channels and in a traceable manner and [made] possible the prevention of sales to undesirable customers and the detection of the origin of particular firearms.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 315-316</a></span>. The provisions of the Act, including those authorizing the warrantless inspections, served these immediate goals and also contributed to achieving the same ultimate purposes that the penal laws were intended to achieve.</p>
<p id="b751-6">This case, too, reveals that an administrative scheme may have the same ultimate purpose as penal laws, even if its regulatory goals are narrower. As we have explained above, New York, like many States, faces a serious social problem in automobile theft and has a substantial interest in regulating the vehicle-dismantling industry because of this problem. The New York penal laws address automobile theft by punishing it or the possession of stolen property, including possession by individuals in the business of buying and selling property. See n. 6, <em>supra.</em><footnotemark><em>23</em></footnotemark><em> </em>In accordance with its interest <page-number citation-index="1" label="714">*714</page-number>in regulating the automobile-junkyard industry, the State also has devised a regulatory manner of dealing with this problem. Section 415-a, as a whole, serves the regulatory goals of seeking to ensure that vehicle dismantlers are legitimate businesspersons and that stolen vehicles and vehicle parts passing through automobile junkyards can be identified.<footnotemark>24</footnotemark> In particular, §415-a5 was designed to contribute to these goals, as explained at the time of its passage:</p>
<blockquote id="b752-5">“This bill attempts to provide enforcement not only through means of law enforcement but by making it unprofitable for persons to operate in the stolen car field.</blockquote>
<blockquote id="b753-4"><page-number citation-index="1" label="715">*715</page-number>“The various businesses which are engaged in this operation have been studied and the control and requirements on the businesses have been written in a manner which would permit the persons engaged in the business to legally operate in a manner conducive to good business practices while making it extremely difficult for a person to profitably transfer a stolen vehicle or stolen part. The general scheme is to identify every person who may legitimately be involved in the operation and to provide a record keeping system which will enable junk vehicles and parts to be traced back to the last legitimately registered or titled owner. Legitimate businessmen engaged in this field have complained with good cause that the lack of comprehensive coverage of the field has put them at a disadvantage with persons who currently are able to operate outside of statute and regulations. They have also legitimately complained that delays inherent in the present statutory regulation and onerous record keeping requirements have made profitable operation difficult.</blockquote>
<blockquote id="b753-5">“The provisions of this bill have been drafted after consultation with respected members of the various industries and provides <em>[sic] </em>a more feasible system of controlling traffic in stolen vehicles and parts.” Letter of Stanley M. Gruss, Deputy Commissioner and Counsel, to Richard A. Brown, Counsel to the Governor (June 20, 1979), 1979 Bill Jacket.</blockquote>
<p id="b753-6">Accordingly, to state that §415-a5 is “really” designed to gather evidence to enable convictions under the penal laws is to ignore the plain administrative purposes of § 415-a, in general, and § 415-a5, in particular.</p>
<p id="b753-7">If the administrative goals of § 415-a5 are recognized, the difficulty the Court of Appeals perceives in allowing inspecting officers to examine vehicles and vehicle parts even in the absence of records evaporates. The regulatory purposes of § 415-a5 certainly are served by having the inspecting offi<page-number citation-index="1" label="716">*716</page-number>cers compare the records of a particular vehicle dismantler with vehicles and vehicle parts in the junkyard. The purposes of maintaining junkyards in the hands of legitimate businesspersons and of tracing vehicles that pass through these businesses, however, <em>also </em>are served by having the officers examine the operator’s inventory even when the operator, for whatever reason, fails to produce the police book.<footnotemark>25</footnotemark> Forbidding inspecting officers to examine the inventory in this situation would permit an illegitimate vehicle dismantler to thwart the purposes of the administrative scheme and would have the absurd result of subjecting his counterpart who maintained records to a more extensive search.<footnotemark>26</footnotemark></p>
<p id="b754-4">Nor do we think that this administrative scheme is unconstitutional simply because, in the course of enforcing it, an inspecting officer may discover evidence of crimes, besides violations of the scheme itself. In <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>the pawnshop operator was charged not only with a violation of the recordkeeping provision, pursuant to which the inspection was made, but also with other violations detected during the inspection, see <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#313" aria-description="Citation for case: United States v. Biswell">406 U. S., at 313, n. 2</a></span>, and convicted of a failure to pay an occupational tax for dealing in specific firearms, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell">id., at 312-313</a></span>. The discovery of evidence of crimes in the course of an otherwise proper administrative inspection does not render that search illegal or the administrative scheme suspect. Cf. <em>United States </em>v. <em>Villamonte-Marquez, </em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#583" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 583-584</a></span>, and n. 3 (1983).<footnotemark>27</footnotemark></p>
<p id="b755-4"><page-number citation-index="1" label="717">*717</page-number>Finally, we fail to see any constitutional significance in the fact that police officers, rather than “administrative” agents, are permitted to conduct the § 415-a5 inspection. The significance respondent alleges lies in the role of police officers as enforcers of the penal laws and in the officers’ power to arrest for offenses other than violations of the administrative scheme. It is, however, important to note that state police officers, like those in New York, have numerous duties in addition to those associated with traditional police work. See <em>People </em>v. <em>De Bour, </em>40 N. Y. 2d 210, 218, <span class="citation" data-id="5530768"><a href="/opinion/5682261/people-v-de-bour/#568" aria-description="Citation for case: People v. De Bour">352 N. E. 2d 562, 568</a></span> (1976) (“To consider the actions of the police solely in terms of arrest and criminal process is an unnecessary distortion”); see also ABA Standards for Criminal Justice 1-1.1(b) and commentary (2d ed. 1980, Supp. 1982). As a practical matter, many States do not have the resources to assign the enforcement of a particular administrative scheme to a specialized agency. So long as a regulatory scheme is properly administrative, it is not rendered illegal by the fact that the inspecting officer has the power to arrest individuals for violations other than those created by the scheme itself.<footnotemark>28</footnotemark> In <page-number citation-index="1" label="718">*718</page-number>sum, we decline to impose upon the States the burden of requiring the enforcement of their regulatory statutes to be carried out by specialized agents.</p>
<p id="b756-4">V</p>
<p id="b756-5">Accordingly, the judgment of the New York Court of Appeals is reversed, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p id="b756-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b732-6"> This statute reads in pertinent part:</p>
<blockquote id="b732-7">“Records and identification, (a) Any records required by this section shall apply only to vehicles or parts of vehicles for which a certificate of title has been issued by the commissioner [of the Department of Motor Vehicles] or which would be eligible to have such a certificate of title issued. Every person required to be registered pursuant to this section shall maintain a record of all motor vehicles, trailers, and major component parts thereof, coming into his possession together with a record of the disposition of any such motor vehicle, trailer or part thereof and shall maintain proof of ownership for any motor vehicle, trailer or major component part thereof while in his possession. Such records shall be maintained in a manner and form prescribed by the commissioner. The commissioner may, by regulation, exempt vehicles or major component parts of vehicles from all or a portion of the record keeping requirements based upon the age of the vehicle if he deems that such record keeping requirements would serve no substantial value. Upon request of an agent of the commissioner or of any police officer and during his regular and usual business hours, a vehicle dismantler shall produce such records and permit said agent or police officer to examine them and any vehicles or parts of vehicles which are subject to the record keeping requirements of this section and which are on the premises. . . . The failure to produce such records or to permit such inspection on the part of any person required to be registered pursuant to this section as required by this paragraph shall be a class A misdemeanor.”</blockquote>
</footnote>
<footnote label="2">
<p id="b732-8"> It was unclear from the record why, on that particular day, Burger’s junkyard was selected for inspection. Tr. 23-24. The junkyards designated for inspection apparently were selected from a list of such businesses compiled by New York City police detectives. <em>Id., </em>at 24.</p>
</footnote>
<footnote label="3">
<p id="b732-9"> An individual operating a vehicle-dismantling business in New York is required to have a license:</p>
<blockquote id="b732-10">“Definition and registration of vehicle dismantlers. A vehicle dis-mantler is any person who is engaged in the business of acquiring motor vehicles or trailers for the purpose of dismantling the same for parts or reselling such vehicles as scrap. No person shall engage in the business of or <page-number citation-index="1" label="695">*695</page-number>operate as a vehicle dismantler unless there shall have been issued to him a registration in accordance with the provisions of this section. A violation of this subdivision shall be a class E felony.” N. Y. Veh. &amp; Traf. Law § 415-al (McKinney 1986).</blockquote>
</footnote>
<footnote label="4">
<p id="b733-8"> There appears to have been some initial confusion among the inspecting officers as to whether Burger had not compiled a police book or whether, at the moment of the inspection, it simply was not in his possession. See Tr. 6, 30, 46-47, 59-60.</p>
</footnote>
<footnote label="5">
<p id="b733-9"> The officers also determined that Burger possessed a wheelchair and a handicapped person’s walker that had been located in a stolen vehicle. See <em>id., </em>at 8-11, 13, 34-36.</p>
</footnote>
<footnote label="6">
<p id="b733-10"> Respondent was charged with two counts of criminal possession of stolen property in the second degree in violation of a New York statute that, at that time, read:</p>
<blockquote id="b733-11">“A person is guilty of criminal possession of stolen property in the second degree when he knowingly possesses stolen property, with intent to benefit himself or a person other than an owner thereof or to impede the recovery by an owner thereof, and when:</blockquote>
<blockquote id="b733-12">“1. The value of the property exceeds two hundred fifty dollars; or</blockquote>
<blockquote id="b733-13">“3. He is a pawnbroker or is in the business of buying, selling or otherwise dealing in property ....</blockquote>
<blockquote id="b733-14">“Criminal possession of stolen property in the second degree is a class E felony.” N. Y. Penal Law § 165.45 (McKinney 1975).</blockquote>
<p id="b733-15">Burger also was charged with three counts of criminal possession of stolen property in the third degree pursuant to the following provision of a New York statute:</p>
<blockquote id="AXq"><page-number citation-index="1" label="696">*696</page-number>“A person is guilty of criminal possession of stolen property in the third degree when he knowingly possesses stolen property, with intent to benefit himself or a person other than an owner thereof or to impede the recovery by an owner thereof.</blockquote>
<blockquote id="AyG">“Criminal possession of stolen property in the third degree is a class A misdemeanor.” N. Y. Penal Law § 165.40 (McKinney 1975).</blockquote>
</footnote>
<footnote label="7">
<p id="b734-12"> In <em>People </em>v. <em>Pace, </em>the Appellate Division was faced with a situation in which officers had conducted a warrantless search of an automobile salvage yard immediately after having their suspicions aroused about criminal activity there. The court did not find the exception for warrantless administrative inspections applicable in that situation, 101 App. Div. 2d, at 340, 475 N. Y. S. 2d, at 446, but made the following footnote remark:</p>
<blockquote id="b734-13">“Subdivision 5 of section 415-a of the Vehicle and Traffic Law, the statute under which the police officers said they were acting, has no application. While this section requires dismantlers to keep a police book, the book was missing when the officers entered and it would thus have been impossible for the officers to exercise the alleged implied authority to compare the book entries to the contents of the yard.” <em>Id., </em>at 339, n. 1, 475 N. Y. S. 2d, at 445, n. 1.</blockquote>
<p id="b734-14">Respondent construed this footnote to mean that police officers had to obtain a search warrant if a vehicle dismantler did not produce a police book <page-number citation-index="1" label="697">*697</page-number>and thus they could not conduct a warrantless inspection in the absence of this book. See <span class="citation" data-id="6204869"><a href="/opinion/6336287/camphill-special-schools-inc-v-prentice/#711" aria-description="Citation for case: Camphill Special Schools, Inc. v. Prentice">126 Misc. 2d 709, 711</a></span>, 479 N. Y. S. 2d 936, 938 (Sup. 1984).</p>
</footnote>
<footnote label="8">
<p id="b735-8"> In addition, the court determined that the search was proper under New York City Charter and Admin. Code § 436 (Supp. 1985). <span class="citation" data-id="6204687"><a href="/opinion/6336105/people-v-burger/#712" aria-description="Citation for case: People v. Burger">125 Misc. 2d, at 712-715</a></span>, 479 N. Y. S. 2d, at 939-940. That section reads:</p>
<blockquote id="b735-9">“The commissioner [of the Police Department] shall possess powers of general supervision and inspection over all licensed and unlicensed pawnbrokers, vendors, junkshop keepers, junk boatmen, cartmen, dealers in second-hand merchandise and auctioneers within the city; and in connection with the performance of any police duties he shall have power to examine such persons, their clerks and employees and their books, business premises, and any articles of merchandise in their possession. A refusal or neglect to comply in any respect with the provisions of this section on the part of any pawnbroker, vendor, junkshop keeper, junk boatman, cart-man, dealer in second-hand merchandise or auctioneer, or any clerk or employee of any thereof shall be triable by a judge of the criminal court and punishable by not more than thirty days’ imprisonment, or by a fine of not more than fifty dollars, or both.”</blockquote>
</footnote>
<footnote label="9">
<p id="b735-10"> The Court of Appeals found that the question of the constitutionality of the statute and charter was squarely presented by this case, as it had not been in <em>People </em>v. <em>Pace, </em>because there was no dispute that the inspection was made pursuant to those provisions. 67 N. Y. 2d, at 342-343, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#928" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 928</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b736-6"> For similar reasons, the Court of Appeals concluded that Charter § 436 also violated the Fourth Amendment’s prohibition on unreasonable searches and seizures. 67 N. Y. 2d, at 344-346, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929-930</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b736-7"> Numerous States have provisions for the warrantless inspections of vehicle dismantlers and automobile junkyards. See, <em>e. g., </em><span class="citation no-link">Ala. Code §40-12-419</span> (1985); <span class="citation no-link">Ariz. Rev. Stat. Ann. §28</span>-1307C (Supp. 1986); Ark. Stat. Ann. §75-1803 (1979); Cal. Veh. Code Ann. §§ 2805(a) and (c) (West Supp. 1987); <span class="citation no-link">Conn. Gen. Stat. §14</span>-67m(a) (Supp. 1987); Del. Code Ann., Tit. 21, § 6717(a) (1985); <span class="citation no-link">Fla. Stat. §812.055</span> (Supp. 1987); <span class="citation no-link">Ga. Code Ann. §43-48-16</span> (1984); Ill. Rev. Stat., ch. 95½, ¶5-403 (Supp. 1986); <span class="citation no-link">Ind. <page-number citation-index="1" label="699">*699</page-number>Code §§ 9-1-3.6</span>-10(a) and (d) and 9-1-3.6-12 (1979 and Supp. 1986); <span class="citation no-link">Iowa Code §§ 321.90</span>(3)(b) and 321.95 (1985); <span class="citation no-link">Kan. Stat. Ann. §8-2408</span>(c) (1982); Ky. Rev. Stat. §177.935(7) (1985); La. Rev. Stat. Ann. §32:757 (West Supp. 1987); Me. Rev. Stat. Ann., Tit. 29, §2459 (Supp. 1986); Md. Transp. Code Ann. § 15-105 (Supp. 1986); <span class="citation no-link">Mich. Comp. Laws § 257.251</span> (Supp. 1987); <span class="citation no-link">Miss. Code Ann. §27-19-313</span> (1972); <span class="citation no-link">Mo. Rev. Stat. §301.225</span> (Supp. 1986); <span class="citation no-link">Mont. Code Ann. §§ 75-10-503</span> and 75-10-513 (1985); <span class="citation no-link">Nev. Rev. Stat. §482.3263</span> (1986); N. H. Rev. Stat. Ann. §261:132 (1982); N. J. Stat. Ann. § 39.10B-2c (West Supp. 1987); N. M. Stat. Ann. § 66-2-12(A)(4) (1984); Okla. Stat., Tit. 47, §591.6 (Supp. 1987); Ore. Rev. Stat. §810.480 (1985); R. I. Gen. Laws §42-14.2-15 (Supp. 1986); S. C. Code § 56-5-5670(b) (1976); S. D. Codified Laws §§32-6B-38 to 32-6B-40 (Supp. 1987); <span class="citation no-link">Tenn. Code Ann. §55-14-106</span> (1980); Tex. Rev. Civ. Stat. Ann., Art. 6687-2(e) (Vernon Supp. 1987); <span class="citation no-link">Utah Code Ann. §§41-3-23</span>(2) and (4) (Supp. 1987); Vt. Stat. Ann., Tit. 23, §466 (1978); Va. Code §46.1-550.12 (Supp. 1986); <span class="citation no-link">Wash. Rev. Code §§46.80.080</span>(5) and 46.80.150 (1970); W. Va. Code § 17A-6-25 (1986); <span class="citation no-link">Wis. Stat. § 218.22</span>(4)(c) (1982); Wyo. Stat. § 31-13-112(e)(iii) (1987).</p>
<p id="AXu">Courts have upheld such statutes against federal constitutional attack. See, <em>e. g., Bionic Auto Parts &amp; Sales, Inc. </em>v. <em>Fahner, </em><span class="citation" data-id="427553"><a href="/opinion/427553/bionic-auto-parts-and-sales-inc-v-tyrone-c-fahner/#1081" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Tyrone C. Fahner">721 F. 2d 1072, 1081</a></span> (CA7 1983); <em>People </em>v. <em>Easley, </em><span class="citation" data-id="2123937"><a href="/opinion/2123937/people-v-easley/#445" aria-description="Citation for case: People v. Easley">90 Cal. App. 3d 440, 445</a></span>, <span class="citation" data-id="2123937"><a href="/opinion/2123937/people-v-easley/#399" aria-description="Citation for case: People v. Easley">153 Cal. Rptr. 396, 399</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/899/">444 U. S. 899</a></span> (1979); <em>Moore </em>v. <em>State, </em><span class="citation" data-id="1108128"><a href="/opinion/1108128/moore-v-state/#216" aria-description="Citation for case: Moore v. State">442 So. 2d 215, 216</a></span> (Fla. 1983); <em>People </em>v. <em>Barnes, </em><span class="citation" data-id="1601166"><a href="/opinion/1601166/people-v-barnes/#42" aria-description="Citation for case: People v. Barnes">146 Mich. App. 37, 42</a></span>, <span class="citation" data-id="1601166"><a href="/opinion/1601166/people-v-barnes/#466" aria-description="Citation for case: People v. Barnes">379 N. W. 2d 464, 466</a></span> (1985); <em>State </em>v. <em>Zinmeister, </em><span class="citation" data-id="3778084"><a href="/opinion/4022001/state-v-zinmeister/#318" aria-description="Citation for case: State v. Zinmeister">27 Ohio App. 3d 313, 318</a></span>, <span class="citation" data-id="3778084"><a href="/opinion/4022001/state-v-zinmeister/#65" aria-description="Citation for case: State v. Zinmeister">501 N. E. 2d 59, 65</a></span> (1985); see also <em>State </em>v. <em>Tindell, </em><span class="citation" data-id="2123138"><a href="/opinion/2123138/state-v-tindell/#483" aria-description="Citation for case: State v. Tindell">272 Ind. 479, 483</a></span>, <span class="citation" data-id="2123138"><a href="/opinion/2123138/state-v-tindell/#748" aria-description="Citation for case: State v. Tindell">399 N. E. 2d 746, 748</a></span> (1980); <em>Shirley </em>v. <em>Commonwealth, </em><span class="citation" data-id="1244252"><a href="/opinion/1244252/shirley-v-commonwealth/#57" aria-description="Citation for case: Shirley v. Commonwealth">218 Va. 49, 57-58</a></span>, <span class="citation" data-id="1244252"><a href="/opinion/1244252/shirley-v-commonwealth/#436" aria-description="Citation for case: Shirley v. Commonwealth">235 S. E. 2d 432, 436-437</a></span> (1977). But see <em>People </em>v. <em>Krull, </em><span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#116" aria-description="Citation for case: People v. Krull">107 Ill. 2d 107, 116-117</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#707" aria-description="Citation for case: People v. Krull">481 N. E. 2d 703, 707-708</a></span> (1985), rev’d, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340</a></span> (1987); <em>State </em>v. <em>Galio, </em>92 N. M. 266, 268-269, <span class="citation" data-id="9611504"><a href="/opinion/1382601/state-v-galio/#46" aria-description="Citation for case: State v. Galio">587 P. 2d 44, 46-47</a></span> (1978).</p>
</footnote>
<footnote label="12">
<p id="b739-7"> We explained in <em>Donovan </em>v. <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey</a></span>: </em>“If the length of regulation were the only criterion, absurd results would occur. Under appellees’ view, new or emerging industries, including ones such as the nuclear power industry that pose enormous potential safety and health problems, <page-number citation-index="1" label="702">*702</page-number>could never be subject to warrantless searches even under the most carefully structured inspection program simply because of the recent vintage of regulation.” <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#606" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 606</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b741-5"> Because we find the inspection at issue here constitutional under § 415-a5, we have no reason to reach the question of the constitutionality of §436 of the New York City Charter. Moreover, because the Court of Appeals addressed only the general question concerning the constitutionality of the administrative inspection, not the specific question whether the search and seizure of the wheelchair and walker were within the scope of the inspection, we do not reach here this latter issue.</p>
</footnote>
<footnote label="14">
<p id="b742-4"> The New York Court of Appeals did not imply that automobile junkyards were <em>not </em>a “closely regulated” business in that State. Rather, it found fault with one aspect of the administrative statutes regulating these junkyards. 67 N. Y. 2d, at 344-345, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929-930</a></span>. In his brief in opposition to the petition for certiorari, respondent appears to concede that this industry in New York is “closely regulated” by his statement that the New York Legislature could enact a ‘“comprehensive regulatory scheme’ ” directed at the industry. Brief in Opposition 3.</p>
</footnote>
<footnote label="15">
<p id="b742-5"> Under § 415-al, “[n]o person shall engage in the business of or operate as a vehicle dismantler unless there shall have been issued to him a registration in accordance with the provisions of this section.” In making an application for a registration, the operator must provide “a listing of all felony convictions and all other convictions relating to the illegal sale or possession of a motor vehicle or motor vehicle parts, and a listing of all arrests for any such violations by the applicant and any other person required to be named in such application.” § 415-a2. Section 415-a3 requires that the operator pay a registration fee, and § 415-a4 stipulates that “no registration shall be issued or renewed unless the applicant has a permanent place of business at which the activity requiring registration is performed which conforms to section one hundred thirty-six of the general municipal law as such section applies and to all local laws or ordinances and the applicant and all persons having a financial interest in the business have been determined by the commissioner to be fit persons to engage in such business.”</p>
</footnote>
<footnote label="16">
<p id="b743-6"> The broad extent of the regulation of the vehicle-dismantling industry further is shown by the fact that § 415-a regulates the activities not only of vehicle dismantlers but also of those in similar businesses, such as salvage pool operators, § 415-al-a, mobile ear crushers, § 415-al-b, itinerant vehicle collectors, § 415-al-e, vehicle rebuilders, § 415-a8, scrap processors, § 415-a9, and scrap collectors and repair shops, § 415-alO. Moreover, the Commissioner of the Department of Motor Vehicles has promulgated regulations dealing specifically with this industry: e. <em>g., </em>N. Y. Comp. Codes, Rules &amp; Regs., Tit. 15, § 81.2 (1986) (registration); § 81.8 (procedures upon acquisition of junk and salvage vehicles); §81.10 (vehicle identification numbers); §81.12 (records).</p>
<p id="b743-7"><em>Amici </em>argue that § 415-a does not create a truly administrative scheme, because its provisions are not sufficiently voluminous. See Brief for American Civil Liberties Union et al. as <em>Amici Curiae </em>34-36. Although the number of regulations certainly is a factor in the determination whether a particular business is “closely regulated,” the sheer quantity of pages of statutory material is not dispositive of this question. Rather, the proper focus is on whether the “regulatory presence is sufficiently comprehensive and defined that the owner of commercial property cannot help but be aware that his property will be subject to periodic inspections undertaken for specific purposes.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 600</a></span>. Section 415-a plainly satisfies this criterion.</p>
</footnote>
<footnote label="17">
<p id="b744-5"> A member of the automobile-junkyard industry described it this way:</p>
<blockquote id="b744-6">“Webster says junk is old metal, rags, and rubbish. The word ‘junk’ can also be used as a verb, and as such would mean to discard. I represent an industry that buys vehicles which are no longer suitable for transportation. These vehicles have been wrecked, damaged, or have otherwise become inoperative. They are taken apart by members of our industry. The components that are still usable are made available to garages, body shops, and the general public as used parts for repair of other vehicles. The portion of the vehicle that is not suitable for parts is passed on to a scrap processor who then transforms the hulk, or the remnants, into a product suitable for resmelting purposes.” Junkyards &amp; Solid Waste Disposal in the Highway Environment, Proceedings of National Seminar, June 10-11, 1975, p. 19 (1976) (statement of Donald J. Rouse, National Association of Auto and Truck Recyclers, now known as Automotive Dismantlers and Recyclers of America).</blockquote>
</footnote>
<footnote label="18">
<p id="b745-8"> In fact, by assuming that Charter § 436 with its use of the terms “junk-shop keepers” and “dealers in second-hand merchandise,” see n. 8, <em>supra, </em>could be applied to respondent, the New York Court of Appeals understood that a vehicle dismantler fell within the scope of those terms. See also <em>People </em>v. <em>Cusumano, </em>108 App. Div. 2d 752, 754, 484 N. Y. S. 2d 909, 912 (1985).</p>
</footnote>
<footnote label="19">
<p id="b747-6"> A similar concern with stemming the social plague of automobile theft has motivated other States to pass legislation aimed at the vehicle-dismantling industry. See, <em>e. g., </em>Ill. Rev. Stat., eh. 9572, ¶ 5-100-1 (Supp. 1985) (legislative finding that “crimes involving the theft of motor vehicles and their parts have risen steadily over the past years, with a resulting loss of millions of dollars to the residents of this State”).</p>
</footnote>
<footnote label="20">
<p id="b747-7"> See Governor’s Message approving L. 1979, chs. 691 and 692, 1979 N. Y. Laws 1826, 1827 (McKinney) (“By making it difficult to traffic in stolen vehicles and parts, it can be anticipated that automobile theft problems will be decreased and the cost to insurance companies and the public <page-number citation-index="1" label="710">*710</page-number>may be reduced”). As the Illinois Legislature found in passing regulations aimed at this industry,</p>
<blockquote id="Afr">“(2) essential to the criminal enterprise of motor vehicle theft operations is the ability of thieves to transfer or sell stolen vehicles or their parts through legitimate commercial channels making them available for sale to the automotive industry; and (3) motor vehicle dealers, used parts dealers, scrap processors, automotive parts recyclers, and rebuilders are engaged in a type of business which often exposes them and their operations to pressures and influences from motor vehicle thieves; and (4) elements of organized crime are constantly attempting to take control of businesses engaged in the sale and repair of motor vehicles so as to further their own criminal interests.” Ill. Rev. Stat., ch. 9572, ¶ 5-100-1 (1985).</blockquote>
<p id="A82">See also <span class="citation no-link">Kan. Stat. Ann. § 8-2402</span> (1982); <span class="citation no-link">Nev. Rev. Stat. § 482.318</span> (1985).</p>
</footnote>
<footnote label="21">
<p id="b749-6"> Respondent contends that § 415-a5 is unconstitutional because it fails to limit the number of searches that may be conducted of a particular business during any given period. Brief for Respondent 12. While such limitations, or the absence thereof, are a factor in an analysis of the adequacy of a particular statute, they are not determinative of the result so long as the statute, as a whole, places adequate limits upon the discretion of the inspecting officers. Indeed, we have approved statutes authorizing war-rantless inspections even when such statutes did not establish a fixed number of inspections for a particular time period. See <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 312, n. 1</a></span> (1972). And we have suggested that, in some situations, inspections must be conducted frequently to achieve the purposes of the statutory scheme. <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 316</a></span> (“Here, if inspection is to be effective and serve as a credible deterrent, unannounced, even <em>frequent, </em>inspections are essential”) (emphasis added).</p>
</footnote>
<footnote label="22">
<p id="b750-8"> With respect to the adequacy of the statutory procedures, this case is indistinguishable from <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>. </em>There, the regulatory provisions of the Gun Control Act permitted warrantless inspections of <em>both </em>records <em>and </em>inventory “at all reasonable times.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 312, n. 1</a></span>. The Court held that the statute gave a firearms dealer adequate notice of “the purposes of the inspector [and] the limits of his task.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 316</a></span>.</p>
</footnote>
<footnote label="23">
<p id="b751-7"> The penal laws often are changed in response to the growth of a particular type of crime. For example, in 1986 New York amended its definition of grand larceny to include the following provision:</p>
<blockquote id="AbA"><page-number citation-index="1" label="714">*714</page-number>“A person is guilty of grand larceny in the fourth degree when he steals property and when:</blockquote>
<blockquote id="Aci">“8. The value of the property exceeds one hundred dollars and the property consists of a motor vehicle, as defined in section one hundred twenty-five of the vehicle and traffic law, other than a motorcycle, as defined in section one hundred twenty-three of such law.” 1986 N. Y. Laws, ch. 515, § 1 (McKinney), codified at N. Y. Penal Law § 155.30 (McKinney Supp. 1987).</blockquote>
</footnote>
<footnote label="24">
<p id="b752-8"> See, <em>e. g., </em>Memorandum of State Department of Motor Vehicles in support of 1973 N. Y. Laws, eh. 225, 1973 N. Y. Laws 2166, 2167 (McKinney) (purpose of § 415-a “is to provide a system of record keeping so that vehicles can be traced through junk yards and to assure that such junk yards are run by legitimate business men rather than by auto theft rings”); Letter of John D. Caemmerer, Chairman of Senate Committee on Transportation, to Michael Whiteman, Counsel to the Governor (Apr. 12, 1973), reprinted in Governor’s Bill Jacket, L. 1973, eh. 225, p. 15 (1973 Bill Jacket) (“This bill establishes much needed safeguards for an industry which can be readily infiltrated by those wishing to dispose of stolen automobiles or automobile parts”); Letter of Peter M. Pryor, Chairman of New York State Consumer Protection Board, to Michael Whiteman, Counsel to the Governor (Apr. 18, 1973), 1973 Bill Jacket, p. 6 (“Organized crime has used the junk and salvage industry as a convenient staging ground for illicit activities concerning motor vehicles as well as for operations into other areas. The proposed legislation opens the junk and salvage business to the scrutiny of the police and the Department of Motor Vehicles thereby reducing the possibility of utilizing such dealerships as covers for covert businesses”).</p>
</footnote>
<footnote label="25">
<p id="b754-5"> Failure to produce a record is a misdemeanor, § 415-a5, which can be a ground for suspension of the operator’s license, § 415-a6. This suspension serves to remove illegitimate operators from the industry.</p>
</footnote>
<footnote label="26">
<p id="b754-6"> Indeed, in <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>we found no constitutional problem with a statute that authorized inspection both of records and inventory, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell">406 U. S., at 312, n. 1</a></span>, and with an actual inspection of a dealer’s premises despite the fact that the dealer’s records were not properly maintained, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#313" aria-description="Citation for case: United States v. Biswell"><em>id., </em>at 313, n. 2</a></span>.</p>
</footnote>
<footnote label="27">
<p id="b754-7"> The legislative history of § 415-a, in general, and § 415-a5, in particular, reveals that the New York Legislature had proper regulatory purposes for enacting the administrative scheme and was not using it as a <page-number citation-index="1" label="717">*717</page-number>“pretext” to enable law enforcement authorities to gather evidence of penal law violations. See <em>supra, </em>at 714-715 and n. 24; see also <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#351" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 351</a></span> (1987) (“[W]e are given no basis for believing that legislators are inclined to subvert their oaths and the Fourth Amendment”). There is, furthermore, no reason to believe that the instant inspection was actually a “pretext” for obtaining evidence of respondent’s violation of the penal laws. It is undisputed that the inspection was made solely pursuant to the administrative scheme. In fact, because the search here was truly a § 415-a5 inspection, the Court of Appeals was able to reach in this case, as it could not in <em>People </em>v. <em>Pace, </em>65 N. Y. 2d 684, <span class="citation no-link">481 N. E. 2d 250</span> (1985), the question of the constitutionality of the statute. See 67 N. Y. 2d, at 342-343, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#928" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 928</a></span>; see also n. 7, <em>supra.</em></p>
</footnote>
<footnote label="28">
<p id="b755-6"> In <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>the search in question was conducted by a city police officer and by a United States Treasury agent, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell">406 U. S., at 312</a></span>, the latter being authorized to make arrests for federal crimes. See <span class="citation no-link">27 CFR § 70.28</span> (1986). The Internal Revenue agents involved in the search in <em>Colonnade Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#73" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72, 73</a></span> (1970), had similar powers. See <span class="citation no-link">26 U. S. C. § 7608</span>(a).</p>
</footnote>
</opinion>
```

---
