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

## GROUP: content/cases/Samson v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Samson v. California"
type: case
citation: "547 U.S. 843 (2006)"
parallel_cite: "126 S. Ct. 2193; 165 L. Ed. 2d 250"
neutral_cite: 2006 U.S. LEXIS 4885
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-06-19
docket: 04-9728
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-06-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Samson v. California
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145640/samson-v-california/"
  cluster_id: 145640
  opinion_id: 145640
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Knights]]", "[[Griffin v. Wisconsin]]", "[[Board of Education v. Earls]]"]
aliases: []
tags: ["case", "fourth-amendment", "parolee", "suspicionless-search", "diminished-privacy", "special-needs"]
holding: "A suspicionless search of a parolee is reasonable; a parolee subject to a search condition has severely diminished privacy expectations,…"
lake:
  record_id: Samson v. California
  status: verified
  projected_at: 2026-07-09
---

# Samson v. California

*547 U.S. 843 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
California law required every parolee to agree in writing to be subject to search by a parole or other peace officer "at any time of the day or night, with or without a search warrant and with or without cause." A police officer who knew Samson was a parolee stopped and searched him on a city street without any particularized suspicion and found methamphetamine. Samson moved to suppress.

## Issue
Whether a suspicionless search of a parolee, conducted pursuant to a state parole search condition, violates the Fourth Amendment.

## Rule
No. Parolees have sharply reduced privacy expectations: "The extent and reach of these conditions clearly demonstrate that parolees like petitioner have severely diminished expectations of privacy by virtue of their status alone." — 547 U.S. at 852. ^pin-852

Weighed against the State's substantial interests in supervising parolees and reducing recidivism, "we conclude that the Fourth Amendment does not prohibit a police officer from conducting a suspicionless search of a parolee." — [547 U.S. at 857](https://www.courtlistener.com/opinion/145640/samson-v-california/#:~:text=we%20conclude%20that%20the%20Fourth). ^pin-857

## Application
Samson was a California parolee subject to the State's clearly expressed, signed suspicionless-search condition, giving him severely diminished privacy expectations; the State's strong interests in closely supervising parolees (who reoffend at high rates) and reintegrating them justified the search. Because the search was not arbitrary, capricious, or harassing — conduct California law independently forbids — the suspicionless street search of Samson was reasonable.

## Conclusion
The suspicionless search of a parolee subject to a search condition is reasonable; the California Court of Appeal's judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Samson* extends the diminished-privacy reasoning of [[United States v. Knights]] from probationers (searched on reasonable suspicion) to parolees (searched suspicionlessly).

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Samson v. California*, 547 U.S. 843 (2006) — https://www.courtlistener.com/opinion/145640/samson-v-california/ — pinpoints: 852, 857.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ae4d862e20a5ff4a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "547 U.S. 843 (2006)", "court": "U.S. Supreme Court", "neutral_cite": "2006 U.S. LEXIS 4885", "official_citation_present": true, "parallel_cite": "126 S. Ct. 2193; 165 L. Ed. 2d 250", "title": "Samson v. California", "year": "2006"}}
{"assertion_id": "5b04e291575696c3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A suspicionless search of a parolee is reasonable; a parolee subject to a search condition has severely diminished privacy expectations,…", "title": "Samson v. California"}}
{"assertion_id": "caa795c745bd4996", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "Samson v. California"}}
{"assertion_id": "6f182b7dc91c0f19", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2006-06-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Samson v. California", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Samson v. California", "varies_by_point": "false"}}
{"assertion_id": "b432cf56d5ca13a5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Samson v. California"}}
```

### lake record — Samson v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Samson v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Samson v. California",
    "case_name_short": "Samson",
    "case_name_full": "Samson v. California",
    "input_case_name": "Samson v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-06-19",
    "year": 2006,
    "docket": "04-9728",
    "cluster_id": 145640,
    "lead_opinion_id": 145640,
    "sibling_ids": [
      145640,
      9434919,
      9434920
    ],
    "absolute_url": "/opinion/145640/samson-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 843",
      "volume": "547",
      "reporter": "U.S.",
      "page": "843",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 2193",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "2193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "165 L. Ed. 2d 250",
        "volume": "165",
        "reporter": "L. Ed. 2d",
        "page": "250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 4885",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4885",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 843",
        "volume": "547",
        "reporter": "U.S.",
        "page": "843",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 2193",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "2193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "165 L. Ed. 2d 250",
        "volume": "165",
        "reporter": "L. Ed. 2d",
        "page": "250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 4885",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4885",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 843",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 843",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-852",
      "page": null,
      "quote": "A police officer who knew Samson was a parolee stopped and searched him on a city street without any particularized suspicion and found methamphetamine. Samson moved to suppress. ## Issue Whether a suspicionless search of a parolee, conducted pursuant to a state parole search condition, violates the Fourth Amendment. ## Rule No. Parolees have sharply reduced privacy expectations:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-857",
      "page": null,
      "quote": "we conclude that the Fourth Amendment does not prohibit a police officer from conducting a suspicionless search of a parolee.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 30946,
      "fragment": "#:~:text=we%20conclude%20that%20the%20Fourth",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-06-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Samson v. California",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
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
        "journal_ref": "Samson v. California:lane1_negative"
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
        "journal_ref": "Samson v. California:lane1_negative"
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
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stenhoff",
          "cluster_id": 4609284,
          "cite": [
            "2019 ND 106",
            "925 N.W.2d 429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
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
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Blue",
          "cluster_id": 3185413,
          "cite": [
            "783 S.E.2d 524",
            "246 N.C. App. 259",
            "2016 N.C. App. LEXIS 293"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Morris",
          "cluster_id": 3185407,
          "cite": [
            "783 S.E.2d 528",
            "246 N.C. App. 349",
            "2016 N.C. App. LEXIS 291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Moore",
          "cluster_id": 3168462,
          "cite": [
            "473 Mass. 481",
            "43 N.E.3d 294"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
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
        "journal_ref": "Samson v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Brishen R. Vanderkolk",
          "cluster_id": 2806588,
          "cite": [
            "32 N.E.3d 775",
            "2015 Ind. LEXIS 507",
            "2015 WL 3608834"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane1_negative"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jacoby, T., Aplt.",
          "cluster_id": 4429713,
          "cite": [
            "170 A.3d 1065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grady v. North Carolina",
          "cluster_id": 2789928,
          "cite": [
            "575 U.S. 306",
            "135 S. Ct. 1368",
            "191 L. Ed. 2d 459",
            "2015 U.S. LEXIS 2124",
            "83 U.S.L.W. 4226",
            "25 Fla. L. Weekly Fed. S 181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Samuels",
          "cluster_id": 2601800,
          "cite": [
            "228 P.3d 229",
            "2009 Colo. App. LEXIS 1789",
            "2009 WL 3297504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warshak v. United States",
          "cluster_id": 1425282,
          "cite": [
            "532 F.3d 521",
            "2008 U.S. App. LEXIS 14717",
            "2008 WL 2698177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vilar",
          "cluster_id": 1039434,
          "cite": [
            "729 F.3d 62",
            "92 A.L.R. Fed. 2d 661",
            "2013 WL 4608948",
            "2013 U.S. App. LEXIS 18143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. James Maximiliano Ochoa",
          "cluster_id": 4472474,
          "cite": [
            "792 N.W.2d 260",
            "2010 Iowa Sup. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lewis",
          "cluster_id": 626016,
          "cite": [
            "674 F.3d 1298",
            "2012 WL 967969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Dean Short",
          "cluster_id": 2687558,
          "cite": [
            "851 N.W.2d 474",
            "2014 WL 3537029",
            "2014 Iowa Sup. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nuckles",
          "cluster_id": 858615,
          "cite": [
            "56 Cal. 4th 601",
            "298 P.3d 867",
            "155 Cal. Rptr. 3d 374",
            "2013 WL 1707968",
            "2013 Cal. LEXIS 3329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCain v. Com.",
          "cluster_id": 1058509,
          "cite": [
            "659 S.E.2d 512",
            "275 Va. 546",
            "2008 Va. LEXIS 55"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
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
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jaime P.",
          "cluster_id": 2588357,
          "cite": [
            "146 P.3d 965",
            "51 Cal. Rptr. 3d 430",
            "40 Cal. 4th 128",
            "2006 Daily Journal DAR 15618",
            "2006 Cal. Daily Op. Serv. 10933",
            "2006 Cal. LEXIS 14082",
            "2006 WL 3437058"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Earl Davis",
          "cluster_id": 2968788,
          "cite": [
            "690 F.3d 226",
            "2012 WL 3518479",
            "2012 U.S. App. LEXIS 17217"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ward",
          "cluster_id": 2010509,
          "cite": [
            "862 N.E.2d 1102",
            "308 Ill. Dec. 899",
            "371 Ill. App. 3d 382",
            "2007 Ill. App. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Weaver",
          "cluster_id": 5639938,
          "cite": [
            "12 N.Y.3d 433",
            "909 N.E.2d 1195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Samson v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145640 OR 9434919 OR 9434920) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDI4NjI0MDAwMDAwJnM9Mjc5Mjg3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145640+OR+9434919+OR+9434920%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145640 OR 9434919 OR 9434920)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OSZzPTE2MzE5NDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145640+OR+9434919+OR+9434920%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145640 OR 9434919 OR 9434920)",
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
    "complete_query": "cites:(145640 OR 9434919 OR 9434920)",
    "indexed_citing_opinions": 593,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145640,
        "count": 505,
        "count_source": "search"
      },
      {
        "opinion_id": 9434919,
        "count": 99,
        "count_source": "search"
      },
      {
        "opinion_id": 9434920,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 985,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/samson-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5ODkyODImcz0xMDEyMDUzOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145640+OR+9434919+OR+9434920%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145640,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 102473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 108606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 108785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 111904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 118468,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 127897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 541733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 776901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 786677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 791251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 1112011,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 1212086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 1444172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 2281190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145640,
        "cited_id": 2545822,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LCU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T18:34:52Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:35:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:35:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:38:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:35:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Samson v. California

```
(Slip Opinion)              OCTOBER TERM, 2005                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                       SAMSON v. CALIFORNIA

    CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA,

                FIRST APPELLATE DISTRICT


   No. 04–9728.       Argued February 22, 2006—Decided June 19, 2006
Pursuant to a California statute—which requires every prisoner eligi
  ble for release on state parole to “agree in writing to be subject to
  search or seizure by a parole officer or other peace officer . . . , with or
  without a search warrant and with or without cause”—and based
  solely on petitioner’s parolee status, an officer searched petitioner
  and found methamphetamine. The trial court denied his motions to
  suppress that evidence, and he was convicted of possession. Affirm
  ing, the State Court of Appeal held that suspicionless searches of pa
  rolees are lawful under California law and that the search in this
  case was reasonable under the Fourth Amendment because it was
  not arbitrary, capricious, or harassing.
Held: The Fourth Amendment does not prohibit a police officer from
 conducting a suspicionless search of a parolee. Pp. 3–12.
    (a) The “totality of the circumstances” must be examined to deter
 mine whether a search is reasonable under the Fourth Amendment.
 United States v. Knights, 534 U. S. 112, 118. Reasonableness “is de
 termined by assessing, on the one hand, the degree to which [the
 search] intrudes upon an individual’s privacy and, on the other, the
 degree to which it is needed for the promotion of legitimate govern
 mental interests.” Id., at 118–119. Applying this approach in
 Knights, the Court found reasonable the warrantless search of a pro
 bationer’s apartment based on reasonable suspicion and a probation
 condition authorized by California law. In evaluating the degree of
 intrusion into Knights’ privacy, the Court found his probationary
 status “salient,” id., at 118, observing that probation is on a contin
 uum of possible punishments and that probationers “do not enjoy ‘the
 absolute liberty’ ” of other citizens, id., at 119. It also found probation
 searches necessary to promote legitimate governmental interests of
2                       SAMSON v. CALIFORNIA

                                  Syllabus

    integrating probationers back into the community, combating recidi
    vism, and protecting potential victims. Balancing those interests, the
    intrusion was reasonable. However, because the search was predi
    cated on both the probation search condition and reasonable suspi
    cion, the Court did not address the reasonableness of a search solely
    predicated upon the probation condition. Pp. 3–5.
       (b) Parolees, who are on the “continuum” of state-imposed punish
    ments, have fewer expectations of privacy than probationers, because
    parole is more akin to imprisonment than probation is. “The essence
    of parole is release from prison, before the completion of sentence, on
    the condition that the prisoner abides by certain rules during the
    balance of the sentence.” Morrissey v. Brewer, 408 U. S. 471, 477.
    California’s system is consistent with these observations. An inmate
    electing to complete his sentence out of physical custody remains in
    the Department of Corrections’ legal custody for the remainder of his
    term and must comply with the terms and conditions of his parole.
    The extent and reach of those conditions demonstrate that parolees
    have severely diminished privacy expectations by virtue of their
    status alone. Additionally, as in Knights, the state law’s parole
    search condition was clearly expressed to petitioner, who signed an
    order submitting to the condition and thus was unambiguously aware
    of it. Examining the totality of the circumstances, petitioner did not
    have an expectation of privacy that society would recognize as legiti
    mate. The State’s interests, by contrast, are substantial. A State has
    an “overwhelming interest” in supervising parolees because they “are
    more likely to commit future criminal offenses.” Pennsylvania Bd. of
    Probation and Parole v. Scott, 524 U. S. 357, 365. Similarly, a State’s
    interests in reducing recidivism, thereby promoting reintegration and
    positive citizenship among probationers and parolees, warrant pri
    vacy intrusions that would not otherwise be tolerated under the
    Fourth Amendment. The Amendment does not render States power
    less to address these concerns effectively. California’s 60-to70
    percent recidivism rate demonstrates that most parolees are ill pre
    pared to handle the pressures of reintegration and require intense
    supervision. The State Legislature has concluded that, given the
    State’s number of parolees and its high recidivism rate, an individu
    alized suspicion requirement would undermine the State’s ability to
    effectively supervise parolees and protect the public from criminal
    acts by reoffenders. Contrary to petitioner’s argument, the fact that
    some States and the Federal Government require a level of individu
    alized suspicion before searching a parolee is of little relevance in de
    termining whether California’s system is drawn to meet the State’s
    needs and is reasonable, taking into account a parolee’s substantially
    diminished expectation of privacy. Nor is there merit to the argu
                     Cite as: 547 U. S. ___ (2006)                    3

                               Syllabus

  ment that California’s law grants discretion without procedural safe
  guards. The concern that the system gives officers unbridled discre
  tion to conduct searches, thereby inflicting dignitary harms that
  arouse strong resentment in parolees and undermine their ability to
  reintegrate into society, is belied by the State’s prohibition on arbi
  trary, capricious, or harassing searches. And petitioner’s concern
  that the law frustrates reintegration efforts by permitting intrusions
  into the privacy interests of third persons is unavailing because that
  concern would arise under a suspicion-based system as well. Pp. 5–
  12.
Affirmed.

   THOMAS, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and SCALIA, KENNEDY, GINSBURG, and ALITO, JJ., joined. STE
VENS, J., filed a dissenting opinion, in which SOUTER and BREYER, JJ.,
joined.
                        Cite as: 547 U. S. ____ (2006)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 04–9728
                                   _________________


      DONALD CURTIS SAMSON, PETITIONER v.

                 CALIFORNIA 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF

        CALIFORNIA, FIRST APPELLATE DISTRICT

                                 [June 19, 2006]

  JUSTICE THOMAS delivered the opinion of the Court.
  California law provides that every prisoner eligible for
release on state parole “shall agree in writing to be subject
to search or seizure by a parole officer or other peace
officer at any time of the day or night, with or without a
search warrant and with or without cause.” Cal. Penal
Code Ann. §3067(a) (West 2000). We granted certiorari to
decide whether a suspicionless search, conducted under
the authority of this statute, violates the Constitution. We
hold that it does not.
                             I
   In September 2002, petitioner Donald Curtis Samson
was on state parole in California, following a conviction for
being a felon in possession of a firearm. On September 6,
2002, Officer Alex Rohleder of the San Bruno Police De
partment observed petitioner walking down a street with
a woman and a child. Based on a prior contact with peti
tioner, Officer Rohleder was aware that petitioner was on
parole and believed that he was facing an at large war
rant. Accordingly, Officer Rohleder stopped petitioner and
asked him whether he had an outstanding parole warrant.
2                  SAMSON v. CALIFORNIA

                      Opinion of the Court

Petitioner responded that there was no outstanding war
rant and that he “was in good standing with his parole
agent.” Brief for Petitioner 4. Officer Rohleder confirmed,
by radio dispatch, that petitioner was on parole and that
he did not have an outstanding warrant. Nevertheless,
pursuant to Cal. Penal Code Ann. §3067(a) (West 2000)
and based solely on petitioner’s status as a parolee, Officer
Rohleder searched petitioner. During the search, Officer
Rohleder found a cigarette box in petitioner’s left breast
pocket. Inside the box he found a plastic baggie contain
ing methamphetamine.
   The State charged petitioner with possession of
methamphetamine pursuant to Cal. Health & Safety Code
Ann. §11377(a) (West 1991). The trial court denied peti
tioner’s motion to suppress the methamphetamine evi
dence, finding that Cal. Penal Code Ann. §3067(a) (West
2000) authorized the search and that the search was not
“arbitrary or capricious.” App. 62–63 (Proceedings on
Motion to Supress). A jury convicted petitioner of the
possession charge and the trial court sentenced him to
seven years’ imprisonment.
   The California Court of Appeal affirmed. Relying on
People v. Reyes, 19 Cal. 4th 743, 968 P. 2d 445 (1998), the
court held that suspicionless searches of parolees are
lawful under California law; that “ ‘[s]uch a search is
reasonable within the meaning of the Fourth Amendment
as long as it is not arbitrary, capricious or harassing’ ”; and
that the search in this case was not arbitrary, capricious,
or harassing. No. A102394 (Ct. App. Cal., 1st App. Dist.,
Oct. 14, 2004), App. 12–14.
   We granted certiorari, 545 U. S. ___ (2005), to answer a
variation of the question this Court left open in United
States v. Knights, 534 U. S. 112, 120, n. 6 (2001)—whether
a condition of release can so diminish or eliminate a re
leased prisoner’s reasonable expectation of privacy that a
suspicionless search by a law enforcement officer would
                      Cite as: 547 U. S. ____ (2006)                      3

                           Opinion of the Court

not offend the Fourth Amendment.1 Answering that
question in the affirmative today, we affirm the judgment
of the California Court of Appeal.
                              II
  “[U]nder our general Fourth Amendment approach” we
“examin[e] the totality of the circumstances” to determine
whether a search is reasonable within the meaning of the
Fourth Amendment. Id., at 118 (internal quotation marks
omitted). Whether a search is reasonable “is determined by
assessing, on the one hand, the degree to which it intrudes
upon an individual’s privacy and, on the other, the degree to
which it is needed for the promotion of legitimate govern
mental interests.” Id., at 118–119 (internal quotation
marks omitted).
  We recently applied this approach in United States v.
Knights. In that case, California law required Knights, as
a probationer, to “ ‘[s]ubmit his . . . person, property, place
of residence, vehicle, personal effects, to search anytime,
with or without a search warrant, warrant of arrest or
reasonable cause by any probation officer or law enforce
ment officer.’ ” Id., at 114 (brackets in original). Several
days after Knights had been placed on probation, police
suspected that he had been involved in several incidents of
arson and vandalism. Based upon that suspicion and
pursuant to the search condition of his probation, a police
officer conducted a warrantless search of Knights’ apart
ment and found arson and drug paraphernalia. Id., at
115–116.
  We concluded that the search of Knights’ apartment was
reasonable. In evaluating the degree of intrusion into
——————
   1 Knights, 534 U. S., at 120, n. 6 (“We do not decide whether the proba

tion condition so diminished, or completely eliminated, Knights’ reason
able expectation of privacy . . . that a search by a law enforcement officer
without any individualized suspicion would have satisfied the reasonable
ness requirement of the Fourth Amendment”).
4                  SAMSON v. CALIFORNIA

                     Opinion of the Court

Knights’ privacy, we found Knights’ probationary status
“salient,” id., at 118, observing that “[p]robation is ‘one
point . . . on a continuum of possible punishments ranging
from solitary confinement in a maximum-security facility
to a few hours of mandatory community service.’ ” Id., at
119 (quoting Griffin v. Wisconsin, 483 U. S. 868, 874
(1987)). Cf. Hudson v. Palmer, 468 U. S. 517, 530 (1984)
(holding that prisoners have no reasonable expectation of
privacy). We further observed that, by virtue of their status
alone, probationers “ ‘do not enjoy “the absolute liberty to
which every citizen is entitled,” ’ ” Knights, supra, at 119
(quoting Griffin, supra, at 874, in turn quoting Morrissey
v. Brewer, 408 U. S. 471, 480 (1972)), justifying the “im
pos[ition] [of] reasonable conditions that deprive the of
fender of some freedoms enjoyed by law-abiding citizens.”
Knights, supra, at 119. We also considered the facts that
Knights’ probation order clearly set out the probation
search condition, and that Knights was clearly informed of
the condition. See Knights, 534 U. S., at 119. We con
cluded that under these circumstances, Knights’ expecta
tion of privacy was significantly diminished. See id., at
119–120.
   We also concluded that probation searches, such as the
search of Knights’ apartment, are necessary to the promo
tion of legitimate governmental interests. Noting the
State’s dual interest in integrating probationers back into
the community and combating recidivism, see id., at 120–
121, we credited the “ ‘assumption’ ” that, by virtue of his
status, a probationer “ ‘is more likely than the ordinary
citizen to violate the law.’ ” Id., at 120 (quoting Griffin,
supra, at 880). We further found that “probationers have
even more of an incentive to conceal their criminal activi
ties and quickly dispose of incriminating evidence than the
ordinary criminal because probationers are aware that
they may be subject to supervision and face revocation of
probation, and possible incarceration, in proceedings in
                  Cite as: 547 U. S. ____ (2006)              5

                      Opinion of the Court

which the trial rights of a jury and proof beyond a reason
able doubt, among other things, do not apply.” Knights,
534 U. S., at 120. We explained that the State did not
have to ignore the reality of recidivism or suppress its
interests in “protecting potential victims of criminal en
terprise” for fear of running afoul of the Fourth Amend
ment. Id., at 121.
  Balancing these interests, we held that “[w]hen an
officer has reasonable suspicion that a probationer subject
to a search condition is engaged in criminal activity, there
is enough likelihood that criminal conduct is occurring
that an intrusion on the probationer’s significantly dimin
ished privacy interests is reasonable.” Ibid. Because the
search at issue in Knights was predicated on both the
probation search condition and reasonable suspicion, we
did not reach the question whether the search would have
been reasonable under the Fourth Amendment had it been
solely predicated upon the condition of probation. Id., at
120, n. 6. Our attention is directed to that question today,
albeit in the context of a parolee search.
                               III
   As we noted in Knights, parolees are on the “continuum”
of state-imposed punishments. Id., at 119 (internal quota
tion marks omitted). On this continuum, parolees have
fewer expectations of privacy than probationers, because
parole is more akin to imprisonment than probation is to
imprisonment. As this Court has pointed out, “parole is an
established variation on imprisonment of convicted crimi
nals. . . . The essence of parole is release from prison, before
the completion of sentence, on the condition that the pris
oner abides by certain rules during the balance of the sen
tence.” Morrissey, supra, at 477. “In most cases, the State
is willing to extend parole only because it is able to condition
it upon compliance with certain requirements.” Pennsyl
vania Bd. of Probation and Parole v. Scott, 524 U. S. 357,
6                     SAMSON v. CALIFORNIA

                          Opinion of the Court

365 (1998). See also United States v. Reyes, 283 F. 3d 446,
461 (CA2 2002) (“[F]ederal supervised release, . . . in
contrast to probation, is meted out in addition to, not in
lieu of, incarceration” (citation and internal quotation
marks omitted)); United States v. Cardona, 903 F. 2d 60,
63 (CA1 1990) (“[O]n the Court’s continuum of possible
punishments, parole is the stronger medicine; ergo, parol
ees enjoy even less of the average citizen’s absolute liberty
than do probationers” (internal quotation marks and
citation omitted)).2
   California’s system of parole is consistent with these
observations: A California inmate may serve his parole
period either in physical custody, or elect to complete his
sentence out of physical custody and subject to certain
conditions. Cal. Penal Code Ann. §3060.5 (West 2000).
Under the latter option, an inmate-turned-parolee re
mains in the legal custody of the California Department of
Corrections through the remainder of his term, §3056, and
——————
    2 Contrary
             to the dissent’s contention, nothing in our recognition that
parolees are more akin to prisoners than probationers is inconsistent
with our precedents. Nor, as the dissent suggests, do we equate parol
ees with prisoners for the purpose of concluding that parolees, like
prisoners, have no Fourth Amendment rights. See post, at 5 (opinion of
STEVENS, J.). That view misperceives our holding. If that were the
basis of our holding, then this case would have been resolved solely
under Hudson v. Palmer, 468 U. S. 517 (1984), and there would have
been no cause to resort to Fourth Amendment analysis. See ibid.
(holding traditional Fourth Amendment analysis of the totality of the
circumstances inapplicable to the question whether a prisoner had a
reasonable expectation of privacy in his prison cell). Nor is our ration
ale inconsistent with Morrissey v. Brewer, 408 U. S. 471, 482 (1972). In
that case, the Court recognized that restrictions on a parolee’s liberty
are not unqualified. That statement, even if accepted as a truism,
sheds no light on the extent to which a parolee’s constitutional rights
are indeed limited—and no one argues that a parolee’s constitutional
rights are not limited. Morrissey itself does not cast doubt on today’s
holding given that the liberty at issue in that case—the Fourteenth
Amendment Due Process right to a hearing before revocation of pa
role—invokes wholly different analysis than the search at issue here.
                 Cite as: 547 U. S. ____ (2006)            7

                     Opinion of the Court

must comply with all of the terms and conditions of parole,
including mandatory drug tests, restrictions on association
with felons or gang members, and mandatory meetings
with parole officers, Cal. Code Regs., tit. 15, §2512 (2005);
Cal. Penal Code Ann. §3067 (West 2000). See also Morris
sey, supra, at 478 (discussing other permissible terms and
conditions of parole). General conditions of parole also
require a parolee to report to his assigned parole officer
immediately upon release, inform the parole officer within
72 hours of any change in employment status, request
permission to travel a distance of more than 50 miles from
the parolee’s home, and refrain from criminal conduct and
possession of firearms, specified weapons, or knives unre
lated to employment. Cal. Code Regs., tit. 15, §2512.
Parolees may also be subject to special conditions, includ
ing psychiatric treatment programs, mandatory absti
nence from alcohol, residence approval, and “[a]ny other
condition deemed necessary by the Board [of Parole Hear
ings] or the Department [of Corrections and Rehabilita
tion] due to unusual circumstances.” §2513. The extent
and reach of these conditions clearly demonstrate that
parolees like petitioner have severely diminished expecta
tions of privacy by virtue of their status alone.
   Additionally, as we found “salient” in Knights with
respect to the probation search condition, the parole
search condition under California law—requiring inmates
who opt for parole to submit to suspicionless searches by a
parole officer or other peace officer “at any time,” Cal.
Penal Code Ann. §3067(a) (West 2000)—was “clearly
expressed” to petitioner. Knights, 534 U. S., at 119. He
signed an order submitting to the condition and thus was
“unambiguously” aware of it. Ibid. In Knights, we found
that acceptance of a clear and unambiguous search condi
tion “significantly diminished Knights’ reasonable expec
tation of privacy.” Id., at 120. Examining the totality of
the circumstances pertaining to petitioner’s status as a
8                      SAMSON v. CALIFORNIA

                          Opinion of the Court

parolee, “an established variation on imprisonment,” Mor
rissey, 408 U. S., at 477, including the plain terms of the
parole search condition, we conclude that petitioner did
not have an expectation of privacy that society would
recognize as legitimate.3
   The State’s interests, by contrast, are substantial. This
Court has repeatedly acknowledged that a State has an
“overwhelming interest” in supervising parolees because
“parolees. . . are more likely to commit future criminal
offenses.” Pennsylvania Bd. of Probation and Parole, 524
U. S., at 365 (explaining that the interest in combating
recidivism “is the very premise behind the system of close
parole supervision”). Similarly, this Court has repeatedly
acknowledged that a State’s interests in reducing recidivism
and thereby promoting reintegration and positive citizen
——————
    3 Because we find that the search at issue here is reasonable under
our general Fourth Amendment approach, we need not reach the issue
whether “acceptance of the search condition constituted consent in the
Schneckloth [v. Bustamonte, 412 U. S. 218 (1973),] sense of a complete
waiver of his Fourth Amendment rights.” United States v. Knights, 534
U. S. 112, 118 (2001). The California Supreme Court has not yet
construed Cal. Penal Code Ann. §3067 (West 2000), the statute which
governs parole for crimes committed after 1996, and which imposes the
consent requirement. The California Court of Appeal has, and it has
concluded that, under §3067(b), “inmates who are otherwise eligible for
parole yet refuse to agree to the mandatory search condition will
remain imprisoned . . . until either the inmate (1) agrees to the search
condition and is otherwise eligible for parole or (2) has lost all worktime
credits and is eligible for release after having served the balance of
his/her sentence.” People v. Middleton, 131 Cal. App. 4th 732, 739–740,
31 Cal. Rptr. 3d 813, 818 (2005). Nonetheless, we decline to rest our
holding today on the consent rationale. The California Supreme Court,
we note, has not yet had a chance to address the question squarely, and
it is far from clear that the State properly raised its consent theory in
the courts below.
   Nor do we address whether California’s parole search condition is
justified as a special need under Griffin v. Wisconsin, 483 U. S. 868
(1987), because our holding under general Fourth Amendment princi
ples renders such an examination unnecessary.
                 Cite as: 547 U. S. ____ (2006)            9

                     Opinion of the Court

ship among probationers and parolees warrant privacy
intrusions that would not otherwise be tolerated under the
Fourth Amendment. See Griffin, 483 U. S., at 879; Knights,
supra, at 121.
  The empirical evidence presented in this case clearly
demonstrates the significance of these interests to the
State of California. As of November 30, 2005, California
had over 130,000 released parolees. California’s parolee
population has a 68-to-70 percent recidivism rate. See
California Attorney General, Crime in California 37 (Apr.
2001) (explaining that 68 percent of adult parolees are
returned to prison, 55 percent for a parole violation, 13
percent for the commission of a new felony offense); J.
Petersilia, Challenges of Prisoner Reentry and Parole in
California, 12 California Policy Research Center Brief, p. 2
(June 2000), available at http://www.ucop.edu/cprc/pa
role.pdf (as visited June 15, 2006, and available in Clerk of
Court’s case file) (“70% of the state’s paroled felons reof
fend within 18 months—the highest recidivism rate in the
nation”). This Court has acknowledged the grave safety
concerns that attend recidivism. See Ewing v. California,
538 U. S. 11, 26 (2003) (plurality opinion) (“Recidivism is a
serious public safety concern in California and throughout
the Nation”).
  As we made clear in Knights, the Fourth Amendment
