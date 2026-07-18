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

## GROUP: content/cases/Monroe v. Pape.md  (`case`, 6 assertions)

### content_page

```
---
title: "Monroe v. Pape"
type: case
citation: "365 U.S. 167 (1961)"
parallel_cite: "81 S. Ct. 473; 5 L. Ed. 2d 492"
neutral_cite: 1961 U.S. LEXIS 1687
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-02-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1961-02-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Monroe v. Pape
  varies_by_point: true
  scope_note: "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law."
  point_overrides:
    - point: legacy-limited-monroe-v-pape
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Monell v. Department of Social Services
          cluster_id: 109881
          cite: 436 U.S. 658
          field_ii: limited
      scope_note: "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106170/monroe-v-pape/"
  cluster_id: 106170
  opinion_id: 106170
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Anchor"
related: ["[[Monell v. Department of Social Services]]", "[[Harlow v. Fitzgerald]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "section-1983", "under-color-of-law", "civil-rights", "federal-remedy"]
holding: "Revived § 1983 as a real federal remedy: 'under color of' state law reaches the MISUSE of authority an officer possesses by virtue of…"
lake:
  record_id: Monroe v. Pape
  status: verified
  projected_at: 2026-07-06
---

# Monroe v. Pape

*365 U.S. 167 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Thirteen Chicago police officers, without a warrant, broke into the Monroe family's home at dawn, ransacked it, made the family stand naked, and detained Mr. Monroe for questioning. The Monroes sued the officers and the City of Chicago under § 1983. The lower courts dismissed, reading § 1983 not to reach the officers' conduct.

## Issue
Whether officers who abuse their authority act "under color of" state law for purposes of § 1983, and whether the federal remedy requires first exhausting state remedies.

## Rule
"Under color of" state law reaches the misuse of authority. The Court reaffirmed that "Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken 'under color of' state law." — 365 U.S. at 184 (quoting *United States v. Classic*). ^pin-184

The Court further held that the § 1983 federal remedy is supplementary to any state remedy and need not be sought and refused before the federal action is brought.

## Application
The Chicago officers acted under [[Section 1983 Liability and Qualified Immunity|color of state law]] when they used their police authority to break into and ransack the Monroes' home and detain Mr. Monroe, even though their conduct also violated state law. The Monroes could therefore sue the officers under § 1983 without first pursuing a state remedy. (The Court also held that the City of Chicago was not a suable "person" under § 1983 — a holding later overruled by *[[Monell v. Department of Social Services|Monell]]*.)

## Conclusion
Reversed as to the individual officers; § 1983 reached their misuse of authority under [[Section 1983 Liability and Qualified Immunity|color of state law]].

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Overruled in part by** [[Monell v. Department of Social Services]] (1978), which held that municipalities ARE suable "persons" under § 1983, rejecting *Monroe*'s contrary municipal-immunity holding. *Monroe*'s core "under color of" state-law holding — reviving § 1983 as a federal remedy for the misuse of official authority — remains good law.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *Monroe v. Pape*, 365 U.S. 167 (1961) — https://www.courtlistener.com/opinion/106170/monroe-v-pape/ — pinpoint: 184.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "36a914780e1df162", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "365 U.S. 167 (1961)", "court": "U.S. Supreme Court", "neutral_cite": "1961 U.S. LEXIS 1687", "official_citation_present": true, "parallel_cite": "81 S. Ct. 473; 5 L. Ed. 2d 492", "title": "Monroe v. Pape", "year": "1961"}}
{"assertion_id": "47da8205f4f819e9", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Anchor", "title": "Monroe v. Pape"}}
{"assertion_id": "c1cc813616bd9adf", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Revived § 1983 as a real federal remedy: 'under color of' state law reaches the MISUSE of authority an officer possesses by virtue of…", "title": "Monroe v. Pape"}}
{"assertion_id": "7695e6c25b7e70e1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1961-02-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Monroe v. Pape", "field_i_validity": "caution", "scope_note": "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law.", "title": "Monroe v. Pape", "varies_by_point": "true"}}
{"assertion_id": "c793adc976155082", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Monroe v. Pape"}}
{"assertion_id": "cd69d14056a24a5a", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-monroe-v-pape"}, "payload": {"by": [{"cite": "436 U.S. 658", "cluster_id": "109881", "field_ii": "limited", "name": "Monell v. Department of Social Services"}], "field_i_validity": "caution", "point": "legacy-limited-monroe-v-pape", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "Monroe v. Pape"}}
```

### lake record — Monroe v. Pape

