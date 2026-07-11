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

## GROUP: _overhaul2/lake/cases/District of Columbia v. Wesby.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "District of Columbia v. Wesby"
type: case
citation: "583 U.S. 48 (2018)"
parallel_cite: "138 S. Ct. 577; 199 L. Ed. 2d 453"
neutral_cite: 2018 U.S. LEXIS 760
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-01-22
docket: 15-1485
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-01-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: District of Columbia v. Wesby
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4460854/district-of-columbia-v-wesby/"
  cluster_id: 4460854
  opinion_id: 4238107
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Gates]]", "[[Maryland v. Pringle]]", "[[Devenpeck v. Alford]]", "[[Brinegar v. United States]]"]
aliases: ["DC v. Wesby"]
tags: ["case", "fourth-amendment", "probable-cause", "totality-of-the-circumstances", "qualified-immunity"]
holding: "Probable cause is a totality inquiry; courts must not divide-and-conquer the facts."
lake:
  record_id: District of Columbia v. Wesby
  status: verified
  projected_at: 2026-07-06
---

# District of Columbia v. Wesby

*583 U.S. 48 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers found a raucous late-night party in a house that neighbors reported should be vacant; the partygoers gave conflicting and implausible accounts of who invited them, and the purported host ("Peaches") admitted by phone she had no permission to use the house. Officers arrested the guests for unlawful entry. The arrestees sued under § 1983, and the D.C. Circuit held the officers lacked probable cause and [[Qualified Immunity|qualified immunity]].

## Issue
Whether officers had probable cause to arrest the partygoers for unlawful entry, judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] rather than fact-by-fact.

## Rule
Yes; probable cause is a totality inquiry and courts may not divide and conquer the facts. "In concluding otherwise, the panel majority engaged in an 'excessively technical dissection' of the factors supporting probable cause." — *District of Columbia v. Wesby*, 583 U.S. 48 (2018) (slip op., at 11). ^pin-op11

The panel erred by "view[ing] each fact 'in isolation, rather than as a factor in the totality of the circumstances.'" — *Id.* ^pin-op11a

## Application
Viewed as a whole — a vacant-looking house, a chaotic party, guests scattering and giving evasive, inconsistent stories about permission, and the supposed host conceding she had none — the circumstances gave a reasonable officer probable cause to believe the partygoers knew they were there unlawfully. Assessing each fact in isolation, as the panel did, was the wrong method; on the totality, probable cause existed (and the officers also had [[Qualified Immunity|qualified immunity]]).

## Conclusion
The officers had probable cause to arrest, and were in any event entitled to [[Qualified Immunity|qualified immunity]]; the judgment against them was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Wesby* reaffirms the totality-of-the-circumstances standard of [[Illinois v. Gates]] and [[Maryland v. Pringle]], rejecting divide-and-conquer analysis of probable cause.

## Appears on
- [[Probable Cause]] — *Key — Progeny / Refinement*