does not render the States powerless to address these
concerns effectively. See 534 U. S., at 121. Contrary to
petitioner’s contention, California’s ability to conduct
suspicionless searches of parolees serves its interest in
reducing recidivism, in a manner that aids, rather than
hinders, the reintegration of parolees into productive
society.
  In California, an eligible inmate serving a determinate
sentence may elect parole when the actual days he has
served plus statutory time credits equal the term imposed
by the trial court, Cal. Penal Code Ann. §§2931, 2933,
10                SAMSON v. CALIFORNIA

                     Opinion of the Court

3000(b)(1) (West 2000), irrespective of whether the inmate
is capable of integrating himself back into productive
society. As the recidivism rate demonstrates, most parol
ees are ill prepared to handle the pressures of reintegra
tion. Thus, most parolees require intense supervision.
The California Legislature has concluded that, given the
number of inmates the State paroles and its high recidi
vism rate, a requirement that searches be based on indi
vidualized suspicion would undermine the State’s ability
to effectively supervise parolees and protect the public
from criminal acts by reoffenders. This conclusion makes
eminent sense. Imposing a reasonable suspicion require
ment, as urged by petitioner, would give parolees greater
opportunity to anticipate searches and conceal criminality.
See Knights, supra, at 120; Griffin, 483 U. S., at 879. This
Court concluded that the incentive-to-conceal concern
justified an “intensive” system for supervising probation
ers in Griffin, id., at 875. That concern applies with even
greater force to a system of supervising parolees. See
United States v. Reyes, 283 F. 3d, at 461 (observing that
the Griffin rationale “appl[ies] a fortiori” to “federal su
pervised release, which, in contrast to probation, is ‘meted
out in addition to, not in lieu of, incareration’ ”); United
States v. Crawford, 372 F. 3d 1048, 1077 (CA9 2004) (en
banc) (Kleinfeld, J., concurring) (explaining that parolees,
in contrast to probationers, “have been sentenced to prison
for felonies and released before the end of their prison
terms” and are “deemed to have acted more harmfully
than anyone except those felons not released on parole”);
Hudson, 468 U. S., at 526 (persons sentenced to terms of
imprisonment have been “deemed to have acted more
harmfully than anyone except those felons not released on
parole”); id., at 529 (observing that it would be “naive” to
institute a system of “ ‘planned random searches’ ” as that
would allow prisoners to “anticipate” searches, thus de
feating the purpose of random searches).
                     Cite as: 547 U. S. ____ (2006)                   11

                          Opinion of the Court

   Petitioner observes that the majority of States and the
Federal Government have been able to further similar
interests in reducing recidivism and promoting re
integration, despite having systems that permit parolee
searches based upon some level of suspicion. Thus, peti
tioner contends, California’s system is constitutionally
defective by comparison. Petitioner’s reliance on the
practices of jurisdictions other than California, however, is
misplaced. That some States and the Federal Government
require a level of individualized suspicion is of little rele
vance to our determination whether California’s supervi
sory system is drawn to meet its needs and is reasonable,
taking into account a parolee’s substantially diminished
expectation of privacy.4
   Nor is there merit to the argument that California’s
parole search law permits “a blanket grant of discretion
——————
   4 The dissent argues that, “once one acknowledges that parolees do

have legitimate expectations of privacy beyond those of prisoners, our
Fourth Amendment jurisprudence does not permit the conclusion,
reached by the Court here for the first time, that a search supported by
neither individualized suspicion nor ‘special needs’ is nonetheless
‘reasonable.’ ” Post, at 2. That simply is not the case. The touchstone
of the Fourth Amendment is reasonableness, not individualized suspi
cion. Thus, while this Court’s jurisprudence has often recognized that
“to accommodate public and private interests some quantum of indi
vidualized suspicion is usually a prerequisite to a constitutional search
or seizure,” United States v. Martinez-Fuerte, 428 U. S. 543, 560 (1976),
we have also recognized that the “Fourth Amendment imposes no
irreducible requirement of such suspicion,” id., at 561. Therefore,
although this Court has only sanctioned suspicionless searches in
limited circumstances, namely programmatic and special needs
searches, we have never held that these are the only limited circum
stances in which searches absent individualized suspicion could be
“reasonable” under the Fourth Amendment. In light of California’s
earnest concerns respecting recidivism, public safety, and reintegration
of parolees into productive society, and because the object of the Fourth
Amendment is reasonableness, our decision today is far from remark
able. Nor, given our prior precedents and caveats, is it “unprece
dented.” Post, at 1.
12                   SAMSON v. CALIFORNIA

                        Opinion of the Court

untethered by any procedural safeguards,” post, at 1
(STEVENS, J., dissenting). The concern that California’s
suspicionless search system gives officers unbridled dis
cretion to conduct searches, thereby inflicting dignitary
harms that arouse strong resentment in parolees and
undermine their ability to reintegrate into productive
society, is belied by California’s prohibition on “arbitrary,
capricious or harassing” searches. See Reyes, 19 Cal. 4th,
at 752, 753–754, 968 P. 2d, at 450, 451; People v. Bravo, 43
Cal. 3d 600, 610, 738 P. 2d 336, 342 (1987) (probation); see
also Cal. Penal Code Ann. §3067(d) (West 2000) (“It is not
the intent of the Legislature to authorize law enforcement
officers to conduct searches for the sole purpose of har
assment”).5 The dissent’s claim that parolees under Cali
fornia law are subject to capricious searches conducted at
the unchecked “whim” of law enforcement officers, post, at
3, 4, ignores this prohibition. Likewise, petitioner’s con
cern that California’s suspicionless search law frustrates
reintegration efforts by permitting intrusions into the
privacy interests of third parties is also unavailing be
cause that concern would arise under a suspicion-based
regime as well.
                             IV
   Thus, we conclude that the Fourth Amendment does not
prohibit a police officer from conducting a suspicionless
search of a parolee. Accordingly, we affirm the judgment
of the California Court of Appeal.
                                           It is so ordered.



——————
  5 Under California precedent, we note, an officer would not act rea

sonably in conducting a suspicionless search absent knowledge that the
person stopped for the search is a parolee. See People v. Sanders, 31
Cal. 4th 318, 331–332, 73 P. 3d 496, 505–506 (2003); Brief for United
States as Amicus Curiae 20.
                 Cite as: 547 U. S. ____ (2006)           1

                    STEVENS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–9728
                         _________________


     DONALD CURTIS SAMSON, PETITIONER v.

                CALIFORNIA 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF

        CALIFORNIA, FIRST APPELLATE DISTRICT

                        [June 19, 2006]

  JUSTICE STEVENS, with whom JUSTICE SOUTER and
JUSTICE BREYER join, dissenting.
  Our prior cases have consistently assumed that the
Fourth Amendment provides some degree of protection for
probationers and parolees. The protection is not as robust
as that afforded to ordinary citizens; we have held that
probationers’ lowered expectation of privacy may justify
their warrantless search upon reasonable suspicion of
wrongdoing, see United States v. Knights, 534 U. S. 112
(2001). We have also recognized that the supervisory
responsibilities of probation officers, who are required to
provide “ ‘individualized counseling’ ” and to monitor their
charges’ progress, Griffin v. Wisconsin, 483 U. S. 868, 876–
877 (1987), and who are in a unique position to judge “how
close a supervision the probationer requires,” id., at 876,
may give rise to special needs justifying departures from
Fourth Amendment strictures. See ibid. (“Although a
probation officer is not an impartial magistrate, neither is
he the police officer who normally conducts searches against
the ordinary citizen”). But neither Knights nor Griffin
supports a regime of suspicionless searches, conducted
pursuant to a blanket grant of discretion untethered by
any procedural safeguards, by law enforcement personnel
who have no special interest in the welfare of the parolee
or probationer.
2                  SAMSON v. CALIFORNIA

                    STEVENS, J., dissenting

   What the Court sanctions today is an unprecedented
curtailment of liberty. Combining faulty syllogism with
circular reasoning, the Court concludes that parolees have
no more legitimate an expectation of privacy in their
persons than do prisoners. However superficially appeal
ing that parity in treatment may seem, it runs roughshod
over our precedent. It also rests on an intuition that fares
poorly under scrutiny. And once one acknowledges that
parolees do have legitimate expectations of privacy beyond
those of prisoners, our Fourth Amendment jurisprudence
does not permit the conclusion, reached by the Court here
for the first time, that a search supported by neither indi
vidualized suspicion nor “special needs” is nonetheless
“reasonable.”
   The suspicionless search is the very evil the Fourth
Amendment was intended to stamp out. See Boyd v.
United States, 116 U. S. 616, 625–630 (1886); see also, e.g.,
Indianapolis v. Edmond, 531 U. S. 32, 37 (2000). The pre-
Revolutionary “writs of assistance,” which permitted
roving searches for contraband, were reviled precisely
because they “placed ‘the liberty of every man in the hands
of every petty officer.’ ” Boyd, 116 U. S., at 625. While
individualized suspicion “is not an ‘irreducible’ component
of reasonableness” under the Fourth Amendment, Ed
mond, 531 U. S., at 37 (quoting United States v. Marti
nez-Fuerte, 428 U. S. 543, 561 (1976)), the requirement
has been dispensed with only when programmatic
searches were required to meet a “ ‘special need’ . . . di
vorced from the State’s general interest in law enforce
ment.” Ferguson v. Charleston, 532 U. S. 67, 79 (2001);
see Edmond, 531 U. S., at 37; see also Griffin, 483 U. S., at
873 (“Although we usually require that a search be under
taken only pursuant to a warrant (and thus supported by
probable cause, as the Constitution says warrants must
be), . . . we have permitted exceptions when ‘special needs,
beyond the normal need for law enforcement, make the
                       Cite as: 547 U. S. ____ (2006)                        3

                          STEVENS, J., dissenting

warrant and probable-cause requirement impracticable’ ”).
   Not surprisingly, the majority does not seek to justify
the search of petitioner on “special needs” grounds. Al
though the Court has in the past relied on special needs to
uphold warrantless searches of probationers, id., at 873,
880, it has never gone so far as to hold that a probationer
or parolee may be subjected to full search at the whim of
any law enforcement officer he happens to encounter,
whether or not the officer has reason to suspect him of
wrongdoing. Griffin, after all, involved a search by a
probation officer that was supported by reasonable suspi
cion. The special role of probation officers was critical to
the analysis; “we deal with a situation,” the Court ex
plained, “in which there is an ongoing supervisory rela
tionship—and one that is not, or at least not entirely,
adversarial—between the object of the search and the
decisionmaker.” Id., at 879. The State’s interest or “spe
cial need,” as articulated in Griffin, was an interest in
supervising the wayward probationer’s reintegration into
society—not, or at least not principally, the general law
enforcement goal of detecting crime, see ante, at 8–9.1
——————
   1 As we observed in Ferguson v. Charleston, 532 U. S. 67 (2001), Grif

fin’s special needs rationale was cast into doubt by our later decision in
Skinner v. Railway Labor Executives’ Assn., 489 U. S. 602 (1989), which
reserved the question whether “ ‘routine use in criminal prosecutions of
evidence obtained pursuant to the administrative scheme would give rise
to an inference of pretext, or otherwise impugn the administrative nature
of the . . . program,’ ” Ferguson, 532 U. S., at 79, n. 15 (quoting Skinner,
489 U. S., at 621, n. 5). But at least the State in Griffin could in good faith
contend that its warrantless searches were supported by a special need
conceptually distinct from law enforcement goals generally. Indeed, that a
State’s interest in supervising its parolees and probationers to ensure
their smooth reintegration may occasionally diverge from its general law
enforcement aims is illustrated by this very case. Petitioner’s possession
of a small amount of illegal drugs would not have been grounds for
revocation of his parole. See Cal. Penal Code Ann. §3063.1(a) (West Supp.
2006). Presumably, the California Legislature determined that it is
unnecessary and perhaps even counterproductive, as a means of further
4                     SAMSON v. CALIFORNIA

                        STEVENS, J., dissenting

   It is no accident, then, that when we later upheld the
search of a probationer by a law enforcement officer (again,
based on reasonable suspicion), we forwent any reliance on
the special needs doctrine. See Knights, 534 U. S. 112.
Even if the supervisory relationship between a probation
officer and her charge may properly be characterized as
one giving rise to needs “divorced from the State’s general
interest in law enforcement,” Ferguson, 532 U. S., at 79;
but see id., at 79, n. 15, the relationship between an ordi
nary law enforcement officer and a probationer unknown
to him may not. “None of our special needs precedents has
sanctioned the routine inclusion of law enforcement, both
in the design of the policy and in using arrests, either
threatened or real, to implement the system designed for
the special needs objectives.” Id., at 88 (KENNEDY, J.,
concurring in judgment).
   Ignoring just how “closely guarded” is that “category of
constitutionally permissible suspicionless searches,”
Chandler v. Miller, 520 U. S. 305, 309 (1997), the Court for
the first time upholds an entirely suspicionless search
unsupported by any special need. And it goes further: In
special needs cases we have at least insisted upon pro
grammatic safeguards designed to ensure evenhandedness
in application; if individualized suspicion is to be jetti
soned, it must be replaced with measures to protect
against the state actor’s unfettered discretion. See, e.g.,
Delaware v. Prouse, 440 U. S. 648, 654–655 (1979) (where
a special need “precludes insistence upon ‘some quantum
of individualized suspicion,’ other safeguards are generally
relied upon to assure that the individual’s reasonable
expectation of privacy is not ‘subject to the discretion of
the official in the field’ ” (quoting Camara v. Municipal
—————— 

ing the goals of the parole system, to reincarcerate former prisoners for

simple possession. The general law enforcement interests the State 

espouses, by contrast, call for reincarceration. 

                       Cite as: 547 U. S. ____ (2006)                        5

                          STEVENS, J., dissenting

Court of City and County of San Francisco, 387 U. S. 523,
532 (1967); footnote omitted); United States v. Brignoni-
Ponce, 422 U. S. 873, 882 (1975) (“[T]he reasonableness
requirement of the Fourth Amendment demands some
thing more than the broad and unlimited discretion
sought by the Government”). Here, by contrast, there are
no policies in place—no “standards, guidelines, or proce
dures,” Prouse, 440 U. S., at 650—to rein in officers and
furnish a bulwark against the arbitrary exercise of discre
tion that is the height of unreasonableness.
   The Court is able to make this unprecedented move only
by making another. Coupling the dubious holding of
Hudson v. Palmer, 468 U. S. 517 (1984), with the bald
statement that “parolees have fewer expectations of pri
vacy than probationers,” ante, at 5, the Court two-steps its
way through a faulty syllogism and, thus, avoids the
application of Fourth Amendment principles altogether.
The logic, apparently, is this: Prisoners have no legitimate
expectation of privacy; parolees are like prisoners; there
fore, parolees have no legitimate expectation of privacy.
The conclusion is remarkable not least because we have
long embraced its opposite.2 It also rests on false prem
ises. First, it is simply not true that a parolee’s status,
vis-à-vis either the State or the Constitution, is tanta
mount to that of a prisoner or even materially distinct
from that of a probationer. See Morrissey v. Brewer, 408
U. S. 471, 482 (1972) (“Though the State properly subjects
[a parolee] to many restrictions not applicable to other
——————
  2 See  Morrissey v. Brewer, 408 U. S. 471, 482 (1972) (“[T]he liberty of a
parolee, although indeterminate, includes many of the core values of
unqualified liberty”); Griffin v. Wisconsin, 483 U. S. 868, 875 (1987) (the
“degree of impingement upon [a probationer’s] privacy . . . is not unlim
ited”); see also Ferguson, 532 U. S., at 101 (SCALIA, J., dissenting) (“I doubt
whether Griffin’s reasonable expectation of privacy in his home was any
less than petitioners’ reasonable expectation of privacy in their urine
taken”).
6                  SAMSON v. CALIFORNIA

                     STEVENS, J., dissenting

citizens, his condition is very different from that of con
finement in a prison”). A parolee, like a probationer, is set
free in the world subject to restrictions intended to facili
tate supervision and guard against antisocial behavior. As
with probation, “the State is willing to extend parole only
because it is able to condition it upon compliance with
certain requirements.” Pennsylvania Bd. of Probation and
Parole v. Scott, 524 U. S. 357, 365 (1998). Certainly,
parole differs from probation insofar as parole is “ ‘meted
out in addition to, not in lieu of, incarceration.’ ” Ante, at 6
(quoting United States v. Reyes, 283 F. 3d 446, 461 (CA2
2002)). And, certainly, parolees typically will have com
mitted more serious crimes—ones warranting a prior term
of imprisonment—than probationers. The latter distinc
tion, perhaps, would support the conclusion that a State
has a stronger interest in supervising parolees than it
does in supervising probationers. But see United States v.
Williams, 417 F. 3d 373, 376, n. 1 (CA3 2005) (“ ‘[T]here is
no constitutional difference between probation and parole
for purposes of the [F]ourth [A]mendment’ ”). But why
either distinction should result in refusal to acknowledge
as legitimate, when harbored by parolees, the same expec
tation of privacy that probationers reasonably may harbor
is beyond fathom.
   In any event, the notion that a parolee legitimately
expects only so much privacy as a prisoner is utterly with
out foundation. Hudson v. Palmer does stand for the
proposition that “[a] right of privacy in traditional Fourth
Amendment terms” is denied individuals who are incar
cerated. 468 U. S., at 527. But this is because it “is neces
sary, as a practical matter, to accommodate a myriad of
‘institutional needs and objectives’ of prison facilities, . . .
chief among which is internal security.” Id., at 524; see
id., at 538 (O’Connor, J., concurring) (“I agree that the
government’s compelling interest in prison safety, together
with the necessarily ad hoc judgments required of prison
                     Cite as: 547 U. S. ____ (2006)                    7

                        STEVENS, J., dissenting

officials, make prison cell searches and seizures appropri
ate for categorical treatment”3); see also Treasury Employ
ees v. Von Raab, 489 U. S. 656, 680 (1989) (SCALIA, J.,
dissenting). These “institutional needs”—safety of in
mates and guards, “internal order,” and sanitation, Hud
son, 468 U. S., at 527–528—manifestly do not apply to
parolees. As discussed above and in Griffin, other state
interests may warrant certain intrusions into a parolee’s
privacy, but Hudson’s rationale cannot be mapped blindly
onto the situation with which we are presented in this
case.
   Nor is it enough, in deciding whether someone’s expec
tation of privacy is “legitimate,” to rely on the existence of
the offending condition or the individual’s notice thereof.
Cf. ante, at 7. The Court’s reasoning in this respect is
entirely circular. The mere fact that a particular State
refuses to acknowledge a parolee’s privacy interest cannot
mean that a parolee in that State has no expectation of
privacy that society is willing to recognize as legitimate—
especially when the measure that invades privacy is both
the subject of the Fourth Amendment challenge and a
clear outlier. With only one or two arguable exceptions,
neither the Federal Government nor any other State
subjects parolees to searches of the kind to which peti
tioner was subjected. And the fact of notice hardly cures
the circularity; the loss of a subjective expectation of pri
vacy would play “no meaningful role” in analyzing the
legitimacy of expectations, for example, “if the Govern
ment were suddenly to announce on nationwide television
that all homes henceforth would be subject to warrantless
entry.” Smith v. Maryland, 442 U. S. 735, 740–741, n. 5
——————
  3 Particularly in view of Justice O’Connor’s concurrence, which em

phasized the prison’s programmatic interests in conducting suspi
cionless searches, see Hudson, 468 U. S., at 538, Hudson is probably best
understood as a “special needs” case—not as standing for the blanket
proposition that prisoners have no Fourth Amendment rights.
8                      SAMSON v. CALIFORNIA

                         STEVENS, J., dissenting

(1979).4
    Threaded through the Court’s reasoning is the sugges
tion that deprivation of Fourth Amendment rights is part
and parcel of any convict’s punishment. See ante, at 4–6.5
If a person may be subject to random and suspicionless
searches in prison, the Court seems to assume, then he
cannot complain when he is subject to the same invasion
outside of prison, so long as the State still can imprison
him. Punishment, though, is not the basis on which Hud
son was decided. (Indeed, it is settled that a prison inmate
“ ‘retains those [constitutional] rights that are not incon
sistent with his status as a prisoner or with the legitimate
penological objectives of the corrections system.’ ” Turner
v. Safley, 482 U. S. 78, 95 (1987).) Nor, to my knowledge,
have we ever sanctioned the use of any search as a puni
tive measure. Instead, the question in every case must be
whether the balance of legitimate expectations of privacy,
on the one hand, and the State’s interests in conducting
the relevant search, on the other, justifies dispensing with
——————
   4 Likewise, the State’s argument that a California parolee “consents”

to the suspicionless search condition is sophistry. Whether or not a
prisoner can choose to remain in prison rather than be released on
parole, cf. ante, at 8, n. 3, he has no “choice” concerning the search
condition; he may either remain in prison, where he will be subjected to
suspicionless searches, or he may exit prison and still be subject to
suspicionless searches. Accordingly, “to speak of consent in this context
is to resort to a manifest fiction, for the [parolee] who purportedly
waives his rights by accepting such a condition has little genuine option
to refuse.” 5 W. LaFave, Search and Seizure: A Treatise on the Fourth
Amendment §10.10(b), pp. 440–441 (4th ed. 2004).
   5 This is a vestige of the long-discredited “act of grace” theory of pa

role. Compare Escoe v. Zerbst, 295 U. S. 490, 492–493 (1935) (“Probation
or suspension of sentence comes as an act of grace to one convicted of a
crime, and may be coupled with such conditions in respect of its duration
as Congress may impose”), with Gagnon v. Scarpelli, 411 U. S. 778, 782, n.
4 (1973) (“a probationer can no longer be denied due process, in reliance
on the dictum in Escoe v. Zerbst, that probation is an ‘act of grace’ ”
(citation omitted)). See also Morrissey, 408 U. S., at 482.
                    Cite as: 547 U. S. ____ (2006)                  9

                       STEVENS, J., dissenting

the warrant and probable-cause requirements that are
otherwise dictated by the Fourth Amendment. That bal
ance is not the same in prison as it is out. We held in
Knights—without recourse to Hudson—that the balance
favored allowing the State to conduct searches based on
reasonable suspicion. Never before have we plunged
below that floor absent a demonstration of “special needs.”
   Had the State imposed as a condition of parole a re
quirement that petitioner submit to random searches by
his parole officer, who is “supposed to have in mind the
welfare of the [parolee]” and guide the parolee’s transition
back into society, Griffin, 483 U. S., at 876–877, the condi
tion might have been justified either under the special
needs doctrine or because at least part of the requisite
“reasonable suspicion” is supplied in this context by the
individual-specific knowledge gained through the supervi
sory relationship. See id., at 879 (emphasizing probation
office’s ability to “assess probabilities in the light of its
knowledge of [the probationer’s] life, character, and cir
cumstances”). Likewise, this might have been a different
case had a court or parole board imposed the condition at
issue based on specific knowledge of the individual’s
criminal history and projected likelihood of reoffending, or
if the State had had in place programmatic safeguards to
ensure evenhandedness. See supra, at 4. Under either of
those scenarios, the State would at least have gone some
way toward averting the greatest mischief wrought by
officials’ unfettered discretion. But the search condition
here is imposed on all parolees—whatever the nature of
their crimes, whatever their likelihood of recidivism, and
whatever their supervisory needs—without any program
matic procedural protections.6
——————
  6 The Court devotes a good portion of its analysis to the recidivism

rates among parolees in California. See ante, at 8–9. One might
question whether those statistics, which postdate the California Su
10                     SAMSON v. CALIFORNIA

                         STEVENS, J., dissenting

   The Court seems to acknowledge that unreasonable
searches “inflic[t] dignitary harms that arouse strong
resentment in parolees and undermine their ability to
reintegrate into productive society.” Ante, at 11; see Terry
v. Ohio, 392 U. S. 1, 19, 29 (1968). It is satisfied, however,
that the California courts’ prohibition against “ ‘arbitrary,
capricious or harassing’ ” searches suffices to avert those
harms—which are of course counterproductive to the
State’s purported aim of rehabilitating former prisoners
and reintegrating them into society. See ante, at 11 (citing
People v. Reyes, 19 Cal. 4th 743, 968 P. 2d 445 (1998)). I
am unpersuaded.        The requirement of individualized
suspicion, in all its iterations, is the shield the Framers
selected to guard against the evils of arbitrary action,
caprice, and harassment. To say that those evils may be
averted without that shield is, I fear, to pay lipservice to
the end while withdrawing the means.7
   Respectfully, I dissent.




——————
preme Court’s decision to allow the purportedly recidivism-reducing
suspicionless searches at issue here, actually demonstrate that the
State’s interest is being served by the searches. Cf. Reply Brief for
Petitioner 10, and n. 10. Of course, one cannot deny that the interest
itself is valid. That said, though, it has never been held sufficient to
justify suspicionless searches. If high crime rates were grounds enough
for disposing of Fourth Amendment protections, the Amendment long
ago would have become a dead letter.
   7 As the Court observes, see ante, at 12, n. 5, under California law “an

officer is entitled to conduct suspicionless searches only of persons
known by him to be parolees.” Brief for United States as Amicus
Curiae 20 (citing People v. Sanders, 31 Cal. 4th 318, 331–332, 73 P. 3d
496, 505 (2003)). It would necessarily be arbitrary, capricious, and
harassing to conduct a suspicionless search of someone without knowl
edge of the status that renders that person, in the State’s judgment,
susceptible to such an invasion.

```

---

## GROUP: content/cases/Scott v. Harris.md  (`case`, 5 assertions)

### content_page

```
---
title: "Scott v. Harris"
type: case
citation: "550 U.S. 372 (2007)"
parallel_cite: "127 S. Ct. 1769; 167 L. Ed. 2d 686"
neutral_cite: 2007 U.S. LEXIS 4748
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2007
date_decided: 2007-04-30
docket: 05-1631
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2007-04-30
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Scott v. Harris
  varies_by_point: false
  scope_note: "Reads Tennessee v. Garner as an application of Graham reasonableness, not a rigid test."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145738/scott-v-harris/"
  cluster_id: 145738
  opinion_id: 145738
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Tennessee v. Garner]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "fourth-amendment", "use-of-force", "seizure", "section-1983"]
holding: "*Garner* is not a rigid separate test but 'simply an application' of *Graham* reasonableness — no 'magical on/off switch'; ramming a fleeing motorist who endangered the public was reasonable."
lake:
  record_id: Scott v. Harris
  status: verified
  projected_at: 2026-07-06
---

# Scott v. Harris

*550 U.S. 372 (2007)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Deputy Timothy Scott ended a high-speed chase of Victor Harris—who had fled a traffic stop and reached roughly 85 m.p.h. on two-lane roads—by ramming the rear of Harris's car, causing a crash that left Harris a quadriplegic. A police video captured the pursuit. Harris sued under 42 U.S.C. § 1983 for excessive force; the lower courts denied Scott [[Qualified Immunity|qualified immunity]].

## Issue
Whether an officer's ramming of a fleeing motorist's vehicle to terminate a dangerous high-speed chase is an unreasonable seizure under the Fourth Amendment, and whether the deadly-force preconditions of *[[Tennessee v. Garner]]* rigidly control that question.

## Rule
The reasonableness of force is judged under the Fourth Amendment's objective-reasonableness standard, and *[[Tennessee v. Garner|Garner]]* does not impose rigid preconditions. "*Garner* did not establish a magical on/off switch that triggers rigid preconditions whenever an officer's actions constitute 'deadly force.'" — 127 S. Ct. 1769, 1777. ^pin-1777

*[[Tennessee v. Garner|Garner]]* "was simply an application of the Fourth Amendment's 'reasonableness' test ... to the use of a particular type of force in a particular situation." — *Id.* The Court then announced the operative rule: "A police officer's attempt to terminate a dangerous high-speed car chase that threatens the lives of innocent bystanders does not violate the Fourth Amendment, even when it places the fleeing motorist at risk of serious injury or death." — *Id.* at 1779. ^pin-1779

## Application
On the videotaped facts, Harris's chase posed a substantial and immediate risk of serious physical injury to bystanders—he swerved through traffic, crossed double-yellow lines, and ran red lights—so no reasonable jury could find otherwise. Scott's ramming was a seizure, but because it was an objectively reasonable response to that danger, *[[Tennessee v. Garner|Garner]]*'s preconditions did not render it [[Common Legal Terms#per-se|per se]] unreasonable. Scott was therefore entitled to summary judgment.

## Conclusion
Scott's attempt to end the chase by forcing Harris off the road was reasonable; Scott was entitled to summary judgment, and the Eleventh Circuit was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Scott* clarifies that [[Tennessee v. Garner]] is not a "magical on/off switch" but an application of the [[Graham v. Connor]] objective-reasonableness standard; it is routinely applied in vehicular-pursuit excessive-force cases.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*