```json
{
  "schema_version": "s2.v1",
  "record_id": "Monroe v. Pape",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Monroe v. Pape",
    "case_name_short": "Monroe",
    "case_name_full": "MONROE Et Al. v. PAPE Et Al.",
    "input_case_name": "Monroe v. Pape",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-02-20",
    "year": 1961,
    "docket": null,
    "cluster_id": 106170,
    "lead_opinion_id": 106170,
    "sibling_ids": [
      106170,
      9422118,
      9422119,
      9422120
    ],
    "absolute_url": "/opinion/106170/monroe-v-pape/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8949295,
        "score": 20,
        "case_name": "Monroe v. Pape"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "365 U.S. 167",
      "volume": "365",
      "reporter": "U.S.",
      "page": "167",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 473",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 492",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 1687",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1687",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "365 U.S. 167",
        "volume": "365",
        "reporter": "U.S.",
        "page": "167",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 473",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 492",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 1687",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1687",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "365 U.S. 167",
    "official_selection": {
      "court_class": "scotus",
      "selected": "365 U.S. 167",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-184",
      "page": null,
      "quote": "state law for purposes of \u00a7 1983, and whether the federal remedy requires first exhausting state remedies. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1961-02-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Monroe v. Pape",
    "varies_by_point": true,
    "scope_note": "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law.",
    "point_overrides": [
      {
        "point": "legacy-limited-monroe-v-pape",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Monell v. Department of Social Services",
            "cluster_id": 109881,
            "cite": "436 U.S. 658",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Overruled in part by Monell v. Department of Social Services (1978) as to municipal liability; the 'under color of' state-law holding remains good law."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Monell v. Department of Social Services",
          "cluster_id": 109881,
          "cite": "436 U.S. 658",
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
          "name": "Gregory Baldwin v. City of Estherville, Iowa",
          "cluster_id": 4629600,
          "cite": [
            "929 N.W.2d 691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Keyon Harrison v. Curt Vanderkooi",
          "cluster_id": 4522518,
          "cite": [
            "918 N.W.2d 785",
            "502 Mich. 751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane1_negative"
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
        "journal_ref": "Monroe v. Pape:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Haywood v. Drown",
          "cluster_id": 1983488,
          "cite": [
            "881 N.E.2d 180",
            "9 N.Y.3d 481",
            "851 N.Y.S.2d 84"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane1_negative"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
          "cluster_id": 108375,
          "cite": [
            "29 L. Ed. 2d 619",
            "91 S. Ct. 1999",
            "403 U.S. 388",
            "1971 U.S. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adickes v. S. H. Kress & Co.",
          "cluster_id": 108153,
          "cite": [
            "26 L. Ed. 2d 142",
            "90 S. Ct. 1598",
            "398 U.S. 144",
            "1970 U.S. LEXIS 31"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Younger v. Harris",
          "cluster_id": 108263,
          "cite": [
            "27 L. Ed. 2d 669",
            "91 S. Ct. 746",
            "401 U.S. 37",
            "1971 U.S. LEXIS 136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Regents of State Colleges v. Roth",
          "cluster_id": 108608,
          "cite": [
            "33 L. Ed. 2d 548",
            "92 S. Ct. 2701",
            "408 U.S. 564",
            "1972 U.S. LEXIS 131",
            "1 I.E.R. Cas. (BNA) 23"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scheuer v. Rhodes",
          "cluster_id": 109009,
          "cite": [
            "40 L. Ed. 2d 90",
            "94 S. Ct. 1683",
            "416 U.S. 232",
            "1974 U.S. LEXIS 126",
            "71 Ohio Op. 2d 474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniels v. Williams",
          "cluster_id": 111555,
          "cite": [
            "88 L. Ed. 2d 662",
            "106 S. Ct. 662",
            "474 U.S. 327",
            "1986 U.S. LEXIS 43",
            "54 U.S.L.W. 4090"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mt. Healthy City School District Board of Education v. Doyle",
          "cluster_id": 109574,
          "cite": [
            "50 L. Ed. 2d 471",
            "97 S. Ct. 568",
            "429 U.S. 274",
            "1977 U.S. LEXIS 29",
            "1 I.E.R. Cas. (BNA) 76"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. Carr",
          "cluster_id": 106366,
          "cite": [
            "7 L. Ed. 2d 663",
            "82 S. Ct. 691",
            "369 U.S. 186",
            "1962 U.S. LEXIS 1567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rizzo v. Goode",
          "cluster_id": 109349,
          "cite": [
            "46 L. Ed. 2d 561",
            "96 S. Ct. 598",
            "423 U.S. 362",
            "1976 U.S. LEXIS 42"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
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
        "journal_ref": "Monroe v. Pape:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106170 OR 9422118 OR 9422119 OR 9422120) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTg2NDQ0ODAwMDAwJnM9MjQxMjI2MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106170+OR+9422118+OR+9422119+OR+9422120%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106170 OR 9422118 OR 9422119 OR 9422120)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTczJnM9MTEyODI1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106170+OR+9422118+OR+9422119+OR+9422120%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106170 OR 9422118 OR 9422119 OR 9422120)",
        "reviewed": 29,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 29,
        "triage_read": 0,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106170 OR 9422118 OR 9422119 OR 9422120)",
    "indexed_citing_opinions": 3267,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106170,
        "count": 3043,
        "count_source": "search"
      },
      {
        "opinion_id": 9422118,
        "count": 291,
        "count_source": "search"
      },
      {
        "opinion_id": 9422119,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422120,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4788,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/monroe-v-pape.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MTA3MTYmcz05NDM2MDY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106170+OR+9422118+OR+9422119+OR+9422120%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106170,
        "cited_id": 88661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 89309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 90305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 90728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 90897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 91885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 92917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 93322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 95317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 95877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 97288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 97326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 98516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 98517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 98595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 99058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 100034,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 100544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101446,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 101911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 102086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 103962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104588,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 105227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 105232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 105236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 105511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 106008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1149975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1334132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1378476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1477715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1480162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1485471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1490664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1491816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1497082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1498873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1506239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1555915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1678770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1682433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1811185,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1883596,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1943607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 1975150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2146861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2195375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2245571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2394729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2396750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 2620779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 3413717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 3415036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 3417801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 3424043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106170,
        "cited_id": 5021031,
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
    "date_created": "2026-07-05T14:27:30Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:27:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:27:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:27:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Monroe v. Pape (truncated)

```
<div>
<center><b><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U.S. 167</a></span> (1961)</b></center>
<center><h1>MONROE ET AL.<br>
v.<br>
PAPE ET AL.</h1></center>
<center>No. 39.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 8, 1960.</center>
<center>Decided February 20, 1961.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><span class="star-pagination">*168</span> <i>Donald Page Moore</i> argued the cause for petitioners. With him on the brief were <i>Morris L. Ernst, Ernst Liebman, Charles Liebman</i> and <i>John W. Rogers.</i></p>
<p><i>Sydney R. Drebin</i> argued the cause for respondents. With him on the brief was <i>John C. Melaniphy.</i></p>
<p>MR. JUSTICE DOUGLAS delivered the opinion of the Court.</p>
<p>This case presents important questions concerning the construction of R. S. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, which reads as follows:</p>
<blockquote>"Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any <span class="star-pagination">*169</span> citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress."</blockquote>
<p>The complaint alleges that 13 Chicago police officers broke into petitioners' home in the early morning, routed them from bed, made them stand naked in the living room, and ransacked every room, emptying drawers and ripping mattress covers. It further alleges that Mr. Monroe was then taken to the police station and detained on "open" charges for 10 hours, while he was interrogated about a two-day-old murder, that he was not taken before a magistrate, though one was accessible, that he was not permitted to call his family or attorney, that he was subsequently released without criminal charges being preferred against him. It is alleged that the officers had no search warrant and no arrest warrant and that they acted "under color of the statutes, ordinances, regulations, customs and usages" of Illinois and of the City of Chicago. Federal jurisdiction was asserted under R. S. § 1979, which we have set out above, and <span class="citation no-link">28 U. S. C. § 1343</span><sup>[1]</sup> and <span class="citation no-link">28 U. S. C. § 1331</span>.<sup>[2]</sup></p>
<p><span class="star-pagination">*170</span> The City of Chicago moved to dismiss the complaint on the ground that it is not liable under the Civil Rights Acts nor for acts committed in performance of its governmental functions. All defendants moved to dismiss, alleging that the complaint alleged no cause of action under those Acts or under the Federal Constitution. The District Court dismissed the complaint. The Court of Appeals affirmed, <span class="citation" data-id="249412"><a href="/opinion/249412/james-monroe-v-frank-pape/" aria-description="Citation for case: James Monroe v. Frank Pape">272 F. 2d 365</a></span>, relying on its earlier decision, <i>Stift</i> v. <i>Lynch,</i> <span class="citation" data-id="248177"><a href="/opinion/248177/stift-v-lynch/" aria-description="Citation for case: Stift v. Lynch">267 F. 2d 237</a></span>. The case is here on a writ of certiorari which we granted because of a seeming conflict of that ruling with our prior cases. <span class="citation multiple-matches"><a href="/c/U.%20S./362/926/">362 U. S. 926</a></span>.</p>
<p></p>
<h2>I.</h2>
<p>Petitioners claim that the invasion of their home and the subsequent search without a warrant and the arrest and detention of Mr. Monroe without a warrant and without arraignment constituted a deprivation of their "rights, privileges, or immunities secured by the Constitution" within the meaning of R. S. § 1979. It has been said that when <span class="citation no-link">18 U. S. C. § 241</span> made criminal a conspiracy "to injure, oppress, threaten or intimidate any citizen in the free exercise or enjoyment of any right or privilege secured to him by the Constitution," it embraced only rights that an individual has by reason of his relation to the central government, not to state governments. <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="9420563"><a href="/opinion/104889/united-states-v-williams/" aria-description="Citation for case: United States v. Williams">341 U. S. 70</a></span>. Cf. <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542</a></span>; <i>Ex parte Yarbrough,</i> <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">110 U. S. 651</a></span>; <i>Guinn</i> v. <i>United States,</i> <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U. S. 347</a></span>. But the history of the section of the Civil Rights Act presently involved does not permit such a narrow interpretation.</p>
<p><span class="star-pagination">*171</span> Section 1979 came onto the books as § 1 of the Ku Klux Act of April 20, 1871. <span class="citation no-link">17 Stat. 13</span>. It was one of the means whereby Congress exercised the power vested in it by § 5 of the Fourteenth Amendment to enforce the provisions of that Amendment.<sup>[3]</sup> Senator Edmunds, Chairman of the Senate Committee on the Judiciary, said concerning this section:</p>
<blockquote>"The first section is one that I believe nobody objects to, as defining the rights secured by the Constitution of the United States when they are assailed by any State law or under color of any State law, and it is merely carrying out the principles of the civil rights bill,<sup>[4]</sup> which has since become a part of the Constitution,"<sup>[5]</sup><i>viz.,</i> the Fourteenth Amendment.</blockquote>
<p>Its purpose is plain from the title of the legislation, "An Act to enforce the Provisions of the Fourteenth Amendment to the Constitution of the United States, and for other Purposes." <span class="citation no-link">17 Stat. 13</span>. Allegation of facts constituting a deprivation under color of state authority of a right guaranteed by the Fourteenth Amendment satisfies to that extent the requirement of R. S. § 1979. See <i>Douglas</i> v. <i>Jeannette,</i> <span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/#161" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157, 161-162</a></span>. So far petitioners are on solid ground. For the guarantee against unreasonable searches and seizures contained in the Fourth Amendment has been made applicable to the States by reason of the Due Process Clause of the Fourteenth Amendment. <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>; <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#213" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 213</a></span>.</p>
<p></p>
<h2>II.</h2>
<p>There can be no doubt at least since <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 346-347</a></span>, that Congress has the power to <span class="star-pagination">*172</span> enforce provisions of the Fourteenth Amendment against those who carry a badge of authority of a State and represent it in some capacity, whether they act in accordance with their authority or misuse it. See <i>Home Tel. &amp; Tel. Co.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/#287" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">227 U. S. 278, 287-296</a></span>. The question with which we now deal is the narrower one of whether Congress, in enacting § 1979, meant to give a remedy to parties deprived of constitutional rights, privileges and immunities by an official's abuse of his position. Cf. <i>Williams</i> v. <i>United States,</i> <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">341 U. S. 97</a></span>; <i>Screws</i> v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span>; <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U. S. 299</a></span>. We conclude that it did so intend.</p>
<p>It is argued that "under color of" enumerated state authority excludes acts of an official or policeman who can show no authority under state law, state custom, or state usage to do what he did. In this case it is said that these policemen, in breaking into petitioners' apartment, violated the Constitution<sup>[6]</sup> and laws of Illinois. It is pointed out that under Illinois law a simple remedy is offered for that violation and that, so far as it appears, the courts of Illinois are available to give petitioners that full redress which the common law affords for violence done to a person; and it is earnestly argued that no "statute, ordinance, regulation, custom or usage" of Illinois bars that redress.</p>
<p>The Ku Klux Act grew out of a message sent to Congress by President Grant on March 23, 1871, reading:</p>
<blockquote>"A condition of affairs now exists in some States of the Union rendering life and property insecure and <span class="star-pagination">*173</span> the carrying of the mails and the collection of the revenue dangerous. The proof that such a condition of affairs exists in some localities is now before the Senate. That the power to correct these evils is beyond the control of State authorities I do not doubt; that the power of the Executive of the United States, acting within the limits of existing laws, is sufficient for present emergencies is not clear. Therefore, I urgently recommend such legislation as in the judgment of Congress shall effectually secure life, liberty, and property, and the enforcement of law in all parts of the United States. . . ."<sup>[7]</sup></blockquote>
<p>The legislationin particular the section with which we are now concernedhad several purposes. There are threads of many thoughts running through the debates. One who reads them in their entirety sees that the present section had three main aims.</p>
<p><i>First,</i> it might, of course, override certain kinds of state laws. Mr. Sloss of Alabama, in opposition, spoke of that object and emphasized that it was irrelevant because there were no such laws:<sup>[8]</sup></p>
<blockquote>"The first section of this bill prohibits any invidious legislation by States against the rights or privileges of citizens of the United States. The object of this section is not very clear, as it is not pretended by its advocates on this floor that any State has passed any laws endangering the rights or privileges of the colored people."</blockquote>
<p><i>Second,</i> it provided a remedy where state law was inadequate. That aspect of the legislation was summed up as follows by Senator Sherman of Ohio:</p>
<blockquote>". . . it is said the reason is that any offense may be committed upon a negro by a white man, and a <span class="star-pagination">*174</span> negro cannot testify in any case against a white man, so that the only way by which any conviction can be had in Kentucky in those cases is in the United States courts, because the United States courts enforce the United States laws by which negroes may testify."<sup>[9]</sup></blockquote>
<p>But the purposes were much broader. The <i>third</i> aim was to provide a federal remedy where the state remedy, though adequate in theory, was not available in practice. The opposition to the measure complained that "It overrides the reserved powers of the States,"<sup>[10]</sup> just as they argued that the second section of the bill "absorb[ed] the entire jurisdiction of the States over their local and domestic affairs."<sup>[11]</sup></p>
<p>This Act of April 20, 1871, sometimes called "the third `force bill,'" was passed by a Congress that had the Klan "particularly in mind."<sup>[12]</sup> The debates are replete with references to the lawless conditions existing in the South in 1871. There was available to the Congress during these debates a report, nearly 600 pages in length, dealing with the activities of the Klan and the inability of the state governments to cope with it.<sup>[13]</sup> This report was drawn on by many of the speakers.<sup>[14]</sup> It was not the unavailability of state remedies but the failure of certain States to enforce the laws with an equal hand that furnished <span class="star-pagination">*175</span> the powerful momentum behind this "force bill." Mr. Lowe of Kansas said:</p>
<blockquote>"While murder is stalking abroad in disguise, while whippings and lynchings and banishment have been visited upon unoffending American citizens, the local administrations have been found inadequate or unwilling to apply the proper corrective. Combinations, darker than the night that hides them, conspiracies, wicked as the worst of felons could devise, have gone unwhipped of justice. Immunity is given to crime, and the records of the public tribunals are searched in vain for any evidence of effective redress."<sup>[15]</sup></blockquote>
<p>Mr. Beatty of Ohio summarized in the House the case for the bill when he said:</p>
<blockquote>". . . certain States have denied to persons within their jurisdiction the equal protection of the laws. The proof on this point is voluminous and unquestionable. . . . [M]en were murdered, houses were burned, women were outraged, men were scourged, and officers of the law shot down; and the State made no successful effort to bring the guilty to punishment or afford protection or redress to the outraged and innocent. The State, from lack of power or inclination, practically denied the equal protection of the law to these persons."<sup>[16]</sup></blockquote>
<p>While one main scourge of the evilperhaps the leading onewas the Ku Klux Klan,<sup>[17]</sup> the remedy created was <span class="star-pagination">*176</span> not a remedy against it or its members but against those who representing a State in some capacity were <i>unable</i> or <i>unwilling</i> to enforce a state law. Senator Osborn of Florida put the problem in these terms:<sup>[18]</sup></p>
<blockquote>"That the State courts in the several States have been unable to enforce the criminal laws of their respective States or to suppress the disorders existing, and in fact that the preservation of life and property in many sections of the country is beyond the power of the State government, is a sufficient reason why Congress should, so far as they have authority under the Constitution, enact the laws necessary for the protection of citizens of the United States. The question of the constitutional authority for the requisite legislation has been sufficiently discussed."</blockquote>
<p>There was, it was said, no quarrel with the state laws on the books. It was their lack of enforcement that was the nub of the difficulty. Speaking of conditions in Virginia, Mr. Porter of that State said:<sup>[19]</sup></p>
<blockquote>"The outrages committed upon loyal men there are under the forms of law."</blockquote>
<p>Mr. Burchard of Illinois pointed out that the statutes of a State may show no discrimination:<sup>[20]</sup></p>
<blockquote>"If the State Legislature pass a law discriminating against any portion of its citizens, of if it fails to enact provisions equally applicable to every class for the protection of their person and property, it will be admitted that the State does not afford the equal protection. But if the statutes show no discrimination, <span class="star-pagination">*177</span> yet in its judicial tribunals one class is unable to secure that enforcement of their rights and punishment for their infraction which is accorded to another, or if secret combinations of men are allowed by the Executive to band together to deprive one class of citizens of their legal rights without a proper effort to discover, detect, and punish the violations of law and order, the State has not afforded to all its citizens the equal protection of the laws."</blockquote>
<p>Mr. Hoar of Massachusetts stated:<sup>[21]</sup></p>
<blockquote>"Now, it is an effectual denial by a State of the equal protection of the laws when any class of officers charged under the laws with their administration permanently and as a rule refuse to extend that protection. If every sheriff in South Carolina refuses to serve a writ for a colored man and those sheriffs are kept in office year after year by the people of South Carolina, and no verdict against them for their failure of duty can be obtained before a South Carolina jury, the State of South Carolina, through the class of officers who are its representatives to afford the equal protection of the laws to that class of citizens, has denied that protection. If the jurors of South Carolina constantly and as a rule refuse to do justice between man and man where the rights of a particular class of its citizens are concerned, and that State affords by its legislation no remedy, that is as much a denial to that class of citizens of the equal protection of the laws as if the State itself put on its statute-book a statute enacting that no verdict should be rendered in the courts of that State in favor of this class of citizens."</blockquote>
<p><span class="star-pagination">*178</span> Senator Pratt of Indiana spoke of the discrimination against Union sympathizers and Negroes in the actual enforcement of the laws:<sup>[22]</sup></p>
<blockquote>"Plausibly and sophistically it is said the laws of North Carolina do not discriminate against them; that the provisions in favor of rights and liberties are general; that the courts are open to all; that juries, grand and petit, are commanded to hear and redress without distinction as to color, race, or political sentiment.</blockquote>
<blockquote>"But it is a fact, asserted in the report, that of the hundreds of outrages committed upon loyal people through the agency of this Ku Klux organization not one has been punished. This defect in the administration of the laws does not extend to other cases. Vigorously enough are the laws enforced against Union people. They only fail in efficiency when a man of known Union sentiments, white or black, invokes their aid. Then Justice closes the door of her temples."</blockquote>
<p>It was precisely that breadth of the remedy which the opposition emphasized. Mr. Kerr of Indiana referring to the section involved in the present litigation said:</p>
<blockquote>"This section gives to any person who may have been injured in any of his rights, privileges, or immunities of person or property, a civil action for damages against the wrongdoer in the Federal courts. The offenses committed against him may be the common violations of the municipal law of his State. It may give rise to numerous vexations and outrageous prosecutions, inspired by mere mercenary considerations, prosecuted in a spirit of plunder, aided by the crimes of perjury and subornation of perjury, more reckless and dangerous to society than the alleged <span class="star-pagination">*179</span> offenses out of which the cause of action may have arisen. It is a covert attempt to transfer another large portion of jurisdiction from the State tribunals, to which it of right belongs, to those of the United States. It is neither authorized nor expedient, and is not calculated to bring peace, or order, or domestic content and prosperity to the disturbed society of the South. The contrary will certainly be its effect."<sup>[23]</sup></blockquote>
<p>Mr. Voorhees of Indiana, also speaking in opposition, gave it the same construction:<sup>[24]</sup></p>
<blockquote>"And now for a few moments let us inspect the provisions of this bill, inspired as it is by the waning and decaying fortunes of the party in power, and called for, as I have shown, by no public necessity whatever. The first and second sections are designed to transfer all criminal jurisdiction from the courts of the States to the courts of the United States. This is to be done upon the assumption that the courts of the southern States fail and refuse to do their duty in the punishment of offenders against the law."</blockquote>
<p>Senator Thurman of Ohio spoke in the same vein about the section we are now considering:<sup>[25]</sup></p>
<blockquote>"It authorizes any person who is deprived of any right, privilege, or immunity secured to him by the <span class="star-pagination">*180</span> Constitution of the United States, to bring an action against the wrong-doer in the Federal courts, and that without any limit whatsoever as to the amount in controversy. The deprivation may be of the slightest conceivable character, the damages in the estimation of any sensible man may not be five dollars or even five cents; they may be what lawyers call merely nominal damages; and yet by this section jurisdiction of that civil action is given to the Federal courts instead of its being prosecuted as now in the courts of the States."</blockquote>
<p>The debates were long and extensive. It is abundantly clear that one reason the legislation was passed was to afford a federal right in federal courts because, by reason of prejudice, passion, neglect, intolerance or otherwise, state laws might not be enforced and the claims of citizens to the enjoyment of rights, privileges, and immunities guaranteed by the Fourteenth Amendment might be denied by the state agencies.</p>
<p>Much is made of the history of § 2 of the proposed legislation. As introduced § 2 was very broad:</p>
<blockquote>". . . if two or more persons shall, within the limits of any State, band, conspire, or combine together to do any act in violation of the rights, privileges, or immunities of any person, to which he is entitled under the Constitution and laws of the United States, which, committed within a place under the sole and exclusive jurisdiction of the United States, would, under any law of the United States then in force, constitute the crime of either murder, manslaughter, mayhem, robbery, assault and battery, perjury, subornation of perjury, criminal obstruction of legal process or resistance of officers in discharge of official duty, arson, or larceny; and if one or more of the parties to said conspiracy or combination shall do <span class="star-pagination">*181</span> any act to effect the object thereof, all the parties to or engaged in said conspiracy or combination, whether principals or accessories, shall be deemed guilty of a felony . . . ."</blockquote>
<p>It was this provision that raised the greatest storm. It was § 2 that was rewritten so as to be in the main confined to conspiracies to interfere with a federal or state officer in the performance of his duties. <span class="citation no-link">17 Stat. 13</span>. Senator Trumbull said:<sup>[26]</sup></p>
<blockquote>"Those provisions were changed, and as the bill passed the House of Representatives, it was understood by the members of that body to go no further than to protect persons in the rights which were guarantied to them by the Constitution and laws of the United States, and it did not undertake to furnish redress for wrongs done by one person upon another in any of the States of the Union in violation of their laws, unless he also violated some law of the United States, nor to punish one person for an ordinary assault and battery committed on another in a State."</blockquote>
<p>But § 1the section with which we are here concerned was not changed as respects any feature with which we are presently concerned.<sup>[27]</sup> The words "under <span class="star-pagination">*182</span> color of" law were in the legislation from the beginning to the end. The changes hailed by the oppositionindeed the history of the evolution of § 2 much relied upon now are utterly irrelevant to the problem before us, <i>viz.,</i> the meaning of "under color of" law. The vindication of States' rights which was hailed in the amendments to § 2 raises no implication as to the construction to be given to "color of any law" in § 1. The scope of § 1under any constructionis admittedly narrower than was the scope of the original version of § 2. Opponents of the Act, however, did not fail to note that by virtue of § 1 federal courts would sit in judgment on the misdeeds of state officers.<sup>[28]</sup> Proponents of the Act, on the other hand, were aware of the extension of federal power contemplated by every section of the Act. They found justification, however, for this extension in considerations such as those advanced by Mr. Hoar:<sup>[29]</sup></p>
<blockquote>"The question is not whether a majority of the people in a majority of the States are likely to be attached to and able to secure their own liberties. The question is not whether the majority of the people in every State are not likely to desire to secure their own rights. It is, whether a majority of the people in every State are sure to be so attached to the principles of civil freedom and civil justice as to be as much desirous of preserving the liberties of others as their own, as to insure that under no temptation of party spirit, under no political excitement, under <span class="star-pagination">*183</span> no jealousy of race or caste, will the majority either in numbers or strength in any State seek to deprive the remainder of the population of their civil rights."</blockquote>
<p>Although the legislation was enacted because of the conditions that existed in the South at that time, it is cast in general language and is as applicable to Illinois as it is to the States whose names were mentioned over and again in the debates. It is no answer that the State has a law which if enforced would give relief. The federal remedy is supplementary to the state remedy, and the latter need not be first sought and refused before the federal one is invoked. Hence the fact that Illinois by its constitution and laws outlaws unreasonable searches and seizures is no barrier to the present suit in the federal court.</p>
<p>We had before us in <i>United States</i> v. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic, supra</a></span></i><i>,</i> § 20 of the Criminal Code, <span class="citation no-link">18 U. S. C. § 242</span>,<sup>[30]</sup> which provides a criminal punishment for anyone who "under color of any law, statute, ordinance, regulation, or custom" subjects any inhabitant of a State to the deprivation of "any rights, privileges, or immunities secured or protected by the Constitution or laws of the United States." Section 242 first came into the law as § 2 of the Civil Rights Act, Act of April 9, 1866, <span class="citation no-link">14 Stat. 27</span>. After passage of the Fourteenth Amendment, this provision was re-enacted and amended by §§ 17, 18, Act of May 31, 1870, <span class="citation no-link">16 Stat. 140</span>, 144.<sup>[31]</sup> The right involved in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case was the right of voters in a primary to have their votes counted. The laws of Louisiana required the defendants "to count the ballots, to record the result of the count, and <span class="star-pagination">*184</span> to certify the result of the election." <i>United States</i> v. <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#325" aria-description="Citation for case: United States v. Classic"><i>Classic, supra,</i> 325-326</a></span>. But according to the indictment they did not perform their duty. In an opinion written by Mr. Justice (later Chief Justice) Stone, in which Mr. Justice Roberts, Mr. Justice Reed, and MR. JUSTICE FRANKFURTER joined, the Court ruled, "Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken `under color of' state law." <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#326" aria-description="Citation for case: United States v. Classic"><i>Id.,</i> 326</a></span>. There was a dissenting opinion; but the ruling as to the meaning of "under color of" state law was not questioned.</p>
<p>That view of the meaning of the words "under color of" state law, <span class="citation no-link">18 U. S. C. § 242</span>, was reaffirmed in <i>Screws</i> v. <i>United States, supra,</i> 108-113. The acts there complained of were committed by state officers in performance of their duties, <i>viz.,</i> making an arrest effective. It was urged there, as it is here, that "under color of" state law should not be construed to duplicate in federal law what was an offense under state law. <i>Id.</i> (dissenting opinion) 138-149, 157-161. It was said there, as it is here, that the ruling in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case as to the meaning of "under color of" state law was not in focus and was ill-advised. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Id.</a></span></i> (dissenting opinion) 146-147. It was argued there, as it is here, that "under color of" state law included only action taken by officials pursuant to state law. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Id.</a></span></i> (dissenting opinion) 141-146. We rejected that view. <i>Id.,</i> 110-113 (concurring opinion) 114-117. We stated:</p>
<blockquote>"The construction given § 20 [<span class="citation no-link">18 U. S. C. § 242</span>] in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case formulated a rule of law which has become the basis of federal enforcement in this important field. The rule adopted in that case was formulated after mature consideration. It should be good for more than one day only. We do not have here a situation comparable to <i>Mahnich</i> v. <i>Southern S. S. Co.,</i> <span class="citation" data-id="103927"><a href="/opinion/103927/mahnich-v-southern-steamship-co/" aria-description="Citation for case: Mahnich v. Southern Steamship Co.">321 U. S. 96</a></span>, where we <span class="star-pagination">*185</span> overruled a decision demonstrated to be a sport in the law and inconsistent with what preceded and what followed. The <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case was not the product of hasty action or inadvertence. It was not out of line with the cases which preceded. It was designed to fashion the governing rule of law in this important field. We are not dealing with constitutional interpretations which throughout the history of the Court have wisely remained flexible and subject to frequent re-examination. The meaning which the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case gave to the phrase `under color of any law' involved only a construction of the statute. Hence if it states a rule undesirable in its consequences, Congress can change it. We add only to the instability and uncertainty of the law if we revise the meaning of § 20 [<span class="citation no-link">18 U. S. C. § 242</span>] to meet the exigencies of each case coming before us." <span class="citation no-link"><i>Id.,</i> 112-113</span>.</blockquote>
<p>We adhered to that view in <i>Williams</i> v. <i>United States, supra,</i> 99.</p>
<p>Mr. Shellabarger, reporting out the bill which became the Ku Klux Act, said of the provision with which we now deal:</p>
<blockquote>"The model for it will be found in the second section of the act of April 9, 1866, known as the `civil rights act.'. . . This section of this bill, on the same state of facts, not only provides a civil remedy for persons whose former condition may have been that of slaves, but also to all people where, under color of State law, they or any of them may be deprived of rights . . . ."<sup>[32]</sup></blockquote>
<p>Thus, it is beyond doubt that this phrase should be accorded the same construction in both statutesin § 1979 and in <span class="citation no-link">18 U. S. C. § 242</span>.</p>
<p><span class="star-pagination">*186</span> Since the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> and <i>Williams</i> decisions, Congress has had several pieces of civil rights legislation before it. In 1956 one bill reached the floor of the House. This measure had at least one provision in it penalizing actions taken "under color of law or otherwise."<sup>[33]</sup> A vigorous minority report was filed attacking, <i>inter alia,</i> the words "or otherwise."<sup>[34]</sup> But not a word of criticism of the phrase "under color of" state law as previously construed by the Court is to be found in that report.</p>
<p>Section 131 (c) of the Act of September 9, 1957, <span class="citation no-link">71 Stat. 634</span>, 637, amended <span class="citation no-link">42 U. S. C. § 1971</span> by adding a new subsection which provides that no person "whether acting under color of law or otherwise" shall intimidate any other person in voting as he chooses for federal officials. A vigorous minority report was filed<sup>[35]</sup> attacking the wide scope of the new subsection by reason of the words "or otherwise." It was said in that minority report that those words went far beyond what this Court had construed "under color of law" to mean.<sup>[36]</sup> But there was not a word of criticism directed to the prior construction given by this Court to the words "under color of" law.</p>
<p>The Act of May 6, 1960, <span class="citation no-link">74 Stat. 86</span>, uses "under color of" law in two contexts, once when § 306 defines "officer of election" and next when § 601 (a) gives a judicial remedy on behalf of a qualified voter denied the opportunity to register. Once again there was a Committee report containing minority views.<sup>[37]</sup> Once again no one challenged the scope given by our prior decisions to the phrase "under color of" law.</p>
<p><span class="star-pagination">*187</span> If the results of our construction of "under color of" law were as horrendous as now claimed, if they were as disruptive of our federal scheme as now urged, if they were such an unwarranted invasion of States' rights as pretended, surely the voice of the opposition would have been heard in those Committee reports. Their silence and the new uses to which "under color of" law have recently been given reinforce our conclusion that our prior decisions were correct on this matter of construction.</p>
<p>We conclude that the meaning given "under color of" law in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case and in the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> and <i>Williams</i> cases was the correct one; and we adhere to it.</p>
<p>In the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> case we dealt with a statute that imposed criminal penalties for acts "wilfully" done. We construed that word in its setting to mean the doing of an act with "a specific intent to deprive a person of a federal right." <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#103" aria-description="Citation for case: Screws v. United States">325 U. S., at 103</a></span>. We do not think that gloss should be placed on § 1979 which we have here. The word "wilfully" does not appear in § 1979. Moreover, § 1979 provides a civil remedy, while in the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> case we dealt with a criminal law challenged on the ground of vagueness. Section 1979 should be read against the background of tort liability that makes a man responsible for the natural consequences of his actions.</p>
<p>So far, then, the complaint states a cause of action. There remains to consider only a defense peculiar to the City of Chicago.</p>
<p></p>
<h2>III.</h2>
<p>The City of Chicago asserts that it is not liable under § 1979. We do not stop to explore the whole range of questions tendered us on this issue at oral argument and in the briefs. For we are of the opinion that Congress did not undertake to bring municipal corporations within the ambit of § 1979.</p>
<p><span class="star-pagination">*188</span> When the bill that became the Act of April 20, 1871, was being debated in the Senate, Senator Sherman of Ohio proposed an amendment which would have made "the inhabitants of the county, city, or parish" in which certain acts of violence occurred liable "to pay full compensation" to the person damaged or his widow or legal representative.<sup>[38]</sup> The amendment was adopted by the Senate.<sup>[39]</sup> The House, however, rejected it.<sup>[40]</sup> The Conference Committee reported another version.<sup>[41]</sup> The <span class="star-pagination">*189</span> House rejected the Conference report.<sup>[42]</sup> In a second conference the Sherman amendment was dropped and in its place § 6 of the Act of April 20, 1871, was substituted.<sup>[43]</sup><span class="star-pagination">*190</span> This new section, which is now R. S. § 1981, <span class="citation no-link">42 U. S. C. § 1986</span>, dropped out all provision for municipal liability and extended liability in damages to "any person or persons, having knowledge that any" of the specified wrongs are being committed. Mr. Poland, speaking for the House Conferees about the Sherman proposal to make municipalities liable, said:</p>
<blockquote>"We informed the conferees on the part of the Senate that the House had taken a stand on that subject and would not recede from it; that that section imposing liability upon towns and counties must go out or we should fail to agree."<sup>[44]</sup></blockquote>
<p>The objection to the Sherman amendment stated by Mr. Poland was that "the House had solemnly decided that in their judgment Congress had no constitutional power to impose any obligation upon county and town organizations, the mere instrumentality for the administration of state law."<sup>[45]</sup> The question of constitutional power of Congress to impose civil liability on municipalities was vigorously debated with powerful arguments advanced in the affirmative.<sup>[46]</sup></p>
<p>Much reliance is placed on the Act of February 25, 1871, <span class="citation no-link">16 Stat. 431</span>, entitled "An Act prescribing the Form of the enacting and resolving Clauses of Acts and Resolutions of Congress, and Rules for the Construction thereof." Section 2 of this Act provides that "the word `person' may extend and be applied to bodies politic and corporate."<sup>[47]</sup><span class="star-pagination">*191</span> It should be noted, however, that this definition is merely an allowable, not a mandatory, one. It is said that doubts should be resolved in favor of municipal liability because private remedies against officers for illegal searches and seizures are conspicuously ineffective,<sup>[48]</sup> and because municipal liability will not only afford plaintiffs responsible defendants but cause those defendants to eradicate abuses that exist at the police level.<sup>[49]</sup> We do not reach those policy considerations. Nor do we reach the constitutional question whether Congress has the power to make municipalities liable for acts of its officers that violate the civil rights of individuals.</p>
<p>The response of the Congress to the proposal to make municipalities liable for certain actions being brought within federal purview by the Act of April 20, 1871, was so antagonistic that we cannot believe that the word "person" was used in this particular Act to include them.<sup>[50]</sup><span class="star-pagination">*192</span> Accordingly we hold that the motion to dismiss the complaint against the City of Chicago was properly granted. But since the complaint should not have been dismissed against the officials the judgment must be and is</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE STEWART joins, concurring.</p>
<p>Were this case here as one of first impression, I would find the "under color of any statute" issue very close indeed. However, in <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i><sup>[1]</sup> and <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i><sup>[2]</sup> this Court considered a substantially identical statutory phrase to have a meaning which, unless we now retreat from it, requires that issue to go for the petitioners here.</p>
<p>From my point of view, the policy of <i>stare decisis,</i> as it should be applied in matters of statutory construction, and, to a lesser extent, the indications of congressional acceptance of this Court's earlier interpretation, require that it appear beyond doubt from the legislative history of the 1871 statute that <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> misapprehended the meaning of the controlling provision,<sup>[3]</sup> before a departure from what was decided in those cases would be justified. Since I can find no such justifying indication in that legislative history, I join the opinion of the Court. However, what has been written on both sides of the matter makes some additional observations appropriate.</p>
<p><span class="star-pagination">*193</span> Those aspects of Congress' purpose which are quite clear in the earlier congressional debates, as quoted by my Brothers DOUGLAS and FRANKFURTER in turn, seem to me to be inherently ambiguous when applied to the case of an isolated abuse of state authority by an official. One can agree with the Court's opinion that:</p>
<blockquote>"It is abundantly clear that one reason the legislation was passed was to afford a federal right in federal courts because, by reason of prejudice, passion, neglect, intolerance or otherwise, state laws might not be enforced and the claims of citizens to the enjoyment of rights, privileges, and immunities guaranteed by the Fourteenth Amendment might be denied by the state agencies. . . ."</blockquote>
<p>without being certain that Congress meant to deal with anything other than abuses so recurrent as to amount to "custom, or usage." One can agree with my Brother FRANKFURTER, in dissent, that Congress had no intention of taking over the whole field of ordinary state torts and crimes, without being certain that the enacting Congress would not have regarded actions by an official, made possible by his position, as far more serious than an ordinary state tort, and therefore as a matter of federal concern. If attention is directed at the rare specific references to isolated abuses of state authority, one finds them neither so clear nor so disproportionately divided between favoring the positions of the majority or the dissent as to make either position seem plainly correct.<sup>[4]</sup></p>
<p>Besides the inconclusiveness I find in the legislative history, it seems to me by no means evident that a position <span class="star-pagination">*194</span> favoring departure from <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> fits better that with which the enacting Congress was concerned than does the position the Court adopted 20 years ago. There are apparent incongruities in the view of the dissent which may be more easily reconciled in terms of the earlier holding in <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span>.</i></p>
<p>The dissent considers that the "under color of" provision of § 1983 distinguishes between unconstitutional actions taken without state authority, which only the State should remedy, and unconstitutional actions authorized by the State, which the Federal Act was to reach. If so, then the controlling difference for the enacting legislature must have been either that the state remedy was more adequate for unauthorized actions than for authorized ones or that there was, in some sense, greater harm from unconstitutional actions authorized by the full panoply of state power and approval than from unconstitutional actions not so authorized or acquiesced in by the State. I find less than compelling the evidence that either distinction was important to that Congress.</p>
<p></p>
<h2>I.</h2>
<p>If the state remedy was considered adequate when the official's unconstitutional act was unauthorized, why should it not be thought equally adequate when the unconstitutional act was authorized? For if one thing is very clear in the legislative history, it is that the Congress of 1871 was well aware that no action requiring state judicial enforcement could be taken in violation of the Fourteenth Amendment without that enforcement being declared void by this Court on direct review from the state courts. And presumably it must also have been understood that there would be Supreme Court review of the denial of a state damage remedy against an official on grounds of state authorization of the unconstitutional <span class="star-pagination">*195</span> action. It therefore seems to me that the same state remedies would, with ultimate aid of Supreme Court review, furnish identical relief in the two situations. This is the point Senator Blair made when, having stated that the object of the Fourteenth Amendment was to prevent any discrimination by the law of any State, he argued that:</p>
<blockquote>"This being forbidden by the Constitution of the United States, and all the judges, State and national, being sworn to support the Constitution of the United States, and the Supreme Court of the United States having power to supervise and correct the action of the State courts when they violated the Constitution of the United States, there could be no danger of the violation of the right of citizens under color of the <i>laws</i> of the States." Cong. Globe, 42d Cong., 1st Sess., at App. 231.</blockquote>
<p>Since the suggested narrow construction of § 1983 presupposes that state measures were adequate to remedy unauthorized deprivations of constitutional rights and since the identical state relief could be obtained for state-authorized acts with the aid of Supreme Court review, this narrow construction would reduce the statute to having merely a jurisdictional function, shifting the load of federal supervision from the Supreme Court to the lower courts and providing a federal tribunal for fact findings in cases involving authorized action. Such a function could be justified on various grounds. It could, for example, be argued that the state courts would be less willing to find a constitutional violation in cases involving "authorized action" and that therefore the victim of such action would bear a greater burden in that he would more likely have to carry his case to this Court, and once here, might be bound by unfavorable state court findings. But the legislative debates do not disclose congressional <span class="star-pagination">*196</span> concern about the burdens of litigation placed upon the victims of "authorized" constitutional violations contrasted to the victims of unauthorized violations. Neither did Congress indicate an interest in relieving the burden placed on this Court in reviewing such cases.</p>
<p>The statute becomes more than a jurisdictional provision only if one attributes to the enacting legislature the view that a deprivation of a constitutional right is significantly different from and more serious than a violation of a state right and therefore deserves a different remedy even though the same act may constitute both a state tort and the deprivation of a constitutional right. This view, by no means unrealistic as a common-sense matter,<sup>[5]</sup> is, I believe, more consistent with the flavor of the legislative history than is a view that the primary purpose of the statute was to grant a lower court forum for fact findings. For example, the tone is surely one of overflowing protection of constitutional rights, and there is not a hint of concern about the administrative burden on the Supreme Court, when Senator Frelinghuysen says:</p>
<blockquote>"As to the civil remedies, for a violation of these privileges, we know that when the courts of a State <span class="star-pagination">*197</span> violate the provisions of the Constitution or the law of the United States there is now relief afforded by a review in the Federal courts. And since the 14th Amendment forbids any State from making or enforcing any law abridging these privileges and immunities, as you cannot reach the Legislatures, the injured party should have an original action in our Federal courts, so that by injunction or by the recovery of damages he could have relief against the party who under color of such law is guilty of infringing his rights. As to the civil remedy no one, I think, can object." <i>Id.,</i> at 501.</blockquote>
<p>And Senator Carpenter reflected a similar belief that the protection granted by the statute was to be very different from the relief available on review of state proceedings:</p>
<blockquote>"The prohibition in the old Constitution that no State should pass a law impairing the obligation of contracts was a negative prohibition laid upon the State. Congress was not authorized to interfere in case the State violated that provision. It is true that when private rights were affected by such a State law, and that was brought before the judiciary, either of the State or nation, it was the duty of the court to pronounce the act void; but there the matter ended. Under the present Constitution, however, in regard to those rights which are secured by the fourteenth amendment, they are not left as the right of the citizen in regard to laws impairing the obligation of contracts was left, to be disposed of by the courts as the cases should arise between man and man, but Congress is clothed with the affirmative power and jurisdiction to correct the evil.</blockquote>
<blockquote>"I think there is one of the fundamental, one of the great, the tremendous revolutions effected in our Government by that article of the Constitution. It <span class="star-pagination">*198</span> gives Congress affirmative power to protect the rights of the citizen, whereas before no such right was given to save the citizen from the violation of any of his rights by State Legislatures, and the only remedy was a judicial one when the case arose." <i>Id.,</i> at 577.</blockquote>
<p>In my view, these considerations put in serious doubt the conclusion that § 1983 was limited to state-authorized unconstitutional acts, on the premise that state remedies respecting them were considered less adequate than those available for unauthorized acts.</p>
<p></p>
<h2>II.</h2>
<p>I think this limited interpretation of § 1983 fares no better when viewed from the other possible premise for it, namely that state-approved constitutional deprivations were considered more offensive than those not so approved. For one thing, the enacting Congress was not unaware of the fact that there was a substantial overlap between the protections granted by state constitutional provisions and those granted by the Fourteenth Amendment. Indeed one opponent of the bill, Senator Trumbull, went so far as to state in a debate with Senators Carpenter and Edmunds that his research indicated a complete overlap in every State, at least as to the protections of the Due Process Clause.<sup>[6]</sup> Thus, in one very significant sense, there was no ultimate state approval of a large portion of otherwise authorized actions depriving a person of due-process rights. I hesitate to assume that the proponents of the present statute, who regarded it as necessary even though they knew that the provisions of the Fourteenth Amendment were self-executing, would have thought the remedies unnecessary whenever there were self-executing provisions of state constitutions also forbidding what the Fourteenth Amendment forbids. The only alternative is <span class="star-pagination">*199</span> to disregard the possibility that a state court would find the action unauthorized on grounds of the state constitution. But if the defendant official is denied the right to defend in the federal court upon the ground that a state court would find his action unauthorized in the light of the state constitution, it is difficult to contend that it is the added harmfulness of state approval that justifies a different remedy for authorized than for unauthorized actions of state officers. Moreover, if indeed the legislature meant to distinguish between authorized and unauthorized acts and yet did not mean the statute to be inapplicable whenever there was a state constitutional provision which, reasonably interpreted, gave protection similar to that of a provision of the Fourteenth Amendment, would there not have been some explanation of this exception to the general rule? The fact that there is none in the legislative history at least makes more difficult a contention that these legislators were in fact making a distinction between use and misuse of state power.</p>
<p>There is a further basis for doubt that it was the additional force of state approval which justified a distinction between authorized and unauthorized actions. No one suggests that there is a difference in the showing the plaintiff must make to assert a claim under § 1983 depending upon whether he is asserting a denial of rights secured by the Equal Protection Clause or a denial of rights secured by the Due Process Clause of the Fourteenth Amendment. If the same Congress which passed what is now § 1983 also provided remedies against two or more nonofficials who conspire to prevent an official from granting equal protection of the laws, see <span class="citation no-link">42 U. S. C. § 1985</span>, then it would seem almost untenable to insist that this Congress would have hesitated, on the grounds of lack of full state approval of the official's act, to provide similar remedies against an official who, unauthorized, denied that equal protection of the laws on his own initiative. For <span class="star-pagination">*200</span> there would be no likely state approval of or even acquiescence in a conspiracy to coerce a state official to deny equal protection. Indeed it is difficult to attribute to a Congress which forbade two private citizens from hindering an official's giving of equal protection an intent to leave that official free to deny equal protection of his own accord.<sup>[7]</sup></p>
<p>We have not passed upon the question whether <span class="citation no-link">42 U. S. C. § 1985</span>,<sup>[8]</sup> which was passed as the second section of the Act that included § 1983, was intended to reach only the Ku Klux Klan or other substantially organized group activity, as distinguished from what its words seem to include, any conspiracy of two persons with "the purpose of preventing or hindering the constituted authorities of any State . . . from giving or securing to all persons within such State . . . the equal protection of the laws . . . ."<sup>[9]</sup> Without now deciding the question, I think <span class="star-pagination">*201</span> it is sufficient to note that the legislative history is not without indications that what the words of the statute seem to state was in fact the meaning assumed by Congress.<sup>[10]</sup></p>
<p><span class="star-pagination">*202</span> These difficulties in explaining the basis of a distinction between authorized and unauthorized deprivations of constitutional rights fortify my view that the legislative history does not bear the burden which <i>stare decisis</i> casts upon it. For this reason and for those stated in the opinion of the Court, I agree that we should not now depart from the holdings of the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> cases.</p>
<p>MR. JUSTICE FRANKFURTER, dissenting except insofar as the Court holds that this action cannot be maintained against the City of Chicago.</p>
<p>Abstractly stated, this case concerns a matter of statutory construction. So stated, the problem before the Court is denuded of illuminating concreteness and thereby of its far-reaching significance for our federal system. Again abstractly stated, this matter of statutory construction is one upon which the Court has already passed. But it has done so under circumstances and in settings that negative those considerations of social policy upon which the doctrine of <i>stare decisions,</i> calling for the controlling application of prior statutory construction, rests.</p>
<p>This case presents the question of the sufficiency of petitioners' complaint in a civil action for damages brought under the Civil Rights Act, R. S. § 1979, <span class="star-pagination">*203</span> <span class="citation no-link">42 U. S. C. § 1983</span>.<sup>[1]</sup> The complaint alleges that on October 29, 1958, at 5:45 a.m., thirteen Chicago police officers, led by Deputy Chief of Detectives Pape, broke through two doors of the Monroe apartment, woke the Monroe couple with flashlights, and forced them at gunpoint to leave their bed and stand naked in the center of the living room; that the officers roused the six Monroe children and herded them into the living room; that Detective Pape struck Mr. Monroe several times with his flashlight, calling him "nigger" and "black boy"; that another officer pushed Mrs. Monroe; that other officers hit and kicked several of the children and pushed them to the floor; that the police ransacked every room, throwing clothing from closets to the floor, dumping drawers, ripping mattress covers; that Mr. Monroe was then taken to the police station and detained on "open" charges for ten hours, during which time he was interrogated about a murder<sup>[2]</sup> and exhibited in lineups; that he was not brought before a magistrate, although numerous magistrate's courts were accessible; that he was not advised of his procedural rights; that he was not permitted to call his family or an attorney; that he was subsequently released without criminal charges having been filed against him. It is also alleged that the actions of the officers throughout were without authority of a search warrant or an arrest warrant; that those actions constituted arbitrary and unreasonable conduct; that the <span class="star-pagination">*204</span> officers were employees of the City of Chicago, which furnished each of them with a badge and an identification card designating him as a member of the Police Department; that the officers were agents of the city, acting in the course of their employment and engaged in the performance of their duties; and that it is the custom of the Department to arrest and confine individuals for prolonged periods on "open" charges for interrogation, with the purpose of inducing incriminating statements, exhibiting its prisoners for identification, holding them <i>incommunicado</i> while police officers investigate their activities, and punishing them by imprisonment without judicial trial. On the basis of these allegations various members of the Monroe family seek damages against the individual police officers and against the City of Chicago. The District Court dismissed the complaint for failure to state a claim and the Court of Appeals for the Seventh Circuit affirmed. <span class="citation" data-id="249412"><a href="/opinion/249412/james-monroe-v-frank-pape/" aria-description="Citation for case: James Monroe v. Frank Pape">272 F. 2d 365</a></span>.</p>
<p>Petitioners base their claim to relief in the federal courts on what was enacted as § 1 of the "Ku Klux Act" of April 20, 1871, "An Act to enforce the Provisions of the Fourteenth Amendment to the Constitution of the United States, and for other Purposes." <span class="citation no-link">17 Stat. 13</span>. It became, with insignificant rephrasing, § 1979 of the Revised Statutes. As now set forth in <span class="citation no-link">42 U. S. C. § 1983</span>, it is, in relevant part, as follows:</p>
<blockquote>"Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State . . . subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress."</blockquote>
<p></p>
<h2>
<span class="star-pagination">*205</span> I.</h2>
<p>In invoking § 1979 (the old designation will be used hereafter), petitioners contend that its protection of "rights, privileges, or immunities secured by the Constitution" encompasses what "due process of law" and "the equal protection of the laws" of the Fourteenth Amendment guarantee against action by the States. In this contention they are supported both by the title of the Act of 1871 and by its legislative history. See the authoritative statement of Mr. Edmunds, reporting the bill from the Senate Committee on the Judiciary, Cong. Globe, 42d Cong., 1st Sess. 568. See also <i>id.,</i> at 332-334, App. 83-85, 310. It is true that a related phrase, "any right or privilege secured . . . by the Constitution or laws," in § 241 of Title 18, U. S. C., was said by a plurality of the Court in <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="9420563"><a href="/opinion/104889/united-states-v-williams/" aria-description="Citation for case: United States v. Williams">341 U. S. 70</a></span>, to comprehend only the rights arising immediately from the relationship of the individual to the central government. And see <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542</a></span>.<sup>[3]</sup> But this construction was demanded by § 241, which penalizes conspiracies of private individuals acting as such, while § 1979 applies only to action taken "under color of any statute," etc. Different problems of statutory meaning are presented by two enactments deriving from different <span class="star-pagination">*206</span> constitutional sources. See the <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/" aria-description="Citation for case: Civil Rights Cases">109 U. S. 3</a></span>. Compare <i>United States</i> v. <i>Williams, supra</i><i>,</i> with <i>Screws</i> v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span>. If petitioners have alleged facts constituting a deprivation under color of state authority of a right assured them by the Fourteenth Amendment, they have brought themselves within § 1979. <i>Douglas</i> v. <i>Jeannette,</i> <span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157</a></span>; <i>Hague</i> v. <i>C. I. O.,</i> <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#525" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U. S. 496, 525-526</a></span> (opinion of Stone, J.).<sup>[4]</sup></p>
<p>To be sure, <i>Screws</i> v. <i>United States, supra</i><i>,</i> requires a finding of specific intent in order to sustain a conviction under the cognate penal provisions of <span class="citation no-link">18 U. S. C. § 242</span><sup>[5]</sup> "an intent to deprive a person of a right which has been made specific either by the express terms of the Constitution or laws of the United States or by decisions interpreting them." <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#104" aria-description="Citation for case: Screws v. United States">325 U. S., at 104</a></span>. Petitioners' complaint here alleges no such specific intent. But, for a number of reasons, this requirement of <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> should not be carried over and applied to civil actions under § 1979. First, the word "willfully" in <span class="citation no-link">18 U. S. C. § 242</span> from which the requirement of intent was derived in <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> does not appear in § 1979. Second, § 1979, by the very fact that it is a civil provision, invites treatment different from that to be given its criminal analogue. The constitutional scruples concerning vagueness which were deemed to compel the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> construction have less force in the context of a civil proceeding,<sup>[6]</sup><span class="star-pagination">*207</span> and § 1979, insofar as it creates an action for damages, must be read in light of the familiar basis of tort liability that a man is responsible for the natural consequences of his acts. Third, even in the criminal area, the specific intent demanded by <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> has proved to be an abstraction serving the purposes of a constitutional need without impressing any actual restrictions upon the nature of the crime which the jury tries. The <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> opinion itself said that "The fact that the defendants may not have been thinking in constitutional terms is not material where their aim was not to enforce local law but to deprive a citizen of a right and that right was protected by the Constitution." <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#106" aria-description="Citation for case: Screws v. United States">325 U. S., at 106</a></span>. And lower courts in applying the statute have allowed inference of the requisite specific intent from evidence, it would appear, of malevolence alone.<sup>[7]</sup> But if intent to infringe "specific" constitutional rights comes in practice to mean no more than intent without justification to bring about the circumstances which infringe those rights, then the consequences of introducing the specific intent issue into a litigation is, in effect, to require fictional pleading, needlessly burden jurors with abstruse instructions, and lessen the degree of control which federal courts have over jury vagaries.</p>
<p>If the courts are to enforce § 1979, it is an unhappy form of judicial disapproval to surround it with doctrines which partially and unequally obstruct its operation. Specific intent in the context of the section would cause <span class="star-pagination">*208</span> such embarrassment without countervailing justification. Petitioners' allegations that respondents in fact did the acts which constituted violations of constitutional rights are sufficient.</p>
<p></p>
<h2>II.</h2>
<p>To show such violations, petitioners invoke primarily the Amendment's Due Process Clause.<sup>[8]</sup> The essence of their claim is that the police conduct here alleged offends those requirements of decency and fairness which, because they are "implicit in the concept of ordered liberty," are imposed by the Due Process Clause upon the States. <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325</a></span>. When we apply to their complaint that standard of a "principle of justice so rooted in the traditions and conscience of our people as to be ranked as fundamental,"<sup>[9]</sup> which has been the touchstone for this Court's enforcement of due process,<sup>[10]</sup> the merit of this constitutional claim is evident. The conception expressed in <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>, that "The security of one's privacy against arbitrary intrusion by the police. . . is basic to a free society," was not an innovation of <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i> The tenet that there exists a realm of sanctuary surrounding every individual and in frangible, save in a very limited class of circumstances, by the agents of government, had informed the decision of the King's Bench two centuries earlier in <i>Entick</i> v. <i>Carrington,</i> 2 Wils. 275, had been the basis of Otis' contemporary speech against the Writ of <span class="star-pagination">*209</span> Assistance, see Gray's notes in Quincy's Massachusetts Reports, App. I, at 471; Tudor, Life of James Otis (1823) 63, and has in the intervening years found expression not only in the Fourth Amendment to the Constitution of the United States, but also in the fundamental law of every State.<sup>[11]</sup> Modern totalitarianisms have been a stark reminder, but did not newly teach, that the kicked-in door is the symbol of a rule of fear and violence fatal to institutions founded on respect for the integrity of man.</p>
<p>The essence of the liberty protected by the common law and by the American constitutions was "the right to shut the door on officials of the state unless their entry is under proper authority of law"; particularly, "the right to resist unauthorized entry which has as its design the securing of information to fortify the coercive power of the state against the individual." <i>Frank</i> v. <i>Maryland,</i> 359 U. S. <span class="star-pagination">*210</span> 360, 365.<sup>[12]</sup> Searches of the dwelling house were the special object of this universal condemnation of official intrusion.<sup>[13]</sup> Night-time search was the evil in its most obnoxious form.<sup>[14]</sup> Few reported cases have presented all of the manifold aggravating circumstances which petitioners here allegeintrusion <i>en masse,</i> by dark, by force, unauthorized by warrant, into an occupied private home, without even the asserted justification of belief by the intruders that the inhabitants were presently committing some criminal act within; physical abuse and the calculated degradation of insult and forced nakedness; sacking and disordering of personal effects throughout the home; arrest and detention against the background terror of threatened criminal proceedings. Wherever similar conduct has appeared, the courts have unanimously condemned police entries as lawless.<sup>[15]</sup></p>
<p><span class="star-pagination">*211</span> If the question whether due process forbids this kind of police invasion were before us in isolation, the answer would be quick. If, for example, petitioners had sought damages in the state courts of Illinois and if those courts had refused redress on the ground that the official character of the respondents clothed them with civil immunity, we would be faced with the sort of situation to which the language in the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> opinion was addressed: "we have no hesitation in saying that were a State affirmatively to sanction such police incursion into privacy it would run counter to the guaranty of the Fourteenth Amendment." <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#28" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 28</a></span>. If that issue is not reached in this case it is not because the conduct which the record here presents can be condoned. But by bringing their action in a Federal District Court petitioners cannot rest on the Fourteenth Amendment <i>simpliciter.</i> They invoke the protection of a specific statute by which Congress restricted federal judicial enforcement of its guarantees to particular enumerated circumstances. They must show not only that their constitutional rights have been infringed, but that they have been infringed "under color of [state] statute, ordinance, regulation, custom, or usage," as that phrase is used in the relevant congressional enactment.</p>
<p></p>
<h2>III.</h2>
<p>Of course, if Congress by appropriate statutory language attempted to reach every act which could be attributed to the States under the Fourteenth Amendment's prohibition: "No State shall . . . ," the reach of the statute would be the reach of the Amendment itself. Relevant to the enforcement of such a statute would be not only the concept of state action as this Court has developed it, see <i>Nixon</i> v. <i>Condon,</i> <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/#89" aria-description="Citation for case: Nixon v. Condon">286 U. S. 73, 89</a></span>, but also considerations of the power of Congress, under the Amendment's Enforcement Clause, to determine what <span class="star-pagination">*212</span> is "appropriate legislation" to protect the rights which the Fourteenth Amendment secures. Cf. <i>United States</i> v. <i>Raines,</i> <span class="citation" data-id="8937760"><a href="/opinion/8947114/united-states-v-raines/" aria-description="Citation for case: United States v. Raines">362 U. S. 17</a></span>. Still, in this supposed case we would arrive at the question of what Congress could do only after we had determined what it was that Congress had done. So, in the case before us now, we must ask what Congress did in 1871. We must determine what Congress meant by "under color" of enumerated state authority.<sup>[16]</sup></p>
<p>Congress used that phrase not only in R. S. § 1979, but also in the criminal provisions of § 2 of the First Civil Rights Act of April 9, 1866, <span class="citation no-link">14 Stat. 27</span>, from which is derived the present <span class="citation no-link">18 U. S. C. § 242</span>,<sup>[17]</sup> and in both cases used it with the same purpose.<sup>[18]</sup> During the seventy years <span class="star-pagination">*213</span> which followed these enactments, cases in this Court in which the "under color" provisions were invoked uniformly involved action taken either in strict pursuance of some specific command of state law<sup>[19]</sup> or within the scope of executive discretion in the administration of state laws.<sup>[20]</sup><span class="star-pagination">*214</span> The same is true, with two exceptions, in the lower federal courts.<sup>[21]</sup> In the first of these two cases it was held that § 1979 was not directed to instances of lawless police brutality, although the ruling was not put on "under color" <span class="star-pagination">*215</span> grounds.<sup>[22]</sup> In the second, an indictment charging a county tax collector with depriving one Ah Koo of a federally secured right under color of a designated California law, set forth in the indictment, was held insufficient against a demurrer. <i>United States</i> v. <i>Jackson,</i> <span class="citation" data-id="9300552"><a href="/opinion/9305449/united-states-v-jackson/" aria-description="Citation for case: United States v. Jackson">26 Fed. Cas. 563</a></span>, No. 15,459 (C. C. D. Cal. 1874). The court wrote:</p>
<blockquote>"The indictment contains no averment that Ah Koo was a foreign miner, and within the provisions of the state law. If this averment be unnecessary . . . the act of congress would then be held to apply to a case of illegal extortion by a tax collector from any person, <span class="star-pagination">*216</span> though such exaction might be wholly unauthorized by the law under which the officer pretended to act.</blockquote>
<blockquote>"We are satisfied that it was not the design of congress to prevent or to punish such abuse of authority by state officers. The object of the act was, not to prevent illegal exactions, but to forbid the execution of state laws, which, by the act itself, are made void. . . .</blockquote>
<blockquote>"It would seem, necessarily, to follow, that the person from whom the tax was exacted must have been a person from whom, under the provisions of the state law, the officer was authorized to exact it. The statute requires that a party shall be subjected to a deprivation of right secured by the statute under color of some law, statute, order or custom; but if this exaction, although made by a tax collector, has been levied upon a person not within the provisions of the state law, the exaction cannot be said to have been made `under color of law,' any more than a similar exaction from a Chinese miner, made by a person wholly unauthorized, and under the pretense of being a tax collector." <span class="citation" data-id="9300552"><a href="/opinion/9305449/united-states-v-jackson/#563" aria-description="Citation for case: United States v. Jackson"><i>Id.,</i> at 563-564</a></span>.</blockquote>
<p>Throughout this period, the only indication of this Court's views on the proper interpretation of the "under color" language is a dictum in the <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/" aria-description="Citation for case: Civil Rights Cases">109 U. S. 3</a></span>. There, in striking down other Civil Rights Act provisions which, as the Court regarded them, attempted to reach private conduct not attributable to state authority, Mr. Justice Bradley contrasted those provisions with § 2 of the Act of 1866: "This [latter] law is clearly corrective in its character, intended to counteract and furnish redress against State laws and proceedings, and customs having the force of law, which sanction the wrongful acts specified." <i>Id.,</i> at 16.</p>
<p>A sharp change from this uniform application of seventy years was made in 1941, but without acknowledgment or <span class="star-pagination">*217</span> indication of awareness of the revolutionary turnabout from what had been established practice. The opinion in <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U. S. 299</a></span>, accomplished this. The case presented an indictment under § 242 charging certain local Commissioners of Elections with altering ballots cast in a primary held to nominate candidates for Congress. Sustaining the sufficiency of the indictment in an extensive opinion concerned principally with the question whether the right to vote in such a primary was a right secured by the Constitution,<sup>[23]</sup> Mr. Justice Stone wrote that the alteration of the ballots was "under color" of state law. This holding was summarily announced without exposition; it had been only passingly argued.<sup>[24]</sup> Of the three authorities cited to support it, two did not involve the "under color" statutes,<sup>[25]</sup> and the third, <i>Hague</i> v. <i>C. I. O.,</i> <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U. S. 496</a></span>, was a case in which highranking municipal officials claimed authorization for their actions under municipal ordinances (here held unconstitutional) <span class="star-pagination">*218</span> and under the general police powers of the State.<sup>[26]</sup> All three of these cases had dealt with "State action" problems, and it is "State action," not the very different question of the "under color" clause, that Mr. Justice Stone appears to have considered.<sup>[27]</sup> (I joined in this opinion without having made an independent examination of the legislative history of the relevant legislation or of the authorities drawn upon for the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> construction. Acquiescence so founded does not preclude the responsible recognition of error disclosed by subsequent study.) When, however, four years later the Court was called on to review the conviction under § 242 of a Georgia County Sheriff who had beaten a Negro prisoner to death, the opinion of four of the six Justices who believed that the statute applied merely invoked <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and <i>stare decisions</i> and did not reconsider the meaning which that case had uncritically assumed was to be attached to the language, "under color" of state authority. <i>Screws</i> v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span>. The briefs in the <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> case did <span class="star-pagination">*219</span> not examine critically the legislative history of the Civil Rights Acts.<sup>[28]</sup> The only reference to this history in the plurality opinion, insofar as it bears on the interpretation of the clause "under color of . . . law," is contained in a pair of sentences discounting two statements by Senators Trumbull and Sherman regarding the Civil Rights Acts of 1866 and 1870, cited by the minority.<sup>[29]</sup> The bulk of the plurality opinion's treatment of the issue consists of the argument that "under color" had been construed in <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> and that the construction there put on the words should not be abandoned or revised. <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#109" aria-description="Citation for case: Screws v. United States">325 U. S., at 109-113</a></span>. The case of <i>Williams</i> v. <i>United States,</i> <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">341 U. S. 97</a></span>, reaffirmed <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> and applied it to circumstances of third-degree brutality practiced by a private detective who held a special police officer's card and was accompanied by a regular policeman.<sup>[30]</sup></p>
<p><span class="star-pagination">*220</span> Thus, although this Court has three times found that conduct of state officials which is forbidden by state law may be "under color" of state law for purposes of the Civil Rights Acts, it is accurate to say that that question has never received here the consideration which its importance merits. That regard for controlling legislative history which is conventionally observed by this Court in determining the true meaning of important legislation that does not construe itself<sup>[31]</sup> has never been applied to the "under color" provisions; particularly, there has never been canvassed the full record of the debates preceding passage of the 1871 Act with which we are concerned in this case. Neither <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> nor <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> nor <i>Williams</i> warrants refusal now to take account of those debates and the illumination they afford. While we may well decline to re-examine recent cases which derive from the judicial process exercised under its adequate safeguards documenting briefs and adequate arguments on both sides as foundation for due deliberationthe relevant demands of <i>stare decisions</i> do not preclude considering, for the first time thoroughly and in the light of the best available evidence of congressional purpose, a statutory <span class="star-pagination">*221</span> interpretation which started as an unexamined assumption on the basis of inapplicable citations and has the claim of a dogma solely through reiteration. Particularly is this so when that interpretation, only recently made, was at its inception a silent reversal of the judicial history of the Civil Rights Acts for three quarters of a century.</p>
<p>"The rule of <i>stare decisions,</i> though one tending to consistency and uniformity of decision, is not inflexible." <i>Hertz</i> v. <i>Woodman,</i> <span class="citation" data-id="9418187"><a href="/opinion/97288/hertz-v-woodman/#212" aria-description="Citation for case: Hertz v. Woodman">218 U. S. 205, 212</a></span>. It is true, of course, that the reason for the rule is more compelling in cases involving inferior law, law capable of change by Congress, than in constitutional cases, where this Court although even in such cases a wise consciousness of the limitations of individual vision has impelled it always to give great weight to prior decisionsnevertheless bears the ultimate obligation for the development of the law as institutions develop. See, <i>e. g., </i><i>Smith</i> v. <i>Allwright,</i> <span class="citation" data-id="103962"><a href="/opinion/103962/smith-v-allwright/" aria-description="Citation for case: Smith v. Allwright">321 U. S. 649</a></span>. But the Court has not always declined to re-examine cases whose outcome Congress might have changed. See Mr. Justice Brandeis, dissenting, in <i>Burnet</i> v. <i>Coronado Oil &amp; Gas Co.,</i> <span class="citation" data-id="8148759"><a href="/opinion/8186832/burnet-v-coronado-oil-gas-co/#406" aria-description="Citation for case: Burnet v. Coronado Oil &amp; Gas Co.">285 U. S. 393, 406-407, n. 1</a></span>. Decisions involving statutory construction, even decisions which Congress has persuasively declined to overrule, have been overruled here. See <i>Girouard</i> v. <i>United States,</i> <span class="citation" data-id="9419823"><a href="/opinion/104285/girouard-v-united-states/" aria-description="Citation for case: Girouard v. United States">328 U. S. 61</a></span>, overruling <i>United States</i> v. <i>Schwimmer,</i> <span class="citation" data-id="9418678"><a href="/opinion/101446/united-states-v-schwimmer/" aria-description="Citation for case: United States v. Schwimmer">279 U. S. 644</a></span>, <i>United States</i> v. <i>Macintosh,</i> <span class="citation" data-id="9418720"><a href="/opinion/101765/united-states-v-macintosh/" aria-description="Citation for case: United States v. MacIntosh">283 U. S. 605</a></span>, and <i>United States</i> v. <i>Bland,</i> <span class="citation" data-id="9418722"><a href="/opinion/101766/united-states-v-bland/" aria-description="Citation for case: United States v. Bland">283 U. S. 636</a></span>; see also <i>Commissioner</i> v. <i>Estate of Church,</i> <span class="citation" data-id="9420263"><a href="/opinion/104616/commissioner-v-estate-of-church/" aria-description="Citation for case: Commissioner v. Estate of Church">335 U. S. 632</a></span>, overruling <i>May</i> v. <i>Heiner,</i> <span class="citation" data-id="101552"><a href="/opinion/101552/may-v-heiner/" aria-description="Citation for case: May v. Heiner">281 U. S. 238</a></span>.</p>
<p>And with regard to the Civil Rights Acts there are reasons of particular urgency which authorize the Court indeed, which make it the Court's responsibilityto reappraise in the hitherto skimpily considered context of R. S. § 1979 what was decided in <i>Classic, Screws</i> and <i>Williams.</i> This is not an area of commercial law in which, presumably, individuals may have arranged their affairs in <span class="star-pagination">*222</span> reliance on the expected stability of decision. Compare <i>National Bank</i> v. <i>Whitney,</i> <span class="citation" data-id="9417263"><a href="/opinion/90305/national-bank-v-whitney/" aria-description="Citation for case: National Bank v. Whitney">103 U. S. 99</a></span>; <i>Vail</i> v. <i>Arizona,</i> <span class="citation" data-id="96723"><a href="/opinion/96723/vail-v-arizona/" aria-description="Citation for case: Vail v. Arizona">207 U. S. 201</a></span>; <i>Walling</i> v. <i>Halliburton Oil Well Cementing Co.,</i> <span class="citation" data-id="9419984"><a href="/opinion/104413/walling-v-halliburton-oil-well-cementing-co/" aria-description="Citation for case: Walling v. Halliburton Oil Well Cementing Co.">331 U. S. 17</a></span>; <i>United States</i> v. <i>South Buffalo R. Co.,</i> <span class="citation" data-id="9420149"><a href="/opinion/104542/united-states-v-south-buffalo-railway-co/" aria-description="Citation for case: United States v. South Buffalo Railway Co.">333 U. S. 771</a></span>. Nor is it merely a mine-run statutory question involving a narrow compass of individual rights and duties. The issue in the present case concerns directly a basic problem of American federalism: the relation of the Nation to the States in the critically important sphere of municipal law administration. In this aspect, it has significance approximating constitutional dimension. Necessarily, the construction of the Civil Rights Acts raises issues fundamental to our institutions. This imposes on this Court a corresponding obligation to exercise its power within the fair limits of its judicial discretion. "We recognize that <i>stare decisions</i> embodies an important social policy. It represents an element of continuity in law, and is rooted in the psychologic need to satisfy reasonable expectations. But <i>stare decisions</i> is a principle of policy and not a mechanical formula of adherence to the latest decision, however recent and questionable. . . ." <i>Helvering</i> v. <i>Hallock,</i> <span class="citation" data-id="9419079"><a href="/opinion/103292/helvering-v-hallock/#119" aria-description="Citation for case: Helvering v. Hallock">309 U. S. 106, 119</a></span>.</p>
<p>Now, while invoking the prior decisions which have given "under color of [law]" a content that ignores the meaning fairly comported by the words of the text and confirmed by the legislative history, the Court undertakes a fresh examination of that legislative history. The decision in this case, therefore, does not rest on <i>stare decisions,</i> and the true construction of the statute may be thought to be as free from the restraints of that doctrine as though the matter were before us for the first time. Certainly, none of the implications which the Court seeks to draw from silences in the minority reports of congressional committees in 1956, 1957, and 1960, or from the use of "under color" language in the very different context of the Act of <span class="citation" data-id="101552"><a href="/opinion/101552/may-v-heiner/#6" aria-description="Citation for case: May v. Heiner">May 6, 1960</a></span>, <span class="star-pagination">*223</span> 74 Stat. 86concerned, in relevant part, with the preservation of election records and with the implementation of the franchiseserves as an impressive bar to re-examination of the true scope of R. S. § 1979 itself in its pertinent legislative setting.<sup>[32]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*224</span> IV.</h2>
<p>This case squarely presents the question whether the intrusion of a city policeman for which that policeman can show no such authority at state law as could be successfully interposed in defense to a state-law action against him, is nonetheless to be regarded as "under color" of state authority within the meaning of R. S. § 1979. Respondents, in breaking into the Monroe apartment, violated the laws of the State of Illinois.<sup>[33]</sup> Illinois law <span class="star-pagination">*225</span> appears to offer a civil remedy for unlawful searches;<sup>[34]</sup> petitioners do not claim that none is available. Rather they assert that they have been deprived of due process of law and of equal protection of the laws under color of state law, although from all that appears the courts of Illinois are available to give them the fullest redress which the common law affords for the violence done them, nor does any "statute, ordinance, regulation, custom, or usage" of the State of Illinois bar that redress. Did the enactment by Congress of § 1 of the Ku Klux Act of 1871 encompass such a situation?</p>
<p>That section, it has been noted, was patterned on the similar criminal provision of § 2, Act of April 9, 1866. The earlier Act had as its primary object the effective nullification of the Black Codes, those statutes of the Southern legislatures which had so burdened and disqualified the Negro as to make his emancipation appear illusory.<sup>[35]</sup> The Act had been vetoed by President Johnson, whose veto message describes contemporary understanding of its second section; the section, he wrote,</p>
<blockquote>"seems to be designed to apply to some existing or future law of State or Territory which may conflict with the provisions of the bill . . . . It provides for counteracting such forbidden legislation by imposing fine and imprisonment upon the legislators who may pass such conflicting laws, or upon the officers or agents who shall put, or attempt to put, them into execution. It means an official offense, not a common <span class="star-pagination">*226</span> crime committed against law upon the persons or property of the black race. Such an act may deprive the black man of his property, but not of the right to hold property. It means a deprivation of the right itself, either by the State judiciary or the State Legislature."<sup>[36]</sup></blockquote>
<p>And Senator Trumbull, then Chairman of the Senate Judiciary Committee,<sup>[37]</sup> in his remarks urging its passage over the veto, expressed the intendment of the second section as those who voted for it read it:</p>
<blockquote>"If an offense is committed against a colored person simply because he is colored, in a State where the law affords him the same protection as if he were white, this act neither has nor was intended to have anything to do with his case, because he has adequate remedies in the State courts; but if he is discriminated against under color of State laws because he is colored, then it becomes necessary to interfere for his protection."<sup>[38]</sup></blockquote>
<p>Section 2 of the 1866 Act was re-enacted in substance in 1870 as part of "An Act to enforce the Right of Citizens. . . to vote in the several States . . . ," <span class="citation no-link">16 Stat. 140</span>, <span class="star-pagination">*227</span> 144. The following colloquy on that occasion is particularly revealing:</p>
<blockquote>"Mr. SHERMAN. . . . My colleague cannot deny that we can by appropriate legislation prevent any private person from shielding himself under a State regulation, and thus denying to a person the right to vote . . . .</blockquote>
<blockquote>"Mr. CASSERLY. I should like to ask the Senator from Ohio how a State can be said to abridge the right of a colored man to vote when some irresponsible person in the streets is the actor in that wrong?</blockquote>
<blockquote>"Mr. SHERMAN. If the offender, who may be a loafer, the meanest man in the streets, covers himself under the protection or color of a law or regulation or constitution of a State, he may be punished for doing it.</blockquote>
<blockquote>"Mr. CASSERLY. Suppose the State law authorizes the colored man to vote; what then?</blockquote>
<blockquote>"Mr. SHERMAN. That is not the case with which we are dealing. . . . This bill only proposes to deal with offenses committed by officers or persons under color of existing State law, under color of existing State constitutions. No man could be convicted under this bill reported by the Judiciary Committee unless the denial of the right to vote was done under color or pretense of State regulation. The whole bill shows that. . . . [T]he first and second sections of the bill . . . simply punish officers as well as persons for discrimination under color of State laws or constitutions; and it so provides all the way through."<sup>[39]</sup></blockquote>
<p><span class="star-pagination">*228</span> The original text of the present § 1979 contained words, left out in the Revised Statutes, which clarified the objective to which the provision was addressed:</p>
<blockquote>"That any person who, under color of any law, statute, ordinance, regulation, custom, or usage of any State, shall subject, or cause to be subjected, any person within the jurisdiction of the United States to the deprivation of any rights, privileges, or immunities secured by the Constitution of the United States, shall, <i>any such law, statute, ordinance, regulation, custom, or usage of the State to the contrary notwithstanding,</i> be liable to the party injured . . . ."<sup>[40]</sup></blockquote>
<p>Representative Shellabarger, reporting the section, explained it to the House as "in its terms carefully confined to giving a civil action for such wrongs against citizenship as are done under color of State laws which abridge these rights."<sup>[41]</sup> Senator Edmunds, steering the measure through the Senate, found constitutional sanction for it in the Fourteenth Amendment, explaining that state action may consist in executive nonfeasance as well as malfeasance, so that any offenses against a citizen in a <span class="star-pagination">*229</span> State are susceptible of federal protection "unless the criminal who shall commit those offenses is punished and the person who suffers receives that redress which the principles and spirit of the laws entitle him to have."<sup>[42]</sup> And James A. Garfield supported the bill in the House as "so guarded as to preserve intact the autonomy of the States, the machinery of the State governments, and the municipal organizations established under State laws."<sup>[43]</sup></p>
<p>Indeed, the Ku Klux Act as a whole encountered in the course of its passage strenuous constitutional objections which focused precisely upon an assertedly unauthorized extension of federal judicial power into areas of exclusive state competence.<sup>[44]</sup> A special target was § 2 of the bill as reported to the House, providing criminal penalties:</p>
<blockquote>"if two or more persons shall, within the limits of any State, band, conspire, or combine together to do <span class="star-pagination">*230</span> any act in violation of the rights, privileges, or immunities of any person, to which he is entitled under the Constitution and laws of the United States, which, committed within a place under the sole and exclusive jurisdiction of the United States, would, under any law of the United States then in force, constitute the crime of either murder, manslaughter, mayhem, robbery, assault and battery, perjury, subornation of perjury, criminal obstruction of legal, process [<i>sic</i>] or resistance of officers in discharge of official duty, arson, or larceny . . . ."<sup>[45]</sup></blockquote>
<p>In vain the proponents of this section argued its propriety, seeking to support it by argument <i>ex necessitate</i> from the complete failure of state judicial and executive organs to control the depredations of the Klan.<sup>[46]</sup> Even <span class="star-pagination">*231</span> in the Reconstruction Congress, the majority party split. Many balked at legislation which they regarded as establishing a general federal jurisdiction for the protection of person and property in the States.<sup>[47]</sup> Only after a complete <span class="star-pagination">*232</span> rewriting of the section to meet these constitutional objections could the bill be passed.<sup>[48]</sup> Yet almost none of those who had decried § 2 as undertaking impermissibly to make the national courts tribunals of concurrent jurisdiction for the punishment of state-law offenses expressed similar objections to § 1, later § 1979.<sup>[49]</sup> One of the most <span class="star-pagination">*233</span> vehement of those who could find no constitutional sanction for federal judicial control of conduct already proscribed by state law, and who therefore opposed original § 2 as reaching beyond the limits of congressional competence, expressly supported § 1 as affording "further redress for violations under State authority of constitutional rights."<sup>[50]</sup></p>
<p>The general understanding of the legislators unquestionably was that, as amended, the Ku Klux Act did "not undertake to furnish redress for wrongs done by one person upon another in any of the States . . . in violation of their laws, unless he also violated some law of the United States, nor to punish one person for an ordinary assault and battery . . . ."<sup>[51]</sup> Even those whoopposing the constitutional objectorsfound sufficient congressional power in the Enforcement Clause of the Fourteenth Amendment to give this kind of redress, deemed inexpedient the exercise of any such power: "Convenience and courtesy to the States suggest a sparing use, and never so far as to supplant the State authorities except in cases of extreme necessity, and when the State governments criminally refuse or neglect those duties which are imposed <span class="star-pagination">*234</span> upon them."<sup>[52]</sup> Extreme Radicals, those who believed that the remedy for the oppressed Unionists in the South was a general expansion of federal judicial jurisdiction so that "loyal men could have the privilege of having their causes, civil and criminal, tried in the Federal courts." were disappointed with the Act as passed.<sup>[53]</sup></p>
<p>Finally, it is significant that the opponents of the Act, exhausting ingenuity to discover constitutional objections to every provision of it, also construed § 1 as addressed only to conduct authorized by state law, and therefore within the admitted permissible reach of Fourteenth Amendment federal power. "The first section of this bill prohibits any invidious legislation by States against the rights or privileges of citizens of the United States," one such opponent paraphrased the provision.<sup>[54]</sup> And Senator Thurman, who insisted vociferously on the absence of federal power to penalize a conspiracy of individuals to violate state law ("that is a case of mere individual violence, having no color whatsoever of authority of law, either Federal or State; and to say that you can punish men for that mere conspiracy, which is their individual act, and which is a crime against the State laws themselves, punishable by the State laws, is simply to wipe out all the State jurisdiction over crimes and transfer it bodily to the Congress"),<sup>[55]</sup> admitted without question the constitutionality of § 1<sup>[56]</sup> ("It refers to a deprivation under color of law, either statute law or `custom or usage' which has become common law").<sup>[57]</sup></p>
<p><span class="star-pagination">*235</span> The Court now says, however, that "It was not the unavailability of state remedies but the failure of certain States to enforce the laws with an equal hand that furnished the powerful momentum behind this `force bill.' " Of course, if the notion of "unavailability" of remedy is limited to mean an absence of statutory, paper right, this is in large part true.<sup>[58]</sup> Insofar as the Court undertakes to demonstrateas the bulk of its opinion seems to do that § 1979 was meant to reach some instances of action not specifically authorized by the avowed, apparent, written law inscribed in the statute books of the States, the argument knocks at an open door. No one would or could deny this, for by its express terms the statute comprehends deprivations of federal rights under color of any "statute, ordinance, regulation, <i>custom, or usage</i>" of a State. (Emphasis added.) The question is, <i>what</i> class of cases other than those involving state statute law were meant to be reached. And, with respect to this question, the Court's conclusion is undermined by the very portions of the legislative debates which it cites. For surely the misconduct of individual municipal police officers, subject to the effective oversight of appropriate state administrative and judicial authorities, presents a situation which differs <i>toto coelo</i> from one in which "Immunity is given to crime, and the records of the public tribunals are searched in vain for any evidence of effective redress,"<sup>[59]</sup> or in which murder rages while a State makes <span class="star-pagination">*236</span> "no successful effort to bring the guilty to punishment or afford protection or redress,"<sup>[60]</sup> or in which the "State courts . . . [are] unable to enforce the criminal laws . . . or to suppress the disorders existing,"<sup>[61]</sup> or in which, in a State's "judicial tribunals one class is unable to secure that enforcement of their rights and punishment for their infraction which is accorded to another,"<sup>[62]</sup> or "of . . . hundreds of outrages . . . not one [is] punished,"<sup>[63]</sup> or "the courts of the . . . States fail and refuse to do their duty in the punishment of offenders against the law,"<sup>[64]</sup> or in which a "class of officers charged under the laws with their administration permanently and as a rule refuse to extend [their] protection."<sup>[65]</sup> These statements indicate that Congressmade keenly aware by the post-bellum conditions in the South that States through their authorities could sanction offenses against the individual by settled practice which established state law as truly as written codesdesigned § 1979 to reach, as well, official conduct which, because engaged in "permanently and as a rule," or "systematically,"<sup>[66]</sup> came through acceptance by law-administering officers to constitute "custom, or usage" having the cast of law. See <i>Nashville, C. &amp; St. L. R. Co.</i> v. <i>Browning,</i> <span class="citation" data-id="103360"><a href="/opinion/103360/nashville-chattanooga-st-louis-railway-v-browning/#369" aria-description="Citation for case: Nashville, Chattanooga &amp; St. Louis Railway v. Browning">310 U. S. 362, 369</a></span>. They do not indicate an attempt to reach, nor does the statute by its terms include, instances of acts in defiance of state law and which no settled state practice, no systematic pattern of official action or inaction, no "custom, or usage, of any State," insulates from effective and adequate reparation by the State's authorities.</p>
<p><span class="star-pagination">*237</span> Rather, all the evidence converges to the conclusion that Congress by § 1979 created a civil liability enforceable in the federal courts only in instances of injury for which redress was barred in the state courts because some "statute, ordinance, regulation, custom, or usage" sanctioned the grievance complained of. This purpose, manifested even by the so-called "Radical" Reconstruction Congress in 1871, accords with the presuppositions of our federal system. The jurisdiction which Article III of the Constitution conferred on the national judiciary reflected the assumption that the state courts, not the federal courts, would remain the primary guardians of that fundamental security of person and property which the long evolution of the common law had secured to one individual as against other individuals. The Fourteenth Amendment did not alter this basic aspect of our federalism.<sup>[67]</sup></p>
<p>Its commands were addressed to the States. Only when the States, through their responsible organs for the formulation and administration of local policy, sought to deny or impede access by the individual to the central government in connection with those enumerated functions assigned to it, or to deprive the individual of a certain minimal fairness in the exercise of the coercive forces of the State, or without reasonable justification to treat him differently than other persons subject to their jurisdiction, was an overriding federal sanction imposed. As between individuals, no corpus of substantive rights was guaranteed by the Fourteenth Amendment, but only "due process of law" in the ascertainment and enforcement of rights and equality in the enjoyment of rights and safeguards that the States afford. This was the base of the distinction between federal citizenship and state <span class="star-pagination">*238</span> citizenship drawn by the <i>Slaughter-House Cases,</i> <span class="citation" data-id="9416892"><a href="/opinion/88661/butchers-benevolent-assn-v-crescent-city-live-stock-landing/" aria-description="Citation for case: Butchers&#x27; Benevolent Ass&#x27;n v. Crescent City Live-Stock...">16 Wall. 36</a></span>. This conception begot the "State action" principle on which, from the time of the <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/" aria-description="Citation for case: Civil Rights Cases">109 U. S. 3</a></span>, this Court has relied in its application of Fourteenth Amendment guarantees. As between individuals, that body of mutual rights and duties which constitute the civil personality of a man remains essentially the creature of the legal institutions of the States.</p>
<p>But, of course, in the present case petitioners argue that the wrongs done them were committed not by individuals but by the police as state officials. There are two senses in which this might be true. It might be true if petitioners alleged that the redress which state courts offer them against the respondents is different than that which those courts would offer against other individuals, guilty of the same conduct, who were not the police. This is not alleged. It might also be true merely because the respondents <i>are</i> the policebecause they are clothed with an appearance of official authority which is in itself a factor of significance in dealings between individuals. Certainly the night-time intrusion of the man with a star and a police revolver is a different phenomenon than the night-time intrusion of a burglar. The aura of power which a show of authority carries with it has been created by state government. For this reason the national legislature, exercising its power to implement the Fourteenth Amendment, might well attribute responsibility for the intrusion to the State and legislate to protect against such intrusion. The pretense of authority alone might seem to Congress sufficient basis for creating an exception to the ordinary rule that it is to the state tribunals that individuals within a State must look for redress against other individuals within that State. The same pretense of authority might suffice to sustain congressional legislation creating the exception. See <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339</a></span>. But until Congress has <span class="star-pagination">*239</span> declared its purpose to shift the ordinary distribution of judicial power for the determination of causes between co-citizens of a State, this Court should not make the shift. Congress has not in § 1979 manifested that intention.</p>
<p>The unwisdom of extending federal criminal jurisdiction into areas of conduct conventionally punished by state penal law is perhaps more obvious than that of extending federal civil jurisdiction into the traditional realm of state tort law. But the latter, too, presents its problems of policy appropriately left to Congress. Suppose that a state legislature or the highest court of a State should determine that within its territorial limits no damages should be recovered in tort for pain and suffering, or for mental anguish, or that no punitive damages should be recoverable. Since the federal courts went out of the business of making "general law," <i>Erie R. Co.</i> v. <i>Tompkins,</i> <span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">304 U. S. 64</a></span>, such decisions of local policy have admittedly been the exclusive province of state lawmakers. Should the civil liability for police conduct which can claim no authority under local law, which is actionable as common-law assault or trespass in the local courts, comport different rules? Should an unlawful intrusion by a policeman in Chicago entail different consequences than an unlawful intrusion by a hoodlum? These are matters of policy in its strictly legislative sense, not for determination by this Court. And if it be, as it is, a matter for congressional choice, the legislative evidence is overwhelming that § 1979 is not expressive of that choice. Indeed, its precise limitation to acts "under color" of state statute, ordinance or other authority appears on its face designed to leave all questions of the nature and extent of liability of individuals to the laws of the several States except when a State seeks to shield those individuals under the special barrier of state authority. To extend Civil Rights Act liability beyond that point is <span class="star-pagination">*240</span> to interfere in areas of state policymaking where Congress has not determined to interfere.</p>
<p>Nor will such interference be negligible. One argument urged in <i><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">Screws</a></span></i> in favor of the result which that case reached was the announced policy of self-restraint of the Department of Justice in the prosecution of cases under <span class="citation no-link">18 U. S. C. § 242</span>. See <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/#159" aria-description="Citation for case: Screws v. United States">325 U. S., at 159-160</a></span>. Experience indicates that private litigants cannot be expected to show the same consideration for the autonomy of local administration which the Department purportedly shows.<sup>[68]</sup></p>
<p>Relevant also are the effects upon the institution of federal constitutional adjudication of sustaining under § 1979 damage actions for relief against conduct allegedly violative of federal constitutional rights, but plainly <span class="star-pagination">*241</span> violative of state law. Permitting such actions necessitates the immediate decision of federal constitutional issues despite the admitted availability of state-law remedies which would avoid those issues.<sup>[69]</sup> This would make inroads, throughout a large area, upon the principle of federal judicial self-limitation which has become a significant instrument in the efficient functioning of the national judiciary. See