## Sources
- *District of Columbia v. Wesby*, 583 U.S. 48 (2018) — https://www.courtlistener.com/opinion/4460854/district-of-columbia-v-wesby/ — pinpoint: slip op., at 11 (CL carries the slip opinion; cluster 4460854 → opinion 4238107).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b6462c581d95d2e6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "District of Columbia v. Wesby"}, "payload": {"all": [{"cite": "583 U.S. 48", "page": "48", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "583"}, {"cite": "138 S. Ct. 577", "page": "577", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "138"}, {"cite": "199 L. Ed. 2d 453", "page": "453", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "199"}, {"cite": "2018 U.S. LEXIS 760", "page": "760", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2018"}], "display": "583 U.S. 48", "official": {"cite": "583 U.S. 48", "page": "48", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "583"}, "official_selection_present": true, "record_id": "District of Columbia v. Wesby"}}
{"assertion_id": "7758b0a614feb2f5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op11a", "record_id": "District of Columbia v. Wesby"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op11a", "pinpoint_status": "slip-only", "quote": "view[ing] each fact 'in isolation, rather than as a factor in the totality of the circumstances.'", "quote_fidelity": "mismatch", "record_id": "District of Columbia v. Wesby", "star_marker": null}}
{"assertion_id": "d8734bbfcd1f8caa", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op11", "record_id": "District of Columbia v. Wesby"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op11", "pinpoint_status": "slip-only", "quote": ") admitted by phone she had no permission to use the house. Officers arrested the guests for unlawful entry. The arrestees sued under § 1983, and the D.C. Circuit held the officers lacked probable cause and qualified immunity. ## Issue Whether officers had probable cause to arrest the partygoers for unlawful entry, judged on the totality of the circumstances rather than fact-by-fact. ## Rule Yes; probable cause is a totality inquiry and courts may not divide and conquer the facts.", "quote_fidelity": "mismatch", "record_id": "District of Columbia v. Wesby", "star_marker": null}}
{"assertion_id": "e9855256e4bdb8da", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "District of Columbia v. Wesby"}, "payload": {"as_of_content": "2018-01-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "District of Columbia v. Wesby", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — District of Columbia v. Wesby

```json
{
  "schema_version": "s2.v1",
  "record_id": "District of Columbia v. Wesby",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "District of Columbia v. Wesby",
    "case_name_short": "Wesby",
    "case_name_full": "",
    "input_case_name": "District of Columbia v. Wesby",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-01-22",
    "year": 2018,
    "docket": "15-1485",
    "cluster_id": 4460854,
    "lead_opinion_id": 4238107,
    "sibling_ids": [
      4238107
    ],
    "absolute_url": "/opinion/4460854/district-of-columbia-v-wesby/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4460853,
        "score": 120,
        "case_name": "District of Columbia v. Wesby"
      },
      {
        "cluster_id": 4460811,
        "score": 120,
        "case_name": "District of Columbia v. Wesby"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "583 U.S. 48",
      "volume": "583",
      "reporter": "U.S.",
      "page": "48",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 577",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "577",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "199 L. Ed. 2d 453",
        "volume": "199",
        "reporter": "L. Ed. 2d",
        "page": "453",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 760",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "760",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "583 U.S. 48",
        "volume": "583",
        "reporter": "U.S.",
        "page": "48",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 577",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "577",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "199 L. Ed. 2d 453",
        "volume": "199",
        "reporter": "L. Ed. 2d",
        "page": "453",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 760",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "760",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "583 U.S. 48",
    "official_selection": {
      "court_class": "scotus",
      "selected": "583 U.S. 48",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op11",
      "page": null,
      "quote": ") admitted by phone she had no permission to use the house. Officers arrested the guests for unlawful entry. The arrestees sued under \u00a7 1983, and the D.C. Circuit held the officers lacked probable cause and qualified immunity. ## Issue Whether officers had probable cause to arrest the partygoers for unlawful entry, judged on the totality of the circumstances rather than fact-by-fact. ## Rule Yes; probable cause is a totality inquiry and courts may not divide and conquer the facts.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op11a",
      "page": null,
      "quote": "view[ing] each fact 'in isolation, rather than as a factor in the totality of the circumstances.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-01-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "District of Columbia v. Wesby",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Mickel",
          "cluster_id": 10680424,
          "cite": [
            "321 Ga. 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The State of Texas v. Christian Bruce Gonzales",
          "cluster_id": 9433471,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Torres",
          "cluster_id": 9381469,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ana Sandoval v. County of San Diego",
          "cluster_id": 4847368,
          "cite": [
            "985 F.3d 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
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
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffery Mays v. Ronald Sprinkle",
          "cluster_id": 4869132,
          "cite": [
            "992 F.3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kee v. City of New York",
          "cluster_id": 5064686,
          "cite": [
            "12 F.4th 150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
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
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
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
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
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
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kathy Dyer v. City of Mesquite Texas",
          "cluster_id": 4765962,
          "cite": [
            "964 F.3d 374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Feminist Majority Foundation v. Richard Hurley",
          "cluster_id": 4574853,
          "cite": [
            "911 F.3d 674"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darnell Hines v. Ashrafe Youseff",
          "cluster_id": 4586720,
          "cite": [
            "914 F.3d 1218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raheem Jacobs v. Cumberland County",
          "cluster_id": 4906491,
          "cite": [
            "8 F.4th 187"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Calvin Dibrell v. City of Knoxville, Tenn.",
          "cluster_id": 4846329,
          "cite": [
            "984 F.3d 1156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kevin Lipman v. Armond Budish",
          "cluster_id": 4782865,
          "cite": [
            "974 F.3d 726"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
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
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Botts",
          "cluster_id": 4495354,
          "cite": [
            "299 Neb. 806",
            "910 N.W.2d 779"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
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
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
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
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry Smith, Jr. v. Melvin Finkley",
          "cluster_id": 4970388,
          "cite": [
            "10 F.4th 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crowson v. Washington County State, Utah",
          "cluster_id": 4843706,
          "cite": [
            "983 F.3d 1166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sachin Gupta v. Chad Melloh",
          "cluster_id": 5303583,
          "cite": [
            "19 F.4th 990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
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
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vivianne Jade Washington v. Investigator Hugh Howard",
          "cluster_id": 6347134,
          "cite": [
            "25 F.4th 891"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Seckinger",
          "cluster_id": 4577639,
          "cite": [
            "301 Neb. 963",
            "920 N.W.2d 842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate of Seth Michael Zakora v. Troy Chrisman",
          "cluster_id": 7855600,
          "cite": [
            "44 F.4th 452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bretton Westmoreland v. Butler Cnty.",
          "cluster_id": 6454550,
          "cite": [
            "29 F.4th 721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "District of Columbia v. Wesby:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4238107) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjMwMDIyNDAwMDAwJnM9NTA2NDI5MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%284238107%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(4238107)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTEmcz00NzI1NzgzJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%284238107%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4238107)",
        "reviewed": 59,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 59,
        "triage_read": 3,
        "triage_snippet_classified": 56
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4238107)",
    "indexed_citing_opinions": 521,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4238107,
        "count": 521,
        "count_source": "search"
      }
    ],
    "citation_count": 2467,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/district-of-columbia-v-wesby.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NzE2NjImcz05NDc2MjI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284238107%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4238107,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 118474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 131150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 137733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 145908,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 160847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 201366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 217512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 217703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 221236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 518124,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 543224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 672041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 1227729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 2303533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4238107,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T02:34:44Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:35:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:35:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:40:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:35:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — District of Columbia v. Wesby

```
(Slip Opinion)              OCTOBER TERM, 2017                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

     DISTRICT OF COLUMBIA ET AL. v. WESBY ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
          THE DISTRICT OF COLUMBIA CIRCUIT

   No. 15–1485. Argued October 4, 2017—Decided January 22, 2018
District of Columbia police officers responded to a complaint about loud
  music and illegal activities in a vacant house. Inside, they found the
  house nearly barren and in disarray. The officers smelled marijuana
  and observed beer bottles and cups of liquor on the floor, which was
  dirty. They found a make-shift strip club in the living room, and a
  naked woman and several men in an upstairs bedroom. Many party-
  goers scattered when they saw the uniformed officers, and some
  hid. The officers questioned everyone and got inconsistent stories.
  Two women identified “Peaches” as the house’s tenant and said that
  she had given the partygoers permission to have the party. But
  Peaches was not there. When the officers spoke by phone to Peaches,
  she was nervous, agitated, and evasive. At first, she claimed that she
  was renting the house and had given the partygoers permission to
  have the party, but she eventually admitted that she did not have
  permission to use the house. The owner confirmed that he had not
  given anyone permission to be there. The officers then arrested the
  partygoers for unlawful entry.
    Several partygoers sued for false arrest under the Fourth Amend-
  ment and District law. The District Court concluded that the officers
  lacked probable cause to arrest the partygoers for unlawful entry and
  that two of the officers, petitioners here, were not entitled to qualified
  immunity. A divided panel of the D. C. Circuit affirmed.
Held:
    1. The officers had probable cause to arrest the partygoers. Pp. 7–
 13.
       (a) Considering the “totality of the circumstances,” Maryland v.
 Pringle, 540 U. S. 366, 371, the officers made an “entirely reasonable
 inference” that the partygoers knew they did not have permission to
2                  DISTRICT OF COLUMBIA v. WESBY

                                   Syllabus

    be in the house, id., at 372. Taken together, the condition of the
    house and the conduct of the partygoers allowed the officers to make
    several “ ‘common-sense conclusions about human behavior.’ ” Illinois
    v. Gates, 462 U. S. 213, 231. Because most homeowners do not live in
    such conditions or permit such activities in their homes, the officers
    could infer that the partygoers knew the party was not authorized.
    The officers also could infer that the partygoers knew that they were
    not supposed to be in the house because they scattered and hid when
    the officers arrived. See Illinois v. Wardlow, 528 U. S. 119, 124–125.
    The partygoers’ vague and implausible answers to questioning also
    gave the officers reason to infer that the partygoers were lying and
    that their lies suggested a guilty mind. Cf. Devenpeck v. Alford, 543
    U. S. 146, 149, 155–156. Peaches’ lying and evasive behavior gave
    the officers reason to discredit everything she said. The officers also
    could have inferred that she lied when she said she had invited the
    partygoers to the house, or that she told the partygoers that she was
    not actually renting the house. Pp. 7–11.
          (b) The panel majority failed to follow two basic and well-
    established principles of law. First, it viewed each fact “in isolation,
    rather than as a factor in the totality of the circumstances.” Pringle,
    supra, at 372, n. 2. Second, it believed that it could dismiss outright
    any circumstances that were “susceptible of innocent explanation,”
    United States v. Arvizu, 534 U. S. 266, 277. Instead, it should have
    asked whether a reasonable officer could conclude—considering all of
    the surrounding circumstances, including the plausibility of the ex-
    planation itself—that there was a “substantial chance of criminal ac-
    tivity,” Gates, supra, at 244, n. 13. Pp. 11–13.
       2. The officers are entitled to qualified immunity. Pp. 13–19.
          (a) As relevant here, officers are entitled to qualified immunity
    under 42 U. S. C. §1983 unless the unlawfulness of their conduct was
    “clearly established at the time,” Reichle v. Howards, 566 U. S. 658,
    664. To be clearly established, a legal principle must be “settled law,”
    Hunter v. Bryant, 502 U. S. 224, 228, and it must clearly prohibit the
    officer’s conduct in the particular circumstances before him, see
    Saucier v. Katz, 533 U. S. 194, 202. In the warrantless arrest con-
    text, “a body of relevant case law” is usually necessary to “ ‘clearly es-
    tablish’ the answer” with respect to probable cause. Brosseau v.
    Haugen, 543 U. S. 194, 199.
       Even assuming that the officers lacked actual probable cause to ar-
    rest the partygoers, they are entitled to qualified immunity because,
    given “the circumstances with which [they] w[ere] confronted,” they
    “reasonably but mistakenly conclude[d] that probable cause [wa]s
    present.” Anderson v. Creighton, 483 U. S. 635, 640, 641. The panel
    majority and the partygoers have failed to identify a single precedent
                      Cite as: 583 U. S. ____ (2018)                      3

                                 Syllabus

  finding a Fourth Amendment violation “under similar circumstanc-
  es.” White v. Pauly, 580 U. S. ___, ___. And this is not an “obvious
  case” where “a body of relevant case law” is unnecessary. Brosseau,
  supra, at 199. Pp. 13–16.
       (b) Instead of following this straightforward analysis, the panel
  majority reasoned that, under clearly established District law, a sus-
  pect’s bona fide belief of a right to enter vitiates probable cause to ar-
  rest for unlawful entry. Thus, it concluded that the “uncontroverted
  evidence” of an invitation in this case meant that the officers could
  not infer the partygoers’ intent from other circumstances or disbe-
  lieve their story. But looking at the entire legal landscape at the
  time of the arrests, a reasonable officer could have interpreted the
  law as permitting the arrests here. There was no controlling case
  holding that a bona fide belief of a right to enter defeats probable
  cause, that officers cannot infer a suspect’s guilty state of mind based
  on his conduct alone, or that officers must accept a suspect’s innocent
  explanation at face value. And several precedents suggested the op-
  posite. Pp. 16–19.
765 F. 3d 13, reversed and remanded.

  THOMAS, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, BREYER, ALITO, KAGAN, and GORSUCH, JJ., joined.
SOTOMAYOR, J., filed an opinion concurring in part and concurring in
the judgment. GINSBURG, J., filed an opinion concurring in the judg-
ment in part.
                       Cite as: 583 U. S. ____ (2018)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 15–1485
                                  _________________


  DISTRICT OF COLUMBIA, ET AL., PETITIONERS v.

            THEODORE WESBY, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

    APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT

                              [January 22, 2018]


   JUSTICE THOMAS delivered the opinion of the Court.
   This case involves a civil suit against the District of
Columbia and five of its police officers, brought by 16
individuals who were arrested for holding a raucous, late-
night party in a house they did not have permission to
enter. The United States Court of Appeals for the District
of Columbia Circuit held that there was no probable cause
to arrest the partygoers, and that the officers were not
entitled to qualified immunity. We reverse on both
grounds.
                             I
  Around 1 a.m. on March 16, 2008, the District’s Metro-
politan Police Department received a complaint about loud
music and illegal activities at a house in Northeast D. C.
The caller, a former neighborhood commissioner, told
police that the house had been vacant for several months.
When officers arrived at the scene, several neighbors
confirmed that the house should have been empty. The
officers approached the house and, consistent with the
complaint, heard loud music playing inside.
  After the officers knocked on the front door, they saw a
2             DISTRICT OF COLUMBIA v. WESBY

                      Opinion of the Court

man look out the window and then run upstairs. One of
the partygoers opened the door, and the officers entered.
They immediately observed that the inside of the house
“ ‘was in disarray’ ” and looked like “ ‘a vacant property.’ ”
841 F. Supp. 2d 20, 31 (DC 2012) (quoting Defs. Exh. A).
The officers smelled marijuana and saw beer bottles and
cups of liquor on the floor. In fact, the floor was so dirty
that one of the partygoers refused to sit on it while being
questioned. Although the house had working electricity
and plumbing, it had no furniture downstairs other than a
few padded metal chairs. The only other signs of habita-
tion were blinds on the windows, food in the refrigerator,
and toiletries in the bathroom.
   In the living room, the officers found a makeshift strip
club. Several women were wearing only bras and thongs,
with cash tucked into their garter belts. The women were
giving lap dances while other partygoers watched. Most of
the onlookers were holding cash and cups of alcohol. After
seeing the uniformed officers, many partygoers scattered
into other parts of the house.
   The officers found more debauchery upstairs. A naked
woman and several men were in the bedroom. A bare
mattress—the only one in the house—was on the floor,
along with some lit candles and multiple open condom
wrappers. A used condom was on the windowsill. The
officers found one partygoer hiding in an upstairs closet,
and another who had shut himself in the bathroom and
refused to come out.
   The officers found a total of 21 people in the house.
After interviewing all 21, the officers did not get a clear or
consistent story. Many partygoers said they were there
for a bachelor party, but no one could identify the bache-
lor. Each of the partygoers claimed that someone had
invited them to the house, but no one could say who. Two
of the women working the party said that a woman named
“Peaches” or “Tasty” was renting the house and had given
                    Cite as: 583 U. S. ____ (2018)                   3

                         Opinion of the Court

them permission to be there. One of the women explained
that the previous owner had recently passed away, and
Peaches had just started renting the house from the
grandson who inherited it. But the house had no boxes or
moving supplies. She did not know Peaches’ real name.
And Peaches was not there.
  An officer asked the woman to call Peaches on her
phone so he could talk to her. Peaches answered and
explained that she had just left the party to go to the
store. When the officer asked her to return, Peaches
refused because she was afraid of being arrested. The
sergeant supervising the investigation also spoke with
Peaches. At first, Peaches claimed to be renting the house
from the owner, who was fixing it up for her. She also said
that she had given the attendees permission to have the
party. When the sergeant again asked her who had given
her permission to use the house, Peaches became evasive
and hung up. The sergeant called her back, and she began
yelling and insisting that she had permission before hang-
ing up a second time. The officers eventually got Peaches
on the phone again, and she admitted that she did not
have permission to use the house.
  The officers then contacted the owner. He told them
that he had been trying to negotiate a lease with Peaches,
but they had not reached an agreement. He confirmed
that he had not given Peaches (or anyone else) permission
to be in the house—let alone permission to use it for a
bachelor party. At that point, the officers arrested the 21
partygoers for unlawful entry. See D. C. Code §22–3302
(2008). The police transported the partygoers to the police
station, where the lieutenant decided to charge them with
disorderly conduct. See §22–1321. The partygoers were
released, and the charges were eventually dropped.1
——————
  1 In their merits brief, the partygoers attempt to dispute several of

these facts. See Brief for Respondents 26–30. But the facts they now
4                DISTRICT OF COLUMBIA v. WESBY

                          Opinion of the Court

                              II
  Respondents, 16 of the 21 partygoers, sued the District
and five of the arresting officers. They sued the officers
for false arrest under the Fourth Amendment, Rev. Stat.
§1979, 42 U. S. C. §1983, and under District law. They
sued the District for false arrest and negligent supervision
under District law. The partygoers’ claims were all “pred-
icated upon the allegation that [they] were arrested with-
out probable cause.” 841 F. Supp. 2d, at 32.
  On cross-motions for summary judgment, the District
Court awarded partial summary judgment to the party-
goers. Id., at 48–49. It concluded that the officers lacked
probable cause to arrest the partygoers for unlawful en-
try.2 Id., at 32–33. The officers were told that Peaches
had invited the partygoers to the house, the District Court
reasoned, and nothing the officers learned in their investi-
gation suggested the partygoers “ ‘knew or should have
known that [they were] entering against the [owner’s]
will.’ ” Id., at 32. The District Court also concluded that
the officers were not entitled to qualified immunity under
——————
contest were presented in the petition for a writ of certiorari, and the
partygoers did not contest them in their brief in opposition. Under this
Court’s Rule 15.2, the partygoers’ failure to contest these factual
assertions at the certiorari stage waived their right to do so at the
merits stage. See Carcieri v. Salazar, 555 U. S. 379, 395–396 (2009).
   Furthermore, although both parties moved for summary judgment,
the undisputed facts here are sufficient to resolve both probable cause
and qualified immunity. Our analysis thus would not change no matter
which party is considered the moving party. Cf. Scott v. Harris, 550
U. S. 372, 378–379 (2007) (explaining that, at summary judgment,
courts must view the facts and draw reasonable inferences in favor of
the nonmoving party).
   2 Because probable cause is an objective standard, an arrest is lawful

if the officer had probable cause to arrest for any offense, not just the
offense cited at the time of arrest or booking. See Devenpeck v. Alford,
543 U. S. 146, 153–155, and n. 2 (2004). Because unlawful entry is the
only offense that the District and its officers discuss in their briefs to
this Court, we likewise limit our analysis to that offense.
                    Cite as: 583 U. S. ____ (2018)                 5

                        Opinion of the Court

§1983.3 It noted that, under District case law, “probable
cause to arrest for unlawful entry requires evidence that
the alleged intruder knew or should have known, upon
entry, that such entry was against the will of the owner.”
Id., at 37. And in its view, the officers had no such evi-
dence. Id., at 32–33, 37–38.
   With liability resolved, the case proceeded to trial on
damages. The jury awarded the partygoers a total of
$680,000 in compensatory damages. After the District
Court awarded attorney’s fees, the total award was nearly
$1 million.
   On appeal, a divided panel of the D. C. Circuit affirmed.
On the question of probable cause, the panel majority
made Peaches’ invitation “central” to its determination
that the officers lacked probable cause to arrest the party-
goers for unlawful entry. 765 F. 3d 13, 21 (2014). The
panel majority asserted that, “in the absence of any con-
flicting information, Peaches’ invitation vitiates the neces-
sary element of [the partygoers’] intent to enter against
the will of the lawful owner.” Ibid. And the panel major-
ity determined that “there is simply no evidence in the
record that [the partygoers] had any reason to think the
invitation was invalid.” Ibid.
   On the question of qualified immunity, the panel major-
ity determined that it was “perfectly clear” that a person
with “a good purpose and bona fide belief of her right to
enter” lacks the necessary intent for unlawful entry. Id.,
at 27. In other words, the officers needed “some evidence”
that the partygoers “knew or should have known they
were entering against the will of the lawful owner.” Ibid.
——————
   3 The District Court granted summary judgment against two of the

officers, but denied summary judgment against the other three because
there were triable issues regarding qualified immunity. See 841
F. Supp. 2d 20, 32–46 (DC 2012). The partygoers voluntarily dismissed
their claims against those three officers. See 765 F. 3d 13, 17 (CADC
2014).
6             DISTRICT OF COLUMBIA v. WESBY

                     Opinion of the Court

And here, the panel majority asserted, the officers must
“have known that uncontroverted evidence of an invitation
to enter the premises would vitiate probable cause for
unlawful entry.” Ibid.
   Judge Brown dissented. She concluded that summary
judgment on the false-arrest claims was improper because,
under the totality of the circumstances, a reasonable
officer “could disbelieve [the partygoers’] claim of innocent
entry” and infer that they knew or should have known
that they did not have permission to be in the house. Id.,
at 34. She also disagreed with the denial of qualified
immunity, contending that a reasonable officer could have
found probable cause to arrest in this “unusual factual
scenario, not well represented in the controlling case law.”
Id., at 36.
   The D. C. Circuit denied rehearing en banc over the
dissent of four judges. The dissenters focused on qualified
immunity, contending that the panel opinion “contra-
vene[d] . . . emphatic Supreme Court directives” that
“police officers may not be held liable for damages unless
the officers were ‘plainly incompetent’ or ‘knowingly vio-
late[d]’ clearly established law.” 816 F. 3d 96, 102 (2016)
(quoting Carroll v. Carman, 574 U. S. ___, ___ (2014) ( per
curiam) (slip op., at 4)). The panel majority— Judges
Pillard and Edwards—responded in a joint concurrence.
816 F. 3d, at 96–101. They insisted that the panel opinion
did not misapply the law of qualified immunity, and that
their disagreement with the dissenters was a mere “case-
specific assessment of the circumstantial evidence in the
record.” Id., at 100.
   We granted certiorari to resolve two questions: whether
the officers had probable cause to arrest the partygoers,
and whether the officers were entitled to qualified immun-
ity. See 580 U. S. ___ (2017). We address each question in
turn.
                  Cite as: 583 U. S. ____ (2018)            7

                      Opinion of the Court 


                               III

   The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.”
Because arrests are “seizures” of “persons,” they must be
reasonable under the circumstances. See Payton v. New
York, 445 U. S. 573, 585 (1980). A warrantless arrest is
reasonable if the officer has probable cause to believe that
the suspect committed a crime in the officer’s presence.
Atwater v. Lago Vista, 532 U. S. 318, 354 (2001).
   To determine whether an officer had probable cause for
an arrest, “we examine the events leading up to the arrest,
and then decide ‘whether these historical facts, viewed
from the standpoint of an objectively reasonable police
officer, amount to’ probable cause.” Maryland v. Pringle,
540 U. S. 366, 371 (2003) (quoting Ornelas v. United
States, 517 U. S. 690, 696 (1996)). Because probable cause
“deals with probabilities and depends on the totality of the
circumstances,” 540 U. S., at 371, it is “a fluid concept”
that is “not readily, or even usefully, reduced to a neat set
of legal rules,” Illinois v. Gates, 462 U. S. 213, 232 (1983).
It “requires only a probability or substantial chance of
criminal activity, not an actual showing of such activity.”
Id., at 243–244, n. 13 (1983). Probable cause “is not a high
bar.” Kaley v. United States, 571 U. S. ___, ___ (2014) (slip
op., at 18).
                            A
   There is no dispute that the partygoers entered the
house against the will of the owner. Nonetheless, the
partygoers contend that the officers lacked probable cause
to arrest them because the officers had no reason to be-
lieve that they “knew or should have known” their “entry
was unwanted.” Ortberg v. United States, 81 A. 3d 303,
308 (D. C. 2013). We disagree. Considering the totality of
the circumstances, the officers made an “entirely reason-
8               DISTRICT OF COLUMBIA v. WESBY

                          Opinion of the Court

able inference” that the partygoers were knowingly taking
advantage of a vacant house as a venue for their late-night
party. Pringle, supra, at 372.
  Consider first the condition of the house. Multiple
neighbors, including a former neighborhood official, in-
formed the officers that the house had been vacant for
several months.4 The house had no furniture, except for a
few padded metal chairs and a bare mattress. The rest of
the house was empty, save for some fixtures and large
appliances. The house had a few signs of inhabitance—
working electricity and plumbing, blinds on the windows,
toiletries in the bathroom, and food in the refrigerator.
But those facts are not necessarily inconsistent with the
house being unoccupied. The owner could have paid the
utilities and kept the blinds while he looked for a new
tenant, and the partygoers could have brought the food
and toiletries. Although one woman told the officers that
Peaches had recently moved in, the officers had reason to
doubt that was true. There were no boxes or other moving
supplies in the house; nor were there other possessions,
such as clothes in the closet, suggesting someone lived
there.
  In addition to the condition of the house, consider the
partygoers’ conduct. The party was still going strong
when the officers arrived after 1 a.m., with music so loud
that it could be heard from outside. Upon entering the
house, multiple officers smelled marijuana.5 The party-
——————
  4 At oral argument, the partygoers argued that the house was not

formally “vacant” under District law. Tr. of Oral Arg. 34. But a rea-
sonable officer could infer that the complaining neighbors used the
term “vacant” in the colloquial, not the legal, sense.
  5 The panel majority dismissed this fact because the officers “did not

see any evidence of drugs” and did “not attempt to justify [the] arrests”
based on drug use. 765 F. 3d, at 23, n. 5. But a reasonable officer could
infer, based on the smell, that marijuana had been used in the house.
See Johnson v. United States, 333 U. S. 10, 13 (1948) (noting that “the
odor” of narcotics can “be evidence of the most persuasive character”).
                    Cite as: 583 U. S. ____ (2018)                 9

                        Opinion of the Court

goers left beer bottles and cups of liquor on the floor, and
they left the floor so dirty that one of them refused to sit
on it. The living room had been converted into a make-
shift strip club. Strippers in bras and thongs, with cash
stuffed in their garter belts, were giving lap dances. Up-
stairs, the officers found a group of men with a single,
naked woman on a bare mattress—the only bed in the
house—along with multiple open condom wrappers and a
used condom.
   Taken together, the condition of the house and the
conduct of the partygoers allowed the officers to make
several “ ‘common-sense conclusions about human behav-
ior.’ ” Gates, supra, at 231 (quoting United States v. Cor-
tez, 449 U. S. 411, 418 (1981)). Most homeowners do not
live in near-barren houses. And most homeowners do not
invite people over to use their living room as a strip club,
to have sex in their bedroom, to smoke marijuana inside,
and to leave their floors filthy.        The officers could
thus infer that the partygoers knew their party was not
authorized.
   The partygoers’ reaction to the officers gave them fur-
ther reason to believe that the partygoers knew they
lacked permission to be in the house. Many scattered at
the sight of the uniformed officers. Two hid themselves,
one in a closet and the other in a bathroom.
“[U]nprovoked flight upon noticing the police,” we have
explained, “is certainly suggestive” of wrongdoing and can
be treated as “suspicious behavior” that factors into the
totality of the circumstances. Illinois v. Wardlow, 528
U. S. 119, 124–125 (2000). In fact, “deliberately furtive
actions and flight at the approach of . . . law officers are
strong indicia of mens rea.” Sibron v. New York, 392 U. S.
40, 66 (1968) (emphasis added). A reasonable officer could
—————— 

And the officers could consider the drug use inside the house as evi-
dence that the partygoers knew their presence was unwelcome. 

10           DISTRICT OF COLUMBIA v. WESBY

                     Opinion of the Court

infer that the partygoers’ scattering and hiding was an
indication that they knew they were not supposed to be
there.
   The partygoers’ answers to the officers’ questions also
suggested their guilty state of mind. When the officers
asked who had given them permission to be there, the
partygoers gave vague and implausible responses. They
could not say who had invited them. Only two people
claimed that Peaches had invited them, and they were
working the party instead of attending it. If Peaches was
the hostess, it was odd that none of the partygoers men-
tioned her name. Additionally, some of the partygoers
claimed the event was a bachelor party, but no one could
identify the bachelor. The officers could have disbelieved
them, since people normally do not throw a bachelor party
without a bachelor. Based on the vagueness and implau-
sibility of the partygoers’ stories, the officers could have
reasonably inferred that they were lying and that their
lies suggested a guilty mind. Cf. Devenpeck v. Alford, 543
U. S. 146, 149, 155–156 (2004) (noting that the suspect’s
“untruthful and evasive” answers to police questioning
could support probable cause).
   The panel majority relied heavily on the fact that
Peaches said she had invited the partygoers to the house.
But when the officers spoke with Peaches, she was nerv-
ous, agitated, and evasive. Cf. Wardlow, supra, at 124
(explaining that the police can take a suspect’s “nervous,
evasive behavior” into account). After initially insisting
that she had permission to use the house, she ultimately
confessed that this was a lie—a fact that the owner con-
firmed. Peaches’ lying and evasive behavior gave the
officers reason to discredit everything she had told them.
For example, the officers could have inferred that Peaches
lied to them when she said she had invited the others to
the house, which was consistent with the fact that hardly
anyone at the party knew her name. Or the officers could
                  Cite as: 583 U. S. ____ (2018)           11

                      Opinion of the Court

have inferred that Peaches told the partygoers (like she
eventually told the police) that she was not actually rent-
ing the house, which was consistent with how the party-
goers were treating it.
  Viewing these circumstances as a whole, a reasonable
officer could conclude that there was probable cause to
believe the partygoers knew they did not have permission
to be in the house.
                              B
   In concluding otherwise, the panel majority engaged in
an “excessively technical dissection” of the factors support-
ing probable cause. Gates, 462 U. S., at 234. Indeed, the
panel majority failed to follow two basic and well-
established principles of law.
   First, the panel majority viewed each fact “in isolation,
rather than as a factor in the totality of the circumstances.”
Pringle, 540 U. S., at 372, n. 2. This was “mistaken in
light of our precedents.” Ibid. The “totality of the circum-
stances” requires courts to consider “the whole picture.”
Cortez, supra, at 417. Our precedents recognize that the
whole is often greater than the sum of its parts—
especially when the parts are viewed in isolation. See
United States v. Arvizu, 534 U. S. 266, 277–278 (2002).
Instead of considering the facts as a whole, the panel
majority took them one by one. For example, it dismissed
the fact that the partygoers “scattered or hid when the
police entered the house” because that fact was “not suffi-
cient standing alone to create probable cause.” 765 F. 3d,
at 23 (emphasis added). Similarly, it found “nothing in
the record suggesting that the condition of the house, on
its own, should have alerted the [partygoers] that they
were unwelcome.” Ibid. (emphasis added). The totality-of-
the-circumstances test “precludes this sort of divide-and-
conquer analysis.” Arvizu, 534 U. S., at 274.
   Second, the panel majority mistakenly believed that it
12            DISTRICT OF COLUMBIA v. WESBY

                      Opinion of the Court

could dismiss outright any circumstances that were “sus-
ceptible of innocent explanation.” Id., at 277. For exam-
ple, the panel majority brushed aside the drinking and the
lap dances as “consistent with” the partygoers’ explanation
that they were having a bachelor party. 765 F. 3d, at 23.
And it similarly dismissed the condition of the house as
“entirely consistent with” Peaches being a “new tenant.”
Ibid. But probable cause does not require officers to rule
out a suspect’s innocent explanation for suspicious facts.
As we have explained, “the relevant inquiry is not whether
particular conduct is ‘innocent’ or ‘guilty,’ but the degree of
suspicion that attaches to particular types of noncriminal
acts.” Gates, 462 U. S., at 244, n. 13. Thus, the panel
majority should have asked whether a reasonable officer
could conclude—considering all of the surrounding cir-
cumstances, including the plausibility of the explanation
itself—that there was a “substantial chance of criminal
activity.” Ibid.
   The circumstances here certainly suggested criminal
activity. As explained, the officers found a group of people
who claimed to be having a bachelor party with no bache-
lor, in a near-empty house, with strippers in the living
room and sexual activity in the bedroom, and who fled at
the first sign of police. The panel majority identified
innocent explanations for most of these circumstances in
isolation, but again, this kind of divide-and-conquer ap-
proach is improper. A factor viewed in isolation is often
more “readily susceptible to an innocent explanation” than
one viewed as part of a totality. Arvizu, supra, at 274.
And here, the totality of the circumstances gave the offic-
ers plenty of reasons to doubt the partygoers’ protestations
of innocence.
   For all of these reasons, we reverse the D. C. Circuit’s
holding that the officers lacked probable cause to arrest.
Accordingly, the District and its officers are entitled to
                     Cite as: 583 U. S. ____ (2018)                  13

                         Opinion of the Court

summary judgment on all of the partygoers’ claims.6
                             IV
  Our conclusion that the officers had probable cause to
arrest the partygoers is sufficient to resolve this case. But
where, as here, the Court of Appeals erred on both the
merits of the constitutional claim and the question of
qualified immunity, “we have discretion to correct its
errors at each step.” Ashcroft v. al-Kidd, 563 U. S. 731,
735 (2011); see, e.g., Plumhoff v. Rickard, 572 U. S. ___
(2014). We exercise that discretion here because the D. C.
Circuit’s analysis, if followed elsewhere, would “under-
mine the values qualified immunity seeks to promote.” al-
Kidd, supra, at 735.7
                             A
  Under our precedents, officers are entitled to qualified
immunity under §1983 unless (1) they violated a federal
statutory or constitutional right, and (2) the unlawfulness
of their conduct was “clearly established at the time.”
Reichle v. Howards, 566 U. S. 658, 664 (2012). “Clearly
established” means that, at the time of the officer’s con-
duct, the law was “ ‘sufficiently clear’ that every ‘reason-
able official would understand that what he is doing’ ” is
unlawful. al-Kidd, supra, at 741 (quoting Anderson v.
Creighton, 483 U. S. 635, 640 (1987)). In other words,
existing law must have placed the constitutionality of the
officer’s conduct “beyond debate.” al-Kidd, supra, at 741.
This demanding standard protects “all but the plainly
——————
  6 The partygoers do not contest that the presence of probable cause
defeats all of their claims.
  7 We continue to stress that lower courts “should think hard, and then

think hard again,” before addressing both qualified immunity and the
merits of an underlying constitutional claim. Camreta v. Greene, 563
U. S. 692, 707 (2011). We addressed the merits of probable cause here,
however, because a decision on qualified immunity alone would not
have resolved all of the claims in this case.
14            DISTRICT OF COLUMBIA v. WESBY

                      Opinion of the Court

incompetent or those who knowingly violate the law.”
Malley v. Briggs, 475 U. S. 335, 341 (1986).
  To be clearly established, a legal principle must have a
sufficiently clear foundation in then-existing precedent.
The rule must be “settled law,” Hunter v. Bryant, 502 U. S.
224, 228 (1991) (per curiam), which means it is dictated by
“controlling authority” or “a robust ‘consensus of cases of
persuasive authority,’ ” al-Kidd, supra, at 741–742 (quot-
ing Wilson v. Layne, 526 U. S. 603, 617 (1999)). It is not
enough that the rule is suggested by then-existing prece-
dent. The precedent must be clear enough that every
reasonable official would interpret it to establish the
particular rule the plaintiff seeks to apply. See Reichle,
566 U. S., at 666. Otherwise, the rule is not one that “every
reasonable official” would know. Id., at 664 (internal
quotation marks omitted).
  The “clearly established” standard also requires that the
legal principle clearly prohibit the officer’s conduct in the
particular circumstances before him. The rule’s contours
must be so well defined that it is “clear to a reasonable
officer that his conduct was unlawful in the situation he
confronted.” Saucier v. Katz, 533 U. S. 194, 202 (2001).
This requires a high “degree of specificity.” Mullenix v.
Luna, 577 U. S. ___, ___ (2015) (per curiam) (slip op., at 6).
We have repeatedly stressed that courts must not “define
clearly established law at a high level of generality, since
doing so avoids the crucial question whether the official
acted reasonably in the particular circumstances that he
or she faced.” Plumhoff, supra, at ___–___ (slip op., at 12–
13) (internal quotation marks and citation omitted). A
rule is too general if the unlawfulness of the officer’s con-
duct “does not follow immediately from the conclusion that
[the rule] was firmly established.” Anderson, supra, at
641. In the context of a warrantless arrest, the rule must
obviously resolve “whether ‘the circumstances with which
[the particular officer] was confronted . . . constitute[d]
                 Cite as: 583 U. S. ____ (2018)           15

                     Opinion of the Court

probable cause.’ ” Mullenix, supra, at ___ (slip op., at 6)
(quoting Anderson, supra, at 640–641; some alterations in
original).
   We have stressed that the “specificity” of the rule is
“especially important in the Fourth Amendment context.”
Mullenix, supra, at ___ (slip op., at 5). Probable cause
“turn[s] on the assessment of probabilities in particular
factual contexts” and cannot be “reduced to a neat set of
legal rules.” Gates, 462 U. S., at 232. It is “incapable of
precise definition or quantification into percentages.”
Pringle, 540 U. S., at 371. Given its imprecise nature,
officers will often find it difficult to know how the general
standard of probable cause applies in “the precise situa-
tion encountered.” Ziglar v. Abbasi, 582 U. S. ___, ___
(2017) (slip op., at 28). Thus, we have stressed the need to
“identify a case where an officer acting under similar
circumstances . . . was held to have violated the Fourth
Amendment.” White v. Pauly, 580 U. S. ___, ___ (2017)
(per curiam) (slip op., at 6); e.g., Plumhoff, supra, at ___.
While there does not have to be “a case directly on point,”
existing precedent must place the lawfulness of the par-
ticular arrest “beyond debate.” al-Kidd, supra, at 741. Of
course, there can be the rare “obvious case,” where the
unlawfulness of the officer’s conduct is sufficiently clear
even though existing precedent does not address similar
circumstances. Brosseau v. Haugen, 543 U. S. 194, 199
(2004) (per curiam). But “a body of relevant case law” is
usually necessary to “ ‘clearly establish’ the answer” with
respect to probable cause. Ibid.
   Under these principles, we readily conclude that the
officers here were entitled to qualified immunity. We start
by defining “the circumstances with which [the officers]
w[ere] confronted.” Anderson, 483 U. S., at 640. The
officers found a group of people in a house that the neigh-
bors had identified as vacant, that appeared to be vacant,
and that the partygoers were treating as vacant. The
16            DISTRICT OF COLUMBIA v. WESBY

                     Opinion of the Court

group scattered, and some hid, at the sight of law en-
forcement. Their explanations for being at the house were
full of holes. The source of their claimed invitation admit-
ted that she had no right to be in the house, and the owner
confirmed that fact.
   Even assuming the officers lacked actual probable cause
to arrest the partygoers, the officers are entitled to quali-
fied immunity because they “reasonably but mistakenly
conclude[d] that probable cause [wa]s present.” Id., at
641. Tellingly, neither the panel majority nor the party-
goers have identified a single precedent—much less a
controlling case or robust consensus of cases—finding a
Fourth Amendment violation “under similar circumstanc-
es.” Pauly, supra, at ___ (slip op., at 6). And it should go
without saying that this is not an “obvious case” where “a
body of relevant case law” is not needed. Brosseau, supra,
at 199. The officers were thus entitled to qualified
immunity.
                              B
   The panel majority did not follow this straightforward
analysis. It instead reasoned that, under clearly estab-
lished District law, a suspect’s “good purpose and bona
fide belief of her right to enter” vitiates probable cause to
arrest her for unlawful entry. 765 F. 3d, at 26–27. The
panel majority then concluded—in a two-sentence para-
graph without any explanation—that the officers must
have known that “uncontroverted evidence of an invitation
to enter the premises would vitiate probable cause for
unlawful entry.” Id., at 27. By treating the invitation as
“uncontroverted evidence,” the panel majority assumed
that the officers could not infer the partygoers’ intent from
other circumstances. And by treating the invitation as if it
automatically vitiated probable cause, the panel majority
assumed that the officers could not disbelieve the party-
goers’ story.
                      Cite as: 583 U. S. ____ (2018)                    17

                          Opinion of the Court

   The rule applied by the panel majority was not clearly
established because it was not “settled law.” Hunter, 502
U. S., at 228. The panel majority relied on a single deci-
sion, Smith v. United States, 281 A. 2d 438 (D. C. 1971).8
The defendant in Smith, who was found trespassing in a
locked construction site near midnight, asserted that he
was entitled to a jury instruction explaining that a bona
fide belief of a right to enter is a complete defense to un-
lawful entry. Id., at 439–440. The D. C. Court of Appeals
affirmed the trial court’s refusal to give the instruction
because the defendant had not established a “reasonable
basis” for his alleged bona fide belief. Ibid. Smith does
not say anything about whether the officers here could
infer from all the evidence that the partygoers knew that
they were trespassing.
   Nor would it have been clear to every reasonable officer
that, in these circumstances, the partygoers’ bona fide
belief that they were invited to the house was “uncontro-
verted.” The officers knew that the partygoers had en-
tered the home against the will of the owner. And District
case law suggested that officers can infer a suspect’s guilty
state of mind based solely on his conduct.9 In Tillman v.

——————
  8 We   have not yet decided what precedents—other than our own—
qualify as controlling authority for purposes of qualified immunity.
See, e.g., Reichle v. Howards, 566 U. S. 658, 665–666 (2012) (reserving
the question whether court of appeals decisions can be “a dispositive
source of clearly established law”). We express no view on that ques-
tion here. Relatedly, our citation to and discussion of various lower
court precedents should not be construed as agreeing or disagreeing
with them, or endorsing a particular reading of them. See City and
County of San Francisco v. Sheehan, 575 U. S. ___, ___, n. 4 (2015) (slip
op., at 14, n. 4). Instead, we address only how a reasonable official
“could have interpreted” them. Reichle, supra, at 667.
   9 The officers cited many of these authorities in their opening brief to

the Court of Appeals. See Brief for Appellants in No. 12–7127 (CADC),
pp. 28–29. Yet the panel majority failed to mention any of them in its
analysis of qualified immunity.
18               DISTRICT OF COLUMBIA v. WESBY

                          Opinion of the Court

Washington Metropolitan Area Transit Authority, 695
A. 2d 94 (D. C. 1997), for example, the D. C. Court of
Appeals held that officers had probable cause to believe
the plaintiff knowingly entered the paid area of a subway
station without paying. Id., at 96. The court rejected the
argument that “the officers had no reason to believe that
[the suspect] was ‘knowingly’ in the paid area” because the
officers “reasonably could have inferred from [the sus-
pect’s] undisputed conduct that he had the intent re-
quired.” Ibid. The court emphasized that officers can rely
on “the ordinary and reasonable inference that people
know what they are doing when they act.” Ibid. The court
also noted that “it would be an unusual case where the
circumstances, while undoubtedly proving an unlawful
act, nonetheless demonstrated so clearly that the suspect
lacked the required intent that the police would not even
have probable cause for an arrest.” Ibid. And the fact
that a case is unusual, we have held, is “an important
indication . . . that [the officer’s] conduct did not violate a
‘clearly established’ right.” Pauly, 580 U. S., at ___ (slip
op., at 7).
   Moreover, existing precedent would have given the
officers reason to doubt that they had to accept the party-
goers’ assertion of a bona fide belief. The D. C. Court of
Appeals has held that officers are not required to take a
suspect’s innocent explanation at face value. See, e.g.,
Nichols v. Woodward & Lothrop, Inc., 322 A. 2d 283, 286
(1974) (holding that an officer was not “obliged to believe
the explanation of a suspected shoplifter”). Similar prece-
dent exists in the Federal Courts of Appeals, which have
recognized that officers are free to disregard either all
innocent explanations,10 or at least innocent explanations
——————
   10 See, e.g., Borgman v. Kedley, 646 F. 3d 518, 524 (CA8 2011) (“[An

officer] need not rely on an explanation given by the suspect”); Cox v.
Hainey, 391 F. 3d 25, 32, n. 2 (CA1 2004) (“A reasonable police officer is
                     Cite as: 583 U. S. ____ (2018)                   19

                          Opinion of the Court

that are inherently or circumstantially implausible.11
These cases suggest that innocent explanations—
even uncontradicted ones—do not have any automatic,
probable-cause-vitiating effect.
  For these reasons, a reasonable officer, looking at the
entire legal landscape at the time of the arrests, could
have interpreted the law as permitting the arrests here.
There was no controlling case holding that a bona fide
belief of a right to enter defeats probable cause, that offic-
ers cannot infer a suspect’s guilty state of mind based on
his conduct alone, or that officers must accept a suspect’s
innocent explanation at face value. Indeed, several prece-
dents suggested the opposite. The officers were thus
entitled to summary judgment based on qualified immunity.
                        *  *    *
  The judgment of the D. C. Circuit is therefore reversed,
and the case is remanded for further proceedings con-
sistent with this opinion.
                                           It is so ordered.

——————
not required to credit a suspect’s story”); Marx v. Gumbinner, 905 F. 2d
1503, 1507, n. 6 (CA11 1990) (“[Officers a]re not required to forego
arresting [a suspect] based on initially discovered facts showing proba-
ble cause simply because [the suspect] offered a different explanation”);
Criss v. Kent, 867 F. 2d 259, 263 (CA6 1988) (“A policeman . . . is under
no obligation to give any credence to a suspect’s story . . . ”).
   11 See e.g., Ramirez v. Buena Park, 560 F. 3d 1012, 1024 (CA9 2009)

(holding that “innocent explanations for [a suspect’s] odd behavior
cannot eliminate the suspicious facts” and that “law enforcement
officers do not have to rule out the possibility of innocent behavior”
(internal quotation marks omitted)); United States v. Edwards, 632
F. 3d 633, 640 (CA10 2001) (holding that probable cause existed where
the suspect “offered only implausible, inconsistent explanations of how
he came into possession of the money”); Bradway v. Gonzales, 26 F. 3d
313, 321 (CA2 1994) (holding that “[a] reasonable officer who found the
[stolen items], and who heard [the suspect’s] implausible explanation
for possessing them, would have believed that probable cause existed”).
                  Cite as: 583 U. S. ____ (2018)            1

                    Opinion of SOTOMAYOR, J.

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 15–1485
                          _________________


  DISTRICT OF COLUMBIA, ET AL., PETITIONERS v.

            THEODORE WESBY, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

    APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT

                       [January 22, 2018]


  JUSTICE SOTOMAYOR, concurring in part and concurring
in the judgment.
  I agree with the majority that the officers here are
entitled to qualified immunity and, for that reason alone, I
concur in the Court’s judgment reversing the judgment of
the Court of Appeals for the District of Columbia. But, I
disagree with the majority’s decision to reach the merits of
the probable-cause question, which it does apparently only
to ensure that, in addition to respondents’ 42 U. S. C.
§1983 claims, the Court’s decision will resolve respond-
ents’ state-law claims of false arrest and negligent su-
pervision. See ante, at 13, n. 7. It is possible that our
qualified-immunity decision alone will resolve those claims.
See Reply Brief 20, n. 7. In light of the lack of a dispute on
an important legal question and the heavily factbound
nature of the probable-cause determination here, I do not
think that the Court should have reached that issue. The
lower courts are well equipped to handle the remaining
state-law claims in the first instance.
                    Cite as: 583 U. S. ____ (2018)                   1

                       OPINION OF GINSBURG, J.

SUPREME COURT OF THE UNITED STATES
                             _________________

                             No. 15–1485
                             _________________


  DISTRICT OF COLUMBIA, ET AL., PETITIONERS v.

            THEODORE WESBY, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

    APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT

                          [January 22, 2018]


  JUSTICE GINSBURG, concurring in the judgment in part.
  This case, well described in the opinion of the Court of
Appeals,* leads me to question whether this Court, in
assessing probable cause, should continue to ignore why
police in fact acted. See ante, at 4, n. 2. No arrests of
plaintiffs-respondents were made until Sergeant Suber so
instructed. His instruction, when conveyed to the officers
he superintended, was based on an error of law. Sergeant
Suber believed that the absence of the premises owner’s
consent, an uncontested fact in this case, sufficed to justify
arrest of the partygoers for unlawful entry. See App. 60
(Suber deposition) (officers had probable cause to arrest
because “Peaches did not have the right, nor did the [party-
goers] have the right[,] to be inside that location”). An
essential element of unlawful entry in the District of
Columbia is that the defendant “knew or should have
known that his entry was unwanted.” Ortberg v. United
States, 81 A. 3d 303, 308 (D. C. 2013). But under Sergeant
Suber’s view of the law, what the arrestees knew or should
have known was irrelevant. They could be arrested, as he
comprehended the law, even if they believed their entry

——————
   * The Court’s account of the undisputed facts goes beyond those re-
cited by the Court of Appeals. Compare ante, at 1–3, with 765 F. 3d 13,
17–18 (CADC 2014).
2             DISTRICT OF COLUMBIA v. WESBY

                    Opinion of GINSBURG, J.

was invited by a lawful occupant.
  Ultimately, plaintiffs-respondents were not booked for
unlawful entry. Instead, they were charged at the police
station with disorderly conduct. Yet no police officers at
the site testified to having observed any activities war-
ranting a disorderly conduct charge. Quite the opposite.
The officers at the scene of the arrest uniformly testified
that they had neither seen nor heard anything that would
justify such a charge, and Sergeant Suber specifically
advised his superiors that the charge was unwarranted.
See 765 F. 3d 13, 18 (CADC 2014); App. 56, 62–63, 79, 84,
90, 103.
  The Court’s jurisprudence, I am concerned, sets the
balance too heavily in favor of police unaccountability to
the detriment of Fourth Amendment protection. A num-
ber of commentators have criticized the path we charted in
Whren v. United States, 517 U. S. 806 (1996), and follow-on
opinions, holding that “an arresting officer’s state of
mind . . . is irrelevant to the existence of probable cause,”
Devenpeck v. Alford, 543 U. S. 146, 153 (2004). See, e.g., 1
W. LaFave, Search and Seizure §1.4(f ), p. 186 (5th ed.
2012) (“The apparent assumption of the Court in Whren,
that no significant problem of police arbitrariness can
exist as to actions taken with probable cause, blinks at
reality.”). I would leave open, for reexamination in a
future case, whether a police officer’s reason for acting, in
at least some circumstances, should factor into the Fourth
Amendment inquiry. Given the current state of the
Court’s precedent, however, I agree that the disposition
gained by plaintiffs-respondents was not warranted by
“settled law.” The defendants-petitioners are therefore
sheltered by qualified immunity.

```

---

## GROUP: _overhaul2/lake/cases/Donovan v. Dewey.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Donovan v. Dewey"
type: case
citation: "452 U.S. 594 (1981)"
parallel_cite: "101 S. Ct. 2534; 69 L. Ed. 2d 262"
neutral_cite: 1980 U.S. LEXIS 58
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-06-17
docket: 80-901
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Donovan v. Dewey
  varies_by_point: false
  scope_note: "Good law; part of the Colonnade-Biswell pervasively-regulated-industry line, later refined into the three-part test of New York v. Burger (1987)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110530/donovan-v-dewey/"
  cluster_id: 110530
  opinion_id: 9428427
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Progeny (pervasively-regulated industry)"
related: ["[[United States v. Biswell]]", "[[Marshall v. Barlow's Inc.]]", "[[See v. City of Seattle]]"]
aliases: []
tags: ["case", "fourth-amendment", "administrative-search", "inspections", "pervasively-regulated", "mines", "warrant"]
holding: "Warrantless inspections of a pervasively regulated industry (mines) are reasonable where a comprehensive statutory scheme — defining the certainty, regularity, frequency, and scope of inspection — provides a constitutionally adequate substitute for a warrant."
lake:
  record_id: Donovan v. Dewey
  status: under_review
  projected_at: 2026-07-06
---

# Donovan v. Dewey

*452 U.S. 594 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Under § 103(a) of the Federal Mine Safety and Health Act of 1977, a federal inspector sought to inspect a stone quarry operated by Dewey without a warrant. The Act authorizes mandatory, unannounced inspections of all mines at specified frequencies. Dewey refused entry and challenged the warrantless-inspection scheme under the Fourth Amendment; the District Court held it unconstitutional under *[[Marshall v. Barlow's Inc|Marshall v. Barlow's, Inc.]]*

## Issue
Whether the Fourth Amendment permits warrantless inspections of mines under a comprehensive federal regulatory scheme that does not require a warrant.

## Rule
Yes. Commercial premises in a pervasively regulated business enjoy reduced privacy. "The greater latitude to conduct warrantless inspections of commercial property reflects the fact that the expectation of privacy that the owner of commercial property enjoys in such property differs significantly from the sanctity accorded an individual's home, and that this privacy interest may, in certain circumstances, be adequately protected by regulatory schemes authorizing warrantless inspections." — 452 U.S. at 598–599. ^pin-598

"Applying this analysis … we conclude that the warrantless inspections required by the Mine Safety and Health Act do not offend the Fourth Amendment." — *Id.* at 602. ^pin-602

"[T]he only real issue before us is whether the statute's inspection program, in terms of the certainty and regularity of its application, provides a constitutionally adequate substitute for a warrant. We believe that it does." — *Id.* at 603. ^pin-603

## Application
Mining is "among the most hazardous" industries, giving Congress a substantial interest in unannounced inspections that a warrant requirement could frustrate. The Act supplied a constitutionally adequate warrant substitute: it mandates inspection of all mines at defined frequencies (surface mines at least twice yearly, underground at least four times), sets the standards in statute and regulation, and constrains inspector discretion — so the operator "is not left to wonder about the purposes of the inspector or the limits of his task." The certainty and regularity of the scheme made the warrantless inspections reasonable.

## Conclusion
The warrantless mine inspections under the Act were constitutional; the judgment for Dewey was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Donovan v. Dewey* applies and extends the *Colonnade-Biswell* pervasively-regulated-industry exception preserved in [[Marshall v. Barlow's Inc.]]; the line was later organized into a three-part test in *[[New York v. Burger]]* (1987). It remains good law.

## Appears on
- [[Special Needs and Administrative Searches]] — *Progeny (pervasively-regulated industry)*

## Sources
- *Donovan v. Dewey*, 452 U.S. 594 (1981) — https://www.courtlistener.com/opinion/110530/donovan-v-dewey/ — pinpoints: 598–599, 602, 603.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fd36d00ade780b13", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Donovan v. Dewey"}, "payload": {"all": [{"cite": "452 U.S. 594", "page": "594", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "452"}, {"cite": "101 S. Ct. 2534", "page": "2534", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}, {"cite": "69 L. Ed. 2d 262", "page": "262", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "69"}, {"cite": "1980 U.S. LEXIS 58", "page": "58", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "452 U.S. 594", "official": {"cite": "452 U.S. 594", "page": "594", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "452"}, "official_selection_present": true, "record_id": "Donovan v. Dewey"}}
{"assertion_id": "0b90fb2df9f6e0ff", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-598", "record_id": "Donovan v. Dewey"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-598", "pinpoint_status": "slip-only", "quote": "--- # Donovan v. Dewey *452 U.S. 594 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Under § 103(a) of the Federal Mine Safety and Health Act of 1977, a federal inspector sought to inspect a stone quarry operated by Dewey without a warrant. The Act authorizes mandatory, unannounced inspections of all mines at specified frequencies. Dewey refused entry and challenged the warrantless-inspection scheme under the Fourth Amendment; the District Court held it unconstitutional under *Marshall v. Barlow's, Inc.* ## Issue Whether the Fourth Amendment permits warrantless inspections of mines under a comprehensive federal regulatory scheme that does not require a warrant. ## Rule Yes. Commercial premises in a pervasively regulated business enjoy reduced privacy.", "quote_fidelity": "mismatch", "record_id": "Donovan v. Dewey", "star_marker": null}}
{"assertion_id": "55cdc239d467aca5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-603", "record_id": "Donovan v. Dewey"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-603", "pinpoint_status": "slip-only", "quote": "[T]he only real issue before us is whether the statute's inspection program, in terms of the certainty and regularity of its application, provides a constitutionally adequate substitute for a warrant. We believe that it does.", "quote_fidelity": "mismatch", "record_id": "Donovan v. Dewey", "star_marker": null}}
{"assertion_id": "b8ce32c55496f0b7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-602", "record_id": "Donovan v. Dewey"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-602", "pinpoint_status": "slip-only", "quote": "Applying this analysis … we conclude that the warrantless inspections required by the Mine Safety and Health Act do not offend the Fourth Amendment.", "quote_fidelity": "mismatch", "record_id": "Donovan v. Dewey", "star_marker": null}}
{"assertion_id": "ff83d6600d46f650", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Donovan v. Dewey"}, "payload": {"as_of_content": "1981-06-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Donovan v. Dewey", "scope_note": "Good law; part of the Colonnade-Biswell pervasively-regulated-industry line, later refined into the three-part test of New York v. Burger (1987).", "varies_by_point": false}}
```

### lake record — Donovan v. Dewey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Donovan v. Dewey",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Donovan v. Dewey",
    "case_name_short": "Donovan",
    "case_name_full": "DONOVAN, SECRETARY OF LABOR v. DEWEY Et Al.",
    "input_case_name": "Donovan v. Dewey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-06-17",
    "year": 1981,
    "docket": "80-901",
    "cluster_id": 110530,
    "lead_opinion_id": 9428427,
    "sibling_ids": [
      110530,
      9428427,
      9428428,
      9428429,
      9428430
    ],
    "absolute_url": "/opinion/110530/donovan-v-dewey/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9032957,
        "score": 20,
        "case_name": "Donovan v. Dewey"
      },
      {
        "cluster_id": 9031727,
        "score": 20,
        "case_name": "Donovan v. Dewey"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "452 U.S. 594",
      "volume": "452",
      "reporter": "U.S.",
      "page": "594",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2534",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 262",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "262",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 58",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "58",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "452 U.S. 594",
        "volume": "452",
        "reporter": "U.S.",
        "page": "594",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2534",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 262",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "262",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 58",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "58",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "452 U.S. 594",
    "official_selection": {
      "court_class": "scotus",
      "selected": "452 U.S. 594",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-598",
      "page": null,
      "quote": "--- # Donovan v. Dewey *452 U.S. 594 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Under \u00a7 103(a) of the Federal Mine Safety and Health Act of 1977, a federal inspector sought to inspect a stone quarry operated by Dewey without a warrant. The Act authorizes mandatory, unannounced inspections of all mines at specified frequencies. Dewey refused entry and challenged the warrantless-inspection scheme under the Fourth Amendment; the District Court held it unconstitutional under *Marshall v. Barlow's, Inc.* ## Issue Whether the Fourth Amendment permits warrantless inspections of mines under a comprehensive federal regulatory scheme that does not require a warrant. ## Rule Yes. Commercial premises in a pervasively regulated business enjoy reduced privacy.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-602",
      "page": null,
      "quote": "Applying this analysis \u2026 we conclude that the warrantless inspections required by the Mine Safety and Health Act do not offend the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-603",
      "page": null,
      "quote": "[T]he only real issue before us is whether the statute's inspection program, in terms of the certainty and regularity of its application, provides a constitutionally adequate substitute for a warrant. We believe that it does.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Donovan v. Dewey",
    "varies_by_point": false,
    "scope_note": "Good law; part of the Colonnade-Biswell pervasively-regulated-industry line, later refined into the three-part test of New York v. Burger (1987).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Phillips v. State",
          "cluster_id": 1747319,
          "cite": [
            "109 S.W.3d 562",
            "2003 WL 1923487"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
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
        "journal_ref": "Donovan v. Dewey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crosby v. Paulk",
          "cluster_id": 74072,
          "cite": [
            "187 F.3d 1339",
            "1999 U.S. App. LEXIS 21641",
            "1999 WL 703193"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perry G. Blocker",
          "cluster_id": 733272,
          "cite": [
            "104 F.3d 720",
            "1997 U.S. App. LEXIS 712",
            "1997 WL 14762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Argent Chemical Laboratories, Inc.",
          "cluster_id": 7038653,
          "cite": [
            "93 F.3d 572",
            "96 Cal. Daily Op. Serv. 6117",
            "96 Daily Journal DAR 10005",
            "1996 U.S. App. LEXIS 20462",
            "1996 WL 465363"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane1_negative"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Krull",
          "cluster_id": 111835,
          "cite": [
            "94 L. Ed. 2d 364",
            "107 S. Ct. 1160",
            "480 U.S. 340",
            "1987 U.S. LEXIS 1061",
            "55 U.S.L.W. 4291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aaron Lindh v. James P. Murphy, Warden",
          "cluster_id": 726705,
          "cite": [
            "96 F.3d 856",
            "1996 U.S. App. LEXIS 24136",
            "1996 WL 517290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thunder Basin Coal Co. v. Reich",
          "cluster_id": 112921,
          "cite": [
            "127 L. Ed. 2d 29",
            "114 S. Ct. 771",
            "510 U.S. 200",
            "1994 U.S. LEXIS 1136",
            "94 Daily Journal DAR 619",
            "7 Fla. L. Weekly Fed. S 695",
            "94 Cal. Daily Op. Serv. 373",
            "62 U.S.L.W. 4058",
            "1994 CCH OSHD 30,312",
            "16 OSHC (BNA) 1553"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Clifford",
          "cluster_id": 111057,
          "cite": [
            "78 L. Ed. 2d 477",
            "104 S. Ct. 641",
            "464 U.S. 287",
            "1984 U.S. LEXIS 14",
            "52 U.S.L.W. 4056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dow Chemical Co. v. United States Ex Rel. Administrator",
          "cluster_id": 111667,
          "cite": [
            "90 L. Ed. 2d 226",
            "106 S. Ct. 1819",
            "476 U.S. 227",
            "1986 U.S. LEXIS 155",
            "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
            "54 U.S.L.W. 4464",
            "24 ERC (BNA) 1385"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Menotti v. City of Seattle",
          "cluster_id": 3032002,
          "cite": [
            "409 F.3d 1113",
            "2005 WL 1300994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 1836924,
          "cite": [
            "842 So. 2d 330",
            "2003 WL 1826561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
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
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald P. Rohrig",
          "cluster_id": 728738,
          "cite": [
            "98 F.3d 1506",
            "1996 U.S. App. LEXIS 28274",
            "1996 WL 627521"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 1160907,
          "cite": [
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "21 Cal. 4th 668"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph J. O'Brien v. City of Grand Rapids William Hegarty Daniel Ostapowicz",
          "cluster_id": 669698,
          "cite": [
            "23 F.3d 990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Swint v. City Of Wadley",
          "cluster_id": 693042,
          "cite": [
            "51 F.3d 988",
            "1995 U.S. App. LEXIS 10481"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vaughn Neita v. City of Chicago",
          "cluster_id": 4239934,
          "cite": [
            "830 F.3d 494",
            "2016 U.S. App. LEXIS 13191",
            "2016 WL 3905604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Free Speech Coalition, Inc. v. Attorney General of the United States",
          "cluster_id": 676451,
          "cite": [
            "677 F.3d 519",
            "2012 WL 1255056",
            "2012 U.S. App. LEXIS 7543"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Donovan v. Dewey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110530 OR 9428427 OR 9428428 OR 9428429 OR 9428430) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDgyMjA4MDAwMDAmcz00OTI5JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110530+OR+9428427+OR+9428428+OR+9428429+OR+9428430%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110530 OR 9428427 OR 9428428 OR 9428429 OR 9428430)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NSZzPTEyMTU1MzQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110530+OR+9428427+OR+9428428+OR+9428429+OR+9428430%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110530 OR 9428427 OR 9428428 OR 9428429 OR 9428430)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 1,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110530 OR 9428427 OR 9428428 OR 9428429 OR 9428430)",
    "indexed_citing_opinions": 458,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110530,
        "count": 397,
        "count_source": "search"
      },
      {
        "opinion_id": 9428427,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9428428,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428429,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428430,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 689,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/donovan-v-dewey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjczMjc3OCZzPTQ4OTgzOTUmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28110530+OR+9428427+OR+9428428+OR+9428429+OR+9428430%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110530,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 110420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 368292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 370334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 373443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 381457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110530,
        "cited_id": 1557646,
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
    "date_created": "2026-07-05T02:40:01Z",
    "date_modified": "2026-07-06T07:40:38Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:40:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:40:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:44:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:40:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Donovan v. Dewey

```
<opinion type="majority">
<author id="b642-4"><page-number citation-index="1" label="596">*596</page-number>Justice Marshall</author>
<p id="Ah4">delivered the opinion of the Court.</p>
<p id="b642-5">In this case we consider whether § 103 (a) of the Federal Mine Safety and Health Act of 1977, <span class="citation no-link">30 U. S. C. § 813</span> (a) (1976 ed., Supp. Ill), which authorizes warrantless inspections of underground and surface mines, violates the Fourth Amendment. Concluding that searches conducted pursuant to this provision are reasonable within the meaning of the Fourth Amendment, we reverse the judgment of the District Court for the Eastern District of Wisconsin invalidating the statute.</p>
<p id="b642-6">I</p>
<p id="b642-7">The Federal Mine Safety and Health Act of 1977, <span class="citation no-link">91 Stat. 1290</span>, <span class="citation no-link">30 U. S. C. § 801</span> <em>et seq. </em>(1976 ed. and Supp. Ill), requires the Secretary of Labor to develop detailed mandatory health and safety standards to govern the operation of the Nation’s mines. 30 XJ. S. C. §811 (1976 ed., Supp. III).<footnotemark>1</footnotemark> Section 103 (a) of the Act, <span class="citation no-link">30 U. S. C. § 813</span> (a) (1976 ed., Supp. HI), provides that federal mine inspectors are to inspect underground mines at least four times per year and surface mines at least twice a year to insure compliance with these standards, and to make followup inspections to determine whether previously discovered violations have been corrected. This section also grants mine inspectors “a right of entry to, upon, or through any coal or other mine” <footnotemark>2</footnotemark> and states that “no advance notice of an inspection shall be provided to any person.” If a mine operator refuses to allow a warrant-less inspection conducted pursuant to § 103 (a), the Secretary <page-number citation-index="1" label="597">*597</page-number>is authorized to institute a civil action to obtain injunctive or other appropriate relief. <span class="citation no-link">30 U. S. C. § 818</span> (a)(1)(C) (1976 ed., Supp. III).</p>
<p id="b643-5">In July 1978, a federal mine inspector attempted to inspect quarries owned by appellee Waukesha Lime and Stone Co. in order to determine whether all 25 safety and health violations uncovered during a prior inspection had been corrected. After the inspector had been on the site for about an hour, Waukesha’s president, appellee Douglas Dewey, refused to allow the inspection to continue unless the inspector first obtain a search warrant. The inspector issued a citation to Waukesha for terminating the inspection,<footnotemark>3</footnotemark> and the Secretary subsequently filed this civil action in the District Court for the Eastern District of Wisconsin seeking to enjoin appellees from refusing to permit warrantless searches of the Waukesha facility.</p>
<p id="b643-6">The District Court granted summary judgment in favor of appellees on the ground that the Fourth Amendment prohibited the warrantless searches of stone quarries authorized by § 103 (a) of the Act.<footnotemark>4</footnotemark> <span class="citation" data-id="1557646"><a href="/opinion/1557646/marshall-v-dewey/" aria-description="Citation for case: Marshall v. Dewey">493 F. Supp. 963</a></span> (1980). The <page-number citation-index="1" label="598">*598</page-number>Secretary appealed directly to this Court pursuant to <span class="citation no-link">28 U. S. C. § 1252</span>. Because the District Court’s ruling invalidated an important prqvision of the Mine Safety and Health Act, we noted probable jurisdiction.<footnotemark>5</footnotemark> <em>Sub nom. Marshall </em>v. <em>Dewey, </em><span class="citation" data-id="9023790"><a href="/opinion/9030506/marshall-v-dewey/" aria-description="Citation for case: Marshall v. Dewey">449 U. S. 1122</a></span> (1981).</p>
<p id="b644-5">II</p>
<p id="b644-6">Our prior cases have established that the Fourth Amendment’s prohibition against unreasonable searches applies to administrative inspections of private commercial property. <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978); <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967). However, unlike searches of private homes, which generally must be conducted pursuant to a warrant in order to be reasonable under the Fourth Amendment,<footnotemark>6</footnotemark> legislative schemes authorizing warrantless administrative searches of commercial property do not necessarily violate the Fourth Amendment. See, <em>e. g., United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972); <em>Colonnade Catering Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970). The greater latitude to conduct warrantless inspections of commercial property reflects the fact that the expectation of privacy that the owner of commercial property enjoys in such property differs significantly from the sanctity accorded an <page-number citation-index="1" label="599">*599</page-number>individual's home, and that this privacy interest may, in certain circumstances, be adequately protected by regulatory schemes authorizing warrantless inspections. <em>United States </em>v. <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Biswell, supra, </em>at 316</a></span>.</p>
<p id="b645-5">The interest of the owner of commercial property is not one in being free from any inspections. Congress has broad authority to regulate commercial enterprises engaged in or affecting interstate commerce, and an inspection program may in some cases be a necessary component of federal regulation. Rather, the Fourth Amendment protects the interest of the owner of property in being free from <em>unreasonable </em>intrusions onto his property by agents of the government. Inspections of commercial property may be unreasonable if they are not authorized by law or are unnecessary for the furtherance of federal interests. <em>Colonnade Catering Corp. </em>v. <em>United States, supra, </em>at 77. Similarly, warrantless inspections of commercial property may be constitutionally objectionable if their occurrence is so random, infrequent, or unpredictable that the owner, for all practical purposes, has no real expectation that his property will from time to time be inspected by government officials. <em>Marshall </em>v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Barlow’s, Inc., supra, at </em>323</a></span>. “Where Congress has authorized inspection but made no rules governing the procedures that inspectors must follow, the Fourth Amendment and its various restrictive rules apply.” <em>Colonnade Corp. </em>v. <em>United States, supra, </em>at 77. In such cases, a warrant may be necessary to protect the owner from the “unbridled discretion [of] executive and administrative officers,” <em>Marshall </em>v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Barlow’s, Inc., supra, </em>at 323</a></span>, by assuring him that “reasonable legislative or administrative standards for conducting an . . . inspection are satisfied with respect to a particular [establishment].” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 538</a></span> (1967).</p>
<p id="b645-6">However, the assurance of regularity provided by a warrant may be unnecessary under certain inspection schemes. Thus, in <em>Colonnade Corp. </em>v. <em>United States, </em>we recognized that because the alcoholic beverage industry had long been <page-number citation-index="1" label="600">*600</page-number>“subject to close supervision and inspection,” Congress enjoyed “broad power to design such powers of inspection ... as it deems necessary to meet the evils at hand.” <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 76-77</a></span>. Similarly, in <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>this Court-concluded that the Gun Control Act of 1968, <span class="citation no-link">18 U. S. C. § 921</span> <em>et seq., </em>provided a sufficiently comprehensive and predictable inspection scheme that the warrantless inspections mandated under the statute did not violate the Fourth Amendment. After describing the strong federal interest in conducting unannounced, warrantless inspections, we noted:</p>
<blockquote id="b646-5">“It is also plain that inspections for compliance with the Gun Control Act pose only limited threats to the dealer’s justifiable expectations of privacy. When a dealer chooses to engage in this pervasively regulated business ... , he does so with the knowledge that his records, firearms, and ammunition will be subject to effective inspection. . . . The dealer is not left to wonder about the purposes of the inspector or the limits of his task.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</blockquote>
<p id="b646-6">These decisions make clear that a warrant may not be constitutionally required when Congress has reasonably determined that warrantless searches are necessary to further a regulatory scheme and the federal regulatory presence is sufficiently comprehensive and defined that the owner of commercial property cannot help but be aware that his property will be subject to periodic inspections undertaken for specific purposes.</p>
<p id="b646-7">We re-emphasized this exception to the warrant requirement most recently in <em>Marshall </em>v. <em>Barlow’s, Inc. </em>In that case, we held that absent consent a warrant was constitutionally required in order to conduct administrative inspections under § 8 (a) of the Occupational Safety and Health Act of 1970, <span class="citation no-link">29 U. S. C. §657</span> (a). That statute imposes health and safety standards on all businesses engaged in or affecting interstate commerce that have employees, <span class="citation no-link">29 U. S. C. <page-number citation-index="1" label="601">*601</page-number>§ 652</span> (5), and authorizes representatives of the Secretary to conduct inspections to ensure compliance with the Act. <span class="citation no-link">29 U. S. C. § 657</span> (a). However, the Act fails to tailor the scope and frequency of such administrative inspections to the particular health and safety concerns posed by the numerous and varied businesses regulated by the statute. Instead, the Act flatly authorizes administrative inspections of “any factory, plant, establishment, construction site, or other area, workplace, or environment where work is performed by an employee of an employer” and empowers inspectors conducting such searches to investigate “any such place of employment and all pertinent conditions, structures, machines, apparatus, devices, equipment, and materials therein, and to question privately any such employer, owner, operator, agent, or employee.” <em><span class="citation no-link">Ibid.</span> </em>Similarly, the Act does not provide any standards to guide inspectors either in their selection of establishments to be searched or in the exercise of their authority to search. The statute instead simply provides that such searches must be performed “at . . . reasonable times, and within reasonable limits and in a reasonable manner.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b647-5">In assessing this regulatory scheme, this Court found that the provision authorizing administrative searches “devolves almost unbridled discretion upon executive and administrative officers, particularly those in the field, as to when to search and whom to search.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 323</a></span>. Accordingly, we concluded that a warrant was constitutionally required to assure a nonconsenting owner, who may have little real expectation that his business will be subject to inspection, that the contemplated search was “authorized by statute, and . . . pursuant to an administrative plan containing specific neutral criteria.” <em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">Ibid.</a></span> </em>However, we expressly limited our holding to the inspection provisions of the Occupational Safety and Health Act, noting that the “reasonableness of a warrantless search . . . will depend upon the specific enforcement needs and privacy guarantees of each statute” and that some statutes “apply only to a single industry, where <page-number citation-index="1" label="602">*602</page-number>regulations might already be so pervasive that a <em>Colonnade-Biswell </em>exception to the warrant requirement could apply.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#321" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Id., </em>at 321</a></span>.</p>
<p id="b648-4">Applying this analysis to the case before us, we conclude that the warrantless inspections required by the Mine Safety and Health Act do not offend the Fourth Amendment. As an initial matter, it is undisputed that there is a substantial federal interest in improving the health and safety conditions in the Nation’s underground and surface mines. In enacting the statute, Congress was plainly aware that the mining industry is among the most hazardous in the country and that the poor health and safety record of this industry has significant deleterious effects on interstate commerce.<footnotemark>7</footnotemark> Nor is it seriously contested that Congress in this case could reasonably determine, as it did with respect to the Gun Control Act in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>that a system of warrantless inspections was <page-number citation-index="1" label="603">*603</page-number>necessary “if the law is to be properly enforced and inspection made effective.” <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>. In designing an inspection program. Congress expressly recognized that a warrant requirement could significantly frustrate effective enforcement of the Act. Thus, it provided in § 103 (a) of the Act that “no advance notice of an inspection shall be provided to any person.” In explaining this provision, the Senate Report notes:</p>
<blockquote id="b649-5">“[I]n [light] of the notorious ease with which many safety or health hazards may be concealed if advance warning of inspection is obtained, a warrant requirement would seriously undercut this Act’s objectives.” S. Rep. No. 95-181, p. 27 (1977).</blockquote>
<p id="b649-6">We see no reason not to defer to this legislative determination. Here, as in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>Congress could properly conclude: “[I]f inspection is to be effective and serve as a credible deterrent, unannounced, even frequent, inspections are essential. In this context, the prerequisite of a warrant could easily frustrate inspection.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</p>
<p id="b649-7">Because a warrant requirement clearly might impede the “specific enforcement needs” of the Act, <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#321" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 321</a></span>, the only real issue before us is whether the statute’s inspection program, in terms of the certainty and regularity of its application, provides a constitutionally adequate substitute for a warrant. We believe that it does. Unlike the statute at issue in <em>Barlow’s, </em>the Mine Safety and Health Act applies to industrial activity with a notorious history of serious accidents and unhealthful working conditions. The Act is specifically tailored to address those concerns,<footnotemark>8</footnotemark> and the regulation of mines it imposes is sufficiently pervasive and defined that the owner of such a facility cannot help but be aware that he “will be subject to effective inspection.” <em>United States </em>v. <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Biswell, supra, </em>at 316</a></span>. First, the Act re<page-number citation-index="1" label="604">*604</page-number>quires inspection of <em>all </em>mines and specifically defines the frequency of inspection. Representatives of the Secretary must inspect all surface mines at least twice annually and all underground mines at least four times annually. <span class="citation no-link">30 U. S. C. § 813</span> (a) (1976 ed., Supp. III). Similarly, all mining operations that generate explosive gases must be inspected at irregular 5-, 10-, or 15-day intervals. § 813 (i). Moreover, the Secretary must conduct followup inspections of mines where violations of the Act have previously been discovered, § 813 (a), and must inspect a mine immediately if notified by a miner or a miner’s representative that a violation of the Act or an imminently dangerous condition exists. § 813 (g).<footnotemark>9</footnotemark> Second, the standards with which a mine operator is required to comply are all specifically set forth in the Act or in Title 30 of the Code of Federal Regulations. Indeed, the Act requires that the Secretary inform mine operators of all standards proposed pursuant to the Act. § 811 (e). Thus, rather than leaving the frequency and purpose of inspections to the unchecked discretion of Government officers, the Act establishes a predictable and guided federal regulatory presence. Like the gun dealer in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>the operator of a mine “is not left to wonder about the purposes of the inspector or the limits of his task.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</p>
<p id="b650-5">Finally, the Act provides a specific mechanism for accommodating any special privacy concerns that a specific mine operator might have. The Act prohibits forcible entries, and instead requires the Secretary, when refused entry onto a mining facility, to file a civil action in federal court to obtain an injunction against future refusals. <span class="citation no-link">30 U. S. C. § 818</span> (a) (1976 ed., Supp. III). This proceeding provides an <page-number citation-index="1" label="605">*605</page-number>adequate forum for the mineowner to show that a specific search is outside the federal regulatory authority, or to seek from the district court an order accommodating any unusual privacy interests that the mineowner might have. See, <em>e. g., Marshall </em>v. <em>Stoudt’s Ferry Preparation Co., </em><span class="citation" data-id="368292"><a href="/opinion/368292/ray-marshall-secretary-of-labor-united-states-department-of-labor-v/#594" aria-description="Citation for case: Ray Marshall, Secretary of Labor, United States...">602 F. 2d 589, 594</a></span> (CA3 1979) (inspectors ordered to keep confidential mine's trade secrets), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/1015/">444 U. S. 1015</a></span> (1980).</p>
<p id="b651-5">Under these circumstances, it is difficult to see what additional protection a warrant requirement would provide. The Act itself clearly notifies the operator that inspections will be performed on a regular basis. Moreover, the Act and the regulations issued pursuant to it inform the operator of what health and safety standards must be met in order to be in compliance with the statute. The discretion of Government officials to determine what facilities to search and what violations to search for is thus directly curtailed by the regulatory scheme. In addition, the statute itself embodies a means by which any special Fourth Amendment interests can be accommodated. Accordingly, we conclude that the general program of warrantless inspections authorized by § 103 (a) of the Act does not violate the Fourth Amendment.</p>
<p id="b651-6">Appellees contend, however, that even if § 103 (a) is constitutional as applied to most segments of the mining industry, it nonetheless violates the Fourth Amendment as applied to authorize warrantless inspections of stone quarries. Appel-lees’ argument essentially tracks the reasoning of the court below. That court, while expressly acknowledging our decisions in <em>Colonnade </em>and <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>found the exception to the warrant requirement defined in those cases to be inapplicable solely because surface quarries, which came under federal regulation in 1966,<footnotemark>10</footnotemark> do “not have a long tradition of government regulation.” <span class="citation" data-id="1557646"><a href="/opinion/1557646/marshall-v-dewey/#964" aria-description="Citation for case: Marshall v. Dewey">493 F. Supp., at 964</a></span>. To be sure, in <em>Colonnade </em>this Court referred to “the long history of the <page-number citation-index="1" label="606">*606</page-number>regulation of the liquor industry,” <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#75" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 75</a></span>, and more recently in <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 313</a></span>, we noted that a “long tradition of close government supervision” militated against imposition of a warrant requirement. However, as previously noted, see <em>supra, </em>at 599, it is the pervasiveness and regularity of the federal regulation that ultimately determines whether a warrant is necessary to render an inspection program reasonable under the Fourth Amendment. Thus in <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>this Court upheld the warrantless search provisions of the Gun Control Act of 1968 despite the fact that “[f]ederal regulation of the interstate traffic in firearms is not as deeply rooted in history as is governmental control of the liquor industry.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>. Of course, the duration of a particular regulatory Scheme will often be an important factor in determining whether it is sufficiently pervasive to make the imposition of a warrant requirement unnecessary. But if the length of regulation were the only criterion, absurd results would occur. Under appellees’ view, new or emerging industries, including ones such as the nuclear power industry that pose enormous potential safety and health problems, could never be subject to warrantless searches even under the most carefully structured inspection program simply because of the recent vintage of regulation.</p>
<p id="b652-5">The Fourth Amendment’s central concept of reasonableness will not tolerate such arbitrary results, and we therefore conclude that warrantless inspection of stone quarries, like similar inspections of other mines covered by the Act, are constitutionally permissible. The judgment of the District Court is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b652-6">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b642-8"> The Act supersedes the Federal Coal Mine Health and Safety Act of 1969, formerly <span class="citation no-link">30 U. S. C. § 801</span> <em>et seq., </em>and repeals and replaces the Federal Metal and Nonmetallic Mine Safety Act of 1966, formerly <span class="citation no-link">30 U. S. C. § 721</span> <em>et seq.</em></p>
</footnote>
<footnote label="2">
<p id="b642-9"> The Act defines “coal or other mine” to include “an area of land from which minerals are extracted in nonliquid form or, if in liquid form, are extracted with workers underground.” <span class="citation no-link">30 U. S. C. § 802</span> (h) (1) (1976 ed., Supp. III). It is undisputed that the quarry operated by appellee company falls within this definition.</p>
</footnote>
<footnote label="3">
<p id="b643-7"> The Act provides that the Secretary shall issue citations and propose civil penalties for violations of the Act or standards promulgated under the Act. <span class="citation no-link">30 U. S. C. §§ 814</span> (a), 820 (a) (1976 ed., Supp. III). The Secretary’s regulations call for issuance of a citation and the assessment of a civil penalty for denial of entry. <span class="citation no-link">30 CFR § 100.4</span> (1980). The Act also allows a mine operator to contest any citation in a hearing before an administrative law judge, whose decision is subject to discretionary review by the Mine Safety and Health Review Commission. <span class="citation no-link">30 U. S. C. §§ 815</span> (d), 823 (d) (1976 ed., Supp. III). The operator thereafter is entitled to review of a final administrative ruling in the appropriate court of appeals. <span class="citation no-link">30 U. S. C. §816</span> (1976 ed., Supp. III).</p>
<p id="b643-8">In this case, the Administrative Law Judge upheld a $1,000 civil penalty proposed by the Secretary. This decision is currently under review by the Mine Safety and Health Review Commission.</p>
</footnote>
<footnote label="4">
<p id="b643-9"> Although the District Court limited its holding to the constitutionality of § 103 (a) as applied to warrantless inspections of stone quarries, the Act makes no distinction as to the type of mine to be inspected, and our <page-number citation-index="1" label="598">*598</page-number>conclusions here apply equally to all warrantless inspections authorized by the Act.</p>
</footnote>
<footnote label="5">
<p id="b644-9"> Three Courts of Appeals have upheld the warrantless inspection provisions of the Act as they apply to quarry operations similar to appellees’ facility. See <em>Marshall </em>v. <em>Texoline Co., </em><span class="citation" data-id="8910771"><a href="/opinion/8921866/marshall-v-texoline-co/" aria-description="Citation for case: Marshall v. Texoline Co.">612 F. 2d 935</a></span> (CA5 1980); <em>Marshall </em>v. <em>Nolichuckey Sand Co., </em><span class="citation" data-id="370334"><a href="/opinion/370334/ray-marshall-secretary-of-labor-united-states-department-of-labor-v/" aria-description="Citation for case: Ray Marshall, Secretary of Labor, United States...">606 F. 2d 693</a></span> (CA6 1979), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./446/908/">446 U. S. 908</a></span> (1980); <em>Marshall </em>v. <em>Stoudt’s Ferry Preparation Co., </em><span class="citation" data-id="368292"><a href="/opinion/368292/ray-marshall-secretary-of-labor-united-states-department-of-labor-v/" aria-description="Citation for case: Ray Marshall, Secretary of Labor, United States...">602 F. 2d 589</a></span> (CA3 1979), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/1015/">444 U. S. 1015</a></span> (1980).</p>
</footnote>
<footnote label="6">
<p id="b644-10"> Absent consent or exigent circumstances, a private home may not be entered to conduct a search or effect an arrest without a warrant. <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981); <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948). Of course, these same restrictions pertain when commercial property is searched for contraband or evidence of crime. <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#352" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 352-359</a></span> (1977).</p>
</footnote>
<footnote label="7">
<p id="b648-5"> In the preamble to the Act, Congress declared:</p>
<blockquote id="b648-6">“[T]here is an urgent need to provide more effective means and measures for improving the working conditions and practices in the Nation’s coal or other mines in order to prevent death and serious physical harm, and in order to prevent occupational diseases originating in such mines. . . .</blockquote>
<blockquote id="b648-7">“[T]he existence of unsafe and unhealthful conditions and practices in the Nation’s coal or other mines is a serious impediment to the future growth of the coal and other mining industry and cannot be tolerated. . . .</blockquote>
<blockquote id="b648-8">“[T]he disruption of production and the loss of income to operators and miners as a result of coal or other mine accidents or occupationally caused diseases unduly impedes and burdens commerce.” <span class="citation no-link">30 U. S. C. §§ 801</span> (c), (d), (f).</blockquote>
<p id="b648-9">These congressional findings were based on extensive evidence showing that the mining industry was among the most hazardous of the Nation’s industries. See S. Rep. No. 95-181 (1977); H. R. Rep. No. 95-312 (1977). Although Congress did not make explicit reference to stone quarries in these findings, stone quarries were deliberately included within the scope of the statute. Since the Mine Safety and Health Act, unlike the Occupational Safety and Health Act, is narrowly and explicitly directed at inherently dangerous industrial activity, the inclusion of stone quarries in the statute is presumptively equivalent to a finding that the stone quarrying industry is inherently dangerous.</p>
</footnote>
<footnote label="8">
<p id="b649-8"> Cf. H. R. Rep. No. 95-312, <em>supra, </em>at 1 (mining operations are “so unique, so complex, and so hazardous as to not fit neatly under the Occupational Safety and Health Act”).</p>
</footnote>
<footnote label="9">
<p id="b650-6"> In contrast, the inspection scheme considered in <em>Barlow’s </em>did not require the periodic inspection of businesses covered by the Occupational Safety and Health Act, and instead left the decision to inspect within the broad discretion of agency officials. Thus, when a Government official attempted to inspect the facility in that case, the owner had no indication of “why an inspection of [his] establishment was within the program.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 323, n. 20</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b651-7"> Stone quarries were first subjected to federal health and safety inspections under the Federal Metal and Nonmetallie Mine Safety Act of 1966, 30 TJ. S. C. §§ 723, 724.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Dow Chemical Co. v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Dow Chemical Co. v. United States"
type: case
citation: "476 U.S. 227 (1986)"
parallel_cite: "106 S. Ct. 1819; 90 L. Ed. 2d 226; 16 Envtl. L. Rep. (Envtl. Law Inst.) 20679; 54 U.S.L.W. 4464; 24 ERC (BNA) 1385"
neutral_cite: 1986 U.S. LEXIS 155
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-05-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-05-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Dow Chemical Co. v. United States
  varies_by_point: false
  scope_note: "Good law; the open-areas-as-open-fields/navigable-airspace holding remains the governing rule for aerial observation of commercial and industrial premises."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/"
  cluster_id: 111667
  opinion_id: 9430504
  identity_checked: true
homes:
  - page: "[[Aerial and Enhanced Surveillance]]"
    role: "Key — Anchor"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[California v. Ciraolo]]", "[[Florida v. Riley]]", "[[Oliver v. United States]]", "[[Kyllo v. United States]]"]
aliases: ["Dow Chemical Co. v. United States Ex Rel. Administrator"]
tags: ["case", "fourth-amendment", "search", "aerial-surveillance", "open-fields", "curtilage", "commercial-premises"]
holding: "Precision aerial photography of the open areas of an industrial complex from navigable airspace is not a Fourth Amendment search; such open areas are more like open fields than the curtilage of a home."
lake:
  record_id: Dow Chemical Co. v. United States
  status: verified
  projected_at: 2026-07-09
---

# Dow Chemical Co. v. United States

*476 U.S. 227 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Dow refused a follow-up EPA inspection of its 2,000-acre chemical-manufacturing complex, the EPA hired a commercial aerial photographer who used a precision aerial mapping camera to photograph the plant's open areas from lawful navigable airspace. Dow sued, claiming the overflight photography was a Fourth Amendment search of an "industrial curtilage" in which it had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Issue
Whether the EPA's warrantless taking of aerial photographs of the open areas of an industrial plant complex, from navigable airspace, constitutes a "search" under the Fourth Amendment.

## Rule
No. The open areas of a large industrial complex are not the constitutional equivalent of the [[Curtilage|curtilage]] of a home; "such an industrial complex is more comparable to an open field and as such it is open to the view and observation of persons in aircraft lawfully in the public airspace immediately above or sufficiently near the area for the reach of cameras." — 476 U.S. at 239. ^pin-239

Accordingly, "the taking of aerial photographs of an industrial plant complex from navigable airspace is not a search prohibited by the Fourth Amendment." — [*Id.*](https://www.courtlistener.com/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/#:~:text=the%20taking%20of%20aerial%20photographs) ^pin-239a

## Application
Dow's exposed manufacturing facilities, though enclosed against ground-level intrusion, were open to observation from the air. Because the photographs were taken from lawful navigable airspace using a conventional (if precise) mapping camera, and because the open areas of the complex resembled open fields rather than the intimate [[Curtilage|curtilage]] of a dwelling, Dow had no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] against the overflight. The Court noted only that surveillance revealing intimate, enclosed details — or use of highly sophisticated equipment not generally available — might raise different questions, but the mapping photography here did not.

## Conclusion
The aerial photography was not a Fourth Amendment search. The judgment for the United States was affirmed on the constitutional question.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Decided the same day as [[California v. Ciraolo]] (naked-eye aerial view of a home's [[Curtilage|curtilage]]) and reinforced by [[Florida v. Riley]] (helicopter observation). [[Kyllo v. United States]] (2001) later cabined *sense-enhancing technology* directed at the *home's* interior, distinguishing the open-area/commercial setting here.

## Appears on
- [[Aerial and Enhanced Surveillance]] — *Key — Anchor*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *Dow Chemical Co. v. United States*, 476 U.S. 227 (1986) — https://www.courtlistener.com/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/ — pinpoint: 239.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0ff1637a5f96b873", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Dow Chemical Co. v. United States"}, "payload": {"all": [{"cite": "476 U.S. 227", "page": "227", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "476"}, {"cite": "106 S. Ct. 1819", "page": "1819", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "106"}, {"cite": "90 L. Ed. 2d 226", "page": "226", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "90"}, {"cite": "1986 U.S. LEXIS 155", "page": "155", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1986"}, {"cite": "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679", "page": "20679", "reporter": "Envtl. L. Rep. (Envtl. Law Inst.)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "16"}, {"cite": "54 U.S.L.W. 4464", "page": "4464", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "54"}, {"cite": "24 ERC (BNA) 1385", "page": "1385", "reporter": "ERC (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "24"}], "display": "476 U.S. 227", "official": {"cite": "476 U.S. 227", "page": "227", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "476"}, "official_selection_present": true, "record_id": "Dow Chemical Co. v. United States"}}
{"assertion_id": "036baa06d872068f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-239", "record_id": "Dow Chemical Co. v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-239", "pinpoint_status": "slip-only", "quote": "under the Fourth Amendment. ## Rule No. The open areas of a large industrial complex are not the constitutional equivalent of the curtilage of a home;", "quote_fidelity": "mismatch", "record_id": "Dow Chemical Co. v. United States", "star_marker": null}}
{"assertion_id": "d47be934a0ec2c72", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-239a", "record_id": "Dow Chemical Co. v. United States"}, "payload": {"fragment": "#:~:text=the%20taking%20of%20aerial%20photographs", "page": null, "pin_id": "pin-239a", "pinpoint_status": "star-verified", "quote": "the taking of aerial photographs of an industrial plant complex from navigable airspace is not a search prohibited by the Fourth Amendment.", "quote_fidelity": "matched", "record_id": "Dow Chemical Co. v. United States", "star_marker": "239"}}
{"assertion_id": "8deb0e7149b31271", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Dow Chemical Co. v. United States"}, "payload": {"as_of_content": "1986-05-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Dow Chemical Co. v. United States", "scope_note": "Good law; the open-areas-as-open-fields/navigable-airspace holding remains the governing rule for aerial observation of commercial and industrial premises.", "varies_by_point": false}}
```

### lake record — Dow Chemical Co. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Dow Chemical Co. v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Dow Chemical Co. v. United States Ex Rel. Administrator",
    "case_name_short": "",
    "case_name_full": "DOW CHEMICAL CO. v. UNITED STATES, by and Through ADMINISTRATOR, ENVIRONMENTAL PROTECTION AGENCY",
    "input_case_name": "Dow Chemical Co. v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-05-19",
    "year": 1986,
    "docket": null,
    "cluster_id": 111667,
    "lead_opinion_id": 9430504,
    "sibling_ids": [
      111667,
      9430504,
      9430505
    ],
    "absolute_url": "/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "476 U.S. 227",
      "volume": "476",
      "reporter": "U.S.",
      "page": "227",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1819",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 L. Ed. 2d 226",
        "volume": "90",
        "reporter": "L. Ed. 2d",
        "page": "226",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
        "volume": "16",
        "reporter": "Envtl. L. Rep. (Envtl. Law Inst.)",
        "page": "20679",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4464",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4464",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 ERC (BNA) 1385",
        "volume": "24",
        "reporter": "ERC (BNA)",
        "page": "1385",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 155",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "155",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "476 U.S. 227",
        "volume": "476",
        "reporter": "U.S.",
        "page": "227",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1819",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 L. Ed. 2d 226",
        "volume": "90",
        "reporter": "L. Ed. 2d",
        "page": "226",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 155",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "155",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
        "volume": "16",
        "reporter": "Envtl. L. Rep. (Envtl. Law Inst.)",
        "page": "20679",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4464",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4464",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 ERC (BNA) 1385",
        "volume": "24",
        "reporter": "ERC (BNA)",
        "page": "1385",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "476 U.S. 227",
    "official_selection": {
      "court_class": "scotus",
      "selected": "476 U.S. 227",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-239",
      "page": null,
      "quote": "under the Fourth Amendment. ## Rule No. The open areas of a large industrial complex are not the constitutional equivalent of the curtilage of a home;",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-239a",
      "page": null,
      "quote": "the taking of aerial photographs of an industrial plant complex from navigable airspace is not a search prohibited by the Fourth Amendment.",
      "star_marker": "239",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26872,
      "fragment": "#:~:text=the%20taking%20of%20aerial%20photographs",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-05-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Dow Chemical Co. v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; the open-areas-as-open-fields/navigable-airspace holding remains the governing rule for aerial observation of commercial and industrial premises.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 1978636,
          "cite": [
            "2008 VT 53",
            "955 A.2d 1144",
            "184 Vt. 23",
            "2008 Vt. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Opinion Piedad Barajas-Avaslos",
          "cluster_id": 785295,
          "cite": [
            "359 F.3d 1204",
            "2004 U.S. App. LEXIS 4569",
            "2004 D.A.R. 3084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terry James Pierre and Otis Harris, III",
          "cluster_id": 560501,
          "cite": [
            "932 F.2d 377",
            "1991 U.S. App. LEXIS 10296",
            "1991 WL 82423"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane1_negative"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Riley",
          "cluster_id": 112175,
          "cite": [
            "102 L. Ed. 2d 835",
            "109 S. Ct. 693",
            "488 U.S. 445",
            "1989 U.S. LEXIS 580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio Civil Service Employees Association v. Richard P. Seiter",
          "cluster_id": 512622,
          "cite": [
            "858 F.2d 1171",
            "3 I.E.R. Cas. (BNA) 1623",
            "1988 U.S. App. LEXIS 13585",
            "1988 WL 100808"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hector Hernan Hoyos",
          "cluster_id": 534551,
          "cite": [
            "892 F.2d 1387"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Elkins Carol Elkins, United States of America v. Carol Elkins James Elkins",
          "cluster_id": 778775,
          "cite": [
            "300 F.3d 638"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darlie Kee Darin Routier v. City of Rowlett Texas Jimmy Ray Patterson Chris Frosch Greg Davis, Assistant District Attorney for Dallas County",
          "cluster_id": 772922,
          "cite": [
            "247 F.3d 206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vaughn Neita v. City of Chicago",
          "cluster_id": 4239934,
          "cite": [
            "830 F.3d 494",
            "2016 U.S. App. LEXIS 13191",
            "2016 WL 3905604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Betts, Tony",
          "cluster_id": 2948317,
          "cite": [
            "397 S.W.3d 198",
            "2013 WL 1628963",
            "2013 Tex. Crim. App. LEXIS 705"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Palmieri v. Pamela Lynch, AKA Pam Lynch, John Doe 1",
          "cluster_id": 788624,
          "cite": [
            "392 F.3d 73",
            "2004 U.S. App. LEXIS 25468",
            "2004 WL 2827676"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tom Wilkinson Eastland, and Cullen Reed Harris",
          "cluster_id": 603530,
          "cite": [
            "989 F.2d 760",
            "1993 U.S. App. LEXIS 7723",
            "1993 WL 112732"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wabun-Inini, AKA Vernon Bellecourt v. William Sessions, Director, Federal Bureau of Investigation, Washington, D.C. Jeffrey J. Jamar, Agent-In-Charge, Minneapolis Office of the Fbi, Minneapolis, Minnesota Peter Cunningham, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota William Clifford, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota John Doe Jane Doe, and Other Presently Unknown Officials of the United States Government, Wabun-Inini, AKA Vernon Bellecourt v. William Sessions, Director, Federal Bureau of Investigation, Washington, D.C. Jeffrey J. Jamar, Agent-In-Charge, Minneapolis Office of the Fbi, Minneapolis, Minnesota Peter Cunningham, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota William Clifford, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota John Doe Jane Doe, and Other Presently Unknown Officials of the United States Government",
          "cluster_id": 539907,
          "cite": [
            "900 F.2d 1234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Connolly",
          "cluster_id": 6580040,
          "cite": [
            "454 Mass. 808",
            "913 N.E.2d 356",
            "2009 Mass. LEXIS 642"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Norris",
          "cluster_id": 1079931,
          "cite": [
            "47 S.W.3d 457",
            "2000 Tenn. Crim. App. LEXIS 437",
            "2000 WL 710506"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wacker",
          "cluster_id": 1364515,
          "cite": [
            "856 P.2d 1029",
            "317 Or. 419",
            "1993 Ore. LEXIS 130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Noel C. Jenkins (96-5338) Linda L. Jenkins (96-5346)",
          "cluster_id": 746252,
          "cite": [
            "124 F.3d 768"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ainsworth",
          "cluster_id": 1442371,
          "cite": [
            "801 P.2d 749",
            "310 Or. 613",
            "1990 Ore. LEXIS 361"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson, Lamar v. Quander, Paul A.",
          "cluster_id": 186640,
          "cite": [
            "440 F.3d 489",
            "370 U.S. App. D.C. 167",
            "2006 U.S. App. LEXIS 6601",
            "2006 WL 662748"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dow Chemical Co. v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111667 OR 9430504 OR 9430505) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 145,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 145,
        "triage_read": 4,
        "triage_snippet_classified": 141
      },
      "lane2_top_cited": {
        "query": "cites:(111667 OR 9430504 OR 9430505)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MyZzPTc1MjM1OSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111667+OR+9430504+OR+9430505%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111667 OR 9430504 OR 9430505)",
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
    "complete_query": "cites:(111667 OR 9430504 OR 9430505)",
    "indexed_citing_opinions": 210,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111667,
        "count": 180,
        "count_source": "search"
      },
      {
        "opinion_id": 9430504,
        "count": 39,
        "count_source": "search"
      },
      {
        "opinion_id": 9430505,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 342,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/dow-chemical-co-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3MzQwMSZzPTQ3NDYxMjAmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111667+OR+9430504+OR+9430505%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111667,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 110062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 404175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 445066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111667,
        "cited_id": 2009668,
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
    "date_created": "2026-07-05T02:44:19Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:44:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:44:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:48:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:44:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Dow Chemical Co. v. United States

```
<opinion type="majority">
<author id="b293-4"><page-number citation-index="1" label="229">*229</page-number>Chief Justice Burger</author>
<p id="ALr">delivered the opinion of the Court.</p>
<p id="b293-5">We granted certiorari to review the holding of the Court of Appeals (a) that the Environmental Protection Agency’s aerial observation of petitioner’s plant complex did not exceed EPA’s statutory investigatory authority, and (b) that EPA’s aerial photography of petitioner’s 2,000-acre plant complex without a warrant was not a search under the Fourth Amendment.</p>
<p id="b293-6">I</p>
<p id="b293-7">Petitioner Dow Chemical Co. operates a 2,000-acre facility manufacturing chemicals at Midland, Michigan. The facility consists of numerous covered buildings, with manufacturing equipment and piping conduits located between the various buildings exposed to visual observation from the air. At all times, Dow has maintained elaborate security around the perimeter of the complex barring ground-level public views of these areas. It also investigates any low-level flights by aircraft over the facility. Dow has not undertaken, however, to conceal all manufacturing equipment within the complex from aerial views. Dow maintains that the cost of covering its exposed equipment would be prohibitive.</p>
<p id="b293-8">In early 1978, enforcement officials of EPA, with Dow’s consent, made an on-site inspection of two powerplants in this complex. A subsequent EPA request for a second inspection, however, was denied, and EPA did not thereafter seek an administrative search warrant. Instead, EPA employed a commercial aerial photographer, using a standard floor-mounted, precision aerial mapping camera, to take photographs of the facility from altitudes of 12,000, 3,000, and 1,200 feet. At all times the aircraft was lawfully within navigable airspace. See 49 U. S. C. App. § 1304; <span class="citation no-link">14 CFR § 91.79</span> (1985).</p>
<p id="b294-4"><page-number citation-index="1" label="230">*230</page-number>EPA did not inform Dow of this aerial photography, but when Dow became aware of it, Dow brought suit in the District Court alleging that EPA’s action violated the Fourth Amendment and was beyond EPA’s statutory investigative authority. The District Court granted Dow’s motion for summary judgment on the ground that EPA had no authority to take aerial photographs and that doing so was a search violating the Fourth Amendment. EPA was permanently enjoined from taking aerial photographs of Dow’s premises and from disseminating, releasing, or copying the photographs already taken. <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch">536 F. Supp. 1355</a></span> (ED Mich. 1982).</p>
<p id="b294-5">The District Court accepted the parties’ concession that EPA’s “‘quest for evidence’” was a “search,” <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/#1358" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch"><em>id., </em>at 1358</a></span>, and limited its analysis to whether the search was unreasonable under <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). Proceeding on the assumption that a search in Fourth Amendment terms had been conducted, the court found that Dow manifested an expectation of privacy in its exposed plant areas because it intentionally surrounded them with buildings and other enclosures. <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/#1364" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch">536 F. Supp., at 1364-1366</a></span>.</p>
<p id="b294-6">The District Court held that this expectation of privacy was reasonable, as reflected in part by trade secret protections restricting Dow’s commercial competitors from aerial photography of these exposed areas. <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/#1366" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch"><em>Id., </em>at 1366-1369</a></span>. The court emphasized that use of “the finest precision aerial camera available” permitted EPA to capture on film “a great deal more than the human eye could ever see.” <span class="citation" data-id="2009668"><a href="/opinion/2009668/dow-chemical-co-v-us-by-and-through-gorsuch/#1367" aria-description="Citation for case: Dow Chemical Co. v. US, by and Through Gorsuch"><em>Id., </em>at 1367</a></span>.</p>
<p id="b294-7">The Court of Appeals reversed. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and...">749 F. 2d 307</a></span> (CA6 1984). It recognized that Dow indeed had a subjective expectation of privacy in certain areas from ground-level intrusions, but the court was not persuaded that Dow had a subjective expectation of being free from <em>aerial </em>surveillance since Dow had taken no precautions against such observation, in contrast to its elaborate ground-level precautions. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#313" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 313</a></span>. The court rejected the argument that it was not feasible to shield any of the critical parts of the exposed plant areas from aerial surveys. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#312" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 312-313</a></span>. The Court of Appeals, <page-number citation-index="1" label="231">*231</page-number>however, did not explicitly reject the District Court’s factual finding as to Dow’s subjective expectations.</p>
<p id="b295-5">Accepting the District Court finding of Dow’s privacy expectation, the Court of Appeals held that it was not a reasonable expectation “[w]hen the entity observed is a multibuilding complex, and the area observed is the outside of these buildings and the spaces in between the buildings.” <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#313" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 313</a></span>. Viewing Dow’s facility to be more like the “open field” in <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984), than a home or an office, it held that the common-law curtilage doctrine did not apply to a large industrial complex of closed buildings connected by pipes, conduits, and other exposed manufacturing equipment. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#313" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and...">749 F. 2d, at 313-314</a></span>. The Court of Appeals looked to “the peculiarly strong concepts of intimacy, personal autonomy and privacy associated with the home” as the basis for the curtilage protection. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#314" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 314</a></span>. The court did not view the use of sophisticated photographic equipment by EPA as controlling.</p>
<p id="Abd">The Court of Appeals then held that EPA clearly acted within its statutory powers even absent express authorization for aerial surveillance, concluding that the delegation of general investigative authority to EPA, similar to that of other law enforcement agencies, was sufficient to support the use of aerial photography. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#315" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and..."><em>Id., </em>at 315</a></span>.</p>
<p id="b295-7">II</p>
<p id="b295-8">The photographs at issue in this case are essentially like those commonly used in mapmaking. Any person with an airplane and an aerial camera could readily duplicate them. In common with much else, the technology of photography has changed in this century. These developments have enhanced industrial processes, and indeed all areas of life; they have also enhanced law enforcement techniques. Whether they may be employed by competitors to penetrate trade secrets is not a question presented in this case. Governments do not generally seek to appropriate trade secrets of the pri<page-number citation-index="1" label="232">*232</page-number>vate sector, and the right to be free of appropriation of trade secrets is protected by law.</p>
<p id="b296-5">Dow nevertheless relies heavily on its claim that trade secret laws protect it from any aerial photography of this industrial complex by its competitors, and that this protection is relevant to our analysis of such photography under the Fourth Amendment. That such photography might be barred by state law with regard to competitors, however, is irrelevant to the questions presented here. State tort law governing unfair competition does not define the limits of the Fourth Amendment. Cf. <em>Oliver </em>v. <em>United States, supra </em>(trespass law does not necessarily define limits of Fourth Amendment). The Government is seeking these photographs in order to regulate, not to compete with, Dow. If the Government were to use the photographs to compete with Dow, Dow might have a Fifth Amendment “taking” claim. Indeed, Dow alleged such a claim in its complaint, but the District Court dismissed it without prejudice. But even trade secret laws would not bar all forms of photography of this industrial complex; rather, only photography with an intent to use any trade secrets revealed by the photographs may be proscribed. Hence, there is no prohibition of photographs taken by a casual passenger on an airliner, or those taken by a company producing maps for its mapmaking purposes.</p>
<p id="b296-6">Dow claims first that EPA has no authority to use aerial photography to implement its statutory authority for “site inspection” under § 114(a) of the Clean Air Act, <span class="citation no-link">42 U. S. C. § 7414</span>(a);<footnotemark>1</footnotemark> second, Dow claims EPA’s use of aerial photogra<page-number citation-index="1" label="233">*233</page-number>phy was a “search” of an area that, notwithstanding the large size of the plant, was within an “industrial curtilage” rather than an “open field,” and that it had a reasonable expectation of privacy from such photography protected by the Fourth Amendment.</p>
<p id="b297-4">Ill</p>
<p id="b297-5">Congress has vested in EPA certain investigatory and enforcement authority, without spelling out precisely how this authority was to be exercised in all the myriad circumstances that might arise in monitoring matters relating to clean air and water standards. When Congress invests an agency with enforcement and investigatory authority, it is not necessary to identify explicitly each and every technique that may be used in the course of executing the statutory mission. Aerial observation authority, for example, is not usually expressly extended to police for traffic control, but it could hardly be thought necessary for a legislative body to tell police that aerial observation could be employed for traffic control of a metropolitan area, or to expressly authorize police to send messages to ground highway patrols that a particular over-the-road truck was traveling in excess of 55 miles per hour. Common sense and ordinary human experience teach that traffic violators are apprehended by observation.</p>
<p id="b297-6">Regulatory or enforcement authority generally carries with it all the modes of inquiry and investigation traditionally employed or useful to execute the authority granted. Environmental standards such as clean air and clean water cannot be enforced only in libraries and laboratories, helpful as those institutions may be.</p>
<p id="b297-7">Under § 114(a)(2), the Clean Air Act provides that “upon presentation of. . . credentials,” EPA has a “right of entry to, upon, or through any premises.” <span class="citation no-link">42 U. S. C. § 7414</span>(a)(2)(A). Dow argues this limited grant of authority to enter does not <page-number citation-index="1" label="234">*234</page-number>authorize any aerial observation. In particular, Dow argues that unannounced aerial observation deprives Dow of its right to be informed that an inspection will be made or has occurred, and its right to claim confidentiality of the information contained in the places to be photographed, as provided in §§ 114(a) and (c), <span class="citation no-link">42 U. S. C. §§ 7414</span>(a) and (c). It is not claimed that EPA has disclosed any of the photographs outside the agency.</p>
<p id="b298-5">Section 114(a), however, appears to expand, not restrict, EPA’s general powers to investigate. Nor is there any suggestion in the statute that the powers conferred by this section are intended to be exclusive. There is no claim that EPA is prohibited from taking photographs from a ground-level location accessible to the general public. EPA, as a regulatory and enforcement agency, needs no explicit statutory provision to employ methods of observation commonly available to the public at large: we hold that the use of aerial observation and photography is within EPA’s statutory authority.<footnotemark>2</footnotemark></p>
<p id="b298-6">IV</p>
<p id="b298-7">We turn now to Dow’s contention that taking aerial photographs constituted a search without a warrant, thereby violating Dow’s rights under the Fourth Amendment. In making this contention, however, Dow concedes that a simple flyover with naked-eye observation, or the taking of a photograph from a nearby hillside overlooking such a facility, would give rise to no Fourth Amendment problem.</p>
<p id="b298-8">In <em>California </em>v. <em>Ciraolo, ante, </em>p. 207, decided today, we hold that naked-eye aerial observation from an altitude of <page-number citation-index="1" label="235">*235</page-number>1,000 feet of a backyard within the curtilage of a home does not constitute a search under the Fourth Amendment.</p>
<p id="b299-5">In the instant case, two additional Fourth Amendment claims are presented: whether the common-law “curtilage” doctrine encompasses a large industrial complex such as Dow’s, and whether photography employing an aerial mapping camera is permissible in this context. Dow argues that an industrial plant, even one occupying 2,000 acres, does not fall within the “open fields” doctrine of <em>Oliver </em>v. <em>United States </em>but rather is an “industrial curtilage” having constitutional protection equivalent to that of the curtilage of a private home. Dow farther contends that any aerial photography of this “industrial curtilage” intrudes upon its reasonable expectations of privacy. Plainly a business establishment or an industrial or commercial facility enjoys certain protections under the Fourth Amendment. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978); <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967).</p>
<p id="b299-6">Two lines of cases are relevant to the inquiry: the curtilage doctrine and the “open fields” doctrine. The curtilage area immediately surrounding a private house has long been given protection as a place where the occupants have a reasonable and legitimate expectation of privacy that society is prepared to accept. See <em>Ciraolo, supra.</em></p>
<p id="b299-7">As the curtilage doctrine evolved to protect much the same kind of privacy as that covering the interior of a structure, the contrasting “open fields” doctrine evolved as well. From <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), to <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984), the Court has drawn a fine as to what expectations are reasonable in the open areas beyond the curtilage of a dwelling: “open fields do not provide the setting for those intimate activities that the [Fourth] Amendment is intended to shelter from governmental interference or surveillance.” <em>Oliver, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#179" aria-description="Citation for case: Oliver v. United States">466 U. S., at 179</a></span>. In <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span>, </em>we held that “an individual may not legitimately demand privacy for activities out of doors in fields, except in the area <page-number citation-index="1" label="236">*236</page-number>immediately surrounding the home.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 178</a></span>. To fall within the “open fields” doctrine the area “need be neither ‘open’ nor a ‘field’ as those terms are used in common speech.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#180" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 180, n. 11</a></span>.</p>
<p id="b300-5">Dow plainly has a reasonable, legitimate, and objective expectation of privacy within the interior of its covered buildings, and it is equally clear that expectation is one society is prepared to observe. <em>E. g., See </em>v. <em>City of <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">Seattle, supra.</a></span> </em>Moreover, it could hardly be expected that Dow would erect a huge cover over a 2,000-acre tract. In contending that its entire enclosed plant complex is an “industrial curtilage,” Dow argues that its exposed manufacturing facilities are analogous to the curtilage surrounding a home because it has taken every possible step to bar access from ground level.</p>
<p id="b300-6">The Court of Appeals held that whatever the limits of an “industrial curtilage” barring ground-level intrusions into Dow’s private areas, the open areas exposed here were more analogous to “open fields” than to a curtilage for purposes of aerial observation. <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#312" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and...">749 F. 2d, at 312-314</a></span>. In <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span>, </em>the Court described the curtilage of a dwelling as “the area to which extends the intimate activity associated with the ‘sanctity of a man’s home and the privacies of life.’” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S., at 180</a></span> (quoting <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886)). See <em>California </em>v. <em>Ciraolo, supra. </em>The intimate activities associated with family privacy and the home and its curtilage simply do not reach the outdoor areas or spaces between structures and buildings of a manufacturing plant.</p>
<p id="b300-7">Admittedly, Dow’s enclosed plant complex, like the area in <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span>, </em>does not fall precisely within the “open fields” doctrine. The area at issue here can perhaps be seen as falling somewhere between “open fields” and curtilage, but lacking some of the critical characteristics of both.<footnotemark>3</footnotemark> Dow’s inner <page-number citation-index="1" label="237">*237</page-number>manufacturing areas are elaborately secured to ensure they are not open or exposed to the public from the ground. Any actual physical entry by EPA into any enclosed area would raise significantly different questions, because “[t]he businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property.” <em>See </em>v. <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle"><em>City of Seattle, supra, </em>at 543</a></span>. The narrow issue raised by Dow’s claim of search and seizure, however, concerns aerial observation of a 2,000-acre outdoor manufacturing facility <em>without </em>physical entry.<footnotemark>4</footnotemark></p>
<p id="b301-5">We pointed out in <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#598" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 598-599</a></span> (1981), that the Government has “greater latitude to conduct warrantless inspections of commercial property” because “the expectation of privacy that the owner of commercial property enjoys.in such property differs significantly <page-number citation-index="1" label="238">*238</page-number>from the sanctity accorded an individual’s home.” We emphasized that unlike a homeowner’s interest in his dwelling, “[t]he interest of the owner of commercial property is not one in being free from any inspections.” <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#599" aria-description="Citation for case: Donovan v. Dewey"><em>Id., </em>at 599</a></span>. And with regard to regulatory inspections, we have held that “[w]hat is observable by the public is observable without a warrant, by the Government inspector as well.” <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#315" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 315</a></span> (footnote omitted).</p>
<p id="b302-5"><em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>recognized that in the open field context, “the public and police lawfully may survey lands from the air.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#179" aria-description="Citation for case: Oliver v. United States">466 U. S., at 179</a></span> (footnote omitted). Here, EPA was not employing some unique sensory device that, for example, could penetrate the walls of buildings and record conversations in Dow’s plants, offices, or laboratories, but rather a conventional, albeit precise, commercial camera commonly used in mapmaking. The Government asserts it has not yet enlarged the photographs to any significant degree, but Dow points out that simple magnification permits identification of objects such as wires as small as inch in diameter.</p>
<p id="b302-6">It may well be, as the Government concedes, that surveillance of private property by using highly sophisticated surveillance equipment not generally available to the public, such as satellite technology, might be constitutionally proscribed absent a warrant. But the photographs here are not so revealing of intimate details as to raise constitutional concerns. Although they undoubtedly give EPA more detailed information than naked-eye views, they remain limited to an outline of the facility’s buildings and equipment. The mere fact that human vision is enhanced somewhat, at least to the degree here, does not give rise to constitutional problems.<footnotemark>5</footnotemark> <page-number citation-index="1" label="239">*239</page-number>An electronic device to penetrate walls or windows so as to hear and record confidential discussions of chemical formulae or other trade secrets would raise very different and far more serious questions; other protections such as trade secret laws are available to protect commercial activities from private surveillance by competitors.<footnotemark>6</footnotemark></p>
<p id="b303-5">We conclude that the open areas of an industrial plant complex with numerous plant structures spread over an area of 2,000 acres are not analogous to the “curtilage” of a dwelling for purposes of aerial surveillance;<footnotemark>7</footnotemark> such an industrial complex is more comparable to an open field and as such it is open to the view and observation of persons in aircraft lawfully in the public airspace immediately above or sufficiently near the area for the reach of cameras.</p>
<p id="b303-6">We hold that the taking of aerial photographs of an industrial plant complex from navigable airspace is not a search prohibited by the Fourth Amendment.</p>
<p id="b303-7">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b296-7"> Section 114(a)(2) provides:</p>
<blockquote id="b296-8">“(2) the Administrator or his authorized representative, upon presentation of his credentials —</blockquote>
<blockquote id="b296-9">“(A) shall have a right of entry to, upon, or through any premises of such person or in which any records required to be maintained under paragraph (1) of this section are located, and</blockquote>
<blockquote id="b296-10">“(B) may at reasonable times have access to and copy any records, inspect any monitoring equipment or method required under paragraph (1), <page-number citation-index="1" label="233">*233</page-number>and sample any emissions which such person is required to sample under paragraph (1).”</blockquote>
</footnote>
<footnote label="2">
<p id="b298-9"> Assuming the Clean Air Act’s explicit provisions for protecting trade secrets obtained by EPA as the result of its investigative efforts is somehow deemed inapplicable to the information obtained here, see <span class="citation no-link">42 U. S. C. § 7414</span>(e), Dow’s fear that EPA might disclose trade secrets revealed in these photographs appears adequately addressed by federal law prohibiting such disclosure generally under the Trade Secrets Act, <span class="citation no-link">18 U. S. C. § 1905</span>, and the Freedom of Information Act, <span class="citation no-link">5 U. S. C. § 552</span>(b)(4). See <em>Chrysler Corp. </em>v. <em>Brown, </em><span class="citation" data-id="9427540"><a href="/opinion/110062/chrysler-corp-v-brown/" aria-description="Citation for case: Chrysler Corp. v. Brown">441 U. S. 281</a></span> (1979).</p>
</footnote>
<footnote label="3">
<p id="b300-8"> In <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span>, </em>we observed that “for most homes, the boundaries of the curtilage will be clearly marked; and the conception defining the curtilage — as the area around the home to which the activity of home life extends — is a familiar one easily understood from our daily experience.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States">466 <page-number citation-index="1" label="237">*237</page-number>U. S., at 182, n. 12</a></span>. While we did not attempt to definitively mark the boundaries of what constitutes an open field, we noted that “[i]t is clear . . . that the term ‘open fields’ may include any unoccupied or undeveloped area outside of the curtilage.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#180" aria-description="Citation for case: Oliver v. United States"><em>Id., </em>at 180, n. 11</a></span>. As <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>recognized, the curtilage surrounding a home is generally a well-defined, limited area. In stark contrast, the areas for which Dow claims enhanced protection cover the equivalent of a half dozen family farms.</p>
</footnote>
<footnote label="4">
<p id="b301-9"> We find it important that this is <em>not </em>an area immediately adjacent to a private home, where privacy expectations are most heightened. Nor is this an area where Dow has made any effort to protect against aerial surveillance. Contrary to the partial dissent’s understanding, <em>post, </em>at 241-242, the Court of Appeals emphasized:</p>
<blockquote id="b301-10">“Dow did not take <em>any </em>precautions against aerial intrusions, even though the plant was near an airport and within the pattern of planes landing and taking off. If elaborate and expensive measures for ground security show that Dow has an actual expectation of privacy in ground security, as Dow argues, then taking <em>no </em>measure for aerial security should say something about its actual privacy expectation in being free from aerial observation.” <span class="citation" data-id="445066"><a href="/opinion/445066/dow-chemical-company-v-united-states-of-america-by-and-through-anne-m/#312" aria-description="Citation for case: Dow Chemical Company v. United States of America, by and...">749 F. 2d 307, 312</a></span> (CA6 1984) (emphasis added).</blockquote>
<p id="AS2">Simply keeping track of the identification numbers of any planes flying overhead, with a later followup to see if photographs were taken, does not constitute a “procedur[e] designed to protect the facility from aerial photography.” <em>Post, </em>at 241.</p>
</footnote>
<footnote label="5">
<p id="b302-7"> The partial dissent emphasizes Dow’s claim that under magnification power lines as small as Vz-ineh in diameter can be observed. <em>Post, </em>at 243. But a glance at the photographs in issue shows that those power lines are observable only because of their stark contrast with the snow-white background. No objects as small as 72-inch in diameter such as a class ring, for example, are recognizable, nor are there any identifiable human faces or <page-number citation-index="1" label="239">*239</page-number>secret documents captured in such a fashion as to implicate more serious privacy concerns. Fourth Amendment eases must be decided on the facts of each case, not by extravagant generalizations. “[W]e have never held that potential, as opposed to actual, invasions of privacy constitute searches for purposes of the Fourth Amendment.” <em>United States </em>v. <em>Karo, </em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#712" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 712</a></span> (1984). On these facts, nothing in these photographs suggests that any reasonable expectations of privacy have been infringed.</p>
</footnote>
<footnote label="6">
<p id="b303-13"> The partial dissent relies heavily on Dow’s claim that aerial photography of its facility is proscribed by trade secret laws. <em>Post, </em>at 248-249, and n. 11. While such laws may protect against use of photography by competitors in the same trade to advance their commercial interests, in no manner do “those laws constitute society’s express determination” that <em>all </em>photography of Dow’s facility violates reasonable expectations of privacy. <em>Post, </em>at 249. No trade secret law cited to us by Dow proscribes the use of aerial photography of Dow’s facilities for law enforcement purposes, let alone photography for private purposes unrelated to competition such as map-making or simple amateur snapshots. See <em>swpra, </em>at 232.</p>
</footnote>
<footnote label="7">
<p id="b303-14"> Our holding here does not reach the issues raised by the Court of Appeals for the Seventh Circuit’s holding regarding a “business curtilage” in <em>United States </em>v. <em>Swart, </em><span class="citation" data-id="404175"><a href="/opinion/404175/united-states-v-dale-a-swart/" aria-description="Citation for case: United States v. Dale A. Swart">679 F. 2d 698</a></span> (CA7 1982); that case involved actual physical entry onto the business premises.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Doyle v. Ohio.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Doyle v. Ohio"
type: case
citation: "426 U.S. 610 (1976)"
parallel_cite: "96 S. Ct. 2240; 49 L. Ed. 2d 91"
neutral_cite: 1976 U.S. LEXIS 66
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-06-17
docket: 75-5014
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Doyle v. Ohio
  varies_by_point: false
  scope_note: "Good law; cabined to post-Miranda silence (see Jenkins v. Anderson, Fletcher v. Weir, Salinas) but the core Doyle rule is intact."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109491/doyle-v-ohio/"
  cluster_id: 109491
  opinion_id: 109491
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Harris v. New York]]", "[[Miranda v. Arizona]]", "[[Salinas v. Texas]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "miranda", "silence", "impeachment", "due-process"]
holding: "Using a defendant's post-arrest, post-Miranda silence to impeach his exculpatory trial testimony violates the Due Process Clause, because the Miranda warnings carry an implicit assurance that silence will carry no penalty."
lake:
  record_id: Doyle v. Ohio
  status: verified
  projected_at: 2026-07-06
---

# Doyle v. Ohio

*426 U.S. 610 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Doyle and a codefendant were arrested for selling marijuana and given [[Miranda and Custodial Interrogation|Miranda warnings]]. They said nothing at arrest. At trial each testified to an [[Brady and Giglio|exculpatory]] story (that they had been framed). On cross-examination the prosecutor impeached them by asking why, if their story were true, they had not told it to the arresting officer at the time of arrest.

## Issue
Whether a state prosecutor may use a defendant's silence at the time of arrest, after [[Miranda and Custodial Interrogation|Miranda warnings]] were given, to impeach an [[Brady and Giglio|exculpatory]] account the defendant offers for the first time at trial.

## Rule
No. Using post-arrest, post-*[[Miranda v. Arizona|Miranda]]* silence to impeach violates due process. Post-arrest silence following [[Miranda and Custodial Interrogation|Miranda warnings]] is "insolubly ambiguous" because it may be nothing more than the arrestee's exercise of his *[[Miranda v. Arizona|Miranda]]* rights. — 426 U.S. at 617. ^pin-617

"[W]hile it is true that the *Miranda* warnings contain no express assurance that silence will carry no penalty, such assurance is implicit to any person who receives the warnings. In such circumstances, it would be fundamentally unfair and a deprivation of due process to allow the arrested person's silence to be used to impeach an explanation subsequently offered at trial." — *Id.* at 618. ^pin-618

## Application
Doyle and his codefendant were given [[Miranda and Custodial Interrogation|Miranda warnings]] and then stayed silent at arrest. The State used that silence on cross-examination to suggest their trial testimony was a recent fabrication. Because the warnings implicitly assured them that silence carried no penalty, using that silence against them was fundamentally unfair and violated the Fourteenth Amendment's Due Process Clause.

## Conclusion
The impeachment use of post-arrest, post-*[[Miranda v. Arizona|Miranda]]* silence violated due process; the convictions were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Doyle* is cabined to silence after [[Miranda and Custodial Interrogation|Miranda warnings]]: impeachment with **pre-arrest** silence (Jenkins v. Anderson) and with **post-arrest but pre-Miranda** silence (Fletcher v. Weir) does not offend *Doyle*; see also [[Salinas v. Texas]] (pre-custody silence). The core *Doyle* rule remains good law.
- Contrast [[Harris v. New York]]: a voluntary statement taken in violation of Miranda may impeach, but *Doyle* bars impeachment by the silence itself.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Doyle v. Ohio*, 426 U.S. 610 (1976) — https://www.courtlistener.com/opinion/109491/doyle-v-ohio/ — pinpoints: 617, 618.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c61e3b195b53987b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Doyle v. Ohio"}, "payload": {"all": [{"cite": "426 U.S. 610", "page": "610", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "426"}, {"cite": "96 S. Ct. 2240", "page": "2240", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "49 L. Ed. 2d 91", "page": "91", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "1976 U.S. LEXIS 66", "page": "66", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "426 U.S. 610", "official": {"cite": "426 U.S. 610", "page": "610", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "426"}, "official_selection_present": true, "record_id": "Doyle v. Ohio"}}
{"assertion_id": "44b73c77ed456fac", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-617", "record_id": "Doyle v. Ohio"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-617", "pinpoint_status": "slip-only", "quote": "--- # Doyle v. Ohio *426 U.S. 610 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Doyle and a codefendant were arrested for selling marijuana and given Miranda warnings. They said nothing at arrest. At trial each testified to an exculpatory story (that they had been framed). On cross-examination the prosecutor impeached them by asking why, if their story were true, they had not told it to the arresting officer at the time of arrest. ## Issue Whether a state prosecutor may use a defendant's silence at the time of arrest, after Miranda warnings were given, to impeach an exculpatory account the defendant offers for the first time at trial. ## Rule No. Using post-arrest, post-*Miranda* silence to impeach violates due process. Post-arrest silence following Miranda warnings is", "quote_fidelity": "mismatch", "record_id": "Doyle v. Ohio", "star_marker": null}}
{"assertion_id": "9bf9ae373ac5bc93", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-618", "record_id": "Doyle v. Ohio"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-618", "pinpoint_status": "slip-only", "quote": "[W]hile it is true that the *Miranda* warnings contain no express assurance that silence will carry no penalty, such assurance is implicit to any person who receives the warnings. In such circumstances, it would be fundamentally unfair and a deprivation of due process to allow the arrested person's silence to be used to impeach an explanation subsequently offered at trial.", "quote_fidelity": "mismatch", "record_id": "Doyle v. Ohio", "star_marker": null}}
{"assertion_id": "0fa8ace7674df7f3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Doyle v. Ohio"}, "payload": {"as_of_content": "1976-06-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Doyle v. Ohio", "scope_note": "Good law; cabined to post-Miranda silence (see Jenkins v. Anderson, Fletcher v. Weir, Salinas) but the core Doyle rule is intact.", "varies_by_point": false}}
```

### lake record — Doyle v. Ohio

```json
{
  "schema_version": "s2.v1",
  "record_id": "Doyle v. Ohio",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Doyle v. Ohio",
    "case_name_short": "Doyle",
    "case_name_full": "Doyle v. Ohio",
    "input_case_name": "Doyle v. Ohio",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-06-17",
    "year": 1976,
    "docket": "75-5014",
    "cluster_id": 109491,
    "lead_opinion_id": 109491,
    "sibling_ids": [
      109491,
      9426459,
      9426460
    ],
    "absolute_url": "/opinion/109491/doyle-v-ohio/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "426 U.S. 610",
      "volume": "426",
      "reporter": "U.S.",
      "page": "610",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 2240",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2240",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 91",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 66",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "426 U.S. 610",
        "volume": "426",
        "reporter": "U.S.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 2240",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2240",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 91",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 66",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "426 U.S. 610",
    "official_selection": {
      "court_class": "scotus",
      "selected": "426 U.S. 610",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-617",
      "page": null,
      "quote": "--- # Doyle v. Ohio *426 U.S. 610 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Doyle and a codefendant were arrested for selling marijuana and given Miranda warnings. They said nothing at arrest. At trial each testified to an exculpatory story (that they had been framed). On cross-examination the prosecutor impeached them by asking why, if their story were true, they had not told it to the arresting officer at the time of arrest. ## Issue Whether a state prosecutor may use a defendant's silence at the time of arrest, after Miranda warnings were given, to impeach an exculpatory account the defendant offers for the first time at trial. ## Rule No. Using post-arrest, post-*Miranda* silence to impeach violates due process. Post-arrest silence following Miranda warnings is",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-618",
      "page": null,
      "quote": "[W]hile it is true that the *Miranda* warnings contain no express assurance that silence will carry no penalty, such assurance is implicit to any person who receives the warnings. In such circumstances, it would be fundamentally unfair and a deprivation of due process to allow the arrested person's silence to be used to impeach an explanation subsequently offered at trial.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Doyle v. Ohio",
    "varies_by_point": false,
    "scope_note": "Good law; cabined to post-Miranda silence (see Jenkins v. Anderson, Fletcher v. Weir, Salinas) but the core Doyle rule is intact.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. Sharrieff M. Kent",
          "cluster_id": 9487155,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Morris",
          "cluster_id": 9415465,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
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
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rivera",
          "cluster_id": 4743993,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sesmas",
          "cluster_id": 4735753,
          "cite": [
            "459 P.3d 1265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Orr",
          "cluster_id": 10367163,
          "cite": [
            "305 Ga. 729"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Randle",
          "cluster_id": 4523033,
          "cite": [
            "2018 SD 61",
            "916 N.W.2d 461"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane1_negative"
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
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
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
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
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
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
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
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dinkins v. State",
          "cluster_id": 1688238,
          "cite": [
            "894 S.W.2d 330",
            "1995 Tex. Crim. App. LEXIS 9",
            "1995 WL 40331"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Anderson",
          "cluster_id": 110298,
          "cite": [
            "65 L. Ed. 2d 86",
            "100 S. Ct. 2124",
            "447 U.S. 231",
            "1980 U.S. LEXIS 131"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Neville",
          "cluster_id": 110832,
          "cite": [
            "74 L. Ed. 2d 748",
            "103 S. Ct. 916",
            "459 U.S. 553",
            "1983 U.S. LEXIS 129",
            "51 U.S.L.W. 4148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greer v. Miller",
          "cluster_id": 111956,
          "cite": [
            "97 L. Ed. 2d 618",
            "107 S. Ct. 3102",
            "483 U.S. 756",
            "1987 U.S. LEXIS 2930"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orange Jell Beechum",
          "cluster_id": 358983,
          "cite": [
            "582 F.2d 898",
            "1978 U.S. App. LEXIS 8198",
            "3 Fed. R. Serv. 1185"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Osband",
          "cluster_id": 5607850,
          "cite": [
            "13 Cal. 4th 622",
            "919 P.2d 640",
            "96 Daily Journal DAR 9137",
            "96 Cal. Daily Op. Serv. 5583",
            "55 Cal. Rptr. 2d 26",
            "1996 Cal. LEXIS 3814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Charles",
          "cluster_id": 110306,
          "cite": [
            "65 L. Ed. 2d 222",
            "100 S. Ct. 2180",
            "447 U.S. 404",
            "1980 U.S. LEXIS 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 844247,
          "cite": [
            "52 Cal. 4th 856",
            "261 P.3d 243",
            "131 Cal. Rptr. 3d 225",
            "2011 Cal. LEXIS 8769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Greenfield",
          "cluster_id": 111553,
          "cite": [
            "88 L. Ed. 2d 623",
            "106 S. Ct. 634",
            "474 U.S. 284",
            "1986 U.S. LEXIS 41",
            "54 U.S.L.W. 4077"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fletcher v. Weir",
          "cluster_id": 110668,
          "cite": [
            "71 L. Ed. 2d 490",
            "102 S. Ct. 1309",
            "455 U.S. 603",
            "1982 U.S. LEXIS 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roberts v. United States",
          "cluster_id": 110234,
          "cite": [
            "63 L. Ed. 2d 622",
            "100 S. Ct. 1358",
            "445 U.S. 552",
            "1980 U.S. LEXIS 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Crittenden",
          "cluster_id": 2614001,
          "cite": [
            "885 P.2d 887",
            "9 Cal. 4th 83",
            "36 Cal. Rptr. 2d 474",
            "94 Daily Journal DAR 18013",
            "94 Cal. Daily Op. Serv. 9702",
            "1994 Cal. LEXIS 6570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hughes",
          "cluster_id": 2581420,
          "cite": [
            "39 P.3d 432",
            "116 Cal. Rptr. 2d 401",
            "27 Cal. 4th 287"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
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
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marvin Baker",
          "cluster_id": 77176,
          "cite": [
            "432 F.3d 1189",
            "2005 WL 3369204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Antwine",
          "cluster_id": 2364064,
          "cite": [
            "743 S.W.2d 51",
            "1987 Mo. LEXIS 374",
            "1987 WL 2721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Rundle",
          "cluster_id": 2633881,
          "cite": [
            "180 P.3d 224",
            "74 Cal. Rptr. 3d 454",
            "43 Cal. 4th 76",
            "2008 Cal. LEXIS 3795"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Monroe",
          "cluster_id": 4764609,
          "cite": [
            "468 P.3d 1273",
            "2020 CO 67"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heidelberg v. State",
          "cluster_id": 2120437,
          "cite": [
            "144 S.W.3d 535",
            "2004 Tex. Crim. App. LEXIS 1479",
            "2004 WL 2109065"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Glasper",
          "cluster_id": 2027353,
          "cite": [
            "917 N.E.2d 401",
            "234 Ill. 2d 173",
            "334 Ill. Dec. 575",
            "2009 Ill. LEXIS 933"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Doyle v. Ohio:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109491 OR 9426459 OR 9426460) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMyMDQ0ODAwMDAwJnM9NDUxOTA2MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109491+OR+9426459+OR+9426460%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(109491 OR 9426459 OR 9426460)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMzkmcz0yODQ1OCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109491+OR+9426459+OR+9426460%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109491 OR 9426459 OR 9426460)",
        "reviewed": 64,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 64,
        "triage_read": 2,
        "triage_snippet_classified": 62
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109491 OR 9426459 OR 9426460)",
    "indexed_citing_opinions": 2961,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109491,
        "count": 2633,
        "count_source": "search"
      },
      {
        "opinion_id": 9426459,
        "count": 386,
        "count_source": "search"
      },
      {
        "opinion_id": 9426460,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4773,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/doyle-v-ohio.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMjQ2MjUmcz0xMDMzNjQxOCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109491+OR+9426459+OR+9426460%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109491,
        "cited_id": 95301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 100906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 103779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 105508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 105661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 105925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 106219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 109101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 109289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 279002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
        "cited_id": 323043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109491,
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
    "date_created": "2026-07-05T02:48:28Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:48:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:48:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:53:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:48:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Doyle v. Ohio

```
<div>
<center><b><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">426 U.S. 610</a></span> (1976)</b></center>
<center><h1>DOYLE<br>
v.<br>
OHIO.</h1></center>
<center>No. 75-5014.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 23, 1976.</center>
<center>Decided June 17, 1976.<sup>[*]</sup></center>
CERTIORARI TO THE COURT OF APPEALS OF OHIO, TUSCARAWAS COUNTY.
<p><i>James R. Willis</i> argued the cause for petitioners and filed briefs in both cases.</p>
<p><i>Ronald L. Collins</i> argued the cause <i>pro hac vice</i> and filed a brief for respondent in both cases.<sup>[]</sup></p>
<p><span class="star-pagination">*611</span> MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>The question in these consolidated cases is whether a state prosecutor may seek to impeach a defendant's exculpatory story, told for the first time at trial, by cross-examining the defendant about his failure to have told the story after receiving <i>Miranda</i> warnings<sup>[1]</sup> at the time of his arrest. We conclude that use of the defendant's post-arrest silence in this manner violates due process, and therefore reverse the convictions of both petitioners.</p>
<p></p>
<h2>I</h2>
<p>Petitioners Doyle and Wood were arrested together and charged with selling 10 pounds of marihuana to a local narcotics bureau informant. They were convicted in the Common Pleas Court of Tuscarawas County, Ohio, in separate trials held about one week apart. The evidence at their trials was identical in all material respects.</p>
<p>The State's witnesses sketched a picture of a routine marihuana transaction. William Bonnell, a well-known "street person" with a long criminal record, offered to assist the local narcotics investigation unit in setting up drug "pushers" in return for support in his efforts to receive lenient treatment in his latest legal problems. The narcotics agents agreed. A short time later, Bonnell advised the unit that he had arranged a "buy" of 10 pounds of marihuana and needed $1,750 to pay for it. Since the banks were closed and time was short, the agents were able to collect only $1,320. Bonnell took this money and left for the rendezvous, under surveillance by four narcotics agents in two cars. As planned, he met petitioners in a bar in Dover, Ohio. From there, he and petitioner Wood drove in Bonnell's <span class="star-pagination">*612</span> pickup truck to the nearby town of New Philadelphia, Ohio, while petitioner Doyle drove off to obtain the marihuana and then meet them at a prearranged location in New Philadelphia. The narcotics agents followed the Bonnell truck. When Doyle arrived at Bonnell's waiting truck in New Philadelphia, the two vehicles proceeded to a parking lot where the transaction took place. Bonnell left in his truck, and Doyle and Wood departed in Doyle's car. They quickly discovered that they had been paid $430 less than the agreed-upon price, and began circling the neighborhood looking for Bonnell. They were stopped within minutes by New Philadelphia police acting on radioed instructions from the narcotics agents. One of those agents, Kenneth Beamer, arrived on the scene promptly, arrested petitioners, and gave them <i>Miranda</i> warnings. A search of the car, authorized by warrant, uncovered the $1,320.</p>
<p>At both trials, defense counsel's cross-examination of the participating narcotics agents was aimed primarily at establishing that, due to a limited view of the parking lot, none of them had seen the actual transaction but had seen only Bonnell standing next to Doyle's car with a package under his arm, presumably after the transaction.<sup>[2]</sup> Each petitioner took the stand at his trial and admitted practically everything about the State's case except the most crucial point: who was <span class="star-pagination">*613</span> selling marihuana to whom. According to petitioners, Bonnell had framed them. The arrangement had been for Bonnell to sell Doyle 10 pounds of marihuana. Doyle had left the Dover bar for the purpose of borrowing the necessary money, but while driving by himself had decided that he only wanted one or two pounds instead of the agreed-upon 10 pounds. When Bonnell reached Doyle's car in the New Philadelphia parking lot, with the marihuana under his arm, Doyle tried to explain his change of mind. Bonnell grew angry, threw the $1,320 into Doyle's car, and took all 10 pounds of the marihuana back to his truck. The ensuing chase was the effort of Wood and Doyle to catch Bonnell to find out what the $1,320 was all about.</p>
<p>Petitioners' explanation of the events presented some difficulty for the prosecution, as it was not entirely implausible and there was little if any direct evidence to contradict it.<sup>[3]</sup> As part of a wide-ranging cross-examination for impeachment purposes, and in an effort to undercut the explanation, the prosecutor asked each petitioner at his respective trial why he had not told the frameup story to Agent Beamer when he arrested petitioners. In the first trial, that of petitioner Wood, the following colloquy occurred:<sup>[4]</sup></p>
<blockquote>"Q. [By the prosecutor.] Mr. Beamer did arrive on the scene?</blockquote>
<blockquote>"A. [By Wood.] Yes, he did.</blockquote>
<blockquote>"Q. And I assume you told him all about what happened to you?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. No.</blockquote>
<blockquote>
<span class="star-pagination">*614</span> "Q. You didn't tell Mr. Beamer?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. No.</blockquote>
<blockquote>"Q. You didn't tell Mr. Beamer this guy put $1,300 in your car?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. No, sir.</blockquote>
<blockquote>"Q. And we can't understand any reason why anyone would put money in your car and you were chasing him around town and trying to give it back?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. I didn't understand that.</blockquote>
<blockquote>"Q. You mean you didn't tell him that?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"A. Tell him what?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Mr. Wood, if that is all you had to do with this and you are innocent, when Mr. Beamer arrived on the scene why didn't you tell him?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. But in any event you didn't bother to tell Mr. Beamer anything about this?</blockquote>
<blockquote>"A. No, sir."</blockquote>
<p>Defense counsel's timely objections to the above questions of the prosecutor were overruled. The cross-examination of petitioner Doyle at his trial contained a similar exchange, and again defense counsel's timely objections were overruled.<sup>[5]</sup></p>
<p><span class="star-pagination">*615</span> Each petitioner appealed to the Court of Appeals, Fifth District, Tuscarawas County, alleging, <i>inter alia,</i> that the trial court erred in allowing the prosecutor to cross-examine the petitioner at his trial about his post-arrest silence. The Court of Appeals affirmed the convictions, stating as to the contentions about the post-arrest silence:</p>
<blockquote>"This was not evidence offered by the state in its case in chief as confession by silence or as substantive evidence of guilt but rather cross examination <span class="star-pagination">*616</span> of a witness as to why he had not told the same story earlier at his first opportunity.</blockquote>
<blockquote>"We find no error in this. It goes to credibility of the witness."</blockquote>
<p>The Supreme Court of Ohio denied further review. We granted certiorari to decide whether impeachment use of a defendant's post-arrest silence violates any provision of the Constitution,<sup>[6]</sup> a question left open last Term in <i>United States</i> v. <i>Hale,</i> <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">422 U. S. 171</a></span> (1975), and on which the Federal Courts of Appeals are in conflict. See <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">id.,</a></span></i> at 173 n. 2.</p>
<p></p>
<h2>II</h2>
<p>The State pleads necessity as justification for the prosecutor's action in these cases. It argues that the discrepancy between an exculpatory story at trial and silence at time of arrest gives rise to an inference that the story was fabricated somewhere along the way, perhaps to fit within the seams of the State's case as it was developed at pretrial hearings. Noting that the prosecution usually has little else with which to counter such an exculpatory story, the State seeks only the right to cross-examine a defendant as to post-arrest silence for the limited purpose of impeachment. In support of its position the State emphasizes the importance of cross-examination <span class="star-pagination">*617</span> in general, see <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="9421572"><a href="/opinion/105661/brown-v-united-states/#154" aria-description="Citation for case: Brown v. United States">356 U. S. 148, 154-155</a></span> (1958), and relies upon those cases in which this Court has permitted use for impeachment purposes of post-arrest statements that were inadmissible as evidence of guilt because of an officer's failure to follow <i>Miranda</i>'s dictates. <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971); <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975); see also <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954). Thus, although the State does not suggest petitioners' silence could be used as evidence of guilt, it contends that the need to present to the jury all information relevant to the truth of petitioners' exculpatory story fully justifies the cross-examination that is at issue.</p>
<p>Despite the importance of cross-examination,<sup>[7]</sup> we have concluded that the <i>Miranda</i> decision compels rejection of the State's position. The warnings mandated by that case, as a prophylactic means of safeguarding Fifth Amendment rights, see <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#443" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 443-444</a></span> (1974), require that a person taken into custody be advised immediately that he has the right to remain silent, that anything he says may be used against him, and that he has a right to retained or appointed counsel before submitting to interrogation. Silence in the wake of these warnings may be nothing more than the arrestee's exercise of these <i>Miranda</i> rights. Thus, every post-arrest silence is insolubly ambiguous because of what the State is required to advise the person arrested.<sup>[8]</sup> See <i>United States</i> v. <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale, supra,</a></span></i> <span class="star-pagination">*618</span> at 177. Moreover, while it is true that the <i>Miranda</i> warnings contain no express assurance that silence will carry no penalty, such assurance is implicit to any person who receives the warnings. In such circumstances, it would be fundamentally unfair and a deprivation of due process to allow the arrested person's silence to be used to impeach an explanation subsequently offered at trial.<sup>[9]</sup></p>
<p><span class="star-pagination">*619</span> MR. JUSTICE WHITE, concurring in the judgment in <i>United States</i> v. <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/#182" aria-description="Citation for case: United States v. Hale"><i>Hale, supra,</i> at 182-183</a></span>, put it very well:</p>
<blockquote>"[W]hen a person under arrest is informed, as <i>Miranda</i> requires, that he may remain silent, that anything he says may be used against him, and that he may have an attorney if he wishes, it seems to me that it does not comport with due process to permit the prosecution during the trial to call attention to his silence at the time of arrest and to insist that because he did not speak about the facts of the case at that time, as he was told he need not do, an unfavorable inference might be drawn as to the truth of his trial testimony. . . . Surely Hale was not informed here that his silence, as well as his words, could be used against him at trial. Indeed, anyone would reasonably conclude from <i>Miranda</i> warnings that this would not be the case."<sup>[10]</sup></blockquote>
<p>We hold that the use for impeachment purposes of petitioners' silence, at the time of arrest and after receiving <i>Miranda</i> warnings, violated the Due Process Clause of the Fourteenth Amendment.<sup>[11]</sup> The State has not <span class="star-pagination">*620</span> claimed that such use in the circumstances of this case might have been harmless error. Accordingly, petitioners' convictions are reversed and their causes remanded to the state courts for further proceedings not inconsistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE BLACKMUN and MR. JUSTICE REHNQUIST join, dissenting.</p>
<p>Petitioners assert that the prosecutor's cross-examination about their failure to mention the purported "frame" until they testified at trial violated their constitutional right to due process and also their constitutional privilege against self-incrimination. I am not persuaded by the first argument; though there is merit in a portion of the second, I do not believe it warrants reversal of these state convictions.</p>
<p></p>
<h2>I</h2>
<p>The Court's due process rationale has some of the characteristics of an estoppel theory. If (a) the defendant is advised that he may remain silent, and (b) he does remain silent, then we (c) presume that his decision was made in reliance on the advice, and (d) conclude that it is unfair in certain cases, though not others,<sup>[1]</sup> to use his silence to impeach his trial testimony. The key to the Court's analysis is apparently a concern that the <i>Miranda</i> warning, which is intended to increase the probability <span class="star-pagination">*621</span> that a person's response to police questioning will be intelligent and voluntary, will actually be deceptive unless we require the State to honor an unstated promise not to use the accused's silence against him.</p>
<p>In my judgment there is nothing deceptive or prejudicial to the defendant in the <i>Miranda</i> warning.<sup>[2]</sup> Nor do I believe that the fact that such advice was given to the defendant lessens the probative value of his silence, or makes the prosecutor's cross-examination about his silence any more unfair than if he had received no such warning.</p>
<p>This is a case in which the defendants' silence at the time of their arrest was graphically inconsistent with their trial testimony that they were the unwitting victims of a "frameup" in which the police did not participate. If defendants had been framed, their failure to mention that fact at the time of their arrest is almost <span class="star-pagination">*622</span> inexplicable; for that reason, under accepted rules of evidence, their silence is tantamount to a prior inconsistent statement and admissible for purposes of impeachment.<sup>[3]</sup></p>
<p>Indeed, there is irony in the fact that the <i>Miranda</i> warning provides the only plausible explanation for their silence. If it were the true explanation, I should think that they would have responded to the questions on cross-examination about why they had remained silent by stating that they relied on their understanding of the advice given by the arresting officers. Instead, however, they gave quite a different jumble of responses.<sup>[4]</sup> Those <span class="star-pagination">*623</span> responses negate the Court's presumption that their silence was induced by reliance on deceptive advice.</p>
<p>Since the record requires us to put to one side the <span class="star-pagination">*624</span> Court's presumption that the defendants' silence was the product of reliance on the <i>Miranda</i> warning, the Court's entire due process rationale collapses. For without reliance <span class="star-pagination">*625</span> on the waiver, the case is no different than if no warning had been given, and nothing in the Court's opinion suggests that there would be any unfairness in <span class="star-pagination">*626</span> using petitioners' prior inconsistent silence for impeachment purposes in such a case.</p>
<p>Indeed, as a general proposition, if we assume the defendant's silence would be admissible for impeachment purposes if no <i>Miranda</i> warning had been given, I should think that the warning would have a tendency to salvage the defendant's credibility as a witness. If the defendant is a truthful witness, and if his silence is the consequence of his understanding of the <i>Miranda</i> warning, he may explain that fact when he is on the stand. Even if he is untruthful, the availability of that explanation puts him in a better position than if he had received no warning. In may judgment, the risk that a truthful defendant will be deceived by the <i>Miranda</i> warning and also will be unable to explain his honest misunderstanding is so much less than the risk that exclusion of the evidence will merely provide a shield for perjury that I cannot accept the Court's due process rationale.</p>
<p>Accordingly, if we assume that the use of a defendant's silence for impeachment purposes would be otherwise unobjectionable, I find no merit in the notion that he is denied due process of law because he received a <i>Miranda</i> warning.</p>
<p></p>
<h2>II</h2>
<p>Petitioners argue that the State violated their Fifth Amendment privilege against self-incrimination by asking the jury to draw an inference of guilt from their constitutionally protected silence. They challenge both the prosecutor's cross-examination and his closing argument.</p>
<p></p>
<h2>A</h2>
<p>Petitioners claim that the cross-examination was improper because it referred to their silence at the time of <span class="star-pagination">*627</span> their arrest, to their failure to testify at the preliminary hearing, and to their failure to reveal the "frame" prior to trial. Their claim applies to the testimony of each defendant at his own trial, and also to the testimony each gave as a witness at the trial of the other. Since I think it quite clear that a defendant may not object to the violation of another person's privilege,<sup>[5]</sup> I shall only discuss the argument that a defendant may not be cross-examined about his own prior inconsistent silence.</p>
<p>In support of their objections to the cross-examination about their silence at the time of arrest, petitioners primarily rely on the statement in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, that the prosecution may not use at trial the fact that the defendant stood mute or claimed the privilege in the face of accusations during custodial interrogation.<sup>[6]</sup> There are two reasons why that statement does not adequately support petitioners' argument.</p>
<p>First, it is not accurate to say that the petitioners "stood mute or claimed the privilege in the face of accusations." Neither petitioner claimed the privilege and <span class="star-pagination">*628</span> petitioner Doyle did not even remain silent.<sup>[7]</sup> The case is not one in which a description of the actual conversation between the defendants and the police would give rise to any inference of guilt if it were not so flagrantly inconsistent with their trial testimony. Rather than a claim of privilege, we simply have a failure to advise the police of a "frame" at a time when it most surely would have been mentioned if petitioners' trial testimony were true. That failure gave rise to an inference of guilt only because it belied their trial testimony.</p>
<p>Second, the dictum in the footnote in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> relies primarily upon <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span>, which held that the Fifth Amendment, as incorporated in the Fourteenth, prohibited the prosecution's use of the defendant's silence in its case in chief. But as long ago as <i>Raffel</i> v. <i>United States,</i> <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">271 U. S. 494</a></span>, this Court recognized the distinction between the prosecution's affirmative use of the defendant's prior silence and the use of prior silence for impeachment purposes. <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> expressly held that the defendant's silence at a prior trial was admissible for purposes of impeachment despite the application in federal prosecutions of the prohibition that <i><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span></i> found in the Fifth Amendment. <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/#496" aria-description="Citation for case: Raffel v. United States"><i>Raffel, supra,</i> at 496-497</a></span>.</p>
<p>Moreover, Mr. Chief Justice Warren, the author of the Court's opinion in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> joined the opinion in <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span>, which squarely held that a valid constitutional objection to the admissibility of evidence as part of the Government's case in chief did not bar the use of that evidence to impeach the defendant's trial testimony. The availability of an objection to the affirmative use of improper evidence does not provide the defendant "with a shield against contradiction of his untruths." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States"><i>Id.,</i> at 65</a></span>. The need to ensure the integrity <span class="star-pagination">*629</span> of the truth-determining function of the adversary trial process has provided the predicate for an unbroken line of decisions so holding.<sup>[8]</sup></p>
<p><span class="star-pagination">*630</span> Although I have no doubt concerning the propriety of the cross-examination about petitioners' failure to mention the purported "frame" at the time of their arrest, a more difficult question is presented by their objection to the questioning about their failure to testify at the preliminary hearing and their failure generally to mention the "frame" before trial.<sup>[9]</sup> Unlike the failure <span class="star-pagination">*631</span> to make the kind of spontaneous comment that discovery of a "frame" would be expected to prompt, there is no significant inconsistency between petitioners' trial testimony <span class="star-pagination">*632</span> and their adherence to counsel's advice not to take the stand at the preliminary hearing; moreover, the decision not to divulge their defense prior to trial is probably attributable to counsel rather than to petitioners.<sup>[10]</sup> Nevertheless, unless and until this Court overrules <i>Raffel</i> v. <i>United States,</i> <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">271 U. S. 494</a></span>,<sup>[11]</sup> I think a state court is <span class="star-pagination">*633</span> free to regard the defendant's decision to take the stand as a waiver of his objection to the use of his failure to testify at an earlier proceeding or his failure to offer his version of the events prior to trial.</p>
<p></p>
<h2>B</h2>
<p>In my judgment portions of the prosecutor's argument to the jury overstepped permissible bounds. In each trial, he commented upon the defendant's silence not only as inconsistent with his testimony that he had been "framed," <span class="star-pagination">*634</span> but also as inconsistent with the defendant's innocence.<sup>[12]</sup> Comment on the lack of credibility of the defendant is plainly proper; it is not proper, however, for the prosecutor <span class="star-pagination">*635</span> to ask the jury to draw a direct inference of guilt from silenceto argue, in effect, that silence is inconsistent with innocence. But since the two inferencesperjury <span class="star-pagination">*636</span> and guiltare inextricably intertwined because they have a common source, it would be unrealistic to permit comment on the former but to find reversible error in the slightest reference to the latter. In the context of the entire argument and the entire trial, I am not persuaded that the rather sophisticated distinction between permissible comment on credibility and impermissible comment on an inference of guilt justifies a reversal of these state convictions.<sup>[13]</sup></p>
<p>Accordingly, although I have some doubt concerning the propriety of the cross-examination about the preliminary hearing and consider a portion of the closing argument improper, I would affirm these convictions.</p>
<h2>NOTES</h2>
<p>[*]  Together with No. 75-5015, <i>Wood</i> v. <i>Ohio,</i> also on certiorari to the same court.</p>
<p>[]  <i>Solicitor General Bork</i> filed a brief for the United States as <i>amicus curiae.</i></p>
<p>[1]  <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467-473</a></span> (1966).</p>
<p>[2]  Defense counsel's efforts were not totally successful. One of the four narcotics agents testified at both trials that he had seen the package passed through the window of Doyle's car to Bonnell. In an effort to impeach that testimony, defense counsel played a tape of the preliminary hearing at which the same agent had testified only to seeing the package under Bonnell's arm. The agent did not retract his trial testimony, and both he and the prosecutor explained the apparent inconsistency by noting that the examination at the preliminary hearing had not focused upon whether anyone had seen the package pass to Bonnell.</p>
<p>[3]  See n. 2. <i>supra.</i></p>
<p>[4]  Trial transcript in <i>Ohio</i> v. <i>Wood.</i> No. 10657. Common Pleas Court, Tuscarawas County, Ohio (hereafter Wood Tr.), 465-470.</p>
<p>[5]  Trial transcript in <i>Ohio</i> v. <i>Doyle,</i> No. 10656, Common Pleas Court, Tuscarawas County, Ohio (hereafter Doyle Tr.), 504-507:
</p>
<p>"Q. [By the prosecutor.] . . . You are innocent?</p>
<p>"A. [By Doyle.] I am innocent. Yes Sir.</p>
<p>"Q. That's why you told the police department and Kenneth Beamer when they arrived</p>
<p>.....</p>
<p>"(Continuing.)about your innocence?</p>
<p>.....</p>
<p>"A. . . . I didn't tell them about my innocence. No.</p>
<p>"Q. You said nothing at all about how you had been set up?</p>
<p>.....</p>
<p>"Q. Did Mr. Wood?</p>
<p>"A. Not that I recall, Sir.</p>
<p>.....</p>
<p>"Q. As a matter of fact, if I recall your testimony correctly, you said instead of protesting your innocence, as you do today, you said in response to a question of Mr. Beamer,`I don't know what you are talking about.'</p>
<p>"A. I believe what I said,`What's this all about?' If I remember, that's the only thing I said.</p>
<p>.....</p>
<p>"A. I was questioning, you know, what it was about. That's what I didn't know. I knew that I was trying to buy, which was wrong, but I didn't know what was going on. I didn't know that Bill Bonnell was trying to frame me, or what-have-you.</p>
<p>.....</p>
<p>"Q. All right,But you didn't protest your innocence at that time?</p>
<p>.....</p>
<p>"A. Not until I knew what was going on."</p>
<p>In addition, the court in both trials permitted the prosecutor, over more objections, to argue petitioners' post-arrest silence to the jury. Closing Argument of Prosecutor 13-14, supplementing Wood Tr.; Doyle Tr. 515, 526.</p>
<p>[6]  Petitioners also claim constitutional error because each of them was cross-examined by the prosecutor as to why he had not told the exculpatory story at the preliminary hearing or any other time prior to the trials. In addition, error of constitutional dimension is asserted because each petitioner was cross-examined as to post-arrest, preliminary hearing, and general pretrial silence when he testified as a <i>defense witness</i> at the other petitioner's trial. These averments of error present different considerations from those implicated by cross-examining petitioners as defendants as to their silence after receiving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings at the time of arrest. In view of our disposition of this case we find it unnecessary to reach these additional issues.</p>
<p>[7]  We recognize, of course, that unless prosecutors are allowed wide leeway in the scope of impeachment cross-examination some defendants would be able to frustrate the truth-seeking function of a trial by presenting tailored defenses insulated from effective challenge. See generally <i>Fitzpatrick</i> v. <i>United States,</i> <span class="citation" data-id="95301"><a href="/opinion/95301/fitzpatrick-v-united-states/#315" aria-description="Citation for case: Fitzpatrick v. United States">178 U. S. 304, 315</a></span> (1900).</p>
<p>[8]  The dissent by MR. JUSTICE STEVENS expresses the view that the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings does not lessen the "probative value of [a defendant's] silence . . . ." <i>Post,</i> at 621. But in <i>United States</i> v. <i>Hale,</i> <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/#177" aria-description="Citation for case: United States v. Hale">422 U. S. 171, 177</a></span> (1975), we noted that silence at the time of arrest may be inherently ambiguous even apart from the effect of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, for in a given case there may be several explanations for the silence that are consistent with the existence of an exculpatory explanation. In <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale</a></span></i> we exercised our supervisory powers over federal courts. The instant cases, unlike <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale</a></span>,</i> come to us from a state court and thus provide no occasion for the exercise of our supervisory powers. Nor is it necessary, in view of our holding above, to express an opinion on the probative value for impeachment purposes of petitioners' silence. We note only that the <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale</a></span></i> court considered silence at the time of arrest likely to be ambiguous and thus of dubious probative value.</p>
<p>[9]  A somewhat analogous situation was presented in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">318 U. S. 189</a></span> (1943). A defendant who testified at his trial was permitted by the trial judge to invoke the Fifth Amendment privilege against self-incrimination in response to certain questions on cross-examination. This Court assumed that it would not have been error for the trial court to have denied the privilege in the circumstances, see <span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/#196" aria-description="Citation for case: Johnson v. United States"><i>id.,</i> at 196</a></span>, in which case a failure to answer would have been a proper basis for adverse inferences and a proper subject for prosecutorial comment. But because the privilege had been granted, even if erroneously, "the requirements of fair trial" made it error for the trial court to permit comment upon the defendant's silence. <i><span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Ibid.</a></span></i>
</p>
<p>"An accused having the assurance of the court that his claim of privilege would be granted might well be entrapped if his assertion of the privilege could then be used against him. His real choice might then be quite different from his apparent one. . . . Elementary fairness requires that an accused should not be misled on that score." <span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/#197" aria-description="Citation for case: Johnson v. United States"><i>Id.,</i> at 197</a></span>.</p>
<p><i>Johnson</i> was decided under this Court's supervisory powers over the federal courts. But the necessity for elementary fairness is not unique to the federal criminal system. Cf. <i>Raley</i> v. <i>Ohio,</i> <span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#437" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 437-440</a></span> (1959).</p>
<p>[10]  The dissenting opinion relies on the fact that petitioners in this case, when cross-examined about their silence, did not offer reliance on <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings as a justification. But the error we perceive lies in the cross-examination on this question, thereby implying an inconsistency that the jury might construe as evidence of guilt. After an arrested person is formally advised by an officer of the law that he has a right to remain silent, the unfairness occurs when the prosecution, in the presence of the jury, is allowed to undertake impeachment on the basis of what may be the exercise of that right.</p>
<p>[11]  It goes almost without saying that the fact of post-arrest silence could be used by the prosecution to contradict a defendant who testifies to an exculpatory version of events and claims to have told the police the same version upon arrest. In that situation the fact of earlier silence would not be used to impeach the exculpatory story, but rather to challenge the defendant's testimony as to his behavior following arrest. Cf. <i>United States</i> v. <i>Fairchild,</i> <span class="citation" data-id="323043"><a href="/opinion/323043/united-states-v-alton-r-fairchild/#1383" aria-description="Citation for case: United States v. Alton R. Fairchild">505 F. 2d 1378, 1383</a></span> (CA5 1975).</p>
<p>[1]  As the Court acknowledges, the "fact of post-arrest silence could be used by the prosecution to contradict a defendant who testifies to an exculpatory version of events and claims to have told the police the same version upon arrest." <i>Ante,</i> at 619 and this page, n. 11.</p>
<p>[2]  At Wood's trial, the arresting officer described the warning he gave petitioners:
</p>
<p>"I told Mr. Wood and Mr. Doyle of the Miranda warning rights they had the right to remain silent, anything they said could and would be used against them in a court of law, and they had the right to an attorney and didn't have to say anything without an attorney being present and if they couldn't afford one, the court would appoint them one at the proper time." Trial transcript in <i>Ohio</i> v. <i>Wood,</i> No. 10657, Common Pleas Court, Tuscarawas County, Ohio (hereafter Wood Tr.), 126. At the Doyle trial, he testified that he "gave them their rights" and gave them a " `Miranda Warning.' " Trial transcript in <i>Ohio</i> v. <i>Doyle,</i> No. 10656, Common Pleas Court, Tuscarawas County, Ohio (hereafter Doyle Tr.), 269. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, requires the following warning:</p>
<p>"[The suspect] must be warned prior to any questioning that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 479</a></span>.</p>
<p>[3]  3A J. Wigmore, Evidence § 1042 (Chadbourn rev. 1970).</p>
<p>[4]  Petitioner Doyle gave the following testimony on direct and cross-examination at his trial:
</p>
<p>"Q. [By defense counsel.] And you were placed under arrest at that time?</p>
<p>"A. [By Doyle.] Yes. I asked what for and he said,`For the sale of marijuana.' I told him,I didn't know what he was talking about.</p>
<p>.....</p>
<p>"Q. [By the prosecutor.] As a matter of fact, if I recall your testimony correctly, you said instead of protesting your innocence, as you do today, you said in response to a question of Mr. Beamer,`I don't know what you are talking about.'</p>
<p>"A. [By Doyle.] I believe what I said,`What's this all about?' If I remember, that's the only thing I said.</p>
<p>"Q. You testified on direct.</p>
<p>"A. If I did, then I didn't understand.</p>
<p>". . . I was questioning, you know, what it was about. That's what I didn't know. I knew that I was trying to buy, which was wrong, but I didn't know what was going on. I didn't know that Bill Bonnell was trying to frame me, or what-have-you.</p>
<p>.....</p>
<p>"Q. All right,But you didn't protest your innocence at that time?</p>
<p>.....</p>
<p>"A. Not until I knew what was going on." Doyle Tr. 479, 506-507.</p>
<p>At Wood's trial, Doyle gave a somewhat different explanation of his silence at the time of arrest:</p>
<p>"Q. [By the prosecutor.] Why didn't [Wood] tell [the police officers] about Mr. Bonnell?</p>
<p>"A. [By Doyle.] Because we didn't know what was going on and wanted to find out.</p>
<p>"Q. So he hid the money under the mat?</p>
<p>"A. The police officers said they stopped us for a red light. I wanted to get my hands on Bill Bonnell.</p>
<p>"Q. It wasn't because you were guilty, was it?</p>
<p>"A. Because I wanted to get my hands on Bill Bonnell because</p>
<p>I suspected he was trying . . .</p>
<p>"Q. Why didn't you tell the police that Bill Bonnell just set you up?</p>
<p>"A. Because I would rather have my own hands on him.</p>
<p>.....</p>
<p>"Q. When Mr. Beamer arrived?</p>
<p>"A. . . . [W]hen Mr. Beamer got there I said to Mr. Beamer what the hell is all this about and he said you are under arrest for the suspicion of selling marijuana and I said you got to be crazy. I was pretty upset.</p>
<p>.....</p>
<p>"Q. So on the night of April 29 you felt that you were being framed like you are being framed today?</p>
<p>"A. I was so confused that night, the night of the arrest.</p>
<p>"Q. How about Mr. Wood?</p>
<p>"A. Mr. Wood didn't know what was going on.</p>
<p>.....</p>
<p>"Q. . . . Are you as mad and upset today as you were that night?</p>
<p>"A. I can't answer that question.</p>
<p>"Q. Did you feel the same way about what happened to you?</p>
<p>"A. That night I felt like I couldn't believe what was happening.</p>
<p>"Q. You didn't like being framed?</p>
<p>"A. That is right. I didn't like some one putting me in a spot like that.</p>
<p>"Q. Didn't it occur to you to try to protect yourself?</p>
<p>"A. Yes, at this time I felt like I wasn't talking to nobody but John James who was the attorney at that time.</p>
<p>"Q. But you felt . . .</p>
<p>"A. The man walked up and didn't ask me anything.</p>
<p>"Q. You didn't talk to a soul about how rotten it was because you were framed?</p>
<p>.....</p>
<p>"A. I will answer the question, sir, the best I can. I didn't know what to say. I was stunned about what was going on and I was asked questions and I answered the questions as simply as I could because I didn't have nobody there to help me answer the questions.</p>
<p>"Q. Wouldn't that have been a marvelous time to protest your innocence?</p>
<p>.....</p>
<p>"A. I don't know if it would or not.</p>
<p>"Q. Do you remember having a conversation with Kenneth Beamer?</p>
<p>"A. Yes, sir.</p>
<p>"Q. What was said?</p>
<p>.....</p>
<p>"A. Kenneth Beamer said I want to know where you stash where your hide out is, where you are keeping the dope and I said I don't know what you are talking about. I believe the question was asked in front of you.</p>
<p>"Q. Where did this conversation take place?</p>
<p>"A. Took place during the search.</p>
<p>.....</p>
<p>"Q. So any way you didn't tell anyone how angry you were that night?</p>
<p>.....</p>
<p>"A. I was very angry.</p>
<p>"Q. But you didn't tell anyone?</p>
<p>"A. That is right. If I started I don't know where I would have stopped. I was upset." Wood Tr. 424-430.</p>
<p>Petitioner Wood testified on cross-examination at his trial as follows:</p>
<p>"Q. [By the prosecutor.] Jefferson Doyle said he was confused, angry and upset [at the time of the arrest]. Were you confused, angry and upset?</p>
<p>.....</p>
<p>"A. [By Wood.] Upset and confused.</p>
<p>"Q. Why were you upset?</p>
<p>"A. Because I didn't know what was going on most of the time.</p>
<p>"Q. Why would you be upset? Because you found $1300 in your back seat?</p>
<p>"A. Mainly because the person that was in the car Jeff [Doyle] was upset confused and angry and . . .</p>
<p>"Q. What has that to do with you?</p>
<p>"A. I am in the car. That is what it has to do with me.</p>
<p>.....</p>
<p>"Q. You are innocent?</p>
<p>"A. Yes.</p>
<p>"Q. Of anything?</p>
<p>"A. I don't know about anything.</p>
<p>"Q. This particular incident, you were placed under arrest, weren't you?</p>
<p>"A. Yes, innocent of this incident.</p>
<p>"Q. Innocent of the entire transaction?</p>
<p>"A. Yes, sir.</p>
<p>"Q. Or even any knowledge of the entire transaction?</p>
<p>"A. Up to a point, sir.</p>
<p>.....</p>
<p>"Q. Mr. Wood, if that is all you had to do with this and you are innocent, when Mr. Beamer arrived on the scene why didn't you tell him?</p>
<p>.....</p>
<p>"A. Mr. Cunningham, in the last eight months to a year there has been so many implications, etc. in the paper and law enforcement that are setting people up and busting them for narcotics and stuff." Wood Tr. 467-469.</p>
<p>[5]  See <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, 206-207</a></span>; 8 J. Wigmore, Evidence § 2270, pp. 416-417 (McNaughton rev. 1961); cf. <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174</a></span>. Cross-examination and comment upon a witness' prior silence does not raise any inference prejudicial to the defendant, and indeed, does not even raise any inference that the defendant remained silent.</p>
<p>[6]  "In accord with our decision today, it is impermissible to penalize an individual for exercising his Fifth Amendment privilege when he is under police custodial interrogation. The prosecution may not, therefore, use at trial the fact that he stood mute or claimed his privilege in the face of accusation. Cf. <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965); <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964); Comment, <span class="citation no-link">31 U. Chi. L. Rev. 556</span> (1964); Developments in the LawConfessions, <span class="citation no-link">79 Harv. L. Rev. 935</span>, 1041-1044 (1966). See also <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#562" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 562</a></span> (1897)." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 468</a></span> n. 37.</p>
<p>[7]  See n. 4, <i>supra.</i></p>
<p>[8]  As the Court recently recognized in a most carefully considered opinion, an adversary system can maintain neither the reality nor the appearance of efficacy without the assurance that its judgments rest upon a complete illumination of a case rather than upon "a partial or speculative presentation of the facts." <i>United States</i> v. <i>Nixon,</i> <span class="citation" data-id="109101"><a href="/opinion/109101/united-states-v-nixon/#709" aria-description="Citation for case: United States v. Nixon">418 U. S. 683, 709</a></span>. The necessity of insuring a complete presentation of all relevant evidence has led to the rule that a criminal defendant who voluntarily forgoes his privilege not to testify, and presents exculpatory or mitigating evidence, thereby subjects himself to relevant cross-examination without the right to reclaim Fifth Amendment protection on a selective basis. <i>Fitzpatrick</i> v. <i>United States,</i> <span class="citation" data-id="95301"><a href="/opinion/95301/fitzpatrick-v-united-states/#315" aria-description="Citation for case: Fitzpatrick v. United States">178 U. S. 304, 315</a></span>.
</p>
<p>"If he takes the stand and testifies in his own defense, his credibility may be impeached and his testimony assailed like that of any other witness, and the breadth of his waiver is determined by the scope of relevant cross-examination. `[H]e has no right to set forth to the jury all the facts which tend in his favor without laying himself open to a cross-examination upon those facts.' " <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="9421572"><a href="/opinion/105661/brown-v-united-states/#154" aria-description="Citation for case: Brown v. United States">356 U. S. 148, 154-155</a></span> (citation omitted).</p>
<p>One need not impute perjury to an entire class to acknowledge that a testifying defendant has more to gain and less to lose than an ordinary witness from fabrications upon the witness stand. Cf. <i>Reagan</i> v. <i>United States,</i> <span class="citation" data-id="94162"><a href="/opinion/94162/reagan-v-united-states/#304" aria-description="Citation for case: Reagan v. United States">157 U. S. 301, 304-311</a></span>; <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="279002"><a href="/opinion/279002/calvin-j-taylor-v-united-states/#284" aria-description="Citation for case: Calvin J. Taylor v. United States">390 F. 2d 278, 284-285</a></span> (CA8 1968) (Blackmun, J.). As the Court notes today: "Unless prosecutors are allowed wide leeway in the scope of impeachment cross-examination some defendants would be able to frustrate the truth-seeking function of a trial by presenting tailored defenses insulated from effective challenge." <i>Ante,</i> at 617 n. 7. In recognition of this fact, this Court has allowed evidence to be used for impeachment purposes that would be inadmissible as evidence of guilt. In <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span>, evidence of narcotics unlawfully seized in connection with an aborted earlier case against a defendant was held admissible for the limited purpose of impeaching the defendant's testimony that he never had been associated with narcotics, although such evidence clearly was inadmissible for any purpose in the prosecution's case in chief. In <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span>, the Court held admissible for the purpose of impeaching a defendant's testimony certain partially inconsistent post-arrest statements which, although voluntary, were unavailable for the prosecution's case because they had been given by the defendant without benefit of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. And last Term, in a decision closely analogous to <i><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span>,</i> the Court held admissible for impeachment purposes post-arrest statements of a defendant made after he had received <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and exercised his right to request a lawyer, but before he had been furnished with counsel as <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires in such circumstances. <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span>.</p>
<p>In each of these cases involving impeachment cross-examination, the need to insure the integrity of the trial by the "traditional truth-testing devices of the adversary process," <i>Harris</i> v. <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York"><i>New York, supra,</i> at 225</a></span>, was deemed to outweigh the policies underlying the relevant exclusionary rules.</p>
<p>[9]  Petitioner Doyle was cross-examined as follows at his trial:
</p>
<p>"Q. [By the prosecutor.] All right. Do you remember the Preliminary Hearing in this case?</p>
<p>"A. [By Doyle.] Yes Sir. I remember it.</p>
<p>"Q. And that was prior to your indictment for this offense, was it not?</p>
<p>"A. Yes sir. I believe,Yes Sir, it was before I was indicted.</p>
<p>"Q. Arraignment. Is that what you mean?</p>
<p>"A. Yes. The next day after the arrest.</p>
<p>"Q. Yes, when evidence was presented and you had the opportunity to hear the testimony of the witnesses against you. Remember that?</p>
<p>"A. Yes Sir.</p>
<p>"Q. Mr. Bonnell testified; Captain Griffin testified; Deputy Chief Deputy White testified?</p>
<p>"A. Yes Sir.</p>
<p>"Q. Kenneth Beamer testified?</p>
<p>"A. Yes Sir.</p>
<p>"Q. You were there, weren't you?</p>
<p>"A. Yes Sir.</p>
<p>"Q. And your lawyer was there,Mr. James?</p>
<p>"A. Yes Sir.</p>
<p>"Q. Tape recording was made of the transcript?</p>
<p>"A. Yes Sir.</p>
<p>"Q. Did you protest your innocence at that proceeding?</p>
<p>.....</p>
<p>"A. I didn'teverything that was done with that was done with my attorney. My attorney did it.</p>
<p>"Q. All right. The first time that you gave this version of the fact was in the trial of Richard Wood,was it not?</p>
<p>.....</p>
<p>"A. Yes Sir. It was the first time I was asked.</p>
<p>"Q. All the time, you being innocent?</p>
<p>"A. Yes Sir." Doyle Tr. 507-508.</p>
<p>Petitioner Wood was subjected to similar cross-examination at his trial:</p>
<p>"Q. [By the prosecutor.] As a matter of fact you never told anyone that you had been set up until today?</p>
<p>.....</p>
<p>"A. [By Wood.] Yes, I believe I did, sir.</p>
<p>"Q. I assume you discussed it with your lawyer?</p>
<p>"A. Yes, I discussed it with my lawyer.</p>
<p>"Q. And you heard the testimony and witnesses against you?</p>
<p>"A. Yes, sir.</p>
<p>"Q. And were you aware Mr. James was able to obtain a tape transcript of the proceedings?</p>
<p>"A. Yes.</p>
<p>"Q. And you no doubt listened to those?</p>
<p>"A. Parts and portions of themsome of it.</p>
<p>"Q. But you never communicated your innocence?</p>
<p>"A. I believe I did one time to Mr. Beamer.</p>
<p>"Q. When might that have been?</p>
<p>"A. When in the jail house.</p>
<p>"Q. So you protested your innocence?</p>
<p>"A. In a little room. I believe he asked us how do you let people get away with people setting up friends like this. He said Bill Bonnell is not your friend and I said no, but I figured he was a good enough acquaintance he would do that.</p>
<p>"Q. Where was that?</p>
<p>"A. Little room there.</p>
<p>"Q. Ever been there before?</p>
<p>"A. Yes, sir.</p>
<p>"Q. When?</p>
<p>.....</p>
<p>"Q. Did you see me there?</p>
<p>"A. I didn't know who you were at the time. I believe you were in and out of there.</p>
<p>"Q. You didn't say anything to me, did you?</p>
<p>"A. No, I didn't know who you were then." Wood Tr. 470-472.</p>
<p>[10]  Under Ohio law, the preliminary hearing determines only whether the defendant should be held for trial. The prosecution need establish, at most, that a crime has been committed and that there is "probable and reasonable cause" to hold the defendant for trial, and the court need only find "substantial credible evidence" of the charge against the defendant. <span class="citation no-link">Ohio Rev. Code Ann. §§ 2937.12</span>, 2937.13 (Supp. 1973). Indeed, if a defendant has been indicted, no hearing need be held. <i>State</i> v. <i>Morris,</i> <span class="citation" data-id="6755494"><a href="/opinion/6865449/state-v-morris/#326" aria-description="Citation for case: State v. Morris">42 Ohio St. 2d 307, 326</a></span>, <span class="citation" data-id="6755494"><a href="/opinion/6865449/state-v-morris/#97" aria-description="Citation for case: State v. Morris">329 N. E. 2d 85, 97</a></span> (1975). Defense counsel thus will have no incentive to divulge the defendant's case at the preliminary hearing if the prosecution has presented substantial evidence of guilt. Since that was the case here, no significant impeaching inference may be drawn from petitioners' silence at that proceeding.
</p>
<p>Petitioners' failure to refer to the "frame" at any time between arrest and trial is somewhat more probative; for if the "frame" story were true, one would have expected counsel to try to persuade the prosecution to dismiss the charges in advance of trial.</p>
<p>[11]  <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> was the last decision of this Court to address the constitutionality of admitting evidence of a defendant's prior silence to impeach his testimony upon direct examination. Raffel had been charged with conspiracy to violate the National Prohibition Act. An agent testified at his first trial that he had admitted ownership of a drinking place; Raffel did not take the stand. The trial ended in a hung jury, and upon retrial, the agent testified as before. Raffel elected to testify and denied making the statement, but he was cross-examined on his failure to testify in the first trial. This Court held that the evidence was admissible because Raffel had completely waived the privilege against self-incrimination by deciding to testify. <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/#499" aria-description="Citation for case: Raffel v. United States">271 U. S., at 499</a></span>.
</p>
<p>Subsequent cases, decided in the exercise of this Court's supervisory powers, have diminished the force of <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> in the federal courts. <i>United States</i> v. <i>Hale,</i> <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">422 U. S. 171</a></span>; <i>Stewart</i> v. <i>United States,</i> <span class="citation" data-id="9422185"><a href="/opinion/106219/stewart-v-united-states/" aria-description="Citation for case: Stewart v. United States">366 U. S. 1</a></span>; <i>Grunewald</i> v. <i>United States,</i> <span class="citation" data-id="9421440"><a href="/opinion/105508/grunewald-v-united-states/" aria-description="Citation for case: Grunewald v. United States">353 U. S. 391</a></span>. All three of these cases held that the defendant's prior silence or prior claim of the privilege was inadmissible for purposes of impeachment; all three distinguished <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> on the ground that the Court there assumed that the defendant's prior silence was significantly inconsistent with his testimony on direct examination. <span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/#175" aria-description="Citation for case: United States v. Hale"><i>Hale, supra,</i> at 175-176</a></span>; <span class="citation" data-id="9422185"><a href="/opinion/106219/stewart-v-united-states/#5" aria-description="Citation for case: Stewart v. United States"><i>Stewart, supra,</i> at 5-7</a></span>; <span class="citation" data-id="9421440"><a href="/opinion/105508/grunewald-v-united-states/#418" aria-description="Citation for case: Grunewald v. United States"><i>Grunewald, supra,</i> at 418-424</a></span>. Two of the three cases relied upon the need to protect the defendant's exercise of the privilege against self-incrimination from unwarranted inferences of guilt, a rationale that is not easily reconciled with the reasoning in <i><span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/" aria-description="Citation for case: Raffel v. United States">Raffel</a></span></i> that the decision to testify constitutes a complete waiver of the protection afforded by the privilege. Compare <i><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">Hale, supra,</a></span></i> at 180 and n. 7, and <span class="citation" data-id="9421440"><a href="/opinion/105508/grunewald-v-united-states/#423" aria-description="Citation for case: Grunewald v. United States"><i>Grunewald, supra,</i> at 423-424</a></span>, with <i>Raffel,</i> <span class="citation" data-id="100906"><a href="/opinion/100906/raffel-v-united-states/#499" aria-description="Citation for case: Raffel v. United States">271 U. S., at 499</a></span>.</p>
<p>[12]  At Doyle's trial, the prosecutor made the following arguments to the jury:
</p>
<p>"Diffuse what the true facts are; obscure the facts and prosecute the prosecution.</p>
<p>"A typical and classic defense, but keep in mind, when you are considering the testimony of the law enforcement officers involved, that not until, Ladies and Gentlemen, not until the trial of this case and prior to this case, the trial of Richard Wood's case, that anybody connected with the prosecution in this case had any idea what stories would be told by Jefferson Doyle and Richard Wood. Not the foggiest idea. Both of them told you on the witness stand that neither one of them said a word to the law enforcement officials on the scene</p>
<p>.....</p>
<p>"(continuing) on the scene at the point of their arrest, at the Preliminary Hearing before Indictment in this case. Not a word that they were innocent; that this was their position; that somehow, they had been `set-up.'</p>
<p>"So, when you evaluate the testimony of the Law Enforcement Officials, consider</p>
<p>.....</p>
<p>"(continuing)what they had to deal with on the night in question and the months subsequent to that.</p>
<p>.....</p>
<p>"Then they decide that they have been `had' somehow. They have been framed.</p>
<p>"Now, remember, this fits with the facts as observed by the law enforcement officers except the basic, crucial facts. Somehow, they have been framed. So, if you can believe this, Ladies and Gentlemen, they take off, chase Bill Bonnell around to give his money back to him or ask him what he did to them, yet they don't bother to tell the Law Enforcement Officers.</p>
<p>"It is unbelievable. I think, when you go to the Jury Room, Ladies and Gentlemen, you are going to decide what really happened.</p>
<p>.....</p>
<p>"We have the Fifth Amendment. I agree with it. It is fundamental to our sense and system of fairness, but if you are innocent</p>
<p>.....</p>
<p>"(continuing)if you are innocent, Ladies and Gentlemen, if you have been framed, if you have been set-on, etc. etc. etc., as we heard in Court these last days, you don't say, when the law enforcement officer says,`You are under arrest,'you don't say,`I don't know what you are talking about.' You tell the truth. You tell them what happened and you go from there. You don't say, `I don't know what you are talking about,'and demand to see your lawyer and refuse to permit a search of your vehicle, forcing the law enforcement agents to get a search warrant.</p>
<p>"If you're innocent, you just don't do it." Doyle Tr. 515-516, 519, 526.</p>
<p>At Wood's trial, he made similar arguments:</p>
<p>"The defense in this case was very careful to make no statements at all until they had the benefit of hearing all the evidence against them and had time to ascertain what they would admit and what they would deny and how they could fit their version of the story with the state's case. During none of this time did we ever hear any business about a set up or frame or anything else. All right.</p>
<p>"Yes, it is the law of our land, and rightfully so, ladies and gentlemen, that nobody must be compelled to incriminate themselves. It is the 5th Amendment. No one can be forced to give testimony against themselves where criminal action charges are pending. It is a very fundamental right and I am glad we have it.</p>
<p>"The idea was nobody can convict himself out of his own mouth and it grew out of the days when they used to whip and beat and extract statements from the defendants and get them to convict themselves out of their own mouth, and I am glad we have that right.</p>
<p>"But ladies and gentlemen, there is one statement I am going to make. If you are innocent, if you are innocent, if you have been framed, if you have been set up as claimed in this case, when do you tell it? When do you tell the policemen that?</p>
<p>.....</p>
<p>"Think about it. After monthsafter various proceedings and for the first time? I am not going to say any more about that but I want you to think about it." Closing Argument of the Prosecutor 12-14, supplementing Wood Tr.</p>
<p>[13]  Petitioner Doyle also argues that he was erroneously cross-examined at his trial on his failure to consent to a search of the car he was driving at the time of the arrest. Petitioner Wood appears to raise the similar claim that testimony of other witnesses that he failed to consent to a search of the car was erroneously admitted at his trial. The parties have not argued these issues separately from the questions whether prior silence in various circumstances may be admitted to impeach a defendant or a defense witness. It is apparent, however, that these questions implicate Fourth Amendment issues that merit independent examination. Accordingly, like the Court, I do not address them.</p>

</div>
```

---