## Sources
- *Scott v. Harris*, 550 U.S. 372 (2007) — https://www.courtlistener.com/opinion/145738/scott-v-harris/ — pinpoints (S. Ct. reporter): 1777, 1779.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1623ae1e16511a50", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "550 U.S. 372 (2007)", "court": "U.S. Supreme Court", "neutral_cite": "2007 U.S. LEXIS 4748", "official_citation_present": true, "parallel_cite": "127 S. Ct. 1769; 167 L. Ed. 2d 686", "title": "Scott v. Harris", "year": "2007"}}
{"assertion_id": "01187c9d6f6cc3db", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "*Garner* is not a rigid separate test but 'simply an application' of *Graham* reasonableness — no 'magical on/off switch'; ramming a fleeing motorist who endangered the public was reasonable.", "title": "Scott v. Harris"}}
{"assertion_id": "36d98911b0fc70c8", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Progeny / Refinement", "title": "Scott v. Harris"}}
{"assertion_id": "01da155f2c63822e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2007-04-30", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Scott v. Harris", "field_i_validity": "good_law", "scope_note": "Reads Tennessee v. Garner as an application of Graham reasonableness, not a rigid test.", "title": "Scott v. Harris", "varies_by_point": "false"}}
{"assertion_id": "ebc1d5838bf94244", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Scott v. Harris"}}
```

### lake record — Scott v. Harris

```json
{
  "schema_version": "s2.v1",
  "record_id": "Scott v. Harris",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Scott v. Harris",
    "case_name_short": "Scott",
    "case_name_full": "Scott v. Harris",
    "input_case_name": "Scott v. Harris",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2007-04-30",
    "year": 2007,
    "docket": "05-1631",
    "cluster_id": 145738,
    "lead_opinion_id": 145738,
    "sibling_ids": [
      145738,
      9435077,
      9435078,
      9435079,
      9435080
    ],
    "absolute_url": "/opinion/145738/scott-v-harris/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "550 U.S. 372",
      "volume": "550",
      "reporter": "U.S.",
      "page": "372",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "127 S. Ct. 1769",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "167 L. Ed. 2d 686",
        "volume": "167",
        "reporter": "L. Ed. 2d",
        "page": "686",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2007 U.S. LEXIS 4748",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "4748",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "550 U.S. 372",
        "volume": "550",
        "reporter": "U.S.",
        "page": "372",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 S. Ct. 1769",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "167 L. Ed. 2d 686",
        "volume": "167",
        "reporter": "L. Ed. 2d",
        "page": "686",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2007 U.S. LEXIS 4748",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "4748",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "550 U.S. 372",
    "official_selection": {
      "court_class": "scotus",
      "selected": "550 U.S. 372",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1777",
      "page": null,
      "quote": "--- # Scott v. Harris *550 U.S. 372 (2007)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Deputy Timothy Scott ended a high-speed chase of Victor Harris\u2014who had fled a traffic stop and reached roughly 85 m.p.h. on two-lane roads\u2014by ramming the rear of Harris's car, causing a crash that left Harris a quadriplegic. A police video captured the pursuit. Harris sued under 42 U.S.C. \u00a7 1983 for excessive force; the lower courts denied Scott qualified immunity. ## Issue Whether an officer's ramming of a fleeing motorist's vehicle to terminate a dangerous high-speed chase is an unreasonable seizure under the Fourth Amendment, and whether the deadly-force preconditions of *Tennessee v. Garner* rigidly control that question. ## Rule The reasonableness of force is judged under the Fourth Amendment's objective-reasonableness standard, and *Garner* does not impose rigid preconditions.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1779",
      "page": null,
      "quote": "was simply an application of the Fourth Amendment's 'reasonableness' test ... to the use of a particular type of force in a particular situation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2007-04-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Scott v. Harris",
    "varies_by_point": false,
    "scope_note": "Reads Tennessee v. Garner as an application of Graham reasonableness, not a rigid test.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullenix v. Luna",
          "cluster_id": 3153112,
          "cite": [
            "577 U.S. 7",
            "136 S. Ct. 305",
            "193 L. Ed. 2d 255",
            "2015 U.S. LEXIS 7160",
            "84 U.S.L.W. 4003",
            "25 Fla. L. Weekly Fed. S 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ricci v. DeStefano",
          "cluster_id": 145848,
          "cite": [
            "174 L. Ed. 2d 490",
            "129 S. Ct. 2658",
            "557 U.S. 557",
            "2009 U.S. LEXIS 4945"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iko v. Shreve",
          "cluster_id": 1026358,
          "cite": [
            "535 F.3d 225",
            "2008 U.S. App. LEXIS 16607",
            "2008 WL 3018444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torgerson v. City of Rochester",
          "cluster_id": 217808,
          "cite": [
            "643 F.3d 1031",
            "2011 U.S. App. LEXIS 10938",
            "94 Empl. Prac. Dec. (CCH) 44,199",
            "112 Fair Empl. Prac. Cas. (BNA) 613",
            "2011 WL 2135636"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City and County of San Francisco v. Sheehan",
          "cluster_id": 2801435,
          "cite": [
            "575 U.S. 600",
            "135 S. Ct. 1765",
            "191 L. Ed. 2d 856",
            "2015 U.S. LEXIS 3200",
            "83 U.S.L.W. 4303",
            "25 Fla. L. Weekly Fed. S 254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillips v. Roane County, Tenn.",
          "cluster_id": 1198739,
          "cite": [
            "534 F.3d 531",
            "2008 U.S. App. LEXIS 15777",
            "2008 WL 2852898"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jacqueline Lewis v. City of Union City, Georgia",
          "cluster_id": 4602166,
          "cite": [
            "918 F.3d 1213"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Antonio Pearson v. Prison Health Service",
          "cluster_id": 4373439,
          "cite": [
            "850 F.3d 526",
            "102 Fed. R. Serv. 1123",
            "2017 WL 892371",
            "2017 U.S. App. LEXIS 4003"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pahls v. Thomas",
          "cluster_id": 875382,
          "cite": [
            "718 F.3d 1210",
            "2013 WL 2398559"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iqbal v. Hasty",
          "cluster_id": 2716,
          "cite": [
            "490 F.3d 143"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tracey White v. Thomas Jackson",
          "cluster_id": 4414209,
          "cite": [
            "865 F.3d 1064",
            "2017 WL 3254496",
            "2017 U.S. App. LEXIS 13926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Victoria Zetwick v. County of Yolo",
          "cluster_id": 4370725,
          "cite": [
            "850 F.3d 436",
            "2017 WL 710476",
            "2017 U.S. App. LEXIS 3260",
            "101 Empl. Prac. Dec. (CCH) 45,744",
            "129 Fair Empl. Prac. Cas. (BNA) 1657"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shawn Eagan v. Michael Dempsey",
          "cluster_id": 4855039,
          "cite": [
            "987 F.3d 667"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maldonado v. Fontanes",
          "cluster_id": 203857,
          "cite": [
            "568 F.3d 263",
            "2009 U.S. App. LEXIS 12716",
            "2009 WL 1547737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Variety Stores, Inc. v. Wal-Mart Stores, Inc.",
          "cluster_id": 4492318,
          "cite": [
            "888 F.3d 651"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lazy Y Ranch Ltd. v. Behrens",
          "cluster_id": 1361176,
          "cite": [
            "546 F.3d 580",
            "2008 U.S. App. LEXIS 20335",
            "2008 WL 4368216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Scott v. Harris:lane2_top_cited"
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
        "journal_ref": "Scott v. Harris:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145738 OR 9435077 OR 9435078 OR 9435079 OR 9435080) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzEwNDYwODAwMDAwJnM9OTQ4NDM2NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145738+OR+9435077+OR+9435078+OR+9435079+OR+9435080%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145738 OR 9435077 OR 9435078 OR 9435079 OR 9435080)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MzQmcz00NDU5MjIyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145738+OR+9435077+OR+9435078+OR+9435079+OR+9435080%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145738 OR 9435077 OR 9435078 OR 9435079 OR 9435080)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzM5OTIzMjAwMDAwJnM9MTAzMzU1MjMmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145738+OR+9435077+OR+9435078+OR+9435079+OR+9435080%29&type=o",
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
    "complete_query": "cites:(145738 OR 9435077 OR 9435078 OR 9435079 OR 9435080)",
    "indexed_citing_opinions": 2857,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145738,
        "count": 2154,
        "count_source": "search"
      },
      {
        "opinion_id": 9435077,
        "count": 721,
        "count_source": "search"
      },
      {
        "opinion_id": 9435078,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435079,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435080,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 13453,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/scott-v-harris.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1MTEwMzYmcz0xMDY2MTczMyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145738+OR+9435077+OR+9435078+OR+9435079+OR+9435080%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145738,
        "cited_id": 76270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 104029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 106395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 111481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 111620,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 111719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 112643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 117898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 136067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 582751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 611060,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145738,
        "cited_id": 791266,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LCU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T18:44:50Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:45:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:45:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:47:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:45:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Scott v. Harris

```
(Slip Opinion)              OCTOBER TERM, 2006                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                             SCOTT v. HARRIS

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

   No. 05–1631.       Argued February 26, 2007—Decided April 30, 2007
Deputy Timothy Scott, petitioner here, terminated a high-speed pursuit
 of respondent’s car by applying his push bumper to the rear of the
 vehicle, causing it to leave the road and crash. Respondent was ren
 dered quadriplegic. He filed suit under 42 U. S. C. §1983 alleging, in
 ter alia, the use of excessive force resulting in an unreasonable sei
 zure under the Fourth Amendment. The District Court denied
 Scott’s summary judgment motion, which was based on qualified
 immunity. The Eleventh Circuit affirmed on interlocutory appeal,
 concluding, inter alia, that Scott’s actions could constitute “deadly
 force” under Tennessee v. Garner, 471 U. S. 1; that the use of such
 force in this context would violate respondent’s constitutional right to
 be free from excessive force during a seizure; and that a reasonable
 jury could so find.
Held: Because the car chase respondent initiated posed a substantial
 and immediate risk of serious physical injury to others, Scott’s at
 tempt to terminate the chase by forcing respondent off the road was
 reasonable, and Scott is entitled to summary judgment. Pp. 3–13.
    (a) Qualified immunity requires resolution of a “threshold question:
 Taken in the light most favorable to the party asserting the injury, do
 the facts alleged show the officer’s conduct violated a constitutional
 right?” Saucier v. Katz, 533 U. S. 194, 201. Pp. 3–4.
    (b) The record in this case includes a videotape capturing the
 events in question. Where, as here, the record blatantly contradicts
 the plaintiff’s version of events so that no reasonable jury could be
 lieve it, a court should not adopt that version of the facts for purposes
 of ruling on a summary judgment motion. Pp. 5–8.
    (c) Viewing the facts in the light depicted by the videotape, it is
 clear that Deputy Scott did not violate the Fourth Amendment.
2                           SCOTT v. HARRIS

                                  Syllabus

    Pp. 8–13.
         (i) Garner did not establish a magical on/off switch that triggers
    rigid preconditions whenever an officer’s actions constitute “deadly
    force.” The Court there simply applied the Fourth Amendment’s
    “reasonableness” test to the use of a particular type of force in a par
    ticular situation. That case has scant applicability to this one, which
    has vastly different facts. Whether or not Scott’s actions constituted
    “deadly force,” what matters is whether those actions were reason
    able. Pp. 8–10.
         (ii) In determining a seizure’s reasonableness, the Court balances
    the nature and quality of the intrusion on the individual’s Fourth
    Amendment interests against the importance of the governmental in
    terests allegedly justifying the intrusion. United States v. Place, 462
    U. S. 696, 703. In weighing the high likelihood of serious injury or
    death to respondent that Scott’s actions posed against the actual and
    imminent threat that respondent posed to the lives of others, the
    Court takes account of the number of lives at risk and the relative
    culpability of the parties involved. Respondent intentionally placed
    himself and the public in danger by unlawfully engaging in reckless,
    high-speed flight; those who might have been harmed had Scott not
    forced respondent off the road were entirely innocent. The Court
    concludes that it was reasonable for Scott to take the action he did.
    It rejects respondent’s argument that safety could have been assured
    if the police simply ceased their pursuit. The Court rules that a po
    lice officer’s attempt to terminate a dangerous high-speed car chase
    that threatens the lives of innocent bystanders does not violate the
    Fourth Amendment, even when it places the fleeing motorist at risk
    of serious injury or death. Pp. 10–13.
433 F. 3d 807, reversed.

  SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, SOUTER, THOMAS, GINSBURG, BREYER, and ALITO,
JJ., joined. GINSBURG, J., and BREYER, J., filed concurring opinions.
STEVENS, J., filed a dissenting opinion.
                        Cite as: 550 U. S. ____ (2007)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 05–1631
                                   _________________


 TIMOTHY SCOTT, PETITIONER v. VICTOR HARRIS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                                 [April 30, 2007] 


   JUSTICE SCALIA delivered the opinion of the Court.
   We consider whether a law enforcement official can,
consistent with the Fourth Amendment, attempt to stop a
fleeing motorist from continuing his public-endangering
flight by ramming the motorist’s car from behind. Put
another way: Can an officer take actions that place a
fleeing motorist at risk of serious injury or death in order
to stop the motorist’s flight from endangering the lives of
innocent bystanders?
                              I
   In March 2001, a Georgia county deputy clocked re
spondent’s vehicle traveling at 73 miles per hour on a road
with a 55-mile-per-hour speed limit. The deputy activated
his blue flashing lights indicating that respondent should
pull over. Instead, respondent sped away, initiating a
chase down what is in most portions a two-lane road, at
speeds exceeding 85 miles per hour. The deputy radioed
his dispatch to report that he was pursuing a fleeing
vehicle, and broadcast its license plate number. Peti
tioner, Deputy Timothy Scott, heard the radio communica
tion and joined the pursuit along with other officers. In
the midst of the chase, respondent pulled into the parking
2                        SCOTT v. HARRIS

                        Opinion of the Court

lot of a shopping center and was nearly boxed in by the
various police vehicles. Respondent evaded the trap by
making a sharp turn, colliding with Scott’s police car,
exiting the parking lot, and speeding off once again down a
two-lane highway.
   Following respondent’s shopping center maneuvering,
which resulted in slight damage to Scott’s police car, Scott
took over as the lead pursuit vehicle. Six minutes and
nearly 10 miles after the chase had begun, Scott decided to
attempt to terminate the episode by employing a “Preci
sion Intervention Technique (‘PIT’) maneuver, which
causes the fleeing vehicle to spin to a stop.” Brief for
Petitioner 4. Having radioed his supervisor for permis
sion, Scott was told to “ ‘[g]o ahead and take him out.’ ”
Harris v. Coweta County, 433 F. 3d 807, 811 (CA11 2005).
Instead, Scott applied his push bumper to the rear of
respondent’s vehicle.1 As a result, respondent lost control
of his vehicle, which left the roadway, ran down an em
bankment, overturned, and crashed. Respondent was
badly injured and was rendered a quadriplegic.
   Respondent filed suit against Deputy Scott and others
under Rev. Stat. §1979, 42 U. S. C. §1983, alleging, inter
alia, a violation of his federal constitutional rights, viz.
use of excessive force resulting in an unreasonable seizure
under the Fourth Amendment. In response, Scott filed a
motion for summary judgment based on an assertion of
qualified immunity. The District Court denied the motion,
finding that “there are material issues of fact on which the
issue of qualified immunity turns which present sufficient
disagreement to require submission to a jury.” Harris v.
——————
  1 Scott says he decided not to employ the PIT maneuver because he

was “concerned that the vehicles were moving too quickly to safely
execute the maneuver.” Brief for Petitioner 4. Respondent agrees that
the PIT maneuver could not have been safely employed. See Brief for
Respondent 9. It is irrelevant to our analysis whether Scott had
permission to take the precise actions he took.
                      Cite as: 550 U. S. ____ (2007)                     3

                          Opinion of the Court

Coweta County, No. 3:01–CV–148–WBH (ND Ga., Sept.
23, 2003), App. to Pet. for Cert. 41a–42a. On interlocutory
appeal,2 the United States Court of Appeals for the Elev
enth Circuit affirmed the District Court’s decision to allow
respondent’s Fourth Amendment claim against Scott to
proceed to trial.3 Taking respondent’s view of the facts as
given, the Court of Appeals concluded that Scott’s actions
could constitute “deadly force” under Tennessee v. Garner,
471 U. S. 1 (1985), and that the use of such force in this
context “would violate [respondent’s] constitutional right
to be free from excessive force during a seizure. Accord
ingly, a reasonable jury could find that Scott violated
[respondent’s] Fourth Amendment rights.” 433 F. 3d, at
816. The Court of Appeals further concluded that “the law
as it existed [at the time of the incident], was sufficiently
clear to give reasonable law enforcement officers ‘fair
notice’ that ramming a vehicle under these circumstances
was unlawful.” Id., at 817. The Court of Appeals thus
concluded that Scott was not entitled to qualified immu
nity. We granted certiorari, 549 U. S. __ (2006), and now
reverse.
                              II
   In resolving questions of qualified immunity, courts are
required to resolve a “threshold question: Taken in the
light most favorable to the party asserting the injury, do
——————
  2 Qualified immunity is “an immunity from suit rather than a mere
defense to liability; and like an absolute immunity, it is effectively lost
if a case is erroneously permitted to go to trial.” Mitchell v. Forsyth,
472 U. S. 511, 526 (1985). Thus, we have held that an order denying
qualified immunity is immediately appealable even though it is inter
locutory; otherwise, it would be “effectively unreviewable.” Id., at 527.
Further, “we repeatedly have stressed the importance of resolving
immunity questions at the earliest possible stage in litigation.” Hunter
v. Bryant, 502 U. S. 224, 227 (1991) (per curiam).
   3 None of the other claims respondent brought against Scott or any

other party are before this Court.
4                          SCOTT v. HARRIS

                          Opinion of the Court

the facts alleged show the officer’s conduct violated a
constitutional right? This must be the initial inquiry.”
Saucier v. Katz, 533 U. S. 194, 201 (2001). If, and only if,
the court finds a violation of a constitutional right, “the
next, sequential step is to ask whether the right was
clearly established . . . in light of the specific context of the
case.” Ibid. Although this ordering contradicts “[o]ur
policy of avoiding unnecessary adjudication of constitu
tional issues,” United States v. Treasury Employees, 513
U. S. 454, 478 (1995) (citing Ashwander v. TVA, 297 U. S.
288, 346–347 (1936) (Brandeis, J., concurring)), we have
said that such a departure from practice is “necessary to
set forth principles which will become the basis for a
[future] holding that a right is clearly established.” Sau
cier, supra, at 201.4 We therefore turn to the threshold
inquiry: whether Deputy Scott’s actions violated the
Fourth Amendment.


——————
   4 Prior to this Court’s announcement of Saucier’s “rigid ‘order of bat

tle,’ ” Brosseau v. Haugen, 543 U. S. 194, 201–202 (2004) (BREYER, J.,
concurring), we had described this order of inquiry as the “better
approach,” County of Sacramento v. Lewis, 523 U. S. 833, 841, n. 5
(1998), though not one that was required in all cases. See id., at 858–
859 (BREYER, J., concurring); id., at 859 (STEVENS, J., concurring in
judgment). There has been doubt expressed regarding the wisdom of
Saucier’s decision to make the threshold inquiry mandatory, especially
in cases where the constitutional question is relatively difficult and the
qualified immunity question relatively straightforward. See, e.g.,
Brosseau, supra, at 201 (BREYER, J., joined by SCALIA and GINSBURG,
JJ., concurring); Bunting v. Mellen, 541 U. S. 1019 (2004) (STEVENS, J.,
joined by GINSBURG and BREYER, JJ., respecting denial of certiorari);
id., at 1025 (SCALIA, J., joined by Rehnquist, C.J., dissenting). See also
Lyons v. Xenia, 417 F. 3d 565, 580–584 (CA6 2005) (Sutton, J., concur
ring). We need not address the wisdom of Saucier in this case, how
ever, because the constitutional question with which we are presented
is, as discussed in Part III–B, infra, easily decided. Deciding that
question first is thus the “better approach,” Lewis, supra, at 841, n. 5,
regardless of whether it is required.
                   Cite as: 550 U. S. ____ (2007)                 5

                        Opinion of the Court

                               III 

                                A

  The first step in assessing the constitutionality of Scott’s
actions is to determine the relevant facts. As this case
was decided on summary judgment, there have not yet
been factual findings by a judge or jury, and respondent’s
version of events (unsurprisingly) differs substantially
from Scott’s version. When things are in such a posture,
courts are required to view the facts and draw reasonable
inferences “in the light most favorable to the party oppos
ing the [summary judgment] motion.” United States v.
Diebold, Inc., 369 U. S. 654, 655 (1962) (per curiam);
Saucier, supra, at 201. In qualified immunity cases, this
usually means adopting (as the Court of Appeals did here)
the plaintiff’s version of the facts.
  There is, however, an added wrinkle in this case: exis
tence in the record of a videotape capturing the events in
question. There are no allegations or indications that this
videotape was doctored or altered in any way, nor any
contention that what it depicts differs from what actually
happened. The videotape quite clearly contradicts the
version of the story told by respondent and adopted by the
Court of Appeals.5 For example, the Court of Appeals
adopted respondent’s assertions that, during the chase,
“there was little, if any, actual threat to pedestrians or
other motorists, as the roads were mostly empty and
[respondent] remained in control of his vehicle.” 433 F. 3d,
at 815. Indeed, reading the lower court’s opinion, one gets
——————
  5 JUSTICE  STEVENS suggests that our reaction to the videotape is
somehow idiosyncratic, and seems to believe we are misrepresenting
its contents. See post, at 4 (dissenting opinion) (“In sum, the
factual statements by the Court of Appeals quoted by the
Court . . . were entirely accurate”). We are happy to allow the
videotape to speak for itself. See Record 36, Exh. A, available at
http://www.supremecourtus.gov/opinions/video/scott_v_harris.rmvb and
in Clerk of Court’s case file.
6                         SCOTT v. HARRIS

                         Opinion of the Court

the impression that respondent, rather than fleeing from
police, was attempting to pass his driving test:
       “[T]aking the facts from the non-movant’s viewpoint,
       [respondent] remained in control of his vehicle, slowed
       for turns and intersections, and typically used his in
       dicators for turns. He did not run any motorists off
       the road. Nor was he a threat to pedestrians in the
       shopping center parking lot, which was free from pe
       destrian and vehicular traffic as the center was closed.
       Significantly, by the time the parties were back on the
       highway and Scott rammed [respondent], the motor-
       way had been cleared of motorists and pedestrians al
       legedly because of police blockades of the nearby inter
       sections.” Id., at 815–816 (citations omitted).
  The videotape tells quite a different story. There we see
respondent’s vehicle racing down narrow, two-lane roads
in the dead of night at speeds that are shockingly fast. We
see it swerve around more than a dozen other cars, cross
the double-yellow line, and force cars traveling in both
directions to their respective shoulders to avoid being hit.6
We see it run multiple red lights and travel for consider
able periods of time in the occasional center left-turn-only
lane, chased by numerous police cars forced to engage in
——————
    6 JUSTICE
            STEVENS hypothesizes that these cars “had already pulled to
the side of the road or were driving along the shoulder because they
heard the police sirens or saw the flashing lights,” so that “[a] jury
could certainly conclude that those motorists were exposed to no
greater risk than persons who take the same action in response to a
speeding ambulance.” Post, at 3. It is not our experience that ambu
lances and fire engines careen down two-lane roads at 85-plus miles per
hour, with an unmarked scout car out in front of them. The risk they
pose to the public is vastly less than what respondent created here.
But even if that were not so, it would in no way lead to the conclusion
that it was unreasonable to eliminate the threat to life that respondent
posed. Society accepts the risk of speeding ambulances and fire engines
in order to save life and property; it need not (and assuredly does not)
accept a similar risk posed by a reckless motorist fleeing the police.
                     Cite as: 550 U. S. ____ (2007)                   7

                         Opinion of the Court

the same hazardous maneuvers just to keep up. Far from
being the cautious and controlled driver the lower court
depicts, what we see on the video more closely resembles a
Hollywood-style car chase of the most frightening sort,
placing police officers and innocent bystanders alike at
great risk of serious injury.7
   At the summary judgment stage, facts must be viewed in
the light most favorable to the nonmoving party only if
there is a “genuine” dispute as to those facts. Fed. Rule
Civ. Proc. 56(c). As we have emphasized, “[w]hen the
moving party has carried its burden under Rule 56(c), its
opponent must do more than simply show that there is
some metaphysical doubt as to the material facts. . . .
Where the record taken as a whole could not lead a ra
tional trier of fact to find for the nonmoving party, there is
no ‘genuine issue for trial.’ ” Matsushita Elec. Industrial
Co. v. Zenith Radio Corp., 475 U. S. 574, 586–587 (1986)
(footnote omitted). “[T]he mere existence of some alleged
factual dispute between the parties will not defeat an
otherwise properly supported motion for summary judg
ment; the requirement is that there be no genuine issue of
material fact.” Anderson v. Liberty Lobby, Inc., 477 U. S.
242, 247–248 (1986). When opposing parties tell two
different stories, one of which is blatantly contradicted by
the record, so that no reasonable jury could believe it, a
court should not adopt that version of the facts for pur
poses of ruling on a motion for summary judgment.
   That was the case here with regard to the factual issue
whether respondent was driving in such fashion as to
endanger human life. Respondent’s version of events is so
utterly discredited by the record that no reasonable jury
——————
  7 This is not to say that each and every factual statement made by the

Court of Appeals is inaccurate. For example, the videotape validates
the court’s statement that when Scott rammed respondent’s vehicle it
was not threatening any other vehicles or pedestrians. (Undoubtedly
Scott waited for the road to be clear before executing his maneuver.)
8                         SCOTT v. HARRIS

                         Opinion of the Court

could have believed him. The Court of Appeals should not
have relied on such visible fiction; it should have viewed
the facts in the light depicted by the videotape.
                                 B
  Judging the matter on that basis, we think it is quite
clear that Deputy Scott did not violate the Fourth
Amendment. Scott does not contest that his decision to
terminate the car chase by ramming his bumper into
respondent’s vehicle constituted a “seizure.” “[A] Fourth
Amendment seizure [occurs] . . . when there is a govern
mental termination of freedom of movement through
means intentionally applied.” Brower v. County of Inyo,
489 U. S. 593, 596–597 (1989) (emphasis deleted). See
also id., at 597 (“If . . . the police cruiser had pulled along
side the fleeing car and sideswiped it, producing the crash,
then the termination of the suspect’s freedom of movement
would have been a seizure”). It is also conceded, by both
sides, that a claim of “excessive force in the course of
making [a] . . .‘seizure’ of [the] person . . . [is] properly
analyzed under the Fourth Amendment’s ‘objective rea
sonableness’ standard.” Graham v. Connor, 490 U. S. 386,
388 (1989). The question we need to answer is whether
Scott’s actions were objectively reasonable.8
                            1
 Respondent urges us to analyze this case as we analyzed
Garner, 471 U. S. 1. See Brief for Respondent 16–29. We
——————
  8 JUSTICE STEVENS incorrectly declares this to be “a question of fact

best reserved for a jury,” and complains we are “usurp[ing] the jury’s
factfinding function.” Post, at 7. At the summary judgment stage,
however, once we have determined the relevant set of facts and drawn
all inferences in favor of the nonmoving party to the extent supportable
by the record, see Part III–A, supra, the reasonableness of Scott’s
actions—or, in JUSTICE STEVENS’ parlance, “[w]hether [respondent’s]
actions have risen to a level warranting deadly force,” post, at 7—is a
pure question of law.
                      Cite as: 550 U. S. ____ (2007)                     9

                          Opinion of the Court

must first decide, he says, whether the actions Scott took
constituted “deadly force.” (He defines “deadly force” as
“any use of force which creates a substantial likelihood of
causing death or serious bodily injury,” id., at 19.) If so,
respondent claims that Garner prescribes certain precon
ditions that must be met before Scott’s actions can survive
Fourth Amendment scrutiny: (1) The suspect must have
posed an immediate threat of serious physical harm to the
officer or others; (2) deadly force must have been neces
sary to prevent escape;9 and (3) where feasible, the officer
must have given the suspect some warning. See Brief for
Respondent 17–18 (citing Garner, supra, at 9–12). Since
these Garner preconditions for using deadly force were not
met in this case, Scott’s actions were per se unreasonable.
  Respondent’s argument falters at its first step; Garner
did not establish a magical on/off switch that triggers rigid
preconditions whenever an officer’s actions constitute
“deadly force.” Garner was simply an application of the
Fourth Amendment’s “reasonableness” test, Graham,
supra, at 388, to the use of a particular type of force in a
particular situation. Garner held that it was unreason
able to kill a “young, slight, and unarmed” burglary sus
——————
   9 Respondent, like the Court of Appeals, defines this second precondi

tion as “ ‘necessary to prevent escape,’ ” Brief for Respondent 17; Harris
v. Coweta County, 433 F. 3d 807, 813 (CA11 2005), quoting Garner, 471
U. S., at 11. But that quote from Garner is taken out of context. The
necessity described in Garner was, in fact, the need to prevent “serious
physical harm, either to the officer or to others.” Ibid. By way of
example only, Garner hypothesized that deadly force may be used “if
necessary to prevent escape” when the suspect is known to have “com
mitted a crime involving the infliction or threatened infliction of serious
physical harm,” ibid., so that his mere being at large poses an inherent
danger to society. Respondent did not pose that type of inherent threat
to society, since (prior to the car chase) he had committed only a minor
traffic offense and, as far as the police were aware, had no prior crimi
nal record. But in this case, unlike in Garner, it was respondent’s flight
itself (by means of a speeding automobile) that posed the threat of
“serious physical harm . . . to others.” Ibid.
10                    SCOTT v. HARRIS

                     Opinion of the Court

pect, 471 U. S., at 21, by shooting him “in the back of the
head” while he was running away on foot, id., at 4, and
when the officer “could not reasonably have believed that
[the suspect] . . . posed any threat,” and “never attempted
to justify his actions on any basis other than the need to
prevent an escape,” id., at 21. Whatever Garner said
about the factors that might have justified shooting the
suspect in that case, such “preconditions” have scant
applicability to this case, which has vastly different facts.
“Garner had nothing to do with one car striking another or
even with car chases in general . . . . A police car’s bump
ing a fleeing car is, in fact, not much like a policeman’s
shooting a gun so as to hit a person.” Adams v. St. Lucie
County Sheriff’s Dept., 962 F. 2d 1563, 1577 (CA11 1992)
(Edmondson, J., dissenting), adopted by 998 F. 2d 923
(CA11 1993) (en banc) (per curiam). Nor is the threat
posed by the flight on foot of an unarmed suspect even
remotely comparable to the extreme danger to human life
posed by respondent in this case. Although respondent’s
attempt to craft an easy-to-apply legal test in the Fourth
Amendment context is admirable, in the end we must still
slosh our way through the factbound morass of “reason
ableness.” Whether or not Scott’s actions constituted
application of “deadly force,” all that matters is whether
Scott’s actions were reasonable.
                              2
  In determining the reasonableness of the manner in
which a seizure is effected, “[w]e must balance the nature
and quality of the intrusion on the individual’s Fourth
Amendment interests against the importance of the gov
ernmental interests alleged to justify the intrusion.”
United States v. Place, 462 U. S. 696, 703 (1983). Scott
defends his actions by pointing to the paramount govern
mental interest in ensuring public safety, and respondent
nowhere suggests this was not the purpose motivating
                     Cite as: 550 U. S. ____ (2007)                  11

                         Opinion of the Court

Scott’s behavior. Thus, in judging whether Scott’s actions
were reasonable, we must consider the risk of bodily harm
that Scott’s actions posed to respondent in light of the
threat to the public that Scott was trying to eliminate.
Although there is no obvious way to quantify the risks on
either side, it is clear from the videotape that respondent
posed an actual and imminent threat to the lives of any
pedestrians who might have been present, to other civilian
motorists, and to the officers involved in the chase. See
Part III–A, supra. It is equally clear that Scott’s actions
posed a high likelihood of serious injury or death to re
spondent—though not the near certainty of death posed
by, say, shooting a fleeing felon in the back of the head,
see Garner, supra, at 4, or pulling alongside a fleeing
motorist’s car and shooting the motorist, cf. Vaughan v.
Cox, 343 F. 3d 1323, 1326–1327 (CA11 2003). So how does
a court go about weighing the perhaps lesser probability of
injuring or killing numerous bystanders against the per
haps larger probability of injuring or killing a single per
son? We think it appropriate in this process to take into
account not only the number of lives at risk, but also their
relative culpability. It was respondent, after all, who
intentionally placed himself and the public in danger by
unlawfully engaging in the reckless, high-speed flight that
ultimately produced the choice between two evils that
Scott confronted. Multiple police cars, with blue lights
flashing and sirens blaring, had been chasing respondent
for nearly 10 miles, but he ignored their warning to stop.
By contrast, those who might have been harmed had Scott
not taken the action he did were entirely innocent. We
have little difficulty in concluding it was reasonable for
Scott to take the action that he did.10
——————
  10 The Court of Appeals cites Brower v. County of Inyo, 489 U. S. 593,

595 (1989), for its refusal to “countenance the argument that by con
tinuing to flee, a suspect absolves a pursuing police officer of any
12                         SCOTT v. HARRIS

                           Opinion of the Court

   But wait, says respondent: Couldn’t the innocent public
equally have been protected, and the tragic accident en
tirely avoided, if the police had simply ceased their pur
suit? We think the police need not have taken that chance
and hoped for the best. Whereas Scott’s action—ramming
respondent off the road—was certain to eliminate the risk
that respondent posed to the public, ceasing pursuit was
not. First of all, there would have been no way to convey
convincingly to respondent that the chase was off, and
that he was free to go. Had respondent looked in his rear
view mirror and seen the police cars deactivate their
flashing lights and turn around, he would have had no
idea whether they were truly letting him get away, or
simply devising a new strategy for capture. Perhaps the
police knew a shortcut he didn’t know, and would reap
pear down the road to intercept him; or perhaps they were
setting up a roadblock in his path. Cf. Brower, 489 U. S.,
at 594. Given such uncertainty, respondent might have
been just as likely to respond by continuing to drive reck
lessly as by slowing down and wiping his brow.11
   Second, we are loath to lay down a rule requiring the
——————
possible liability for all ensuing actions during the chase,” 433 F. 3d, at
816. The only question in Brower was whether a police roadblock
constituted a seizure under the Fourth Amendment. In deciding that
question, the relative culpability of the parties is, of course, irrelevant;
a seizure occurs whenever the police are “responsib[le] for the termina
tion of [a person’s] movement,” 433 F. 3d, at 816, regardless of the
reason for the termination. Culpability is relevant, however, to the
reasonableness of the seizure—to whether preventing possible harm to
the innocent justifies exposing to possible harm the person threatening
them.
   11 Contrary to JUSTICE STEVENS’ assertions, we do not “assum[e] that

dangers caused by flight from a police pursuit will continue after the
pursuit ends,” post, at 6, nor do we make any “factual assumptions,”
post, at 5, with respect to what would have happened if the police had
gone home. We simply point out the uncertainties regarding what
would have happened, in response to respondent’s factual assumption
that the high-speed flight would have ended.
                 Cite as: 550 U. S. ____ (2007)           13

                     Opinion of the Court

police to allow fleeing suspects to get away whenever they
drive so recklessly that they put other people’s lives in
danger. It is obvious the perverse incentives such a rule
would create: Every fleeing motorist would know that
escape is within his grasp, if only he accelerates to 90
miles per hour, crosses the double-yellow line a few times,
and runs a few red lights. The Constitution assuredly
does not impose this invitation to impunity-earned-by
recklessness. Instead, we lay down a more sensible rule: A
police officer’s attempt to terminate a dangerous high-
speed car chase that threatens the lives of innocent by
standers does not violate the Fourth Amendment, even
when it places the fleeing motorist at risk of serious injury
or death.
                        *    *    *
   The car chase that respondent initiated in this case
posed a substantial and immediate risk of serious physical
injury to others; no reasonable jury could conclude other
wise. Scott’s attempt to terminate the chase by forcing
respondent off the road was reasonable, and Scott is enti
tled to summary judgment. The Court of Appeals’ decision
to the contrary is reversed.
                                           It is so ordered.
                 Cite as: 550 U. S. ____ (2007)            1

                    GINSBURG, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                         No. 05–1631
                          _________________


 TIMOTHY SCOTT, PETITIONER v. VICTOR HARRIS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                        [April 30, 2007] 


   JUSTICE GINSBURG, concurring.
   I join the Court’s opinion and would underscore two
points. First, I do not read today’s decision as articulating
a mechanical, per se rule. Cf. post, at 3 (BREYER, J., con
curring). The inquiry described by the Court, ante, at 10–
13, is situation specific. Among relevant considerations:
Were the lives and well-being of others (motorists, pedes
trians, police officers) at risk? Was there a safer way,
given the time, place, and circumstances, to stop the flee
ing vehicle? “[A]dmirable” as “[an] attempt to craft an
easy-to-apply legal test in the Fourth Amendment context
[may be],” the Court explains, “in the end we must still
slosh our way through the factbound morass of ‘reason
ableness.’ ” Ante, at 10.
   Second, were this case suitable for resolution on quali
fied immunity grounds, without reaching the constitutional
question, JUSTICE BREYER’s discussion would be engaging.
See post, at 1–3 (urging the Court to overrule Saucier v.
Katz, 533 U. S. 194 (2001)). In joining the Court’s opinion,
however, JUSTICE BREYER apparently shares the view that,
in the appeal before us, the constitutional question war
rants an answer. The video footage of the car chase, he
agrees, demonstrates that the officer’s conduct did not
transgress Fourth Amendment limitations. See post, at 1.
Confronting Saucier, therefore, is properly reserved for
another day and case. See ante, at 4, n. 4.
                 Cite as: 550 U. S. ____ (2007)           1

                    BREYER, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 05–1631
                         _________________


 TIMOTHY SCOTT, PETITIONER v. VICTOR HARRIS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                        [April 30, 2007] 


   JUSTICE BREYER, concurring.
   I join the Court’s opinion with one suggestion and two
qualifications. Because watching the video footage of the
car chase made a difference to my own view of the case, I
suggest that the interested reader take advantage of the
link in the Court’s opinion, ante, at 5, n. 5, and watch it.
Having done so, I do not believe a reasonable jury could, in
this instance, find that Officer Timothy Scott (who joined
the chase late in the day and did not know the specific
reason why the respondent was being pursued) acted in
violation of the Constitution.
   Second, the video makes clear the highly fact-dependent
nature of this constitutional determination. And that fact-
dependency supports the argument that we should over
rule the requirement, announced in Saucier v. Katz, 533
U. S. 194 (2001), that lower courts must first decide the
“constitutional question” before they turn to the “qualified
immunity question.” See id., at 200 (“[T]he first inquiry
must be whether a constitutional right would have been
violated on the facts alleged”). Instead, lower courts
should be free to decide the two questions in whatever
order makes sense in the context of a particular case.
Although I do not object to our deciding the constitutional
question in this particular case, I believe that in order to
lift the burden from lower courts we can and should recon
sider Saucier’s requirement as well.
2                     SCOTT v. HARRIS

                     BREYER, J., concurring

   Sometimes (e.g., where a defendant is clearly entitled to
qualified immunity) Saucier’s fixed order-of-battle rule
wastes judicial resources in that it may require courts to
answer a difficult constitutional question unnecessarily.
Sometimes (e.g., where the defendant loses the constitu
tional question but wins on qualified immunity) that
order-of-battle rule may immunize an incorrect constitu
tional ruling from review. Sometimes, as here, the order-
of-battle rule will spawn constitutional rulings in areas of
law so fact dependent that the result will be confusion
rather than clarity. And frequently the order-of-battle
rule violates that older, wiser judicial counsel “not to pass
on questions of constitutionality . . . unless such adjudica
tion is unavoidable.”      Spector Motor Service, Inc. v.
McLaughlin, 323 U. S. 101, 105 (1944); see Ashwander v.
TVA, 297 U. S. 288, 347 (1936) (Brandeis, J., concurring)
(“The Court will not pass upon a constitutional question
although properly presented by the record, if there is also
present some other ground upon which the case may be
disposed of”). In a sharp departure from this counsel,
Saucier requires courts to embrace unnecessary constitu
tional questions not to avoid them.
   It is not surprising that commentators, judges, and, in
this case, 28 States in an amicus brief, have invited us to
reconsider Saucier’s requirement. See Leval, Judging
Under the Constitution: Dicta About Dicta, 81
N. Y. U. L. Rev. 1249, 1275 (2006) (calling the require
ment “a puzzling misadventure in constitutional dictum”);
Dirrane v. Brookline Police Dept., 315 F. 3d 65, 69–70
(CA1 2002) (referring to the requirement as “an uncom
fortable exercise” when “the answer whether there was a
violation may depend on a kaleidoscope of facts not yet
fully developed”); Lyons v. Xenia, 417 F. 3d 565, 580–584
(CA6 2005) (Sutton, J., concurring); Brief for State
of Illinois et al. as Amici Curiae. I would accept that
invitation.
                  Cite as: 550 U. S. ____ (2007)             3

                     BREYER, J., concurring

   While this Court should generally be reluctant to over
turn precedents, stare decisis concerns are at their weak
est here. See, e.g., Payne v. Tennessee, 501 U. S. 808, 828
(1991) (“Considerations in favor of stare decisis” are at
their weakest in cases “involving procedural and eviden
tiary rules”). The order-of-battle rule is relatively novel, it
primarily affects judges, and there has been little reliance
upon it.
   Third, I disagree with the Court insofar as it articulates
a per se rule. The majority states: “A police officer’s at
tempt to terminate a dangerous high-speed car chase that
threatens the lives of innocent bystanders does not violate
the Fourth Amendment, even when it places the fleeing
motorist at risk of serious injury or death.” Ante, at 13.
This statement is too absolute. As JUSTICE GINSBURG
points out, ante, at 1, whether a high-speed chase violates
the Fourth Amendment may well depend upon more cir
cumstances than the majority’s rule reflects. With these
qualifications, I join the Court’s opinion.
                 Cite as: 550 U. S. ____ (2007)            1

                    STEVENS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 05–1631
                         _________________


 TIMOTHY SCOTT, PETITIONER v. VICTOR HARRIS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                        [April 30, 2007] 


   JUSTICE STEVENS, dissenting.
   Today, the Court asks whether an officer may “take
actions that place a fleeing motorist at risk of serious
injury or death in order to stop the motorist’s flight from
endangering the lives of innocent bystanders.” Ante, at 1.
Depending on the circumstances, the answer may be an
obvious “yes,” an obvious “no,” or sufficiently doubtful that
the question of the reasonableness of the officer’s actions
should be decided by a jury, after a review of the degree of
danger and the alternatives available to the officer. A
high speed chase in a desert in Nevada is, after all, quite
different from one that travels through the heart of Las
Vegas.
     Relying on a de novo review of a videotape of a portion
of a nighttime chase on a lightly traveled road in Georgia
where no pedestrians or other “bystanders” were present,
buttressed by uninformed speculation about the possible
consequences of discontinuing the chase, eight of the
jurors on this Court reach a verdict that differs from the
views of the judges on both the District Court and the
Court of Appeals who are surely more familiar with the
hazards of driving on Georgia roads than we are. The
Court’s justification for this unprecedented departure from
our well-settled standard of review of factual determina
tions made by a district court and affirmed by a court of
appeals is based on its mistaken view that the Court of
2                         SCOTT v. HARRIS

                        STEVENS, J., dissenting

Appeals’ description of the facts was “blatantly contra
dicted by the record” and that respondent’s version of the
events was “so utterly discredited by the record that no
reasonable jury could have believed him.” Ante, at 7–8.
   Rather than supporting the conclusion that what we see
on the video “resembles a Hollywood-style car chase of the
most frightening sort,” ante, at 7,1 the tape actually con
firms, rather than contradicts, the lower courts’ appraisal
of the factual questions at issue. More important, it surely
does not provide a principled basis for depriving the re
spondent of his right to have a jury evaluate the question
whether the police officers’ decision to use deadly force to
bring the chase to an end was reasonable.
   Omitted from the Court’s description of the initial
speeding violation is the fact that respondent was on a
four-lane portion of Highway 34 when the officer clocked
his speed at 73 miles per hour and initiated the chase.2
More significant—and contrary to the Court’s assumption
that respondent’s vehicle “force[d] cars traveling in both
directions to their respective shoulders to avoid being hit”
ante, at 6—a fact unmentioned in the text of the opinion
explains why those cars pulled over prior to being passed
——————
  1 I can only conclude that my colleagues were unduly frightened by

two or three images on the tape that looked like bursts of lightning or
explosions, but were in fact merely the headlights of vehicles zooming
by in the opposite lane. Had they learned to drive when most high-
speed driving took place on two-lane roads rather than on superhigh
ways—when split-second judgments about the risk of passing a slow
poke in the face of oncoming traffic were routine—they might well have
reacted to the videotape more dispassionately.
  2 According to the District Court record, when respondent was clocked

at 73 miles per hour, the deputy who recorded his speed was sitting in
his patrol car on Highway 34 between Lora Smith Road and Sullivan
Road in Coweta County, Georgia. At that point, as well as at the point
at which Highway 34 intersects with Highway 154—where the deputy
caught up with respondent and the videotape begins—Highway 34 is a
four-lane road, consisting of two lanes in each direction with a wide
grass divider separating the flow of traffic.
                    Cite as: 550 U. S. ____ (2007)                   3

                        STEVENS, J., dissenting

by respondent. The sirens and flashing lights on the
police cars following respondent gave the same warning
that a speeding ambulance or fire engine would have
provided.3 The 13 cars that respondent passed on his side
of the road before entering the shopping center, and both
of the cars that he passed on the right after leaving the
center, no doubt had already pulled to the side of the road
or were driving along the shoulder because they heard the
police sirens or saw the flashing lights before respondent
or the police cruisers approached.4 A jury could certainly
conclude that those motorists were exposed to no greater
risk than persons who take the same action in response to
a speeding ambulance, and that their reactions were fully
consistent with the evidence that respondent, though
speeding, retained full control of his vehicle.
   The police sirens also minimized any risk that may have
arisen from running “multiple red lights,” ibid. In fact,
respondent and his pursuers went through only two inter
sections with stop lights and in both cases all other vehi
cles in sight were stationary, presumably because they
had been warned of the approaching speeders. Inciden
tally, the videos do show that the lights were red when the
police cars passed through them but, because the cameras
were farther away when respondent did so and it is diffi
cult to discern the color of the signal at that point, it is not
entirely clear that he ran either or both of the red lights.
In any event, the risk of harm to the stationary vehicles

——————
  3 While still on the four-lane portion of Highway 34, the deputy who

had clocked respondent’s speed turned on his blue light and siren in an
attempt to get respondent to pull over. It was when the deputy turned
on his blue light that the dash-mounted video camera was activated
and began to record the pursuit.
  4 Although perhaps understandable, because their volume on the

sound recording is low (possibly due to sound proofing in the officer’s
vehicle), the Court appears to minimize the significance of the sirens
audible throughout the tape recording of the pursuit.
4                     SCOTT v. HARRIS

                    STEVENS, J., dissenting

was minimized by the sirens, and there is no reason to
believe that respondent would have disobeyed the signals
if he were not being pursued.
   My colleagues on the jury saw respondent “swerve
around more than a dozen other cars,” and “force cars
traveling in both directions to their respective shoulders,”
ante, at 6, but they apparently discounted the possibility
that those cars were already out of the pursuit’s path as a
result of hearing the sirens. Even if that were not so,
passing a slower vehicle on a two-lane road always in
volves some degree of swerving and is not especially dan
gerous if there are no cars coming from the opposite direc
tion. At no point during the chase did respondent pull into
the opposite lane other than to pass a car in front of him;
he did the latter no more than five times and, on most of
those occasions, used his turn signal. On none of these
occasions was there a car traveling in the opposite direc
tion. In fact, at one point, when respondent found himself
behind a car in his own lane and there were cars traveling
in the other direction, he slowed and waited for the cars
traveling in the other direction to pass before overtaking
the car in front of him while using his turn signal to do so.
This is hardly the stuff of Hollywood. To the contrary, the
video does not reveal any incidents that could even be
remotely characterized as “close calls.”
   In sum, the factual statements by the Court of Appeals
quoted by the Court, ante, at 5–6, were entirely accurate.
That court did not describe respondent as a “cautious”
driver as my colleagues imply, ante, at 7, but it did cor
rectly conclude that there is no evidence that he ever lost
control of his vehicle. That court also correctly pointed out
that the incident in the shopping center parking lot did
not create any risk to pedestrians or other vehicles be
cause the chase occurred just before 11 p.m. on a weekday
night and the center was closed. It is apparent from the
record (including the videotape) that local police had
                     Cite as: 550 U. S. ____ (2007)                    5

                        STEVENS, J., dissenting

blocked off intersections to keep respondent from entering
residential neighborhoods and possibly endangering other
motorists. I would add that the videos also show that no
pedestrians, parked cars, sidewalks, or residences were
visible at any time during the chase. The only “innocent
bystanders” who were placed “at great risk of serious
injury,” ante, at 7, were the drivers who either pulled off
the road in response to the sirens or passed respondent in
the opposite direction when he was driving on his side of
the road.
   I recognize, of course, that even though respondent’s
original speeding violation on a four-lane highway was
rather ordinary, his refusal to stop and subsequent flight
was a serious offense that merited severe punishment. It
was not, however, a capital offense, or even an offense that
justified the use of deadly force rather than an abandon
ment of the chase. The Court’s concern about the “immi
nent threat to the lives of any pedestrians who might have
been present,” ante, at 11, while surely valid in an appro
priate case, should be discounted in a case involving a
nighttime chase in an area where no pedestrians were
present.
   What would have happened if the police had decided to
abandon the chase? We now know that they could have
apprehended respondent later because they had his li
cense plate number. Even if that were not true, and even
if he would have escaped any punishment at all, the use of
deadly force in this case was no more appropriate than the
use of a deadly weapon against a fleeing felon in Tennessee
v. Garner, 471 U. S. 1 (1985). In any event, any uncer
tainty about the result of abandoning the pursuit has not
prevented the Court from basing its conclusions on its own
factual assumptions.5 The Court attempts to avoid the
——————
  5 In noting that Scott’s action “was certain to eliminate the risk that

respondent posed to the public” while “ceasing pursuit was not,” the
6                          SCOTT v. HARRIS

                         STEVENS, J., dissenting

conclusion that deadly force was unnecessary by speculat
ing that if the officers had let him go, respondent might
have been “just as likely” to continue to drive recklessly as
to slow down and wipe his brow. Ante, at 12. That specu
lation is unconvincing as a matter of common sense and
improper as a matter of law. Our duty to view the evi
dence in the light most favorable to the nonmoving party
would foreclose such speculation if the Court had not used
its observation of the video as an excuse for replacing the
rule of law with its ad hoc judgment. There is no eviden
tiary basis for an assumption that dangers caused by
flight from a police pursuit will continue after the pursuit
ends. Indeed, rules adopted by countless police depart
ments throughout the country are based on a judgment
that differs from the Court’s. See, e.g., App. to Brief for
Georgia Association of Chiefs of Police, Inc., as Amicus
Curiae A–52 (“During a pursuit, the need to apprehend
the suspect should always outweigh the level of danger
created by the pursuit. When the immediate danger to the
public created by the pursuit is greater than the immedi
ate or potential danger to the public should the suspect
remain at large, then the pursuit should be discontinued
or terminated. . . . [P]ursuits should usually be discontin
——————
Court prioritizes total elimination of the risk of harm to the public over
the risk that respondent may be seriously injured or even killed. Ante,
at 12 (emphasis in original). The Court is only able to make such a
statement by assuming, based on its interpretation of events on the
videotape, that the risk of harm posed in this case, and the type of
harm involved, rose to a level warranting deadly force. These are the
same types of questions that, when disputed, are typically resolved by a
jury; this is why both the District Court and the Court of Appeals saw
fit to have them be so decided. Although the Court claims only to have
drawn factual inferences in respondent’s favor “to the extent supportable
by the record,” ante, at 8, n. 8 (emphasis in original), its own view of the
record has clearly precluded it from doing so to the same extent as the
two courts through which this case has already traveled, see ante, at 2–
3, 5–6.
                     Cite as: 550 U. S. ____ (2007)                   7

                        STEVENS, J., dissenting

ued when the violator’s identity has been established to
the point that later apprehension can be accomplished
without danger to the public”).
   Although Garner may not, as the Court suggests, “estab
lish a magical on/off switch that triggers rigid precondi
tions” for the use of deadly force, ante, at 9, it did set a
threshold under which the use of deadly force would be
considered constitutionally unreasonable:
     “Where the officer has probable cause to believe that
     the suspect poses a threat of serious physical harm,
     either to the officer or to others, it is not constitution
     ally unreasonable to prevent escape by using deadly
     force. Thus, if the suspect threatens the officer with a
     weapon or there is probable cause to believe that he
     has committed a crime involving the infliction or
     threatened infliction of serious physical harm, deadly
     force may be used if necessary to prevent escape, and
     if, where feasible, some warning has been given.” 471
     U. S., at 11–12.
Whether a person’s actions have risen to a level warrant
ing deadly force is a question of fact best reserved for a
jury.6 Here, the Court has usurped the jury’s factfinding
function and, in doing so, implicitly labeled the four other
judges to review the case unreasonable. It chastises the
Court of Appeals for failing to “vie[w] the facts in the light
depicted by the videotape” and implies that no reasonable
person could view the videotape and come to the conclu
sion that deadly force was unjustified. Ante, at 8. How
ever, the three judges on the Court of Appeals panel ap
——————
  6 In its opinion, the Court of Appeals correctly noted: “We reject the

defendants’ argument that Harris’ driving must, as a matter of law, be
considered sufficiently reckless to give Scott probable cause to believe
that he posed a substantial threat of imminent physical harm to
motorists and pedestrians. This is a disputed issue to be resolved by a
jury.” Harris v. Coweta County, 433 F. 3d 807, 815 (CA11 2005).
8                         SCOTT v. HARRIS

                        STEVENS, J., dissenting

parently did view the videotapes entered into evidence7
and described a very different version of events:
     “At the time of the ramming, apart from speeding and
     running two red lights, Harris was driving in a non-
     aggressive fashion (i.e., without trying to ram or run
     into the officers). Moreover, . . . Scott’s path on the
     open highway was largely clear. The videos intro
     duced into evidence show little to no vehicular (or pe
     destrian) traffic, allegedly because of the late hour
     and the police blockade of the nearby intersections.
     Finally, Scott issued absolutely no warning (e.g., over
     the loudspeaker or otherwise) prior to using deadly
     force.” Harris v. Coweta County, 433 F. 3d 807, 819,
     n. 14 (CA11 2005).
If two groups of judges can disagree so vehemently about
the nature of the pursuit and the circumstances surround
ing that pursuit, it seems eminently likely that a reason
able juror could disagree with this Court’s characteriza
tion of events. Moreover, under the standard set forth in
Garner, it is certainly possible that “a jury could conclude
that Scott unreasonably used deadly force to seize Harris
by ramming him off the road under the instant circum
stances.” 433 F. 3d, at 821.
   The Court today sets forth a per se rule that presumes
its own version of the facts: “A police officer’s attempt to
terminate a dangerous high-speed car chase that threatens
the lives of innocent bystanders does not violate the Fourth
Amendment, even when it places the fleeing motorist at
risk of serious injury or death.” Ante, at 13 (emphasis
added). Not only does that rule fly in the face of the flexi
ble and case-by-case “reasonableness” approach applied in
Garner and Graham v. Connor, 490 U. S. 386 (1989), but it

——————
  7 In total, there are four police tapes which captured portions of the

pursuit, all recorded from different officers’ vehicles.
                      Cite as: 550 U. S. ____ (2007)                     9

                         STEVENS, J., dissenting

is also arguably inapplicable to the case at hand, given
that it is not clear that this chase threatened the life of
any “innocent bystande[r].”8 In my view, the risks inher
ent in justifying unwarranted police conduct on the basis
of unfounded assumptions are unacceptable, particularly
when less drastic measures—in this case, the use of stop
sticks9 or a simple warning issued from a loudspeaker—
could have avoided such a tragic result. In my judgment,
jurors in Georgia should be allowed to evaluate the rea
sonableness of the decision to ram respondent’s speeding
vehicle in a manner that created an obvious risk of death
and has in fact made him a quadriplegic at the age of 19.
  I respectfully dissent.




——————
  8 It is unclear whether, in referring to “innocent bystanders,” the

Court is referring to the motorists driving unfazed in the opposite
direction or to the drivers who pulled over to the side of the road, safely
out of respondent’s and petitioner’s path.
  9 “Stop sticks” are a device which can be placed across the roadway

and used to flatten a vehicle’s tires slowly to safely terminate a pursuit.

```

---

## GROUP: content/cases/Screws v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Screws v. United States"
type: case
citation: "325 U.S. 91 (1945)"
parallel_cite: "65 S. Ct. 1031; 89 L. Ed. 1495; 162 A.L.R. 1330"
neutral_cite: 1945 U.S. LEXIS 2096
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1945
date_decided: 1945-05-07
docket: 42
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1945-05-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Screws v. United States
  varies_by_point: false
  scope_note: "Plurality (Douglas, J., announcing the judgment); the specific-intent construction of § 242 remains the controlling reading."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/104135/screws-v-united-states/"
  cluster_id: 104135
  opinion_id: 104135
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Monroe v. Pape]]"]
aliases: []
tags: ["case", "civil-rights", "color-of-law", "section-242", "willfulness"]
holding: "Construing 18 U.S.C. § 242 'willfully' — the criminal civil-rights statute requires a specific-intent (willful) deprivation of constitutional rights under color of law."
lake:
  record_id: Screws v. United States
  status: verified
  projected_at: 2026-07-06
---

# Screws v. United States

*325 U.S. 91 (1945)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Georgia sheriff M. Claude Screws and two other officers arrested Robert Hall, a young Black man, and beat him to death with their fists and a blackjack. They were convicted under the criminal civil-rights statute (now 18 U.S.C. § 242) of willfully depriving Hall, [[Section 1983 Liability and Qualified Immunity|under color of law]], of rights secured by the Constitution. They argued the statute was unconstitutionally vague.

## Issue
Whether § 242's prohibition on willfully depriving a person of constitutional rights [[Section 1983 Liability and Qualified Immunity|under color of law]] is void for vagueness, and what mental state "willfully" requires.

## Rule
The statute is saved from vagueness by reading "willfully" to require specific intent. "We do say that a requirement of a specific intent to deprive a person of a federal right made definite by decision or other rule of law saves the Act from any charge of unconstitutionality on the grounds of vagueness." — 325 U.S. at 103. ^pin-103

The Court also reaffirmed that action "under color of" state law includes the misuse of authority an officer possesses only because he is clothed with his official position.

## Application
Because the trial court had not instructed the jury that the defendants must have acted with the specific intent to deprive Hall of a federal constitutional right, the convictions could not stand under the proper construction of "willfully," and the Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for a new trial under that standard.

## Conclusion
Section 242 is not void for vagueness when read to require a willful—specific-intent—deprivation; the convictions were reversed for the faulty jury instruction and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Douglas, J., announced the judgment).
- The specific-intent construction of § 242 remains the controlling reading, and *Screws*'s "under color of law" analysis informs civil liability under § 1983 ([[Monroe v. Pape]]).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Screws v. United States*, 325 U.S. 91 (1945) — https://www.courtlistener.com/opinion/104135/screws-v-united-states/ — pinpoint: 103.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d8dd3927e9083511", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "325 U.S. 91 (1945)", "court": "U.S. Supreme Court", "neutral_cite": "1945 U.S. LEXIS 2096", "official_citation_present": true, "parallel_cite": "65 S. Ct. 1031; 89 L. Ed. 1495; 162 A.L.R. 1330", "title": "Screws v. United States", "year": "1945"}}
{"assertion_id": "cd7f6349fa795a4e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Construing 18 U.S.C. § 242 'willfully' — the criminal civil-rights statute requires a specific-intent (willful) deprivation of constitutional rights under color of law.", "title": "Screws v. United States"}}
{"assertion_id": "e1b94807b9ac09f6", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Related (cross-doctrine)", "title": "Screws v. United States"}}
{"assertion_id": "0957be2cb567c2e9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1945-05-07", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Screws v. United States", "field_i_validity": "good_law", "scope_note": "Plurality (Douglas, J., announcing the judgment); the specific-intent construction of § 242 remains the controlling reading.", "title": "Screws v. United States", "varies_by_point": "false"}}
{"assertion_id": "6e5fd6c7e4306e0f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Screws v. United States"}}
```

### lake record — Screws v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Screws v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Screws v. United States",
    "case_name_short": "Screws",
    "case_name_full": "SCREWS Et Al. v. UNITED STATES",
    "input_case_name": "Screws v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1945-05-07",
    "year": 1945,
    "docket": "42",
    "cluster_id": 104135,
    "lead_opinion_id": 104135,
    "sibling_ids": [
      104135,
      9419636,
      9419637,
      9419638,
      9419639
    ],
    "absolute_url": "/opinion/104135/screws-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "325 U.S. 91",
      "volume": "325",
      "reporter": "U.S.",
      "page": "91",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "65 S. Ct. 1031",
        "volume": "65",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 1495",
        "volume": "89",
        "reporter": "L. Ed.",
        "page": "1495",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "162 A.L.R. 1330",
        "volume": "162",
        "reporter": "A.L.R.",
        "page": "1330",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1945 U.S. LEXIS 2096",
        "volume": "1945",
        "reporter": "U.S. LEXIS",
        "page": "2096",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "325 U.S. 91",
        "volume": "325",
        "reporter": "U.S.",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 S. Ct. 1031",
        "volume": "65",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 1495",
        "volume": "89",
        "reporter": "L. Ed.",
        "page": "1495",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1945 U.S. LEXIS 2096",
        "volume": "1945",
        "reporter": "U.S. LEXIS",
        "page": "2096",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "162 A.L.R. 1330",
        "volume": "162",
        "reporter": "A.L.R.",
        "page": "1330",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "325 U.S. 91",
    "official_selection": {
      "court_class": "scotus",
      "selected": "325 U.S. 91",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-103",
      "page": null,
      "quote": "requires. ## Rule The statute is saved from vagueness by reading",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1945-05-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Screws v. United States",
    "varies_by_point": false,
    "scope_note": "Plurality (Douglas, J., announcing the judgment); the specific-intent construction of \u00a7 242 remains the controlling reading.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Kelly",
          "cluster_id": 2780739,
          "cite": [
            "470 Mass. 682",
            "25 N.E.3d 288"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dustin Myers v. Murry Bowman",
          "cluster_id": 857864,
          "cite": [
            "713 F.3d 1319",
            "2013 WL 1442055",
            "2013 U.S. App. LEXIS 7216",
            "24 Fla. L. Weekly Fed. C 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Winot",
          "cluster_id": 1545853,
          "cite": [
            "988 A.2d 188",
            "294 Conn. 753",
            "2010 Conn. LEXIS 45"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Franco Andre Goyzueta v. State",
          "cluster_id": 2853303,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellee-Cross-Appellant v. Eva C. Temple, Appellant-Cross-Appellee",
          "cluster_id": 794242,
          "cite": [
            "447 F.3d 130",
            "97 A.F.T.R.2d (RIA) 2265",
            "2006 U.S. App. LEXIS 10885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
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
        "journal_ref": "Screws v. United States:lane2_top_cited"
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
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wolff v. McDonnell",
          "cluster_id": 109097,
          "cite": [
            "41 L. Ed. 2d 935",
            "94 S. Ct. 2963",
            "418 U.S. 539",
            "1974 U.S. LEXIS 91",
            "71 Ohio Op. 2d 336"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
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
        "journal_ref": "Screws v. United States:lane2_top_cited"
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
        "journal_ref": "Screws v. United States:lane2_top_cited"
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
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul v. Davis",
          "cluster_id": 109402,
          "cite": [
            "47 L. Ed. 2d 405",
            "96 S. Ct. 1155",
            "424 U.S. 693",
            "1976 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monroe v. Pape",
          "cluster_id": 106170,
          "cite": [
            "5 L. Ed. 2d 492",
            "81 S. Ct. 473",
            "365 U.S. 167",
            "1961 U.S. LEXIS 1687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Koon v. United States",
          "cluster_id": 118044,
          "cite": [
            "135 L. Ed. 2d 392",
            "116 S. Ct. 2035",
            "518 U.S. 81",
            "1996 U.S. LEXIS 3877"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffman Estates v. Flipside, Hoffman Estates, Inc.",
          "cluster_id": 110661,
          "cite": [
            "71 L. Ed. 2d 362",
            "102 S. Ct. 1186",
            "455 U.S. 489",
            "1982 U.S. LEXIS 78",
            "50 U.S.L.W. 4267"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Shea v. Littleton",
          "cluster_id": 108906,
          "cite": [
            "38 L. Ed. 2d 674",
            "94 S. Ct. 669",
            "414 U.S. 488",
            "1974 U.S. LEXIS 41"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Breckenridge",
          "cluster_id": 108362,
          "cite": [
            "29 L. Ed. 2d 338",
            "91 S. Ct. 1790",
            "403 U.S. 88",
            "1971 U.S. LEXIS 3774",
            "3 Empl. Prac. Dec. (CCH) 8284",
            "9 Fair Empl. Prac. Cas. (BNA) 1196"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morissette v. United States",
          "cluster_id": 104952,
          "cite": [
            "96 L. Ed. 2d 288",
            "72 S. Ct. 240",
            "342 U.S. 246",
            "1952 U.S. LEXIS 2714",
            "96 L. Ed. 288"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lopez",
          "cluster_id": 117927,
          "cite": [
            "131 L. Ed. 2d 626",
            "115 S. Ct. 1624",
            "514 U.S. 549",
            "1995 U.S. LEXIS 3039"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Golding",
          "cluster_id": 7893833,
          "cite": [
            "213 Conn. 233",
            "567 A.2d 823",
            "1989 Conn. LEXIS 349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
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
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lanier",
          "cluster_id": 118098,
          "cite": [
            "137 L. Ed. 2d 432",
            "117 S. Ct. 1219",
            "520 U.S. 259",
            "1997 U.S. LEXIS 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hamdi v. Rumsfeld",
          "cluster_id": 137001,
          "cite": [
            "159 L. Ed. 2d 578",
            "124 S. Ct. 2633",
            "542 U.S. 507",
            "2004 U.S. LEXIS 4761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Papachristou v. City of Jacksonville",
          "cluster_id": 108472,
          "cite": [
            "31 L. Ed. 2d 110",
            "92 S. Ct. 839",
            "405 U.S. 156",
            "1972 U.S. LEXIS 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parker v. Levy",
          "cluster_id": 109077,
          "cite": [
            "41 L. Ed. 2d 439",
            "94 S. Ct. 2547",
            "417 U.S. 733",
            "1974 U.S. LEXIS 81"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harriss",
          "cluster_id": 105232,
          "cite": [
            "98 L. Ed. 2d 989",
            "74 S. Ct. 808",
            "347 U.S. 612",
            "1954 U.S. LEXIS 2657",
            "98 L. Ed. 989"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner Broadcasting System, Inc. v. Federal Communications Commission",
          "cluster_id": 117869,
          "cite": [
            "129 L. Ed. 2d 497",
            "114 S. Ct. 2445",
            "512 U.S. 622",
            "1994 U.S. LEXIS 4831"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Sparks",
          "cluster_id": 110353,
          "cite": [
            "66 L. Ed. 2d 185",
            "101 S. Ct. 183",
            "449 U.S. 24",
            "1980 U.S. LEXIS 9",
            "49 U.S.L.W. 4001"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chapman v. Houston Welfare Rights Organization",
          "cluster_id": 110076,
          "cite": [
            "60 L. Ed. 2d 508",
            "99 S. Ct. 1905",
            "441 U.S. 600",
            "1979 U.S. LEXIS 101"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Goguen",
          "cluster_id": 108988,
          "cite": [
            "39 L. Ed. 2d 605",
            "94 S. Ct. 1242",
            "415 U.S. 566",
            "1974 U.S. LEXIS 113"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(104135 OR 9419636 OR 9419637 OR 9419638 OR 9419639) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDk4MDU3NjAwMDAwJnM9MzY0NzYmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28104135+OR+9419636+OR+9419637+OR+9419638+OR+9419639%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(104135 OR 9419636 OR 9419637 OR 9419638 OR 9419639)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NzImcz0xMDk5NjYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28104135+OR+9419636+OR+9419637+OR+9419638+OR+9419639%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(104135 OR 9419636 OR 9419637 OR 9419638 OR 9419639)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(104135 OR 9419636 OR 9419637 OR 9419638 OR 9419639)",
    "indexed_citing_opinions": 1336,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 104135,
        "count": 1235,
        "count_source": "search"
      },
      {
        "opinion_id": 9419636,
        "count": 142,
        "count_source": "search"
      },
      {
        "opinion_id": 9419637,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9419638,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9419639,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2025,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/screws-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMDIwNDMmcz05Mzg4MjcwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28104135+OR+9419636+OR+9419637+OR+9419638+OR+9419639%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 104135,
        "cited_id": 85535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 89309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 89649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 91064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 91179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 91598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 91704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 92834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 93322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 94052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 94235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 94648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 95097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 95317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 97275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 97326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 97928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99947,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101955,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102826,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103632,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103870,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1087658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1087739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1410732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1410842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1447641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1480783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1500930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1511950,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1564666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1567036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1620902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1739405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1755008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 2394729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 2620779,
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
    "date_created": "2026-07-05T18:47:38Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:47:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:47:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:57:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:47:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Screws v. United States (truncated)

```
<div>
<center><b><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U.S. 91</a></span> (1945)</b></center>
<center><h1>SCREWS ET AL.<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 42.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 20, 1944.</center>
<center>Decided May 7, 1945.</center>
CERTIORARI TO THE CIRCUIT COURT OF APPEALS FOR THE FIFTH CIRCUIT.
<p><span class="star-pagination">*92</span> <i>Mr. James F. Kemp,</i> with whom <i>Messrs. Clint W. Hager</i> and <i>Robert B. Short</i> were on the brief, for petitioners.</p>
<p><i>Solicitor General Fahy,</i> with whom <i>Assistant Attorney General Tom C. Clark, Messrs. Robert S. Erdahl</i> and <i>Irving S. Shapiro</i> were on the brief, for the United States.</p>
<p><i>Messrs. William H. Hastie, Thurgood Marshall</i> and <i>Leon A. Ransom</i> filed a brief on behalf of the National Association for the Advancement of Colored People, as <i>amicus curiae,</i> urging affirmance.</p>
<p>MR. JUSTICE DOUGLAS announced the judgment of the Court and delivered the following opinion, in which the CHIEF JUSTICE, MR. JUSTICE BLACK and MR. JUSTICE REED concur.</p>
<p>This case involves a shocking and revolting episode in law enforcement. Petitioner Screws was sheriff of Baker County, Georgia. He enlisted the assistance of petitioner Jones, a policeman, and petitioner Kelley, a special deputy, in arresting Robert Hall, a citizen of the United States and of Georgia. The arrest was made late at night at Hall's home on a warrant charging Hall with theft of a tire. Hall, a young negro about thirty years of age, was handcuffed and taken by car to the court house. As Hall alighted from the car at the court-house square, the three petitioners began beating him with their fists and with a solid-bar blackjack about eight inches long and weighing two pounds. They claimed Hall had reached for a gun and had used insulting language as he alighted from the <span class="star-pagination">*93</span> car. But after Hall, still handcuffed, had been knocked to the ground they continued to beat him from fifteen to thirty minutes until he was unconscious. Hall was then dragged feet first through the court-house yard into the jail and thrown upon the floor dying. An ambulance was called and Hall was removed to a hospital where he died within the hour and without regaining consciousness. There was evidence that Screws held a grudge against Hall and had threatened to "get" him.</p>
<p>An indictment was returned against petitioners  one count charging a violation of § 20 of the Criminal Code, <span class="citation no-link">18 U.S.C. § 52</span> and another charging a conspiracy to violate § 20 contrary to § 37 of the Criminal Code, <span class="citation no-link">18 U.S.C. § 88</span>. Sec. 20 provides:</p>
<p>"Whoever, under color of any law, statute, ordinance, regulation, or custom, willfully subjects, or causes to be subjected, any inhabitant of any State, Territory, or District to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution and laws of the United States, or to different punishments, pains, or penalties, on account of such inhabitant being an alien, or by reason of his color, or race, than are prescribed for the punishment of citizens, shall be fined not more than $1,000, or imprisoned not more than one year, or both." The indictment charged that petitioners, acting under color of the laws of Georgia, "willfully" caused Hall to be deprived of "rights, privileges, or immunities secured or protected" to him by the Fourteenth Amendment  the right not to be deprived of life without due process of law; the right to be tried, upon the charge on which he was arrested, by due process of law and if found guilty to be punished in accordance with the laws of Georgia; that is to say that petitioners "unlawfully and wrongfully did assault, strike and beat the said Robert Hall about the head with human fists and a blackjack causing injuries" to Hall "which were the proximate and immediate cause <span class="star-pagination">*94</span> of his death." A like charge was made in the conspiracy count.</p>
<p>The case was tried to a jury.<sup>[1]</sup> The court charged the jury that due process of law gave one charged with a crime the right to be tried by a jury and sentenced by a court. On the question of intent it charged that</p>
<p>". . . if these defendants, without its being necessary to make the arrest effectual or necessary to their own personal protection, beat this man, assaulted him or killed him while he was under arrest, then they would be acting illegally under color of law, as stated by this statute, and would be depriving the prisoner of certain constitutional rights guaranteed to him by the Constitution of the United States and consented to by the State of Georgia."</p>
<p>The jury returned a verdict of guilty and a fine and imprisonment on each count was imposed. The Circuit Court of Appeals affirmed the judgment of conviction, one judge dissenting. <span class="citation" data-id="9653538"><a href="/opinion/1567036/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">140 F.2d 662</a></span>. The case is here on a petition for a writ of certiorari which we granted because of the importance in the administration of the criminal laws of the questions presented.</p>
<p></p>
<h2>I</h2>
<p>We are met at the outset with the claim that § 20 is unconstitutional, insofar as it makes criminal acts in violation of the due process clause of the Fourteenth Amendment. The argument runs as follows: It is true that this Act as construed in <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#328" aria-description="Citation for case: United States v. Classic">313 U.S. 299, 328</a></span>, was upheld in its application to certain ballot box frauds committed by state officials. But in that case the constitutional rights protected were the rights to vote <span class="star-pagination">*95</span> specifically guaranteed by Art. I, § 2 and § 4 of the Constitution. Here there is no ascertainable standard of guilt. There have been conflicting views in the Court as to the proper construction of the due process clause. The majority have quite consistently construed it in broad general terms. Thus it was stated in <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#101" aria-description="Citation for case: Twining v. New Jersey">211 U.S. 78, 101</a></span>, that due process requires that "no change in ancient procedure can be made which disregards those fundamental principles, to be ascertained from time to time by judicial action, which have relation to process of law and protect the citizen in his private right, and guard him against the arbitrary action of government." In <i>Snyder</i> v. <i>Massachusetts,</i> <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U.S. 97, 105</a></span>, it was said that due process prevents state action which "offends some principle of justice so rooted in the traditions and conscience of our people as to be ranked as fundamental." The same standard was expressed in <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U.S. 319, 325</a></span>, in terms of a "scheme of ordered liberty." And the same idea was recently phrased as follows: "The phrase formulates a concept less rigid and more fluid than those envisaged in other specific and particular provisions of the Bill of Rights. Its application is less a matter of rule. Asserted denial is to be tested by an appraisal of the totality of facts in a given case. That which may, in one setting, constitute a denial of fundamental fairness, shocking to the universal sense of justice, may, in other circumstances, and in the light of other considerations, fall short of such denial." <i>Betts</i> v. <i>Brady,</i> <span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/#462" aria-description="Citation for case: Betts v. Brady">316 U.S. 455, 462</a></span>.</p>
<p>It is said that the Act must be read as if it contained those broad and fluid definitions of due process and that if it is so read it provides no ascertainable standard of guilt. It is pointed out that in <i>United States</i> v. <i>Cohen Grocery Co.,</i> <span class="citation" data-id="9418445"><a href="/opinion/99713/united-states-v-l-cohen-grocery-co/#89" aria-description="Citation for case: United States v. L. Cohen Grocery Co.">255 U.S. 81, 89</a></span>, an Act of Congress was struck down, the enforcement of which would have been "the exact equivalent of an effort to carry out a statute <span class="star-pagination">*96</span> which in terms merely penalized and punished all acts detrimental to the public interest when unjust and unreasonable in the estimation of the court and jury." In that case the act declared criminal was the making of "any unjust or unreasonable rate or charge in handling or dealing in or with any necessaries." 255 U.S. p. 86. The Act contained no definition of an "unjust or unreasonable rate" nor did it refer to any source where the measure of "unjust or unreasonable" could be ascertained. In the instant case the decisions of the courts are, to be sure, a source of reference for ascertaining the specific content of the concept of due process. But even so the Act would incorporate by reference a large body of changing and uncertain law. That law is not always reducible to specific rules, is expressible only in general terms, and turns many times on the facts of a particular case. Accordingly, it is argued that such a body of legal principles lacks the basic specificity necessary for criminal statutes under our system of government. Congress did not define what it desired to punish but referred the citizen to a comprehensive law library in order to ascertain what acts were prohibited. To enforce such a statute would be like sanctioning the practice of Caligula who "published the law, but it was written in a very small hand, and posted up in a corner, so that no one could make a copy of it." Suetonius, Lives of the Twelve Caesars, p. 278.</p>
<p>The serious character of that challenge to the constitutionality of the Act is emphasized if the customary standard of guilt for statutory crimes is taken. As we shall see, specific intent is at times required. Holmes, The Common Law, pp. 66 <i>et seq.</i> But the general rule was stated in <i>Ellis</i> v. <i>United States,</i> <span class="citation" data-id="9418092"><a href="/opinion/96682/ellis-v-united-states/#257" aria-description="Citation for case: Ellis v. United States">206 U.S. 246, 257</a></span>, as follows: "If a man intentionally adopts certain conduct in certain circumstances known to him, and that conduct is forbidden by the law under those circumstances, he intentionally breaks the law in the only sense in which the law ever considers intent." And see <i>Horning</i> v. <i>District of</i> <span class="star-pagination">*97</span> <i>Columbia,</i> <span class="citation" data-id="9418436"><a href="/opinion/99651/horning-v-district-of-columbia/#137" aria-description="Citation for case: Horning v. District of Columbia">254 U.S. 135, 137</a></span>; <i>Nash</i> v. <i>United States,</i> <span class="citation" data-id="97928"><a href="/opinion/97928/nash-v-united-states/#377" aria-description="Citation for case: Nash v. United States">229 U.S. 373, 377</a></span>. Under that test a local law enforcement officer violates § 20 and commits a federal offense for which he can be sent to the penitentiary if he does an act which some court later holds deprives a person of due process of law. And he is a criminal though his motive was pure and though his purpose was unrelated to the disregard of any constitutional guarantee. The treacherous ground on which state officials  police, prosecutors, legislators, and judges  would walk is indicated by the character and closeness of decisions of this Court interpreting the due process clause of the Fourteenth Amendment. A confession obtained by too long questioning (<i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U.S. 143</a></span>); the enforcement of an ordinance requiring a license for the distribution of religious literature (<i>Murdock</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9419338"><a href="/opinion/103831/murdock-v-pennsylvania/" aria-description="Citation for case: Murdock v. Pennsylvania">319 U.S. 105</a></span>); the denial of the assistance of counsel in certain types of cases (Cf. <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U.S. 45</a></span> with <i>Betts</i> v. <i><span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/" aria-description="Citation for case: Betts v. Brady">Brady, supra</a></span></i>); the enforcement of certain types of anti-picketing statutes (<i>Thornhill</i> v. <i>Alabama,</i> <span class="citation" data-id="103347"><a href="/opinion/103347/thornhill-v-alabama/" aria-description="Citation for case: Thornhill v. Alabama">310 U.S. 88</a></span>); the enforcement of state price control laws (<i>Olsen</i> v. <i>Nebraska,</i> <span class="citation" data-id="103522"><a href="/opinion/103522/olsen-v-nebraska-ex-rel-western-reference-bond-assn-inc/" aria-description="Citation for case: Olsen v. Nebraska Ex Rel. Western Reference &amp; Bond Assn.,...">313 U.S. 236</a></span>); the requirement that public school children salute the flag (<i>Board of Education</i> v. <i>Barnette,</i> <span class="citation" data-id="9419378"><a href="/opinion/103870/west-virginia-state-board-of-education-v-barnette/" aria-description="Citation for case: West Virginia State Board of Education v. Barnette">319 U.S. 624</a></span>)  these are illustrative of the kind of state action<sup>[2]</sup> which might or might not be caught in the broad reaches of § 20 dependent on the prevailing view of the Court as constituted when the case arose. Those who enforced local law today might not know for many months (and meanwhile could not find out) whether what they did deprived some one of due process of law. The enforcement of a criminal statute so construed would indeed cast <span class="star-pagination">*98</span> law enforcement agencies loose at their own risk on a vast uncharted sea.</p>
<p>If such a construction is not necessary, it should be avoided. This Court has consistently favored that interpretation of legislation which supports its constitutionality. <i>Ashwander</i> v. <i>Tennessee Valley Authority,</i> <span class="citation" data-id="9418878"><a href="/opinion/102605/ashwander-v-tennessee-valley-authority/#348" aria-description="Citation for case: Ashwander v. Tennessee Valley Authority">297 U.S. 288, 348</a></span>; <i>Labor Board</i> v. <i>Jones &amp; Laughlin Steel Corp.,</i> <span class="citation" data-id="102804"><a href="/opinion/102804/national-labor-relations-board-v-jones-laughlin-steel-corp/#30" aria-description="Citation for case: National Labor Relations Board v. Jones &amp; Laughlin Steel...">301 U.S. 1, 30</a></span>; <i>Anniston Mfg. Co.</i> v. <i>Davis,</i> <span class="citation" data-id="9418917"><a href="/opinion/102826/anniston-manufacturing-co-v-davis/#351" aria-description="Citation for case: Anniston Manufacturing Co. v. Davis">301 U.S. 337, 351-352</a></span>. That reason is impelling here so that if at all possible § 20 may be allowed to serve its great purpose  the protection of the individual in his civil liberties.</p>
<p>Sec. 20 was enacted to enforce the Fourteenth Amendment.<sup>[3]</sup> It derives<sup>[4]</sup> from § 2 of the Civil Rights Act of April 9, 1866. <span class="citation no-link">14 Stat. 27</span>.<sup>[5]</sup> Senator Trumbull, chairman of the Senate Judiciary Committee which reported the bill, stated that its purpose was "to protect all persons in the United States in their civil rights, and furnish the means of their vindication." Cong. Globe, 39th Cong., 1st Sess., p. 211. In origin it was an antidiscrimination measure (as its language indicated), framed to protect Negroes in their newly won rights. See Flack, The Adoption of the Fourteenth Amendment (1908), p. 21. It was <span class="star-pagination">*99</span> amended by § 17 of the Act of May 31, 1870, <span class="citation no-link">16 Stat. 144</span>,<sup>[6]</sup> and made applicable to "any inhabitant of any State or Territory."<sup>[7]</sup> The prohibition against the "deprivation of any rights, privileges, or immunities, secured or protected by the Constitution and laws of the United States" was introduced by the revisers in 1874. R.S. § 5510. Those words were taken over from § 1 of the Act of April 20, 1871, <span class="citation no-link">17 Stat. 13</span> (the so-called Ku-Klux Act) which provided civil suits for redress of such wrongs.<sup>[8]</sup> See Cong. Rec., <span class="star-pagination">*100</span> 43d Cong., 1st Sess., p. 828. The 1874 revision was applicable to any person who under color of law, etc., "subjects, or causes to be subjected" any inhabitant to the deprivation of any rights, etc. The requirement for a "willful" violation was introduced by the draftsmen of the Criminal Code of 1909. Act of March 4, 1909, <span class="citation no-link">35 Stat. 1092</span>. And we are told "willfully" was added to § 20 in order to make the section "less severe." 43 Cong. Rec., 60th Cong., 2d Sess., p. 3599.</p>
<p>We hesitate to say that when Congress sought to enforce the Fourteenth Amendment<sup>[9]</sup> in this fashion it did a vain thing. We hesitate to conclude that for 80 years this effort of Congress, renewed several times, to protect the important rights of the individual guaranteed by the Fourteenth Amendment has been an idle gesture. Yet if the Act falls by reason of vagueness so far as due process of law is concerned, there would seem to be a similar lack of specificity when the privileges and immunities clause (<i>Madden</i> v. <i>Kentucky,</i> <span class="citation" data-id="9419076"><a href="/opinion/103290/madden-v-kentucky-ex-rel-commissioner/" aria-description="Citation for case: Madden v. Kentucky Ex Rel. Commissioner">309 U.S. 83</a></span>) and the equal protection clause (<i>Smith</i> v. <i>Texas,</i> <span class="citation" data-id="103391"><a href="/opinion/103391/smith-v-texas/" aria-description="Citation for case: Smith v. Texas">311 U.S. 128</a></span>; <i>Hill</i> v. <i>Texas,</i> <span class="citation" data-id="103690"><a href="/opinion/103690/hill-v-texas/" aria-description="Citation for case: Hill v. Texas">316 U.S. 400</a></span>) of the Fourteenth Amendment are involved. Only if no construction can save the Act from this claim of unconstitutionality are we willing to reach that result. We do not reach it, for we are of the view that if § 20 is confined more narrowly than the lower courts confined it, it can be preserved as one of the sanctions to the great rights which the Fourteenth Amendment was designed to secure.</p>
<p></p>
<h2>
<span class="star-pagination">*101</span> II</h2>
<p>We recently pointed out that "willful" is a word "of many meanings, its construction often being influenced by its context." <i>Spies</i> v. <i>United States,</i> <span class="citation" data-id="103753"><a href="/opinion/103753/spies-v-united-states/#497" aria-description="Citation for case: Spies v. United States">317 U.S. 492, 497</a></span>. At times, as the Court held in <i>United States</i> v. <i>Murdock,</i> <span class="citation" data-id="102166"><a href="/opinion/102166/united-states-v-murdock/#394" aria-description="Citation for case: United States v. Murdock">290 U.S. 389, 394</a></span>, the word denotes an act which is intentional rather than accidental. And see <i>United States</i> v. <i>Illinois Central R. Co.,</i> <span class="citation" data-id="102970"><a href="/opinion/102970/united-states-v-illinois-central-railroad/" aria-description="Citation for case: United States v. Illinois Central Railroad">303 U.S. 239</a></span>. But "when used in a criminal statute it generally means an act done with a bad purpose." <i>Id.,</i> p. 394. And see <i>Felton</i> v. <i>United States,</i> <span class="citation" data-id="1087739"><a href="/opinion/1087739/felton-v-united-states/" aria-description="Citation for case: Felton v. United States">96 U.S. 699</a></span>; <i>Potter</i> v. <i>United States,</i> <span class="citation" data-id="94052"><a href="/opinion/94052/potter-v-united-states/" aria-description="Citation for case: Potter v. United States">155 U.S. 438</a></span>; <i>Spurr</i> v. <i>United States,</i> <span class="citation" data-id="95097"><a href="/opinion/95097/spurr-v-united-states/" aria-description="Citation for case: Spurr v. United States">174 U.S. 728</a></span>; <i>Hargrove</i> v. <i>United States,</i> <span class="citation" data-id="1564666"><a href="/opinion/1564666/hargrove-v-united-states/" aria-description="Citation for case: Hargrove v. United States">67 F.2d 820</a></span>. In that event something more is required than the doing of the act proscribed by the statute. Cf. <i>United States</i> v. <i>Balint,</i> <span class="citation" data-id="99947"><a href="/opinion/99947/united-states-v-balint/" aria-description="Citation for case: United States v. Balint">258 U.S. 250</a></span>. An evil motive to accomplish that which the statute condemns becomes a constituent element of the crime. <i>Spurr</i> v. <i>United States, supra,</i> p. 734; <i>United States</i> v. <i>Murdock, supra,</i> p. 395. And that issue must be submitted to the jury under appropriate instructions. <i>United States</i> v. <i>Ragen,</i> <span class="citation" data-id="103582"><a href="/opinion/103582/united-states-v-ragen/#524" aria-description="Citation for case: United States v. Ragen">314 U.S. 513, 524</a></span>.</p>
<p>An analysis of the cases in which "willfully" has been held to connote more than an act which is voluntary or intentional would not prove helpful as each turns on its own peculiar facts. Those cases, however, make clear that if we construe "willfully" in § 20 as connoting a purpose to deprive a person of a specific constitutional right, we would introduce no innovation. The Court, indeed, has recognized that the requirement of a specific intent to do a prohibited act may avoid those consequences to the accused which may otherwise render a vague or indefinite statute invalid. The constitutional vice in such a statute is the essential injustice to the accused of placing him on trial for an offense, the nature of which the statute does not define and hence of which it gives no warning. <span class="star-pagination">*102</span> See <i>United States</i> v. <i>Cohen Grocery Co., supra</i><i>.</i> But where the punishment imposed is only for an act knowingly done with the purpose of doing that which the statute prohibits, the accused cannot be said to suffer from lack of warning or knowledge that the act which he does is a violation of law. The requirement that the act must be willful or purposeful may not render certain, for all purposes, a statutory definition of the crime which is in some respects uncertain. But it does relieve the statute of the objection that it punishes without warning an offense of which the accused was unaware. That was pointed out by Mr. Justice Brandeis speaking for the Court in <i>Omaechevarria</i> v. <i>Idaho,</i> <span class="citation" data-id="99130"><a href="/opinion/99130/omaechevarria-v-idaho/" aria-description="Citation for case: Omaechevarria v. Idaho">246 U.S. 343</a></span>. An Idaho statute made it a misdemeanor to graze sheep "upon any range usually occupied by any cattle grower." The argument was that the statute was void for indefiniteness because it failed to provide for the ascertainment of boundaries of a "range" or for determining what length of time was necessary to make a prior occupation a "usual" one. The Court ruled that "any danger to sheepmen which might otherwise arise from indefiniteness, is removed by § 6314 of Revised Codes, which provides that: `In every crime or public offense there must exist a union, or joint operation, of act and intent, or criminal negligence.'" <i>Id.,</i> p. 348. A similar ruling was made in <i>Hygrade Provision Co.</i> v. <i>Sherman,</i> <span class="citation" data-id="1620902"><a href="/opinion/1620902/hygrade-provision-co-v-sherman/" aria-description="Citation for case: Hygrade Provision Co. v. Sherman">266 U.S. 497</a></span>. The charge was that a criminal statute which regulated the sale of "kosher" meat or products "sanctioned by the orthodox Hebrew religious requirements" was unconstitutional for want of any ascertainable standard of guilt. The Court speaking through Mr. Justice Sutherland stated, ". . . since the statutes require a specific intent to defraud in order to encounter their prohibitions, the hazard of prosecution which appellants fear loses whatever substantial foundation it might have in the absence of such a requirement." 266 U.S. pp. 502-503. In <i>United States</i> v. <i><span class="citation" data-id="103582"><a href="/opinion/103582/united-states-v-ragen/" aria-description="Citation for case: United States v. Ragen">Ragen, supra</a></span></i><i>,</i> we took <span class="star-pagination">*103</span> that course in a prosecution for willful evasion of a federal income tax where it was alleged that the defendant had deducted more than "reasonable" allowances for salaries. By construing the statute to require proof of bad faith we avoided the serious question which the rule of <i>United States</i> v. <i>Cohen Grocery Co., supra</i><i>,</i> might have presented. We think a like course is appropriate here.</p>
<p>Moreover, the history of § 20 affords some support for that narrower construction. As we have seen, the word "willfully" was not added to the Act until 1909. Prior to that time it may be that Congress intended that he who deprived a person of any right protected by the Constitution should be liable without more. That was the pattern of criminal legislation which has been sustained without any charge or proof of <i>scienter. </i><i>Shevlin-Carpenter Co.</i> v. <i>Minnesota,</i> <span class="citation" data-id="97275"><a href="/opinion/97275/shevlin-carpenter-co-v-minnesota/" aria-description="Citation for case: Shevlin-Carpenter Co. v. Minnesota">218 U.S. 57</a></span>; <i>United States</i> v. <i><span class="citation" data-id="99947"><a href="/opinion/99947/united-states-v-balint/" aria-description="Citation for case: United States v. Balint">Balint, supra</a></span></i><i>.</i> And the present Act in its original form would have been susceptible of the same interpretation apart from the equal protection clause of the Fourteenth Amendment, where "purposeful discriminatory" action must be shown. <i>Snowden</i> v. <i>Hughes,</i> <span class="citation" data-id="9419429"><a href="/opinion/103921/snowden-v-hughes/#8" aria-description="Citation for case: Snowden v. Hughes">321 U.S. 1, 8-9</a></span>. But as we have seen, the word "willfully" was added to make the section "less severe." We think the inference is permissible that its severity was to be lessened by making it applicable only where the requisite bad purpose was present, thus requiring specific intent not only where discrimination is claimed but in other situations as well. We repeat that the presence of a bad purpose or evil intent alone may not be sufficient. We do say that a requirement of a specific intent to deprive a person of a federal right made definite by decision or other rule of law saves the Act from any charge of unconstitutionality on the grounds of vagueness.</p>
<p>Once the section is given that construction, we think that the claim that the section lacks an ascertainable standard of guilt must fail. The constitutional requirement that a criminal statute be definite serves a high function. <span class="star-pagination">*104</span> It gives a person acting with reference to the statute fair warning that his conduct is within its prohibition. This requirement is met when a statute prohibits only "willful" acts in the sense we have explained. One who does act with such specific intent is aware that what he does is precisely that which the statute forbids. He is under no necessity of guessing whether the statute applies to him (see <i>Connally</i> v. <i>General Construction Co.,</i> <span class="citation" data-id="100759"><a href="/opinion/100759/connally-v-general-construction-co/" aria-description="Citation for case: Connally v. General Construction Co.">269 U.S. 385</a></span>) for he either knows or acts in reckless disregard of its prohibition of the deprivation of a defined constitutional or other federal right. See <i>Gorin</i> v. <i>United States,</i> <span class="citation" data-id="103434"><a href="/opinion/103434/gorin-v-united-states/#27" aria-description="Citation for case: Gorin v. United States">312 U.S. 19, 27-28</a></span>. Nor is such an act beyond the understanding and comprehension of juries summoned to pass on them. The Act would then not become a trap for law enforcement agencies acting in good faith. "A mind intent upon willful evasion is inconsistent with surprised innocence." <i>United States</i> v. <span class="citation" data-id="103582"><a href="/opinion/103582/united-states-v-ragen/#524" aria-description="Citation for case: United States v. Ragen"><i>Ragen, supra,</i> p. 524</a></span>.</p>
<p>It is said, however, that this construction of the Act will not save it from the infirmity of vagueness since neither a law enforcement official nor a trial judge can know with sufficient definiteness the range of rights that are constitutional. But that criticism is wide of the mark. For the specific intent required by the Act is an intent to deprive a person of a right which has been made specific either by the express terms of the Constitution or laws of the United States or by decisions interpreting them. Take the case of a local officer who persists in enforcing a type of ordinance which the Court has held invalid as violative of the guarantees of free speech or freedom of worship. Or a local official continues to select juries in a manner which flies in the teeth of decisions of the Court. If those acts are done willfully, how can the officer possibly claim that he had no fair warning that his acts were prohibited by the statute? He violates the statute not merely because he has a bad purpose but because he acts in defiance of announced rules of law. He who defies a <span class="star-pagination">*105</span> decision interpreting the Constitution knows precisely what he is doing. If sane, he hardly may be heard to say that he knew not what he did. Of course, willful conduct cannot make definite that which is undefined. But willful violators of constitutional requirements, which have been defined, certainly are in no position to say that they had no adequate advance notice that they would be visited with punishment. When they act willfully in the sense in which we use the word, they act in open defiance or in reckless disregard of a constitutional requirement which has been made specific and definite. When they are convicted for so acting, they are not punished for violating an unknowable something.</p>
<p>The Act so construed has a narrower range in all its applications than if it were interpreted in the manner urged by the government. But the only other alternative, if we are to avoid grave constitutional questions, is to construe it as applicable only to those acts which are clearly marked by the specific provisions of the Constitution as deprivations of constitutional rights, privileges, or immunities, and which are knowingly done within the rule of <i>Ellis</i> v. <i>United States, supra</i><i>.</i> But as we have said, that course would mean that all protection for violations of due process of law would drop out of the Act. We take the course which makes it possible to preserve the entire Act and save all parts of it from constitutional challenge. If Congress desires to give the Act wider scope, it may find ways of doing so. Moreover, here as in <i>Apex Hosiery Co.</i> v. <i>Leader,</i> <span class="citation" data-id="9419107"><a href="/opinion/103367/apex-hosiery-co-v-leader/" aria-description="Citation for case: Apex Hosiery Co. v. Leader">310 U.S. 469</a></span>, we are dealing with a situation where the interpretation of the Act which we adopt does not preclude any state from punishing any act made criminal by its own laws. Indeed, the narrow construction which we have adopted more nearly preserves the traditional balance between the States and the national government in law enforcement than that which is urged upon us.</p>
<p><span class="star-pagination">*106</span> <i>United States</i> v. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic, supra</a></span></i><i>,</i> met the test we suggest. In that case we were dealing merely with the validity of an indictment, not with instructions to the jury. The indictment was sufficient since it charged a willful failure and refusal of the defendant election officials to count the votes cast, by their alteration of the ballots and by their false certification of the number of votes cast for the respective candidates. 313 U.S. pp. 308-309. The right so to vote is guaranteed by Art. I, § 2 and § 4 of the Constitution. Such a charge is adequate since he who alters ballots or without legal justification destroys them would be acting willfully in the sense in which § 20 uses the term. The fact that the defendants may not have been thinking in constitutional terms is not material where their aim was not to enforce local law but to deprive a citizen of a right and that right was protected by the Constitution. When they so act they at least act in reckless disregard of constitutional prohibitions or guarantees. Likewise, it is plain that basic to the concept of due process of law in a criminal case is a trial  a trial in a court of law, not a "trial by ordeal." <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U.S. 278, 285</a></span>. It could hardly be doubted that they who "under color of any law, statute, ordinance, regulation, or custom" act with that evil motive violate § 20. Those who decide to take the law into their own hands and act as prosecutor, jury, judge, and executioner plainly act to deprive a prisoner of the trial which due process of law guarantees him. And such a purpose need not be expressed; it may at times be reasonably inferred from all the circumstances attendant on the act. See <i>Tot</i> v. <i>United States,</i> <span class="citation" data-id="103855"><a href="/opinion/103855/tot-v-united-states/" aria-description="Citation for case: Tot v. United States">319 U.S. 463</a></span>.</p>
<p>The difficulty here is that this question of intent was not submitted to the jury with the proper instructions. The court charged that petitioners acted illegally if they applied more force than was necessary to make the arrest effectual or to protect themselves from the prisoner's alleged <span class="star-pagination">*107</span> assault. But in view of our construction of the word "willfully" the jury should have been further instructed that it was not sufficient that petitioners had a generally bad purpose. To convict it was necessary for them to find that petitioners had the purpose to deprive the prisoner of a constitutional right, e. g. the right to be tried by a court rather than by ordeal. And in determining whether that requisite bad purpose was present the jury would be entitled to consider all the attendant circumstances  the malice of petitioners, the weapons used in the assault, its character and duration, the provocation, if any, and the like.</p>
<p>It is true that no exception was taken to the trial court's charge. Normally we would under those circumstances not take note of the error. See <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/#200" aria-description="Citation for case: Johnson v. United States">318 U.S. 189, 200</a></span>. But there are exceptions to that rule. <i>United States</i> v. <i>Atkinson,</i> <span class="citation" data-id="102591"><a href="/opinion/102591/united-states-v-atkinson/#160" aria-description="Citation for case: United States v. Atkinson">297 U.S. 157, 160</a></span>; <i>Clyatt</i> v. <i>United States,</i> <span class="citation" data-id="9417982"><a href="/opinion/96244/clyatt-v-united-states/#221" aria-description="Citation for case: Clyatt v. United States">197 U.S. 207, 221-222</a></span>. And where the error is so fundamental as not to submit to the jury the essential ingredients of the only offense on which the conviction could rest, we think it is necessary to take note of it on our own motion. Even those guilty of the most heinous offenses are entitled to a fair trial. Whatever the degree of guilt, those charged with a federal crime are entitled to be tried by the standards of guilt which Congress has prescribed.</p>
<p></p>
<h2>III</h2>
<p>It is said, however, that petitioners did not act "under color of any law" within the meaning of § 20 of the Criminal Code. We disagree. We are of the view that petitioners acted under "color" of law in making the arrest of Robert Hall and in assaulting him. They were officers of the law who made the arrest. By their own admissions they assaulted Hall in order to protect themselves and to keep their prisoner from escaping. It was their duty <span class="star-pagination">*108</span> under Georgia law to make the arrest effective. Hence, their conduct comes within the statute.</p>
<p>Some of the arguments which have been advanced in support of the contrary conclusion suggest that the question under § 20 is whether Congress has made it a federal offense for a state officer to violate the law of his State. But there is no warrant for treating the question in state law terms. The problem is not whether state law has been violated but whether an inhabitant of a State has been deprived of a federal right by one who acts under "color of any law." He who acts under "color" of law may be a federal officer or a state officer. He may act under "color" of federal law or of state law. The statute does not come into play merely because the federal law or the state law under which the officer purports to act is violated. It is applicable when and only when someone is deprived of a federal right by that action. The fact that it is also a violation of state law does not make it any the less a federal offense punishable as such. Nor does its punishment by federal authority encroach on state authority or relieve the state from its responsibility for punishing state offenses.<sup>[10]</sup></p>
<p>We agree that when this statute is applied to the action of state officials, it should be construed so as to respect the proper balance between the States and the federal government in law enforcement. Violation of local law does not necessarily mean that federal rights have been invaded. The fact that a prisoner is assaulted, injured, or even murdered by state officials does not necessarily mean that he is deprived of any right protected or secured by the <span class="star-pagination">*109</span> Constitution or laws of the United States. Cf. <i>Logan</i> v. <i>United States,</i> <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">144 U.S. 263</a></span>, dealing with assaults by federal officials. The Fourteenth Amendment did not alter the basic relations between the States and the national government. <i>United States</i> v. <i>Harris,</i> <span class="citation" data-id="90728"><a href="/opinion/90728/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">106 U.S. 629</a></span>; <i>In re Kemmler,</i> <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/#448" aria-description="Citation for case: In Re Kemmler">136 U.S. 436, 448</a></span>. Our national government is one of delegated powers alone. Under our federal system the administration of criminal justice rests with the States except as Congress, acting within the scope of those delegated powers, has created offenses against the United States. <i>Jerome</i> v. <i>United States,</i> <span class="citation" data-id="103771"><a href="/opinion/103771/jerome-v-united-states/#105" aria-description="Citation for case: Jerome v. United States">318 U.S. 101, 105</a></span>. As stated in <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/#553" aria-description="Citation for case: United States v. Cruikshank">92 U.S. 542, 553-554</a></span>, "It is no more the duty or within the power of the United States to punish for a conspiracy to falsely imprison or murder within a State, than it would be to punish for false imprisonment or murder itself." And see <i>United States</i> v. <i>Fox,</i> <span class="citation" data-id="89649"><a href="/opinion/89649/united-states-v-fox/#672" aria-description="Citation for case: United States v. Fox">95 U.S. 670, 672</a></span>. It is only state action of a "particular character" that is prohibited by the Fourteenth Amendment and against which the Amendment authorizes Congress to afford relief. <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/#11" aria-description="Citation for case: Civil Rights Cases">109 U.S. 3, 11, 13</a></span>. Thus Congress in § 20 of the Criminal Code did not undertake to make all torts of state officials federal crimes. It brought within § 20 only specified acts done "under color" of law and then only those acts which deprived a person of some right secured by the Constitution or laws of the United States.</p>
<p>This section was before us in <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#326" aria-description="Citation for case: United States v. Classic">313 U.S. 299, 326</a></span>, where we said: "Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken `under color of' state law." In that case state election officials were charged with failure to count the votes as cast, alteration of the ballots, and false certification of the number of votes cast for the respective candidates. 313 U.S. pp. 308-309. We stated that those acts of the defendants "were committed in the course of <span class="star-pagination">*110</span> their performance of duties under the Louisiana statute requiring them to count the ballots, to record the result of the count, and to certify the result of the election." <i>Id.,</i> pp. 325-326. In the present case, as we have said, the defendants were officers of the law who had made an arrest and who by their own admissions made the assault in order to protect themselves and to keep the prisoner from escaping, i.e., to make the arrest effective. That was a duty they had under Georgia law. <i>United States</i> v. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> is, therefore, indistinguishable from this case so far as "under color of" state law is concerned. In each officers of the State were performing official duties; in each the power which they were authorized to exercise was misused. We cannot draw a distinction between them unless we are to say that § 20 is not applicable to police officers. But the broad sweep of its language leaves no room for such an exception.</p>
<p>It is said that we should abandon the holding of the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case. It is suggested that the present problem was not clearly in focus in that case and that its holding was ill-advised. A reading of the opinion makes plain that the question was squarely involved and squarely met. It followed the rule announced in <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U.S. 339, 346</a></span>, that a state judge who in violation of state law discriminated against negroes in the selection of juries violated the Act of March 1, 1875, <span class="citation no-link">18 Stat. 336</span>. It is true that that statute did not contain the words under "color" of law. But the Court in deciding what was state action within the meaning of the Fourteenth Amendment held that it was immaterial that the state officer exceeded the limits of his authority. ". . . as he acts in the name and for the State, and is clothed with the State's power, his act is that of the State. This must be so, or the constitutional prohibition has no meaning. Then the State has clothed one of its agents with power to annul or to evade it." <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#347" aria-description="Citation for case: Ex Parte Virginia">100 U.S. at p. 347</a></span>. And see <i>Virginia</i> v. <i>Rives,</i> <span class="star-pagination">*111</span> <span class="citation" data-id="90040"><a href="/opinion/90040/virginia-v-rives/#321" aria-description="Citation for case: Virginia v. Rives">100 U.S. 313, 321</a></span>. The <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case recognized, without dissent, that the contrary view would defeat the great purpose which § 20 was designed to serve. Reference is made to statements<sup>[11]</sup> of Senator Trumbull in his discussion of § 2 of the Civil Rights Act of 1866, <span class="citation no-link">14 Stat. 27</span>, and to statements of Senator Sherman concerning the 1870 Act<sup>[12]</sup> as supporting the conclusion that "under color of any law" was designed to include only action taken by officials pursuant to state law. But those statements in their context are inconclusive on the precise problem involved in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case and in the present case. We are not dealing here with a case where an officer not authorized to act nevertheless takes action. Here the state officers were authorized to make an arrest and to take such steps as were necessary to make the arrest effective. They acted without authority only in the sense that they used excessive force in making the arrest effective. It is clear that under "color" of law means under "pretense" of law. Thus acts of officers in the ambit of their personal pursuits are plainly excluded. Acts of officers who undertake to perform their official duties are included whether they hew to the line of their authority or overstep it. If, as suggested, the statute was designed to embrace only action which the State in fact authorized, the words "under color of any law" were hardly apt words to express the idea.</p>
<p>Nor are the decisions under § 33 of the Judicial Code, <span class="citation no-link">28 U.S.C. § 76</span>, in point. That section gives the right of removal to a federal court of any criminal prosecution begun in a state court against a revenue officer of the United States "on account of any act done under color of his office or of any such (revenue) law." The cases under it recognize that it is an "exceptional" procedure which wrests from state courts the power to try offenses against <span class="star-pagination">*112</span> their own laws. <i>Maryland</i> v. <i>Soper</i> (<i>No. 1</i>), <span class="citation" data-id="100776"><a href="/opinion/100776/maryland-v-soper-judge/#29" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 9, 29, 35</a></span>; <i>Colorado</i> v. <i>Symes,</i> <span class="citation" data-id="101949"><a href="/opinion/101949/colorado-v-symes/#518" aria-description="Citation for case: Colorado v. Symes">286 U.S. 510, 518</a></span>. Thus the requirements of the showing necessary for removal are strict. See <i>Maryland</i> v. <i>Soper</i> (<i>No. 2</i>), <span class="citation" data-id="1410732"><a href="/opinion/1410732/maryland-v-soper-judge/#42" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 36, 42</a></span>, saying that acts "necessary to make the enforcement effective" are done under "color" of law. Hence those cases do not supply an authoritative guide to the problems under § 20 which seeks to afford protection against officers who possess authority to act and who exercise their powers in such a way as to deprive a person of rights secured to him by the Constitution or laws of the United States. It is one thing to deprive state courts of their authority to enforce their own laws. It is quite another to emasculate an Act of Congress designed to secure individuals their constitutional rights by finely spun distinctions concerning the precise scope of the authority of officers of the law. Cf. <i>Yick Wo</i> v. <i>Hopkins,</i> <span class="citation" data-id="91704"><a href="/opinion/91704/yick-wo-v-hopkins/" aria-description="Citation for case: Yick Wo v. Hopkins">118 U.S. 356</a></span>.</p>
<p>But beyond that is the problem of <i>stare decisis.</i> The construction given § 20 in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case formulated a rule of law which has become the basis of federal enforcement in this important field. The rule adopted in that case was formulated after mature consideration. It should be good for more than one day only. We do not have here a situation comparable to <i>Mahnich</i> v. <i>Southern S.S. Co.,</i> <span class="citation" data-id="103927"><a href="/opinion/103927/mahnich-v-southern-steamship-co/" aria-description="Citation for case: Mahnich v. Southern Steamship Co.">321 U.S. 96</a></span>, where we overruled a decision demonstrated to be a sport in the law and inconsistent with what preceded and what followed. The <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case was not the product of hasty action or inadvertence. It was not out of line with the cases which preceded. It was designed to fashion the governing rule of law in this important field. We are not dealing with constitutional interpretations which throughout the history of the Court have wisely remained flexible and subject to frequent re-examination. The meaning which the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case gave to the phrase "under color of any law" involved only a construction of the statute. Hence if it states a rule undesirable <span class="star-pagination">*113</span> in its consequences, Congress can change it. We add only to the instability and uncertainty of the law if we revise the meaning of § 20 to meet the exigencies of each case coming before us.</p>
<p>Since there must be a new trial, the judgment below is</p>
<p><i>Reversed.</i></p>
<p id="rutconcur">MR. JUSTICE RUTLEDGE, concurring in the result.</p>
<p>For the compelling reason stated at the end of this opinion I concur in reversing the judgment and remanding the cause for further proceedings. But for that reason, my views would require that my vote be cast to affirm the judgment, for the reasons stated by MR. JUSTICE MURPHY and others I feel forced, in the peculiar situation, to state.</p>
<p>The case comes here established in fact as a gross abuse of authority by state officers. Entrusted with the state's power and using it, without a warrant or with one of only doubtful legality<sup>[1]</sup> they invaded a citizen's home, arrested him for alleged theft of a tire, forcibly took him in handcuffs to the courthouse yard, and there beat him to death. Previously they had threatened to kill him, fortified themselves at a near-by bar, and resisted the bartender's importunities not to carry out the arrest. Upon this and other evidence which overwhelmingly supports (<span class="citation" data-id="9653538"><a href="/opinion/1567036/screws-v-united-states/#665" aria-description="Citation for case: Screws v. United States">140 F.2d at 665</a></span>) the verdict, together with instructions adequately <span class="star-pagination">*114</span> covering an officer's right to use force, the jury found the petitioners guilty.</p>
<p></p>
<h2>I</h2>
<p>The verdict has shaped their position here. Their contention hardly disputes the facts on which it rests.<sup>[2]</sup> They do not come therefore as faithful state officers, innocent of crime. Justification has been foreclosed. Accordingly, their argument now admits the offense, but insists it was against the state alone, not the nation. So they have made their case in this Court.<sup>[3]</sup></p>
<p>In effect, the position urges it is murder they have done,<sup>[4]</sup> not deprivation of constitutional right. Strange as the argument is the reason. It comes to this, that abuse of state power creates immunity to federal power. Because what they did violated the state's laws, the nation cannot reach their conduct.<sup>[5]</sup> It may deprive the citizen of his liberty and his life. But whatever state officers may do in abuse of their official capacity can give this Government and its courts no concern. This, though the prime object of the Fourteenth Amendment and § 20 was to secure these fundamental rights against wrongful denial by exercise of the power of the states.</p>
<p>The defense is not pretty. Nor is it valid. By a long course of decision from <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/" aria-description="Citation for case: Ex Parte Virginia">100 U.S. 339</a></span>, to <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U.S. 299</a></span>, it has been rejected.<sup>[6]</sup><span class="star-pagination">*115</span> The ground should not need ploughing again. It was cleared long ago and thoroughly. It has been kept clear, until the ancient doubt, laid in the beginning, was resurrected in the last stage of this case. The evidence has nullified any pretense that petitioners acted as individuals, about their personal though nefarious business. They used the power of official place in all that was done. The verdict has foreclosed semblance of any claim that only private matters, not touching official functions, were involved. Yet neither was the state's power, they say.</p>
<p>There is no third category. The Amendment and the legislation were not aimed at rightful state action. Abuse of state power was the target. Limits were put to state authority, and states were forbidden to pass them, by whatever agency.<sup>[7]</sup> It is too late now, if there were better reason than exists for doing so, to question that in these matters abuse binds the state and is its act, when done by <span class="star-pagination">*116</span> one to whom it has given power to make the abuse effective to achieve the forbidden ends. Vague ideas of dual federalism,<sup>[8]</sup> of ultra vires doctrine imported from private agency,<sup>[9]</sup> and of want of finality in official action,<sup>[10]</sup> do not nullify what four years of civil strife secured and eighty years have verified. For it was abuse of basic civil and political rights, by states and their officials, that the Amendment and the enforcing legislation were adopted to uproot.</p>
<p>The danger was not merely legislative or judicial. Nor was it threatened only from the state's highest officials. It was abuse by whatever agency the state might invest with its power capable of inflicting the deprivation. In all its flux, time makes some things axiomatic. One has been that state officials who violate their oaths of office and flout <span class="star-pagination">*117</span> the fundamental law are answerable to it when their misconduct brings upon them the penalty it authorizes and Congress has provided.</p>
<p>There could be no clearer violation of the Amendment or the statute. No act could be more final or complete, to denude the victim of rights secured by the Amendment's very terms. Those rights so destroyed cannot be restored. Nor could the part played by the state's power in causing their destruction be lessened, though other organs were now to repudiate what was done. The state's law might thus be vindicated. If so, the vindication could only sustain, it could not detract from the federal power. Nor could it restore what the federal power shielded. Neither acquittal nor conviction, though affirmed by the state's highest court, could resurrect what the wrongful use of state power has annihilated. There was in this case abuse of state power, which for the Amendment's great purposes was state action, final in the last degree, depriving the victim of his liberty and his life without due process of law.</p>
<p>If the issues made by the parties themselves were allowed to govern, there would be no need to say more. At various stages petitioners have sought to show that they used no more force than was necessary, that there was no state action, and that the evidence was not sufficient to sustain the verdict and the judgment. These issues, in various formulations,<sup>[11]</sup> have comprehended their case. All have been resolved against them without error. This should end the matter.</p>
<p></p>
<h2>
<span class="star-pagination">*118</span> II</h2>
<p>But other and most important issues have been injected and made decisive to reverse the judgment. Petitioners have not denied that they acted "willfully" within the meaning of § 20 or that they intended to do the acts which took their victim's liberty and life. In the trial court they claimed justification. But they were unable to prove it. The verdict, on overwhelming evidence, has concluded against them their denial of bad purpose and reckless disregard of rights. This is necessarily implied in the finding that excessive force was used. No complaint was made of the charge in any of these respects and no request for additional charges concerning them was offered. Nor, in the application for certiorari or the briefs, have they raised questions of the requisite criminal intent or of unconstitutional vagueness in the statute's definition of the crime. However, these issues have been brought forward, so far as the record discloses, first by the dissenting opinion in the Court of Appeals, then by inquiry at the argument and in the disposition here.</p>
<p>The story would be too long, to trace in more than outline the history of § 20 and companion provisions, in particular § 19,<sup>[12]</sup> with which it must be considered on any suggestion of fatal ambiguity. But this history cannot be ignored, unless we would risk throwing overboard what the nation's greatest internal conflict created and eight <span class="star-pagination">*119</span> decades have confirmed, in protection of individual rights against impairment by the states.</p>
<p>Sections 19 and 20 are twin sections in all respects that concern any question of vagueness in defining the crimes. There are important differences. Section 19 strikes at conspiracies, § 20 at substantive offenses. The former protects "citizens," the latter "inhabitants." There are, however, no differences in the basic rights guarded. Each protects in a different way the rights and privileges secured to individuals by the Constitution. If one falls for vagueness in pointing to these, the other also must fall for the same reason. If one stands, so must both. It is not one statute therefore which we sustain or nullify. It is two.</p>
<p>The sections have stood for nearly eighty years. Nor has this been without attack for ambiguity. Together the two sections have repelled it. In 1915, one of this Court's greatest judges, speaking for it, summarily disposed of the suggestion that § 19 is invalid: "It is not open to question that this statute is constitutional. . . [It] dealt with Federal rights and with all Federal rights, and protected them in the lump . . ." <i>United States</i> v. <i>Mosley,</i> <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/#386" aria-description="Citation for case: United States v. Mosley">238 U.S. 383, 386, 387</a></span>. And in <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U.S. 299</a></span>, the Court with equal vigor reaffirmed the validity of both sections, against dissenting assault for fatal <span class="star-pagination">*120</span> ambiguity in relation to the constitutional rights then in question. These more recent pronouncements but reaffirmed earlier and repeated ones. The history should not require retelling. But old and established freedoms vanish when history is forgotten.</p>
<p>Section 20 originated in the Civil Rights Act of 1866 (<span class="citation no-link">14 Stat. 27</span>), § 19 in the Enforcement Act of 1870 (<span class="citation no-link">16 Stat. 141</span>, § 6). Their great original purpose was to strike at discrimination, particularly against Negroes, the one securing civil, the other political rights. But they were not drawn so narrowly. From the beginning § 19 protected all "citizens," § 20 "inhabitants."</p>
<p>At first § 20 secured only rights enumerated in the Civil Rights Act. The first ten years brought it, through broadening changes, to substantially its present form. Only the word "willfully" has been added since then, a change of no materiality, for the statute implied it beforehand.<sup>[13]</sup> <span class="citation no-link">35 Stat. 1092</span>. The most important change of the first decade replaced the specific enumeration of the Civil Rights Act with the present broad language covering "the deprivation of any rights, privileges, or immunities, secured or protected by the Constitution and laws of the United States." R.S. § 5510. This inclusive designation brought § 20 into conformity with § 19's original coverage of "any right or privilege secured to him by the Constitution or laws of the United States." Since then, under these generic designations, the two have been literally identical in the scope of the rights they secure. The slight difference in wording cannot be one of substance.<sup>[14]</sup></p>
<p><span class="star-pagination">*121</span> Throughout a long and varied course of application the sections have remained unimpaired on the score of vagueness in the crimes they denounce. From 1874 to today they have repelled all attacks proposed to invalidate them. None has succeeded. If time and uniform decision can give stability to statutes, these have acquired it.</p>
<p>Section 20 has not been much used, in direct application, until recently. There were however a number of early decisions.<sup>[15]</sup> Of late the section has been applied more frequently, in considerable variety of situation, against varied and vigorous attack.<sup>[16]</sup> In <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#321" aria-description="Citation for case: United States v. Classic">313 U.S. at 321</a></span>, as has been stated, this Court gave it clear-cut sanction. The opinion expressly repudiated any idea that the section, or § 19, is vitiated by ambiguity. Moreover, this was done in terms which leave no room to say that the decision was not focused upon that question.<sup>[17]</sup> True, application to Fourteenth Amendment <span class="star-pagination">*122</span> rights was reserved because the question was raised for the first time in the Government's brief filed here. 313 U.S. at 329. But the statute was sustained in application to a vast range of rights secured by the Constitution, apart from the reserved segment, as the opinion's language and the single reservation itself attest. The ruling, thus broad, could not have been inadvertent. For it was repeated concerning both sections, broadly, forcefully, and upon citation of long-established authority. And this was done in response to a vigorous dissent which made the most of the point of vagueness.<sup>[18]</sup> The point was flatly, and deliberately, rejected. The Court could not have been blinded by other issues to the import of this one.</p>
<p>The <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> decision thus cannot be put aside in this case. Nor can it be demonstrated that the rights secured by the Fourteenth Amendment are more numerous or more dubious than the aggregate encompassed by other <span class="star-pagination">*123</span> constitutional provisions. Certainly "the equal protection of the laws," guaranteed by the Amendment, is not more vague and indefinite than many rights protected by other commands.<sup>[19]</sup> The same thing is true of "the privileges or immunities of citizens of the United States." The Fifth Amendment contains a due process clause as broad in its terms restricting national power as the Fourteenth is of state power.<sup>[20]</sup> If § 20 (with § 19) is valid in general coverage of other constitutional rights, it cannot be void in the less sweeping application to Fourteenth Amendment rights. If it is valid to assure the rights "plainly and directly" secured by other provisions, it is equally valid to protect those "plainly and directly" secured by the Fourteenth Amendment, including the expressly guaranteed rights not to be deprived of life, liberty or property without due process of law. If in fact there could be any difference among the various rights protected, in view of the history it would be that the section applies more clearly to Fourteenth Amendment rights than to others. Its phrases "are all phrases of large generalities. But they are not generalities of unillumined vagueness; they are generalities circumscribed by history and appropriate to the largeness of the problems of government with which they were concerned." <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U.S. 401</a></span>, concurring opinion, p. 413.</p>
<p>Historically, the section's function and purpose have been to secure rights given by the Amendment. From the Amendment's adoption until 1874, it was Fourteenth Amendment legislation. Surely when in that year the section was expanded to include other rights these were <span class="star-pagination">*124</span> not dropped out. By giving the citizen additional security in the exercise of his voting and other political rights, which was the section's effect, unless the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case falls, Congress did not take from him the protection it previously afforded (wholly apart from the prohibition of different penalties)<sup>[21]</sup> against deprivation of such rights on account of race, color or previous condition of servitude, or repeal the prior safeguard of civil rights.</p>
<p>To strike from the statute the rights secured by the Fourteenth Amendment, but at the same time to leave within its coverage the vast area bounded by other constitutional provisions, would contradict both reason and history. No logic but one which nullifies the historic foundations of the Amendment and the section could support such an emasculation. There should be no judicial hack work cutting out some of the great rights the Amendment secures but leaving in others. There can be none excising all protected by the Amendment, but leaving <span class="star-pagination">*125</span> every other given by the Constitution intact under the statute's aegis.</p>
<p>All that has been said of § 20 applies with equal force to § 19. It had an earlier more litigious history, firmly establishing its validity.<sup>[22]</sup> It also has received recent application,<sup>[23]</sup><span class="star-pagination">*126</span> without question for ambiguity except in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case, which nevertheless gave it equal sanction with its substantive counterpart.</p>
<p>Separately, and often together in application, §§ 19 and 20 have been woven into our fundamental and statutory law. They have place among our more permanent legal achievements. They have safeguarded many rights and privileges apart from political ones. Among those buttressed, either by direct application or through the general conspiracy statute, § 37 (<span class="citation no-link">18 U.S.C. § 88</span>),<sup>[24]</sup> are the rights to a fair trial, including freedom from sham trials; to be free from arrest and detention by methods constitutionally forbidden and from extortion of property by such methods; from extortion of confessions; from mob action incited or shared by state officers; from failure to furnish police protection on proper occasion and demand; from interference with the free exercise of religion, freedom of the press, freedom of speech and assembly;<sup>[25]</sup> and <span class="star-pagination">*127</span> the necessary import of the decisions is that the right to be free from deprivation of life itself, without due process of law, that is, through abuse of state power by state officials, is as fully protected as other rights so secured.</p>
<p>So much experience cannot be swept aside, or its teaching annulled, without overthrowing a great, and a firmly established, constitutional tradition. Nor has the feared welter of uncertainty arisen. Defendants have attacked the sections, or their application, often and strenuously. Seldom has complaint been made that they are too vague and uncertain. Objections have centered principally about "state action," including "color of law" and failure by inaction to discharge official duty, cf. <i>Catlette</i> v. <i>United States,</i> <span class="citation" data-id="1480783"><a href="/opinion/1480783/catlette-v-united-states/" aria-description="Citation for case: Catlette v. United States">132 F.2d 902</a></span>, and about the strength of federal power to reach particular abuses.<sup>[26]</sup> More rarely they have touched other matters, such as the limiting effect of official privilege<sup>[27]</sup> and, in occasional instances, <i>mens rea.</i><sup>[28]</sup><span class="star-pagination">*128</span> In all this wealth of attack accused officials have little used the shield of ambiguity. The omission, like the Court's rejection in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case, cannot have been inadvertent. There are valid reasons for it, apart from the old teaching that the matter has been foreclosed.</p>
<p>One is that the generality of the section's terms simply has not worked out to be a hazard of unconstitutional, or even serious, proportions. It has not proved a source of practical difficulty. In no other way can be explained the paucity of the objection's appearance in the wealth of others made. If experience is the life of the law, as has been said, this has been true preeminently in the application of §§ 19 and 20.</p>
<p>Moreover, statutory specificity has two purposes, to give due notice that an act has been made criminal before it is done and to inform one accused of the nature of the offense charged, so that he may adequately prepare and make his defense. More than this certainly the Constitution does not require. Cf. Amend. VI. All difficulty on the latter score vanishes, under § 20, with the indictment's particularization of the rights infringed and the acts infringing them. If it is not sufficient in either respect, in these as in other cases the motion to quash or one for a bill of particulars is at the defendant's disposal. The decided cases demonstrate that accused persons have had little or no difficulty to ascertain the rights they have been charged with transgressing or the acts of transgression.<sup>[29]</sup> So it was with the defendants in this case. They were not puzzled to know for what they were indicted, as their proof and their defense upon the law conclusively show. They simply misconceived that the victim had no federal rights and that what they had done was not a crime within the federal power to penalize.<sup>[30]</sup> That kind of error relieves no one from penalty.</p>
<p><span class="star-pagination">*129</span> In the other aspect of specificity, two answers, apart from experience, suffice. One is that § 20, and § 19, are no more general and vague, Fourteenth Amendment rights included, than other criminal statutes commonly enforced against this objection. The Sherman Act is the most obvious illustration.<sup>[31]</sup></p>
<p>Furthermore, the argument of vagueness, to warn men of their conduct, ignores the nature of the criminal act itself and the notice necessarily given from this. Section 20 strikes only at abuse of official functions by state officers. It does not reach out for crimes done by men in general. Not murder per se, but murder by state officers in the course of official conduct and done with the aid of state power, is outlawed. These facts, inherent in the crime, give all the warning constitutionally required. For one, so situated, who goes so far in misconduct can have no excuse of innocence or ignorance.</p>
<p>Generally state officials know something of the individual's basic legal rights. If they do not, they should, for they assume that duty when they assume their office. Ignorance of the law is no excuse for men in general. It is less an excuse for men whose special duty is to apply it, and therefore to know and observe it. If their knowledge is not comprehensive, state officials know or should know when they pass the limits of their authority, so far at any rate that their action exceeds honest error of judgment and amounts to abuse of their office and its function. When they enter such a domain in dealing with the citizen's rights, they should do so at their peril, whether that <span class="star-pagination">*130</span> be created by state or federal law. For their sworn oath and their first duty are to uphold the Constitution, then only the law of the state which too is bound by the charter. Since the statute, as I think, condemns only something more than error of judgment, made in honest effort at once to apply and to follow the law, cf. <i>United States</i> v. <i>Murdock,</i> <span class="citation" data-id="102166"><a href="/opinion/102166/united-states-v-murdock/" aria-description="Citation for case: United States v. Murdock">290 U.S. 389</a></span>, officials who violate it must act in intentional or reckless disregard of individual rights and cannot be ignorant that they do great wrong.<sup>[32]</sup> This being true, they must be taken to act at peril of incurring the penalty placed upon such conduct by the federal law, as they do of that the state imposes.</p>
<p>What has been said supplies all the case requires to be decided on the question of criminal intent. If the criminal act is limited, as I think it must be and the statute intends, to infraction of constitutional rights, including rights secured by the Fourteenth Amendment, by conduct which amounts to abuse of one's official place or reckless disregard of duty, no undue hazard or burden can be placed on state officials honestly seeking to perform the rightful functions of their office. Others are not entitled to greater protection.</p>
<p>But, it is said, a penumbra of rights may be involved, which none can know until decision has been made and infraction may occur before it is had. It seems doubtful this could be true in any case involving the abuse of official function which the statute requires and, if it could, that one guilty of such an abuse should have immunity for that reason. Furthermore, the doubtful character of the <span class="star-pagination">*131</span> right infringed could give reason at the most to invalidate the particular charge, not for outlawing the statute or narrowly restricting its application in advance of compelling occasion.</p>
<p>For there is a body of well-established, clear-cut fundamental rights, including many secured by the Fourteenth Amendment, to all of which the sections may and do apply, without specific enumeration and without creating hazards of uncertainty for conduct or defense. Others will enter that category. So far, at the least when they have done so, the sections should stand without question of their validity. Beyond this, the character of the act proscribed and the intent it necessarily implies would seem to afford would-be violators all of notice the law requires, that they act at peril of the penalty it places on their misconduct.</p>
<p>We have in this case no instance of mere error in judgment, made in good faith. It would be time enough to reverse and remand a conviction, obtained without instructions along these lines, if such a case should arise. Actually the substance of such instruction was given in the wholly adequate charge concerning the officer's right to use force, though not to excess. When, as here, a state official abuses his place consciously or grossly in abnegation of its rightful obligation, and thereby tramples underfoot the established constitutional rights of men or citizens, his conviction should stand when he has had the fair trial and full defense the petitioners have been given in this case.</p>
<p></p>
<h2>III</h2>
<p>Two implicit but highly important considerations must be noticed more definitely. One is the fear grounded in concern for possible maladjustment of federal-state relations if this and like convictions are sustained. Enough has been said to show that the fear is not well grounded. The same fear was expressed, by some in exaggerated and <span class="star-pagination">*132</span> highly emotional terms, when § 2 of the Civil Rights Act, the antecedent of § 20, was under debate in Congress.<sup>[33]</sup> The history of the legislation's enforcement gives it no support. The fear was not realized in later experience. Eighty years should be enough to remove any remaining vestige. The volume of prosecutions and convictions has been small, in view of the importance of the subject matter and the length of time the statutes have been in force. There are reasons for this, apart from self-restraint of federal prosecuting officials.</p>
<p>One lies in the character of the criminal act and the intent which must be proved. A strong case must be made to show abuse of official function, and therefore to secure indictment or conviction. Trial must be "by an impartial jury of the State and the district wherein the crime shall have been committed." Const., Amend. VI; cf. Art. III, § 2. For all practical purposes this means within the state of which the accused is an officer. Citizens of the state have not been, and will not be, ready to indict or convict their local officers on groundless charges or in doubtful cases. The sections can be applied effectively only when twelve of them concur in a verdict which accords with the prosecuting official's belief that the accused has violated another's fundamental rights. A federal official therefore faces both a delicate and a difficult task when he undertakes to charge and try a state officer under the terms of §§ 19 and 20. The restraint which has been shown is as much enforced by these limitations as it has been voluntary.</p>
<p><span class="star-pagination">*133</span> These are the reasons why prosecution has not been frequent, has been brought only in cases of gross abuse, and therefore has produced no grave or substantial problem of interference by federal authority in state affairs. But if the problem in this phase of the case were more serious than it has been or is likely to be, the result legally could not be to give state officials immunity from the obligations and liabilities the Amendment and its supporting legislation have imposed. For the verdict of the struggle which brought about adoption of the Amendment was to the contrary.</p>
<p>Lying beneath all the surface arguments is a deeper implication, which comprehends them. It goes to federal power. It is that Congress could not in so many words denounce as a federal crime the intentional and wrongful taking of an individual's life or liberty by a state official acting in abuse of his official function and applying to the deed all the power of his office. This is the ultimate purport of the notions that state action is not involved and that the crime is against the state alone, not the nation. It is reflected also in the idea that the statute can protect the victim in his many procedural rights encompassed in the right to a fair trial before condemnation, but cannot protect him in the right which comprehends all others, the right to life itself.</p>
<p>Suffice it to say that if these ideas did not pass from the American scene once and for all, as I think they did, upon adoption of the Amendment without more, they have long since done so. Violation of state law there may be. But from this no immunity to federal authority can arise where any part of the Constitution has made it supreme. To the Constitution state officials and the states themselves owe first obligation. The federal power lacks no strength to reach their malfeasance in office when it infringes constitutional rights. If that is a great power, it is one generated by the Constitution and the Amendments, <span class="star-pagination">*134</span> to which the states have assented and their officials owe prime allegiance.<sup>[34]</sup></p>
<p>The right not to be deprived of life or liberty by a state officer who takes it by abuse of his office and its power is such a right. To secure these rights is not beyond federal power. This §§ 19 and 20 have done, in a manner history long since has validated.</p>
<p>Accordingly, I would affirm the judgment.</p>
<p>My convictions are as I have stated them. Were it possible for me to adhere to them in my vote, and for the Court at the same time to dispose of the cause, I would act accordingly. The Court, however, is divided in opinion. If each member accords his vote to his belief, the case cannot have disposition. Stalemate should not prevail for any reason, however compelling, in a criminal cause or, if avoidable, in any other. My views concerning appropriate disposition are more nearly in accord with those stated by MR. JUSTICE DOUGLAS, in which three other members of the Court concur, than they are with the views of my dissenting brethren who favor outright reversal. Accordingly, in order that disposition may be made of this case, my vote has been cast to reverse the decision of the Court of Appeals and remand the cause to the District Court for further proceedings in accordance with the disposition required by the opinion of MR. JUSTICE DOUGLAS.</p>
<p>MR. JUSTICE MURPHY, dissenting.</p>
<p>I dissent. Robert Hall, a Negro citizen, has been deprived not only of the right to be tried by a court rather than by ordeal. He has been deprived of the right to life itself. That right belonged to him not because he was a Negro or a member of any particular race or creed. That right was his because he was an American citizen, because <span class="star-pagination">*135</span> he was a human being. As such, he was entitled to all the respect and fair treatment that befits the dignity of man, a dignity that is recognized and guaranteed by the Constitution. Yet not even the semblance of due process has been accorded him. He has been cruelly and unjustifiably beaten to death by local police officers acting under color of authority derived from the state. It is difficult to believe that such an obvious and necessary right is indefinitely guaranteed by the Constitution or is foreign to the knowledge of local police officers so as to cast any reasonable doubt on the conviction under § 20 of the Criminal Code of the perpetrators of this "shocking and revolting episode in law enforcement."</p>
<p>The Constitution and § 20 must be read together inasmuch as § 20 refers in part to certain provisions of the Constitution. Section 20 punishes anyone, acting under color of any law, who willfully deprives any person of any right, privilege or immunity secured or protected by the Constitution or laws of the United States. The pertinent part of the Constitution in this instance is § 1 of the Fourteenth Amendment, which firmly and unmistakably provides that no state shall deprive any person of life without due process of law. Translated in light of this specific provision of the Fourteenth Amendment, § 20 thus punishes anyone, acting under color of state law, who willfully deprives any person of life without due process of law. Such is the clear statutory provision upon which this conviction must stand or fall.</p>
<p>A grave constitutional issue, however, is said to lurk in the alleged indefiniteness of the crime outlawed by § 20. The rights, privileges and immunities secured or protected by the Constitution or laws of the United States are claimed to be so uncertain and flexible, dependent upon changeable legal concepts, as to leave a state official confused and ignorant as to what actions of his might run afoul of the law. The statute, it is concluded, must be set aside for vagueness.</p>
<p><span class="star-pagination">*136</span> It is axiomatic, of course, that a criminal statute must give a clear and unmistakable warning as to the acts which will subject one to criminal punishment. And courts are without power to supply that which Congress has left vague. But this salutary principle does not mean that if a statute is vague as to certain criminal acts but definite as to others the entire statute must fall. Nor does it mean that in the first case involving the statute to come before us we must delineate all the prohibited acts that are obscure and all those that are explicit.</p>
<p>Thus it is idle to speculate on other situations that might involve § 20 which are not now before us. We are unconcerned here with state officials who have coerced a confession from a prisoner, denied counsel to a defendant or made a faulty tax assessment. Whatever doubt may exist in those or in other situations as to whether the state officials could reasonably anticipate and recognize the relevant constitutional rights is immaterial in this case. Our attention here is directed solely to three state officials who, in the course of their official duties, have unjustifiably beaten and crushed the body of a human being, thereby depriving him of trial by jury and of life itself. The only pertinent inquiry is whether § 20, by its reference to the Fourteenth Amendment guarantee that no state shall deprive any person of life without due process of law, gives fair warning to state officials that they are criminally liable for violating this right to life.</p>
<p>Common sense gives an affirmative answer to that problem. The reference in § 20 to rights protected by the Constitution is manifest and simple. At the same time, the right not to be deprived of life without due process of law is distinctly and lucidly protected by the Fourteenth Amendment. There is nothing vague or indefinite in these references to this most basic of all human rights. Knowledge of a comprehensive law library is unnecessary for officers of the law to know that the right to murder <span class="star-pagination">*137</span> individuals in the course of their duties is unrecognized in this nation. No appreciable amount of intelligence or conjecture on the part of the lowliest state official is needed for him to realize that fact; nor should it surprise him to find out that the Constitution protects persons from his reckless disregard of human life and that statutes punish him therefor. To subject a state official to punishment under § 20 for such acts is not to penalize him without fair and definite warning. Rather it is to uphold elementary standards of decency and to make American principles of law and our constitutional guarantees mean something more than pious rhetoric.</p>
<p>Under these circumstances it is unnecessary to send this case back for a further trial on the assumption that the jury was not charged on the matter of the willfulness of the state officials, an issue that was not raised below or before us. The evidence is more than convincing that the officials willfully, or at least with wanton disregard of the consequences, deprived Robert Hall of his life without due process of law. A new trial could hardly make that fact more evident; the failure to charge the jury on willfulness was at most an inconsequential error. Moreover, the presence or absence of willfulness fails to decide the constitutional issue raised before us. Section 20 is very definite and certain in its reference to the right to life as spelled out in the Fourteenth Amendment quite apart from the state of mind of the state officials. A finding of willfulness can add nothing to the clarity of that reference.</p>
<p>It is an illusion to say that the real issue in this case is the alleged failure of § 20 fully to warn the state officials that their actions were illegal. The Constitution, § 20 and their own consciences told them that. They knew that they lacked any mandate or authority to take human life unnecessarily or without due process of law in the course of their duties. They knew that their excessive and abusive <span class="star-pagination">*138</span> use of authority would only subvert the ends of justice. The significant question, rather, is whether law enforcement officers and those entrusted with authority shall be allowed to violate with impunity the clear constitutional rights of the inarticulate and the friendless. Too often unpopular minorities, such as Negroes, are unable to find effective refuge from the cruelties of bigoted and ruthless authority. States are undoubtedly capable of punishing their officers who commit such outrages. But where, as here, the states are unwilling for some reason to prosecute such crimes the federal government must step in unless constitutional guarantees are to become atrophied.</p>
<p>This necessary intervention, however, will be futile if courts disregard reality and misuse the principle that criminal statutes must be clear and definite. Here state officers have violated with reckless abandon a plain constitutional right of an American citizen. The two courts below have found and the record demonstrates that the trial was fair and the evidence of guilt clear. And § 20 unmistakably outlaws such actions by state officers. We should therefore affirm the judgment.</p>
<p id="frankdissent">MR. JUSTICE ROBERTS, MR. JUSTICE FRANKFURTER and MR. JUSTICE JACKSON, dissenting.</p>
<p>Three law enforcement officers of Georgia, a county sheriff, a special deputy and a city policeman, arrested a young Negro charged with a local crime, that of stealing a tire. While he was in their custody and handcuffed, they so severely beat the lad that he died. This brutal misconduct rendered these lawless law officers guilty of manslaughter, if not of murder, under Georgia law. Instead of leaving this misdeed to vindication by Georgia law, the United States deflected Georgia's responsibility by instituting a federal prosecution. But this was a criminal homicide only under Georgia law. The United States could not prosecute the petitioners for taking life. Instead <span class="star-pagination">*139</span> a prosecution was brought, and the conviction now under review was obtained, under § 20 of the Criminal Code, <span class="citation no-link">18 U.S.C. § 52</span>. Section 20, originating in § 2 of the Civil Rights Act of April 9, 1866, <span class="citation no-link">14 Stat. 27</span>, was put on the statute books on May 31, 1870, but for all practical purposes it has remained a dead letter all these years. This section provides that "Whoever, under color of any law, statute, ordinance, regulation, or custom, willfully subjects . . . any inhabitant of any State . .. to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution and laws of the United States . . . shall be fined not more than one thousand dollars, or imprisoned not more than one year, or both." Under § 37 of the Criminal Code, <span class="citation no-link">18 U.S.C. § 88</span>, a conspiracy to commit any federal offense is punishable by imprisonment for two years. The theory of this prosecution is that one charged with crime is entitled to due process of law and that that includes the right to an orderly trial of which the petitioners deprived the Negro.</p>
<p>Of course the petitioners are punishable. The only issue is whether Georgia alone has the power and duty to punish, or whether this patently local crime can be made the basis of a federal prosecution. The practical question is whether the States should be relieved from responsibility to bring their law officers to book for homicide, by allowing prosecutions in the federal courts for a relatively minor offense carrying a short sentence. The legal question is whether, for the purpose of accomplishing this relaxation of State responsibility, hitherto settled principles for the protection of civil liberties shall be bent and tortured.</p>
<p></p>
<h2>I</h2>
<p>By the Thirteenth Amendment slavery was abolished. In order to secure equality of treatment for the emancipated, the Fourteenth Amendment was adopted at the <span class="star-pagination">*140</span> same time. To be sure, the latter Amendment has not been confined to instances of discrimination because of race or color. Undoubtedly, however, the necessary protection of the new freedmen was the most powerful impulse behind the Fourteenth Amendment. The vital part of that Amendment, § 1, reads as follows:</p>
<p>"All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside. No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws."</p>
<p>By itself, this Amendment is merely an instrument for striking down action by the States in defiance of it. It does not create rights and obligations actively enforceable by federal law. However, like all rights secured by the Constitution of the United States, those created by the Fourteenth Amendment could be enforced by appropriate federal legislation. The general power of Congress to pass measures effectuating the Constitution is given by Art. I, § 8, cl. 18  the Necessary-and-Proper Clause. In order to indicate the importance of enforcing the guarantees of Amendment XIV, its fifth section specifically provides: "The Congress shall have power to enforce, by appropriate legislation, the provisions of this article."</p>
<p>Accordingly, Congress passed various measures for its enforcement. It is familiar history that much of this legislation was born of that vengeful spirit which to no small degree envenomed the Reconstruction era. Legislative respect for constitutional limitations was not at its height and Congress passed laws clearly unconstitutional. See <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/" aria-description="Citation for case: Civil Rights Cases">109 U.S. 3</a></span>. One of the laws of this period was the Act of May 31, 1870, <span class="citation no-link">16 Stat. 140</span>. In its <span class="star-pagination">*141</span> present form, as § 20, it is now here for the first time on full consideration as to its meaning and its constitutionality, unembarrassed by preoccupation both on the part of counsel and Court with the more compelling issue of the power of Congress to control State procedure for the election of federal officers. If § 20 were read as other legislation is read, by giving it the meaning which its language in its proper setting naturally and spontaneously yields, it is difficult to believe that there would be real doubt about the proper construction. The unstrained significance of the words chosen by Congress, the disclosed purpose for which they were chosen and to which they were limited, the always relevant implications of our federal system especially in the distribution of power and responsibility for the enforcement of the criminal law as between the States and the National Government, all converge to make plain what conduct Congress outlawed by the Act of 1870 and what impliedly it did not.</p>
<p>The Fourteenth Amendment prohibited a State from so acting as to deprive persons of new federal rights defined by it. Section 5 of the Amendment specifically authorized enabling legislation to enforce that prohibition. Since a State can act only through its officers, Congress provided for the prosecution of any officer who deprives others of their guaranteed rights and denied such an officer the right to defend by claiming the authority of the State for his action. In short, Congress said that no State can empower an officer to commit acts which the Constitution forbade the State from authorizing, whether such unauthorized command be given for the State by its legislative or judicial voice, or by a custom contradicting the written law. See <i>Nashville, C. &amp; St. L.R. Co.</i> v. <i>Browning,</i> <span class="citation" data-id="103360"><a href="/opinion/103360/nashville-chattanooga-st-louis-railway-v-browning/#369" aria-description="Citation for case: Nashville, Chattanooga &amp; St. Louis Railway v. Browning">310 U.S. 362, 369</a></span>. The present prosecution is not based on an officer's claim that that for which the United States seeks his punishment was commanded or authorized by the law of his State. On the contrary, <span class="star-pagination">*142</span> the present prosecution is based on the theory that Congress made it a federal offense for a State officer to violate the explicit law of his State. We are asked to construe legislation which was intended to effectuate prohibitions against States for defiance of the Constitution, to be equally applicable where a State duly obeys the Constitution, but an officer flouts State law and is unquestionably subject to punishment by the State for his disobedience.</p>
<p>So to read § 20 disregards not merely the normal function of language to express ideas appropriately. It fails not merely to leave to the States the province of local crime enforcement, that the proper balance of political forces in our federalism requires. It does both, heedless of the Congressional purpose, clearly evinced even during the feverish Reconstruction days, to leave undisturbed the power and the duty of the States to enforce their criminal law by restricting federal authority to the punishment only of those persons who violate federal rights under claim of State authority and not by exerting federal authority against offenders of State authority. Such a distortion of federal power devised against recalcitrant State authority never entered the minds of the proponents of the legislation.</p>
<p>Indeed, we have the weightiest evidence to indicate that they rejected that which now, after seventy-five years, the Government urges. Section 20 of the Criminal Code derived from § 2 of the Civil Rights Act of 1866, <span class="citation no-link">14 Stat. 27</span>. During the debate on that section, Senator Trumbull, the Chairman of the Senate Judiciary Committee, answered fears concerning the loose inclusiveness of the phrase "color of law." In particular, opponents of the Act were troubled lest it would make criminals of State judges and officials for carrying out their legal duties. Senator Trumbull agreed that they would be guilty if they consciously helped to enforce discriminatory State <span class="star-pagination">*143</span> legislation. Federal law, replied Senator Trumbull, was directed against those, and only against those, who were not punishable by State law precisely because they acted in obedience to unconstitutional State law and by State law justified their action. Said Senator Trumbull, "If an offense is committed against a colored person simply because he is colored, in a State where the law affords him the same protection as if he were white, this act neither has nor was intended to have anything to do with his case, because he has adequate remedies in the State courts; but if he is discriminated against under color of State laws because he is colored, then it becomes necessary to interfere for his protection." Cong. Globe, 39th Cong., 1st Sess., p. 1758. And this language applies equally to § 17 of the Act of May 31, 1870, <span class="citation no-link">16 Stat. 140</span>, 144 (now § 20 of the Criminal Code), which reenacted the Civil Rights Act.</p>
<p>That this legislation was confined to attempted deprivations of federal rights by State law and was not extended to breaches of State law by its officials, is likewise confirmed by observations of Senator Sherman, another leading Reconstruction statesman. When asked about the applicability of the 1870 Act to a Negro's right to vote when State law provided for that right, Senator Sherman replied, "That is not the case with which we are dealing. I intend to propose an amendment to present a question of that kind. This bill only proposes to deal with offenses committed by officers or persons under color of existing State law, under color of existing State constitutions. No man could be convicted under this bill reported by the Judiciary Committee unless the denial of the right to vote was done under color or pretense of State regulation. The whole bill shows that. My honorable friend from California has not read this bill with his usual care if he does not see that that runs through the whole of the provisions of the first and second sections of the bill, which <span class="star-pagination">*144</span> simply punish officers as well as persons for discrimination under color of State laws or constitutions; and so it provides all the way through." Cong. Globe, 41st Cong., 2d Sess., p. 3663. The debates in Congress are barren of any indication that the supporters of the legislation now before us had the remotest notion of authorizing the National Government to prosecute State officers for conduct which their State had made a State offense where the settled custom of the State did not run counter to formulated law.</p>
<p>Were it otherwise it would indeed be surprising. It was natural to give the shelter of the Constitution to those basic human rights for the vindication of which the successful conduct of the Civil War was the end of a long process. And the extension of federal authority so as to guard against evasion by any State of these newly created federal rights was an obvious corollary. But to attribute to Congress the making overnight of a revolutionary change in the balance of the political relations between the National Government and the States without reason, is a very different thing. And to have provided for the National Government to take over the administration of criminal justice from the States to the extent of making every lawless act of the policeman on the beat or in the station house, whether by way of third degree or the illegal ransacking for evidence in a man's house (see <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>; <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>; <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U.S. 278</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227</a></span>), a federal offense, would have constituted a revolutionary break with the past overnight. The desire for such a dislocation in our federal system plainly was not contemplated by the Lyman Trumbulls and the John Shermans, and not even by the Thaddeus Stevenses.</p>
<p>Regard for maintaining the delicate balance "between the judicial tribunals of the Union and of the States" in <span class="star-pagination">*145</span> the enforcement of the criminal law has informed this Court, as it has influenced Congress, "in recognition of the fact that the public good requires that those relations be not disturbed by unnecessary conflict between courts equally bound to guard and protect rights secured by the Constitution." <i>Ex parte Royall,</i> <span class="citation" data-id="91598"><a href="/opinion/91598/ex-parte-royall/#251" aria-description="Citation for case: Ex Parte Royall">117 U.S. 241, 251</a></span>. Observance of this basic principle under our system of Government has led this Court to abstain, even under more tempting circumstances than those now here, from needless extension of federal criminal authority into matters that normally are of State concern and for which the States had best be charged with responsibility.</p>
<p>We have reference to § 33 of the Judicial Code, as amended, <span class="citation no-link">28 U.S.C. § 76</span>. That provision gives the right of removal to a federal court of any criminal prosecution begun in a State court against a revenue officer of the United States "on account of any act done under color of his office or of any such [revenue] law." Where a State prosecution for manslaughter is resisted by the claim that what was done was justifiably done by a United States officer one would suppose that this Court would be alert to construe very broadly "under color of his office or of any such law" in order to avoid the hazards of trial, whether through conscious or unconscious discrimination or hostility, of a United States officer accused of homicide and to assure him a trial in a presumably more impartial federal court. But this Court long ago indicated that misuse of federal authority does not come within the statute's protection. <i>Tennessee</i> v. <i>Davis,</i> <span class="citation" data-id="90038"><a href="/opinion/90038/tennessee-v-davis/#261" aria-description="Citation for case: Tennessee v. Davis">100 U.S. 257, 261-262</a></span>. More recently, this Court in a series of cases unanimously insisted that a petition for removal must show with particularity that the offense for which the State is prosecuting resulted from a discharge of federal duty. "It must appear that the prosecution of him, for whatever offense, has arisen out of the acts done by him under color of federal authority and in enforcement of federal law, and <span class="star-pagination">*146</span> he must by direct averment exclude the possibility that it was based on acts or conduct of his not justified by his federal duty. . . . The defense he is to make is that of his immunity from punishment by the State, because what he did was justified by his duty under the federal law, and because he did nothing else on which the prosecution could be based." <i>Maryland</i> v. <i>Soper</i> (No. 1), <span class="citation" data-id="100776"><a href="/opinion/100776/maryland-v-soper-judge/#33" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 9, 33</a></span>. And see <i>Maryland</i> v. <i>Soper</i> (No. 2), <span class="citation" data-id="1410732"><a href="/opinion/1410732/maryland-v-soper-judge/" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 36</a></span>; <i>Maryland</i> v. <i>Soper</i> (No. 3), <span class="citation" data-id="1410842"><a href="/opinion/1410842/maryland-v-soper-no-3/" aria-description="Citation for case: Maryland v. Soper (No. 3)">270 U.S. 44</a></span>; <i>Colorado</i> v. <i>Symes,</i> <span class="citation" data-id="101949"><a href="/opinion/101949/colorado-v-symes/" aria-description="Citation for case: Colorado v. Symes">286 U.S. 510</a></span>. To the suggestion that such a limited construction of the removal statute enacted for the protection of the United States officers would restrict its effectiveness, the answer was that if Congress chose to afford even greater protection and to withdraw from the States the right and duty to enforce their criminal law in their own courts, it should express its desire more specifically. <i>Maryland</i> v. <i>Soper</i> (No. 2), <span class="citation" data-id="1410732"><a href="/opinion/1410732/maryland-v-soper-judge/#42" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 36, 42, 44</a></span>. That answer should be binding in the situation now before us.</p>
<p>The reasons which led this Court to give such a retricted scope to the removal statute are even more compelling as to § 20. The matter concerns policies inherent in our federal system and the undesirable consequences of federal prosecution for crimes which are obviously and predominantly State crimes no matter how much sophisticated argumentation may give them the appearance of federal crimes. Congress has not expressed a contrary purpose, either by the language of its legislation or by anything appearing in the environment out of which its language came. The practice of government for seventy-five years likewise speaks against it. Nor is there a body of judicial opinion which bids us find in the unbridled excess of a State officer, constituting a crime under his State law, action taken "under color of law" which federal law forbids.</p>
<p>Only two reported cases considered § 20 before <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U.S. 299</a></span>. In <i>United States</i> v. <i>Buntin,</i> <span class="star-pagination">*147</span> <span class="citation" data-id="8122539"><a href="/opinion/8160884/united-states-v-buntin/" aria-description="Citation for case: United States v. Buntin">10 F. 730</a></span>, a teacher, in reliance on a State statute, refused admittance to a colored child, while in <i>United States</i> v. <i>Stone,</i> <span class="citation" data-id="8779667"><a href="/opinion/8795605/united-states-v-stone/" aria-description="Citation for case: United States v. Stone">188 F. 836</a></span>, election supervisors who acted under a Maryland election law were held to act "under color of law." In neither case was there a patent violation of State law but rather an attempt at justification under State law. <i>United States</i> v. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic, supra</a></span></i><i>,</i> is the only decision that looks the other way. In that case primary election officials were held to have acted "under color of law" even though the acts complained of as a federal offense were likewise condemned by Louisiana law. The truth of the matter is that the focus of attention in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case was not our present problem, but was the relation of primaries to the protection of the electoral process under the United States Constitution. The views in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case thus reached ought not to stand in the way of a decision on the merits of a question which has now for the first time been fully explored and its implications for the workings of our federal system have been adequately revealed.</p>
<p>It was assumed quite needlessly in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case that the scope of § 20 was coextensive with the Fourteenth Amendment. Because the weight of the case was elsewhere, we did not pursue the difference between the power granted to Congress by that Amendment to bar "any State" from depriving persons of the newly created constitutional rights and the limited extent to which Congress exercised that power, in what is now § 20, by making it an offense for one acting "under color of any law" to deprive another of such constitutional rights. It may well be that Congress could, within the bounds of the Fourteenth Amendment, treat action taken by a State official even though in defiance of State law and not condoned by ultimate State authority as the action of "a State." It has never been satisfactorily explained how a State can be said to deprive a person of liberty or property without <span class="star-pagination">*148</span> due process of law when the foundation of the claim is that a minor official has disobeyed the authentic command of his State. See <i>Raymond</i> v. <i>Chicago Traction Co.,</i> <span class="citation" data-id="96704"><a href="/opinion/96704/raymondv-v-chicago-union-traction-co/#40" aria-description="Citation for case: Raymondv v. Chicago Union Traction Co.">207 U.S. 20, 40, 41</a></span>. Although action taken under such circumstances has been deemed to be deprivation by a "State" of rights guaranteed by the Fourteenth Amendment for purposes of federal jurisdiction, the doctrine has had a fluctuating and dubious history. Compare <i>Barney</i> v. <i>City of New York,</i> <span class="citation" data-id="96036"><a href="/opinion/96036/barney-v-city-of-new-york/" aria-description="Citation for case: Barney v. City of New York">193 U.S. 430</a></span>, with <i>Raymond</i> v. <i>Chicago Traction Co., supra</i><i>; </i><i>Memphis</i> v. <i>Cumberland Telephone Co.,</i> <span class="citation" data-id="9418191"><a href="/opinion/97326/city-of-memphis-v-cumberland-telephone-telegraph-co/" aria-description="Citation for case: City of Memphis v. Cumberland Telephone &amp; Telegraph Co.">218 U.S. 624</a></span>, with <i>Home Tel. &amp; Tel. Co.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">227 U.S. 278</a></span>. <i>Barney</i> v. <i>City of New York, supra</i><i>,</i> which ruled otherwise, although questioned, has never been overruled. See, for instance, <i>Iowa-Des Moines Bank</i> v. <i>Bennett,</i> <span class="citation" data-id="101816"><a href="/opinion/101816/iowa-des-moines-national-bank-v-bennett/#246" aria-description="Citation for case: Iowa-Des Moines National Bank v. Bennett">284 U.S. 239, 246-247</a></span>, and <i>Snowden</i> v. <i>Hughes,</i> <span class="citation" data-id="9419429"><a href="/opinion/103921/snowden-v-hughes/#13" aria-description="Citation for case: Snowden v. Hughes">321 U.S. 1, 13</a></span>.<sup>[1]</sup></p>
<p>But assuming unreservedly that conduct such as that now before us, perpetrated by State officers in flagrant defiance of State law, may be attributed to the State under the Fourteenth Amendment, this does not make it action under "color of any law." Section 20 is much narrower than the power of Congress. Even though Congress might have swept within the federal criminal law any action that could be deemed within the vast reach of the Fourteenth Amendment, Congress did not do so. The presuppositions of our federal system, the pronouncements of the statesmen who shaped this legislation, and the normal meaning of language powerfully counsel against attributing to Congress intrusion into the sphere of criminal law traditionally <span class="star-pagination">*149</span> and naturally reserved for the States alone. When due account is taken of the considerations that have heretofore controlled the political and legal relations between the States and the National Government, there is not the slightest warrant in the reason of things for torturing language plainly designed for nullifying a claim of acting under a State law that conflicts with the Constitution so as to apply to situations where State law is in conformity with the Constitution and local misconduct is in undisputed violation of that State law. In the absence of clear direction by Congress we should leave to the States the enforcement of their criminal law, and not relieve States of the responsibility for vindicating wrongdoing that is essentially local or weaken the habits of local law enforcement by tempting reliance on federal authority for an occasional unpleasan

[...TRUNCATED 68811 of 188811 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Sgro v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Sgro v. United States"
type: case
citation: "287 U.S. 206 (1932)"
parallel_cite: "53 S. Ct. 138; 77 L. Ed. 260; 85 A.L.R. 108"
neutral_cite: 1932 U.S. LEXIS 13
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1932
date_decided: 1932-12-05
docket: 55
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1932-12-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Sgro v. United States
  varies_by_point: false
  scope_note: "Foundational warrant-staleness / prompt-execution holding; the principle that a stale warrant cannot be revived by redating without a fresh probable-cause finding remains good law and is widely cited."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/101970/sgro-v-united-states/"
  cluster_id: 101970
  opinion_id: 101970
  identity_checked: true
homes:
  - page: "[[Scope Manner and Related Issues]]"
    role: "Progeny (staleness)"
related: ["[[Byars v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "search-warrant", "staleness", "warrant-execution"]
holding: "A search warrant void for non-execution within its statutory life cannot be revived by redating; reissuing a warrant is a new proceeding that must rest on a fresh, contemporaneous probable-cause finding."
lake:
  record_id: Sgro v. United States
  status: verified
  projected_at: 2026-07-09
---

# Sgro v. United States

*287 U.S. 206 (1932)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A United States Commissioner issued a search warrant for the Bouckville Hotel on July 6, 1926, based on an affidavit that the proprietor, Sgro, had sold beer. The warrant was not executed within the ten days the governing statute allowed. On July 27, 1926 — after the warrant had expired — the prohibition agents returned it to the Commissioner, who simply changed the date from July 6 to July 27 and "thus reissued" it on the strength of the original July 6 affidavit. Agents searched the hotel under the redated warrant and found liquor, which was introduced at trial over Sgro's objection.

## Issue
Whether a search warrant that has become void for non-execution within its statutory period may be revived and made valid simply by redating ("reissuing") it on the original affidavit, without a fresh probable-cause determination at the time of reissue.

## Rule
No. The statute made the unexecuted warrant void after ten days, and "[t]here is no provision which authorizes the commissioner to extend its life or to revive it." — 287 U.S. at 210–211. ^pin-210

"The issue of a second warrant is essentially a new proceeding which must have adequate support. The fact that it is a second warrant gives the commissioner no privilege to dispense with the statutory conditions. These cannot be escaped by describing the action as a reissue." — [*Id.* at 211](https://www.courtlistener.com/opinion/101970/sgro-v-united-states/#:~:text=The%20issue%20of%20a%20second). ^pin-211

The supporting proof "must speak as of the time of the issue of that warrant," and "[t]he new warrant must rest upon a proper finding and statement by the commissioner that probable cause then exists." — *Id.* Because probable cause must appear current when the warrant issues, "[t]he purpose of the statute would be thwarted if by the simple expedient of redating, without more, the time for the execution of a warrant could be extended." — *Id.* ^pin-211b

## Application
The proceeding on the July 6 warrant had terminated and that warrant "was dead." On the July 27 application "the commissioner took no proof to show that probable cause then existed and he made no finding of probable cause at that time"; he "simply changed the date of the old warrant and it was 'thus reissued.'" That action was unauthorized, so the redated warrant could not support the search. — 287 U.S. at 212. ^pin-212

## Conclusion
The redated warrant was invalid and the search unlawful; the judgment of conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. Decided on the governing federal warrant statute, *Sgro* states the enduring Fourth Amendment principle that probable cause must be current at issuance and that a stale or expired warrant cannot be revived by redating without a fresh probable-cause showing — the foundational staleness / prompt-execution rule still cited today.

## Appears on
- [[Scope Manner and Related Issues]] — *Progeny (staleness)*

## Sources
- *Sgro v. United States*, 287 U.S. 206 (1932) — https://www.courtlistener.com/opinion/101970/sgro-v-united-states/ — pinpoints: 210, 211, 212.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c7f378e3e1f3ebca", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "287 U.S. 206 (1932)", "court": "U.S. Supreme Court", "neutral_cite": "1932 U.S. LEXIS 13", "official_citation_present": true, "parallel_cite": "53 S. Ct. 138; 77 L. Ed. 260; 85 A.L.R. 108", "title": "Sgro v. United States", "year": "1932"}}
{"assertion_id": "1b61e18f59fb6260", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A search warrant void for non-execution within its statutory life cannot be revived by redating; reissuing a warrant is a new proceeding that must rest on a fresh, contemporaneous probable-cause finding.", "title": "Sgro v. United States"}}
{"assertion_id": "39ebb9347dbfa226", "dimension": "support", "kind": "home_role", "locator": {"home": "Scope Manner and Related Issues"}, "payload": {"home": "Scope Manner and Related Issues", "role": "Progeny (staleness)", "title": "Sgro v. United States"}}
{"assertion_id": "06a8b3d89682866f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Sgro v. United States"}}
{"assertion_id": "1a1dc2f28590d27b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1932-12-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Sgro v. United States", "field_i_validity": "good_law", "scope_note": "Foundational warrant-staleness / prompt-execution holding; the principle that a stale warrant cannot be revived by redating without a fresh probable-cause finding remains good law and is widely cited.", "title": "Sgro v. United States", "varies_by_point": "false"}}
```

### lake record — Sgro v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Sgro v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Sgro v. United States",
    "case_name_short": "Sgro",
    "case_name_full": "Sgro v. United States",
    "input_case_name": "Sgro v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1932-12-05",
    "year": 1932,
    "docket": "55",
    "cluster_id": 101970,
    "lead_opinion_id": 101970,
    "sibling_ids": [
      101970,
      9418758,
      9418759
    ],
    "absolute_url": "/opinion/101970/sgro-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "287 U.S. 206",
      "volume": "287",
      "reporter": "U.S.",
      "page": "206",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "53 S. Ct. 138",
        "volume": "53",
        "reporter": "S. Ct.",
        "page": "138",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 260",
        "volume": "77",
        "reporter": "L. Ed.",
        "page": "260",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 A.L.R. 108",
        "volume": "85",
        "reporter": "A.L.R.",
        "page": "108",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1932 U.S. LEXIS 13",
        "volume": "1932",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "287 U.S. 206",
        "volume": "287",
        "reporter": "U.S.",
        "page": "206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 S. Ct. 138",
        "volume": "53",
        "reporter": "S. Ct.",
        "page": "138",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 260",
        "volume": "77",
        "reporter": "L. Ed.",
        "page": "260",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1932 U.S. LEXIS 13",
        "volume": "1932",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 A.L.R. 108",
        "volume": "85",
        "reporter": "A.L.R.",
        "page": "108",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "287 U.S. 206",
    "official_selection": {
      "court_class": "scotus",
      "selected": "287 U.S. 206",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-210",
      "page": null,
      "quote": ") it on the original affidavit, without a fresh probable-cause determination at the time of reissue. ## Rule No. The statute made the unexecuted warrant void after ten days, and",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-211",
      "page": null,
      "quote": "The issue of a second warrant is essentially a new proceeding which must have adequate support. The fact that it is a second warrant gives the commissioner no privilege to dispense with the statutory conditions. These cannot be escaped by describing the action as a reissue.",
      "star_marker": "211",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6625,
      "fragment": "#:~:text=The%20issue%20of%20a%20second",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-211b",
      "page": null,
      "quote": "must speak as of the time of the issue of that warrant,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-212",
      "page": null,
      "quote": "On the July 27 application",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1932-12-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Sgro v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational warrant-staleness / prompt-execution holding; the principle that a stale warrant cannot be revived by redating without a fresh probable-cause finding remains good law and is widely cited.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Guastucci",
          "cluster_id": 4796647,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harry, Ca2008-01-013 (12-8-2008)",
          "cluster_id": 3938320,
          "cite": [
            "2008 Ohio 6380"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Webb, Dennis L.",
          "cluster_id": 185466,
          "cite": [
            "255 F.3d 890",
            "347 U.S. App. D.C. 162",
            "2001 U.S. App. LEXIS 16837",
            "2001 WL 848613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jason R. Bervaldi",
          "cluster_id": 770469,
          "cite": [
            "226 F.3d 1256",
            "2000 WL 1299557"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Ricciardelli",
          "cluster_id": 610895,
          "cite": [
            "998 F.2d 8",
            "1993 U.S. App. LEXIS 14891",
            "1993 WL 210540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 2428024,
          "cite": [
            "827 S.W.2d 416",
            "1992 WL 27945"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Imo v. State",
          "cluster_id": 1670863,
          "cite": [
            "816 S.W.2d 474",
            "1991 WL 155846"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Acevedo",
          "cluster_id": 6075247,
          "cite": [
            "175 A.D.2d 323",
            "572 N.Y.S.2d 101",
            "1991 N.Y. App. Div. LEXIS 9510"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Edwards",
          "cluster_id": 5688749,
          "cite": [
            "69 N.Y.2d 814",
            "513 N.Y.S.2d 960",
            "506 N.E.2d 530",
            "1987 N.Y. LEXIS 15449"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Maguire",
          "cluster_id": 2160403,
          "cite": [
            "498 A.2d 1028",
            "146 Vt. 49",
            "1985 Vt. LEXIS 349"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Christopher",
          "cluster_id": 6006278,
          "cite": [
            "101 A.D.2d 504",
            "476 N.Y.S.2d 640",
            "1984 N.Y. App. Div. LEXIS 18141"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Winkles v. State",
          "cluster_id": 1622479,
          "cite": [
            "634 S.W.2d 289",
            "1982 Tex. Crim. App. LEXIS 932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Peltier v. State",
          "cluster_id": 2385774,
          "cite": [
            "626 S.W.2d 30",
            "1981 Tex. Crim. App. LEXIS 1217"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane1_negative"
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
        "journal_ref": "Sgro v. United States:lane2_top_cited"
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
        "journal_ref": "Sgro v. United States:lane2_top_cited"
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
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Grubbs",
          "cluster_id": 145670,
          "cite": [
            "164 L. Ed. 2d 195",
            "126 S. Ct. 1494",
            "547 U.S. 90",
            "2006 U.S. LEXIS 2496"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Novembrino",
          "cluster_id": 1516571,
          "cite": [
            "519 A.2d 820",
            "105 N.J. 95",
            "1987 N.J. LEXIS 265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Elie F. Abboud (04-3942) and Michel Abboud (04-3943)",
          "cluster_id": 793369,
          "cite": [
            "438 F.3d 554",
            "97 A.F.T.R.2d (RIA) 1142",
            "2006 U.S. App. LEXIS 3797",
            "2006 WL 354808"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 8939436,
          "cite": [
            "757 F.2d 1359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zap v. United States",
          "cluster_id": 104314,
          "cite": [
            "328 U.S. 624",
            "66 S. Ct. 1277",
            "90 L. Ed. 1477",
            "1946 U.S. LEXIS 2998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James H. Spikes (96-3899) Marilyn Smith (96-3660)",
          "cluster_id": 758684,
          "cite": [
            "158 F.3d 913",
            "49 Fed. R. Serv. 1564",
            "1998 U.S. App. LEXIS 21399",
            "1998 WL 551966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America, Plaintiff-Appellee, v. Scott Douglas LACY, Defendant-Appellant",
          "cluster_id": 744128,
          "cite": [
            "119 F.3d 742",
            "97 Cal. Daily Op. Serv. 5466",
            "97 Daily Journal DAR 8856",
            "1997 U.S. App. LEXIS 17067",
            "1997 WL 378104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald James Causey",
          "cluster_id": 498394,
          "cite": [
            "834 F.2d 1179",
            "1987 U.S. App. LEXIS 17041",
            "1987 WL 23392"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samuel Rosencranz v. United States of America, Anthony Dipietro v. United States",
          "cluster_id": 270626,
          "cite": [
            "356 F.2d 310",
            "1966 U.S. App. LEXIS 7245"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 449643,
          "cite": [
            "757 F.2d 1359",
            "1985 U.S. App. LEXIS 29735"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Martino, John Torrioni, Policardo Despaigne, A/K/A \"Paulie,\" Odell Miller, A/K/A \"Pluggy,\" John Radice, and John Perry",
          "cluster_id": 397139,
          "cite": [
            "664 F.2d 860",
            "1981 U.S. App. LEXIS 16278"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Russo",
          "cluster_id": 2191658,
          "cite": [
            "487 N.W.2d 698",
            "439 Mich. 584"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Kenneth Banks, A/K/A Kenny, United States of America v. William Kenneth Banks, A/K/A Kenny, United States of America v. Garry Copeland, A/K/A Fat Garry, United States of America v. Fernando Cumbo Blow, United States of America v. Bruce Elliott Boone, Sr., United States of America v. Samuel Collins, Jr., A/K/A Cross, A/K/A Cadillac Sam, A/K/A Norristown Sam",
          "cluster_id": 658315,
          "cite": [
            "10 F.3d 1044",
            "1993 U.S. App. LEXIS 30572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory James Freeman and David Lyle Boese, A/K/A Dennis Phillip Stevens and David Sterling",
          "cluster_id": 407601,
          "cite": [
            "685 F.2d 942",
            "1982 U.S. App. LEXIS 26042"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael J. McNeese and Laura Conwell",
          "cluster_id": 540059,
          "cite": [
            "901 F.2d 585",
            "30 Fed. R. Serv. 383",
            "1990 U.S. App. LEXIS 7055",
            "1990 WL 55059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Scott Zimmerman",
          "cluster_id": 776207,
          "cite": [
            "277 F.3d 426",
            "187 A.L.R. Fed. 761",
            "2002 U.S. App. LEXIS 73",
            "2002 WL 13167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Feola",
          "cluster_id": 2307132,
          "cite": [
            "651 F. Supp. 1068",
            "1987 U.S. Dist. LEXIS 435"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Spinelli v. United States",
          "cluster_id": 277169,
          "cite": [
            "382 F.2d 871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cook",
          "cluster_id": 1291238,
          "cite": [
            "583 P.2d 130",
            "22 Cal. 3d 67",
            "148 Cal. Rptr. 605",
            "1978 Cal. LEXIS 277"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sgro v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(101970 OR 9418758 OR 9418759) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTc3ODI0MDAwMDAmcz0zODYyMTkmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28101970+OR+9418758+OR+9418759%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(101970 OR 9418758 OR 9418759)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDImcz0yNDU1ODI0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28101970+OR+9418758+OR+9418759%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(101970 OR 9418758 OR 9418759)",
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
    "complete_query": "cites:(101970 OR 9418758 OR 9418759)",
    "indexed_citing_opinions": 444,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 101970,
        "count": 392,
        "count_source": "search"
      },
      {
        "opinion_id": 9418758,
        "count": 67,
        "count_source": "search"
      },
      {
        "opinion_id": 9418759,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 657,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/sgro-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3ODAwNzEmcz00NDc4OTUxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28101970+OR+9418758+OR+9418759%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 101970,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101970,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101970,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101970,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101970,
        "cited_id": 101899,
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
    "date_created": "2026-07-05T19:17:37Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:17:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:17:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:24:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:17:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Sgro v. United States

```
<div>
<center><b><span class="citation" data-id="9418758"><a href="/opinion/101970/sgro-v-united-states/" aria-description="Citation for case: Sgro v. United States">287 U.S. 206</a></span> (1932)</b></center>
<center><h1>SGRO<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 55.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 10, 1932.</center>
<center>Decided December 5, 1932.</center>
CERTIORARI TO THE CIRCUIT COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><i>Mr. Irving K. Baxter</i> for petitioner.</p>
<p><i>Assistant Attorney General Youngquist,</i> with whom <i>Solicitor General Thacher,</i> and <i>Messrs. John J. Byrne</i> and <i>W. Marvin Smith</i> were on the brief, for the United States.</p>
<p><span class="star-pagination">*208</span> MR. CHIEF JUSTICE HUGHES delivered the opinion of the Court.</p>
<p>The petitioner was charged with violating the National Prohibition Act by possessing and selling intoxicating liquor at the Bouckville Hotel. The District Court denied his request to restrain the use of evidence procured by federal officers while searching the hotel under a warrant alleged to be invalid. This evidence was introduced at the trial over his objection. He was found guilty and the judgment against him was affirmed by the Circuit Court of Appeals. [54 F. (2d) 1083.] This Court granted certiorari. The only question presented is as to the validity of the warrant.</p>
<p>Subject to petitioner's contention, the parties entered into a stipulation of facts which so far as pertinent to the question is as follows:</p>
<p>"That on or about the sixth day of July, 1926, William Arthur, United States Commissioner, at Rome, New York, issued a search warrant based upon an affidavit introduced in evidence in this case, of C.G. Dodd, in which Dodd swore that he made a purchase of beer of the defendant; that on the twenty-seventh day of July, 1926, the said search warrant not having been executed in the interim and ten days from the date of the search warrant having expired, the search warrant was taken by the prohibition agents to whom it was directed back to the commissioner and by him, or by someone in his office under his direction and control, the date of the search warrant was changed from July sixth to July twenty-seventh, 1926, and thus reissued; that acting under the color of such search warrant," the search in question was made.</p>
<p><span class="star-pagination">*209</span> The record also contains a certificate by the United States Commissioner, under date of December 20, 1926, as follows:</p>
<p>"I hereby certify that the complaint or affidavit, upon which the search warrant was issued in the above entitled matter, was made before me on the 6th day of July, 1926. That the search warrant was issued on or about said 6th day of July, 1926, but was not executed within the ten days prescribed by statute, and was returned to me by Albert Vandiver, Prohibition Agent in Charge of the Syracuse office requesting that same be reissued or redated, and my docket book shows that same was reissued on the 27th day of July, 1926, and mailed back to said Vandiver."</p>
<p>The National Prohibition Act, § 25, <span class="citation no-link">41 Stat. 305</span>, 315, U.S.C., Tit. 27, § 39, authorizes the issue of warrants to search for intoxicating liquors as provided in Title XI of the Act of June 15, 1917, <span class="citation no-link">40 Stat. 228</span>.<sup>[1]</sup> Section 11 of the last mentioned Act has the following requirement:</p>
<p><span class="star-pagination">*210</span> "SEC. 11. A search warrant must be executed and returned to the judge or commissioner who issued it within ten days after its date; after the expiration of this time the warrant, unless executed, is void."</p>
<p>As the original warrant was issued on July sixth and was not executed within ten days, it became void under this explicit provision. But the Government contends that the warrant could be redated and reissued, and that in this form it should be regarded as a new warrant under which the search could lawfully be made.</p>
<p>With this argument we cannot agree. The proceeding by search warrant is a drastic one. Its abuse led to the adoption of the Fourth Amendment, and this, together with legislation regulating the process, should be liberally construed in favor of the individual. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U.S. 616, 635</a></span>; <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#32" aria-description="Citation for case: Byars v. United States">273 U.S. 28, 32</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U.S. 192, 196, 197</a></span>; <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U.S. 452, 464</a></span>. The statute requires that the judge or commissioner issuing a search warrant for intoxicating liquors must be satisfied "of the existence of the grounds of the application or that there is probable cause to believe their existence." Act of June 15, 1917, Tit. XI, § 6. He must take proof to that end. <i>Id.,</i> §§ 4, 5. The warrant must state "the particular grounds or probable cause for its issue and the names of the persons whose affidavits have been taken in support thereof." <i>Id.,</i> § 6. While the statute does not fix the time within which proof of probable cause must be taken by the judge or commissioner, it is manifest that the proof must be of facts so closely related to the time of the issue of the warrant as to justify a finding of probable cause at that time. Whether the proof meets this test <span class="star-pagination">*211</span> must be determined by the circumstances of each case. It is in the light of the requirement that probable cause must properly appear when the warrant issues that we must read the provision which in explicit terms makes a warrant void unless executed within ten days after its date. That period marks the permitted duration of the proceeding in which the warrant is issued. There is no provision which authorizes the commissioner to extend its life or to revive it.</p>
<p>The issue of a second warrant is essentially a new proceeding which must have adequate support. The fact that it is a second warrant gives the commissioner no privilege to dispense with the statutory conditions. These cannot be escaped by describing the action as a reissue. If the warrant is the old one, sought to be revived, the proceeding is a nullity, and if it is a new warrant, the commissioner must act accordingly. The statute in terms requires him before issuing the warrant to take proof of probable cause. This he must do by examining on oath the complainant and his witness and requiring their affidavits or depositions. The proof supplied must have appropriate relation to the application for the new warrant and must speak as of the time of the issue of that warrant. The commissioner has no authority to rely on affidavits which have sole relation to a different time and have not been brought down to date or supplemented so that they can be deemed to disclose grounds existing when the new warrant is issued. The new warrant must rest upon a proper finding and statement by the commissioner that probable cause then exists. That determination, as of that time, cannot be left to mere inference or conjecture. The purpose of the statute would be thwarted if by the simple expedient of redating, without more, the time for the execution of a warrant could be extended.</p>
<p><span class="star-pagination">*212</span> Applying these principles to the instant case, the warrant cannot be sustained. The proceeding for the warrant issued on July sixth had terminated and that warrant was dead. On the new application of July twenty-seventh the commissioner took no proof to show that probable cause then existed and he made no finding of probable cause at that time. It is impossible by any process of reasoning to obscure or alter what he actually did. He simply changed the date of the old warrant and it was "thus reissued." Such action was unauthorized.</p>
<p><i>Judgment reversed.</i></p>
<p>MR. JUSTICE STONE and MR. JUSTICE CARDOZO think that the Commissioner, by redating the warrant, in effect, issued a new warrant, which was adequately supported by facts disclosed in the affidavit, then before him, on which the first warrant had been issued.</p>
<p>Separate opinion of MR. JUSTICE McREYNOLDS.</p>
<p>I concur in the conclusion that the judgment below should be reversed.</p>
<p>An information charged that Petitioner Sgro had violated the National Prohibition Act by keeping intoxicating liquor at an hotel. In due time and manner he unsuccessfully asked the District Court to prohibit the use of all evidence procured by federal officers while searching the hotel under color of a warrant alleged to be invalid. At the trial this evidence was introduced over his objection. A verdict of guilty followed; judgment thereon was affirmed by the Circuit Court of Appeals. If the challenged search warrant was invalid, this judgment must be reversed.</p>
<p>By stipulation it appears </p>
<p>"That on or about the sixth day of July, 1926, William Arthur, United States Commissioner, at Rome, New York, issued a search warrant based upon an affidavit introduced in evidence in this case, of C.G. Dodd, in which Dodd <span class="star-pagination">*213</span> swore that he made a purchase of beer of the defendant; that on the twenty-seventh day of July, 1926, the said search warrant not having been executed in the interim and ten days from the date of the search warrant having expired, the search warrant was taken by the prohibition agents to whom it was directed back to the commissioner and by him, or by someone in his office under his direction and control, the date of the search warrant was changed from July sixth to July twenty-seventh, 1926, and thus reissued; that acting under the color of such search warrant, Prohibition Agents Henry E. March, Bernard J. Dwyer and B.G. Silvernail went to the premises described in the search warrant, namely the Bouckville Hotel, of which the defendant is the proprietor, at Bouckville, New York, in the Northern District of New York, and there, the defendant being present, searched the premises and found one pint of gin, a pint of beer in the bar room of the said premises, and also found in the cellar of said premises under said bar room three and a half barrels of liquid, . . . ."</p>
<p>The Fourth Amendment provides  "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>The National Prohibition Act, § 25, <span class="citation no-link">41 Stat. 305</span>, 315, U.S.C.A., Title 27, § 39, authorizes the issuance of warrants to search for intoxicating liquors under the circumstances specified by Title XI, Public Laws No. 24, 65th Congress (Espionage Act), approved June 15, 1917, <span class="citation no-link">40 Stat. 228</span>. The following are among the provisions of the latter Act </p>
<p>"Sec. 2. A search warrant may be issued under this title upon either of the following grounds:</p>
<p><span class="star-pagination">*214</span> "3. When the property, or any paper, is possessed, controlled, or used in violation of section twenty-two of this title; in which case it may be taken on the warrant from the person violating said section, or from any person in whose possession it may be, or from any house or other place in which it is concealed.</p>
<p>"Sec. 3. A search warrant can not be issued but upon probable cause, supported by affidavit, naming or describing the person and particularly describing the property and the place to be searched.</p>
<p>"Sec. 4. The judge or commissioner must, before issuing the warrant, examine on oath the complainant and any witness he may produce, and require their affidavits or take their depositions in writing and cause them to be subscribed by the parties making them.</p>
<p>"Sec. 5. The affidavits or depositions must set forth the facts tending to establish the grounds of the application or probable cause for believing that they exist.</p>
<p>"Sec. 6. If the judge or commissioner is thereupon satisfied of the existence of the grounds of the application or that there is probable cause to believe their existence, he must issue a search warrant, signed by him with his name of office, to a civil officer of the United States duly authorized to enforce or assist in enforcing any law thereof, or to a person so duly authorized by the President of the United States, stating the particular grounds or probable cause for its issue and the names of the persons whose affidavits have been taken in support thereof, and commanding him forthwith to search the person or place named, for the property specified, and to bring it before the judge or commissioner.</p>
<p>"Sec. 11. A search warrant must be executed and returned to the judge or commissioner who issued it within ten days after its date; after the expiration of this time the warrant, unless executed, is void."</p>
<p><span class="star-pagination">*215</span> Counsel for the United States submit that while under the Espionage Act (§ 11) a search warrant not executed within ten days becomes invalid, the statute does not inhibit utilization of an outlawed warrant as a mere form or blank when preparing a new one based upon the original affidavit; that here the act of the Commissioner in changing the date upon the July sixth warrant and then reissuing it under date of July twenty-seventh was to all intents and purposes the issuing of an entirely new and valid warrant supported by the Dodd affidavit of July sixth. This argument is pertinent and should be answered.</p>
<p>It fairly may be assumed that the Commissioner who issued the warrant on July twenty-seventh relied upon the original (July sixth) affidavit which remained before him; and if this was permissible, the new warrant, of course, was good  just as good as if no earlier one had been issued upon the same affidavit. But if the original affidavit had become stale by the passage of time, then the new warrant lacked adequate support and was invalid. Manifestly, it is important that there should be some definite rule by which to determine when such an affidavit is impotent; otherwise, the matter is left at large  dependent upon varying views of reasonableness.</p>
<p>The proceeding by search warrant is a drastic one. Its abuse led to the adoption of the Fourth Amendment, and this, together with legislation regulating such process, should be liberally construed in favor of the individual. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U.S. 616, 635</a></span>; <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U.S. 585</a></span>; <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U.S. 192, 196, 197</a></span>.</p>
<p>The statutes require that a warrant to search for intoxicating liquors shall rest upon duly established probable cause to believe that at the time it issues the liquor is unlawfully possessed. The supporting affidavit must relate <span class="star-pagination">*216</span> to facts which tend to show an unlawful situation actually or probably existing at the moment. Section 11, Espionage Act, declares that after ten days a warrant not fully executed shall be void. That is the prescribed period during which the circumstances existing when it issued can be supposed to continue.</p>
<p>Considering the whole statute, and especially the evident purpose of Congress to protect against unnecessary delays and uncertainties, I think no search warrant should issue upon an affidavit more than ten days old. After attaining that age statements therein cannot properly indicate presently existing conditions. In practice the contrary view would permit results which the prescribed ten days' limitation was intended to prevent. The disclosed unlawful situation is not presumed to continue more than ten days after a warrant issues and it seems entirely reasonable to conclude that Congress did not intend to sanction a less rigid limitation upon the supporting affidavit.</p>
<p>It follows that the Commissioner's warrant of July twenty-seventh was invalid, even if it be assumed that he then actually relied upon the original supporting affidavit dated three weeks earlier.</p>
<h2>NOTES</h2>
<p>[1]   The following are among the provisions of the Act of June 15, 1917, Tit. XI, <span class="citation no-link">40 Stat. 228</span>:
</p>
<p>"Sec. 3. A search warrant can not be issued but upon probable cause, supported by affidavit, naming or describing the person and particularly describing the property and the place to be searched.</p>
<p>"Sec. 4. The judge or commissioner must, before issuing the warrant, examine on oath the complainant and any witness he may produce, and require their affidavits or take their depositions in writing and cause them to be subscribed by the parties making them.</p>
<p>"Sec. 5. The affidavits or depositions must set forth the facts tending to establish the grounds of the application or probable cause for believing that they exist.</p>
<p>"Sec. 6. If the judge or commissioner is thereupon satisfied of the existence of the grounds of the application or that there is probable cause to believe their existence, he must issue a search warrant signed by him with his name of office, to a civil officer of the United States duly authorized to enforce or assist in enforcing any law thereof, or to a person so duly authorized by the President of the United States, stating the particular grounds or probable cause for its issue and the names of the persons whose affidavits have been taken in support thereof, and commanding him forthwith to search the person or place named, for the property specified, and to bring it before the judge or commissioner."</p>

</div>
```

---