[...TRUNCATED 140224 of 260224 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/New York v. Belton.md  (`case`, 7 assertions)

### content_page

```
---
title: "New York v. Belton"
type: case
citation: "453 U.S. 454 (1981)"
parallel_cite: "101 S. Ct. 2860; 69 L. Ed. 2d 768"
neutral_cite: 1981 U.S. LEXIS 13
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-09-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 2026-06-30
  as_of_treatment: 2026-06-30
  composite_basis: principal-holding
  composite_basis_ref: search.vehicle.sia-recent-occupant
  varies_by_point: true
  scope_note: "Composite reflects the principal holding; the vehicle-search point is superseded by Arizona v. Gant (2009) — Belton's container rule survives within Gant's narrowed framework."
  point_overrides:
    - point: search.vehicle.sia-recent-occupant
      point_label: "Vehicle search incident to a recent occupant's arrest"
      field_i_validity: superseded
      as_of_treatment: 2026-06-30
      s3_binding_status: bound
      by:
        - name: Arizona v. Gant
          cluster_id: 145887
          cite: 556 U.S. 332
          field_ii: limited
      scope_note: "The automatic passenger-compartment rule is replaced by Gant's two-justification test."
lake:
  record_id: New York v. Belton
  status: verified
  projected_at: 2026-07-06
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110559/new-york-v-belton/"
  cluster_id: 110559
  opinion_id: 9428488
  identity_checked: true
homes:
  - page: "[[SIA Vehicles]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
related: ["[[Arizona v. Gant]]", "[[Chimel v. California]]", "[[Thornton v. United States]]", "[[Davis v. United States (2011)|Davis v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile", "vehicle-search"]
holding: "Defines the SCOPE of a vehicle search incident to arrest: on a lawful custodial arrest of a vehicle occupant, police may search the…"
---

# New York v. Belton

*453 U.S. 454 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Caution — varies by point**
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A police officer stopped a speeding car with four occupants, smelled marijuana, and saw an envelope he associated with marijuana. He ordered the occupants out, arrested all four, and searched the passenger compartment, finding cocaine in the zipped pocket of Belton's jacket on the back seat.

## Issue
What is the permissible scope of a search of an automobile's passenger compartment incident to the lawful custodial arrest of an occupant.

## Rule
The Court adopted a [[Common Legal Terms#bright-line-rule|bright-line rule]]: "when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile." — 453 U.S. at 460. ^pin-460

"It follows from this conclusion that the police may also examine the contents of any containers found within the passenger compartment." — *Id.* ^pin-460b

**This bright-line authority was later limited by [[Arizona v. Gant]]** as applied to vehicle [[Search Incident to Arrest|searches incident to arrest]] (see Treatment).

## Application
Because the officer had made lawful custodial arrests of the car's occupants, he was entitled to search the passenger compartment as a contemporaneous incident of those arrests, including the zipped pocket of the jacket on the back seat. On these facts the cocaine was the product of a lawful [[Search Incident to Arrest|search incident to arrest]].

## Conclusion
The search of the jacket was a lawful [[Search Incident to Arrest|search incident to arrest]]; the New York Court of Appeals' suppression order was reversed.

## Treatment & subsequent history

**Composite: Caution — treatment varies by point.** *Belton* is not simply "good" or "bad" law; its validity depends on which point you rely on.

| Point of law | Status | Controlling authority |
|---|---|---|
| Vehicle search incident to a recent occupant's arrest | **Superseded** | *[[Arizona v. Gant]]*, 556 U.S. 332 (2009) — the automatic passenger-compartment rule is replaced by *[[Arizona v. Gant\|Gant]]*'s two-justification test |
| Containers within the passenger compartment (within a lawful search) | **Good law** | *Belton*'s container rule survives inside *[[Arizona v. Gant\|Gant]]*'s narrowed framework |

*[[Arizona v. Gant|Gant]]* rejected the broad reading of *Belton* that authorized an automatic passenger-compartment search whenever an occupant was arrested. After *[[Arizona v. Gant|Gant]]*, a vehicle [[Search Incident to Arrest|search incident to arrest]] is permissible only if the arrestee is within reaching distance of the passenger compartment at the time of the search, or it is reasonable to believe the vehicle contains evidence of the offense of arrest. Officers' reasonable pre-*[[Arizona v. Gant|Gant]]* reliance on *Belton* was addressed in [[Davis v. United States (2011)|Davis v. United States]].

## Appears on
- [[SIA Vehicles]] — *Key — Progeny / Refinement*
- [[Traffic Stops]] — *Related (cross-doctrine)*

## Sources
- *New York v. Belton*, 453 U.S. 454 (1981) — https://www.courtlistener.com/opinion/110559/new-york-v-belton/ — pinpoint: 460.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "01987a56b2574d60", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "453 U.S. 454 (1981)", "court": "U.S. Supreme Court", "neutral_cite": "1981 U.S. LEXIS 13", "official_citation_present": true, "parallel_cite": "101 S. Ct. 2860; 69 L. Ed. 2d 768", "title": "New York v. Belton", "year": "1981"}}
{"assertion_id": "166c581f1f198dca", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Related (cross-doctrine)", "title": "New York v. Belton"}}
{"assertion_id": "268bca330823eee8", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Vehicles"}, "payload": {"home": "SIA Vehicles", "role": "Key — Progeny / Refinement", "title": "New York v. Belton"}}
{"assertion_id": "5b557fb6f4a0e52d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Defines the SCOPE of a vehicle search incident to arrest: on a lawful custodial arrest of a vehicle occupant, police may search the…", "title": "New York v. Belton"}}
{"assertion_id": "12c93532ae2dc714", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2026-06-30", "as_of_treatment": "2026-06-30", "composite_basis": "principal-holding", "composite_basis_ref": "search.vehicle.sia-recent-occupant", "field_i_validity": "caution", "scope_note": "Composite reflects the principal holding; the vehicle-search point is superseded by Arizona v. Gant (2009) — Belton's container rule survives within Gant's narrowed framework.", "title": "New York v. Belton", "varies_by_point": "true"}}
{"assertion_id": "9386a34d1af324a2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "New York v. Belton"}}
{"assertion_id": "a2aa0b0a530592b5", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "search.vehicle.sia-recent-occupant"}, "payload": {"by": [{"cite": "556 U.S. 332", "cluster_id": "145887", "field_ii": "limited", "name": "Arizona v. Gant"}], "field_i_validity": "superseded", "point": "search.vehicle.sia-recent-occupant", "point_label": "Vehicle search incident to a recent occupant's arrest", "s3_binding_status": "bound", "title": "New York v. Belton"}}
```

### lake record — New York v. Belton

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Belton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Belton",
    "case_name_short": "Belton",
    "case_name_full": "New York v. Belton",
    "input_case_name": "New York v. Belton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-09-23",
    "year": 1981,
    "docket": null,
    "cluster_id": 110559,
    "lead_opinion_id": 9428488,
    "sibling_ids": [
      110559,
      9428488,
      9428489,
      9428490,
      9428491,
      9428492
    ],
    "absolute_url": "/opinion/110559/new-york-v-belton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9031723,
        "score": 20,
        "case_name": "New York v. Belton"
      },
      {
        "cluster_id": 9030420,
        "score": 20,
        "case_name": "New York v. Belton"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "453 U.S. 454",
      "volume": "453",
      "reporter": "U.S.",
      "page": "454",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2860",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2860",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 768",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "768",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 13",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "453 U.S. 454",
        "volume": "453",
        "reporter": "U.S.",
        "page": "454",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2860",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2860",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 768",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "768",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 13",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "453 U.S. 454",
    "official_selection": {
      "court_class": "scotus",
      "selected": "453 U.S. 454",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-460",
      "page": null,
      "quote": "--- # New York v. Belton *453 U.S. 454 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **Caution \u2014 varies by point** <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A police officer stopped a speeding car with four occupants, smelled marijuana, and saw an envelope he associated with marijuana. He ordered the occupants out, arrested all four, and searched the passenger compartment, finding cocaine in the zipped pocket of Belton's jacket on the back seat. ## Issue What is the permissible scope of a search of an automobile's passenger compartment incident to the lawful custodial arrest of an occupant. ## Rule The Court adopted a bright-line rule:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-460b",
      "page": null,
      "quote": "It follows from this conclusion that the police may also examine the contents of any containers found within the passenger compartment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "2026-06-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "principal-holding",
    "composite_basis_ref": "search.vehicle.sia-recent-occupant",
    "varies_by_point": true,
    "scope_note": "Composite reflects the principal holding; the vehicle-search point is superseded by Arizona v. Gant (2009) \u2014 Belton's container rule survives within Gant's narrowed framework.",
    "point_overrides": [
      {
        "point": "search.vehicle.sia-recent-occupant",
        "point_label": "Vehicle search incident to a recent occupant's arrest",
        "field_i_validity": "superseded",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "bound",
        "by": [
          {
            "name": "Arizona v. Gant",
            "cluster_id": 145887,
            "cite": "556 U.S. 332",
            "field_ii": "limited"
          }
        ],
        "scope_note": "The automatic passenger-compartment rule is replaced by Gant's two-justification test."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andre Anderson v. State of Indiana",
          "cluster_id": 4327181,
          "cite": [
            "64 N.E.3d 903",
            "2016 Ind. App. LEXIS 432",
            "2016 WL 7078344"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Arredondo",
          "cluster_id": 6238731,
          "cite": [
            "199 Cal. Rptr. 3d 563",
            "245 Cal. App. 4th 186",
            "2016 Cal. App. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jermaine Lebron v. State of Florida",
          "cluster_id": 2686855,
          "cite": [
            "135 So. 3d 1040",
            "39 Fla. L. Weekly Supp. 62",
            "2014 WL 321817",
            "2014 Fla. LEXIS 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Long",
          "cluster_id": 111020,
          "cite": [
            "77 L. Ed. 2d 1201",
            "103 S. Ct. 3469",
            "463 U.S. 1032",
            "1983 U.S. LEXIS 7",
            "51 U.S.L.W. 5231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Wilson",
          "cluster_id": 118086,
          "cite": [
            "137 L. Ed. 2d 41",
            "117 S. Ct. 882",
            "519 U.S. 408",
            "1997 U.S. LEXIS 1271"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ballard",
          "cluster_id": 1533349,
          "cite": [
            "987 S.W.2d 889",
            "1999 Tex. Crim. App. LEXIS 14",
            "1999 WL 89535"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knowles v. Iowa",
          "cluster_id": 118250,
          "cite": [
            "142 L. Ed. 2d 492",
            "119 S. Ct. 484",
            "525 U.S. 113",
            "1998 U.S. LEXIS 8068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Square",
          "cluster_id": 1827528,
          "cite": [
            "433 So. 2d 104"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Archer v. Commonwealth",
          "cluster_id": 1067256,
          "cite": [
            "492 S.E.2d 826",
            "26 Va. App. 1",
            "1997 Va. App. LEXIS 683"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110559 OR 9428488 OR 9428489 OR 9428490 OR 9428491 OR 9428492) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjk3ODE0NDAwMDAwJnM9MzEyODkxNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110559+OR+9428488+OR+9428489+OR+9428490+OR+9428491+OR+9428492%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110559 OR 9428488 OR 9428489 OR 9428490 OR 9428491 OR 9428492)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNzYmcz0zMDA2NDExJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110559+OR+9428488+OR+9428489+OR+9428490+OR+9428491+OR+9428492%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110559 OR 9428488 OR 9428489 OR 9428490 OR 9428491 OR 9428492)",
        "reviewed": 27,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 27,
        "triage_read": 1,
        "triage_snippet_classified": 26
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110559 OR 9428488 OR 9428489 OR 9428490 OR 9428491 OR 9428492)",
    "indexed_citing_opinions": 2230,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110559,
        "count": 2032,
        "count_source": "search"
      },
      {
        "opinion_id": 9428488,
        "count": 238,
        "count_source": "search"
      },
      {
        "opinion_id": 9428489,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428490,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428491,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428492,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3483,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-belton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NTY0NTkmcz05NjkxMjk4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110559+OR+9428488+OR+9428489+OR+9428490+OR+9428491+OR+9428492%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110559,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 109196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 347138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 382105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 382713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 382715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 1391930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 1687668,
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
    "date_created": "2026-07-05T15:31:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:32:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm",
        "at": "2026-07-05T15:32:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:32:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Belton

```
<opinion type="majority">
<author id="b497-8">Justice Stewart</author>
<p id="AyB">delivered the opinion of the Court.</p>
<p id="b497-9">When the occupant of an automobile is subjected to a lawful custodial arrest, does the constitutionally permissible scope of a search incident to his arrest include the passenger compartment of the automobile in which he was riding? That is the question at issue in the present case.</p>
<p id="b497-10">I</p>
<p id="b497-11">On April 9, 1978, Trooper Douglas Nicot, a New York State policeman driving an unmarked car on the New York Thruway, was passed by another automobile traveling at an excessive rate of speed. Nicot gave chase, overtook the speeding vehicle, and ordered its driver to pull it over to the side of the road and stop. There were four men in the car, one of whom was Roger Belton, the respondent in this case. The policeman asked to see the driver’s license and automobile registration, and discovered that none of the men owned the vehicle or was related to its owner. Meanwhile, the policeman had smelled burnt marihuana and had seen on <page-number citation-index="1" label="456">*456</page-number>the floor of the car an envelope marked “Supergold” that he associated with marihuana. He therefore directed the men to get out of the car, and placed them under arrest for the unlawful possession of marihuana. He patted down each of the men and “split them up into four separate areas of the Thruway at this time so they would not be in physical touching area of each other.” He then picked up the envelope marked “Supergold” and found that it contained marihuana. After giving the arrestees the warnings required by <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, the state policeman searched each one of them. He then searched the passenger compartment of the car. On the back seat he found a black leather jacket belonging to Belton. He unzipped one of the pockets of the jacket and discovered cocaine. Placing the jacket in his automobile, he drove the four arrestees to a nearby police station.</p>
<p id="b498-5">Belton was subsequently indicted for criminal possession of a controlled substance. In the trial court he moved that the cocaine the trooper had seized from the jacket pocket be suppressed. The court denied the motion. Belton then pleaded guilty to a lesser included offense, but preserved his claim that the cocaine had been seized in violation of the Fourth and Fourteenth Amendments. See <em>Lefkowitz </em>v. <em>Newsome, </em><span class="citation" data-id="9426003"><a href="/opinion/109196/lefkowitz-v-newsome/" aria-description="Citation for case: Lefkowitz v. Newsome">420 U. S. 283</a></span>. The Appellate Division of the New York Supreme Court upheld the constitutionality of the search and seizure, reasoning that “[o]nce defendant was validly arrested for possession of marihuana, the officer was justified in searching the immediate area for other contraband.” 68 App. Div. 2d 198, 201, 416 N. Y. S. 2d 922, 926.</p>
<p id="b498-6">The New York Court of Appeals reversed, holding that “[a] warrantless search of the zippered pockets of an unacces-sible jacket may not be upheld as a search incident to a lawful arrest where there is no longer any danger that the arrestee or a confederate might gain access to the article.” 60 N. Y. 2d 447, 449, <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#421" aria-description="Citation for case: People v. Belton">407 N. E. 2d 420, 421</a></span>. Two judges dis<page-number citation-index="1" label="457">*457</page-number>sented. They pointed out that the “search was conducted by a lone peace officer who was in the process of arresting four unknown individuals whom he had stopped in a speeding car owned by none of them and apparently containing an uncertain quantity of a controlled substance. The suspects were standing by the side of the car as the officer gave it a quick check to confirm his suspicions before attempting to transport them to police headquarters . . . <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#454" aria-description="Citation for case: People v. Belton"><em>Id., </em>at 454</a></span>, <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#424" aria-description="Citation for case: People v. Belton">407 N. E. 2d, at 424</a></span>. We granted certiorari to consider the constitutionally permissible scope of a search in circumstances such as these. <span class="citation multiple-matches"><a href="/c/U.%20S./449/1109/">449 U. S. 1109</a></span>.</p>
<p id="b499-4">II</p>
<p id="b499-5">It is a first principle of Fourth Amendment jurisprudence that the police may not conduct a search unless they first convince a neutral magistrate that there is probable cause to do so. This Court has recognized, however, that “the exigencies of the situation” may sometimes make exemption from the warrant requirement “imperative.” <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span>. Specifically, the Court held in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, that a lawful custodial arrest creates a situation which justifies the contemporaneous search without a warrant of the person arrested and of the immediately surrounding area. Such searches have long been considered valid because of the need “to remove any weapons that [the arrestee] might seek to use in order to resist arrest or effect his escape” and the need to prevent the concealment or destruction of evidence. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><em>Id., </em>at 763</a></span>.</p>
<p id="b499-6">The Court’s opinion in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>emphasized the principle that, as the Court had said in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span>, “[t]he scope of [a] search must be 'strictly tied to and justified by’ the circumstances which rendered its initiation permissible.” Quoted in <em>Chimel </em>v. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California"><em>California, supra, </em>at 762</a></span>. Thus while the Court in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>found “ample justification” for a search of “the area from within which [an arrestee] <page-number citation-index="1" label="458">*458</page-number>might gain possession of a weapon or destructible evidence,” the Court found “no comparable justification ... for routinely searching any room other than that in which an arrest occurs — or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>.</p>
<p id="b500-5">Although the principle that limits a search incident to a lawful custodial arrest may be stated clearly enough, courts have discovered the principle difficult to apply in specific cases. Yet, as one commentator has pointed out, the protection of the Fourth and Fourteenth Amendments “can only be realized if the police are acting under a set of rules which, in most instances, makes it possible to reach a correct determination beforehand as to whether an invasion of privacy is justified in the interest of law enforcement.” LaFave, “Case-By-Case Adjudication” versus “Standardized Procedures”: The Robinson Dilemma, 1974 S. Ct. Rev. 127, 142. This is because</p>
<blockquote id="b500-6">“Fourth Amendment doctrine, given force and effect by the exclusionary rule, is primarily intended to regulate the police in their day-to-day activities and thus ought to be expressed in terms that are readily applicable by the police in the context of the law enforcement activities in which they are necessarily engaged. A highly sophisticated set of rules, qualified by all sorts of ifs, ands, and buts and requiring the drawing of subtle nuances and hairline distinctions, may be the sort of heady stuff upon which the facile minds of lawyers and judges eagerly feed, but they may be 'literally impossible of application by the officer in the field.’ ” <em>Id., </em>at 141.</blockquote>
<p id="b500-7">In short, “[a] single familiar standard is essential to guide police officers, who have only limited time and expertise to reflect on and balance the social and individual interests involved in the specific circumstances they confront.” <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span>.</p>
<p id="b501-4"><page-number citation-index="1" label="459">*459</page-number>So it was that, in <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span>, the Court hewed to a straightforward rule, easily applied, and predictably enforced: “[I]n the case of a lawful custodial arrest a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a 'reasonable’ search under that Amendment.” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><em>Id., </em>at 235</a></span>. In so holding, the Court rejected the suggestion that “there must be litigated in each case the issue of whether or not there was present one of the reasons supporting the authority for a search of the person incident to a lawful arrest.” <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Ibid.</a></span></em></p>
<p id="b501-5">But no straightforward rule has emerged from the litigated cases respecting the question involved here — the question of the proper scope of a search of the interior of an automobile incident to a lawful custodial arrest of its occupants. The difficulty courts have had is reflected in the conflicting views of the New York judges who dealt with the problem in the present case, and is confirmed by a look at even a small sample drawn from the narrow class of cases in which courts have decided whether, in the course of a search incident to the lawful custodial arrest of the occupants of an automobile, police may search inside the automobile after the arrestees are no longer in it. On the one hand, decisions in cases such as <em>United States </em>v. <em>Sanders, </em><span class="citation" data-id="9467153"><a href="/opinion/382713/united-states-v-willard-r-sanders/" aria-description="Citation for case: United States v. Willard R. Sanders">631 F. 2d 1309</a></span> (CA8 1980); <em>United States </em>v. <em>Dixon, </em><span class="citation" data-id="347138"><a href="/opinion/347138/united-states-v-lewis-nathaniel-dixon/" aria-description="Citation for case: United States v. Lewis Nathaniel Dixon">558 F. 2d 919</a></span> (CA9 1977); and <em>United States </em>v. <em>Frick, </em><span class="citation" data-id="9460209"><a href="/opinion/316377/united-states-v-robert-lee-frick-and-quimet-john-petersen/" aria-description="Citation for case: United States v. Robert Lee Frick and Quimet John Petersen">490 F. 2d 666</a></span> (CA5 1973), have upheld such warrantless searches as incident to lawful arrests. On the other hand, in cases such as <em>United States </em>v. <em>Benson, </em><span class="citation" data-id="9467155"><a href="/opinion/382715/united-states-v-jeffrey-joseph-benson/" aria-description="Citation for case: United States v. Jeffrey Joseph Benson">631 F. 2d 1336</a></span> (CA8 1980), and <em>United States </em>v. <em>Rigales, </em><span class="citation" data-id="382105"><a href="/opinion/382105/united-states-v-ernesto-g-rigales-jr/" aria-description="Citation for case: United States v. Ernesto G. Rigales, Jr.">630 F. 2d 364</a></span> (CA5 1980), such searches, in comparable factual circumstances, have been held constitutionally invalid.<footnotemark>1</footnotemark></p>
<p id="b501-6">When a person cannot know how a court will apply a <page-number citation-index="1" label="460">*460</page-number>settled principle to a recurring factual situation, that person cannot know the scope of his constitutional protection, nor can a policeman know the scope of his authority. While the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>case established that a search incident to an arrest may not stray beyond the area within the immediate control of the arrestee, courts have found no workable definition of “the area within the immediate control of the arrestee” when that area arguably includes the interior of an automobile and the arrestee is its recent occupant. Our reading of the cases suggests the generalization that articles inside the relatively narrow compass of the passenger compartment of an automobile are in fact generally, even if not inevitably, within “the area into which an arrestee might reach in order to grab a weapon or evidentiary ite[m].” <em>Chimel, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. In order to establish the workable rule this category of cases requires, we read Chimel’s definition of the limits of the area that may be searched in light of that generalization. Accordingly, we hold that when a policeman has made a lawful custodial arrest of the occupant of an automobile,<footnotemark>2</footnotemark> he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile.<footnotemark>3</footnotemark></p>
<p id="b502-5">It follows from this conclusion that the police may also examine the contents of any containers found within the passenger compartment, for if the passenger compartment is within reach of the arrestee, so also will containers in it be within his reach.<footnotemark>4</footnotemark> <em>United States </em>v. <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra;</a></span> Draper </em><page-number citation-index="1" label="461">*461</page-number>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. Such a container may, of course, be searched whether it is open or closed, since the justification for the search is not that the arrestee has no privacy interest in the container, but that the lawful custodial arrest justifies the infringement of any privacy interest the arrestee may have. Thus, while the Court in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>held that the police could not search all the drawers in an arrestee’s house simply because the police had arrested him at home, the Court noted that drawers within an arrestee’s reach could be searched because of the danger their contents might pose to the police. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>.</p>
<p id="b503-5">It is true, of course, that these containers will sometimes be such that they could hold neither a weapon nor evidence of the criminal conduct for which the suspect was arrested. However, in <em>United States </em>v. <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>, </em>the Court rejected the argument that such a container — there a “crumpled up' cigarette package” — located during a search of Robinson incident to his arrest could not be searched: “The authority to search the person incident to a lawful custodial arrest, while based upon the need to disarm and to discover evidence, does not depend on what a court may later decide was the probability in a particular arrest situation that weapons or evidence would in fact be found upon the person of the suspect. A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification.” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson">414 U. S., at 235</a></span>.</p>
<p id="b503-6">The New York Court of Appeals relied upon <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span>, and <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span>, in concluding that the search and seizure in the present case were constitutionally invalid.<footnotemark>5</footnotemark> But neither of those <page-number citation-index="1" label="462">*462</page-number>cases involved an arguably valid search incident to a lawful custodial arrest. As the Court pointed out in the <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>case: “Here the search was conducted more than an hour after federal agents had gained exclusive control of the footlocker and long after respondents were securely in custody; the search therefore cannot be viewed as incidental to the arrest or as justified by any other exigency.” <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#15" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 15</a></span>. And in the <em>Sanders </em>case, the Court explicitly stated that it did not “consider the constitutionality of searches of luggage incident to the arrest of its possessor. See, <em>e. g., United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973). The State has not argued that respondent’s suitcase was searched incident to his arrest, and it appears that the bag was not within his ‘immediate control’ at the time of the search.” 442 U. S., at 764, n. 11. (The suitcase in question was in the trunk of the taxicab. See n. 4, <em>supra.)</em></p>
<p id="b504-5">Ill</p>
<p id="b504-6">It is not questioned that the respondent was the subject of a lawful custodial arrest on a charge of possessing marihuana. The search of the respondent’s jacket followed immediately upon that arrest. The jacket was located inside the passenger compartment of the car in which the respondent had been a passenger just before he was arrested. The jacket was. thus within the area which we have concluded was “within the arrestee’s immediate control” within the meaning of the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>case.<footnotemark>6</footnotemark> The search of the jacket, therefore, was a <page-number citation-index="1" label="463">*463</page-number>search incident to a lawful custodial arrest, and it did not violate the Fourth and Fourteenth Amendments. Accordingly, the judgment is reversed.</p>
<p id="b505-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b501-7"> The state-court cases are in similar disarray. Compare, <em>e. g., Hinkel </em>v. <em>Anchorage, </em><span class="citation" data-id="9617077"><a href="/opinion/1391930/hinkel-v-anchorage/" aria-description="Citation for case: Hinkel v. Anchorage">618 P. 2d 1069</a></span> (Alaska 1980), with <em>Ulesky </em>v. <em>State, </em><span class="citation" data-id="1687668"><a href="/opinion/1687668/ulesky-v-state/" aria-description="Citation for case: Ulesky v. State">379 So. 2d 121</a></span> (Fla. App. 1979).</p>
</footnote>
<footnote label="2">
<p id="b502-6"> The validity of the custodial arrest of Belton has not been questioned in this case. Cf. <em>Gustafson </em>v. <em>Florida </em><span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#266" aria-description="Citation for case: Gustafson v. Florida">414 U. S. 260, 266</a></span> (concurring opinion).</p>
</footnote>
<footnote label="3">
<p id="b502-7"> Our holding today does no more than determine the meaning of Chimel’s principles in this particular and problematic context. It in no way alters the fundamental principles established in the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>case regarding the basic scope of searches incident to lawful custodial arrests.</p>
</footnote>
<footnote label="4">
<p id="b502-8"> “Container” here denotes any object capable of holding another object. It thus includes closed or open glove compartments, consoles, or other receptacles located anywhere within the passenger compartment, as well as <page-number citation-index="1" label="461">*461</page-number>luggage, boxes, bags, clothing, and the like. Our holding encompasses only the interior of the passenger compartment of an automobile and does not encompass the trunk.</p>
</footnote>
<footnote label="5">
<p id="b503-10"> It seems to have been the theory of the Court of Appeals that the search and seizure in the present case could not have been incident to the <page-number citation-index="1" label="462">*462</page-number>respondent’s arrest, because Trooper Nicot, by the very act of searching the respondent’s jacket and seizing the contents of its pocket, had gained “exclusive control” of them. 50 N. Y. 2d 447, 451, <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#422" aria-description="Citation for case: People v. Belton">407 N. E. 2d 420, 422</a></span>. But under this fallacious theory no search or seizure incident to a lawful custodial arrest would ever be valid; by seizing an article even on the arrestee’s person, an officer may be said to have reduced that article to his “exclusive control.”</p>
</footnote>
<footnote label="6">
<p id="b504-8"> Because of this disposition of the case, there is no need here to consider whether the search and seizure were permissible under the so-called <page-number citation-index="1" label="463">*463</page-number>“automobile exception.” <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span>; <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Olmstead v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Olmstead v. United States"
type: case
citation: "277 U.S. 438 (1928)"
parallel_cite: "48 S. Ct. 564; 72 L. Ed. 944; 66 A.L.R. 376"
neutral_cite: 1928 U.S. LEXIS 694
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1928
date_decided: 1928-06-04
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1928-06-04
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Olmstead v. United States
  varies_by_point: false
  scope_note: "Overruled on the privacy point by Katz v. United States (1967); survives only as history. The property-trespass approach was later revived as an alternative test in United States v. Jones (2012)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/101320/olmstead-v-united-states/"
  cluster_id: 101320
  opinion_id: 101320
  identity_checked: true
homes:
  - page: "[[Trespass]]"
    role: "Historical / origin"
  - page: "[[Electronic Surveillance and Title III]]"
    role: "Key — Historical (overruled by Katz)"
related: ["[[Katz v. United States]]", "[[United States v. Jones]]", "[[Berger v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "wiretap", "trespass", "overruled", "historical"]
holding: "Wiretapping with no physical entry was not a search — pure property/trespass framing; overruled on the privacy point by *Katz* (property instinct later revived by *Jones*)."
lake:
  record_id: Olmstead v. United States
  status: verified
  projected_at: 2026-07-09
---

# Olmstead v. United States

*277 U.S. 438 (1928)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal Prohibition agents gathered evidence against a large bootlegging operation by wiretapping the defendants' telephone lines. The taps were placed on wires in the streets and in the basement of the building — without any physical trespass into the defendants' homes or offices.

## Issue
Whether wiretapping a person's telephone conversations, accomplished without physical entry into a constitutionally protected area, is a "search and seizure" within the Fourth Amendment.

## Rule
*(Historical — this holding has been overruled; see Treatment.)* The Court tied Fourth Amendment protection to physical trespass and tangible things: "The Amendment itself shows that the search is to be of material things — the person, the house, his papers or his effects." — 277 U.S. at 464. ^pin-464

Because the wiretaps involved no physical entry, the Court held there was no search or seizure: "There was no searching. There was no seizure. The evidence was secured by the use of the sense of hearing and that only." — [*Id.*](https://www.courtlistener.com/opinion/101320/olmstead-v-united-states/#:~:text=There%20was%20no%20searching.%20There) ^pin-464b

## Application
Because the wiretaps involved no physical entry into the defendants' premises and seized no tangible "material things" — only overheard conversations — the Court held there had been no search or seizure, and the wiretap evidence was admissible against Olmstead.

## Conclusion
On these facts the warrantless wiretapping was held not to be a Fourth Amendment search, and the convictions were affirmed. *(This holding no longer states the law — see Treatment.)*

## Treatment & subsequent history
- **Status:** overruled *(as of 2026-06-30)* — **Historical**.
- **Overruled by [[Katz v. United States]] (1967)**, which rejected *Olmstead*'s trespass and "material things" framing and held that the Fourth Amendment protects people, not places, so that a warrantless wiretap of a telephone conversation is a search. The property-trespass approach *Olmstead* embodied was later partially revived as an alternative test in [[United States v. Jones]] (2012), but *Olmstead*'s holding that wiretapping is not a search remains overruled.

## Appears on
- [[Trespass]] — *Historical / origin*
- [[Electronic Surveillance and Title III]] — *Key — Historical (overruled by Katz)*

## Sources
- *Olmstead v. United States*, 277 U.S. 438 (1928) — https://www.courtlistener.com/opinion/101320/olmstead-v-united-states/ — pinpoint: 464.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d6966e390d0a60f2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "277 U.S. 438 (1928)", "court": "U.S. Supreme Court", "neutral_cite": "1928 U.S. LEXIS 694", "official_citation_present": true, "parallel_cite": "48 S. Ct. 564; 72 L. Ed. 944; 66 A.L.R. 376", "title": "Olmstead v. United States", "year": "1928"}}
{"assertion_id": "03bdde9aed40fa58", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Wiretapping with no physical entry was not a search — pure property/trespass framing; overruled on the privacy point by *Katz* (property instinct later revived by *Jones*).", "title": "Olmstead v. United States"}}
{"assertion_id": "438875892ec94eb3", "dimension": "support", "kind": "home_role", "locator": {"home": "Electronic Surveillance and Title III"}, "payload": {"home": "Electronic Surveillance and Title III", "role": "Key — Historical (overruled by Katz)", "title": "Olmstead v. United States"}}
{"assertion_id": "b2b213e2b42220d2", "dimension": "support", "kind": "home_role", "locator": {"home": "Trespass"}, "payload": {"home": "Trespass", "role": "Historical / origin", "title": "Olmstead v. United States"}}
{"assertion_id": "87f945dbefeadad3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Olmstead v. United States"}}
{"assertion_id": "a450281457d3bd23", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1928-06-04", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Olmstead v. United States", "field_i_validity": "superseded", "scope_note": "Overruled on the privacy point by Katz v. United States (1967); survives only as history. The property-trespass approach was later revived as an alternative test in United States v. Jones (2012).", "title": "Olmstead v. United States", "varies_by_point": "false"}}
```

### lake record — Olmstead v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Olmstead v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Olmstead v. United States",
    "case_name_short": "Olmstead",
    "case_name_full": "OLMSTEAD Et Al. v. UNITED STATES; GREEN Et Al. v. SAME; McINNIS v. SAME",
    "input_case_name": "Olmstead v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1928-06-04",
    "year": 1928,
    "docket": null,
    "cluster_id": 101320,
    "lead_opinion_id": 101320,
    "sibling_ids": [
      101320,
      9418652,
      9418653,
      9418654,
      9418655,
      9418656
    ],
    "absolute_url": "/opinion/101320/olmstead-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "277 U.S. 438",
      "volume": "277",
      "reporter": "U.S.",
      "page": "438",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "48 S. Ct. 564",
        "volume": "48",
        "reporter": "S. Ct.",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 L. Ed. 944",
        "volume": "72",
        "reporter": "L. Ed.",
        "page": "944",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 A.L.R. 376",
        "volume": "66",
        "reporter": "A.L.R.",
        "page": "376",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1928 U.S. LEXIS 694",
        "volume": "1928",
        "reporter": "U.S. LEXIS",
        "page": "694",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "277 U.S. 438",
        "volume": "277",
        "reporter": "U.S.",
        "page": "438",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 S. Ct. 564",
        "volume": "48",
        "reporter": "S. Ct.",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 L. Ed. 944",
        "volume": "72",
        "reporter": "L. Ed.",
        "page": "944",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1928 U.S. LEXIS 694",
        "volume": "1928",
        "reporter": "U.S. LEXIS",
        "page": "694",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 A.L.R. 376",
        "volume": "66",
        "reporter": "A.L.R.",
        "page": "376",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "277 U.S. 438",
    "official_selection": {
      "court_class": "scotus",
      "selected": "277 U.S. 438",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-464",
      "page": null,
      "quote": "within the Fourth Amendment. ## Rule *(Historical \u2014 this holding has been overruled; see Treatment.)* The Court tied Fourth Amendment protection to physical trespass and tangible things:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-464b",
      "page": null,
      "quote": "There was no searching. There was no seizure. The evidence was secured by the use of the sense of hearing and that only.",
      "star_marker": "464",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 22716,
      "fragment": "#:~:text=There%20was%20no%20searching.%20There",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1928-06-04",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Olmstead v. United States",
    "varies_by_point": false,
    "scope_note": "Overruled on the privacy point by Katz v. United States (1967); survives only as history. The property-trespass approach was later revived as an alternative test in United States v. Jones (2012).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": "389 U.S. 347",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
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
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrew Lennette, Individually and on behalf of C.L., O.L. and S.L., Minor Children v. State of Iowa, Melody Siver, Amy Howell, and Valerie Lovaglia",
          "cluster_id": 6476611,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
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
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Henderson",
          "cluster_id": 8714803,
          "cite": [
            "857 F. Supp. 2d 191",
            "2012 WL 1432552",
            "2012 U.S. Dist. LEXIS 57729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Rabb",
          "cluster_id": 5640827,
          "cite": [
            "16 N.Y.3d 145",
            "945 N.E.2d 447"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mason v. State",
          "cluster_id": 2167970,
          "cite": [
            "290 S.W.3d 498",
            "2009 WL 1563551"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Scattaretico v. Puglisi",
          "cluster_id": 6587685,
          "cite": [
            "60 Mass. App. Ct. 138",
            "799 N.E.2d 1258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Devereaux v. Abbey",
          "cluster_id": 7099058,
          "cite": [
            "263 F.3d 1070",
            "2001 Daily Journal DAR 9669",
            "2001 Cal. Daily Op. Serv. 7797",
            "2001 U.S. App. LEXIS 19674",
            "2001 WL 1008128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Poritz",
          "cluster_id": 1473573,
          "cite": [
            "662 A.2d 367",
            "142 N.J. 1",
            "36 A.L.R. 5th 711",
            "1995 N.J. LEXIS 519"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 104313,
          "cite": [
            "328 U.S. 582",
            "66 S. Ct. 1256",
            "90 L. Ed. 1453",
            "1946 U.S. LEXIS 2180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Tony C.",
          "cluster_id": 1386533,
          "cite": [
            "582 P.2d 957",
            "21 Cal. 3d 888",
            "148 Cal. Rptr. 366",
            "1978 Cal. LEXIS 269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCambridge v. City of Little Rock",
          "cluster_id": 1495689,
          "cite": [
            "766 S.W.2d 909",
            "298 Ark. 219",
            "16 Media L. Rep. (BNA) 1593",
            "1989 Ark. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Owens",
          "cluster_id": 1227976,
          "cite": [
            "729 P.2d 524",
            "302 Or. 196",
            "1986 Ore. LEXIS 1790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Riser",
          "cluster_id": 1148989,
          "cite": [
            "47 Cal. 2d 566",
            "305 P.2d 1",
            "1956 Cal. LEXIS 302"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. May",
          "cluster_id": 5691156,
          "cite": [
            "81 N.Y.2d 725",
            "609 N.E.2d 113",
            "593 N.Y.S.2d 760",
            "1992 N.Y. LEXIS 4219"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America v. WESTINGHOUSE ELECTRIC CORPORATION, Appellant",
          "cluster_id": 386024,
          "cite": [
            "638 F.2d 570",
            "8 BNA OSHC 2131",
            "8 OSHC (BNA) 2131",
            "1980 U.S. App. LEXIS 12983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashish Patel, Anverali Satani, Nazira Momin, Minaz Chamadia, and Vijay Lakshmi Yogi v. Texas Department of Licensing and Regulation",
          "cluster_id": 2831518,
          "cite": [
            "469 S.W.3d 69",
            "58 Tex. Sup. Ct. J. 1298",
            "2015 Tex. LEXIS 617",
            "2015 WL 3982687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCORMICK v. CARRIER",
          "cluster_id": 830367,
          "cite": [
            "487 Mich. 180",
            "795 N.W.2d 517"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. White",
          "cluster_id": 1194272,
          "cite": [
            "640 P.2d 1061",
            "97 Wash. 2d 92",
            "1982 Wash. LEXIS 1262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(101320 OR 9418652 OR 9418653 OR 9418654 OR 9418655 OR 9418656) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OTc5MjAwMDAwMDAmcz0yMzg2MzMxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28101320+OR+9418652+OR+9418653+OR+9418654+OR+9418655+OR+9418656%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(101320 OR 9418652 OR 9418653 OR 9418654 OR 9418655 OR 9418656)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzgmcz0zNzQ3MTYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28101320+OR+9418652+OR+9418653+OR+9418654+OR+9418655+OR+9418656%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(101320 OR 9418652 OR 9418653 OR 9418654 OR 9418655 OR 9418656)",
        "reviewed": 19,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 19,
        "triage_read": 1,
        "triage_snippet_classified": 18
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(101320 OR 9418652 OR 9418653 OR 9418654 OR 9418655 OR 9418656)",
    "indexed_citing_opinions": 1206,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 101320,
        "count": 1092,
        "count_source": "search"
      },
      {
        "opinion_id": 9418652,
        "count": 157,
        "count_source": "search"
      },
      {
        "opinion_id": 9418653,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9418654,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9418655,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9418656,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2291,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/olmstead-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5MDA1NDImcz03ODYwNjEyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28101320+OR+9418652+OR+9418653+OR+9418654+OR+9418655+OR+9418656%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 101320,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 84810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 87533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 87601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 87628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 87951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 88038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 88341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 88397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 88700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 89027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 89664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 90098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 90320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 91053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 91577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93392,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 95090,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 95218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 95873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 96460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 96812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 97242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 98638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99248,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99914,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100934,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 3543071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 4732864,
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
    "date_created": "2026-07-05T16:11:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Olmstead v. United States

```
<div>
<center><b><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U.S. 438</a></span> (1928)</b></center>
<center><h1>OLMSTEAD ET AL.<br>
v.<br>
UNITED STATES.<br>
GREEN ET AL.<br>
v.<br>
SAME.<br>
McINNIS<br>
v.<br>
SAME.</h1></center>
<center>Nos. 493, 532 and 533.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 20, 21, 1928.</center>
<center>Decided June 4, 1928.</center>
CERTIORARI TO THE CIRCUIT COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*439</span> <i>Mr. John F. Dore,</i> with whom <i>Messrs. F.C. Reagan</i> and <i>J.L. Finch</i> were on the brief, for petitioners in No. 493.</p>
<p><i>Mr. Frank R. Jeffery,</i> for petitioner in No. 533, and some of the petitioners in No. 532.</p>
<p><i>Messrs. Arthur E. Griffin, George F. Vanderveer,</i> and <i>Samuel B. Bassett,</i> on a brief for petitioners in No. 532.</p>
<p><i>Mr. Michael J. Doherty,</i> Special Assistant to the Attorney General, with whom <i>Solicitor General Mitchell</i> was on the brief, for the United States.</p>
<p><i>Messrs. Otto B. Rupp, Charles M. Bracelen, Robert H. Strahan,</i> and <i>Clarence B. Randall</i> on behalf of The Pacific Telephone and Telegraph Company, American Telephone and Telegraph Company, United States Independent Telephone Association, and the Tri-State Telephone and Telegraph Company, as <i>amici curiae,</i> filed a brief by special leave of Court.</p>
<p><span class="star-pagination">*455</span> MR. CHIEF JUSTICE TAFT delivered the opinion of the Court.</p>
<p>These cases are here by certiorari from the Circuit Court of Appeals for the Ninth Circuit. 19 F. (2d) 842 and 850. The petition in No. 493 was filed August 30, 1927; in Nos. 532 and 533, September 9, 1927. They were granted with the distinct limitation that the hearing should be confined to the single question whether the use of evidence of private telephone conversations between the defendants and others, intercepted by means of wire tapping, amounted to a violation of the Fourth and Fifth Amendments.</p>
<p>The petitioners were convicted in the District Court for the Western District of Washington of a conspiracy to violate the National Prohibition Act by unlawfully possessing, transporting and importing intoxicating liquors and maintaining nuisances, and by selling intoxicating liquors. Seventy-two others in addition to the petitioners were indicted. Some were not apprehended, some were acquitted and others pleaded guilty.</p>
<p>The evidence in the records discloses a conspiracy of amazing magnitude to import, possess and sell liquor unlawfully. <span class="star-pagination">*456</span> It involved the employment of not less than fifty persons, of two seagoing vessels for the transportation of liquor to British Columbia, of smaller vessels for coastwise transportation to the State of Washington, the purchase and use of a ranch beyond the suburban limits of Seattle, with a large underground cache for storage and a number of smaller caches in that city, the maintenance of a central office manned with operators, the employment of executives, salesmen, deliverymen, dispatchers, scouts, bookkeepers, collectors and an attorney. In a bad month sales amounted to $176,000; the aggregate for a year must have exceeded two millions of dollars.</p>
<p>Olmstead was the leading conspirator and the general manager of the business. He made a contribution of $10,000 to the capital; eleven others contributed $1,000 each. The profits were divided one-half to Olmstead and the remainder to the other eleven. Of the several offices in Seattle the chief one was in a large office building. In this there were three telephones on three different lines. There were telephones in an office of the manager in his own home, at the homes of his associates, and at other places in the city. Communication was had frequently with Vancouver, British Columbia. Times were fixed for the deliveries of the "stuff," to places along Puget Sound near Seattle and from there the liquor was removed and deposited in the caches already referred to. One of the chief men was always on duty at the main office to receive orders by telephones and to direct their filling by a corps of men stationed in another room  the "bull pen." The call numbers of the telephones were given to those known to be likely customers. At times the sales amounted to 200 cases of liquor per day.</p>
<p>The information which led to the discovery of the conspiracy and its nature and extent was largely obtained by intercepting messages on the telephones of the conspirators by four federal prohibition officers. Small <span class="star-pagination">*457</span> wires were inserted along the ordinary telephone wires from the residences of four of the petitioners and those leading from the chief office. The insertions were made without trespass upon any property of the defendants. They were made in the basement of the large office building. The taps from house lines were made in the streets near the houses.</p>
<p>The gathering of evidence continued for many months. Conversations of the conspirators of which refreshing stenographic notes were currently made, were testified to by the government witnesses. They revealed the large business transactions of the partners and their subordinates. Men at the wires heard the orders given for liquor by customers and the acceptances; they became auditors of the conversations between the partners. All this disclosed the conspiracy charged in the indictment. Many of the intercepted conversations were not merely reports but parts of the criminal acts. The evidence also disclosed the difficulties to which the conspirators were subjected, the reported news of the capture of vessels, the arrest of their men and the seizure of cases of liquor in garages and other places. It showed the dealing by Olmstead, the chief conspirator, with members of the Seattle police, the messages to them which secured the release of arrested members of the conspiracy, and also direct promises to officers of payments as soon as opportunity offered.</p>
<p>The Fourth Amendment provides  "The right of the people to be secure in their persons, houses, papers, and effects against unreasonable searches and seizures shall not be violated; and no warrants shall issue but upon probable cause, supported by oath or affirmation and particularly describing the place to be searched and the persons or things to be seized." And the Fifth: "No person . . . shall be compelled, in any criminal case, to be a witness against himself."</p>
<p><span class="star-pagination">*458</span> It will be helpful to consider the chief cases in this Court which bear upon the construction of these Amendments.</p>
<p><i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>, was an information filed by the District Attorney in the federal court in a cause of seizure and forfeiture against thirty-five cases of plate glass, which charged that the owner and importer, with intent to defraud the revenue, made an entry of the imported merchandise by means of a fraudulent or false invoice. It became important to show the quantity and value of glass contained in twenty-nine cases previously imported. The fifth section of the Act of June 22, 1874, provided that in cases not criminal under the revenue laws, the United States Attorney, whenever he thought an invoice, belonging to the defendant, would tend to prove any allegation made by the United States, might by a written motion describing the invoice and setting forth the allegation which he expected to prove, secure a notice from the court to the defendant to produce the invoice, and if the defendant refused to produce it, the allegations stated in the motion should be taken as confessed, but if produced, the United States Attorney should be permitted, under the direction of the court, to make an examination of the invoice, and might offer the same in evidence. This Act had succeeded the Act of 1867, which provided that in such cases the District Judge, on affidavit of any person interested, might issue a warrant to the marshal to enter the premises where the invoice was and take possession of it and hold it subject to the order of the judge. This had been preceded by the Act of 1863 of a similar tenor, except that it directed the warrant to the collector instead of the marshal. The United States Attorney followed the Act of 1874 and compelled the production of the invoice.</p>
<p>The court held the Act of 1874 repugnant to the Fourth and Fifth Amendments. As to the Fourth Amendment, Justice Bradley said (page 621):</p>
<p><span class="star-pagination">*459</span> "But, in regard to the Fourth Amendment, it is contended that, whatever might have been alleged against the constitutionality of the acts of 1863 and 1867, that of 1874, under which the order in the present case was made, is free from constitutional objection because it does not authorize the search and seizure of books and papers, but only requires the defendant or claimant to produce them. That is so; but it declares that if he does not produce them, the allegations which it is affirmed they will prove shall be taken as confessed. This is tantamount to compelling their production; for the prosecuting attorney will always be sure to state the evidence expected to be derived from them as strongly as the case will admit of. It is true that certain aggravating incidents of actual search and seizure, such as forcible entry into a man's house and searching amongst his papers, are wanting, and to this extent the proceeding under the Act of 1874 is a mitigation of that which was authorized by the former acts; but it accomplishes the substantial object of those acts in forcing from a party evidence against himself. It is our opinion, therefore, that a compulsory production of a man's private papers to establish a criminal charge against him, or to forfeit his property, is within the scope of the Fourth Amendment to the Constitution, in all cases in which a search and seizure would be; because it is a material ingredient, and effects the sole object and purpose of search and seizure."</p>
<p>Concurring, Mr. Justice Miller and Chief Justice Waite said that they did not think the machinery used to get this evidence amounted to a search and seizure, but they agreed that the Fifth Amendment had been violated.</p>
<p>The statute provided an official demand for the production of a paper or document by the defendant for official search and use as evidence on penalty that by refusal he should be conclusively held to admit the incriminating <span class="star-pagination">*460</span> character of the document as charged. It was certainly no straining of the language to construe the search and seizure under the Fourth Amendment to include such official procedure.</p>
<p>The next case, and perhaps the most important, is <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>,  a conviction for using the mails to transmit coupons or tickets in a lottery enterprise. The defendant was arrested by a police officer without a warrant. After his arrest other police officers and the United States marshal went to his house, got the key from a neighbor, entered the defendant's room and searched it, and took possession of various papers and articles. Neither the marshal nor the police officers had a search warrant. The defendant filed a petition in court asking the return of all his property. The court ordered the return of everything not pertinent to the charge, but denied return of relevant evidence. After the jury was sworn, the defendant again made objection, and on introduction of the papers contended that the search without warrant was a violation of the Fourth and Fifth Amendments and they were therefore inadmissible. This court held that such taking of papers by an official of the United States, acting under color of his office, was in violation of the constitutional rights of the defendant, and upon making seasonable application he was entitled to have them restored, and that by permitting their use upon the trial, the trial court erred.</p>
<p>The opinion cited with approval language of Mr. Justice Field in <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727, 733</a></span>, saying that the Fourth Amendment as a principle of protection was applicable to sealed letters and packages in the mail and that, consistently with it, such matter could only be opened and examined upon warrants issued on oath or affirmation particularly describing the thing to be seized.</p>
<p>In <i>Silverthorne Lumber Company</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>, the defendants were arrested at their homes and <span class="star-pagination">*461</span> detained in custody. While so detained, representatives of the Government without authority went to the office of their company and seized all the books, papers and documents found there. An application for return of the things was opposed by the District Attorney, who produced a subpoena for certain documents relating to the charge in the indictment then on file. The court said:</p>
<p>"Thus the case is not that of knowledge acquired through the wrongful act of a stranger, but it must be assumed that the Government planned or at all events ratified the whole performance."</p>
<p>And it held that the illegal character of the original seizure characterized the entire proceeding and under the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case the seized papers must be restored.</p>
<p>In <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>, the defendant was convicted of concealing whiskey on which the tax had not been paid. At the trial he presented a petition asking that private property seized in a search of his house and store "within his curtilage," without warrant should be returned. This was denied. A woman, who claimed to be his wife, was told by the revenue officers that they had come to search the premises for violation of the revenue law. She opened the door; they entered and found whiskey. Further searches in the house disclosed more. It was held that this action constituted a violation of the Fourth Amendment, and that the denial of the motion to restore the whiskey and to exclude the testimony was error.</p>
<p>In <i>Gouled</i> v. <i>The United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>, the facts were these: Gouled and two others were charged with conspiracy to defraud the United States. One pleaded guilty and another was acquitted. Gouled prosecuted error. The matter was presented here on questions propounded by the lower court. The first related to the admission in evidence of a paper surreptitiously taken from the office of the defendant by one acting under the direction <span class="star-pagination">*462</span> of an officer of the Intelligence Department of the Army of the United States. Gouled was suspected of the crime. A private in the U.S. Army, pretending to make a friendly call on him, gained admission to his office and in his absence, without warrant of any character, seized and carried away several documents. One of these belonging to Gouled, was delivered to the United States Attorney and by him introduced in evidence. When produced, it was a surprise to the defendant. He had had no opportunity to make a previous motion to secure a return of it. The paper had no pecuniary value, but was relevant to the issue made on the trial. Admission of the paper was considered a violation of the Fourth Amendment.</p>
<p><i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U.S. 20</a></span>, held that the Fourth and Fifth Amendments were violated by admission in evidence of contraband narcotics found in defendant's house, several blocks distant from the place of arrest, after his arrest, and seized there without a warrant. Under such circumstances the seizure could not be justified as incidental to the arrest.</p>
<p>There is no room in the present case for applying the Fifth Amendment unless the Fourth Amendment was first violated. There was no evidence of compulsion to induce the defendants to talk over their many telephones. They were continually and voluntarily transacting business without knowledge of the interception. Our consideration must be confined to the Fourth Amendment.</p>
<p>The striking outcome of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case and those which followed it was the sweeping declaration that the Fourth Amendment, although not referring to or limiting the use of evidence in courts, really forbade its introduction if obtained by government officers through a violation of the Amendment. Theretofore many had supposed that under the ordinary common law rules, if the tendered evidence was pertinent, the method of obtaining it was <span class="star-pagination">*463</span> unimportant. This was held by the Supreme Judicial Court of Massachusetts in <i>Commonwealth</i> v. <i>Dana,</i> 2 Metcalf, 329, 337. There it was ruled that the only remedy open to a defendant whose rights under a state constitutional equivalent of the Fourth Amendment had been invaded was by suit and judgment for damages, as Lord Camden held in <i>Entick</i> v. <i>Carrington,</i> 19 Howell State Trials, 1029. Mr. Justice Bradley made effective use of this case in <i>Boyd</i> v. <i>United States</i><i>.</i> But in the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, and those which followed, this Court decided with great emphasis, and established as the law for the federal courts, that the protection of the Fourth Amendment would be much impaired unless it was held that not only was the official violator of the rights under the Amendment subject to action at the suit of the injured defendant, but also that the evidence thereby obtained could not be received.</p>
<p>The well known historical purpose of the Fourth Amendment, directed against general warrants and writs of assistance, was to prevent the use of governmental force to search a man's house, his person, his papers and his effects; and to prevent their seizure against his will. This phase of the misuse of governmental power of compulsion is the emphasis of the opinion of the Court in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case. This appears too in the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, in the <i>Silverthorne</i> case and in the <i><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">Amos</a></span></i> case.</p>
<p><i>Gouled</i> v. <i>United States</i> carried the inhibition against unreasonable searches and seizures to the extreme limit. Its authority is not to be enlarged by implication and must be confined to the precise state of facts disclosed by the record. A representative of the Intelligence Department of the Army, having by stealth obtained admission to the defendant's office, seized and carried away certain private papers valuable for evidential purposes. This was held an unreasonable search and seizure within the Fourth Amendment. A stealthy entrance in such circumstances <span class="star-pagination">*464</span> became the equivalent to an entry by force. There was actual entrance into the private quarters of defendant and the taking away of something tangible. Here we have testimony only of voluntary conversations secretly overheard.</p>
<p>The Amendment itself shows that the search is to be of material things  the person, the house, his papers or his effects. The description of the warrant necessary to make the proceeding lawful, is that it must specify the place to be searched and the person or <i>things</i> to be seized.</p>
<p>It is urged that the language of Mr. Justice Field in <i>Ex parte Jackson,</i> already quoted, offers an analogy to the interpretation of the Fourth Amendment in respect of wire tapping. But the analogy fails. The Fourth Amendment may have proper application to a sealed letter in the mail because of the constitutional provision for the Postoffice Department and the relations between the Government and those who pay to secure protection of their sealed letters. See Revised Statutes, §§ 3978 to 3988, whereby Congress monopolizes the carriage of letters and excludes from that business everyone else, and § 3929 which forbids any postmaster or other person to open any letter not addressed to himself. It is plainly within the words of the Amendment to say that the unlawful rifling by a government agent of a sealed letter is a search and seizure of the sender's papers or effects. The letter is a paper, an effect, and in the custody of a Government that forbids carriage except under its protection.</p>
<p>The United States takes no such care of telegraph or telephone messages as of mailed sealed letters. The Amendment does not forbid what was done here. There was no searching. There was no seizure. The evidence was secured by the use of the sense of hearing and that only. There was no entry of the houses or offices of the defendants.</p>
<p><span class="star-pagination">*465</span> By the invention of the telephone, fifty years ago, and its application for the purpose of extending communications, one can talk with another at a far distant place. The language of the Amendment can not be extended and expanded to include telephone wires reaching to the whole world from the defendant's house or office. The intervening wires are not part of his house or office any more than are the highways along which they are stretched.</p>
<p>This Court in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U.S. 132, 149</a></span>, declared:</p>
<p>"The Fourth Amendment is to be construed in the light of what was deemed an unreasonable search and seizure when it was adopted and in a manner which will conserve public interests as well as the interests and rights of individual citizens."</p>
<p>Justice Bradley in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case, and Justice Clark in the <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span></i> case, said that the Fifth Amendment and the Fourth Amendment were to be liberally construed to effect the purpose of the framers of the Constitution in the interest of liberty. But that can not justify enlargement of the language employed beyond the possible practical meaning of houses, persons, papers, and effects, or so to apply the words search and seizure as to forbid hearing or sight.</p>
<p><i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U.S. 57</a></span>, held that the testimony of two officers of the law who trespassed on the defendant's land, concealed themselves one hundred yards away from his house and saw him come out and hand a bottle of whiskey to another, was not inadmissible. While there was a trespass, there was no search of person, house, papers or effects. <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U.S. 559, 563</a></span>; <i>Eversole</i> v. <i>State,</i> 106 Tex. Cr. 567.</p>
<p>Congress may of course protect the secrecy of telephone messages by making them, when intercepted, inadmissible in evidence in federal criminal trials, by direct legislation, <span class="star-pagination">*466</span> and thus depart from the common law of evidence. But the courts may not adopt such a policy by attributing an enlarged and unusual meaning to the Fourth Amendment. The reasonable view is that one who installs in his house a telephone instrument with connecting wires intends to project his voice to those quite outside, and that the wires beyond his house and messages while passing over them are not within the protection of the Fourth Amendment. Here those who intercepted the projected voices were not in the house of either party to the conversation.</p>
<p>Neither the cases we have cited nor any of the many federal decisions brought to our attention hold the Fourth Amendment to have been violated as against a defendant unless there has been an official search and seizure of his person, or such a seizure of his papers or his tangible material effects, or an actual physical invasion of his house "or curtilage" for the purpose of making a seizure.</p>
<p>We think, therefore, that the wire tapping here disclosed did not amount to a search or seizure within the meaning of the Fourth Amendment.</p>
<p>What has been said disposes of the only question that comes within the terms of our order granting certiorari in these cases. But some of our number, departing from that order, have concluded that there is merit in the two-fold objection overruled in both courts below that evidence obtained through intercepting of telephone messages by government agents was inadmissible because the mode of obtaining it was unethical and a misdemeanor under the law of Washington. To avoid any misapprehension of our views of that objection we shall deal with it in both of its phases.</p>
<p>While a Territory, the English common law prevailed in Washington and thus continued after her admission in 1889. The rules of evidence in criminal cases in courts of the United States sitting there, consequently are those of the common law. <i>United States</i> v. <i>Reid,</i> <span class="citation" data-id="86700"><a href="/opinion/86700/united-states-v-reid/" aria-description="Citation for case: United States v. Reid">12 How. 361</a></span>, <span class="star-pagination">*467</span> 363, 366; <i>Logan</i> v. <i>United States,</i> <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/#301" aria-description="Citation for case: Logan v. United States">144 U.S. 263, 301</a></span>; <i>Rosen</i> v. <i>United States,</i> <span class="citation" data-id="9418348"><a href="/opinion/99065/rosen-v-united-states/" aria-description="Citation for case: Rosen v. United States">245 U.S. 467</a></span>; <i>Withaup</i> v. <i>United States,</i> <span class="citation" data-id="8753153"><a href="/opinion/8769634/withaup-v-united-states/#534" aria-description="Citation for case: Withaup v. United States">127 Fed. 530, 534</a></span>; <i>Robinson</i> v. <i>United States,</i> <span class="citation" data-id="8832383"><a href="/opinion/8847089/robinson-v-united-states/#685" aria-description="Citation for case: Robinson v. United States">292 Fed. 683, 685</a></span>.</p>
<p>The common law rule is that the admissibility of evidence is not affected by the illegality of the means by which it was obtained. Professor Greenleaf in his work on evidence, vol. 1, 12th ed., by Redfield, § 254(a) says:</p>
<p>"It may be mentioned in this place, that though papers and other subjects of evidence may have been <i>illegally taken</i> from the possession of the party against whom they are offered, or otherwise unlawfully obtained, this is no valid objection to their admissibility, if they are pertinent to the issue. The court will not take notice how they were obtained, whether lawfully or unlawfully, nor will it form an issue, to determine that question."</p>
<p>Mr. Jones in his work on the same subject refers to Mr. Greenleaf's statement, and says:</p>
<p>"Where there is no violation of a constitutional guaranty, the verity of the above statement is absolute." Vol. 5, § 2075, note 3.</p>
<p>The rule is supported by many English and American cases cited by Jones in vol. 5, § 2075, note 3, and § 2076, note 6; and by Wigmore, vol. 4, § 2183. It is recognized by this Court in <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U.S. 585</a></span>. The <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, announced an exception to the common law rule by excluding all evidence in the procuring of which government officials took part by methods forbidden by the Fourth and Fifth Amendments. Many state courts do not follow the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case. <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N.Y. 13</a></span>. But those who do, treat it as an exception to the general common law rule and required by constitutional limitations. <i>Hughes</i> v. <i>State,</i> <span class="citation" data-id="8302107"><a href="/opinion/8334068/hughes-v-state/#551" aria-description="Citation for case: Hughes v. State">145 Tenn. 544, 551, 566</a></span>; <i>State</i> v. <i>Wills,</i> <span class="citation" data-id="8179537"><a href="/opinion/8216688/state-v-wills/#677" aria-description="Citation for case: State v. Wills">91 W. Va. 659, 677</a></span>; <i>State</i> v. <i>Slamon,</i> <span class="citation" data-id="6585198"><a href="/opinion/6705054/state-v-slamon/#214" aria-description="Citation for case: State v. Slamon">73 Vt. 212, 214, 215</a></span>; <i>Gindrat</i> v. <i>People,</i> <span class="citation" data-id="6964776"><a href="/opinion/7060795/gindrat-v-people/#111" aria-description="Citation for case: Gindrat v. People">138 Ill. 103, 111</a></span>; <i>People</i> v. <i>Castree,</i> <span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/#396" aria-description="Citation for case: People v. Castree">311 Ill. 392, 396, 397</a></span>; <i>State</i> v. <span class="star-pagination">*468</span> <i>Gardner,</i> <span class="citation" data-id="3543071"><a href="/opinion/3564065/state-v-gardner/#21" aria-description="Citation for case: State v. Gardner">77 Mont. 8, 21</a></span>; <i>State</i> v. <i>Fahn,</i> 53 N. Dak. 203, 210. The common law rule must apply in the case at bar.</p>
<p>Nor can we, without the sanction of congressional enactment, subscribe to the suggestion that the courts have a discretion to exclude evidence, the admission of which is not unconstitutional, because unethically secured. This would be at variance with the common law doctrine generally supported by authority. There is no case that sustains, nor any recognized text book that gives color to such a view. Our general experience shows that much evidence has always been receivable although not obtained by conformity to the highest ethics. The history of criminal trials shows numerous cases of prosecutions of oath-bound conspiracies for murder, robbery, and other crimes, where officers of the law have disguised themselves and joined the organizations, taken the oaths and given themselves every appearance of active members engaged in the promotion of crime, for the purpose of securing evidence. Evidence secured by such means has always been received.</p>
<p>A standard which would forbid the reception of evidence if obtained by other than nice ethical conduct by government officials would make society suffer and give criminals greater immunity than has been known heretofore. In the absence of controlling legislation by Congress, those who realize the difficulties in bringing offenders to justice may well deem it wise that the exclusion of evidence should be confined to cases where rights under the Constitution would be violated by admitting it.</p>
<p>The statute of Washington, adopted in 1909, provides (Remington Compiled Statutes, 1922, § 2656-18) that:</p>
<p>"Every person . . . who shall intercept, read or in any manner interrupt or delay the sending of a message over any telegraph or telephone line . . . shall be guilty of a misdemeanor."</p>
<p><span class="star-pagination">*469</span> This statute does not declare that evidence obtained by such interception shall be inadmissible, and by the common law, already referred to, it would not be. <i>People</i> v. <i>McDonald,</i> 177 App. Div. (N.Y.) 806. Whether the State of Washington may prosecute and punish federal officers violating this law and those whose messages were intercepted may sue them civilly is not before us. But clearly a statute, passed twenty years after the admission of the State into the Union can not affect the rules of evidence applicable in courts of the United States in criminal cases. Chief Justice Taney, in <i>United States</i> v. <i>Reid,</i> <span class="citation" data-id="86700"><a href="/opinion/86700/united-states-v-reid/#363" aria-description="Citation for case: United States v. Reid">12 How. 361, 363</a></span>, construing the 34th section of the Judiciary Act, said:</p>
<p>"But it could not be supposed, without very plain words to show it, that Congress intended to give the states the power of prescribing the rules of evidence in trials for offenses against the United States. For this construction would place the criminal jurisprudence of one sovereignty under the control of another." See also <i>Withaup</i> v. <i>United States,</i> <span class="citation" data-id="8753153"><a href="/opinion/8769634/withaup-v-united-states/#534" aria-description="Citation for case: Withaup v. United States">127 Fed. 530, 534</a></span>.</p>
<p>The judgments of the Circuit Court of Appeals are affirmed. The mandates will go down forthwith under Rule 31.</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE HOLMES:</p>
<p>My brother BRANDEIS has given this case so exhaustive an examination that I desire to add but a few words. While I do not deny it, I am not prepared to say that the penumbra of the Fourth and Fifth Amendments covers the defendant, although I fully agree that Courts are apt to err by sticking too closely to the words of a law where those words import a policy that goes beyond them. <i>Gooch</i> v. <i>Oregon Short Line R.R. Co.,</i> <span class="citation" data-id="99914"><a href="/opinion/99914/gooch-v-oregon-short-line-railroad/#24" aria-description="Citation for case: Gooch v. Oregon Short Line Railroad">258 U.S. 22, 24</a></span>. But I think, as MR. JUSTICE BRANDEIS says, that apart from the Constitution the Government ought not to use <span class="star-pagination">*470</span> evidence obtained and only obtainable by a criminal act. There is no body of precedents by which we are bound, and which confines us to logical deduction from established rules. Therefore we must consider the two objects of desire, both of which we cannot have, and make up our minds which to choose. It is desirable that criminals should be detected, and to that end that all available evidence should be used. It also is desirable that the Government should not itself foster and pay for other crimes, when they are the means by which the evidence is to be obtained. If it pays its officers for having got evidence by crime I do not see why it may not as well pay them for getting it in the same way, and I can attach no importance to protestations of disapproval if it knowingly accepts and pays and announces that in the future it will pay for the fruits. We have to chose, and for my part I think it a less evil that some criminals should escape than that the Government should play an ignoble part.</p>
<p>For those who agree with me, no distinction can be taken between the Government as prosecutor and the Government as judge. If the existing code does not permit district attorneys to have a hand in such dirty business it does not permit the judge to allow such iniquities to succeed. See <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>. And if all that I have said so far be accepted it makes no difference that in this case wire tapping is made a crime by the law of the State, not by the law of the United States. It is true that a State cannot make rules of evidence for Courts of the United States, but the State has authority over the conduct in question, and I hardly think that the United States would appear to greater advantage when paying for an odious crime against State law than when inciting to the disregard of its own. I am aware of the often repeated statement that in a criminal proceeding the Court will not take notice of the manner in which papers offered in evidence have been <span class="star-pagination">*471</span> obtained. But that somewhat rudimentary mode of disposing of the question has been overthrown by <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span> and the cases that have followed it. I have said that we are free to choose between two principles of policy. But if we are to confine ourselves to precedent and logic the reason for excluding evidence obtained by violating the Constitution seems to me logically to lead to excluding evidence obtained by a crime of the officers of the law.</p>
<p>MR. JUSTICE BRANDEIS, dissenting.</p>
<p>The defendants were convicted of conspiring to violate the National Prohibition Act. Before any of the persons now charged had been arrested or indicted, the telephones by means of which they habitually communicated with one another and with others had been tapped by federal officers. To this end, a lineman of long experience in wire-tapping was employed, on behalf of the Government and at its expense. He tapped eight telephones, some in the homes of the persons charged, some in their offices. Acting on behalf of the Government and in their official capacity, at least six other prohibition agents listened over the tapped wires and reported the messages taken. Their operations extended over a period of nearly five months. The type-written record of the notes of conversations overheard occupies 775 typewritten pages. By objections seasonably made and persistently renewed, the defendants objected to the admission of the evidence obtained by wire-tapping, on the ground that the Government's wire-tapping constituted an unreasonable search and seizure, in violation of the Fourth Amendment; and that the use as evidence of the conversations overheard compelled the defendants to be witnesses against themselves, in violation of the Fifth Amendment.</p>
<p>The Government makes no attempt to defend the methods employed by its officers. Indeed, it concedes <span class="star-pagination">*472</span> that if wire-tapping can be deemed a search and seizure within the Fourth Amendment, such wire-tapping as was practiced in the case at bar was an unreasonable search and seizure, and that the evidence thus obtained was inadmissible. But it relies on the language of the Amendment; and it claims that the protection given thereby cannot properly be held to include a telephone conversation.</p>
<p>"We must never forget," said Mr. Chief Justice Marshall in <i>McCulloch</i> v. <i>Maryland,</i> <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/#407" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316, 407</a></span>, "that it is a constitution we are expounding." Since then, this Court has repeatedly sustained the exercise of power by Congress, under various clauses of that instrument, over objects of which the Fathers could not have dreamed. See <i>Pensacola Telegraph Co.</i> v. <i>Western Union Telegraph Co.,</i> <span class="citation" data-id="9417106"><a href="/opinion/89664/pensacola-telegraph-co-v-western-union-telegraph-co/#9" aria-description="Citation for case: Pensacola Telegraph Co. v. Western Union Telegraph Co.">96 U.S. 1, 9</a></span>; <i>Northern Pacific Ry. Co.</i> v. <i>North Dakota,</i> <span class="citation" data-id="99406"><a href="/opinion/99406/northern-pacific-railway-co-v-north-dakota-ex-rel-langer/" aria-description="Citation for case: Northern Pacific Railway Co. v. North Dakota Ex Rel. Langer">250 U.S. 135</a></span>; <i>Dakota Central Telephone Co.</i> v. <i>South Dakota,</i> <span class="citation" data-id="99408"><a href="/opinion/99408/dakota-central-telephone-co-v-south-dakota-ex-rel-payne/" aria-description="Citation for case: Dakota Central Telephone Co. v. South Dakota Ex Rel. Payne">250 U.S. 163</a></span>; <i>Brooks</i> v. <i>United States,</i> <span class="citation" data-id="100610"><a href="/opinion/100610/brooks-v-united-states/" aria-description="Citation for case: Brooks v. United States">267 U.S. 432</a></span>. We have likewise held that general limitations on the powers of Government, like those embodied in the due process clauses of the Fifth and Fourteenth Amendments, do not forbid the United States or the States from meeting modern conditions by regulations which "a century ago, or even half a century ago, probably would have been rejected as arbitrary and oppressive." <i>Village of Euclid</i> v. <i>Ambler Realty Co.,</i> <span class="citation" data-id="100934"><a href="/opinion/100934/village-of-euclid-v-ambler-realty-co/#387" aria-description="Citation for case: Village of Euclid v. Ambler Realty Co.">272 U.S. 365, 387</a></span>; <i>Buck</i> v. <i>Bell,</i> <span class="citation" data-id="101076"><a href="/opinion/101076/buck-v-bell/" aria-description="Citation for case: Buck v. Bell">274 U.S. 200</a></span>. Clauses guaranteeing to the individual protection against specific abuses of power, must have a similar capacity of adaptation to a changing world. It was with reference to such a clause that this Court said in <i>Weems</i> v. <i>United States,</i> <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/" aria-description="Citation for case: Weems v. United States">217 U.S. 349</a></span>, 373: "Legislation, both statutory and constitutional, is enacted, it is true, from an experience of evils, but its general language should not, therefore, be necessarily confined to the form that evil had theretofore taken. Time works changes, brings into existence new conditions <span class="star-pagination">*473</span> and purposes. Therefore a principle to be vital must be capable of wider application than the mischief which gave it birth. This is peculiarly true of constitutions. They are not ephemeral enactments, designed to meet passing occasions. They are, to use the words of Chief Justice Marshall `designed to approach immortality as nearly as human institutions can approach it.' The future is their care and provision for events of good and bad tendencies of which no prophecy can be made. In the application of a constitution, therefore, our contemplation cannot be only of what has been but of what may be. Under any other rule a constitution would indeed be as easy of application as it would be deficient in efficacy and power. Its general principles would have little value and be converted by precedent into impotent and lifeless formulas. Rights declared in words might be lost in reality."</p>
<p>When the Fourth and Fifth Amendments were adopted, "the form that evil had theretofore taken," had been necessarily simple. Force and violence were then the only means known to man by which a Government could directly effect self-incrimination. It could compel the individual to testify  a compulsion effected, if need be, by torture. It could secure possession of his papers and other articles incident to his private life  a seizure effected, if need be, by breaking and entry. Protection against such invasion of "the sanctities of a man's home and the privacies of life" was provided in the Fourth and Fifth Amendments by specific language. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U.S. 616, 630</a></span>. But "time works changes, brings into existence new conditions and purposes." Subtler and more far-reaching means of invading privacy have become available to the Government. Discovery and invention have made it possible for the Government, by means far more effective than stretching upon the rack, to obtain disclosure in court of what is whispered in the closet.</p>
<p><span class="star-pagination">*474</span> Moreover, "in the application of a constitution, our contemplation cannot be only of what has been but of what may be." The progress of science in furnishing the Government with means of espionage is not likely to stop with wire-tapping. Ways may some day be developed by which the Government, without removing papers from secret drawers, can reproduce them in court, and by which it will be enabled to expose to a jury the most intimate occurrences of the home. Advances in the psychic and related sciences may bring means of exploring unexpressed beliefs, thoughts and emotions. "That places the liberty of every man in the hands of every petty officer" was said by James Otis of much lesser intrusions than these.<sup>[1]</sup> To Lord Camden, a far slighter intrusions seemed "subversive of all the comforts of society."<sup>[2]</sup> Can it be that the Constitution affords no protection against such invasions of individual security?</p>
<p>A sufficient answer is found in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#627" aria-description="Citation for case: Boyd v. United States">116 U.S. 616, 627-630</a></span>, a case that will be remembered as long as civil liberty lives in the United States. This Court there reviewed the history that lay behind the Fourth and Fifth Amendments. We said with reference to Lord Camden's judgment in <i>Entick</i> v. <i>Carrington,</i> 19 Howell's State Trials, 1030: "The principles laid down in this opinion affect the very essence of constitutional liberty and security. They reach farther than the concrete form of the case there before the court, with its adventitious circumstances; they apply to all invasions on the part of the Government and its employes of the sanctities of a man's home and the privacies of life. It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security, <span class="star-pagination">*475</span> personal liberty and private property, where that right has never been forfeited by his conviction of some public offence,  it is the invasion of this sacred right which underlies and constitutes the essence of Lord Camden's judgment. Breaking into a house and opening boxes and drawers are circumstances of aggravation; but any forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence of a crime or to forfeit his goods, is within the condemnation of that judgment. In this regard the Fourth and Fifth Amendments run almost into each other."<sup>[3]</sup></p>
<p>In <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727</a></span>, it was held that a sealed letter entrusted to the mail is protected by the Amendments. The mail is a public service furnished by the Government. The telephone is a public service furnished by its authority. There is, in essence, no difference between the sealed letter and the private telephone message. As Judge Rudkin said below: "True the one is visible, the other invisible; the one is tangible, the other intangible; the one is sealed and the other unsealed, but these are distinctions without a difference." The evil incident to invasion of the privacy of the telephone is far greater than that involved in tampering with the mails. Whenever a telephone line is tapped, the privacy of the persons at both ends of the line is invaded and all conversations <span class="star-pagination">*476</span> between them upon any subject, and although proper, confidential and privileged, may be overheard. Moreover, the tapping of one man's telephone line involves the tapping of the telephone of every other person whom he may call or who may call him. As a means of espionage, writs of assistance and general warrants are but puny instruments of tyranny and oppression when compared with wire-tapping.</p>
<p>Time and again, this Court in giving effect to the principle underlying the Fourth Amendment, has refused to place an unduly literal construction upon it. This was notably illustrated in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case itself. Taking language in its ordinary meaning, there is no "search" or "seizure" when a defendant is required to produce a document in the orderly process of a court's procedure. "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures," would not be violated, under any ordinary construction of language, by compelling obedience to a subpoena. But this Court holds the evidence inadmissible simply because the information leading to the issue of the subpoena has been unlawfully secured. <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>. Literally, there is no "search" or "seizure" when a friendly visitor abstracts papers from an office; yet we held in <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>, that evidence so obtained could not be used. No court which looked at the words of the Amendment rather than at its underlying purpose would hold, as this Court did in <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727, 733</a></span>, that its protection extended to letters in the mails. The provision against self-incrimination in the Fifth Amendment has been given an equally broad construction. The language is: "No person. . . shall be compelled in any criminal case to be a witness against himself." Yet we have held, not only that the <span class="star-pagination">*477</span> protection of the Amendment extends to a witness before a grand jury, although he has not been charged with crime, <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U.S. 547, 562, 586</a></span>. but that: "It applies alike to civil and criminal proceedings, wherever the answer might tend to subject to criminal responsibility him who gives it. The privilege protects a mere witness as fully as it does one who is also a party defendant." <i>McCarthy</i> v. <i>Arndstein,</i> <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U.S. 34, 40</a></span>. The narrow language of the Amendment has been consistently construed in the light of its object, "to insure that a person should not be compelled, when acting as a witness in any investigation, to give testimony which might tend to show that he himself had committed a crime. The privilege is limited to criminal matters, but it is as broad as the mischief against which it seeks to guard." <i>Counselman</i> v. <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock"><i>Hitchcock, supra,</i> p. 562</a></span>.</p>
<p>Decisions of this Court applying the principle of the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case have settled these things. Unjustified search and seizure violates the Fourth Amendment, whatever the character of the paper;<sup>[4]</sup> whether the paper when taken by the federal officers was in the home,<sup>[5]</sup> in an office<sup>[6]</sup> or elsewhere;<sup>[7]</sup> whether the taking was effected by force,<sup>[8]</sup> by <span class="star-pagination">*478</span> fraud,<sup>[9]</sup> or in the orderly process of a court's procedure.<sup>[10]</sup> From these decisions, it follows necessarily that the Amendment is violated by the officer's reading the paper without a physical seizure, without his even touching it; and that use, in any criminal proceeding, of the contents of the paper so examined  as where they are testified to by a federal officer who thus saw the document or where, through knowledge so obtained, a copy has been procured elsewhere<sup>[11]</sup>  any such use constitutes a violation of the Fifth Amendment.</p>
<p>The protection guaranteed by the Amendments is much broader in scope. The makers of our Constitution undertook to secure conditions favorable to the pursuit of happiness. They recognized the significance of man's spiritual nature, of his feelings and of his intellect. They knew that only a part of the pain, pleasure and satisfactions of life are to be found in material things. They sought to protect Americans in their beliefs, their thoughts, their emotions and their sensations. They conferred, as against the Government, the right to be let alone  the most comprehensive of rights and the right most valued by civilized men. To protect that right, every unjustifiable intrusion by the Government upon the privacy of the individual, whatever the means employed, must be deemed a violation of the Fourth Amendment. And the use, as evidence <span class="star-pagination">*479</span> in a criminal proceeding, of facts ascertained by such intrusion must be deemed a violation of the Fifth.</p>
<p>Applying to the Fourth and Fifth Amendments the established rule of construction, the defendants' objections to the evidence obtained by wire-tapping must, in my opinion, be sustained. It is, of course, immaterial where the physical connection with the telephone wires leading into the defendants' premises was made. And it is also immaterial that the intrusion was in aid of law enforcement. Experience should teach us to be most on our guard to protect liberty when the Government's purposes are beneficent. Men born to freedom are naturally alert to repel invasion of their liberty by evil-minded rulers. The greatest dangers to liberty lurk in insidious encroachment by men of zeal, well-meaning but without understanding.<sup>[12]</sup></p>
<p>Independently of the constitutional question, I am of opinion that the judgment should be reversed. By the laws of Washington, wire-tapping is a crime.<sup>[13]</sup> Pierce's <span class="star-pagination">*480</span> Code, 1921, § 8976(18). To prove its case, the Government was obliged to lay bare the crimes committed by its officers on its behalf. A federal court should not permit such a prosecution to continue. Compare <i>Harkin</i> v. <i>Brundage,</i> <span class="citation" data-id="101214"><a href="/opinion/101214/harkin-v-brundage/" aria-description="Citation for case: Harkin v. Brundage">276 U.S. 36</a></span>, <i>id.</i> 604.</p>
<p><span class="star-pagination">*481</span> The situation in the case at bar differs widely from that presented in <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U.S. 465</a></span>. There, only a single lot of papers was involved. They had been obtained by a private detective while acting on behalf of a private party; without the knowledge of any federal official; long before anyone had thought of instituting a <span class="star-pagination">*482</span> federal prosecution. Here, the evidence obtained by crime was obtained at the Government's expense, by its officers, while acting on its behalf; the officers who committed these crimes are the same officers who were charged with the enforcement of the Prohibition Act; the crimes of these officers were committed for the purpose of securing evidence with which to obtain an indictment and to secure a conviction. The evidence so obtained constitutes the warp and woof of the Government's case. The aggregate of the Government evidence occupies 306 pages of the printed record. More than 210 of them are filled by recitals of the details of the wire-tapping and of facts ascertained thereby.<sup>[14]</sup> There is literally no other evidence of guilt on the part of some of the defendants except that illegally obtained by these officers. As to nearly all the defendants (except those who admitted guilt), the evidence relied upon to secure a conviction consisted mainly of that which these officers had so obtained by violating the state law.</p>
<p>As Judge Rudkin said below: "Here we are concerned with neither eavesdroppers nor thieves. Nor are we concerned with the acts of private individuals. . . . We are concerned only with the acts of federal agents whose powers are limited and controlled by the Constitution of the United States." The Eighteenth Amendment has not in terms empowered Congress to authorize anyone to violate the criminal laws of a State. And Congress has never purported to do so. Compare <i>Maryland</i> v. <i>Soper,</i> <span class="citation" data-id="100776"><a href="/opinion/100776/maryland-v-soper-judge/" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 9</a></span>. The terms of appointment of federal prohibition agents do not purport to confer upon them authority to violate any criminal law. Their superior officer, the Secretary of the Treasury, has not instructed them to commit <span class="star-pagination">*483</span> crime on behalf of the United States. It may be assumed that the Attorney General of the United States did not give any such instruction.<sup>[15]</sup></p>
<p>When these unlawful acts were committed, they were crimes only of the officers individually. The Government was innocent, in legal contemplation; for no federal official is authorized to commit a crime on its behalf. When the Government, having full knowledge, sought, through the Department of Justice, to avail itself of the fruits of these acts in order to accomplish its own ends, it assumed moral responsibility for the officers' crimes. Compare <i>The Paquete Habana,</i> <span class="citation" data-id="95873"><a href="/opinion/95873/the-paquete-habana/#465" aria-description="Citation for case: The Paquete Habana">189 U.S. 453, 465</a></span>; <i>O'Reilly deCamara</i> v. <i>Brooke,</i> <span class="citation" data-id="96812"><a href="/opinion/96812/oreilly-de-camara-v-brooke/#52" aria-description="Citation for case: O&#x27;Reilly De Camara v. Brooke">209 U.S. 45, 52</a></span>; <i>Dodge</i> v. <i>United States,</i> <span class="citation" data-id="100949"><a href="/opinion/100949/dodge-v-united-states/#532" aria-description="Citation for case: Dodge v. United States">272 U.S. 530, 532</a></span>; <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U.S. 310</a></span>. And if this Court should permit the Government, by means of its officers' crimes, to effect its purpose of punishing the defendants, there would seem to be present all the elements of a ratification. If so, the Government itself would become a lawbreaker.</p>
<p>Will this Court by sustaining the judgment below sanction such conduct on the part of the Executive? The governing principle has long been settled. It is that a court will not redress a wrong when he who invokes its aid has unclean hands.<sup>[16]</sup> The maxim of unclean hands comes <span class="star-pagination">*484</span> from courts of equity.<sup>[17]</sup> But the principle prevails also in courts of law. Its common application is in civil actions between private parties. Where the Government is the actor, the reasons for applying it are even more persuasive. Where the remedies invoked are those of the criminal law, the reasons are compelling.<sup>[18]</sup></p>
<p>The door of a court is not barred because the plaintiff has committed a crime. The confirmed criminal is as much entitled to redress as his most virtuous fellow citizen; no record of crime, however long, makes one an outlaw. The court's aid is denied only when he who seeks it has violated the law in connection with the very transaction as to which he seeks legal redress.<sup>[19]</sup> Then aid is denied despite the defendant's wrong. It is denied in order to maintain respect for law; in order is to promote confidence in the administration of justice; in order to preserve the judicial process from contamination. The rule is one, not of action, but of inaction. It is sometimes <span class="star-pagination">*485</span> spoken of as a rule of substantive law. But it extends to matters of procedure as well.<sup>[20]</sup> A defense may be waived. It is waived when not pleaded. But the objection that the plaintiff comes with unclean hands will be taken by the court itself.<sup>[21]</sup> It will be taken despite the wish to the contrary of all the parties to the litigation. The court protects itself.</p>
<p>Decency, security and liberty alike demand that government officials shall be subjected to the same rules of conduct that are commands to the citizen. In a government of laws, existence of the government will be imperilled if it fails to observe the law scrupulously. Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example. Crime is contagious. If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy. To declare that in the administration of the criminal law the end justifies the means  to declare that the Government may commit crimes in order to secure the conviction of a private criminal  would bring terrible retribution. Against that pernicious doctrine this Court should resolutely set its face.</p>
<p>MR. JUSTICE BUTLER, dissenting.</p>
<p>I sincerely regret that I cannot support the opinion and judgments of the Court in these cases.</p>
<p><span class="star-pagination">*486</span> The order allowing the writs of certiorari operated to limit arguments of counsel to the constitutional question. I do not participate in the controversy that has arisen here as to whether the evidence was inadmissible because the mode of obtaining it was unethical and a misdemeanor under state law. I prefer to say nothing concerning those questions because they are not within the jurisdiction taken by the order.</p>
<p>The Court is required to construe the provision of the Fourth Amendment that declares: "The right of the people to be secure in their persons, houses, papers and effects, against unreasonable searches and seizures, shall not be violated." The Fifth Amendment prevents the use of evidence obtained through searches and seizures in violation of the rights of the accused protected by the Fourth Amendment.</p>
<p>The single question for consideration is this: May the Government, consistently with that clause, have its officers whenever they see fit, tap wires, listen to, take down and report, the private messages and conversations transmitted by telephones?</p>
<p>The United States maintains that "The `wire tapping' operations of the federal prohibition agents were not a `search and seizure' in violation of the security of the `persons, houses, papers and effects' of the petitioners in the constitutional sense or within the intendment of the Fourth Amendment." The Court, adhering to and reiterating the principles laid down and applied in prior decisions<sup>[*]</sup> construing the search and seizure clause, in substance adopts the contention of the Government.</p>
<p>The question at issue depends upon a just appreciation of the facts.</p>
<p><span class="star-pagination">*487</span> Telephones are used generally for transmission of messages concerning official, social, business and personal affairs including communications that are private and privileged  those between physician and patient, lawyer and client, parent and child, husband and wife. The contracts between telephone companies and users contemplate the private use of the facilities employed in the service. The communications belong to the parties between whom they pass. During their transmission the exclusive use of the wire belongs to the persons served by it. Wire tapping involves interference with the wire while being used. Tapping the wires and listening in by the officers literally constituted a search for evidence. As the communications passed, they were heard and taken down.</p>
<p>In <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>, there was no "search or seizure" within the literal or ordinary meaning of the words, nor was Boyd  if these constitutional provisions were read strictly according to the letter  compelled in a "criminal case" to be a "witness" against himself. The statute, there held unconstitutional because repugnant to the search and seizure clause, merely authorized judgment for sums claimed by the Government on account of revenue if the defendant failed to produce his books, invoices and papers. The principle of that case has been followed, developed and applied in this and many other courts. And it is in harmony with the rule of liberal construction that always has been applied to provisions of the Constitution safeguarding personal rights (<i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#32" aria-description="Citation for case: Byars v. United States">273 U.S. 28, 32</a></span>), as well as to those granting governmental powers. <i>McCulloch</i> v. <i>Maryland,</i> <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/#404" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316, 404, 406, 407, 421</a></span>. <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/#153" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137, 153, 176</a></span>. <i>Cohens</i> v. <i>Virginia,</i> <span class="citation" data-id="85330"><a href="/opinion/85330/cohens-v-virginia/" aria-description="Citation for case: Cohens v. Virginia">6 Wheat. 264</a></span>. <i>Myers</i> v. <i>United States,</i> <span class="citation" data-id="9418565"><a href="/opinion/100926/myers-v-united-states/" aria-description="Citation for case: Myers v. United States">272 U.S. 52</a></span>.</p>
<p>This Court has always construed the Constitution in the light of the principles upon which it was founded. <span class="star-pagination">*488</span> The direct operation or literal meaning of the words used do not measure the purpose or scope of its provisions. Under the principles established and applied by this Court, the Fourth Amendment safeguards against all evils that are like and equivalent to those embraced within the ordinary meaning of its words. That construction is consonant with sound reason and in full accord with the course of decisions since <i>McCulloch</i> v. <i>Maryland</i><i>.</i> That is the principle directly applied in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case.</p>
<p>When the facts in these cases are truly estimated, a fair application of that principle decides the constitutional question in favor of the petitioners. With great deference, I think they should be given a new trial.</p>
<p>MR. JUSTICE STONE, dissenting.</p>
<p>I concur in the opinions of MR. JUSTICE HOLMES and MR. JUSTICE BRANDEIS. I agree also with that of MR. JUSTICE BUTLER so far as it deals with the merits. The effect of the order granting certiorari was to limit the argument to a single question, but I do not understand that it restrains the Court from a consideration of any question which we find to be presented by the record, for, under Jud. Code, § 240(a), this Court determines a case here on certiorari "with the same power and authority, and with like effect, as if the cause had been brought [here] by unrestricted writ of error or appeal."</p>
<h2>NOTES</h2>
<p>[1]  Otis' Argument against Writs of Assistance. See Tudor, James Otis, p. 66; John Adams, Works, Vol. II, p. 524; Minot, Continuation of the History of Massachusetts Bay, Vol. II, p. 95.</p>
<p>[2]  <i>Entick</i> v. <i>Carrington,</i> 19 Howell's State Trials, 1030, 1066.</p>
<p>[3]  In <i>Interstate Commerce Commission</i> v. <i>Brimson,</i> <span class="citation" data-id="93951"><a href="/opinion/93951/interstate-commerce-commission-v-brimson/#479" aria-description="Citation for case: Interstate Commerce Commission v. Brimson">154 U.S. 447, 479</a></span>, the statement made in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case was repeated; and the Court quoted the statement of Mr. Justice Field in <i>In re Pacific Railway Commission,</i> <span class="citation" data-id="8310981"><a href="/opinion/8342559/in-re-pacific-railway-commission/" aria-description="Citation for case: In re Pacific Railway Commission">32 Fed. 241</a></span>, 250: "Of all the rights of the citizen, few are of greater importance or more essential to his peace and happiness than the right of personal security, and that involves, not merely protection of his person from assault, but exemption of his private affairs, books, and papers, from the inspection and scrutiny of others. Without the enjoyment of this right, all others would lose half their value." The <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case has been recently reaffirmed in <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>, in <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>, and in <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>.</p>
<p>[4]  <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>.</p>
<p>[5]  <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>; <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>; <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U.S. 20</a></span>; <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>.</p>
<p>[6]  <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>; <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#70" aria-description="Citation for case: Hale v. Henkel">201 U.S. 43, 70</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>; <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U.S. 192</a></span>.</p>
<p>[7]  <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727, 733</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U.S. 132, 156</a></span>; <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U.S. 310</a></span>.</p>
<p>[8]  <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>; <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U.S. 132, 156</a></span>; <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U.S. 20</a></span>; <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U.S. 310</a></span>.</p>
<p>[9]  <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>.</p>
<p>[10]  <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>; <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#70" aria-description="Citation for case: Hale v. Henkel">201 U.S. 43, 70</a></span>. See <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>; <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U.S. 192</a></span>.</p>
<p>[11]  <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>. Compare <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#307" aria-description="Citation for case: Gouled v. United States">255 U.S. 298, 307</a></span>. In <i>Stroud</i> v. <i>United States,</i> <span class="citation" data-id="99464"><a href="/opinion/99464/stroud-v-united-states/" aria-description="Citation for case: Stroud v. United States">251 U.S. 15</a></span>, and <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U.S. 57</a></span>, the letter and articles admitted were not obtained by unlawful search and seizure. They were voluntary dilosures by the defendant. Compare <i>Smith</i> v. <i>United States,</i> 2 F. (2d) 715; <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/" aria-description="Citation for case: United States v. Lee">274 U.S. 559</a></span>.</p>
<p>[12]  The point is thus stated by counsel for the telephone companies, who have filed a brief as <i>amici curiae:</i> "Criminals will not escape detection and conviction merely because evidence obtained by tapping wires of a public telephone system is inadmissible, if it should be so held; but, in any event, it is better that a few criminals escape than that the privacies of life of all the people be exposed to the agents of the government, who will act at their own discretion, the honest and the dishonest, unauthorized and unrestrained by the courts. Legislation making wire tapping a crime will not suffice if the courts nevertheless hold the evidence to be lawful."</p>
<p>[13]  In the following states it is a criminal offense to intercept a message sent by telegraph and/or telephone: Alabama, Code, 1923, § 5256; Arizona, Revised Statutes, 1913, Penal Code, § 692; Arkansas, Crawford &amp; Moses Digest, 1921, § 10246; California, Deering's Penal Code, 1927, § 640; Colorado, Compiled Laws, 1921, § 6969; Connecticut, General Statutes, 1918, § 6292; Idaho, Compiled Statutes, 1919, §§ 8574, 8586; Illinois, Revised Statutes, 1927, c. 134, § 21; Iowa, Code, 1927, § 13121; Kansas, Revised Statutes, 1923, c. 17, § 1908; Michigan, Compiled Laws, 1915, § 15403; Montana, Penal Code, 1921, § 11518; Nebraska, Compiled Statutes, 1922, § 7115; Nevada, Revised Laws, 1912, §§ 4608, 6572(18); New York, Consolidated Laws, c. 40, § 1423(6); North Dakota, Compiled Laws, 1913, § 10231; Ohio, Page's General Code, 1926, § 13402; Oklahoma, Session Laws, 1923, c. 46; Oregon, Olson's Laws, 1920, § 2265; South Dakota, Revised Code, 1919, § 4312; Tennessee, Shannon's Code, 1919, §§ 1839, 1840; Utah, Compiled Laws, 1917, § 8433; Virginia, Code, 1924, § 4477(2), (3); Washington, Pierce's Code, 1921, § 8976(18); Wisconsin, Statutes, 1927, § 348.37; Wyoming, Compiled Statutes, 1920, § 7148. Compare <i>State</i> v. <i>Behringer,</i> <span class="citation" data-id="6474480"><a href="/opinion/6599138/state-v-behringer/" aria-description="Citation for case: State v. Behringer">19 Ariz. 502</a></span>; <i>State</i> v. <i>Nordskog,</i> <span class="citation" data-id="4732864"><a href="/opinion/4925570/state-v-nordskog/" aria-description="Citation for case: State v. Nordskog">76 Wash. 472</a></span>.
</p>
<p>In the following states it is a criminal offense for a company engaged in the transmission of messages by telegraph and/or telephone, or its employees, or, in many instances, persons conniving with them, to disclose or to assist in the disclosure of any message: Alabama, Code, 1923, §§ 5543, 5545; Arizona, Revised Statutes, 1913, Penal Code, §§ 621, 623, 691; Arkansas, Crawford &amp; Moses Digest, 1921, § 10250; California, Deering's Penal Code, 1927, §§ 619, 621, 639, 641; Colorado, Compiled Laws, 1921, §§ 6966, 6968, 6970; Connecticut, General Statutes, 1918, § 6292; Florida, Revised General Statutes, 1920, §§ 5754, 5755; Idaho, Compiled Statutes, 1919, §§ 8568, 8570; Illinois, Revised Statutes, 1927, c. 134, §§ 7, 7a; Indiana, Burns' Revised Statutes, 1926, § 2862; Iowa, Code, 1924, § 8305; Louisiana, Acts, 1918, c. 134, p. 228; Maine, Revised Statutes, 1916, c. 60, § 24; Maryland, Bagby's Code, 1926, § 489; Michigan, Compiled Statutes, 1915, § 15104; Minnesota, General Statutes, 1923, §§ 10423, 10424; Mississippi, Hemingway's Code, 1927, § 1174; Missouri, Revised Statutes, 1919, § 3605; Montana, Penal Code, 1921, § 11494; Nebraska, Compiled Statutes, 1922, § 7088; Nevada, Revised Laws, 1912, §§ 4603, 4605, 4609, 4631; New Jersey, Compiled Statutes, 1910, p. 5319; New York, Consolidated Laws, c. 40, §§ 552, 553; North Carolina, Consolidated Statutes, 1919, §§ 4497, 4498, 4499; North Dakota, Compiled Laws, 1913, § 10078; Ohio, Page's General Code, 1926, § 13388, 13419; Oklahoma, Session Laws, 1923, c. 46; Oregon, Olson's Laws, 1920, §§ 2260, 2266; Pennsylvania, Statutes, 1920, §§ 6306, 6308, 6309; Rhode Island, General Laws, 1923, § 6104; South Dakota, Revised Code, 1919, §§ 4346, 9801; Tennessee, Shannon's Code, 1919, §§ 1837, 1838; Utah, Compiled Laws, 1917, §§ 8403, 8405, 8434; Washington, Pierce's Code, 1921, §§ 8982, 8983, Wisconsin, Statutes, 1927, § 348.36.</p>
<p>The Alaskan Penal Code, Act of March 3, 1899, c. 429, <span class="citation no-link">30 Stat. 1253</span>, 1278, provides that "if any officer, agent, operator, clerk, or employee of any telegraph company, or any other person, shall wilfully divulge to any other person than the party from whom the same was received, or to whom the same was addressed, or his agent or attorney, any message received or sent, or intended to be sent, over any telegraph line, or the contents, substance, purport, effect, or meaning of such message, or any part thereof,. . . the person so offending shall be deemed guilty of a misdemeanor, and shall be punished by a fine not to exceed one thousand dollars or imprisonment not to exceed one year, or by both such fine and imprisonment, in the discretion of the court."</p>
<p>The Act of October 29, 1918, c. 197, <span class="citation no-link">40 Stat. 1017</span>, provided: "That whoever during the period of governmental operation of the telephone and telegraph systems of the United States . . . shall, without authority and without the knowledge and consent of the other users thereof, except as may be necessary for operation of the service, tap any telegraph or telephone line, or wilfully interfere with the operation of such telephone and telegraph systems or with the transmission of any telephone or telegraph message, or with the delivery of any such message, or whoever being employed in any such telephone or telegraph service shall divulge the contents of any such telephone or telegraph message to any person not duly authorized to receive the same, shall be fined not exceeding $1,000 or imprisoned for not more than one year, or both."</p>
<p>The Radio Act, February 23, 1927, c. 169, § 27, <span class="citation no-link">44 Stat. 1162</span>, 1172, provides that "no person not being authorized by the sender shall intercept any message and divulge or publish the contents, substance, purport, effect, or meaning of such intercepted message to any person."</p>
<p>[14]  The above figures relate to Case No. 493. In Nos. 532-533, the Government evidence fills 278 pages, of which 140 are recitals of the evidence obtained by wire-tapping.</p>
<p>[15]  According to the Government's brief, p. 41, "The Prohibition Unit of the Treasury disclaims it [wire-tapping] and the Department of Justice has frowned on it." See also "Prohibition Enforcement," 69th Congress, 2d Session, Senate Doc. No. 198, pp. IV, V, 13, 15, referred to Committee, January 25, 1927; also Same, Part 2.</p>
<p>[16]  See <i>Hannay</i> v. <i>Eve,</i> <span class="citation" data-id="84810"><a href="/opinion/84810/hannay-v-eve/#247" aria-description="Citation for case: Hannay v. Eve">3 Cranch, 242, 247</a></span>; <i>Bank of the </i><i>United States</i> v. <i>Owens,</i> <span class="citation" data-id="85646"><a href="/opinion/85646/president-of-the-bank-of-the-united-states-v-owens/#538" aria-description="Citation for case: President of the Bank of the United States v. Owens">2 Pet. 527, 538</a></span>; <i>Bartle</i> v. <i>Coleman,</i> <span class="citation" data-id="85698"><a href="/opinion/85698/bartle-v-nutt/#188" aria-description="Citation for case: Bartle v. Nutt">4 Pet. 184, 188</a></span>; <i>Kennett</i> v. <i>Chambers,</i> <span class="citation" data-id="86769"><a href="/opinion/86769/kennett-v-chambers/#52" aria-description="Citation for case: Kennett v. Chambers">14 How. 38, 52</a></span>; <i>Marshall</i> v. <i>Baltimore &amp; Ohio R.R. Co.,</i> <span class="citation" data-id="9416542"><a href="/opinion/86875/marshall-v-baltimore-ohio-railroad/#334" aria-description="Citation for case: Marshall v. Baltimore &amp; Ohio Railroad">16 How. 314, 334</a></span>; <i>Tool Co.</i> v. <i>Norris,</i> 2 Wall 45, 54; <i>The Ouachita Cotton,</i> <span class="citation" data-id="87951"><a href="/opinion/87951/the-ouachita-cotton/#532" aria-description="Citation for case: The Ouachita Cotton">6 Wall. 521, 532</a></span>; <i>Coppell</i> v. <i>Hall,</i> <span class="citation" data-id="88038"><a href="/opinion/88038/coppell-v-hall/" aria-description="Citation for case: Coppell v. Hall">7 Wall. 542</a></span>; <i>Forsyth</i> v. <i>Woods,</i> <span class="citation" data-id="88341"><a href="/opinion/88341/forsyth-v-woods/#486" aria-description="Citation for case: Forsyth v. Woods">11 Wall. 484, 486</a></span>; <i>Hanauer</i> v. <i>Doane,</i> <span class="citation" data-id="88397"><a href="/opinion/88397/hanauer-v-doane/#349" aria-description="Citation for case: Hanauer v. Doane">12 Wall. 342, 349</a></span>; <i>Trist</i> v. <i>Child,</i> <span class="citation" data-id="89027"><a href="/opinion/89027/trist-v-child/#448" aria-description="Citation for case: Trist v. Child">21 Wall. 441, 448</a></span>; <i>Meguire</i> v. <i>Corwine,</i> <span class="citation" data-id="90098"><a href="/opinion/90098/meguire-v-corwine/#111" aria-description="Citation for case: Meguire v. Corwine">101 U.S. 108, 111</a></span>; <i>Oscanyan</i> v. <i>Arms Co.,</i> <span class="citation" data-id="90320"><a href="/opinion/90320/oscanyan-v-arms-co/" aria-description="Citation for case: Oscanyan v. Arms Co.">103 U.S. 261</a></span>; <i>Irwin</i> v. <i>Williar,</i> <span class="citation" data-id="91053"><a href="/opinion/91053/irwin-v-williar/#510" aria-description="Citation for case: Irwin v. Williar">110 U.S. 499, 510</a></span>; <i>Woodstock Iron Co.</i> v. <i>Richmond &amp; Danville Extension Co.,</i> <span class="citation" data-id="92439"><a href="/opinion/92439/woodstock-iron-co-v-richmond-danville-extension-co/" aria-description="Citation for case: Woodstock Iron Co. v. Richmond &amp; Danville Extension Co.">129 U.S. 643</a></span>; <i>Gibbs</i> v. <i>Consolidated Gas Co.,</i> <span class="citation" data-id="92483"><a href="/opinion/92483/gibbs-v-consolidated-gas-co-of-baltimore/#411" aria-description="Citation for case: Gibbs v. Consolidated Gas Co. of Baltimore">130 U.S. 396, 411</a></span>; <i>Embrey</i> v. <i>Jemison,</i> <span class="citation" data-id="92547"><a href="/opinion/92547/embrey-v-jemison/#348" aria-description="Citation for case: Embrey v. Jemison">131 U.S. 336, 348</a></span>; <i>West</i> v. <i>Camden,</i> <span class="citation" data-id="92798"><a href="/opinion/92798/west-v-camden/#521" aria-description="Citation for case: West v. Camden">135 U.S. 507, 521</a></span>; <i>McMullen</i> v. <i>Hoffman,</i> <span class="citation" data-id="95090"><a href="/opinion/95090/mcmullen-v-hoffman/#654" aria-description="Citation for case: McMullen v. Hoffman">174 U.S. 639, 654</a></span>; <i>Hazelton</i> v. <i>Sheckells,</i> <span class="citation" data-id="96460"><a href="/opinion/96460/hazelton-v-sheckells/" aria-description="Citation for case: Hazelton v. Sheckells">202 U.S. 71</a></span>; <i>Crocker</i> v. <i>United States,</i> <span class="citation" data-id="98638"><a href="/opinion/98638/crocker-v-united-states/#78" aria-description="Citation for case: Crocker v. United States">240 U.S. 74, 78</a></span>. Compare <i>Holman</i> v. <i>Johnson,</i> 1 Cowp. 341.</p>
<p>[17]  See <i>Creath's Administrator</i> v. <i>Sims,</i> <span class="citation" data-id="86416"><a href="/opinion/86416/creaths-administrator-v-sims/#204" aria-description="Citation for case: Creath&#x27;s Administrator v. Sims">5 How. 192, 204</a></span>; <i>Kennett</i> v. <i>Chambers,</i> <span class="citation" data-id="86769"><a href="/opinion/86769/kennett-v-chambers/#49" aria-description="Citation for case: Kennett v. Chambers">14 How. 38, 49</a></span>; <i>Randall</i> v. <i>Howard,</i> <span class="citation" data-id="87533"><a href="/opinion/87533/randall-v-howard/#586" aria-description="Citation for case: Randall v. Howard">2 Black, 585, 586</a></span>; <i>Wheeler</i> v. <i>Sage,</i> <span class="citation" data-id="87601"><a href="/opinion/87601/wheeler-v-sage/#530" aria-description="Citation for case: Wheeler v. Sage">1 Wall. 518, 530</a></span>; <i>Dent</i> v. <i>Ferguson,</i> <span class="citation" data-id="92567"><a href="/opinion/92567/dent-v-ferguson/#64" aria-description="Citation for case: Dent v. Ferguson">132 U.S. 50, 64</a></span>; <i>Pope Manufacturing Co.</i> v. <i>Gormully,</i> <span class="citation" data-id="93318"><a href="/opinion/93318/pope-manufacturing-co-v-gormully/#236" aria-description="Citation for case: Pope Manufacturing Co. v. Gormully">144 U.S. 224, 236</a></span>; <i>Miller</i> v. <i>Ammon,</i> <span class="citation" data-id="93392"><a href="/opinion/93392/miller-v-ammon/#425" aria-description="Citation for case: Miller v. Ammon">145 U.S. 421, 425</a></span>; <i>Hazelton</i> v. <i>Sheckells,</i> <span class="citation" data-id="96460"><a href="/opinion/96460/hazelton-v-sheckells/#79" aria-description="Citation for case: Hazelton v. Sheckells">202 U.S. 71, 79</a></span>. <i>Compare </i><i>International News Service</i> v. <i>Associated Press,</i> <span class="citation" data-id="9418368"><a href="/opinion/99248/international-news-service-v-associated-press/#245" aria-description="Citation for case: International News Service v. Associated Press">248 U.S. 215, 245</a></span>.</p>
<p>[18]  Compare <i>State</i> v. <i>Simmons,</i> <span class="citation" data-id="7887295"><a href="/opinion/7936833/state-v-simmons/#264" aria-description="Citation for case: State v. Simmons">39 Kan. 262, 264-265</a></span>; <i>State</i> v. <i>Miller,</i> <span class="citation" data-id="6616565"><a href="/opinion/6734774/state-v-miller/#163" aria-description="Citation for case: State v. Miller">44 Mo. App. 159, 163-164</a></span>; <i>In re Robinson,</i> <span class="citation" data-id="6646653"><a href="/opinion/6763902/in-re-robinson/" aria-description="Citation for case: In re Robinson">29 Neb. 135</a></span>; <i>Harris</i> v. <i>State,</i> 15 Tex. App. 629, 634-635, 639.</p>
<p>[19]  See <i>Armstrong</i> v. <i>Toler,</i> <span class="citation" data-id="85492"><a href="/opinion/85492/armstrong-v-toler/" aria-description="Citation for case: Armstrong v. Toler">11 Wheat. 258</a></span>; <i>Brooks</i> v. <i>Martin,</i> <span class="citation" data-id="9416695"><a href="/opinion/87628/brooks-v-martin/" aria-description="Citation for case: Brooks v. Martin">2 Wall. 70</a></span>; <i>Planters' Bank</i> v. <i>Union Bank,</i> <span class="citation" data-id="9416906"><a href="/opinion/88700/planters-bank-v-union-bank/#499" aria-description="Citation for case: Planters&#x27; Bank v. Union Bank">16 Wall. 483, 499-500</a></span>; <i>Houston &amp; Texas Central R.R. Co.</i> v. <i>Texas,</i> <span class="citation" data-id="9841847"><a href="/opinion/95218/houston-texas-central-railroad-v-texas/#99" aria-description="Citation for case: Houston &amp; Texas Central Railroad v. Texas">177 U.S. 66, 99</a></span>; <i>Bothwell</i> v. <i>Buckbee, Mears Co.,</i> <span class="citation" data-id="101177"><a href="/opinion/101177/bothwell-v-buckbee-mears-co/" aria-description="Citation for case: Bothwell v. Buckbee-Mears Co">275 U.S. 274</a></span>.</p>
<p>[20]  See <i>Lutton</i> v. <i>Benin,</i> 11 Mod. 50; <i>Barlow</i> v. <i><span class="citation" data-id="88038"><a href="/opinion/88038/coppell-v-hall/" aria-description="Citation for case: Coppell v. Hall">Hall</a></span>,</i> 2 Anst. 461; <i>Wells</i> v. <i>Gurney,</i> 8 Barn. &amp; Cress. 769; <i>Ilsley</i> v. <i>Nichols,</i> <span class="citation no-link">12 Pick. 270</span>; <i>Carpenter</i> v. <i>Spooner,</i> <span class="citation" data-id="8357529"><a href="/opinion/8387511/carpenter-v-spooner/" aria-description="Citation for case: Carpenter v. Spooner">2 Sandf. 717</a></span>; <i>Metcalf</i> v. <i>Clark,</i> <span class="citation" data-id="5460681"><a href="/opinion/5615894/metcalf-v-clark/" aria-description="Citation for case: Metcalf v. Clark">41 Barb. 45</a></span>; <i>Williams</i> ads. <i>Reed,</i> <span class="citation" data-id="8058110"><a href="/opinion/8097589/williams-v-reed/" aria-description="Citation for case: Williams v. Reed">29 N.J.L. 385</a></span>; <i>Hill</i> v. <i>Goodrich,</i> <span class="citation" data-id="6578342"><a href="/opinion/6698340/hill-v-goodrich/" aria-description="Citation for case: Hill v. Goodrich">32 Conn. 588</a></span>; <i>Townsend</i> v. <i>Smith,</i> <span class="citation" data-id="6602971"><a href="/opinion/6721916/townsend-v-smith/" aria-description="Citation for case: Townsend v. Smith">47 Wis. 623</a></span>; <i>Blandin</i> v. <i>Ostrander,</i> <span class="citation" data-id="8802105"><a href="/opinion/8817552/blandin-v-ostrander/" aria-description="Citation for case: Blandin v. Ostrander">239 Fed. 700</a></span>; <i>Harkin</i> v. <i>Brundage,</i> <span class="citation" data-id="101214"><a href="/opinion/101214/harkin-v-brundage/" aria-description="Citation for case: Harkin v. Brundage">276 U.S. 36</a></span>, <i>id.,</i> 604.</p>
<p>[21]  <i>Coppell</i> v. <i>Hall,</i> <span class="citation" data-id="88038"><a href="/opinion/88038/coppell-v-hall/#558" aria-description="Citation for case: Coppell v. Hall">7 Wall. 542, 558</a></span>; <i>Oscanyan</i> v. <i>Arms Co.,</i> <span class="citation" data-id="90320"><a href="/opinion/90320/oscanyan-v-arms-co/#267" aria-description="Citation for case: Oscanyan v. Arms Co.">103 U.S. 261, 267</a></span>; <i>Higgins</i> v. <i>McCrea,</i> <span class="citation" data-id="91577"><a href="/opinion/91577/higgins-v-mccrea/#685" aria-description="Citation for case: Higgins v. McCrea">116 U.S. 671, 685</a></span>. Compare <i>Evans</i> v. <i>Richardson,</i> 3 Mer. 469; <i>Norman</i> v. <i>Cole,</i> 3 Esp. 253; <i>Northwestern Salt Co.</i> v. <i>Electrolytic Alkali Co.,</i> [1913] 3 K.B. 422.</p>
<p>[*]  <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727</a></span>. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>. <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>. <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>. <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>.</p>

</div>
```

---

## GROUP: content/cases/Oregon v. Elstad.md  (`case`, 6 assertions)

### content_page

```
---
title: "Oregon v. Elstad"
type: case
citation: "470 U.S. 298 (1985)"
parallel_cite: "105 S. Ct. 1285; 84 L. Ed. 2d 222; 53 U.S.L.W. 4244"
neutral_cite: 1985 U.S. LEXIS 60
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-04
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1985-03-04
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Oregon v. Elstad
  varies_by_point: true
  scope_note: "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn."
  point_overrides:
    - point: legacy-limited-oregon-v-elstad
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Missouri v. Seibert
          cluster_id: 137002
          cite: 542 U.S. 600
          field_ii: limited
      scope_note: "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111364/oregon-v-elstad/"
  cluster_id: 111364
  opinion_id: 9429930
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Missouri v. Seibert]]", "[[Miranda v. Arizona]]", "[[Dickerson v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "two-step", "unwarned-statement", "waiver"]
holding: "An initial, un-warned but voluntary statement does not automatically taint a later confession; if the suspect is then properly…"
lake:
  record_id: Oregon v. Elstad
  status: verified
  projected_at: 2026-07-06
---

# Oregon v. Elstad

*470 U.S. 298 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers came to Elstad's home with a warrant for his arrest in a burglary. Before any *[[Miranda v. Arizona|Miranda]]* warnings, an officer said he believed Elstad was involved, and Elstad admitted, "Yes, I was there." About an hour later at the station, he was given full *[[Miranda v. Arizona|Miranda]]* warnings, waived his rights, and gave a complete written confession.

## Issue
Whether an initial, voluntary but un-Mirandized admission taints a later, properly warned confession.

## Rule
No, absent coercion. "[A]bsent deliberately coercive or improper tactics in obtaining the initial statement, the mere fact that a suspect has made an unwarned admission does not warrant a presumption of compulsion. A subsequent administration of *Miranda* warnings to a suspect who has given a voluntary but unwarned statement ordinarily should suffice to remove the conditions that precluded admission of the earlier statement." — 470 U.S. at 314. ^pin-314

"We hold today that a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite *Miranda* warnings." — *Id.* at 318. ^pin-318

**As applied to deliberate "question-first" two-step interrogations, this rule was later limited by [[Missouri v. Seibert]]** (see Treatment).

## Application
Elstad's initial "Yes, I was there" was voluntary and not the product of coercive tactics, so it did not create a presumption that his later station-house confession was compelled. Once he received and waived his *[[Miranda v. Arizona|Miranda]]* rights, his subsequent written confession was admissible. The Court reversed the suppression of the second statement.

## Conclusion
The properly warned confession was admissible despite the earlier unwarned admission; the Oregon Court of Appeals' suppression order was reversed.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Limited as applied by [[Missouri v. Seibert]] (2004)**: where officers deliberately use a "question-first, warn-later" two-step technique to undermine *[[Miranda v. Arizona|Miranda]]*, the midstream warnings may be ineffective and the second statement inadmissible. *Elstad* continues to govern the ordinary case of an inadvertent or good-faith failure to warn followed by a properly warned statement. *Elstad* also relies on [[Miranda v. Arizona]] as a prophylactic, not constitutional, rule — a characterization later qualified by [[Dickerson v. United States]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Oregon v. Elstad*, 470 U.S. 298 (1985) — https://www.courtlistener.com/opinion/111364/oregon-v-elstad/ — pinpoints: 314, 318.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b10eb827ec7d8e72", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "470 U.S. 298 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 60", "official_citation_present": true, "parallel_cite": "105 S. Ct. 1285; 84 L. Ed. 2d 222; 53 U.S.L.W. 4244", "title": "Oregon v. Elstad", "year": "1985"}}
{"assertion_id": "4a0f9d6a9b22bd97", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An initial, un-warned but voluntary statement does not automatically taint a later confession; if the suspect is then properly…", "title": "Oregon v. Elstad"}}
{"assertion_id": "d0a9474a41fee776", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "Oregon v. Elstad"}}
{"assertion_id": "0290af64c7d7dbec", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Oregon v. Elstad"}}
{"assertion_id": "2672bdba730d4286", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-oregon-v-elstad"}, "payload": {"by": [{"cite": "542 U.S. 600", "cluster_id": "137002", "field_ii": "limited", "name": "Missouri v. Seibert"}], "field_i_validity": "caution", "point": "legacy-limited-oregon-v-elstad", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "Oregon v. Elstad"}}
{"assertion_id": "eda0a15913a1f047", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-03-04", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Oregon v. Elstad", "field_i_validity": "caution", "scope_note": "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn.", "title": "Oregon v. Elstad", "varies_by_point": "true"}}
```

### lake record — Oregon v. Elstad

```json
{
  "schema_version": "s2.v1",
  "record_id": "Oregon v. Elstad",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Oregon v. Elstad",
    "case_name_short": "Elstad",
    "case_name_full": "Oregon v. Elstad",
    "input_case_name": "Oregon v. Elstad",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-04",
    "year": 1985,
    "docket": null,
    "cluster_id": 111364,
    "lead_opinion_id": 9429930,
    "sibling_ids": [
      111364,
      9429930,
      9429931,
      9429932
    ],
    "absolute_url": "/opinion/111364/oregon-v-elstad/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "470 U.S. 298",
      "volume": "470",
      "reporter": "U.S.",
      "page": "298",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1285",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 222",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4244",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4244",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 60",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "60",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "470 U.S. 298",
        "volume": "470",
        "reporter": "U.S.",
        "page": "298",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1285",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 222",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 60",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "60",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4244",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4244",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "470 U.S. 298",
    "official_selection": {
      "court_class": "scotus",
      "selected": "470 U.S. 298",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-314",
      "page": null,
      "quote": "About an hour later at the station, he was given full *Miranda* warnings, waived his rights, and gave a complete written confession. ## Issue Whether an initial, voluntary but un-Mirandized admission taints a later, properly warned confession. ## Rule No, absent coercion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-318",
      "page": null,
      "quote": "We hold today that a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite *Miranda* warnings.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1985-03-04",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Oregon v. Elstad",
    "varies_by_point": true,
    "scope_note": "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn.",
    "point_overrides": [
      {
        "point": "legacy-limited-oregon-v-elstad",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Missouri v. Seibert",
            "cluster_id": 137002,
            "cite": "542 U.S. 600",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": "542 U.S. 600",
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
        "journal_ref": "Oregon v. Elstad:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Abbott",
          "cluster_id": 10366844,
          "cite": [
            "303 Ga. 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane1_negative"
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
        "journal_ref": "Oregon v. Elstad:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portillo",
          "cluster_id": 3210008,
          "cite": [
            "787 S.E.2d 822",
            "247 N.C. App. 834",
            "2016 N.C. App. LEXIS 619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Rigterink v. State of Florida",
          "cluster_id": 3196514,
          "cite": [
            "193 So. 3d 846",
            "41 Fla. L. Weekly Supp. 177",
            "2016 WL 1592714",
            "2016 Fla. LEXIS 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane1_negative"
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
        "journal_ref": "Oregon v. Elstad:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Hillery",
          "cluster_id": 111552,
          "cite": [
            "88 L. Ed. 2d 598",
            "106 S. Ct. 617",
            "474 U.S. 254",
            "1986 U.S. LEXIS 40",
            "54 U.S.L.W. 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leday v. State",
          "cluster_id": 1678149,
          "cite": [
            "983 S.W.2d 713",
            "1998 Tex. Crim. App. LEXIS 172",
            "1998 WL 870371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. Martinez",
          "cluster_id": 127927,
          "cite": [
            "155 L. Ed. 2d 984",
            "123 S. Ct. 1994",
            "538 U.S. 760",
            "2003 U.S. LEXIS 4274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillips v. People",
          "cluster_id": 4636609,
          "cite": [
            "2019 CO 72",
            "443 P.3d 1016"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Russell",
          "cluster_id": 1296847,
          "cite": [
            "882 P.2d 747",
            "125 Wash. 2d 24",
            "63 U.S.L.W. 2291",
            "1994 Wash. LEXIS 635"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 1653372,
          "cite": [
            "836 S.W.2d 530",
            "1992 Tenn. LEXIS 401"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Samayoa",
          "cluster_id": 5607879,
          "cite": [
            "15 Cal. 4th 795",
            "938 P.2d 2",
            "97 Daily Journal DAR 7699",
            "64 Cal. Rptr. 2d 400",
            "97 Cal. Daily Op. Serv. 4760",
            "1997 Cal. LEXIS 2966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patane",
          "cluster_id": 137003,
          "cite": [
            "159 L. Ed. 2d 667",
            "124 S. Ct. 2620",
            "542 U.S. 630",
            "2004 U.S. LEXIS 4577"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1890229,
          "cite": [
            "313 S.W.3d 274",
            "2010 Tex. Crim. App. LEXIS 722",
            "2010 WL 2382555"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connecticut v. Barrett",
          "cluster_id": 111796,
          "cite": [
            "93 L. Ed. 2d 920",
            "107 S. Ct. 828",
            "479 U.S. 523",
            "1987 U.S. LEXIS 419",
            "55 U.S.L.W. 4151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111364 OR 9429930 OR 9429931 OR 9429932) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQzNTcxMjAwMDAwJnM9NDI5MjY1NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111364+OR+9429930+OR+9429931+OR+9429932%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111364 OR 9429930 OR 9429931 OR 9429932)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTkmcz03NTEzNDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111364+OR+9429930+OR+9429931+OR+9429932%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111364 OR 9429930 OR 9429931 OR 9429932)",
        "reviewed": 45,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 45,
        "triage_read": 0,
        "triage_snippet_classified": 45
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111364 OR 9429930 OR 9429931 OR 9429932)",
    "indexed_citing_opinions": 1760,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111364,
        "count": 1568,
        "count_source": "search"
      },
      {
        "opinion_id": 9429930,
        "count": 232,
        "count_source": "search"
      },
      {
        "opinion_id": 9429931,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429932,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2824,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/oregon-v-elstad.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMzg3OTYmcz0xMDI4MTUxMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111364+OR+9429930+OR+9429931+OR+9429932%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111364,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 104440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 244463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 260072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 262430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 263485,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 275353,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 280455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 280782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 315338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 317110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 336178,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 339054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 348792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 349630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 397374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 414117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 877624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1112895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1144156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1145231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1161498,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1170008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1173989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1180469,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1231742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1234251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1248061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1306478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1320417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1360101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1419581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1472767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1496973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1502926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1519558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1566744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1631959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1634761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1635158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1758320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1837744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1851084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1962849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1992428,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2012195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2023548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2064265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2084604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2093616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2096024,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2112079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2122160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2141638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2195849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2211745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2225068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2280368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2285307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2609123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2615164,
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
    "date_created": "2026-07-05T16:20:09Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:20:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:20:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:20:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Oregon v. Elstad

```
<opinion type="majority">
<author id="b356-5">Justice O’Connor</author>
<p id="AQH">delivered the opinion of the Court.</p>
<p id="b356-6">This case requires us to decide whether an initial failure of law enforcement officers to administer the warnings required by <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), without more, “taints” subsequent admissions made after a suspect has been fully advised of and has waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. Respondent, Michael James Elstad, was convicted of burglary by an Oregon trial court. The Oregon Court of Appeals reversed, holding that respondent’s signed confession, although voluntary, was rendered inadmissible by a prior remark made in response to questioning without benefit of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./465/1078/">465 U. S. 1078</a></span> (1984), and we now reverse.</p>
<p id="b356-7">I</p>
<p id="b356-8">In December 1981, the home of Mr. and Mrs. Gilbert Gross, in the town of Salem, Polk County, Ore., was burglarized. Missing were art objects and furnishings valued at $150,000. A witness to the burglary contacted the Polk County Sheriff’s Office, implicating respondent Michael El-stad, an 18-year-old neighbor and friend of the Grosses’ teenage son. Thereupon, Officers Burke and McAllister went to the home of respondent Elstad, with a warrant for his arrest. Elstad’s mother answered the door. She led the officers to her son’s room where he lay on his bed, clad in shorts and listening to his stereo. The officers asked him to get dressed and to accompany them into the living room. Officer McAllister asked respondent’s mother to step into the kitchen, where he explained that they had a warrant for her <page-number citation-index="1" label="301">*301</page-number>son’s arrest for the burglary of a neighbor’s residence. Officer Burke remained with Elstad in the living room. He later testified:</p>
<blockquote id="b357-4">“I sat down with Mr. Elstad and I asked him if he was aware of why Detective McAllister and myself were there to talk with him. He stated no, he had no idea why we were there. I then asked him if he knew a person by the name of Gross, and he said yes, he did, and also added that he heard that there was a robbery at the Gross house. And at that point I told Mr. Elstad that I felt he was involved in that, and he looked at me and stated, ‘Yes, I was there.’” App. 19-20.</blockquote>
<p id="b357-5">The officers then escorted Elstad to the back of the patrol car. As they were about to leave for the Polk County Sheriff’s office, Elstad’s father arrived home and came to the rear of the patrol car. The officers advised him that his son was a suspect in the burglary. Officer Burke testified that Mr. Elstad became quite agitated, opened the rear door of the car and admonished his son: “I told you that you were going to get into trouble. You wouldn’t listen to me. You never learn.” <em>Id., </em>at 21.</p>
<p id="b357-6">Elstad was transported to the Sheriff’s headquarters and approximately one hour later, Officers Burke and McAllister joined him in McAllister’s office. McAllister then advised respondent for the first time of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, reading from a standard card. Respondent indicated he understood his rights, and, having these rights in mind, wished to speak with the officers. Elstad gave a full statement, explaining that he had known that the Gross family was out of town and had been paid to lead several acquaintances to the Gross residence and show them how to gain entry through a defective sliding glass door. The statement was typed, reviewed by respondent, read back to him for correction, initialed and signed by Elstad and both officers. As an afterthought, Elstad added and initialed the sentence, “After leaving the house Robby &amp; I went back to [the] van &amp; Robby handed <page-number citation-index="1" label="302">*302</page-number>me a small bag of grass.” App. 42. Respondent concedes that the officers made no threats or promises either at his residence or at the Sheriff’s office.</p>
<p id="b358-5">Respondent was charged with first-degree burglary. He was represented at trial by retained counsel. Elstad waived his right to a jury, and his case was tried by a Circuit Court Judge. Respondent moved at once to suppress his oral statement and signed confession. He contended that the statement he made in response to questioning at his house “let the cat out of the bag,” citing <em>United States </em>v. <em>Bayer, </em><span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/" aria-description="Citation for case: United States v. Bayer">331 U. S. 532</a></span> (1947), and tainted the subsequent confession as “fruit of the poisonous tree,” citing <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). The judge ruled that the statement, “I was there,” had to be excluded because the defendant had not been advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. The written confession taken after Elstad’s arrival at the Sheriff’s office, however, was admitted in evidence. The court found:</p>
<blockquote id="b358-6">“[H]is written statement was given freely, voluntarily and knowingly by the defendant after he had waived his right to remain silent and have counsel present which waiver was evidenced by the card which the defendant had signed. [It] was not tainted in any way by the previous brief statement between the defendant and the Sheriff’s Deputies that had arrested him.” App. 45.</blockquote>
<p id="b358-7">Elstad was found guilty of burglary in the first degree. He received a 5-year sentence and was ordered to pay $18,000 in restitution.</p>
<p id="b358-8">Following his conviction, respondent appealed to the Oregon Court of Appeals, relying on <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>and <em><span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/" aria-description="Citation for case: United States v. Bayer">Bayer</a></span>. </em>The State conceded that Elstad had been in custody when he made his statement, “I was there,” and accordingly agreed that this statement was inadmissible as having been given without the prescribed <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. But the State maintained that any conceivable “taint” had been dissipated prior to the respondent’s written confession by McAllister’s careful administration of the requisite warnings. The Court <page-number citation-index="1" label="303">*303</page-number>of Appeals reversed respondent’s conviction, identifying the crucial constitutional inquiry as “whether there was a sufficient break in the stream of events between [the] inadmissible statement and the written confession to insulate the latter statement from the effect of what went before.” <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#676" aria-description="Citation for case: State v. Elstad">61 Ore. App. 673, 676</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#554" aria-description="Citation for case: State v. Elstad">658 P. 2d 552, 554</a></span> (1983). The Oregon court concluded:</p>
<blockquote id="b359-5">“Regardless of the absence of actual compulsion, the coercive impact of the unconstitutionally obtained statement remains, because in a defendant’s mind it has sealed his fate. It is this impact that must be dissipated in order to make a subsequent confession admissible. In determining whether it has been dissipated, lapse of time, and change of place from the original surroundings are the most important considerations.” <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#677" aria-description="Citation for case: State v. Elstad"><em>Id., </em>at 677</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#554" aria-description="Citation for case: State v. Elstad">658 P. 2d, at 554</a></span>.</blockquote>
<p id="b359-6">Because of the brief period separating the two incidents, the “cat was sufficiently out of the bag to exert a coercive impact on [respondent’s] later admissions.” <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#678" aria-description="Citation for case: State v. Elstad"><em>Id., </em>at 678</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#555" aria-description="Citation for case: State v. Elstad">658 P. 2d, at 555</a></span>.</p>
<p id="b359-7">The State of Oregon petitioned the Oregon Supreme Court for review, and review was declined. This Court granted certiorari to consider the question whether the Self-Incrimination Clause of the Fifth Amendment requires the suppression of a confession, made after proper <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and a valid waiver of rights, solely because the police had obtained an earlier voluntary but unwarned admission from the defendant.</p>
<p id="b359-8">II</p>
<p id="b359-9">The arguments advanced in favor of; suppression of respondent’s written confession rely heavily on metaphor. One metaphor, familiar from the Fourth Amendment context, would require that respondent’s confession, regardless of its integrity, voluntariness, and probative value, be suppressed as the “tainted fruit of the poisonous tree” of the Miranda, violation. A second metaphor questions whether a <page-number citation-index="1" label="304">*304</page-number>confession can be truly voluntary once the “cat is out of the bag.” Taken out of context, each of these metaphors can be misleading. They should not be used to obscure fundamental differences between the role of the Fourth Amendment exclusionary rule and the function of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>in guarding against the prosecutorial use of compelled statements as prohibited by the Fifth Amendment. The Oregon court assumed and respondent here contends that a failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings necessarily breeds the same consequences as police infringement of a constitutional right, so that evidence uncovered following an unwarned statement must be suppressed as “fruit of the poisonous tree.” We believe this view misconstrues the nature of the protections afforded by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and therefore misreads the consequences of police failure to supply them.</p>
<p id="b360-5">A</p>
<p id="b360-6">Prior to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the admissibility of an accused’s in-custody statements was judged solely by whether they were “voluntary” within the meaning of the Due Process Clause. See, <em>e. g., Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span> (1963); <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940). If a suspect’s statements had been obtained by “techniques and methods offensive to due process,” <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S., at 515</a></span>, or under circumstances in which the suspect clearly had no opportunity to exercise “a free and unconstrained will,” <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#514" aria-description="Citation for case: Haynes v. Washington"><em>id., </em>at 514</a></span>, the statements would not be admitted. The Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>required suppression of many statements that would have been admissible under traditional due process analysis by presuming that statements made while in custody and without adequate warnings were protected by the Fifth Amendment. The Fifth Amendment, of course, is not concerned with nontestimonial evidence. See <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 764</a></span> (1966) (defendant may be compelled to supply blood samples). Nor is it concerned <page-number citation-index="1" label="305">*305</page-number>with moral and psychological pressures to confess emanating from sources other than official coercion. See, <em>e. g., California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span>, and n. 3 (1983) <em>(per curiam); Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#303" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 303</a></span>, and n. 10 (1980); <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495-496</a></span> (1977). Voluntary statements “remain a proper element in law enforcement.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>. “Indeed, far from being prohibited by the Constitution, admissions of guilt by wrongdoers, if not coerced, are inherently desirable. . . . Absent some officially coerced self-accusation, the Fifth Amendment privilege is not violated by even the most damning admissions.” <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977). As the Court noted last Term in <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984) (footnote omitted):</p>
<blockquote id="b361-5">“The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court, however, presumed that interrogation in certain custodial circumstances is inherently coercive and . . . that statements made under those circumstances are inadmissible unless the suspect is specifically informed of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and freely decides to forgo those rights. The prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings therefore are ‘not themselves rights protected by the Constitution but [are] instead measures to insure that the right against compulsory self-incrimination [is] protected.’ <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974); see <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#492" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 492</a></span> (1981) (Powell, J., concurring). Requiring <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before custodial interrogation provides ‘practical reinforcement’ for the Fifth Amendment right.”</blockquote>
<p id="b361-6">Respondent’s contention that his confession was tainted by the earlier failure of the police to provide <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and must be excluded as “fruit of the poisonous tree” assumes the existence of a constitutional violation. This figure of speech is drawn from <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), in which the Court held that evidence and wit<page-number citation-index="1" label="306">*306</page-number>nesses discovered as a result of a search in violation of the Fourth Amendment must be excluded from evidence. The <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>doctrine applies as well when the fruit of the Fourth Amendment violation is a confession. It is settled law that “a confession obtained through custodial interrogation after an illegal arrest should be excluded unless intervening events break the causal connection between the illegal arrest and the confession so that the confession is ‘sufficiently an act of free will to purge the primary taint.’” <em>Taylor </em>v. <em>Alabama, </em><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#690" aria-description="Citation for case: Taylor v. Alabama">457 U. S. 687, 690</a></span> (1982) (quoting <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 602</a></span> (1975)).</p>
<p id="b362-5">But as we explained in <em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Quarles</a></span> </em>and <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span>, </em>a procedural <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation differs in significant respects from violations of the Fourth Amendment, which have traditionally mandated a broad application of the “fruits” doctrine. The purpose of the Fourth Amendment exclusionary rule is to deter unreasonable searches, no matter how probative their fruits. <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#216" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 216-217</a></span> (1979); <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#600" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 600-602</a></span>. “The exclusionary rule, . . . when utilized to effectuate the Fourth Amendment, serves interests and policies that are distinct from those it serves under the Fifth.” <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois"><em>Id., </em>at 601</a></span>. Where a Fourth Amendment violation “taints” the confession, a finding of voluntariness for the purposes of the Fifth Amendment is merely a threshold requirement in determining whether the confession may be admitted in evidence. <em>Taylor </em>v. <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#690" aria-description="Citation for case: Taylor v. Alabama"><em>Alabama, supra, </em>at 690</a></span>. Beyond this, the prosecution must show a sufficient break in events to undermine the inference that the confession was caused by the Fourth Amendment violation.</p>
<p id="b362-6">The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>exclusionary rule, however, serves the Fifth Amendment and sweeps more broadly than the Fifth Amendment itself. It may be triggered even in the absence of a Fif th Amendment violation.<footnotemark>1</footnotemark> The Fif th Amendment prohib<page-number citation-index="1" label="307">*307</page-number>its use by the prosecution in its case in chief only of <em>compelled </em>testimony. Failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings creates a presumption of compulsion. Consequently, unwarned statements that are otherwise voluntary within the meaning of the Fifth Amendment must nevertheless be excluded from evidence under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>Thus, in the individual case, <em>Miranda’s </em>preventive medicine provides a remedy even to the defendant who has suffered no identifiable constitutional harm. See <em>New York </em>v. <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles"><em>Quarles, supra, </em>at 654</a></span>; <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974).</p>
<p id="b363-4">But the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>presumption, though irrebuttable for purposes of the prosecution’s case in chief, does not require that the statements and their fruits be discarded as inherently tainted. Despite the fact that patently <em>voluntary </em>statements taken in violation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>must be excluded from the prosecution’s case, the presumption of coercion does not bar their use for impeachment purposes on cross-examination. <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971). The Court in <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em>rejected as an “extravagant extension of the Constitution,” the theory that a defendant who had confessed under circumstances that made the confession inadmissible, could thereby enjoy the freedom to “deny every fact disclosed or discovered as a ‘fruit’ of his confession, free from confrontation with his prior statements” and that the voluntariness of his confession would be totally irrelevant. <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York"><em>Id., </em>at 225</a></span>, and n. 2. Where an unwarned statement is preserved for use in situations that fall outside the sweep of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>presumption, “the primary criterion of admissibility <page-number citation-index="1" label="308">*308</page-number>[remains] the ‘old’ due process voluntariness test.” Schul-hofer, Confessions and the Court, <span class="citation no-link">79 Mich. L. Rev. 865</span>, 877 (1981).</p>
<p id="b364-5">In <em>Michigan </em>v. <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker, supra,</a></span> </em>the Court was asked to extend the <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>fruits doctrine to suppress the testimony of a witness for the prosecution whose identity was discovered as the result of a statement taken from the accused without benefit of full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. As in respondent’s case, the breach of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>procedures in <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span> </em>involved no actual compulsion. The Court concluded that the unwarned questioning “did not abridge respondent’s constitutional privilege . . . but departed only from the prophylactic standards later laid down by this Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to safeguard that privilege.” <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 446</a></span>. Since there was no actual infringement of the suspect’s constitutional rights, the case was not controlled by the doctrine expressed in <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>that fruits of a constitutional violation must be suppressed. In deciding “how sweeping the judicially imposed consequences” of a failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings should be, <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 445</a></span>, the <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span> </em>Court noted that neither the general goal of deterring improper police conduct nor the Fifth Amendment goal of assuring trustworthy evidence would be served by suppression of the witness’ testimony. The unwarned confession must, of course, be suppressed, but the Court ruled that introduction of the third-party witness’ testimony did not violate Tucker’s Fifth Amendment rights.</p>
<p id="b364-6">We believe that this reasoning applies with equal force when the alleged “fruit” of a noncoercive <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation is neither a witness nor an article of evidence but the accused’s own voluntary testimony. As in <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span>, </em>the absence of any coercion or improper tactics undercuts the twin rationales— trustworthiness and deterrence — for a broader rule. Once warned, the suspect is free to exercise his own volition in deciding whether or not to make a statement to the authorities. The Court has often noted: “‘[A] living witness is not to be <page-number citation-index="1" label="309">*309</page-number>mechanically equated with the proffer of inanimate eviden-tiary objects illegally seized. . . . [T]he living "witness is an individual human personality whose attributes of will, perception, memory and <em>volition </em>interact to determine what testimony he wall give.”’ <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#277" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 277</a></span> (1978) (emphasis added) (quoting from <em>Smith </em>v. <em>United States, </em>117 U. S. App. D. C. 1, 3-4, <span class="citation" data-id="9449714"><a href="/opinion/262430/wilson-m-smith-jr-v-united-states-of-america-raymond-bowden-v-united/#881" aria-description="Citation for case: Wilson M. Smith, Jr. v. United States of America, Raymond...">324 F. 2d 879, 881-882</a></span> (1963) (Burger, J.) (footnotes omitted), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./377/954/">377 U. S. 954</a></span> (1964)).</p>
<p id="b365-5">Because <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings may inhibit persons from giving information, this Court has determined that they need be administered only after the person is taken into “custody” or his freedom has otherwise been significantly restrained. <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>. Unfortunately, the task of defining “custody” is a slippery one, and “policemen investigating serious crimes [cannot realistically be expected to] make no errors whatsoever.” <em>Michigan </em>v. <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker"><em>Tucker, supra, </em>at 446</a></span>. If errors are made by law enforcement officers in administering the prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>procedures, they should not breed the same irremediable consequences as police infringement of the Fifth Amendment itself. It is an unwarranted extension of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to hold that a simple failure to administer the warnings, unaccompanied by any actual coercion or other circumstances calculated to undermine the suspect’s ability to exercise his free will, so taints the investigatory process that a subsequent voluntary and informed waiver is ineffective for some indeterminate period. Though <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires that the unwarned admission must be suppressed, the admissibility of any subsequent statement should turn in these circumstances solely on whether it is knowingly and voluntarily made.</p>
<p id="b365-6">B</p>
<p id="b365-7">The Oregon court, however, believed that the unwarned remark compromised the voluntariness of respondent’s later confession. It was the court’s view that the prior <em>answer </em><page-number citation-index="1" label="310">*310</page-number>and not the unwarned questioning impaired respondent’s ability to give a valid waiver and that only lapse of time and change of place could dissipate what it termed the “coercive impact” of the inadmissible statement. When a prior statement is actually coerced, the time that passes between confessions, the change in place of interrogations, and the change in identity of the interrogators all bear on whether that coercion has carried over into the second confession. See <em>Westover </em>v. <em>United States, </em>decided together with <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#494" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 494</a></span>; <em>Clewis </em>v. <em>Texas, </em><span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707</a></span> (1967). The failure of police to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings does not mean that the statements received have actually been coerced, but only that courts will presume the privilege against compulsory self-incrimination has not been intelligently exercised. See <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S., at 654</a></span>, and n. 5; <em>Miranda </em>v. <em>Arizona, supra, </em>at 457. Of the courts that have considered whether a properly warned confession must be suppressed because it was preceded by an unwarned but clearly voluntary admission, the majority have explicitly or implicitly recognized that <em>Westover's </em>requirement of a break in the stream of events is inapposite.<footnotemark>2</footnotemark> In these circumstances, a careful and thorough <page-number citation-index="1" label="311">*311</page-number>administration of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings serves to cure the condition that rendered the unwarned statement inadmissible. The warning conveys the relevant information and thereafter the suspect’s choice whether to exercise his privilege to remain silent should ordinarily be viewed as an “act of free will.” <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 486</a></span>.</p>
<p id="b367-4">The Oregon court nevertheless identified a subtle form of lingering compulsion, the psychological impact of the suspect’s conviction that he has let the cat out of the bag and, in so doing, has sealed his own fate. But endowing the psychological effects of <em>voluntary </em>unwarned admissions with constitutional implications would, practically speaking, disable the police from obtaining the suspect’s informed cooperation even when the official coercion proscribed by the Fifth Amendment played no part in either his warned or unwarned confessions. As the Court remarked in <em><span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/" aria-description="Citation for case: United States v. Bayer">Bayer</a></span>:</em></p>
<blockquote id="b367-5">“[AJfter an accused has once let the cat out of the bag by confessing, no matter what the inducement, he is never thereafter free of the psychological and practical disadvantages of having confessed. He can never get the cat back in the bag. The secret is out for good. In such a sense, a later confession may always be looked upon as fruit of the first. But this Court has never gone so far as to hold that making a confession under circumstances which preclude its use, perpetually disables the confessor from making a usable one after those conditions have been removed.” <span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/#540" aria-description="Citation for case: United States v. Bayer">331 U. S., at 540-541</a></span>.</blockquote>
<p id="b367-6">Even in such extreme cases as <em>Lyons </em>v. <em>Oklahoma, </em><span class="citation" data-id="9419526"><a href="/opinion/104010/lyons-v-oklahoma/" aria-description="Citation for case: Lyons v. Oklahoma">322 U. S. 596</a></span> (1944), in which police forced a full confession from the accused through unconscionable methods of interrogation, the Court has assumed that the coercive effect of the confes<page-number citation-index="1" label="312">*312</page-number>sion could, with time, be dissipated. See also <em>Westover </em>v. <em>United States, supra, </em>at 496.</p>
<p id="b368-5">This Court has never held that the psychological impact of voluntary disclosure of a guilty secret qualifies as state compulsion or compromises the voluntariness of a subsequent informed waiver. The Oregon court, by adopting this expansive view of Fifth Amendment compulsion, effectively immunizes a suspect who responds to <em>pre-Miranda </em>warning questions from the consequences of his subsequent informed waiver of the privilege of remaining silent. See <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#679" aria-description="Citation for case: State v. Elstad">61 Ore. App., at 679</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#555" aria-description="Citation for case: State v. Elstad">658 P. 2d, at 555</a></span> (Gillette, P. J., concurring). This immunity comes at a high cost to legitimate law enforcement activity, while adding little desirable protection to. the individual’s interest in not being <em>compelled </em>to testify against himself. Cf. <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#107" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 107-111</a></span> (1975) (White, J., concurring in result). When neither the initial nor the subsequent admission is coerced, little, justification exists for permitting the highly probative evidence of a voluntary confession to be irretrievably lost to the factfinder.</p>
<p id="b368-6">There is a vast difference between the direct consequences flowing from coercion of a confession by physical violence or other deliberate means calculated to break the suspect’s will and the uncertain consequences of disclosure of a “guilty secret” freely given in response to an unwarned but non-coercive question, as in this case. Justice Brennan’s contention that it is impossible to perceive any causal distinction between this case and one involving a confession that is coerced by torture is wholly unpersuasive.<footnotemark>3</footnotemark> Certainly, in <page-number citation-index="1" label="313">*313</page-number>respondent’s case, the causal connection between any psychological disadvantage created by his admission and his ultimate decision to cooperate is speculative and attenuated at</p>
<p id="b370-3"><page-number citation-index="1" label="314">*314</page-number>Though belated, the reading of respondent’s rights was undeniably complete. McAllister testified that he read the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings aloud from a printed card and recorded best. It is difficult to tell with certainty what motivates a suspect to speak. A suspect’s confession may be traced to factors as disparate as “a prearrest event such as a visit with a minister,” <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#220" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 220</a></span> (Stevens, J., concurring), or an intervening event such as the exchange of words respondent had with his father. We must conclude that, absent deliberately coercive or improper tactics in obtaining the initial statement, the mere fact that a suspect has made an unwarned admission does not warrant a presumption of compulsion. A subsequent administration of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to a suspect who has given a voluntary but unwarned statement ordinarily should suffice to remove the conditions that precluded admission of the earlier statement. In such circumstances, the finder of fact may reasonably conclude that the suspect made a rational and intelligent choice whether to waive or invoke his rights.</p>
<p id="b370-7">I — I <page-number citation-index="1" label="315">*315</page-number>Elstad’s responses.<footnotemark>4</footnotemark> There is no question that respondent knowingly and voluntarily waived his right to remain silent before he described his participation in the burglary. It is also beyond dispute that respondent’s earlier remark was voluntary, within the meaning of the Fifth Amendment. Neither the environment nor the manner of either “interrogation” was coercive. The initial conversation took place at midday, in the living room area of respondent’s own home, with his mother in the kitchen area, a few steps away. Although in retrospect the officers testified that respondent was then in custody, at the time he made his statement he had not been informed that he was under arrest. The arresting officers’ testimony indicates that the brief stop in the living room before proceeding to the station house was not to interrogate the suspect but to notify his mother of the reason for his arrest. App. 9-10.</p>
<p id="b371-5">The State has conceded the issue of custody and thus we must assume that Burke breached <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>procedures in failing to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before initiating the discussion in the living room. This breach may have been the result of confusion as to whether the brief exchange qualified as “custodial interrogation” or it may simply have reflected Burke’s reluctance to initiate an alarming police <page-number citation-index="1" label="316">*316</page-number>procedure before McAllister had spoken with respondent’s mother. Whatever the reason for Burke’s oversight, the incident had none of the earmarks of coercion. See <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#109" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 109-110</a></span> (1980). Nor did the officers exploit the unwarned admission to pressure respondent into waiving his right to remain silent.</p>
<p id="b372-5">Respondent, however, has argued that he was unable to give a fully <em>informed </em>waiver of his rights because he was unaware that his prior statement could not be used against him. Respondent suggests that Officer McAllister, to cure this deficiency, should have added an additional warning to those given him at the Sheriff’s office. Such a requirement is neither practicable nor constitutionally necessary. In many cases, a breach of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>procedures may not be identified as such until long after full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are administered and a valid confession obtained. See, <em>e. g., United States </em>v. <em>Bowler, </em><span class="citation" data-id="348792"><a href="/opinion/348792/united-states-v-patrick-earl-bowler/#1324" aria-description="Citation for case: United States v. Patrick Earl Bowler">561 F. 2d 1323, 1324-1325</a></span> (CA9 1977) (certain statements ruled inadmissible by trial court); <em>United States </em>v. <em>Toral, </em><span class="citation" data-id="336178"><a href="/opinion/336178/united-states-v-marco-antonio-toral/#896" aria-description="Citation for case: United States v. Marco Antonio Toral">536 F. 2d 893, 896</a></span> (CA9 1976); <em>United States </em>v. <em>Knight, </em><span class="citation" data-id="9453695"><a href="/opinion/280455/united-states-v-richard-s-knight/#974" aria-description="Citation for case: United States v. Richard S. Knight">395 F. 2d 971, 974-975</a></span> (CA2 1968) (custody unclear). The standard <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings explicitly inform the suspect of his right to consult a lawyer before speaking. Police officers are ill-equipped to pinch-hit for counsel, construing the murky and difficult questions of when “custody” begins or whether a given unwarned statement will ultimately be held admissible. See <em>Tanner </em>v. <em>Vincent, </em><span class="citation" data-id="339054"><a href="/opinion/339054/carlson-tanner-jr-v-leon-vincent-warden-of-green-haven-prison/#936" aria-description="Citation for case: Carlson Tanner, Jr. v. Leon Vincent, Warden of Green...">541 F. 2d 932, 936</a></span> (CA2 1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1065/">429 U. S. 1065</a></span> (1977).</p>
<p id="b372-6">This Court has never embraced the theory that a defendant’s ignorance of the full consequences of his decisions vitiates their voluntariness. See <em>California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S., at 1125-1126, n. 3</a></span>; <em>McMann </em>v. <em>Richardson, </em><span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/#769" aria-description="Citation for case: McMann v. Richardson">397 U. S. 759, 769</a></span> (1970). If the prosecution has actually violated the defendant’s Fifth Amendment rights by introducing an inadmissible confession at trial, compelling the defendant to testify in rebuttal, the rule announced in <em>Harrison </em>v. <em>United States, </em><span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/" aria-description="Citation for case: Harrison v. United States">392 U. S. 219</a></span> (1968), precludes use of that testimony <page-number citation-index="1" label="317">*317</page-number>on retrial. “Having ‘released the spring’ by using the petitioner’s unlawfully obtained confessions against him, the Government must show that its illegal action did not induce his testimony.” <span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/#224" aria-description="Citation for case: Harrison v. United States">Id., at 224-225</a></span>. But the Court has refused to find that a defendant who confesses, after being falsely told that his codefendant has turned State’s evidence, does so involuntarily. <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969). The Court has also rejected the argument that a defendant’s ignorance that a prior coerced confession could not be admitted in evidence compromised the voluntariness of his guilty plea. <em>McMann </em>v. <span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/#769" aria-description="Citation for case: McMann v. Richardson"><em>Richardson, supra, </em>at 769</a></span>. Likewise, in <em>California </em>v. <em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">Beheler, supra,</a></span> </em>the Court declined to accept defendant’s contention that, because he was unaware of the potential adverse consequences of statements he made to the police, his participation in the interview was involuntary. Thus we have not held that the <em>sine qua non </em>for a knowing and voluntary waiver of the right to remain silent is a full and complete appreciation of all of the consequences flowing from the nature and the quality of the evidence in the case.</p>
<p id="At24">J — I &lt;1</p>
<p id="Aiu">When police ask questions of a suspect in custody without administering the required warnings, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>dictates that the answers received be presumed compelled and that they be excluded from evidence at trial in the State’s case in chief. The Court has carefully adhered to this principle, permitting a narrow exception only where pressing public safety concerns demanded. See <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#655" aria-description="Citation for case: New York v. Quarles">467 U. S., at 655-656</a></span>. The Court today in no way retreats from the bright-line rule of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>We do not imply that good faith excuses, a failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings; nor do we condone inherently coercive police tactics or methods offensive to due process that render the initial admission involuntary and undermine the suspect’s will to invoke his rights once they are read to him. A handful of courts have, however, applied our precedents relating to confessions ob<page-number citation-index="1" label="318">*318</page-number>tained under coercive circumstances to situations involving wholly voluntary admissions, requiring a passage of time or break in events before a second, fully warned statement can be deemed voluntary. Far from establishing a rigid rule, we direct courts to avoid one; there is no warrant for presuming coercive effect where the suspect’s initial inculpatory statement, though technically in violation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>was voluntary.<footnotemark>5</footnotemark> The relevant inquiry is whether, in fact, the second statement was also voluntarily made. As in any such inquiry, the finder of fact must examine the surrounding circumstances and the entire course of police conduct with respect to the suspect in evaluating the voluntariness of his statements. The fact that a suspect chooses to speak after being informed of his rights is, of course, highly probative. We find that the dictates of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and the goals of the Fifth Amendment proscription against use of compelled testimony are fully satisfied in the circumstances of this case by barring use of the unwarned statement in the case in chief. No further purpose is served by imputing “taint” to subsequent statements obtained pursuant to a voluntary and knowing waiver. We hold today that a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings.</p>
<p id="b374-5">The judgment of the Court of Appeals of Oregon is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b374-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b362-7"> Justice Stevens expresses puzzlement at our statement that a simple failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings is not in itself a violation of the Fifth Amendment. Yet the Court so held in <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 <page-number citation-index="1" label="307">*307</page-number>U. S. 649, 654</a></span> (1983), and <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974). The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court itself recognized this point when it disclaimed any intent to create a “constitutional straitjacket” and invited Congress and the States to suggest “potential alternatives for protecting the privilege.” 384 U. S., at 467. A <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation does not <em>constitute </em>coercion but rather affords a bright-line, legal presumption of coercion, requiring suppression of all unwarned statements. It has never been remotely suggested that any statement taken from Mr. Elstad without benefit of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings would be admissible.</p>
</footnote>
<footnote label="2">
<p id="b366-5"> See, <em>e. g., United States </em>v. <em>Bowler, </em><span class="citation" data-id="348792"><a href="/opinion/348792/united-states-v-patrick-earl-bowler/#1326" aria-description="Citation for case: United States v. Patrick Earl Bowler">561 F. 2d 1323, 1326</a></span> (CA9 1977); <em>Tanner </em>v. <em>Vincent, </em><span class="citation" data-id="339054"><a href="/opinion/339054/carlson-tanner-jr-v-leon-vincent-warden-of-green-haven-prison/" aria-description="Citation for case: Carlson Tanner, Jr. v. Leon Vincent, Warden of Green...">541 F. 2d 932</a></span> (CA2 1976); <em>United States </em>v. <em>Toral, </em><span class="citation" data-id="336178"><a href="/opinion/336178/united-states-v-marco-antonio-toral/#896" aria-description="Citation for case: United States v. Marco Antonio Toral">536 F. 2d 893, 896-897</a></span> (CA9 1976); <em>United States </em>v. <em>Knight, </em><span class="citation" data-id="9453695"><a href="/opinion/280455/united-states-v-richard-s-knight/#975" aria-description="Citation for case: United States v. Richard S. Knight">395 F. 2d 971, 975</a></span> (CA21968); <em>State </em>v. <em>Montes, </em><span class="citation" data-id="1145231"><a href="/opinion/1145231/state-v-montes/#496" aria-description="Citation for case: State v. Montes">136 Ariz. 491,496-497</a></span>, <span class="citation" data-id="1145231"><a href="/opinion/1145231/state-v-montes/#196" aria-description="Citation for case: State v. Montes">667 P. 2d 191,196-197</a></span> (1983); <em>State </em>v. <em>Derrico, </em><span class="citation" data-id="1502926"><a href="/opinion/1502926/state-v-derrico/#166" aria-description="Citation for case: State v. Derrico">181 Conn. 151, 166-167</a></span>, <span class="citation" data-id="1502926"><a href="/opinion/1502926/state-v-derrico/#365" aria-description="Citation for case: State v. Derrico">434 A. 2d 356, 365-366</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/1064/">449 U. S. 1064</a></span> (1980); <em>State </em>v. <em>Holt, </em><span class="citation" data-id="1690277"><a href="/opinion/1690277/state-v-holt/#890" aria-description="Citation for case: State v. Holt">354 So. 2d 888, 890</a></span> (Fla. App.), cert. denied, <span class="citation no-link">361 So. 2d 832</span> (Fla. 1978); <em>Fried </em>v. <em>State, </em><span class="citation" data-id="1496973"><a href="/opinion/1496973/fried-v-state/#644" aria-description="Citation for case: Fried v. State">42 Md. App. 643, 644-648</a></span>, <span class="citation" data-id="1496973"><a href="/opinion/1496973/fried-v-state/#102" aria-description="Citation for case: Fried v. State">402 A. 2d 101, 102-104</a></span> (1979); <em>Commonwealth </em>v. <em>White, </em><span class="citation" data-id="2225068"><a href="/opinion/2225068/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">353 Mass. 409</a></span>, <span class="citation" data-id="2225068"><a href="/opinion/2225068/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">232 N. E. 2d 335</a></span> (1967); <em>State </em>v. <em>Sickels, </em><span class="citation" data-id="1725960"><a href="/opinion/1725960/state-v-sickels/#813" aria-description="Citation for case: State v. Sickels">275 N. W. 2d 809, 813-814</a></span> (Minn. 1979); <em>State </em>v. <em>Dakota, </em><span class="citation" data-id="1837744"><a href="/opinion/1837744/state-v-dakota/" aria-description="Citation for case: State v. Dakota">300 Minn. 12</a></span>, <span class="citation" data-id="1837744"><a href="/opinion/1837744/state-v-dakota/" aria-description="Citation for case: State v. Dakota">217 N. W. 2d 748</a></span> (1974); <em>State </em>v. <em>Raymond, </em><span class="citation" data-id="2012195"><a href="/opinion/2012195/state-v-raymond/#170" aria-description="Citation for case: State v. Raymond">305 Minn. 160,170</a></span>, <span class="citation" data-id="2012195"><a href="/opinion/2012195/state-v-raymond/#886" aria-description="Citation for case: State v. Raymond">232 N. W. 2d 879, 886</a></span> (1975) (noting common thread in line of cases holding prejudicial coercion not present “just because [defendant] had made an earlier confession which ‘let the cat out of the bag’ ”); <em>Commonwealth </em>v. <em>Chacko, </em><span class="citation" data-id="1472767"><a href="/opinion/1472767/commonwealth-v-chacko/#580" aria-description="Citation for case: Commonwealth v. Chacko">500 Pa. 571, 580-582</a></span>, <span class="citation" data-id="1472767"><a href="/opinion/1472767/commonwealth-v-chacko/#316" aria-description="Citation for case: Commonwealth v. Chacko">459 A. 2d 311, 316</a></span> (1983) (“After being given his <em>Miranda </em>warnings it is clear [defendant] maintained his intention to provide his questioners with <page-number citation-index="1" label="311">*311</page-number>his version of the incident”). But see <em>In re Pablo A. C., </em><span class="citation" data-id="9721638"><a href="/opinion/2122160/people-v-pablo-c/" aria-description="Citation for case: People v. Pablo C.">129 Cal. App. 3d 984</a></span>,<span class="citation" data-id="9721638"><a href="/opinion/2122160/people-v-pablo-c/" aria-description="Citation for case: People v. Pablo C.">181 Cal. Rptr. 468</a></span> (1982); <em>State </em>v. <em>Hibdon, </em><span class="citation" data-id="1231742"><a href="/opinion/1231742/state-v-hibdon/" aria-description="Citation for case: State v. Hibdon">57 Ore. App. 509</a></span>, <span class="citation" data-id="1231742"><a href="/opinion/1231742/state-v-hibdon/" aria-description="Citation for case: State v. Hibdon">645 P. 2d 580</a></span> (1982); <em>State </em>v. <em>Lavaris, </em><span class="citation" data-id="1234251"><a href="/opinion/1234251/state-v-lavaris/#857" aria-description="Citation for case: State v. Lavaris">99 Wash. 2d 851, 857-860</a></span>, <span class="citation" data-id="1234251"><a href="/opinion/1234251/state-v-lavaris/#1237" aria-description="Citation for case: State v. Lavaris">664 P. 2d 1234, 1237-1239</a></span> (1983).</p>
</footnote>
<footnote label="3">
<p id="b368-7"> Most of the 50 cases cited by Justice Brennan in his discussion of consecutive confessions concern an initial unwarned statement obtained through overtly or inherently coercive methods which raise serious Fifth Amendment and due process concerns. Without describing each case cited, the following are representative of the situations Justice Brennan views as analogous to this case: <em>e. g., Darwin </em>v. <em>Connecticut, </em><span class="citation" data-id="9423713"><a href="/opinion/107694/darwin-v-connecticut/" aria-description="Citation for case: Darwin v. Connecticut">391 U. S. 346</a></span> (1968) (suspect interrogated for 48 hours incommunicado while officers denied access to counsel); <em>Beecher </em>v. <em>Alabama, </em><span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/#36" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35, 36</a></span> (1967) (officer fired rifle next to suspect’s ear and said “If you don’t tell the truth I am <page-number citation-index="1" label="313">*313</page-number>going to kill you”); <em>Clewis </em>v. <em>Texas, </em><span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707</a></span> (1967) (suspect was arrested without probable cause, interrogated for nine days with little food or sleep, and gave three unwarned “confessions” each of which he immediately retracted); <em>Reck </em>v. <em>Pate, </em><span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#439" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 439-440, n. 3</a></span> (1961) (mentally retarded youth interrogated incommunicado for a week “during which time he was frequently ill, fainted several times, vomited blood on the floor of the police station and was twice taken to the hospital on a stretcher”). Typical of the state cases cited in the dissent’s discussion are: <em>e. g., Cagle </em>v. <em>State, </em><span class="citation" data-id="1635158"><a href="/opinion/1635158/cagle-v-state/#4" aria-description="Citation for case: Cagle v. State">45 Ala. App. 3, 4</a></span>, <span class="citation" data-id="1635158"><a href="/opinion/1635158/cagle-v-state/#120" aria-description="Citation for case: Cagle v. State">221 So. 2d 119, 120</a></span> (1969) (police interrogated wounded suspect at police station for one hour before obtaining statement, took him to hospital to have his severe wounds treated, only then giving the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings; suspect prefaced second statement with “I have already give the Chief a statement and I might as well give one to you, too”), cert. denied, <span class="citation multiple-matches"><a href="/c/Ala./284/727/">284 Ala. 727</a></span>, <span class="citation multiple-matches"><a href="/c/So.%202d/221/121/">221 So. 2d 121</a></span> (1969); <em>People </em>v. <em>Saiz, </em><span class="citation" data-id="9558965"><a href="/opinion/1196896/people-v-saiz/" aria-description="Citation for case: People v. Saiz">620 P. 2d 15</a></span> (Colo. 1980) (two hours’ unwarned custodial interrogation of 16-year-old in violation of state law requiring parent’s presence, culminating in visit to scene of crime); <em>People </em>v. <em>Bodner, </em>75 App. Div. 2d 440, 430 N. Y. S. 2d 433 (1980) (confrontation at police station and at scene of crime between police and retarded youth with mental age of eight or nine); <em>State </em>v. <em>Badger, </em><span class="citation" data-id="2285307"><a href="/opinion/2285307/state-v-badger/#441" aria-description="Citation for case: State v. Badger">141 Vt. 430, 441</a></span>, <span class="citation" data-id="2285307"><a href="/opinion/2285307/state-v-badger/" aria-description="Citation for case: State v. Badger">450 A. 2d 336</a></span>, 343 .(1982) (unwarned “close and intense” station house questioning of 15-year-old, including threats and promises, resulted in confession at 1:20 a. m.; court held “[w]arnings . . . were insufficient to cure such blatant abuse or compensate for the coercion in this case”).</p>
<p id="b369-6">Justice Brennan cannot seriously mean to equate such situations with the case at bar. Likewise inapposite are the cases the dissent cites concerning suspects whose invocation of their rights to remain silent and to have counsel present were flatly ignored while police subjected them to continued interrogation. See, <em>e. g., United States ex rel. Sanders </em>v. <em>Rowe, </em><span class="citation" data-id="2093616"><a href="/opinion/2093616/united-states-ex-rel-sanders-v-rowe/" aria-description="Citation for case: United States Ex Rel. Sanders v. Rowe">460 F. Supp. 1128</a></span> (ND Ill. 1978); <em>People </em>v. <em>Braeseke, </em><span class="citation" data-id="9578828"><a href="/opinion/1320417/people-v-braeseke/" aria-description="Citation for case: People v. Braeseke">25 Cal. 3d 691</a></span>, <span class="citation" data-id="9578828"><a href="/opinion/1320417/people-v-braeseke/" aria-description="Citation for case: People v. Braeseke">602 P. 2d 384</a></span> (1979), vacated on other grounds, <span class="citation multiple-matches"><a href="/c/U.%20S./446/932/">446 U. S. 932</a></span> (1980); <em>Smith </em>v. <em>State, </em><span class="citation" data-id="1306478"><a href="/opinion/1306478/smith-v-state/" aria-description="Citation for case: Smith v. State">132 Ga. App. 491</a></span>, <span class="citation" data-id="1306478"><a href="/opinion/1306478/smith-v-state/" aria-description="Citation for case: Smith v. State">208 S. E. 2d 351</a></span> (1974). Finally, many of the decisions Justice Brennan claims require that the “taint” be “dissipated” simply recite the stock “cat” and “tree” metaphors but go on to find the second confession voluntary without identifying any break in the stream of events beyond the simple administration of a careful and thorough warning. See cases cited in n. 2, <em>supra.</em></p>
<p id="b369-7">Out of the multitude of decisions Justice Brennan cites, no more than half a dozen fairly can be said to suppress confessions on facts remotely <page-number citation-index="1" label="314">*314</page-number>comparable to those in the instant case, and some of these decisions involved other elements not present here. See <em>United States </em>v. <em>Pierce, </em><span class="citation" data-id="9453756"><a href="/opinion/280782/united-states-v-thomas-michael-pierce/" aria-description="Citation for case: United States v. Thomas Michael Pierce">397 F. 2d 128</a></span> (CA4 1968) (thorough custodial interrogation at station house); <em>United States </em>v. <em>Pellegrini, </em><span class="citation" data-id="2096024"><a href="/opinion/2096024/united-states-v-pellegrini/#257" aria-description="Citation for case: United States v. Pellegrini">309 F. Supp. 250, 257</a></span> (SDNY 1970) (officers induced unwarned suspect to produce “the clinching evidence of his crime”); <em>In re Pablo A. C., </em><span class="citation" data-id="9721638"><a href="/opinion/2122160/people-v-pablo-c/" aria-description="Citation for case: People v. Pablo C.">129 Cal. App. 3d 984</a></span>, <span class="citation" data-id="9721638"><a href="/opinion/2122160/people-v-pablo-c/" aria-description="Citation for case: People v. Pablo C.">181 Cal. Rptr. 468</a></span> (1982) (25-minute interrogation of juvenile; court finds causal connection but notes that all prior cited eases relying on “cat-out-of-bag” theory have involved coercion); <em>State </em>v. <em>Lekas, </em><span class="citation" data-id="9542762"><a href="/opinion/1161498/state-v-lekas/" aria-description="Citation for case: State v. Lekas">201 Kan. 579</a></span>, <span class="citation" data-id="9542762"><a href="/opinion/1161498/state-v-lekas/" aria-description="Citation for case: State v. Lekas">442 P. 2d 11</a></span> (1968) (parolee taken into custody and questioned at courthouse). At least one State Supreme Court cited by Justice Brennan that read <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>as mandating suppression of a subsequent voluntary and fully warned confession did so with express reluctance, convinced that admissibility of a subsequent confession should turn on voluntariness alone. See <em>Brunson </em>v. <em>State, </em><span class="citation" data-id="1724789"><a href="/opinion/1724789/brunson-v-state/#819" aria-description="Citation for case: Brunson v. State">264 So. 2d 817, 819-820</a></span> (Miss. 1972).</p>
</footnote>
<footnote label="4">
<p id="b371-6"> The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>advice on the card was clear and comprehensive, incorporating the warning that any statements could be used in a court of law; the rights to remain silent, consult an attorney at state expense, and interrupt the conversation at any time; and the reminder that any statements must be voluntary. The reverse side of the card carried three questions in boldface and recorded Elstad’s responses:</p>
<blockquote id="b371-7">“DO YOU UNDERSTAND THESE RIGHTS? ‘Yeh’</blockquote>
<blockquote id="b371-8">“DO YOU HAVE ANY QUESTIONS ABOUT YOUR RIGHTS? ‘No’ “HAVING THESE RIGHTS IN MIND, DO YOU WISH TO TALK TO US NOW? ‘Yeh I do!”’</blockquote>
<p id="b371-9">The card is dated and signed by respondent and by Officer McAllister. A recent high school graduate, Elstad was fully capable of understanding this careful administering of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings.</p>
</footnote>
<footnote label="5">
<p id="b374-9"> Justice Brennan, with an apocalyptic tone, heralds this opinion as dealing a “crippling blow to <em>Miranda.’’ Post, </em>at 319. Justice Brennan not only distorts the reasoning and holding of our decision, but, worse, invites trial courts and prosecutors to do the same.</p>
</footnote>
</opinion>
```

---
