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

## GROUP: _overhaul2/lake/cases/Illinois v. Rodriguez.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Illinois v. Rodriguez"
type: case
citation: "497 U.S. 177 (1990)"
parallel_cite: "110 S. Ct. 2793; 111 L. Ed. 2d 148; 58 U.S.L.W. 4892"
neutral_cite: 1990 U.S. LEXIS 3295
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Rodriguez
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112475/illinois-v-rodriguez/"
  cluster_id: 112475
  opinion_id: 112475
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Matlock]]", "[[Georgia v. Randolph]]", "[[Fernandez v. California]]", "[[Schneckloth v. Bustamonte]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "apparent-authority", "third-party-consent"]
holding: "APPARENT AUTHORITY: a warrantless entry on third-party consent is valid if officers REASONABLY (though mistakenly) believed the…"
lake:
  record_id: Illinois v. Rodriguez
  status: verified
  projected_at: 2026-07-06
---

# Illinois v. Rodriguez

*497 U.S. 177 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gail Fischer, showing signs of a beating, told police that Rodriguez had assaulted her and led them to his apartment, which she unlocked with her key, referring to it as "our" apartment. Officers entered without a warrant, found drugs and paraphernalia in plain view, and arrested Rodriguez. In fact Fischer had moved out weeks earlier and lacked common authority: her name was not on the lease, she did not pay rent, and she could not admit others on her own.

## Issue
Whether a warrantless entry based on a third party's consent is valid when the police reasonably, but mistakenly, believe the consenting person has common authority over the premises.

## Rule
The validity of an entry on [[Consent Searches|apparent authority]] is measured by objective reasonableness, not by whether the consenting party actually had authority. The Court held that the determination of consent to enter must "be judged against an objective standard: would the facts available to the officer at the moment . . . 'warrant a man of reasonable caution in the belief'" that the consenting party had authority over the premises. — 497 U.S. at 188. ^pin-188

"If not, then warrantless entry without further inquiry is unlawful unless authority actually exists. But if so, the search is valid." — *Id.* at 188–189. ^pin-188a

## Application
Fischer let the officers in with her own key and referred to the apartment as hers, but she had in fact moved out and lacked actual common authority. The lower courts had ruled that a mistaken belief could never validate the entry; that was error, because the entry is valid if the officers reasonably believed Fischer had common authority. The Court therefore [[Reading and Citing Cases#on-remand|remanded]] for a determination whether the officers' belief in her authority was objectively reasonable.

## Conclusion
A reasonable, even if mistaken, belief in a third party's common authority can validate a warrantless entry; the case was reversed and [[Reading and Citing Cases#on-remand|remanded]] to apply that apparent-authority standard.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Rodriguez* supplements the actual-common-authority rule of [[United States v. Matlock]] with an apparent-authority doctrine; [[Georgia v. Randolph]] and [[Fernandez v. California]] later address a physically present co-occupant's refusal.

## Appears on
- [[Consent Searches]] — *Key — Progeny / Refinement*

## Sources
- *Illinois v. Rodriguez*, 497 U.S. 177 (1990) — https://www.courtlistener.com/opinion/112475/illinois-v-rodriguez/ — pinpoints: 188, 189.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "240f75f4a62bfe89", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Rodriguez"}, "payload": {"all": [{"cite": "497 U.S. 177", "page": "177", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "497"}, {"cite": "110 S. Ct. 2793", "page": "2793", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "111 L. Ed. 2d 148", "page": "148", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "111"}, {"cite": "1990 U.S. LEXIS 3295", "page": "3295", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}, {"cite": "58 U.S.L.W. 4892", "page": "4892", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "58"}], "display": "497 U.S. 177", "official": {"cite": "497 U.S. 177", "page": "177", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "497"}, "official_selection_present": true, "record_id": "Illinois v. Rodriguez"}}
{"assertion_id": "724cc0119ca8bd1b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-188a", "record_id": "Illinois v. Rodriguez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-188a", "pinpoint_status": "slip-only", "quote": "If not, then warrantless entry without further inquiry is unlawful unless authority actually exists. But if so, the search is valid.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Rodriguez", "star_marker": null}}
{"assertion_id": "c10810dcf5e25480", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-188", "record_id": "Illinois v. Rodriguez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-188", "pinpoint_status": "slip-only", "quote": "apartment. Officers entered without a warrant, found drugs and paraphernalia in plain view, and arrested Rodriguez. In fact Fischer had moved out weeks earlier and lacked common authority: her name was not on the lease, she did not pay rent, and she could not admit others on her own. ## Issue Whether a warrantless entry based on a third party's consent is valid when the police reasonably, but mistakenly, believe the consenting person has common authority over the premises. ## Rule The validity of an entry on apparent authority is measured by objective reasonableness, not by whether the consenting party actually had authority. The Court held that the determination of consent to enter must", "quote_fidelity": "mismatch", "record_id": "Illinois v. Rodriguez", "star_marker": null}}
{"assertion_id": "5c8ce41b80f59b8a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Rodriguez"}, "payload": {"as_of_content": "1990-06-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Rodriguez", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Illinois v. Rodriguez

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Rodriguez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Rodriguez",
    "case_name_short": "Rodriguez",
    "case_name_full": "Illinois v. Rodriguez",
    "input_case_name": "Illinois v. Rodriguez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-06-21",
    "year": 1990,
    "docket": null,
    "cluster_id": 112475,
    "lead_opinion_id": 112475,
    "sibling_ids": [
      112475,
      9432101,
      9432102
    ],
    "absolute_url": "/opinion/112475/illinois-v-rodriguez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9094047,
        "score": 20,
        "case_name": "Illinois v. Rodriguez"
      },
      {
        "cluster_id": 9094046,
        "score": 20,
        "case_name": "Illinois v. Rodriguez"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "497 U.S. 177",
      "volume": "497",
      "reporter": "U.S.",
      "page": "177",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 2793",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2793",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 L. Ed. 2d 148",
        "volume": "111",
        "reporter": "L. Ed. 2d",
        "page": "148",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4892",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4892",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 3295",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3295",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "497 U.S. 177",
        "volume": "497",
        "reporter": "U.S.",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 2793",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2793",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 L. Ed. 2d 148",
        "volume": "111",
        "reporter": "L. Ed. 2d",
        "page": "148",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 3295",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3295",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4892",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4892",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "497 U.S. 177",
    "official_selection": {
      "court_class": "scotus",
      "selected": "497 U.S. 177",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-188",
      "page": null,
      "quote": "apartment. Officers entered without a warrant, found drugs and paraphernalia in plain view, and arrested Rodriguez. In fact Fischer had moved out weeks earlier and lacked common authority: her name was not on the lease, she did not pay rent, and she could not admit others on her own. ## Issue Whether a warrantless entry based on a third party's consent is valid when the police reasonably, but mistakenly, believe the consenting person has common authority over the premises. ## Rule The validity of an entry on apparent authority is measured by objective reasonableness, not by whether the consenting party actually had authority. The Court held that the determination of consent to enter must",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-188a",
      "page": null,
      "quote": "If not, then warrantless entry without further inquiry is unlawful unless authority actually exists. But if so, the search is valid.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Rodriguez",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Jones",
          "cluster_id": 4517594,
          "cite": [
            "193 A.3d 957"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Henry Bams",
          "cluster_id": 4396584,
          "cite": [
            "858 F.3d 937",
            "2017 WL 2380680",
            "2017 U.S. App. LEXIS 9735"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane1_negative"
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
        "journal_ref": "Illinois v. Rodriguez:lane1_negative"
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
        "journal_ref": "Illinois v. Rodriguez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schriro v. Landrigan",
          "cluster_id": 145734,
          "cite": [
            "167 L. Ed. 2d 836",
            "127 S. Ct. 1933",
            "550 U.S. 465",
            "2007 U.S. LEXIS 5496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
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
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patrick v. State",
          "cluster_id": 1713584,
          "cite": [
            "906 S.W.2d 481",
            "1995 WL 379872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
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
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
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
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
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
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
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
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Evans",
          "cluster_id": 117905,
          "cite": [
            "131 L. Ed. 2d 34",
            "115 S. Ct. 1185",
            "514 U.S. 1",
            "1995 U.S. LEXIS 1806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Valtierra v. State",
          "cluster_id": 1370428,
          "cite": [
            "310 S.W.3d 442",
            "2010 Tex. Crim. App. LEXIS 828",
            "2010 WL 1850384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
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
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Labron",
          "cluster_id": 118063,
          "cite": [
            "135 L. Ed. 2d 1031",
            "116 S. Ct. 2485",
            "518 U.S. 938",
            "1996 U.S. LEXIS 4268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
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
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heien v. North Carolina",
          "cluster_id": 2760668,
          "cite": [
            "190 L. Ed. 2d 475",
            "135 S. Ct. 530",
            "2014 U.S. LEXIS 8306",
            "83 U.S.L.W. 4021",
            "25 Fla. L. Weekly Fed. S 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peterson v. City of Fort Worth, Tex.",
          "cluster_id": 69197,
          "cite": [
            "588 F.3d 838",
            "2009 U.S. App. LEXIS 25183",
            "2009 WL 3818826"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Stone",
          "cluster_id": 4958214,
          "cite": [
            "2021 COA 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tibbetts",
          "cluster_id": 6889013,
          "cite": [
            "92 Ohio St. 3d 146",
            "749 N.E.2d 226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Givens",
          "cluster_id": 2482051,
          "cite": [
            "934 N.E.2d 470",
            "237 Ill. 2d 311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bull",
          "cluster_id": 1998703,
          "cite": [
            "705 N.E.2d 824",
            "185 Ill. 2d 179",
            "235 Ill. Dec. 641",
            "1998 Ill. LEXIS 1578"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 1670023,
          "cite": [
            "755 N.W.2d 664",
            "279 Mich. App. 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Henderson",
          "cluster_id": 2094180,
          "cite": [
            "568 N.E.2d 1234",
            "142 Ill. 2d 258",
            "154 Ill. Dec. 785",
            "1990 Ill. LEXIS 138"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brimage v. State",
          "cluster_id": 2417512,
          "cite": [
            "918 S.W.2d 466",
            "1996 Tex. Crim. App. LEXIS 5",
            "1994 WL 511395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Roy C. Blakeney (90-5664), Kenneth A. Kutnyak (90-5665), and James E. Box (90-6041)",
          "cluster_id": 567212,
          "cite": [
            "942 F.2d 1001",
            "33 Fed. R. Serv. 1362",
            "1991 U.S. App. LEXIS 19690"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Pitman",
          "cluster_id": 2234418,
          "cite": [
            "813 N.E.2d 93",
            "211 Ill. 2d 502",
            "286 Ill. Dec. 36",
            "2004 Ill. LEXIS 989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Rodriguez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112475 OR 9432101 OR 9432102) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDU2OTYzMjAwMDAwJnM9MzE4MzM4NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112475+OR+9432101+OR+9432102%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112475 OR 9432101 OR 9432102)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTAmcz03NzA0MjkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112475+OR+9432101+OR+9432102%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112475 OR 9432101 OR 9432102)",
        "reviewed": 48,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 48,
        "triage_read": 0,
        "triage_snippet_classified": 48
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112475 OR 9432101 OR 9432102)",
    "indexed_citing_opinions": 1600,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112475,
        "count": 1445,
        "count_source": "search"
      },
      {
        "opinion_id": 9432101,
        "count": 182,
        "count_source": "search"
      },
      {
        "opinion_id": 9432102,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2585,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-rodriguez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwODY5NDcmcz0xMDI4MjE4NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112475+OR+9432101+OR+9432102%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112475,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 111798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 403411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112475,
        "cited_id": 1129895,
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
    "date_created": "2026-07-05T08:26:15Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:26:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:26:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:31:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:26:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Rodriguez

```
<div>
<center><b><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">497 U.S. 177</a></span> (1990)</b></center>
<center><h1>ILLINOIS<br>
v.<br>
RODRIGUEZ</h1></center>
<center>No. 88-2018.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued March 20, 1990.</center>
<center>Decided June 21, 1990.</center>
CERTIORARI TO THE APPELLATE COURT OF ILLINOIS, FIRST DISTRICT
<p><span class="star-pagination">*178</span> <i>Joseph Claps,</i> First Assistant Attorney General of Illinois, argued the cause for petitioner. With him on the briefs were <i>Neil F. Hartigan,</i> Attorney General, <i>Robert J. Ruiz,</i> Solicitor General, <i>Terence M. Madsen,</i> Assistant Attorney General, <i>Cecil A. Partee, Renée Goldfarb,</i> and <i>Theodore Fotios Burtzos.</i></p>
<p><i>Michael R. Dreeben</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Starr, Assistant Attorney General Dennis,</i> and <i>Deputy Solicitor General Bryson.</i></p>
<p><i>James W. Reilley</i> argued the cause for respondent. With him on the brief were <i>Christine P. Curran, Dianne Ruthman,</i> and <i>Rick Halprin.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*179</span> JUSTICE SCALIA delivered the opinion of the Court.</p>
<p>In <i>United States</i> v. <i>Matlock,</i> <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">415 U. S. 164</a></span> (1974), this Court reaffirmed that a warrantless entry and search by law enforcement officers does not violate the Fourth Amendment's proscription of "unreasonable searches and seizures" if the officers have obtained the consent of a third party who possesses common authority over the premises. The present case presents an issue we expressly reserved in <i><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">Matlock</a></span>,</i> see <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#177" aria-description="Citation for case: United States v. Matlock"><i>id.,</i> at 177</a></span>, n. 14: Whether a warrantless entry is valid when based upon the consent of a third party whom the police, at the time of the entry, reasonably believe to possess common authority over the premises, but who in fact does not do so.</p>
<p></p>
<h2>I</h2>
<p>Respondent Edward Rodriguez was arrested in his apartment by law enforcement officers and charged with possession of illegal drugs. The police gained entry to the apartment with the consent and assistance of Gail Fischer, who had lived there with respondent for several months. The relevant facts leading to the arrest are as follows.</p>
<p>On July 26, 1985, police were summoned to the residence of Dorothy Jackson on South Wolcott in Chicago. They were met by Ms. Jackson's daughter, Gail Fischer, who showed signs of a severe beating. She told the officers that she had been assaulted by respondent Edward Rodriguez earlier that day in an apartment on South California Avenue. Fischer stated that Rodriguez was then asleep in the apartment, and she consented to travel there with the police in order to unlock the door with her key so that the officers could enter and arrest him. During this conversation, Fischer several times referred to the apartment on South California as "our" apartment, and said that she had clothes and furniture there. It is unclear whether she indicated that she currently lived at the apartment, or only that she used to live there.</p>
<p><span class="star-pagination">*180</span> The police officers drove to the apartment on South California, accompanied by Fischer. They did not obtain an arrest warrant for Rodriguez, nor did they seek a search warrant for the apartment. At the apartment, Fischer unlocked the door with her key and gave the officers permission to enter. They moved through the door into the living room, where they observed in plain view drug paraphernalia and containers filled with white powder that they believed (correctly, as later analysis showed) to be cocaine. They proceeded to the bedroom, where they found Rodriguez asleep and discovered additional containers of white powder in two open attaché cases. The officers arrested Rodriguez and seized the drugs and related paraphernalia.</p>
<p>Rodriguez was charged with possession of a controlled substance with intent to deliver. He moved to suppress all evidence seized at the time of his arrest, claiming that Fischer had vacated the apartment several weeks earlier and had no authority to consent to the entry. The Cook County Circuit Court granted the motion, holding that at the time she consented to the entry Fischer did not have common authority over the apartment. The Court concluded that Fischer was not a "usual resident" but rather an "infrequent visitor" at the apartment on South California, based upon its findings that Fischer's name was not on the lease, that she did not contribute to the rent, that she was not allowed to invite others to the apartment on her own, that she did not have access to the apartment when respondent was away, and that she had moved some of her possessions from the apartment. The Circuit Court also rejected the State's contention that, even if Fischer did not possess common authority over the premises, there was no Fourth Amendment violation if the police <i>reasonably believed</i> at the time of their entry that Fischer possessed the authority to consent.</p>
<p>The Appellate Court of Illinois affirmed the Circuit Court in all respects. The Illinois Supreme Court denied the State's petition for leave to appeal, <span class="citation no-link">125 Ill. 2d 572</span>, 537 <span class="star-pagination">*181</span> N. E. 2d 816 (1989), and we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./493/932/">493 U. S. 932</a></span> (1989).</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment generally prohibits the warrantless entry of a person's home, whether to make an arrest or to search for specific objects. <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948). The prohibition does not apply, however, to situations in which voluntary consent has been obtained, either from the individual whose property is searched, see <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), or from a third party who possesses common authority over the premises, see <i>United States</i> v. <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#171" aria-description="Citation for case: United States v. Matlock"><i>Matlock, supra,</i> at 171</a></span>. The State of Illinois contends that that exception applies in the present case.</p>
<p>As we stated in <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#171" aria-description="Citation for case: United States v. Matlock"><i>Matlock, supra,</i> at 171, n. 7</a></span>, "[c]ommon authority" rests "on mutual use of the property by persons generally having joint access or control for most purposes. . . ." The burden of establishing that common authority rests upon the State. On the basis of this record, it is clear that burden was not sustained. The evidence showed that although Fischer, with her two small children, had lived with Rodriguez beginning in December 1984, she had moved out on July 1, 1985, almost a month before the search at issue here, and had gone to live with her mother. She took her and her children's clothing with her, though leaving behind some furniture and household effects. During the period after July 1 she sometimes spent the night at Rodriguez's apartment, but never invited her friends there, and never went there herself when he was not home. Her name was not on the lease nor did she contribute to the rent. She had a key to the apartment, which she said at trial she had taken without Rodriguez's knowledge (though she testified at the preliminary hearing that Rodriguez had given her the key). On these facts the State has not established that, with respect to the South California apartment, Fischer had <span class="star-pagination">*182</span> "joint access or control for most purposes." To the contrary, the Appellate Court's determination of no common authority over the apartment was obviously correct.</p>
<p></p>
<h2>III</h2>
<p></p>
<h2>A</h2>
<p>The State contends that, even if Fischer did not in fact have authority to give consent, it suffices to validate the entry that the law enforcement officers reasonably believed she did. Before reaching the merits of that contention, we must consider a jurisdictional objection: that the decision below rests on an adequate and independent state ground. Respondent asserts that the Illinois Constitution provides greater protection than is afforded under the Fourth Amendment, and that the Appellate Court relied upon this when it determined that a reasonable belief by the police officers was insufficient.</p>
<p>When a state-court decision is clearly based on state law that is both adequate and independent, we will not review the decision. <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1041</a></span> (1983). But when "a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law," we require that it contain a "`plain statement' that [it] rests upon adequate and independent state grounds," <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long"><i>id.,</i> at 1040, 1042</a></span>; otherwise, "we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so." <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long"><i>Id.,</i> at 1041</a></span>. Here, the Appellate Court's opinion contains no "plain statement" that its decision rests on state law. The opinion does not rely on (or even mention) any specific provision of the Illinois Constitution, nor even the Illinois Constitution generally. Even the Illinois cases cited by the opinion rely upon no constitutional provisions other than the Fourth and Fourteenth Amendments of the United States Constitution. We conclude that the Appellate Court of Illinois rested its decision on federal law.</p>
<p></p>
<h2>
<span class="star-pagination">*183</span> B</h2>
<p>On the merits of the issue, respondent asserts that permitting a reasonable belief of common authority to validate an entry would cause a defendant's Fourth Amendment rights to be "vicariously waived." Brief for Respondent 32. We disagree.</p>
<p>We have been unyielding in our insistence that a defendant's waiver of his trial rights cannot be given effect unless it is "knowing" and "intelligent." <i>Colorado</i> v. <i>Spring,</i> <span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/#574" aria-description="Citation for case: Colorado v. Spring">479 U. S. 564, 574-575</a></span> (1987); <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938). We would assuredly not permit, therefore, evidence seized in violation of the Fourth Amendment to be introduced on the basis of a trial court's mere "reasonable belief"derived from statements by unauthorized personsthat the defendant has waived his objection. But one must make a distinction between, on the one hand, trial rights that <i>derive</i> from the violation of constitutional guarantees and, on the other hand, the nature of those constitutional guarantees themselves. As we said in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>:</i></p>
<blockquote>"There is a vast difference between those rights that protect a fair criminal trial and the rights guaranteed under the Fourth Amendment. Nothing, either in the purposes behind requiring a `knowing' and `intelligent' waiver of trial rights, or in the practical application of such a requirement suggests that it ought to be extended to the constitutional guarantee against unreasonable searches and seizures." <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#241" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 241</a></span>.</blockquote>
<p>What Rodriguez is assured by the trial right of the exclusionary rule, where it applies, is that no evidence seized in violation of the Fourth Amendment will be introduced at his trial unless he consents. What he is assured by the Fourth Amendment itself, however, is not that no government search of his house will occur unless he consents; but that no such search will occur that is "unreasonable." U. S. Const., Amdt. 4. There are various elements, of course, <span class="star-pagination">*184</span> that can make a search of a person's house "reasonable"one of which is the consent of the person or his cotenant. The essence of respondent's argument is that we should impose upon this element a requirement that we have not imposed upon other elements that regularly compel government officers to exercise judgment regarding the facts: namely, the requirement that their judgment be not only responsible but correct.</p>
<p>The fundamental objective that alone validates all unconsented government searches is, of course, the seizure of persons who have committed or are about to commit crimes, or of evidence related to crimes. But "reasonableness," with respect to this necessary element, does not demand that the government be factually correct in its assessment that that is what a search will produce. Warrants need only be supported by "probable cause," which demands no more than a proper "assessment of probabilities in particular factual contexts . . . ." <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 232</a></span> (1983). If a magistrate, based upon seemingly reliable but factually inaccurate information, issues a warrant for the search of a house in which the sought-after felon is not present, has never been present, and was never likely to have been present, the owner of that house suffers one of the inconveniences we all expose ourselves to as the cost of living in a safe society; he does not suffer a violation of the Fourth Amendment.</p>
<p>Another element often, though not invariably, required in order to render an unconsented search "reasonable" is, of course, that the officer be authorized by a valid warrant. Here also we have not held that "reasonableness" precludes error with respect to those factual judgments that law enforcement officials are expected to make. In <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79</a></span> (1987), a warrant supported by probable cause with respect to one apartment was erroneously issued for an entire floor that was divided (though not clearly) into two apartments. We upheld the search of the apartment not properly covered by the warrant. We said:</p>
<blockquote>
<span class="star-pagination">*185</span> "[T]he validity of the search of respondent's apartment pursuant to a warrant authorizing the search of the entire third floor depends on whether the officers' failure to realize the overbreadth of the warrant was objectively understandable and reasonable. Here it unquestionably was. The objective facts available to the officers at the time suggested no distinction between [the suspect's] apartment and the third-floor premises." <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#88" aria-description="Citation for case: Maryland v. Garrison"><i>Id.,</i> at 88</a></span>.</blockquote>
<p>The ordinary requirement of a warrant is sometimes supplanted by other elements that render the unconsented search "reasonable." Here also we have not held that the Fourth Amendment requires factual accuracy. A warrant is not needed, for example, where the search is incident to an arrest. In <i>Hill</i> v. <i>California,</i> <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U. S. 797</a></span> (1971), we upheld a search incident to an arrest, even though the arrest was made of the wrong person. We said:</p>
<blockquote>"The upshot was that the officers in good faith believed Miller was Hill and arrested him. They were quite wrong as it turned out, and subjective good-faith belief would not in itself justify either the arrest or the subsequent search. But sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers' mistake was understandable and the arrest a reasonable response to the situation facing them at the time." <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#803" aria-description="Citation for case: Hill v. California"><i>Id.,</i> at 803-804</a></span>.</blockquote>
<p>It would be superfluous to multiply these examples. It is apparent that in order to satisfy the "reasonableness" requirement of the Fourth Amendment, what is generally demanded of the many factual determinations that must regularly be made by agents of the governmentwhether the magistrate issuing a warrant, the police officer executing a warrant, or the police officer conducting a search or seizure under one of the exceptions to the warrant requirementis not that they always be correct, but that they always be reasonable. <span class="star-pagination">*186</span> As we put it in <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949):</p>
<blockquote>"Because many situations which confront officers in the course of executing their duties are more or less ambiguous, room must be allowed for some mistakes on their part. But the mistakes must be those of reasonable men, acting on facts leading sensibly to their conclusions of probability."</blockquote>
<p>We see no reason to depart from this general rule with respect to facts bearing upon the authority to consent to a search. Whether the basis for such authority exists is the sort of recurring factual question to which law enforcement officials must be expected to apply their judgment; and all the Fourth Amendment requires is that they answer it reasonably. The Constitution is no more violated when officers enter without a warrant because they reasonably (though erroneously) believe that the person who has consented to their entry is a resident of the premises, than it is violated when they enter without a warrant because they reasonably (though erroneously) believe they are in pursuit of a violent felon who is about to escape. See <i>Archibald</i> v. <i>Mosel,</i> <span class="citation" data-id="403411"><a href="/opinion/403411/tonora-archibald-v-charles-mosel/" aria-description="Citation for case: Tonora Archibald v. Charles Mosel">677 F. 2d 5</a></span> (CA1 1982).<sup>[*]</sup></p>
<p><span class="star-pagination">*187</span> <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span> (1964), is in our view not to the contrary. There, in holding that police had improperly entered the defendant's hotel room based on the consent of a hotel clerk, we stated that "the rights protected by the Fourth Amendment are not to be eroded . . . by unrealistic doctrines of `apparent authority.'" <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#488" aria-description="Citation for case: Stoner v. California"><i>Id.,</i> at 488</a></span>. It is ambiguous, of course, whether the word "unrealistic" is descriptive or limitingthat is, whether we were condemning as unrealistic all reliance upon apparent authority, or whether we were condemning only such reliance upon apparent authority as is unrealistic. Similarly ambiguous is the opinion's earlier statement that "there [is no] substance to the claim that the search was reasonable because the police, relying upon the night clerk's expressions of consent, had a reasonable basis for the belief that the clerk had authority to consent to the search." <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Ibid.</a></span></i> Was there no substance to it because it failed as a matter of law, or because the facts could not possibly support it? At one point the opinion does seem to speak clearly:</p>
<blockquote>"It is important to bear in mind that it was the petitioner's constitutional right which was at stake here, and not the night clerk's nor the hotel's. It was a right, therefore, which only the petitioner could waive by word or deed, either directly or through an agent." <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#489" aria-description="Citation for case: Stoner v. California"><i>Id.,</i> at 489</a></span>.</blockquote>
<p>But as we have discussed, what is at issue when a claim of apparent consent is raised is not whether the right to be free of searches has been <i>waived,</i> but whether the right to be free of <i>unreasonable</i> searches has been <i>violated.</i> Even if one does not think the <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i> opinion had this subtlety in mind, the supposed clarity of its foregoing statement is immediately compromised, as follows:</p>
<blockquote>
<span class="star-pagination">*188</span> "It is true that the night clerk clearly and unambiguously consented to the search. But there is nothing in the record to indicate that <i>the police had any basis whatsoever to believe that</i> the night clerk had been authorized by the petitioner to permit the police to search the petitioner's room." <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Ibid.</a></span></i> (emphasis added).</blockquote>
<p>The italicized language should have been deleted, of course, if the statement two sentences earlier meant that an appearance of authority could never validate a search. In the last analysis, one must admit that the rationale of <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i> was ambiguousand perhaps deliberately so. It is at least a reasonable reading of the case, and perhaps a preferable one, that the police could not rely upon the obtained consent because they knew it came from a hotel clerk, knew that the room was rented and exclusively occupied by the defendant, and could not reasonably have believed that the former had general access to or control over the latter. Similarly ambiguous in its implications (the Court's opinion does not even allude to, much less discuss the effects of, "reasonable belief'") is <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span> (1961). In sum, we were correct in <i>Matlock,</i> <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#177" aria-description="Citation for case: United States v. Matlock">415 U. S., at 177, n. 14</a></span>, when we regarded the present issue as unresolved.</p>
<p>As <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i> demonstrates, what we hold today does not suggest that law enforcement officers may always accept a person's invitation to enter premises. Even when the invitation is accompanied by an explicit assertion that the person lives there, the surrounding circumstances could conceivably be such that a reasonable person would doubt its truth and not act upon it without further inquiry. As with other factual determinations bearing upon search and seizure, determination of consent to enter must "be judged against an objective standard: would the facts available to the officer at the moment. . . `warrant a man of reasonable caution in the belief'" that the consenting party had authority over the premises? <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21-22</a></span> (1968). If not, then warrantless <span class="star-pagination">*189</span> entry without further inquiry is unlawful unless authority actually exists. But if so, the search is valid.</p>
<p></p>
<h2>* * *</h2>
<p>In the present case, the Appellate Court found it unnecessary to determine whether the officers reasonably believed that Fischer had the authority to consent, because it ruled as a matter of law that a reasonable belief could not validate the entry. Since we find that ruling to be in error, we remand for consideration of that question. The judgment of the Illinois Appellate Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p>JUSTICE MARSHALL, with whom JUSTICE BRENNAN and JUSTICE STEVENS join, dissenting.</p>
<p>Dorothy Jackson summoned police officers to her house to report that her daughter Gail Fischer had been beaten. Fischer told police that Ed Rodriguez, her boyfriend, was her assaulter. During an interview with Fischer, one of the officers asked if Rodriguez dealt in narcotics. Fischer did not respond. Fischer did agree, however, to the officers' request to let them into Rodriguez's apartment so that they could arrest him for battery. The police, without a warrant and despite the absence of an exigency, entered Rodriguez's home to arrest him. As a result of their entry, the police discovered narcotics that the State subsequently sought to introduce in a drug prosecution against Rodriguez.</p>
<p>The majority agrees with the Illinois Appellate Court's determination that Fischer did not have authority to consent to the officers' entry of Rodriguez's apartment. <i>Ante,</i> at 181-182. The Court holds that the warrantless entry into Rodriguez's home was nonetheless valid if the officers reasonably believed that Fischer had authority to consent. <i>Ante</i> this page. The majority's defense of this position rests on a misconception of the basis for third-party consent searches. That <span class="star-pagination">*190</span> such searches do not give rise to claims of constitutional violations rests not on the premise that they are "reasonable" under the Fourth Amendment, see <i>ante,</i> at 183-184, but on the premise that a person may voluntarily limit his expectation of privacy by allowing others to exercise authority over his possessions. Cf. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967) ("What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection"). Thus, an individual's decision to permit another "joint access [to] or control [over the property] for most purposes," <i>United States</i> v. <i>Matlock,</i> <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#171" aria-description="Citation for case: United States v. Matlock">415 U. S. 164, 171, n. 7</a></span> (1974), limits that individual's reasonable expectation of privacy and to that extent limits his Fourth Amendment protections. Cf. <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#148" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 148</a></span> (1978) (because passenger in car lacked "legitimate expectation of privacy in the glove compartment," Court did not decide whether search would violate Fourth Amendment rights of someone who had such expectation). If an individual has not so limited his expectation of privacy, the police may not dispense with the safeguards established by the Fourth Amendment.</p>
<p>The baseline for the reasonableness of a search or seizure in the home is the presence of a warrant. <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989). Indeed, "searches and seizures inside a home without a warrant are presumptively unreasonable." <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980). Exceptions to the warrant requirement must therefore serve "compelling" law enforcement goals. <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 394</a></span> (1978). Because the sole law enforcement purpose underlying third-party consent searches is avoiding the inconvenience of securing a warrant, a departure from the warrant requirement is not justified simply because an officer reasonably believes a third party has consented to a search of the defendant's home. In holding otherwise, the majority ignores our longstanding view that "the informed and deliberate determinations <span class="star-pagination">*191</span> of magistrates . . . as to what searches and seizures are permissible under the Constitution are to be preferred over the hurried action of officers and others who may happen to make arrests." <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 464</a></span> (1932).</p>
<p></p>
<h2>I</h2>
<p>The Fourth Amendment provides that "[t]he right of the people to be secure in their . . . houses . . . shall not be violated." We have recognized that the "physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed." <i>United States</i> v. <i>United States District Court, Eastern District of Michigan,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972). We have further held that "a search or seizure carried out on a suspect's premises without a warrant is <i>per se</i> unreasonable, unless the police can show that it falls within one of a carefully defined set of exceptions." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474</a></span> (1971). Those exceptions must be crafted in light of the warrant requirement's purposes. As this Court stated in <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948):</p>
<blockquote>"The presence of a search warrant serves a high function. Absent some grave emergency, the Fourth Amendment has interposed a magistrate between the citizen and the police. This was done not to shield criminals nor to make the home a safe haven for illegal activities. It was done so that an objective mind might weigh the need to invade that privacy in order to enforce the law. The right of privacy was deemed too precious to entrust to the discretion of those whose job is the detection of crime and the arrest of criminals." <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States"><i>Id.,</i> at 455-456</a></span>.</blockquote>
<p>The Court has tolerated departures from the warrant requirement only when an exigency makes a warrantless search imperative to the safety of the police and of the community. See, <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States"><i>e. g., id.,</i> at 456</a></span> ("We cannot be true to that <span class="star-pagination">*192</span> constitutional requirement and excuse the absence of a search warrant without a showing by those who seek exemption from the constitutional mandate that the exigencies of the situation made that course imperative"); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967) (hot pursuit); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969) (interest in officers' safety justifies search incident to an arrest); <i>Michigan</i> v. <i>Tyler,</i> <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 509</a></span> (1978) ("compelling need for official action and no time to secure a warrant" justifies warrantless entry of burning building). The Court has often heard, and steadfastly rejected, the invitation to carve out further exceptions to the warrant requirement for searches of the home because of the burdens on police investigation and prosecution of crime. Our rejection of such claims is not due to a lack of appreciation of the difficulty and importance of effective law enforcement, but rather to our firm commitment to "the view of those who wrote the Bill of Rights that the privacy of a person's home and property may not be totally sacrificed in the name of maximum simplicity in enforcement of the criminal law." <i><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey, supra,</a></span></i> at 393 (citing <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#6" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 6-11</a></span> (1977)).</p>
<p>In the absence of an exigency, then, warrantless home searches and seizures are unreasonable under the Fourth Amendment. The weighty constitutional interest in preventing unauthorized intrusions into the home overrides any law enforcement interest in relying on the reasonable but potentially mistaken belief that a third party has authority to consent to such a search or seizure. Indeed, as the present case illustrates, only the minimal interest in avoiding the inconvenience of obtaining a warrant weighs in on the law enforcement side.</p>
<p>Against this law enforcement interest in expediting arrests is "the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion." <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span> (1961). To be sure, in some cases in which police officers reasonably rely on a <span class="star-pagination">*193</span> third party's consent, the consent will prove valid, no intrusion will result, and the police will have been spared the inconvenience of securing a warrant. But in other cases, such as this one, the authority claimed by the third party will be false. The reasonableness of police conduct must be measured in light of the possibility that the target has not consented. Where "[n]o reason is offered for not obtaining a search warrant except the inconvenience to the officers and some slight delay necessary to prepare papers and present the evidence to a magistrate," the Constitution demands that the warrant procedure be observed. <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 15</a></span> (1948). The concerns of expediting police work and avoiding paperwork "are never very convincing reasons and, in these circumstances, certainly are not enough to by-pass the constitutional requirement." <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Ibid.</a></span></i> In this case, as in <i>Johnson,</i> "[n]o suspect was fleeing or likely to take flight. The search was of permanent premises, not of a movable vehicle. No evidence or contraband was threatened with removal or destruction . . . . If the officers in this case were excused from the constitutional duty of presenting their evidence to a magistrate, it is difficult to think of a case in which it should be required." <i>Ibid.</i></p>
<p>Unlike searches conducted pursuant to the recognized exceptions to the warrant requirement, see <i>supra,</i> at 191-192, third-party consent searches are not based on an exigency and therefore serve no compelling social goal. Police officers, when faced with the choice of relying on consent by a third party or securing a warrant, should secure a warrant and must therefore accept the risk of error should they instead choose to rely on consent.</p>
<p></p>
<h2>II</h2>
<p>Our prior cases discussing searches based on third-party consent have never suggested that such searches are "reasonable." In <i>United States</i> v. <i><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">Matlock</a></span></i><i>,</i> this Court upheld a warrantless search conducted pursuant to the consent of a <span class="star-pagination">*194</span> third party who was living with the defendant. The Court rejected the defendant's challenge to the search, stating that a person who permits others to have "joint access or control for most purposes . . . assume[s] the risk that [such persons] might permit the common area to be searched." <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#171" aria-description="Citation for case: United States v. Matlock">415 U. S., at 171, n. 7</a></span>; see also <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#740" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 740</a></span> (1969) (holding that defendant who left a duffel bag at another's house and allowed joint use of the bag "assumed the risk that [the person] would allow someone else to look inside"). As the Court's assumption-of-risk analysis makes clear, third-party consent limits a person's ability to challenge the reasonableness of the search only because that person voluntarily has relinquished some of his expectation of privacy by sharing access or control over his property with another person.</p>
<p>A search conducted pursuant to an officer's reasonable but mistaken belief that a third party had authority to consent is thus on an entirely different constitutional footing from one based on the consent of a third party who in fact has such authority. Even if the officers reasonably believed that Fischer had authority to consent, she did not, and Rodriguez's expectation of privacy was therefore undiminished. Rodriguez accordingly can challenge the warrantless intrusion into his home as a violation of the Fourth Amendment. This conclusion flows directly from <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span> (1964). There, the Court required the suppression of evidence seized in reliance on a hotel clerk's consent to a warrantless search of a guest's room. The Court reasoned that the guest's right to be free of unwarranted intrusion "was a right . . . which only [he] could waive by word or deed, either directly or through an agent." <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#489" aria-description="Citation for case: Stoner v. California"><i>Id.,</i> at 489</a></span>. Accordingly, the Court rejected resort to "unrealistic doctrines of `apparent authority'" as a means of upholding the search to which the guest had not consented. <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#488" aria-description="Citation for case: Stoner v. California"><i>Id.,</i> at 488</a></span>.<sup>[1]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*195</span> III</h2>
<p>Acknowledging that the third party in this case lacked authority to consent, the majority seeks to rely on cases suggesting that reasonable but mistaken factual judgments by police will not invalidate otherwise reasonable searches. The majority reads these cases as establishing a "general rule" that "what is generally demanded of the many factual determinations that must regularly be made by agents of the governmentwhether the magistrate issuing a warrant, the police officer executing a warrant, or the police officer conducting a search or seizure under one of the exceptions to the <span class="star-pagination">*196</span> warrant requirementis not that they always be correct, but that they always be reasonable." <i>Ante,</i> at 185-186.</p>
<p>The majority's assertion, however, is premised on the erroneous assumption that third-party consent searches are generally reasonable. The cases the majority cites thus provide no support for its holding. In <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), for example, the Court confirmed the unremarkable proposition that police need only probable cause, not absolute certainty, to justify the arrest of a suspect on a highway. As <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span></i> makes clear, the possibility of factual error is built into the probable cause standard, and such a standard, by its very definition, will in some cases result in the arrest of a suspect who has not actually committed a crime. Because probable cause defines the reasonableness of searches and seizures outside of the home, a search is reasonable under the Fourth Amendment whenever that standard is met, notwithstanding the possibility of "mistakes" on the part of police. <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States"><i>Id.,</i> at 176</a></span>. In contrast, our cases have already struck the balance against warrantless home intrusions in the absence of an exigency. See <i>supra,</i> at 191-192. Because reasonable factual errors by law enforcement officers will not validate unreasonable searches, the reasonableness of the officer's mistaken belief that the third party had authority to consent is irrelevant.<sup>[2]</sup></p>
<p><span class="star-pagination">*197</span> The majority's reliance on <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79</a></span> (1987), is also misplaced. In <i><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">Garrison</a></span>,</i> the police obtained a valid warrant for the search of the "third floor apartment" of a building whose third floor in fact housed two apartments. <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#80" aria-description="Citation for case: Maryland v. Garrison"><i>Id.,</i> at 80</a></span>. Although the police had probable cause to search only one of the apartments, they entered both apartments because "[t]he objective facts available to the officers at the time suggested no distinction between [the apartment for which they legitimately had the warrant and the entire third floor]." <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#88" aria-description="Citation for case: Maryland v. Garrison"><i>Id.,</i> at 88</a></span>. The Court held that the officers' reasonable mistake of fact did not render the search unconstitutional. <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#88" aria-description="Citation for case: Maryland v. Garrison"><i>Id.,</i> at 88-89</a></span>. As in <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span>,</i> the Court's decision was premised on the general reasonableness of the type of police action involved. Because searches based on warrants are generally reasonable, the officers' reasonable mistake of fact did not render their search "unreasonable." This reasoning is evident in the Court's conclusion that little would be gained by adopting additional burdens "over and above the bedrock requirement that, with the exceptions we have traced in our cases, the police may conduct searches only pursuant to a reasonably detailed warrant." <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#89" aria-description="Citation for case: Maryland v. Garrison"><i>Garrison, supra,</i> at 89, n. 14</a></span>.</p>
<p><i>Garrison,</i> like <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span>,</i> thus tells us nothing about the reasonableness under the Fourth Amendment of a warrantless arrest in the home based on an officer's reasonable but mistaken belief that the third party consenting to the arrest was empowered to do so. The majority's glib assertion that "[i]t would be superfluous to multiply" its citations to cases like <i>Brinegar, Hill,</i> and <i>Garrison, ante,</i> at 185, is thus correct, but for a reason entirely different than the majority suggests. Those cases provide no illumination of the issue raised in this case, and further citation to like cases would be <span class="star-pagination">*198</span> as superfluous as the discussion on which the majority's conclusion presently depends.</p>
<p></p>
<h2>IV</h2>
<p>Our cases demonstrate that third-party consent searches are free from constitutional challenge only to the extent that they rest on consent by a party empowered to do so. The majority's conclusion to the contrary ignores the legitimate expectations of privacy on which individuals are entitled to rely. That a person who allows another joint access to his property thereby limits his expectation of privacy does not justify trampling the rights of a person who has not similarly relinquished any of his privacy expectation.</p>
<p>Instead of judging the validity of consent searches, as we have in the past, based on whether a defendant has in fact limited his expectation of privacy, the Court today carves out an additional exception to the warrant requirement for third-party consent searches without pausing to consider whether "`the exigencies of the situation' make the needs of law enforcement so compelling that the warrantless search is objectively reasonable under the Fourth Amendment," <i>Mincey,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona">437 U. S., at 394</a></span> (citations omitted). Where this free-floating creation of "reasonable" exceptions to the warrant requirement will end, now that the Court has departed from the balancing approach that has long been part of our Fourth Amendment jurisprudence, is unclear. But by allowing a person to be subjected to a warrantless search in his home without his consent and without exigency, the majority has taken away some of the liberty that the Fourth Amendment was designed to protect.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the State of California by <i>John K. Van de Kamp,</i> Attorney General, <i>Richard B. Iglehart,</i> Chief Assistant Attorney General, <i>John H. Sugiyama,</i> Senior Assistant Attorney General, and <i>Ronald S. Matthias</i> and <i>Clifford K. Thompson, Jr.,</i> Deputy Attorneys General; and for Americans for Effective Law Enforcement, Inc., et al. by <i>Gregory U. Evans, Daniel B. Hales, George D. Webster, Joseph A. Morris, Jack E. Yelverton, Fred E. Inbau, Wayne W. Schmidt, Bernard J. Farber,</i> and <i>James P. Manak.</i>
</p>
<p><i>Benjamin S. Waxman</i> and <i>Jeffrey S. Weiner</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p>[*]  JUSTICE MARSHALL's dissent rests upon a rejection of the proposition that searches pursuant to valid third-party consent are "generally reasonable." <i>Post,</i> at 196. Only a warrant or exigent circumstances, he contends, can produce "reasonableness"; consent validates the search only because the object of the search thereby "limit[s] his expectation of privacy," <i>post,</i> at 198, so that the search becomes not really a search at all. We see no basis for making such an artificial distinction. To describe a consented search as a noninvasion of privacy and thus a nonsearch is strange in the extreme. And while it must be admitted that this ingenious device can explain why consented searches are lawful, it cannot explain why seemingly consented searches are "unreasonable," which is all that the Constitution forbids. See <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653-654</a></span> (1979) ("The essential purpose of the proscriptions in the Fourth Amendment is to impose a standard of `reasonableness' upon the exercise of discretion by government officials"). The only basis for contending that the constitutional standard could not possibly have been met here is the argument that reasonableness must be judged by the facts as they were, rather than by the facts as they were known. As we have discussed in text, that argument has long since been rejected.</p>
<p>[1]  The majority insists that the rationale of <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i> is "ambiguousand perhaps deliberately so" with respect to the permissibility of third-party searches where the suspect has not conferred actual authority on the third party. <i>Ante,</i> at 188. <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i> itself is clear, however; today's majority manufactures the ambiguity. When the <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i> Court stated that the Fourth Amendment is not to be eroded "by unrealistic doctrines of `apparent authority,'" <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#488" aria-description="Citation for case: Stoner v. California">376 U. S., at 488</a></span>, and that "only the petitioner could waive by word or deed" his freedom from a warrantless search, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#489" aria-description="Citation for case: Stoner v. California"><i>id.,</i> at 489</a></span>, the Court rejected precisely the proposition that the majority today adopts.
</p>
<p>The majority regards <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i>'s rejection of "unrealistic doctrines of `apparent authority'" as ambiguous on the theory that the Court might have been referring only to unreasonable <i>applications</i> of such doctrines and not to the doctrines themselves. <i>Ante,</i> at 187. But <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i>'s express description of apparent authority <i>doctrines</i> as unrealistic cannot be viewed as mere happenstance. The Court in fact used the word "applications" in the same sentence to refer to misapplications of the <i>actual</i> authority doctrine: "Our decisions make clear that the rights protected by the Fourth Amendment are not to be eroded by strained applications of the law of agency <i>or</i> by unrealistic doctrines of `apparent authority.'" <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#488" aria-description="Citation for case: Stoner v. California">376 U. S., at 488</a></span> (emphasis added). The full sentence thus unambiguously confirms that <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i> rejected any reliance on <i>apparent</i> authority doctrines.</p>
<p>Nor did the <i><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">Stoner</a></span></i> Court leave open the door for a police officer to rely on a reasonable but mistaken belief in a third party's authority to consent when it remarked that "there is nothing in the record to indicate that the police had any basis whatsoever to believe that the night clerk had been authorized by the petitioner to permit the police to search the petitioner's room." <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#489" aria-description="Citation for case: Stoner v. California"><i>Id.,</i> at 489</a></span>. Stating that a defendant must "by word or deed" waive his rights, <i>ibid.,</i> is not inconsistent with noting that, in a particular case, the absence of actual waiver is confirmed by the police's inability to identify any basis for their contention that waiver had indeed occurred.</p>
<p>[2]  The same analysis applies to <i>Hill</i> v. <i>California,</i> <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U. S. 797</a></span> (1971), where the Court upheld a search incident to an arrest in which officers reasonably but mistakenly believed that the person arrested in the defendant's home was the defendant. The Court refused to disturb the state court's holding that "`[w]hen the police have probable cause to arrest one party, and when they reasonably mistake a second party for the first party, then the arrest of the second party is a valid arrest.'" <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#802" aria-description="Citation for case: Hill v. California"><i>Id.,</i> at 802</a></span> (brackets in original) (quoting <i>People</i> v. <i>Hill,</i> <span class="citation" data-id="1129895"><a href="/opinion/1129895/people-v-hill/#553" aria-description="Citation for case: People v. Hill">69 Cal. 2d 550, 553</a></span>, <span class="citation" data-id="1129895"><a href="/opinion/1129895/people-v-hill/#523" aria-description="Citation for case: People v. Hill">446 P. 2d 521, 523</a></span> (1968)). Given that the Court decided <i>Hill</i> before the extension of the warrant requirement to arrests in the home, <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), <i>Hill</i> should be understood no less than <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span></i> as simply a gloss on the meaning of "probable cause." The holding in <i>Hill</i> rested on the fact that the police had probable cause to believe that Hill had committed a crime. In such circumstances, the reasonableness of the arrest for which the police had probable cause was not undermined by the officers' factual mistake regarding the identity of the person arrested.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Illinois v. Wardlow.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Illinois v. Wardlow"
type: case
citation: "528 U.S. 119 (2000)"
parallel_cite: "120 S. Ct. 673; 145 L. Ed. 2d 570"
neutral_cite: 2000 U.S. LEXIS 504
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2000
date_decided: 2000-01-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2000-01-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Wardlow
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118326/illinois-v-wardlow/"
  cluster_id: 118326
  opinion_id: 9433881
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[Florida v. J.L.]]", "[[Alabama v. White]]", "[[Brown v. Texas]]"]
aliases: []
tags: ["case", "fourth-amendment", "reasonable-suspicion", "terry-stop", "flight", "high-crime-area"]
holding: "Unprovoked headlong flight upon noticing police, combined with presence in a high-crime area, can furnish reasonable suspicion for a…"
lake:
  record_id: Illinois v. Wardlow
  status: verified
  projected_at: 2026-07-09
---

# Illinois v. Wardlow

*528 U.S. 119 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers in a four-car caravan converged on a Chicago area known for heavy narcotics trafficking. Officer Nolan saw Wardlow standing next to a building holding an opaque bag; when Wardlow looked at the officers, he fled. Nolan caught him, conducted a protective pat-down, felt a hard object, and found a handgun. Wardlow moved to suppress the gun, arguing the stop lacked reasonable suspicion.

## Issue
Whether unprovoked flight upon noticing the police, in an area of heavy narcotics trafficking, can furnish the reasonable suspicion needed for a *[[Terry v. Ohio|Terry]]* stop.

## Rule
Yes. "Our cases have also recognized that nervous, evasive behavior is a pertinent factor in determining reasonable suspicion." — 528 U.S. at 124. ^pin-124

"Headlong flight—wherever it occurs—is the consummate act of evasion: It is not necessarily indicative of wrongdoing, but it is certainly suggestive of such." — [*Id.*](https://www.courtlistener.com/opinion/118326/illinois-v-wardlow/#:~:text=Headlong%20flight%E2%80%94wherever%20it%20occurs%E2%80%94is%20the) ^pin-124a

Location is also a relevant consideration: "An individual's presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime. But officers are not required to ignore the relevant characteristics of a location in determining whether the circumstances are sufficiently suspicious to warrant further investigation." — *Id.* ^pin-124b

## Application
Wardlow was present in an area of heavy narcotics trafficking and engaged in unprovoked, headlong flight the moment he noticed the police. Taking those facts together — the high-crime location as context plus the evasive flight — Officer Nolan had reasonable suspicion that Wardlow was involved in criminal activity, justifying the *[[Terry v. Ohio|Terry]]* stop and the protective pat-down that uncovered the handgun.

## Conclusion
The stop was supported by reasonable suspicion; the judgment suppressing the handgun was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Wardlow* applies the reasonable-suspicion standard of [[Terry v. Ohio]], treating unprovoked flight in a high-crime area as supplying reasonable suspicion under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Appears on
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *Illinois v. Wardlow*, 528 U.S. 119 (2000) — https://www.courtlistener.com/opinion/118326/illinois-v-wardlow/ — pinpoint: 124.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b5b96b492f971b4c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Wardlow"}, "payload": {"all": [{"cite": "528 U.S. 119", "page": "119", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "528"}, {"cite": "120 S. Ct. 673", "page": "673", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "120"}, {"cite": "145 L. Ed. 2d 570", "page": "570", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "145"}, {"cite": "2000 U.S. LEXIS 504", "page": "504", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2000"}], "display": "528 U.S. 119", "official": {"cite": "528 U.S. 119", "page": "119", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "528"}, "official_selection_present": true, "record_id": "Illinois v. Wardlow"}}
{"assertion_id": "4036ab833e871c80", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-124", "record_id": "Illinois v. Wardlow"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-124", "pinpoint_status": "slip-only", "quote": "--- # Illinois v. Wardlow *528 U.S. 119 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers in a four-car caravan converged on a Chicago area known for heavy narcotics trafficking. Officer Nolan saw Wardlow standing next to a building holding an opaque bag; when Wardlow looked at the officers, he fled. Nolan caught him, conducted a protective pat-down, felt a hard object, and found a handgun. Wardlow moved to suppress the gun, arguing the stop lacked reasonable suspicion. ## Issue Whether unprovoked flight upon noticing the police, in an area of heavy narcotics trafficking, can furnish the reasonable suspicion needed for a *Terry* stop. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Wardlow", "star_marker": null}}
{"assertion_id": "965c3de5f94b9152", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-124b", "record_id": "Illinois v. Wardlow"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-124b", "pinpoint_status": "slip-only", "quote": "An individual's presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime. But officers are not required to ignore the relevant characteristics of a location in determining whether the circumstances are sufficiently suspicious to warrant further investigation.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Wardlow", "star_marker": null}}
{"assertion_id": "a29d80fb7444499f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-124a", "record_id": "Illinois v. Wardlow"}, "payload": {"fragment": "#:~:text=Headlong%20flight%E2%80%94wherever%20it%20occurs%E2%80%94is%20the", "page": null, "pin_id": "pin-124a", "pinpoint_status": "star-verified", "quote": "Headlong flight—wherever it occurs—is the consummate act of evasion: It is not necessarily indicative of wrongdoing, but it is certainly suggestive of such.", "quote_fidelity": "matched", "record_id": "Illinois v. Wardlow", "star_marker": "124"}}
{"assertion_id": "dcb47c34c2c3a5bd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Wardlow"}, "payload": {"as_of_content": "2000-01-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Wardlow", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Illinois v. Wardlow

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Wardlow",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Wardlow",
    "case_name_short": "Wardlow",
    "case_name_full": "Illinois v. Wardlow",
    "input_case_name": "Illinois v. Wardlow",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2000-01-19",
    "year": 2000,
    "docket": null,
    "cluster_id": 118326,
    "lead_opinion_id": 9433881,
    "sibling_ids": [
      118326,
      9433881,
      9433882
    ],
    "absolute_url": "/opinion/118326/illinois-v-wardlow/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "528 U.S. 119",
      "volume": "528",
      "reporter": "U.S.",
      "page": "119",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "120 S. Ct. 673",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "145 L. Ed. 2d 570",
        "volume": "145",
        "reporter": "L. Ed. 2d",
        "page": "570",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. LEXIS 504",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "504",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "528 U.S. 119",
        "volume": "528",
        "reporter": "U.S.",
        "page": "119",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "120 S. Ct. 673",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "145 L. Ed. 2d 570",
        "volume": "145",
        "reporter": "L. Ed. 2d",
        "page": "570",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. LEXIS 504",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "504",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "528 U.S. 119",
    "official_selection": {
      "court_class": "scotus",
      "selected": "528 U.S. 119",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-124",
      "page": null,
      "quote": "--- # Illinois v. Wardlow *528 U.S. 119 (2000)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers in a four-car caravan converged on a Chicago area known for heavy narcotics trafficking. Officer Nolan saw Wardlow standing next to a building holding an opaque bag; when Wardlow looked at the officers, he fled. Nolan caught him, conducted a protective pat-down, felt a hard object, and found a handgun. Wardlow moved to suppress the gun, arguing the stop lacked reasonable suspicion. ## Issue Whether unprovoked flight upon noticing the police, in an area of heavy narcotics trafficking, can furnish the reasonable suspicion needed for a *Terry* stop. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-124a",
      "page": null,
      "quote": "Headlong flight\u2014wherever it occurs\u2014is the consummate act of evasion: It is not necessarily indicative of wrongdoing, but it is certainly suggestive of such.",
      "star_marker": "124",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10036,
      "fragment": "#:~:text=Headlong%20flight%E2%80%94wherever%20it%20occurs%E2%80%94is%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-124b",
      "page": null,
      "quote": "An individual's presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime. But officers are not required to ignore the relevant characteristics of a location in determining whether the circumstances are sufficiently suspicious to warrant further investigation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-01-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Wardlow",
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
        "journal_ref": "Illinois v. Wardlow:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Connecticut State University Organization of Administrative Faculty, AFSCME, Council 4, Local 2836, AFL-CIO",
          "cluster_id": 10131753,
          "cite": [
            "349 Conn. 148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane1_negative"
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
        "journal_ref": "Illinois v. Wardlow:lane1_negative"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balentine v. State",
          "cluster_id": 1662103,
          "cite": [
            "71 S.W.3d 763",
            "2002 WL 496960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peso Chavez and Gregory Lee, Individually and on Behalf of All Persons Similarly Situated v. The Illinois State Police, Terrance W. Gainer, Individually and in His Official Capacity as Director of the Illinois State Police, Michael Snyders, Individually and in His Official Capacity as Illinois State Police Operation Valkyrie Coordinator, Edward Kresl, Individually and in His Official Capacity as District Commander of the Illinois State Police, and Larry Thomas, Daniel Gillette, Craig Graham, Robert P. Cessna, Robert Lauterbach, and Dale Fraher, Officers of the Illinois State Police, in Their Individual Capacities",
          "cluster_id": 773427,
          "cite": [
            "251 F.3d 612",
            "49 Fed. R. Serv. 3d 1127",
            "2001 U.S. App. LEXIS 10560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. City of New York",
          "cluster_id": 8439619,
          "cite": [
            "478 F.3d 76",
            "2007 U.S. App. LEXIS 2782",
            "2007 WL 415171"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mendoza",
          "cluster_id": 2594735,
          "cite": [
            "6 P.3d 150",
            "99 Cal. Rptr. 2d 485",
            "24 Cal. 4th 130",
            "24 Cal. 130",
            "2000 Daily Journal DAR 9423",
            "2000 Cal. Daily Op. Serv. 7144",
            "2000 Cal. LEXIS 6118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. City Of New York",
          "cluster_id": 796947,
          "cite": [
            "478 F.3d 76"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derichsweiler v. State",
          "cluster_id": 2539048,
          "cite": [
            "348 S.W.3d 906",
            "2011 Tex. Crim. App. LEXIS 112",
            "2011 WL 255299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Christopher Lee Davis",
          "cluster_id": 1043997,
          "cite": [
            "354 S.W.3d 718",
            "2011 Tenn. LEXIS 962"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Huggins",
          "cluster_id": 2575903,
          "cite": [
            "131 P.3d 995",
            "41 Cal. Rptr. 3d 593",
            "38 Cal. 4th 175",
            "2006 Cal. Daily Op. Serv. 2949",
            "2006 Daily Journal DAR 4247",
            "2006 Cal. LEXIS 4393"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Utah v. Strieff",
          "cluster_id": 3214882,
          "cite": [
            "579 U.S. 232",
            "195 L. Ed. 2d 400",
            "2016 U.S. LEXIS 3926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Woodard",
          "cluster_id": 2540788,
          "cite": [
            "341 S.W.3d 404",
            "2011 Tex. Crim. App. LEXIS 447",
            "2011 WL 1261320"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patricia Scott v. Clay County, Tennessee Chinn Anderson Billy Pierce Michael Thompson",
          "cluster_id": 767897,
          "cite": [
            "205 F.3d 867",
            "2000 U.S. App. LEXIS 2965",
            "2000 WL 228300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. German Espinoza Montero-Camargo, United States of America v. Lorenzo Sanchez-Guillen",
          "cluster_id": 768288,
          "cite": [
            "208 F.3d 1122",
            "2000 Daily Journal DAR 3733",
            "2000 Cal. Daily Op. Serv. 2774",
            "2000 U.S. App. LEXIS 6494",
            "2000 WL 364861"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118326 OR 9433881 OR 9433882) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjI2MzA3MjAwMDAwJnM9NDg5OTkwNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118326+OR+9433881+OR+9433882%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118326 OR 9433881 OR 9433882)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjkmcz03NzE2MjQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118326+OR+9433881+OR+9433882%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118326 OR 9433881 OR 9433882)",
        "reviewed": 158,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 158,
        "triage_read": 3,
        "triage_snippet_classified": 155
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118326 OR 9433881 OR 9433882)",
    "indexed_citing_opinions": 2136,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118326,
        "count": 1819,
        "count_source": "search"
      },
      {
        "opinion_id": 9433881,
        "count": 347,
        "count_source": "search"
      },
      {
        "opinion_id": 9433882,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4171,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-wardlow.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0OTg2ODYmcz0xMDY1NjYyNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118326+OR+9433881+OR+9433882%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118326,
        "cited_id": 94334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 94447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 1420729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 1439197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 1613365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2010084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2115969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2116553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2189647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2207148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2239930,
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
    "date_created": "2026-07-05T08:31:25Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:31:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:31:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:36:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:31:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Wardlow

```
<opinion type="majority">
<author id="b333-4"><page-number citation-index="1" label="121">*121</page-number>CHIEF Justice Rehnquist</author>
<p id="Apc">delivered the opinion of the Court.</p>
<p id="b333-5">Respondent Wardlow fled upon seeing police officers patrolling an area known for heavy narcotics trafficking. Two of the officers caught up with him, stopped him, and conducted a protective patdown search for weapons. Discovering a .38-caliber handgun, the officers arrested Wardlow. We hold that the officers’ stop did not violate the Fourth Amendment to the United States Constitution.</p>
<p id="b333-6">On September 9, 1995, Officers Nolan and Harvey were working as uniformed officers in the special operations section of the Chicago Police Department. The officers were driving the last car of a four-car caravan converging on an area known for heavy narcotics trafficking in order to investigate drug transactions. The officers were traveling together because they expected to find a crowd of people in the area, including lookouts and customers.</p>
<p id="b333-7">As the caravan passed 4035 West Van Burén, Officer Nolan observed respondent Wardlow standing next to the building <page-number citation-index="1" label="122">*122</page-number>holding an opaque bag. Respondent looked in the direction of the officers and fled. Nolan and Harvey turned their ear southbound, watched him as he ran through the gangway and an alley, and eventually cornered him on the street. Nolan then exited his ear and stopped respondent. He immediately conducted a protective patdown search for weapons because in his experience it was common for there to be weapons in the near vicinity of narcotics transactions. During the frisk, Officer Nolan squeezed the bag respondent was carrying and felt a heavy, hard object similar to the shape of a gun. The officer then opened the bag and discovered a .38-caliber handgun with five live rounds of ammunition. The officers arrested Wardlow.</p>
<p id="b334-5">The Illinois trial court denied respondent’s motion to suppress, finding the gun was recovered during a lawful stop and frisk. App. 14. Following a stipulated bench trial, Wardlow was convicted of unlawful use of a weapon by a felon. The Illinois Appellate Court reversed Wardlow’s conviction, concluding that the gun should have been suppressed because Officer Nolan did not have reasonable suspicion sufficient to justify an investigative stop pursuant to <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). <span class="citation" data-id="2116553"><a href="/opinion/2116553/people-v-wardlow/" aria-description="Citation for case: People v. Wardlow">287 Ill. App. 3d 367</a></span>, <span class="citation" data-id="2116553"><a href="/opinion/2116553/people-v-wardlow/" aria-description="Citation for case: People v. Wardlow">678 N. E. 2d 65</a></span> (1997).</p>
<p id="b334-6">The Illinois Supreme Court agreed. <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/" aria-description="Citation for case: People v. Wardlow">183 Ill. 2d 306</a></span>, <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/" aria-description="Citation for case: People v. Wardlow">701 N. E. 2d 484</a></span> (1998). While rejecting the Appellate Court’s conclusion that Wardlow was not in a high crime area, the Illinois Supreme Court determined that sudden flight in such an area does not create a reasonable suspicion justifying a <em>Terry </em>stop. <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#310" aria-description="Citation for case: People v. Wardlow">183 Ill. 2d, at 310</a></span>, <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#486" aria-description="Citation for case: People v. Wardlow">701 N. E. 2d, at 486</a></span>. Relying on <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), the court explained that although police have the right to approach individuals and ask questions, the individual has no obligation to respond. The person may decline to answer and simply go on his or her way, and the refusal to respond, alone, does not provide a legitimate basis for an investigative stop. <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#311" aria-description="Citation for case: People v. Wardlow">183 Ill. <page-number citation-index="1" label="123">*123</page-number>2d, at 311-312</a></span>, <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#486" aria-description="Citation for case: People v. Wardlow">701 N. E. 2d, at 486-487</a></span>. The court then determined that flight may simply be an exercise of this right to “go on one’s way,” and, thus, could not constitute reasonable suspicion justifying a <em>Terry </em>stop. <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#312" aria-description="Citation for case: People v. Wardlow">183 Ill. 2d, at 312</a></span>, <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#487" aria-description="Citation for case: People v. Wardlow">701 N. E. 2d, at 487</a></span>.</p>
<p id="b335-5">The Illinois Supreme Court also rejected the argument that flight combined with the fact that it occurred in a high crime area supported a finding of reasonable suspicion because the “high crime area” factor was not sufficient standing alone to justify a <em>Terry </em>stop. Finding no independently suspicious circumstances to support an investigatory detention, the court held that the stop and subsequent arrest violated the Fourth Amendment. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./526/1097/">526 U. S. 1097</a></span> (1999), and now reverse.<footnotemark>1</footnotemark></p>
<p id="b335-6">This case, involving a brief encounter between a citizen and a police officer on a public street, is governed by the analysis we first applied in <em>Terry. </em>In <em>Terry, </em>we held that an officer may, consistent with the Fourth Amendment, conduct a brief, investigatory stop when the officer has a reasonable, articulable suspicion that criminal activity is afoot. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 30</a></span>. While “reasonable suspicion” is a less demanding standard than probable cause and requires a showing considerably less than preponderance of the evidence, the Fourth Amendment requires at least a minimal level of objective justification for making the stop. <em>United States </em>v. <em>Sokolow, </em><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7</a></span> (1989). The officer must be able <page-number citation-index="1" label="124">*124</page-number>to articulate more than an “inchoate and unparticularized suspicion or ‘hunch’” of criminal activity. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 27</a></span>.<footnotemark>2</footnotemark></p>
<p id="b336-5">Nolan and Harvey were among eight officers in a four-car caravan that was converging on an area known for heavy narcotics trafficking, and the officers anticipated encountering a large number of people in the area, including drug customers and individuals serving as lookouts. App. 8. It was in this context that Officer Nolan decided to investigate Wardlow after observing him flee. An individual’s presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime. <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979). But officers are not required to <em>ignore </em>the relevant characteristics of a location in determining whether the circumstances are sufficiently suspicious to warrant further investigation. Accordingly, we have previously noted the fact that the stop occurred in a “high crime area” among the relevant contextual considerations in a <em>Terry </em>analysis. <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#144" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 144, 147-148</a></span> (1972).</p>
<p id="b336-6">In this case, moreover, it was not merely respondent’s presence in an area of heavy narcotics trafficking that aroused the officers’ suspicion, but his unprovoked flight upon noticing the police. Our cases have also recognized that nervous, evasive behavior is a pertinent factor in determining reasonable suspicion. <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#885" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 885</a></span> (1975); <em>Florida </em>v. <em>Rodriguez, </em><span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#6" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1, 6</a></span> (1984) <em>(per curiam); United States </em>v. <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#8" aria-description="Citation for case: United States v. Sokolow"><em>Sokolow, supra, </em>at 8-9</a></span>. Headlong flight—wherever it occurs—is the consummate act of evasion: It is not necessarily indicative of wrongdoing, but it is certainly suggestive of such. In reviewing the propriety of an officer’s conduct, courts do not have available empirical studies dealing with inferences drawn from suspicious <page-number citation-index="1" label="125">*125</page-number>behavior, and we cannot reasonably demand scientific certainty from judges or law enforcement officers where none exists. Thus, the determination of reasonable suspicion must be based on eommonsense judgments and inferences about human behavior. See <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981). We conclude Officer Nolan was justified in suspecting that Wardlow was involved in criminal activity, and, therefore, in investigating further.</p>
<p id="b337-5">Such a holding is entirely consistent with our decision in <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), where we held that when an officer, without reasonable suspicion or probable cause, approaches an individual, the individual has a right to ignore the police and go about his business. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#498" aria-description="Citation for case: Florida v. Royer"><em>Id., </em>at 498</a></span>. And any “refusal to cooperate, without more, does not furnish the minimal level of objective justification needed for a detention or seizure.” <em>Florida </em>v. <em>Bostick, </em><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 437</a></span> (1991). But unprovoked flight is simply not a mere refusal to cooperate. Flight, by its very nature, is not “going about one’s business”; in fact, it is just the opposite. Allowing officers confronted with such flight to stop the fugitive and investigate further is quite consistent with the individual’s right to go about his business or to stay put and remain silent in the face of police questioning.</p>
<p id="b337-6">Respondent and <em>amici </em>also argue that there are innocent reasons for flight from police and that, therefore, flight is not necessarily indicative of ongoing criminal activity. This fact is undoubtedly true, but does not establish a violation of the Fourth Amendment. Even in <em>Terry, </em>the conduct justifying the stop was ambiguous and susceptible of an innocent explanation. The officer observed two individuals pacing back and forth in front of a store, peering into the window and periodically conferring. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#5" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 5-6</a></span>. All of this conduct was by itself lawful, but it also suggested that the individuals were casing the store for a planned robbery. <em>Terry </em>recognized that the officers could detain the individuals to resolve the ambiguity. <em>Id., </em>at 30.</p>
<p id="b338-4"><page-number citation-index="1" label="126">*126</page-number>In allowing such detentions, <em>Terry </em>accepts the risk that officers may stop innocent people. Indeed, the Fourth Amendment accepts that risk in connection with more drastic police action; persons arrested and detained on probable cause to believe they have committed a crime may turn out to be innocent. The <em>Terry </em>stop is a far more minimal intrusion, simply allowing the officer to briefly investigate further. If the officer does not learn facts rising to the level of probable cause, the individual must be allowed to go on his way. But in this case the officers found respondent in possession of a handgun, and arrested him for violation of an Illinois firearms statute. No question of the propriety of the arrest itself is before us.</p>
<p id="b338-5">The judgment of the Supreme Court of Illinois is reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b338-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b335-7">The state courts have differed on whether unprovoked flight is sufficient grounds to constitute reasonable suspicion. See, <em>e. g., State </em>v. <em>Anderson, </em><span class="citation" data-id="9736767"><a href="/opinion/2207148/state-v-anderson/" aria-description="Citation for case: State v. Anderson">155 Wis. 2d 77</a></span>, <span class="citation" data-id="9736767"><a href="/opinion/2207148/state-v-anderson/" aria-description="Citation for case: State v. Anderson">454 N. W. 2d 763</a></span> (1990) (flight alone is sufficient); <em>Platt </em>v. <em>State, </em><span class="citation" data-id="9743977"><a href="/opinion/2239930/platt-v-state/" aria-description="Citation for case: Platt v. State">589 N. E. 2d 222</a></span> (Ind. 1992) (same); <em>Harris </em>v. <em>State, </em><span class="citation" data-id="1420729"><a href="/opinion/1420729/harris-v-state/" aria-description="Citation for case: Harris v. State">205 Ga. App. 813</a></span>, <span class="citation" data-id="1420729"><a href="/opinion/1420729/harris-v-state/" aria-description="Citation for case: Harris v. State">423 S. E. 2d 723</a></span> (1992) (flight in high crime area sufficient); <em>State </em>v. <em>Hicks, </em><span class="citation" data-id="1613365"><a href="/opinion/1613365/state-v-hicks/" aria-description="Citation for case: State v. Hicks">241 Neb. 357</a></span>, <span class="citation" data-id="1613365"><a href="/opinion/1613365/state-v-hicks/" aria-description="Citation for case: State v. Hicks">488 N. W. 2d 359</a></span> (1992) (flight is not enough); <em>State </em>v. <em>Tucker, </em>136 N. J. 158, <span class="citation" data-id="2010084"><a href="/opinion/2010084/state-v-tucker/" aria-description="Citation for case: State v. Tucker">642 A. 2d 401</a></span> (1994) (same); <em>People </em>v. <em>Shabaz, </em><span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/" aria-description="Citation for case: People v. Shabaz">424 Mich. 42</a></span>, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d 451</a></span> (1985) (same); <em>People </em>v. <em>Wilson, </em><span class="citation" data-id="1439197"><a href="/opinion/1439197/people-v-wilson/" aria-description="Citation for case: People v. Wilson">784 P. 2d 325</a></span> (Colo. 1989) (same).</p>
</footnote>
<footnote label="2">
<p id="b336-7"> We granted certiorari solely on the question whether the initial stop was supported by reasonable suspicion. Therefore, we express no opinion as to the lawfulness of the frisk independently of the stop.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Imbler v. Pachtman.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Imbler v. Pachtman
type: case
citation: "424 U.S. 409 (1976)"
parallel_cite: "96 S. Ct. 984; 47 L. Ed. 2d 128"
neutral_cite: 1976 U.S. LEXIS 25
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-03-02
docket: No. 74-5435
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
  opinion_url: "https://www.courtlistener.com/opinion/109387/imbler-v-pachtman/"
  cluster_id: 109387
  opinion_id: null
  identity_checked: true
lake:
  record_id: Imbler v. Pachtman
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Absolute Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Buckley v. Fitzsimmons]]"
  - "[[Briscoe v. LaHue]]"
tags:
  - case
  - section-1983
  - prosecutorial-immunity
  - absolute-immunity
  - judicial-phase
holding: "A state prosecutor is absolutely immune from a § 1983 damages suit for conduct intimately associated with the judicial phase of the criminal process — that is, in initiating a prosecution and in presenting the State's case — even where the claim is that the prosecutor knowingly used false testimony and suppressed exculpatory evidence."
aliases:
  - Imbler v. Pachtman
  - "Imbler v. Pachtman (1976)"
---

# Imbler v. Pachtman

*424 U.S. 409 (1976)* (No. 74-5435) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109387 → combined opinion 109387 (Powell, J.; 424 U.S. 409, decided Mar. 2, 1976). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*431`). S9 promotes. -->

## Background
Paul Imbler was convicted of murder in a prosecution handled by deputy district attorney Richard Pachtman. Imbler was later released on federal [[Common Legal Terms#habeas-corpus|habeas]] after evidence emerged that the State's case had rested in part on testimony the prosecutor allegedly knew to be false and on the suppression of [[Brady and Giglio|exculpatory]] material. Imbler then sued Pachtman under § 1983 for damages. The lower courts held the prosecutor absolutely immune from such a suit, and the Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
Whether a state prosecutor may be held liable in damages under § 1983 for allegedly knowingly using false testimony and suppressing [[Brady and Giglio|exculpatory]] evidence in securing a conviction.

## Rule
Drawing on the common-law immunity of prosecutors and the policy reasons behind it, the Court confined its holding to the prosecutor's advocacy role but held that role absolutely immune: "We hold only that in initiating a prosecution and in presenting the State's case, the prosecutor is immune from a civil suit for damages under § 1983." — 424 U.S. at 431. ^pin-431

## Application
Deciding to prosecute and presenting the State's case are functions intimately associated with the judicial phase of the criminal process, and the reasons for absolute immunity — shared with judges and grand jurors — apply with full force: exposing prosecutors to damages suits by every convicted defendant would deflect their energies and distort the independent judgment the office requires. The Court pointedly reserved whether the same immunity covers a prosecutor's administrative or investigative acts, leaving that question for another day.

## Conclusion
The judgment was **affirmed**. Powell, J., delivered the opinion of the Court; White, J. (joined by Brennan and Marshall, JJ.), concurred in the judgment; Stevens, J., took no part in the consideration or decision of the case.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Imbler* is the foundational grant of **absolute prosecutorial immunity** for advocacy. The question it expressly reserved — whether investigative or administrative acts are also absolutely immune — was answered in *[[Buckley v. Fitzsimmons]]* (1993): only **qualified** immunity attaches to a prosecutor's investigative fabrication of evidence and press statements. Teach *Imbler* with *[[Buckley v. Fitzsimmons|Buckley]]* (the advocacy/investigation line) and *[[Briscoe v. LaHue]]* (witness immunity).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Imbler v. Pachtman*, 424 U.S. 409 (1976)](https://www.courtlistener.com/opinion/109387/imbler-v-pachtman/) — pinpoint: 431 (Powell, J., for the Court; the CL opinion text carries the reporter star `*431` immediately before the holding, which sits between `*431` and `*432`). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e4c763c59cb9c00a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Imbler v. Pachtman"}, "payload": {"all": [{"cite": "424 U.S. 409", "page": "409", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "424"}, {"cite": "96 S. Ct. 984", "page": "984", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "47 L. Ed. 2d 128", "page": "128", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "47"}, {"cite": "1976 U.S. LEXIS 25", "page": "25", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "424 U.S. 409", "official": {"cite": "424 U.S. 409", "page": "409", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "424"}, "official_selection_present": true, "record_id": "Imbler v. Pachtman"}}
{"assertion_id": "41aec0c15bfa3612", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Imbler v. Pachtman"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Imbler v. Pachtman", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Imbler v. Pachtman

```json
{
  "schema_version": "s2.v1",
  "record_id": "Imbler v. Pachtman",
  "status": "under_review",
  "identity": {
    "case_name": "Imbler v. Pachtman",
    "case_name_short": "Imbler",
    "case_name_full": "Imbler v. Pachtman, District Attorney",
    "input_case_name": "Imbler v. Pachtman",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-03-02",
    "year": 1976,
    "docket": "No. 74-5435",
    "cluster_id": 109387,
    "lead_opinion_id": 9426281,
    "sibling_ids": [],
    "absolute_url": "/opinion/109387/imbler-v-pachtman/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "424 U.S. 409",
      "volume": "424",
      "reporter": "U.S.",
      "page": "409",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 984",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "984",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "47 L. Ed. 2d 128",
        "volume": "47",
        "reporter": "L. Ed. 2d",
        "page": "128",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 25",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "25",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "424 U.S. 409",
        "volume": "424",
        "reporter": "U.S.",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 984",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "984",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "47 L. Ed. 2d 128",
        "volume": "47",
        "reporter": "L. Ed. 2d",
        "page": "128",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 25",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "25",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "424 U.S. 409",
    "official_selection": {
      "court_class": "scotus",
      "selected": "424 U.S. 409",
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
    "date_created": "2026-07-06T13:53:37Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "imbler-v-pachtman--109387",
      "to_record_id": "Imbler v. Pachtman",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Imbler v. Pachtman

```
<opinion type="majority">
<author id="b464-8">Me. Justice Powell</author>
<p id="Av">delivered the opinion of the Court.</p>
<p id="b464-9">The question presented in this case is whether a state prosecuting attorney who acted within the scope of his duties in initiating and pursuing a criminal prosecution is amenable to suit under <span class="citation no-link">42 U. S. C. § 1983</span> for alleged deprivations of the defendant's constitutional rights. The Court of Appeals for the Ninth Circuit held that he is not. <span class="citation" data-id="9460865"><a href="/opinion/320782/paul-kern-imbler-v-richard-pachtman/" aria-description="Citation for case: Paul Kern Imbler v. Richard Pachtman">500 F. 2d 1301</a></span>. We affirm.</p>
<p id="b464-10">I</p>
<p id="b464-11">The events which culminated in this suit span many years and several judicial proceedings. They began in <page-number citation-index="1" label="411">*411</page-number>January 1961, when two men attempted to rob a Los Angeles market run by Morris Hasson. One shot and fatally wounded Hasson, and the two fled in different directions. Ten days later Leonard Lingo was killed while attempting a robbery in Pomona, Cal., but his two accomplices escaped. Paul Imbler, petitioner in this case, turned himself in the next day as one of those accomplices. Subsequent investigation led the Los Angeles District Attorney to believe that Imbler and Lingo had perpetrated the first crime as well, and that Imbler had killed Hasson. Imbler was charged with first-degree felony murder for Hasson’s death.</p>
<p id="b465-5">The State’s case consisted of eyewitness testimony from Hasson’s wife and identification testimony from three men who had seen Hasson’s assailants fleeing after the shooting. Mrs. Hasson was unable to identify the gunman because a hat had obscured his face, but from police photographs she identified the killer’s companion as Leonard Lingo. The primary identification witness was Alfred Costello, a passerby on the night of the crime, who testified that he had a clear view both as the gunman emerged from the market and again a few moments later when the fleeing gunman — after losing his hat — r turned to fire a shot at Costello<footnotemark>1</footnotemark> and to shed his coat<footnotemark>2</footnotemark> before continuing on. . Costello positively identified Imbler as the gunman. The second identification witness, an attendant at a parking lot through which the gunman ultimately escaped, testified that he had a side and front view as the man passed. Finally, a customer who was leaving Hasson’s market as the robbers entered <page-number citation-index="1" label="412">*412</page-number>testified that he had a good look then and as they exited moments later. All of these witnesses identified Imbler as the gunman, and the customer also identified the second man as Leonard Lingo. Rigorous cross-examination failed to shake any of these witnesses.<footnotemark>3</footnotemark></p>
<p id="b466-5">Imbler’s defense was an alibi. He claimed to have spent the night of the Hasson killing bar-hopping with several persons, and to have met Lingo for the first time the morning before the attempted robbery in Pomona. This testimony was corroborated by Mayes, the other accomplice in the Pomona robbery, who also claimed to have accompanied Imbler on the earlier rounds of the bars. The jury found Imbler guilty and fixed punishment at death.<footnotemark>4</footnotemark> On appeal the Supreme Court of California affirmed unanimously over numerous contentions of error. <em>People </em>v. <em>Imbler, </em><span class="citation" data-id="1131905"><a href="/opinion/1131905/people-v-imbler/" aria-description="Citation for case: People v. Imbler">57 Cal. 2d 711</a></span>, <span class="citation" data-id="1131905"><a href="/opinion/1131905/people-v-imbler/" aria-description="Citation for case: People v. Imbler">371 P. 2d 304</a></span> (1962).</p>
<p id="b466-6">Shortly thereafter Deputy District Attorney Richard Pachtman, who had been the prosecutor at Imbler’s trial and who is the respondent before this Court, wrote to the Governor of California describing evidence turned up after trial by himself and an investigator for the state correctional authority. In substance, the evidence consisted of newly discovered corroborating witnesses for Imbler’s alibi, as well as new revelations about prime witness Costello’s background which indicated that he was less trustworthy than he had represented originally to Pachtman and in his testimony. Pachtman noted that leads to some of this information had been available to Imbler’s counsel prior to trial but apparently <page-number citation-index="1" label="413">*413</page-number>had not been developed, that Costello had testified convincingly and withstood intense cross-examination, and that none of the new evidence was conclusive of Imbler’s innocence. He explained that he wrote from a belief that “a prosecuting attorney has a duty to be fair and see that all true facts, whether helpful to the case or not, should be presented.” <footnotemark>5</footnotemark></p>
<p id="b467-5">Imbler filed a state habeas corpus petition shortly after Pachtman’s letter. The Supreme Court of California appointed one of its retired justices as referee to hold a hearing, at which Costello was the main attraction. He recanted his trial identification of Imbler, and it also was established that on cross-examination and redirect he had painted a picture of his own background that was more flattering than trüe. Imbler’s corroborating witnesses, uncovered by prosecutor Pachtman’s investigations, also testified.</p>
<p id="b467-6">In his brief to the Supreme Court of California on this habeas petition, Imbler’s counsel described Pacht-man’s post-trial detective work as “[i]n the highest tradition of law enforcement and justice,” and as a premier example of “devotion to duty.” <footnotemark>6</footnotemark> But he also charged that the prosecution had knowingly used false testimony and suppressed material evidence at Imbler’s trial.<footnotemark>7</footnotemark> In a thorough opinion by then Justice Traynor, the Supreme Court of California unanimously rejected these contentions and denied the writ. <em>In re Imbler, </em><page-number citation-index="1" label="414">*414</page-number><span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/" aria-description="Citation for case: In Re Imbler">60 Cal. 2d 554</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/" aria-description="Citation for case: In Re Imbler">387 P. 2d 6</a></span> (1963). The California court noted that the hearing record fully supported the referee’s finding that Costello’s recantation of his identification lacked credibility compared to the original identification itself, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#562" aria-description="Citation for case: In Re Imbler"><em>id., </em>at 562</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#10" aria-description="Citation for case: In Re Imbler">387 P. 2d, at 10-11</a></span>, and that the new corroborating witnesses who appeared on Imbler’s behalf were unsure of their stories or were otherwise impeached, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#569" aria-description="Citation for case: In Re Imbler"><em>id., </em>at 569-570</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#14" aria-description="Citation for case: In Re Imbler">387 P. 2d, at 14</a></span>.</p>
<p id="b468-5">In 1964, the year after denial of his state habeas petition, Imbler succeeded in having his death sentence overturned on grounds unrelated to this case. <em>In re Imbler, </em><span class="citation" data-id="9558198"><a href="/opinion/1194513/in-re-imbler/" aria-description="Citation for case: In Re Imbler">61 Cal. 2d 556</a></span>, <span class="citation" data-id="9558198"><a href="/opinion/1194513/in-re-imbler/" aria-description="Citation for case: In Re Imbler">393 P. 2d 687</a></span> (1964). Rather than resentence him, the State stipulated to life imprisonment. There the matter lay for several years, until in late 1967 or early 1968 Imbler filed a habeas corpus petition in Federal District Court based on the same contentions previously urged upon and rejected by the Supreme Court of California.</p>
<p id="b468-6">The District Court held no hearing. Instead, it decided the petition upon the record, including Pacht-man’s letter to the Governor and the transcript of the referee’s hearing ordered by the Supreme Court of California. Reading that record quite differently than had the seven justices of the State Supreme Court, the District Court found eight instances of state misconduct at Imbler’s trial, the cumulative effect of which required issuance of the writ. <em>Imbler </em>v. <em>Craven, </em><span class="citation" data-id="1868466"><a href="/opinion/1868466/imbler-v-craven/#812" aria-description="Citation for case: Imbler v. Craven">298 F. Supp. 795, 812</a></span> (CD Cal. 1969). Six occurred during Costello’s testimony and amounted in the court’s view to the culpable use by the prosecution of misleading or false testimony.<footnotemark>8</footnotemark> The other two instances were suppressions of <page-number citation-index="1" label="415">*415</page-number>evidence favorable to Imbler by a police fingerprint expert who testified at trial and by the police who investigated Hasson’s murder.<footnotemark>9</footnotemark> The District Court ordered that the writ of habeas corpus issue unless California retried Imbler within 60 days, and denied a petition for rehearing.</p>
<p id="b469-5">The State appealed to the Court of Appeals for the Ninth Circuit, claiming that the District Court had failed to give appropriate deference to the factual determinations of the Supreme Court of California as required by <span class="citation no-link">28 U. S. C. § 2254</span> (d). The Court of Appeals affirmed, finding that the District Court had merely “reached different conclusions than the state court in applying federal constitutional standards to [the] facts,” <em>Imbler </em>v. <em>California, </em><span class="citation" data-id="289539"><a href="/opinion/289539/paul-k-imbler-v-state-of-california/#632" aria-description="Citation for case: Paul K. Imbler v. State of California">424 F. 2d 631, 632</a></span>, and certiorari was denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/865/">400 U. S. 865</a></span> (1970). California chose not to retry Imbler, and he was released.</p>
<p id="b469-6">At this point, after a decade of litigation and with Imbler now free, the stage was set for the present suit. In April 1972, Imbler filed a civil rights action, under <span class="citation no-link">42 U. S. C. § 1983</span> and related statutes, against respondent Pachtman, the police fingerprint expert, and various other officers of the Los Angeles police force. He alleged <page-number citation-index="1" label="416">*416</page-number>that a conspiracy among them unlawfully to charge and convict him had caused him loss of liberty and other grievous injury. He demanded $2.7 million in actual and exemplary damages from each defendant, plus $15,-000 attorney’s fees.</p>
<p id="b470-5">Imbler attempted to incorporate into his complaint the District Court’s decision granting the writ of habeas corpus, and for the most part tracked that court’s opinion in setting out the overt acts in furtherance of the alleged conspiracy. The gravamen of his complaint against Pachtman was that he had “with intent, and on other occasions with negligence” allowed Costello to give false testimony as found by the District Court, and that the fingerprint expert’s suppression of evidence was “chargeable under federal law” to Pachtman. In addition Imbler claimed that Pachtman had prosecuted him with knowledge of a lie detector test that had “cleared” Imbler, and that Pachtman had used at trial a police artist’s sketch of Hasson’s killer made shortly after the crime and allegedly altered to resemble Imbler more closely after the investigation had focused upon him.</p>
<p id="b470-6">Pachtman moved under Fed. Rule Civ. Proc. 12 (b)(6) to have the complaint dismissed as to him. The District Court, noting that public prosecutors repeatedly had been held immune from civil liability for “acts done as part of their traditional official functions,” found that Pacht-man’s alleged acts fell into that category and granted his motion. Following the entry of final judgment as to Pachtman under Fed. Rule Civ. Proc. 54 (b), Imbler appealed to the Court of Appeals for the Ninth Circuit. That court, one judge dissenting, affirmed the District Court in an opinion finding Pachtman’s alleged acts to have been committed “during prosecutorial activities which can only be characterized as an ‘integral part of the judicial process,’ ” <span class="citation" data-id="9460865"><a href="/opinion/320782/paul-kern-imbler-v-richard-pachtman/#1302" aria-description="Citation for case: Paul Kern Imbler v. Richard Pachtman">500 F. 2d, at 1302</a></span>, quoting <page-number citation-index="1" label="417">*417</page-number><em>Marlowe </em>v. <em>Coakley, </em><span class="citation" data-id="282495"><a href="/opinion/282495/benjamin-f-marlowe-v-j-frank-coakley/" aria-description="Citation for case: Benjamin F. Marlowe v. J. Frank Coakley">404 F. 2d 70</a></span> (CA9 1968). We granted certiorari to consider the important and recurring issue of prosecutorial liability under the Civil Rights Act of 1871. <span class="citation multiple-matches"><a href="/c/U.%20S./420/945/">420 U. S. 945</a></span> (1975).</p>
<p id="b471-5">II</p>
<p id="b471-6">Title <span class="citation no-link">42 U. S. C. § 1983</span> provides that “[e]very person” who acts under color of state law to deprive another of a constitutional right shall be answerable to that person in a suit for damages.<footnotemark>10</footnotemark> The statute thus creates a species of tort liability that on its face admits of no immunities, and some have argued that it should be applied as stringently as it reads.<footnotemark>11</footnotemark> But that view has not prevailed.</p>
<p id="b471-7">This Court first considered the implications of the statute’s literal sweep in <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367</a></span> (1951). There it was claimed that members of a state legislative committee had called the plaintiff to appear before them, not for a proper legislative purpose, but to intimidate him into silence on certain matters of public concern, and thereby had deprived him of his constitutional rights. Because legislators in both England and this country had enjoyed absolute immunity for their official actions, <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Tenney</a></span> </em>squarely presented the issue of whether the Reconstruction Congress had intended to <page-number citation-index="1" label="418">*418</page-number>restrict the availability in § 1983 suits of those immunities which historically, and for reasons of public policy, had been accorded to various categories of officials. The Court concluded that immunities “well grounded in history and reason” had not been abrogated “by covert inclusion in the general language” of § 1983. <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S., at 376</a></span>. Regardless of any unworthy purpose animating their actions, legislators were held to enjoy under this statute their usual immunity when acting “in a field where legislators traditionally have power to act.” <em>Id., </em>at 379.</p>
<p id="b472-5">The decision in <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Tenney</a></span> </em>established that § 1983 is to be read in harmony with general principles of tort immunities and defenses rather than in derogation of them. Before today the Court has had occasion to consider the liability of several types of government officials in addition to legislators. The common-law absolute immunity of judges for “acts committed within their judicial jurisdiction,” see <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/" aria-description="Citation for case: Bradley v. Fisher">13 Wall. 335</a></span> (1872), was found to be preserved under § 1983 in <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 554-555</a></span> (1967).<footnotemark>12</footnotemark> In the same case, local police officers sued for a deprivation of liberty resulting from unlawful arrest were held to enjoy under § 1983 a “good faith and probable cause” defense coextensive with their defense to false arrest actions at <page-number citation-index="1" label="419">*419</page-number>common law. <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S., at <em>555-557. </em></a></span>We found qualified immunities appropriate in two recent cases.<footnotemark>13</footnotemark> In <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974), we concluded that the Governor and other executive officials of a State had a qualified immunity that varied with “the scope of discretion and responsibilities of the office and all the circumstances as they reasonably appeared at the time of the action. . . .” <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#247" aria-description="Citation for case: Scheuer v. Rhodes"><em>Id., </em>at 247</a></span>.<footnotemark>14</footnotemark> Last Term in <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975), we held that school officials, in the context of imposing disciplinary penalties, were not liable so long as they could not reasonably have known that their action violated students’ clearly established constitutional rights, and provided they did not act with malicious intention to cause constitutional or other injury. <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland"><em>Id., </em>at 322</a></span>; cf. <em>O'Connor </em>v. <em>Donaldson, </em><span class="citation" data-id="9842006"><a href="/opinion/109303/oconnor-v-donaldson/#577" aria-description="Citation for case: O&#x27;Connor v. Donaldson">422 U. S. 563, 577</a></span> (1975). In <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>and in <em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">Wood</a></span>, </em>as in the two earlier cases, the considerations underlying the nature of the immunity of the respective officials in suits at common law led to essentially the same immunity under § 1983.<footnotemark>15</footnotemark> See <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#318" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 318-321</a></span>; <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#239" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S., at 239-247</a></span>, and n. 4.</p>
<p id="b474-7"><page-number citation-index="1" label="420">*420</page-number>III</p>
<p id="b474-1">This case marks our first opportunity to address the § 1983 liability of a state prosecuting officer. The Courts of Appeals, however, have confronted the issue many times and under varying circumstances. Although the precise contours of their holdings have been unclear at times, at bottom they are virtually unanimous that a prosecutor enjoys absolute immunity from § 1983 suits for damages when he acts within the scope of his prosecutorial duties.<footnotemark>16</footnotemark> These courts sometimes have described the prosecutor’s immunity as a form of “quasi-judicial” immunity and referred to it as derivative of the immunity of judges recognized in <em>Pierson </em>v. <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Ray, supra.</a></span></em><footnotemark><em>17</em></footnotemark><em> </em>Petitioner focuses upon the “quasi-judicial” characterization, and contends that it illustrates a fundamental illogic in according absolute immunity to a prosecutor. He argues that the prosecutor, ás a member of the executive branch, cannot claim the immunity reserved for the judiciary, but only a qualified immunity <page-number citation-index="1" label="421">*421</page-number>akin to that accorded other executive officials in this Court’s previous cases.</p>
<p id="b475-5">Petitioner takes an overly simplistic approach to the issue of prosecutorial liability. As noted above, our earlier decisions on § 1983 immunities were not products of judicial fiat that officials in different branches of government are differently amenable to suit under § 1983. Rather, each was predicated upon a considered inquiry into the immunity historically accorded the relevant official at common law and the interests behind it. The liability of a state prosecutor under § 1983 must be determined in the same manner.</p>
<p id="b475-6">A</p>
<p id="b475-7">The function of a prosecutor that most often invites a common-law tort action is his decision to initiate a prosecution, as this may lead to a suit for malicious prosecution if the State’s case misfires. The first American case to address the question of a prosecutor’s amenability to such an action was <em>Griffith </em>v. <em>Slinkard, </em><span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/" aria-description="Citation for case: Griffith v. Slinkard">146 Ind. 117</a></span>, <span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/" aria-description="Citation for case: Griffith v. Slinkard">44 N. E. 1001</a></span> (1896).<footnotemark>18</footnotemark> The complaint charged that a local prosecutor without probable cause added the plaintiff’s name to a grand jury true bill after the grand jurors had refused to indict him, with the result that the plaintiff was arrested and forced to appear in court repeatedly before the charge finally was <em>nolle prossed. </em>Despite allegations of malice, the Supreme Court of Indiana dismissed the action on the ground that the prosecutor was absolutely immune. <span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/#122" aria-description="Citation for case: Griffith v. Slinkard"><em>Id., </em>at 122</a></span>, <span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/#1002" aria-description="Citation for case: Griffith v. Slinkard">44 N. E., at 1002</a></span>.</p>
<p id="b476-4"><page-number citation-index="1" label="422">*422</page-number>The <em><span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/" aria-description="Citation for case: Griffith v. Slinkard">Griffith</a></span> </em>view on prosecutorial immunity became the clear majority rule on the issue.<footnotemark>19</footnotemark> The question eventually came to this Court on writ of certiorari to the Court of Appeals for the Second Circuit. In <em>Yaselli </em>v. <em>Goff, </em><span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/" aria-description="Citation for case: Yaselli v. Goff">12 F. 2d 396</a></span> (1926), the claim was that the defendant, a Special Assistant to the Attorney General of the United States, maliciously and without probable cause procured plaintiff’s grand jury indictment by the willful introduction of false and misleading evidence. Plaintiff sought some $300,000 in damages for having been subjected to the rigors of a trial, in which the court ultimately directed a verdict against the Government. The District Court dismissed the complaint, and the Court of Appeals affirmed. After reviewing the development of the doctrine of prosecutorial immunity, <span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/#399" aria-description="Citation for case: Yaselli v. Goff"><em>id., </em>at 399-404</a></span>, that court stated:</p>
<blockquote id="b476-5">“In our opinion the law requires us to hold that a special assistant to the Attorney General of the United States, in the performance of the duties imposed upon him by law, is immune from a civil action for malicious prosecution based on an indictment and prosecution, although it results in a verdict of not guilty rendered by a jury. The immunity is absolute, and is grounded on principles of public policy.” <span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/#406" aria-description="Citation for case: Yaselli v. Goff"><em>Id., </em>at 406</a></span>.</blockquote>
<p id="b476-6">After briefing and oral argument, this Court affirmed the Court of Appeals in a <em>per curiam </em>opinion. <em>Yaselli </em>v. <em>Goff, </em><span class="citation" data-id="8146727"><a href="/opinion/8184801/yaselli-v-goff/" aria-description="Citation for case: Yaselli v. Goff">275 U. S. 503</a></span> (1927).</p>
<p id="b476-7">The common-law immunity of a prosecutor is based upon the same considerations that underlie the common-<page-number citation-index="1" label="423">*423</page-number>law immunities of judges and grand jurors acting within the scope of their duties.<footnotemark>20</footnotemark> These include concern that harassment by unfounded litigation would cause a deflection of the prosecutor’s energies from his public duties, and the possibility that he would shade his decisions instead of exercising the independence of judgment required by his public trust. One court expressed both considerations as follows:</p>
<blockquote id="b477-5">“The office of public prosecutor is one which must be administered with courage and independence. Yet how can this be if the prosecutor is made subject to suit by those whom he accuses and fails to convict? To allow this would open the way for unlimited harassment and embarrassment of the most conscientious officials by those who would profit thereby. There would be involved in every case the possible consequences of a failure to obtain a con<page-number citation-index="1" label="424">*424</page-number>viction. There would always be a question of possible civil action in case the prosecutor saw fit to move dismissal of the case. . . . The apprehension of such consequences would tend toward great uneasiness and toward weakening the fearless and impartial policy which should characterize the administration of this office. The work of the prosecutor would thus be impeded and we would have moved away from the desired objective of stricter and fairer law enforcement.” <em>Pearson </em>v. <em>Reed, </em><span class="citation" data-id="1422703"><a href="/opinion/1422703/pearson-v-reed/#287" aria-description="Citation for case: Pearson v. Reed">6 Cal. App. 2d 277, 287</a></span>, <span class="citation" data-id="1422703"><a href="/opinion/1422703/pearson-v-reed/#597" aria-description="Citation for case: Pearson v. Reed">44 P. 2d 592, 597</a></span> (1935).</blockquote>
<p id="b478-5">See also <em>Yaselli </em>v. <em>Goff, </em><span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/#404" aria-description="Citation for case: Yaselli v. Goff">12 F. 2d, at 404-406</a></span>.</p>
<p id="b478-6">B</p>
<p id="b478-7">The common-law rule of immunity is thus well settled.<footnotemark>21</footnotemark> We now must determine whether the same considerations of public policy that underlie the common-law rule likewise countenance absolute immunity under § 1983. We think they do.</p>
<p id="b478-8">If a prosecutor had only a qualified immunity, the threat of § 1983 suits would undermine performance of his duties no less than would the threat of common-law suits for malicious prosecution. A prosecutor is duty bound to exercise his best judgment both in deciding which suits to bring and in conducting them in court. The public trust of the prosecutor’s office would suffer if he were constrained in making every decision by the consequences in terms of his own potential liability in a <page-number citation-index="1" label="425">*425</page-number>suit for damages. Such suits could be expected with some frequency, for a defendant often will transform his resentment at being prosecuted into the ascription of improper and malicious actions to the State’s advocate. Cf. <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/#348" aria-description="Citation for case: Bradley v. Fisher">13 Wall., at 348</a></span>; <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 554</a></span>. Further, if the prosecutor could be made to answer in court each time such a person charged him with wrongdoing, his energy and attention would be diverted from the pressing duty of enforcing the criminal law.</p>
<p id="b479-5">Moreover, suits that survived the pleadings would pose substantial danger of liability even to the honest prosecutor. The prosecutor’s possible knowledge of a witness’ falsehoods, the materiality of evidence not revealed to the defense, the propriety of a closing argument, and— ultimately in every case — the likelihood that prosecu-torial misconduct so infected a trial as to deny due process, are typical of issues with which judges struggle in actions for post-trial relief, sometimes to differing conclusions.<footnotemark>22</footnotemark> The presentation of such issues in a § 1983 action often would require a virtual retrial of the criminal offense in a new forum, and the resolution of some technical issues by the lay jury. It is fair to say, we think, that the honest prosecutor would face greater difficulty in meeting the standards of qualified immunity than other executive or administrative officials. Frequently acting under serious constraints of time and even information, a prosecutor inevitably makes many decisions that could engender colorable claims of constitutional deprivation. Defending these decisions, often years after they were made, could impose unique <page-number citation-index="1" label="426">*426</page-number>and intolerable burdens upon a prosecutor responsible annually for hundreds of indictments and trials. Cf. <em>Bradley </em>v. <span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/#349" aria-description="Citation for case: Bradley v. Fisher"><em>Fisher, supra, </em>at 349</a></span>.</p>
<p id="b480-5">The affording of only a qualified immunity to the prosecutor also could have an adverse effect upon the functioning of the criminal justice system. Attaining the system’s goal of accurately determining guilt or innocence requires that both the prosecution and the defense have wide discretion in the conduct of the trial and the presentation of evidence.<footnotemark>23</footnotemark> The veracity of witnesses in criminal cases frequently is subject to doubt before and after they testify, as is illustrated by the history of this case. If prosecutors were hampered in exercising their judgment as to the use of such witnesses by concern about resulting personal liability, the triers of fact in criminal cases often would be denied relevant evidence.<footnotemark>24</footnotemark></p>
<p id="b481-4"><page-number citation-index="1" label="427">*427</page-number>The ultimate fairness of the operation of the system itself could be weakened by subjecting prosecutors to § 1983 liability. Various post-trial procedures are available to determine whether an accused has received a fair trial. These procedures include the remedial powers of the trial judge, appellate review, and state and federal post-conviction collateral remedies. In all of these the attention of the reviewing judge or tribunal is focused primarily on whether there was a fair trial under law. This focus should not be blurred by even the subconscious knowledge that a post-trial decision in favor of the accused might result in the prosecutor’s being called upon to respond in damages for his error or mistaken judgment.<footnotemark>25</footnotemark></p>
<p id="b481-5">We conclude that the considerations outlined above dictate the same absolute immunity under § 1983 that the prosecutor enjoys at common law. To be sure, this immunity does leave the genuinely wronged defendant without civil redress against a prosecutor whose malicious or dishonest action deprives him of liberty. But the alternative of qualifying a prosecutor’s immunity would disserve the broader public interest. It would prevent the vigorous and fearless performance of the prosecutor’s duty that is essential to the proper function<page-number citation-index="1" label="428">*428</page-number>ing of the criminal justice system.<footnotemark>26</footnotemark> Moreover, it often would prejudice defendants in criminal cases by skewing post-conviction judicial decisions that should be made with the sole purpose of insuring justice. With the issue thus framed, we find ourselves in agreement with Judge Learned Hand, who wrote of the prosecutor’s immunity from actions for malicious prosecution:</p>
<blockquote id="b482-5">“As is so often the case, the answer must be found in a balance between the evils inevitable in either alternative. In this instance it has been thought in the end better to leave unredressed the wrongs done by dishonest officers than to subject those who try to do their duty to the constant dread of retaliation.” <em>Gregoire </em>v. <em>Biddle, </em><span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/#581" aria-description="Citation for case: Gregoire v. Biddle">177 F. 2d 579, 581</a></span> (CA2 1949), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./339/949/">339 U. S. 949</a></span> (1950).</blockquote>
<p id="b482-6">See <em>Yaselli </em>v. <em>Goff, </em><span class="citation" data-id="1490367"><a href="/opinion/1490367/yaselli-v-goff/#404" aria-description="Citation for case: Yaselli v. Goff">12 F. 2d, at 404</a></span>; cf. <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#320" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 320</a></span>.<footnotemark>27</footnotemark></p>
<p id="b482-7">We emphasize that the immunity of prosecutors from <page-number citation-index="1" label="429">*429</page-number>liability in suits under § 1983 does not leave the public powerless to deter misconduct or to punish that which occurs. This Court has never suggested that the policy considerations which compel civil immunity for certain governmental officials also place them beyond the reach of the criminal law. Even judges, cloaked with absolute civil immunity for centuries, could be punished criminally for willful deprivations of constitutional rights on the strength of <span class="citation no-link">18 U. S. C. § 242</span>,<footnotemark>28</footnotemark> the criminal analog of § 1983. <em>O’Shea </em>v. <em>Littleton, </em><span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/#503" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U. S. 488, 503</a></span> (1974); cf. <em>Gravel </em>v. <em>United States, </em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#627" aria-description="Citation for case: Gravel v. United States">408 U. S. 606, 627</a></span> (1972). The prosecutor would fare no better for his willful acts.<footnotemark>29</footnotemark> Moreover, a prosecutor stands perhaps unique, among officials whose acts could deprive persons of constitutional rights, in his amenability to professional discipline by an association of his peers.<footnotemark>30</footnotemark> These checks undermine the argument that the imposition of civil liability is the only way to insure that prosecutors are mindful of the constitutional rights of persons accused of crime.</p>
<p id="b484-4"><page-number citation-index="1" label="430">*430</page-number>IV</p>
<p id="b484-5">It remains to delineate the boundaries of our holding. As noted, <em>supra, </em>at 416, the Court of Appeals emphasized that each of respondent’s challenged activities was an “integral part of the judicial process.” 600 F. 2d, at 1302. The purpose of the Court of Appeals’ focus upon the functional nature of the activities rather than respondent’s status was to distinguish and leave standing those cases, in its Circuit and in some others, which hold that a prosecutor engaged in certain investigative activities enjoys, not the absolute immunity associated with the judicial process, but only a good-faith defense comparable to the policeman’s.<footnotemark>31</footnotemark> See <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#557" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 557</a></span>. We agree with the Court of Appeals that respondent’s activities were intimately associated with the judicial phase of the criminal process, and thus were functions to which the reasons for absolute immunity apply with full force.<footnotemark>32</footnotemark> We have no occasion to consider whether like or similar reasons require immunity for those aspects of the prosecutor’s responsibility that cast him in the role of an administrator or investigative <page-number citation-index="1" label="431">*431</page-number>officer rather than that of advocate.<footnotemark>33</footnotemark> We hold only that in initiating a prosecution and in presenting the State’s case, the prosecutor is immune from a civil suit for damages under § 1983.<footnotemark>34</footnotemark> The judgment of the Court of Appeals for the Ninth Circuit accordingly is</p>
<p id="b485-5">
<em>Affirmed.</em>
</p>
<p id="b486-4"><page-number citation-index="1" label="432">*432</page-number>Mr. Justice Stevens took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b465-6"> This shot formed the basis of a second count against Imbler for assault, which was tried with the murder count.</p>
</footnote>
<footnote label="2">
<p id="b465-7"> This coat, identified by Mrs. Hasson as that worn by her husband’s assailant, yielded a gun determined by ballistics evidence to be the murder weapon.</p>
</footnote>
<footnote label="3">
<p id="b466-7"> A fourth man who saw Hasson’s killer leaving the scene identified Imbler in a pretrial lineup, but police were unable to find him at the time of trial.</p>
</footnote>
<footnote label="4">
<p id="b466-8"> Imbler also received a 10-year prison term on the assault charge. See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="5">
<p id="b467-7"> Brief for Respondent, App. A, p. 6. The record does not indicate what specific action was taken in response to Pachtman’s letter. We do note that the letter was dated August 17, 1962, and that Imbler’s execution, scheduled for September 12, 1962, subsequently was stayed. The letter became a part of the permanent record in the case available to the courts in all subsequent litigation.</p>
</footnote>
<footnote label="6">
<p id="b467-8"> Brief for Respondent 5.</p>
</footnote>
<footnote label="7">
<p id="b467-9"> See generally <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959); <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963).</p>
</footnote>
<footnote label="8">
<p id="b468-7"> The District Court found that Costello had given certain ambiguous or misleading testimony, and had lied flatly about his criminal record, his education, and his current income. As to the misleading testimony, the court found that either Pachtman or a <page-number citation-index="1" label="415">*415</page-number>police officer present in the courtroom knew it was misleading. As to the false testimony, the District Court concluded that Pachtman had “cause to suspect” its falsity although, apparently, no actual knowledge thereof. See <span class="citation" data-id="1868466"><a href="/opinion/1868466/imbler-v-craven/#799" aria-description="Citation for case: Imbler v. Craven">298 F. Supp., at 799-807</a></span>. The Supreme Court of California earlier had addressed and rejected allegations based on many of the same parts of Costello's testimony. It found either an absence of falsehood or an absence of prosecutorial knowledge in each instance. See <em>In re Imbler, </em><span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#562" aria-description="Citation for case: In Re Imbler">60 Cal. 2d 554, 562-565</a></span>, and n. 3, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#10" aria-description="Citation for case: In Re Imbler">387 P. 2d 6, 10-12</a></span>, and n. 3 (1963).</p>
</footnote>
<footnote label="9">
<p id="b469-8"> See <span class="citation" data-id="1868466"><a href="/opinion/1868466/imbler-v-craven/#809" aria-description="Citation for case: Imbler v. Craven">298 F. Supp., at 809-811</a></span>. The Supreme Court of California earlier had rejected similar allegations. See <em>In re Imbler, supra, </em>at 566-568, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#12" aria-description="Citation for case: In Re Imbler">387 P. 2d, at 12-13</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b471-8"> Title <span class="citation no-link">42 U. S. C. § 1983</span>, originally passed as § 1 of the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, reads in full:</p>
<blockquote id="b471-9">“Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.”</blockquote>
</footnote>
<footnote label="11">
<p id="b471-10"> See, e. <em>g., Pierson </em>v. <em>Ray, </em><span class="citation multiple-matches"><a href="/c/U.%20S./386/647/">386 U. S. 647</a></span>, 559 (1967) (Douglas, J., dissenting); <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#382" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 382-383</a></span> (1951) (Douglas, J., dissenting).</p>
</footnote>
<footnote label="12">
<p id="b472-6"> The Court described the immunity of judges as follows:</p>
<blockquote id="b472-7">“Few doctrines were more solidly established at common law than the immunity of judges from liability for damages for acts committed within their judicial jurisdiction, as this Court recognized when it adopted the doctrine, in <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/" aria-description="Citation for case: Bradley v. Fisher">13 Wall. 335</a></span> (1872). This immunity applies even when the judge is accused of acting maliciously and corruptly, and it ‘is not for the protection or benefit of a malicious or corrupt judge, but for the benefit of the public, whose interest it is that the judges should be at liberty to exercise their functions with independence and without fear of consequences.’ ” <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#553" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 553-554</a></span> (citation omitted).</blockquote>
</footnote>
<footnote label="13">
<p id="b473-5"> The procedural difference between the absolute and the qualified immunities is important. An absolute immunity defeats a suit at the outset, so long as the official’s actions were within the scope of the immunity. The fate of an official with qualified immunity depends upon the circumstances and motivations of his actions, as established by the evidence at trial. See <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#238" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 238-239</a></span> (1974); <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#320" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 320-322</a></span> (1975).</p>
</footnote>
<footnote label="14">
<p id="b473-6"> The elements of this immunity were described in <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>as follows:</p>
<blockquote id="b473-7">“It is the existence of reasonable grounds for the belief formed at the time and in light of all the circumstances, coupled with good faith belief, that affords a basis for qualified immunity of executive officers for acts performed in the course of official conduct.” <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#247" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S., at 247-248</a></span>.</blockquote>
</footnote>
<footnote label="15">
<p id="b473-8"> In <em>Tenney </em>v. <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Brandhove</a></span>, </em>of course, the Court looked to the <page-number citation-index="1" label="420">*420</page-number>immunity accorded legislators by the Federal and State Constitutions, as well as that developed by the common law. <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#372" aria-description="Citation for case: Tenney v. Brandhove">341 U. S., at 372-375</a></span>. See generally <em>Doe </em>v. <em>McMillan, </em><span class="citation" data-id="9425326"><a href="/opinion/108802/doe-v-mcmillan/" aria-description="Citation for case: Doe v. McMillan">412 U. S. 306</a></span> (1973).</p>
</footnote>
<footnote label="16">
<p id="b474-3"> <em>Fanale </em>v. <em>Sheeky, </em><span class="citation multiple-matches"><a href="/c/F.%202d/385/866/">385 F. 2d 866</a></span>, 868 (CA2 1967); <em>Bauers </em>v. <em>Heisel, </em><span class="citation" data-id="9451819"><a href="/opinion/272024/william-j-bauers-jr-v-herbert-t-heisel-jr/" aria-description="Citation for case: William J. Bauers, Jr. v. Herbert T. Heisel, Jr">361 F. 2d 581</a></span> (CA3 1966), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./386/1021/">386 U. S. 1021</a></span> (1967); <em>Carmack </em>v. <em>Gibson, </em><span class="citation" data-id="272579"><a href="/opinion/272579/herbert-b-carmack-v-wallace-gibson-judge-circuit-court-of-jefferson/#864" aria-description="Citation for case: Herbert B. Carmack v. Wallace Gibson, Judge, Circuit...">363 F. 2d 862, 864</a></span> (CA5 1966); <em>Tyler </em>v. <em>Witkowski, </em><span class="citation" data-id="325501"><a href="/opinion/325501/maurice-tyler-v-joseph-witkowski/#450" aria-description="Citation for case: Maurice Tyler v. Joseph Witkowski">511 F. 2d 449, 450-451</a></span> (CA7 1975); <em>Barnes </em>v. <em>Dorsey, </em><span class="citation" data-id="312106"><a href="/opinion/312106/eugene-barnes-v-sam-elmer-dorsey/#1060" aria-description="Citation for case: Eugene Barnes v. Sam Elmer Dorsey">480 F. 2d 1057, 1060</a></span> (CA8 1973); <em>Kostal </em>v. <em>Stoner, </em><span class="citation" data-id="6921515"><a href="/opinion/7020406/kostal-v-stoner/#493" aria-description="Citation for case: Kostal v. Stoner">292 F. 2d 492, 493</a></span> (CA10 1961), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./369/868/">369 U. S. 868</a></span> (1962); cf. <em>Guerro </em>v. <em>Mulhearn, </em><span class="citation" data-id="320118"><a href="/opinion/320118/thomas-a-guerro-v-roger-f-mulhearn-ralph-f-andrews-v-kathy-decote/#1255" aria-description="Citation for case: Thomas A. Guerro v. Roger F. Mulhearn, Ralph F. Andrews...">498 F. 2d 1249, 1255-1256</a></span> (CA1 1974); <em>Weathers </em>v. <em>Ebert, </em><span class="citation" data-id="322638"><a href="/opinion/322638/roy-w-weathers-v-paul-ebert/#515" aria-description="Citation for case: Roy W. Weathers v. Paul Ebert">505 F. 2d 514, 515-516</a></span> (CA4 1974). But compare <em>Hurlburt </em>v. <em>Graham, </em><span class="citation" data-id="262073"><a href="/opinion/262073/edward-joseph-hurlburt-an-infant-over-the-age-of-14-years-by-dorothy-e/" aria-description="Citation for case: Edward Joseph Hurlburt, an Infant Over the Age of 14...">323 F. 2d 723</a></span> (CA6 1963), with <em>Hilliard </em>v. <em>Williams, </em><span class="citation" data-id="305314"><a href="/opinion/305314/lilly-mae-onie-lee-whitelaw-hilliard-v-john-l-williams/" aria-description="Citation for case: Lilly Mae Onie Lee Whitelaw Hilliard v. John L. Williams">465 F. 2d 1212</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./409/1029/">409 U. S. 1029</a></span> (1972). See Part IV, <em>infra.</em></p>
</footnote>
<footnote label="17">
<p id="AqS"> <em>E. g., Tyler </em>v. <span class="citation" data-id="325501"><a href="/opinion/325501/maurice-tyler-v-joseph-witkowski/#450" aria-description="Citation for case: Maurice Tyler v. Joseph Witkowski"><em>Witkowski, supra, </em>at 450</a></span>; <em>Kostal </em>v. <span class="citation" data-id="6921515"><a href="/opinion/7020406/kostal-v-stoner/#493" aria-description="Citation for case: Kostal v. Stoner"><em>Stoner, supra, </em>at 493</a></span>; <em>Hampton </em>v. <em>City of Chicago, </em><span class="citation" data-id="8890918"><a href="/opinion/8903845/hampton-v-city-of-chicago/#608" aria-description="Citation for case: Hampton v. City of Chicago">484 F. 2d 602, 608</a></span> (CA7 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/917/">415 U. S. 917</a></span> (1974). See n. <em>20, infra.</em></p>
</footnote>
<footnote label="18">
<p id="b475-8"> The Supreme Court of Indiana in <em><span class="citation" data-id="7052941"><a href="/opinion/7144738/griffith-v-slinkard/" aria-description="Citation for case: Griffith v. Slinkard">Griffith</a></span> </em>cited an earlier Massachusetts decision, apparently as authority for its own holding. But that case, <em>Parker </em>v. <em>Huntington, </em><span class="citation" data-id="6410355"><a href="/opinion/6536635/parker-v-huntington/" aria-description="Citation for case: Parker v. Huntington">68 Mass. 124</a></span> (1854), involved the elements of a malicious prosecution cause of action rather than the immunity of a prosecutor. See also Note, <span class="citation no-link">73 U. Pa. L. Rev. 300</span>, 304 (1925).</p>
</footnote>
<footnote label="19">
<p id="b476-8"> <em>Smith </em>v. <em>Parman, </em><span class="citation" data-id="7903738"><a href="/opinion/7952516/smith-v-parman/" aria-description="Citation for case: Smith v. Parman">101 Kan. 115</a></span>, <span class="citation" data-id="7903738"><a href="/opinion/7952516/smith-v-parman/" aria-description="Citation for case: Smith v. Parman">165 P. 663</a></span> (1917); <em>Semmes </em>v. <em>Collins, </em><span class="citation" data-id="7993445"><a href="/opinion/8037139/semmes-v-collins/" aria-description="Citation for case: Semmes v. Collins">120 Miss. 265</a></span>, <span class="citation" data-id="7993445"><a href="/opinion/8037139/semmes-v-collins/" aria-description="Citation for case: Semmes v. Collins">82 So. 145</a></span> (1919); <em>Kittler </em>v. <em>Kelsch, </em><span class="citation" data-id="3679965"><a href="/opinion/3933190/kittler-v-kelsch/" aria-description="Citation for case: Kittler v. Kelsch">56 N. D. 227</a></span>, <span class="citation" data-id="3679965"><a href="/opinion/3933190/kittler-v-kelsch/" aria-description="Citation for case: Kittler v. Kelsch">216 N. W. 898</a></span> (1927); <em>Watts </em>v. <em>Gerking, </em><span class="citation" data-id="6908241"><a href="/opinion/7008041/watts-v-gerking/" aria-description="Citation for case: Watts v. Gerking">111 Ore. 654</a></span>, <span class="citation no-link">228 P. 135</span> (1924) (on rehearing). Contra, <em>Leong Yau </em>v. <em>Carden, </em><span class="citation" data-id="6485314"><a href="/opinion/6609156/leong-yau-v-carden/" aria-description="Citation for case: Leong Yau v. Carden">23 Haw. 362</a></span> (1916).</p>
</footnote>
<footnote label="20">
<p id="b477-6"> The immunity of a judge for acts within his jurisdiction has roots extending to the earliest days of the common law. See <em>Floyd </em>v. <em>Barker, </em>12 Coke 23, 77 Eng. Rep. 1305 (1608). Chancellor Kent traced some of its history in <em>Yates </em>v. <em>Lansing, </em><span class="citation" data-id="5472513"><a href="/opinion/5627426/yates-v-lansing/" aria-description="Citation for case: Yates v. Lansing">5 Johns. 282</a></span> (N. Y. 1810), and this Court accepted the rule of judicial immunity in <em>Bradley </em>v. <em>Fisher, </em><span class="citation" data-id="9416839"><a href="/opinion/88468/bradley-v-fisher/" aria-description="Citation for case: Bradley v. Fisher">13 Wall. 335</a></span> (1872). See n. 12, <em>supra. </em>The immunity of grand jurors, an almost equally venerable common-law tenet, see <em>Floyd </em>v. <em>Barker, supra, </em>also has been adopted in this country. See, <em>e. g., Turpen </em>v. <em>Booth, </em><span class="citation" data-id="5439895"><a href="/opinion/5597013/turpen-v-booth/" aria-description="Citation for case: Turpen v. Booth">56 Cal. 65</a></span> (1880); <em>Hunter </em>v. <em>Mathis, </em><span class="citation" data-id="7039285"><a href="/opinion/7131846/hunter-v-mathis/" aria-description="Citation for case: Hunter v. Mathis">40 Ind. 356</a></span> (1872). Courts that have extended the same immunity to the prosecutor have sometimes remarked on the fact that all three officials — judge, grand juror, and prosecutor — exercise a discretionary judgment on the basis of evidence presented to them. <em>Smith </em>v. <em><span class="citation" data-id="7903738"><a href="/opinion/7952516/smith-v-parman/" aria-description="Citation for case: Smith v. Parman">Parman, supra;</a></span> Watts </em>v. <em><span class="citation" data-id="6908241"><a href="/opinion/7008041/watts-v-gerking/" aria-description="Citation for case: Watts v. Gerking">Gerking, supra.</a></span> </em>It is the functional comparability of their judgments to those of the judge that has resulted in both grand jurors and prosecutors being referred to as “quasi-judicial” officers, and their immunities being termed “quasi-judicial” as well. See, <em>e. g., Turpen </em>v. <span class="citation" data-id="5439895"><a href="/opinion/5597013/turpen-v-booth/#69" aria-description="Citation for case: Turpen v. Booth"><em>Booth, supra, </em>at 69</a></span>; <em>Watts </em>v. <span class="citation" data-id="6908241"><a href="/opinion/7008041/watts-v-gerking/#661" aria-description="Citation for case: Watts v. Gerking"><em>Gerking, supra, </em>at 661</a></span>, 228 P., at 138.</p>
</footnote>
<footnote label="21">
<p id="b478-9"> See, <em>e. g., Gregoire </em>v. <em>Biddle, </em><span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/" aria-description="Citation for case: Gregoire v. Biddle">177 F. 2d 579</a></span> (CA2 1949), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./339/949/">339 U. S. 949</a></span> (1950); <em>Cooper </em>v. <em>O’Connor, </em>69 App. D. C. 100, <span class="citation" data-id="1544268"><a href="/opinion/1544268/cooper-v-oconnor/#140" aria-description="Citation for case: Cooper v. O&#x27;CONNOR">99 F. 2d 135, 140-141</a></span> (1938); <em>Anderson </em>v. <em>Rohrer, </em><span class="citation" data-id="1876540"><a href="/opinion/1876540/anderson-v-rohrer/" aria-description="Citation for case: Anderson v. Rohrer">3 F. Supp. 367</a></span> (SD Fla. 1933); <em>Pearson </em>v. <em>Reed, </em><span class="citation" data-id="1422703"><a href="/opinion/1422703/pearson-v-reed/" aria-description="Citation for case: Pearson v. Reed">6 Cal. App. 2d 277</a></span>, <span class="citation" data-id="1422703"><a href="/opinion/1422703/pearson-v-reed/" aria-description="Citation for case: Pearson v. Reed">44 P. 2d 592</a></span> (1935); <em>Anderson </em>v. <em>Manley, </em><span class="citation" data-id="4001444"><a href="/opinion/4225250/anderson-v-manley/" aria-description="Citation for case: Anderson v. Manley">181 Wash. 327</a></span>, <span class="citation" data-id="4001444"><a href="/opinion/4225250/anderson-v-manley/" aria-description="Citation for case: Anderson v. Manley">43 P. 2d 39</a></span> (1935). See generally Restatement of Torts § 656 and comment, b (1938); 1 F. Harper &amp; F. James, The Law of Torts § 4.3, pp. 305-306 (1956).</p>
</footnote>
<footnote label="22">
<p id="b479-6"> This is illustrated by the history of the disagreement as to the culpability of the prosecutor’s conduct in this case. We express no opinion as to which of the courts was correct. See nn. 8 and 9, <em>supra.</em></p>
</footnote>
<footnote label="23">
<p id="b480-6"> In the law of defamation, a concern for the airing of all evidence has resulted in an absolute privilege for any courtroom statement relevant to the subject matter of the proceeding. In the case of lawyers the privilege extends to their briefs and pleadings as well. See generally 1 T. Cooley, Law of Torts § 153 (4th ed. 1932); 1 F. Harper &amp; F. James, <em>supra, </em>§ 5.22. In the leading case of <em>Hoar </em>v. <em>Wood, </em><span class="citation" data-id="6407880"><a href="/opinion/6534162/hoar-v-wood/" aria-description="Citation for case: Hoar v. Wood">44 Mass. 193</a></span> (1841), Chief Justice Shaw expressed the policy decision as follows:</p>
<blockquote id="b480-7">“Subject to this restriction [of relevancy], it is, on the whole, for the public interest, and best calculated to subserve the purposes of justice, to allow counsel full freedom of speech, in conducting the causes and advocating and sustaining the rights, of their constituents; and this freedom of discussion ought not to be impaired by numerous and refined distinctions.” <span class="citation" data-id="6407880"><a href="/opinion/6534162/hoar-v-wood/#197" aria-description="Citation for case: Hoar v. Wood"><em>Id., </em>at 197-198</a></span>.</blockquote>
</footnote>
<footnote label="24">
<p id="b480-8"> A prosecutor often must decide, especially in cases of wide public interest, whether to proceed to trial where there is a sharp conflict in the evidence. The appropriate course of action in such a case may well be to permit a jury to resolve the conflict. Yet, a prosecutor understandably would be reluctant to go forward with a close case where an acquittal likely would trigger a suit against him for damages. Cf. American Bar Association Project on Stand<page-number citation-index="1" label="427">*427</page-number>ards for Criminal Justice, Prosecution and Defense Function §3.9 (c) (Approved Draft 1971).</p>
</footnote>
<footnote label="25">
<p id="b481-7"> The possibility of personal liability also could dampen the prosecutor’s exercise of his duty to bring to the attention of the court or of proper officials all significant evidence suggestive of innocence or mitigation. At trial this duty is enforced by the requirements of due process, but after a conviction the prosecutor also is bound by the ethics of his office to inform the appropriate authority of after-acquired or other information that casts doubt upon the correctness of the conviction. Cf. ABA Code of Professional Responsibility §EC 7-13 (1969); ABA, Standards, <em>supra, </em>§3.11. Indeed, the record in this case suggests that respondent’s recognition of this duty led to the post-conviction hearing which in turn resulted ultimately in the District Court’s granting of the writ of habeas corpus.</p>
</footnote>
<footnote label="26">
<p id="b482-8"> In addressing the consequences of subjecting judges to suits for damages under § 1983, the Court has commented:</p>
<blockquote id="b482-9">“Imposing such a burden on judges would contribute not to principled and fearless decision-making but to intimidation.” <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 554</a></span>.</blockquote>
</footnote>
<footnote label="27">
<p id="b482-10"> Petitioner contends that his suit should be allowed, even if others would not be, because the District Court’s issuance of the writ of habeas corpus shows that his suit has substance. We decline to carve out such an exception to prosecutorial immunity. Petitioner’s success on habeas, where the question was the alleged misconduct by several state agents, does not necessarily establish the merit of his civil rights action where only the respondent’s alleged wrongdoing is at issue. Certainly nothing determined on habeas would bind respondent, who was not a • party. Moreover, using the habeas proceeding as a “door-opener” for a subsequent civil rights action would create the risk of injecting extraneous concerns into that proceeding. As we noted in the text, consideration of the habeas petition could well be colored by an awareness of potential prosecutorial liability.</p>
</footnote>
<footnote label="28">
<p id="b483-5"> “Whoever, under color of any law, statute, ordinance, regulation, or custom, willfully subjects any inhabitant of any State, Territory, or District to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution or laws of the United States, or to different punishments, pains, or penalties, on account of such inhabitant being an alien, or by reason of his color, or race, than are prescribed for the punishment of citizens, shall be fined not more than $1,000 or imprisoned not more than one year, or both; and if death results shall be subject to imprisonment for any term of years or for life.”</p>
</footnote>
<footnote label="29">
<p id="b483-6"> California also appears to provide for criminal punishment of a prosecutor who commits some of the acts ascribed to respondent by petitioner. <span class="citation no-link">Cal. Penal Code § 127</span> (1970); cf. <em>In re Branch, </em><span class="citation" data-id="1345315"><a href="/opinion/1345315/in-re-branch/#210" aria-description="Citation for case: In Re Branch">70 Cal. 2d 200, 210-211</a></span>, <span class="citation" data-id="1345315"><a href="/opinion/1345315/in-re-branch/#181" aria-description="Citation for case: In Re Branch">449 P. 2d 174, 181</a></span> (1969).</p>
</footnote>
<footnote label="30">
<p id="b483-7"> See ABA Code of Professional Responsibility § EC 7-13. See generally ABA, Standards, <em>supra, </em>n. 24, §§ 1.1 (c), (e), and Commentary, pp. 44-45.</p>
</footnote>
<footnote label="31">
<p id="b484-6"> <em>Guerro </em>v. <em>Mulhearn, </em><span class="citation" data-id="320118"><a href="/opinion/320118/thomas-a-guerro-v-roger-f-mulhearn-ralph-f-andrews-v-kathy-decote/#1256" aria-description="Citation for case: Thomas A. Guerro v. Roger F. Mulhearn, Ralph F. Andrews...">498 F. 2d, at 1256</a></span>; <em>Hampton </em>v. <em>City of Chicago, </em><span class="citation" data-id="8890918"><a href="/opinion/8903845/hampton-v-city-of-chicago/#608" aria-description="Citation for case: Hampton v. City of Chicago">484 F. 2d, at 608-609</a></span>; <em>Robichaud </em>v. <em>Ronan, </em><span class="citation" data-id="8873827"><a href="/opinion/8887719/robichaud-v-ronan/#537" aria-description="Citation for case: Robichaud v. Ronan">351 F. 2d 533, 537</a></span> (CA9 1965); cf. <em>Madison </em>v. <em>Purdy, </em><span class="citation" data-id="284582"><a href="/opinion/284582/john-madison-and-kim-madison-v-e-wilson-purdy-and-richard-e-gerstein/" aria-description="Citation for case: John Madison and Kim Madison v. E. Wilson Purdy and...">410 F. 2d 99</a></span> (CA5 1969); <em>Lewis </em>v. <em>Brautigam, </em><span class="citation" data-id="237817"><a href="/opinion/237817/james-n-lewis-v-george-brautigam-i-ray-mills-dayton-blackford-and/" aria-description="Citation for case: James N. Lewis v. George Brautigam, I. Ray Mills, Dayton...">227 F. 2d 124</a></span> (CA5 1955). But cf. <em>Cambist Films, Inc. </em>v. <em>Duggan, </em><span class="citation" data-id="9459299"><a href="/opinion/309629/cambist-films-inc-a-corporation-v-robert-w-duggan/#889" aria-description="Citation for case: Cambist Films, Inc., a Corporation v. Robert W. Duggan">475 F. 2d 887, 889</a></span> (CA3 1973).</p>
</footnote>
<footnote label="32">
<p id="Akd"> Both in his complaint in District Court and in his argument to us, petitioner characterizes some of respondent’s actions as “police-related” or investigative. Specifically, he points to a request by respondent of the police during a courtroom recess that they hold off questioning Costello about a pending bad-check charge until after Costello had completed his testimony. Petitioner asserts that this request was an investigative activity because it was a direction to police officers engaged in the investigation of crime. Seen in its proper light, however, respondent’s request of the officers was an effort to control the presentation of his witness’ testimony, a task fairly within his function as an advocate.</p>
</footnote>
<footnote label="33">
<p id="b485-6"> We recognize that the duties of the prosecutor in his role as advocate for the State involve actions preliminary to the initiation of a prosecution and actions apart from the courtroom. A prosecuting attorney is required constantly, in the course of his duty as such, to make decisions on a wide variety of sensitive issues. These include questions of whether to present a ease to a grand jury, whether to file an information, whether and when to prosecute, whether to dismiss an indictment against particular defendants, which witnesses to call, and what other evidence to present. Preparation, both for the initiation of the criminal process and for a trial, may require the obtaining, reviewing, and evaluating of evidence. At some point, and with respect to some decisions, the prosecutor no doubt functions as an administrator rather than as an officer of the court. Drawing a proper line between these functions may present difficult questions, but this case does not require us to anticipate them.</p>
</footnote>
<footnote label="34">
<p id="b485-7"> Mr. Justice White, concurring in the judgment, would distinguish between willful use by a prosecutor of perjured testimony and willful suppression by a prosecutor of exculpatory information. In the former case, Mr. Justice White agrees that absolute immunity is appropriate. He thinks, however, that only a qualified immunity is appropriate where information relevant to the defense is “unconstitutionally <em>withheld </em>. . . from the court.” <em>Post, </em>at 443.</p>
<p id="b485-8">We do not accept the distinction urged by Mr. Justice White {or several reasons. As a matter of principle, we perceive no less ,n infringement of a defendant’s rights by the knowing use of per-ured testimony than by the deliberate withholding of exculpatory [information. The conduct in either case is reprehensible, warranting criminal prosecution as well as disbarment. See <em>supra, </em>at 429 nn. 29 and 30. Moreover, the distinction is not susceptible of practical application. A claim of using perjured-testimony simply may be re-framed and asserted as a claim of suppression of the evidence upon which the knowledge of perjury rested. That the two types of claims can thus be viewed is clear from our cases discussing the constitutional prohibitions against both practices. <em>Mooney </em>v. <em>Holohan, </em><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#110" aria-description="Citation for case: Mooney v. Holohan">294 <page-number citation-index="1" label="432">*432</page-number>U. S. 103, 110</a></span> (1935); <em>Alcorta </em>v. <em>Texas, </em><span class="citation" data-id="105566"><a href="/opinion/105566/alcorta-v-texas/#31" aria-description="Citation for case: Alcorta v. Texas">355 U. S. 28, 31-32</a></span> (1957); <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#86" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 86</a></span> (1963); <em>Miller </em>v. <em>Pate, </em><span class="citation" data-id="107354"><a href="/opinion/107354/miller-v-pate/" aria-description="Citation for case: Miller v. Pate">386 U. S. 1</a></span>, 4—6 (1967); <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#151" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 151-155</a></span> (1972). It is also illustrated by the history of this case: at least one of the charges of prosecutorial • misconduct discussed by the Federal District Court in terms of suppression of evidence had been discussed by the Supreme Court of California in terms of use of perjured testimony. Compare <em>Imbler </em>v. <em>Craven, </em><span class="citation" data-id="1868466"><a href="/opinion/1868466/imbler-v-craven/#809" aria-description="Citation for case: Imbler v. Craven">298 F. Supp., at 809-811</a></span>, with <em>In re Imbler, </em><span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#566" aria-description="Citation for case: In Re Imbler">60 Cal. 2d, at 566-567</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#12" aria-description="Citation for case: In Re Imbler">387 P. 2d, at 12-13</a></span>. Denying absolute immunity from suppression claims could thus eviscerate, in many situations, the absolute immunity from claims of using perjured testimony.</p>
<p id="b486-8">We further think Mr. Justice White’s suggestion, post, at 440 n. 5, that absolute immunity should be accorded only when the prosecutor makes a “full disclosure” of all facts casting doubt upon the State’s testimony, would place upon the prosecutor a duty exceeding the disclosure requirements of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and its progeny, see <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>; <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span> (1972); cf. <em>Donnelly </em>v. <em>DeChristoforo, </em><span class="citation" data-id="9425708"><a href="/opinion/109024/donnelly-v-dechristoforo/#647" aria-description="Citation for case: Donnelly v. DeChristoforo">416 U. S. 637, 647-648</a></span> (1974). It also would weaken the adversary system at the same time it interfered seriously with the legitimate exercise of prosecutorial discretion.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Immigration & Naturalization Service v. Lopez-Mendoza.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Immigration & Naturalization Service v. Lopez-Mendoza"
type: case
citation: "468 U.S. 1032 (1984)"
parallel_cite: "104 S. Ct. 3479; 82 L. Ed. 2d 778; 52 U.S.L.W. 5190"
neutral_cite: 1984 U.S. LEXIS 156
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-07-05
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Immigration & Naturalization Service v. Lopez-Mendoza"
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/"
  cluster_id: 111265
  opinion_id: 9429772
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Janis]]", "[[United States v. Calandra]]", "[[Mapp v. Ohio]]"]
aliases: ["INS v. Lopez-Mendoza"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "deportation", "civil-proceedings"]
holding: "The exclusionary rule generally does NOT apply in civil deportation/removal proceedings: an admission of unlawful presence made after an…"
lake:
  record_id: "Immigration & Naturalization Service v. Lopez-Mendoza"
  status: verified
  projected_at: 2026-07-06
---

# Immigration & Naturalization Service v. Lopez-Mendoza

*468 U.S. 1032 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Two respondents, Lopez-Mendoza and Sandoval-Sanchez, were arrested by INS agents and placed in civil deportation proceedings. Lopez-Mendoza objected only to the immigration judge's jurisdiction over his person, claiming his arrest was unlawful. Sandoval-Sanchez sought to suppress his admission of unlawful presence as the fruit of an assertedly unlawful arrest.

## Issue
Whether the Fourth Amendment exclusionary rule applies in a civil deportation proceeding so as to require suppression of the respondent's identity or of an admission obtained after an allegedly unlawful arrest.

## Rule
The exclusionary rule generally does not apply in civil deportation hearings. As to identity: "The 'body' or identity of a defendant or respondent in a criminal or civil proceeding is never itself suppressible as a fruit of an unlawful arrest, even if it is conceded that an unlawful arrest, search, or interrogation occurred." — 468 U.S. at 1039. ^pin-1039

As to evidence generally, applying a cost-benefit balance: "In these circumstances we are persuaded that the Janis balance between costs and benefits comes out against applying the exclusionary rule in civil deportation hearings held by the INS." — *Id.* at 1050. ^pin-1050

## Application
Lopez-Mendoza's challenge failed because his identity (his "body") is never suppressible, so the manner of his arrest did not bar the proceeding against him. As to Sandoval-Sanchez, the Court weighed the limited deterrent value of exclusion against its high social costs — including releasing persons whose continuing unlawful presence is itself an ongoing violation — and concluded the balance ran against applying the exclusionary rule, so his admission of unlawful presence was not suppressed.

## Conclusion
The exclusionary rule does not generally apply in INS civil deportation proceedings; the orders of deportation were upheld.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lopez-Mendoza* applies the cost-benefit framework of [[United States v. Janis]] to civil deportation, confirming that the exclusionary rule of [[Mapp v. Ohio]] does not generally reach such proceedings.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *INS v. Lopez-Mendoza*, 468 U.S. 1032 (1984) — https://www.courtlistener.com/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/ — pinpoints: 1039, 1050.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "efadeaacd6ae4350", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Immigration & Naturalization Service v. Lopez-Mendoza"}, "payload": {"all": [{"cite": "468 U.S. 1032", "page": "1032", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "468"}, {"cite": "104 S. Ct. 3479", "page": "3479", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "82 L. Ed. 2d 778", "page": "778", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "82"}, {"cite": "1984 U.S. LEXIS 156", "page": "156", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 5190", "page": "5190", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "468 U.S. 1032", "official": {"cite": "468 U.S. 1032", "page": "1032", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "468"}, "official_selection_present": true, "record_id": "Immigration & Naturalization Service v. Lopez-Mendoza"}}
{"assertion_id": "d08eb481b4618d84", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1050", "record_id": "Immigration & Naturalization Service v. Lopez-Mendoza"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1050", "pinpoint_status": "slip-only", "quote": "In these circumstances we are persuaded that the Janis balance between costs and benefits comes out against applying the exclusionary rule in civil deportation hearings held by the INS.", "quote_fidelity": "mismatch", "record_id": "Immigration & Naturalization Service v. Lopez-Mendoza", "star_marker": null}}
{"assertion_id": "f1ce0f926f56c062", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1039", "record_id": "Immigration & Naturalization Service v. Lopez-Mendoza"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1039", "pinpoint_status": "slip-only", "quote": "--- # Immigration & Naturalization Service v. Lopez-Mendoza *468 U.S. 1032 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Two respondents, Lopez-Mendoza and Sandoval-Sanchez, were arrested by INS agents and placed in civil deportation proceedings. Lopez-Mendoza objected only to the immigration judge's jurisdiction over his person, claiming his arrest was unlawful. Sandoval-Sanchez sought to suppress his admission of unlawful presence as the fruit of an assertedly unlawful arrest. ## Issue Whether the Fourth Amendment exclusionary rule applies in a civil deportation proceeding so as to require suppression of the respondent's identity or of an admission obtained after an allegedly unlawful arrest. ## Rule The exclusionary rule generally does not apply in civil deportation hearings. As to identity:", "quote_fidelity": "mismatch", "record_id": "Immigration & Naturalization Service v. Lopez-Mendoza", "star_marker": null}}
{"assertion_id": "de63481ec684172d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Immigration & Naturalization Service v. Lopez-Mendoza"}, "payload": {"as_of_content": "1984-07-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Immigration & Naturalization Service v. Lopez-Mendoza", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Immigration & Naturalization Service v. Lopez-Mendoza

```json
{
  "schema_version": "s2.v1",
  "record_id": "Immigration & Naturalization Service v. Lopez-Mendoza",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Immigration & Naturalization Service v. Lopez-Mendoza",
    "case_name_short": "Lopez-Mendoza",
    "case_name_full": "IMMIGRATION AND NATURALIZATION SERVICE v. LOPEZ-MENDOZA Et Al.",
    "input_case_name": "Immigration & Naturalization Service v. Lopez-Mendoza",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-07-05",
    "year": 1984,
    "docket": null,
    "cluster_id": 111265,
    "lead_opinion_id": 9429772,
    "sibling_ids": [
      111265,
      9429772,
      9429773,
      9429774,
      9429775,
      9429776
    ],
    "absolute_url": "/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9287486,
        "score": 20,
        "case_name": "Immigration & Naturalization Service v. Lopez-Mendoza"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 1032",
      "volume": "468",
      "reporter": "U.S.",
      "page": "1032",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3479",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 778",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "778",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5190",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5190",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 156",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "156",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 1032",
        "volume": "468",
        "reporter": "U.S.",
        "page": "1032",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3479",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 778",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "778",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 156",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "156",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5190",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5190",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 1032",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 1032",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1039",
      "page": null,
      "quote": "--- # Immigration & Naturalization Service v. Lopez-Mendoza *468 U.S. 1032 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Two respondents, Lopez-Mendoza and Sandoval-Sanchez, were arrested by INS agents and placed in civil deportation proceedings. Lopez-Mendoza objected only to the immigration judge's jurisdiction over his person, claiming his arrest was unlawful. Sandoval-Sanchez sought to suppress his admission of unlawful presence as the fruit of an assertedly unlawful arrest. ## Issue Whether the Fourth Amendment exclusionary rule applies in a civil deportation proceeding so as to require suppression of the respondent's identity or of an admission obtained after an allegedly unlawful arrest. ## Rule The exclusionary rule generally does not apply in civil deportation hearings. As to identity:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1050",
      "page": null,
      "quote": "In these circumstances we are persuaded that the Janis balance between costs and benefits comes out against applying the exclusionary rule in civil deportation hearings held by the INS.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Immigration & Naturalization Service v. Lopez-Mendoza",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Gonzaga-Ortega v. Holder",
          "cluster_id": 808514,
          "cite": [
            "694 F.3d 1069",
            "2012 WL 4040247",
            "2012 U.S. App. LEXIS 19329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Conteh v. Gonzales",
          "cluster_id": 202370,
          "cite": [
            "461 F.3d 45",
            "2006 U.S. App. LEXIS 21422",
            "2006 WL 2406942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane1_negative"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. St. Cyr",
          "cluster_id": 118452,
          "cite": [
            "150 L. Ed. 2d 347",
            "121 S. Ct. 2271",
            "533 U.S. 289",
            "2001 U.S. LEXIS 4670",
            "2001 Cal. Daily Op. Serv. 5235",
            "2001 Daily Journal DAR 6475",
            "2001 Colo. J. C.A.R. 3473",
            "69 U.S.L.W. 4510",
            "14 Fla. L. Weekly Fed. S 401"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reno v. Flores",
          "cluster_id": 112833,
          "cite": [
            "123 L. Ed. 2d 1",
            "113 S. Ct. 1439",
            "507 U.S. 292",
            "1993 U.S. LEXIS 2399"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. United States",
          "cluster_id": 118278,
          "cite": [
            "143 L. Ed. 2d 424",
            "119 S. Ct. 1307",
            "526 U.S. 314",
            "1999 U.S. LEXIS 2348"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Peque",
          "cluster_id": 5642633,
          "cite": [
            "22 N.Y.3d 168",
            "3 N.E.3d 617"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Svitlana Denko v. Immigration and Naturalization Service",
          "cluster_id": 784396,
          "cite": [
            "351 F.3d 717",
            "2003 U.S. App. LEXIS 24605",
            "2003 WL 22879815"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mayfield v. United States",
          "cluster_id": 594,
          "cite": [
            "599 F.3d 964",
            "2010 U.S. App. LEXIS 6015",
            "2010 WL 1052341"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Huddleston",
          "cluster_id": 2435833,
          "cite": [
            "924 S.W.2d 666",
            "1996 Tenn. LEXIS 387",
            "1996 WL 328642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Emmanuel Senyo Agyeman v. Immigration & Naturalization Service",
          "cluster_id": 778380,
          "cite": [
            "296 F.3d 871",
            "2002 Daily Journal DAR 8261",
            "2002 Cal. Daily Op. Serv. 6569",
            "2002 U.S. App. LEXIS 14740",
            "2002 WL 1611190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 8437415,
          "cite": [
            "327 F.3d 56"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. 4492 South Livonia Road",
          "cluster_id": 8983256,
          "cite": [
            "889 F.2d 1258",
            "1989 U.S. App. LEXIS 17524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Julio Lozada v. Immigration and Naturalization Service",
          "cluster_id": 511756,
          "cite": [
            "857 F.2d 10",
            "1988 U.S. App. LEXIS 12733",
            "1988 WL 94706"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. National Center for Immigrants' Rights, Inc.",
          "cluster_id": 112668,
          "cite": [
            "116 L. Ed. 2d 546",
            "112 S. Ct. 551",
            "502 U.S. 183",
            "1991 U.S. LEXIS 7178",
            "60 U.S.L.W. 4052",
            "91 Daily Journal DAR 15426"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramiro Cruz Espinoza v. Immigration & Naturalization Service",
          "cluster_id": 686823,
          "cite": [
            "45 F.3d 308"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. $191,910.00 in U.S. Currency, Bruce R. Morgan, Claimant-Appellee",
          "cluster_id": 663161,
          "cite": [
            "16 F.3d 1051",
            "94 Daily Journal DAR 2139",
            "94 Cal. Daily Op. Serv. 1214",
            "1994 U.S. App. LEXIS 2681",
            "1994 WL 46744"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Laduke v. Alan C. Nelson, Etc.",
          "cluster_id": 452994,
          "cite": [
            "762 F.2d 1318",
            "1985 U.S. App. LEXIS 19963",
            "53 U.S.L.W. 2625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez Lara v. Lyons",
          "cluster_id": 4983177,
          "cite": [
            "10 F.4th 19"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111265 OR 9429772 OR 9429773 OR 9429774 OR 9429775 OR 9429776) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQzNjc2ODAwMDAwJnM9NzkzNzM2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111265+OR+9429772+OR+9429773+OR+9429774+OR+9429775+OR+9429776%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111265 OR 9429772 OR 9429773 OR 9429774 OR 9429775 OR 9429776)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzMmcz01NTY0MDkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111265+OR+9429772+OR+9429773+OR+9429774+OR+9429775+OR+9429776%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111265 OR 9429772 OR 9429773 OR 9429774 OR 9429775 OR 9429776)",
        "reviewed": 20,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 20,
        "triage_read": 0,
        "triage_snippet_classified": 20
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111265 OR 9429772 OR 9429773 OR 9429774 OR 9429775 OR 9429776)",
    "indexed_citing_opinions": 715,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111265,
        "count": 619,
        "count_source": "search"
      },
      {
        "opinion_id": 9429772,
        "count": 113,
        "count_source": "search"
      },
      {
        "opinion_id": 9429773,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429774,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429775,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429776,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1189,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/immigration-and-naturalization-service-v-lopez-mendoza.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMDM0NzEmcz05Mzg4MzQxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111265+OR+9429772+OR+9429773+OR+9429774+OR+9429775+OR+9429776%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111265,
        "cited_id": 93665,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 97876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 100280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 105227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 105684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 107043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 111223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 280943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 324058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 328798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 331113,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 350514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 352273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 364939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 374682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 399492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 421840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 427728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 1428147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 1600515,
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
    "date_created": "2026-07-05T08:36:35Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:36:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:36:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:42:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:36:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Immigration & Naturalization Service v. Lopez-Mendoza

```
<opinion type="majority">
<author id="b1076-4">Justice O’Connor</author>
<p id="AgK">announced the judgment of the Court and delivered the opinion of the Court with respect to Parts I, II, III, and IV, and an opinion with respect to Part V, in which Justice Blackmun, Justice Powell, and Justice Rehnquist joined.<footnotemark>*</footnotemark></p>
<p id="b1076-5">This litigation requires us to decide whether an admission of unlawful presence in this country made subsequently to an allegedly unlawful arrest must be excluded as evidence in a civil deportation hearing. We hold that the exclusionary rule need not be applied in such a proceeding.</p>
<p id="b1076-6">I</p>
<p id="b1076-7">Respondents Adan Lopez-Mendoza and Elias Sandoval-Sanchez, both citizens of Mexico, were summoned to separate deportation proceedings in California and Washington, and both were ordered deported. They challenged the regularity of those proceedings on grounds related to the lawfulness of their respective arrests by officials of the Immigration and Naturalization Service (INS). On administrative appeal the Board of Immigration Appeals (BIA), an agency of the Department of Justice, affirmed the deportation orders.</p>
<p id="b1076-8">The Court of Appeals for the Ninth Circuit, sitting en banc, reversed Sandoval-Sanchez’ deportation order and vacated and remanded Lopez-Mendoza’s deportation order. <span class="citation" data-id="8916793"><a href="/opinion/8927000/lopez-mendoza-v-immigration-naturalization-service/" aria-description="Citation for case: Lopez-Mendoza v. Immigration &amp; Naturalization Service">705 F. 2d 1059</a></span> (1983). It ruled that Sandoval-Sanchez’ admission of his illegal presence in this country was the fruit of an unlawful arrest, and that the exclusionary rule applied in a deportation proceeding. Lopez-Mendoza’s deportation order was vacated and his case remanded to the BIA to <page-number citation-index="1" label="1035">*1035</page-number>determine whether the Fourth Amendment had been violated in the course of his arrest. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./464/1037/">464 U. S. 1037</a></span> (1984).</p>
<p id="b1077-5">A</p>
<p id="b1077-6">Respondent Lopez-Mendoza was arrested in 1976 by INS agents at his place of employment, a transmission repair shop in San Mateo, Cal. Responding to a tip, INS investigators arrived at the shop shortly before 8 a. m. The agents had not sought a warrant to search the premises or to arrest any of its occupants. The proprietor of the shop firmly refused to allow the agents to interview his employees during working hours. Nevertheless, while one agent engaged the proprietor in conversation another entered the shop and approached Lopez-Mendoza. In response to the agent’s questioning, Lopez-Mendoza gave his name and indicated that he was from Mexico with no close family ties in the United States. The agent then placed him under arrest. Lopez-Mendoza underwent further questioning at INS offices, where he admitted he was born in Mexico, was still a citizen of Mexico, and had entered this country without inspection by immigration authorities. Based on his answers, the agents prepared a “Record of Deportable Alien” (Form 1-213), and an affidavit which Lopez-Mendoza executed, admitting his Mexican nationality and his illegal entry into this country.</p>
<p id="b1077-7">A hearing was held before an Immigration Judge. Lopez-Mendoza’s counsel moved to terminate the proceeding on the ground that Lopez-Mendoza had been arrested illegally. The judge ruled that the legality of the arrest was not relevant to the deportation proceeding and therefore declined to rule on the legality of Lopez-Mendoza’s arrest. <em>Matter of Lopez-Mendoza, </em>No. A22 452 208 (INS, Dec. 21, 1977), reprinted in App. to Pet. for Cert. 97a. The Form 1-213 and the affidavit executed by Lopez-Mendoza were received into evidence without objection from Lopez-Mendoza. On the basis of this evidence the Immigration Judge found Lopez-<page-number citation-index="1" label="1036">*1036</page-number>Mendoza deportable. Lopez-Mendoza was granted the option of voluntary departure.</p>
<p id="b1078-5">The BIA dismissed Lopez-Mendoza’s appeal. It noted that “[t]he mere fact of an illegal arrest has no bearing on a subsequent deportation proceeding,” <em>In re Lopez-Mendoza, </em>No. A22 452 208 (BIA, Sept. 19, 1979), reprinted in App. to Pet. for Cert. 100a, 102a, and observed that Lopez-Mendoza had not objected to the admission into evidence of Form 1-213 and the affidavit he had executed. <em>Id., </em>at 103a. The BIA also noted that the exclusionary rule is not applied to redress the injury to the privacy of the search victim, and that the BIA had previously concluded that application of the rule in deportation proceedings to deter unlawful INS conduct was inappropriate. <em>Matter of Sandoval, </em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/" aria-description="Citation for case: SANDOVAL">17 I. &amp; N. Dec. 70</a></span> (BIA 1979).</p>
<p id="b1078-6">The Court of Appeals vacated the order of deportation and remanded for a determination whether Lopez-Mendoza’s Fourth Amendment rights had been violated when he was arrested.</p>
<p id="b1078-7">B</p>
<p id="b1078-8">Respondent Sandoval-Sanchez (who is not the same individual who was involved in <em>Matter of Sandoval, supra) </em>was arrested in 1977 at his place of employment, a potato processing plant in Pasco, Wash. INS Agent Bower and other officers went to the plant, with the permission of its personnel manager, to check for illegal aliens. During a change in shift, officers stationed themselves at the exits while Bower and a uniformed Border Patrol agent entered the plant. They went to the lunchroom and identified themselves as immigration officers. Many people in the room rose and headed for the exits or milled around; others in the plant left their equipment and started running; still others who were entering the plant turned around and started walking back out. The two officers eventually stationed themselves at the main entrance to the plant and looked for passing employees who averted their heads, avoided eye contact, or tried to hide <page-number citation-index="1" label="1037">*1037</page-number>themselves in a group. Those individuals were addressed with innocuous questions in English. Any who could not respond in English and who otherwise aroused Agent Bower’s suspicions were questioned in Spanish as to their right to be in the United States.</p>
<p id="b1079-5">Respondent Sandoval-Sanchez was in a line of workers entering the plant. Sandoval-Sanchez testified that he did not realize that immigration officers were checking people entering the plant, but that he did see standing at the plant entrance a man in uniform who appeared to be a police officer. Agent Bower testified that it was probable that he, not his partner, had questioned Sandoval-Sanchez at the plant, but that he could not be absolutely positive. The employee he thought he remembered as Sandoval-Sanchez had been “very evasive,” had averted his head, turned around, and walked away when he saw Agent Bower. App. 137, 138. Bower was certain that no one was questioned about his status unless his actions had given the agents reason to believe that he was an undocumented alien.</p>
<p id="b1079-6">Thirty-seven employees, including Sandoval-Sanchez, were briefly detained at the plant and then taken to the county jail. About one-third immediately availed themselves of the option of voluntary departure and were put on a bus to Mexico. Sandoval-Sanchez exercised his right to a deportation hearing. Sandoval-Sanchez was then questioned further, and Agent Bower recorded Sandoval-Sanchez’ admission of unlawful entry. Sandoval-Sanchez contends he was not aware that he had a right to remain silent.</p>
<p id="b1079-7">At his deportation hearing Sandoval-Sanchez contended that the evidence offered by the INS should be suppressed as the fruit of an unlawful arrest. The Immigration Judge considered and rejected Sandoval-Sanchez’ claim that he had been illegally arrested, but ruled in the alternative that the legality of the arrest was not relevant to the deportation hearing. <em>Matter of Sandoval-Sanchez, </em>No. A22 346 925 <page-number citation-index="1" label="1038">*1038</page-number>(INS, Oct. 7, 1977), reprinted in App. to Pet. for Cert. 104a. Based on the written record of Sandoval-Sanchez’ admissions the Immigration Judge found him deportable and granted him voluntary departure. The BIA dismissed Sandoval-Sanchez’ appeal. <em>In re Sandoval-Sanchez, </em>No. A22 346 925 (BIA, Feb. 21, 1980). It concluded that the circumstances of the arrest had not affected the voluntariness of his recorded admission, and again declined to invoke the exclusionary rule, relying on its earlier decision in <em>Matter of Sandoval, supra.</em></p>
<p id="b1080-7">On appeal the Court of Appeals concluded that Sandoval-Sanchez’ detention by the immigration officers violated the Fourth Amendment, that the statements he made were a product of that detention, and that the exclusionary rule barred their use in a deportation hearing. The deportation order against Sandoval-Sanchez was accordingly reversed.</p>
<p id="b1080-8">f — n J — 4</p>
<p id="b1080-3">A deportation proceeding is a purely civil action to determine eligibility to remain in this country, not to punish an unlawful entry, though entering or remaining unlawfully in this country is itself a crime. <span class="citation no-link">8 U. S. C. §§ 1302</span>,1306, 1325. The deportation hearing looks prospectively to the respondent’s right to remain in this country in the future. Past conduct is relevant only insofar as it may shed light on the respondent’s right to remain. See <span class="citation no-link">8 U. S. C. §§ 1251</span>, 1252(b); <em>Bugajewitz </em>v. <em>Adams, </em><span class="citation" data-id="97876"><a href="/opinion/97876/bugajewitz-v-adams/#591" aria-description="Citation for case: Bugajewitz v. Adams">228 U. S. 585, 591</a></span> (1913); <em>Fong Yue Ting </em>v. <em>United States, </em><span class="citation" data-id="9417622"><a href="/opinion/93665/fong-yue-ting-v-united-states/#730" aria-description="Citation for case: Fong Yue Ting v. United States">149 U. S. 698, 730</a></span> (1893).</p>
<p id="b1080-4">A deportation hearing is held before an immigration judge. The judge’s sole power is to order deportation; the judge cannot adjudicate guilt or punish the respondent for any crime related to unlawful entry into or presence in this country. Consistent with the civil nature of the proceeding, various protections that apply in the context of a criminal trial do not apply in a deportation hearing. The respondent must be given “a reasonable opportunity to be present at [the] proceeding,” but if the respondent fails to avail himself <page-number citation-index="1" label="1039">*1039</page-number>of that opportunity the hearing may proceed in his absence. <span class="citation no-link">8 U. S. C. § 1252</span>(b). In many deportation cases the INS must show only identity and alienage; the burden then shifts to the respondent to prove the time, place, and manner of his entry. See <span class="citation no-link">8 U. S. C. § 1361</span>; <em>Matter of Sandoval, </em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/" aria-description="Citation for case: SANDOVAL">17 I. &amp; N. Dec. 70</a></span> (BIA 1979). A decision of deportability need be based only on “reasonable, substantial, and probative evidence,” <span class="citation no-link">8 U. S. C. § 1252</span>(b)(4). The BIA for its part has required only “clear, unequivocal and convincing” evidence of the respondent’s deportability, not proof beyond a reasonable doubt. <span class="citation no-link">8 CFR §242.14</span>(a) (1984). The Courts of Appeals have held, for example that the absence of <em>Miranda </em>warnings does not render an otherwise voluntary statement by the respondent inadmissible in a deportation case. <em>Navia-Duran </em>v. <em>INS, </em><span class="citation" data-id="352273"><a href="/opinion/352273/maria-irma-navia-duran-v-immigration-and-naturalization-service/#808" aria-description="Citation for case: Maria Irma Navia-Duran v. Immigration and Naturalization...">568 F. 2d 803, 808</a></span> (CA1 1977); <em>Avila-Gallegos </em>v. <em>INS, </em><span class="citation" data-id="331113"><a href="/opinion/331113/miguel-avila-gallegos-v-immigration-and-naturalization-service/#667" aria-description="Citation for case: Miguel Avila-Gallegos v. Immigration and Naturalization...">525 F. 2d 666, 667</a></span> (CA2 1975); <em>Chavez-Raya </em>v. <em>INS, </em><span class="citation" data-id="328798"><a href="/opinion/328798/ampara-chavez-raya-and-gloria-quintanar-de-chavez-v-immigration-and/#399" aria-description="Citation for case: Ampara Chavez-Raya and Gloria Quintanar De Chavez v....">519 F. 2d 397, 399-401</a></span> (CA7 1975). See also <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#236" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 236-237</a></span> (1960) (search permitted incidental to an arrest pursuant to an administrative warrant issued by the INS); <em>Galvan </em>v. <em>Press, </em><span class="citation" data-id="9421085"><a href="/opinion/105227/galvan-v-press/#531" aria-description="Citation for case: Galvan v. Press">347 U. S. 522, 531</a></span> (1954) <em>(Ex Post Facto </em>Clause has no application to deportation); <em>Carlson </em>v. <em>Landon, </em><span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/#544" aria-description="Citation for case: Carlson v. Landon">342 U. S. 524, 544-546</a></span> (1952) (Eighth Amendment does not require bail to be granted in certain deportation cases); <em>United States ex rel. Bilokumsky </em>v. <em>Tod, </em><span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#157" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U. S. 149, 157</a></span> (1923) (involuntary confessions admissible at deportation hearing). In short, a deportation hearing is intended to provide a streamlined determination of eligibility to remain in this country, nothing more. The purpose of deportation is not to punish past transgressions but rather to put an end to a continuing violation of the immigration laws.</p>
<p id="b1081-5">III</p>
<p id="b1081-6">The “body” or identity of a defendant or respondent in a criminal or civil proceeding is never itself suppressible as a fruit of an unlawful arrest, even if it is conceded that an unlawful arrest, search, or interrogation occurred. See <em>Ger-</em><page-number citation-index="1" label="1040">*1040</page-number><em>stein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 119</a></span> (1975); <em>Frisbie </em>v. <em>Collins, </em><span class="citation" data-id="104977"><a href="/opinion/104977/frisbie-v-collins/#522" aria-description="Citation for case: Frisbie v. Collins">342 U. S. 519, 522</a></span> (1952); <em>United States ex rel. Bilokumsky </em>v. <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#158" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod"><em>Tod, supra, </em>at 158</a></span>. A similar rule applies in forfeiture proceedings directed against contraband or forfeitable property. See, <em>e. g., United States </em>v. <em>Eighty-Eight Thousand, Five Hundred Dollars, </em><span class="citation" data-id="399492"><a href="/opinion/399492/united-states-v-eighty-eight-thousand-five-hundred-dollars-appeal-of/" aria-description="Citation for case: United States v. Eighty-Eight Thousand, Five Hundred...">671 F. 2d 293</a></span> (CA8 1982); <em>United States </em>v. <em>One (1) 1971 Harley-Davidson Motorcycle, </em><span class="citation" data-id="324058"><a href="/opinion/324058/united-states-v-one-1-1971-harley-davidson-motorcycle-serial-4a25791h1/" aria-description="Citation for case: United States v. One (1) 1971 Harley-Davidson Motorcycle...">508 F. 2d 351</a></span> (CA9 1974); <em>United States </em>v. <em>One 1965 Buick, </em><span class="citation" data-id="280943"><a href="/opinion/280943/united-states-v-one-1965-buick-etc-wilbur-dean-and-delores-dean/" aria-description="Citation for case: United States v. One 1965 Buick, Etc., Wilbur Dean and...">397 F. 2d 782</a></span> (CA6 1968).</p>
<p id="b1082-7">On this basis alone the Court of Appeals’ decision as to respondent Lopez-Mendoza must be reversed. At his deportation hearing Lopez-Mendoza objected only to the fact that he had been summoned to a deportation hearing following an unlawful arrest; he entered no objection to the evidence offered against him. The BIA correctly ruled that “[t]he mere fact of an illegal arrest has no bearing on a subsequent deportation proceeding.”<footnotemark>1</footnotemark> <em>In re Lopez-Mendoza, </em>No. A22 452 208 (BIA, Sept. 19, 1979), reprinted in App. to Pet. for Cert. 102a.</p>
<p id="b1082-8"><em>&gt; </em>HH</p>
<p id="b1082-3">Respondent Sandoval-Sanchez has a more substantial claim. He objected not to his compelled presence at a deportation proceeding, but to evidence offered at that proceeding. The general rule in a criminal proceeding is that statements and other evidence obtained as a result of an unlawful, warrantless arrest are suppressible if the link between the <page-number citation-index="1" label="1041">*1041</page-number>evidence and the unlawful conduct is not too attenuated. <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). The reach of the exclusionary rule beyond the context of a criminal prosecution, however, is less clear. Although this Court has once stated in dictum that “[i]t may be assumed that evidence obtained by the [Labor] Department through an illegal search and seizure cannot be made the basis of a finding in deportation proceedings,” <em>United States ex rel. Bilokumsky </em>v. <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#155" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod"><em>Tod, supra, </em>at 155</a></span>, the Court has never squarely addressed the question before. Lower court decisions dealing with this question are sparse.<footnotemark>2</footnotemark></p>
<p id="b1083-5">In <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976), this Court set forth a framework for deciding in what types of proceeding application of the exclusionary rule is appropriate. Imprecise as the exercise may be, the Court recognized in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>that there is no choice but to weigh the likely social benefits of excluding unlawfully seized evidence against the likely costs. On the benefit side of the balance “the ‘prime purpose’ of the [exclusionary] rule, if not the sole one, ‘is to deter future unlawful police conduct.’ ” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#446" aria-description="Citation for case: United States v. Janis"><em>Id., </em>at 446</a></span>, quoting <em>United States </em>v. Calandra, <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347</a></span> (1974). On the cost side there is the loss of often probative evidence and all of the secondary costs that flow from the less accurate or more cumbersome adjudication that therefore occurs.</p>
<p id="b1083-6">At stake in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>was application of the exclusionary rule in a federal civil tax assessment proceeding following, the unlawful seizure of evidence by state, not federal, officials. The Court noted at the outset that “[i]n the complex and tur<page-number citation-index="1" label="1042">*1042</page-number>bulent history of the rule, the Court never has applied it to exclude evidence from a civil proceeding, federal or state.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#447" aria-description="Citation for case: United States v. Janis">428 U. S., at 447</a></span> (footnote omitted). Two factors in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>suggested that the deterrence value of the exclusionary rule in the context of that case was slight. First, the state law enforcement officials were already “punished” by the exclusion of the evidence in the state criminal trial as a result of the same conduct. <em>Id,., </em>at 448. Second, the evidence was also excludable in any federal criminal trial that might be held. Both factors suggested that further application of the exclusionary rule in the federal civil proceeding would contribute little more to the deterrence of unlawful conduct by state officials. On the cost side of the balance, <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>focused simply on the loss of “concededly relevant and reliable evidence.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#447" aria-description="Citation for case: United States v. Janis"><em>Id., </em>at 447</a></span>. The Court concluded that, on balance, this cost outweighed the likely social benefits achievable through application of the exclusionary rule in the federal civil proceeding.</p>
<p id="b1084-5">While it seems likely that the deterrence value of applying the exclusionary rule in deportation proceedings would be higher than it was in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>it is also quite clear that the social costs would be very much greater as well. Applying the <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>balancing test to the benefits and costs of excluding concededly reliable evidence from a deportation proceeding, we therefore reach the same conclusion as in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>.</em></p>
<p id="b1084-6">The likely deterrence value of the exclusionary rule in deportation proceedings is difficult to assess. On the one hand, a civil deportation proceeding is a civil complement to a possible criminal prosecution, and to this extent it resembles the civil proceeding under review in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>. </em>The INS does not suggest that the exclusionary rule should not continue to apply in criminal proceedings against an alien who unlawfully enters or remains in this country, and the prospect of losing evidence that might otherwise be used in a criminal prosecution undoubtedly supplies some residual deterrent to unlawful conduct by INS officials. But it must be acknowledged <page-number citation-index="1" label="1043">*1043</page-number>that only a very small percentage of arrests of aliens are intended or expected to lead to criminal prosecutions. Thus the arresting officer’s primary objective, in practice, will be to use evidence in the civil deportation proceeding. Moreover, here, in contrast to <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>the agency officials who effect the unlawful arrest are the same officials who subsequently bring the deportation action. As recognized in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>the exclusionary rule is likely to be most effective when applied to such “intrasovereign” violations.</p>
<p id="b1085-5">Nonetheless, several other factors significantly reduce the likely deterrent value of the exclusionary rule in a civil deportation proceeding. First, regardless of how the arrest is effected, deportation will still be possible when evidence not derived directly from the arrest is sufficient to support deportation. As the BIA has recognized, in many deportation proceedings “the sole matters necessary for the Government to establish are the respondent’s identity and alienage — at which point the burden shifts to the respondent to prove the time, place and manner of entry.” <em>Matter of Sandoval, </em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/#79" aria-description="Citation for case: SANDOVAL">17 I. &amp; N. Dec., at 79</a></span>. Since the person and identity of the respondent are not themselves suppressible, see <em>supra, </em>at 1039-1040, the INS must prove only alienage, and that will sometimes be possible using evidence gathered independently of, or sufficiently attenuated from, the original arrest. See <em>Matter of Sandoval, supra, </em>at 79; see, <em>e. g., Avila-Gallegos </em>v. <span class="citation" data-id="331113"><a href="/opinion/331113/miguel-avila-gallegos-v-immigration-and-naturalization-service/" aria-description="Citation for case: Miguel Avila-Gallegos v. Immigration and Naturalization..."><em>INS, 525 </em>F. 2d 666</a></span> (CA2 1975). The INS’s task is simplified in this regard by the civil nature of the proceeding. As Justice Brandéis stated: “Silence is often evidence of the most persuasive character. . . . [T]here is no rule of law which prohibits officers charged with the administration of the immigration law from drawing an inference from the silence of one who is called upon to speak. ... A person arrested on the preliminary warrant is not protected by a presumption of citizenship comparable to the presumption of innocence in a criminal case. There is no provision which forbids drawing an adverse inference from the fact of stand<page-number citation-index="1" label="1044">*1044</page-number>ing mute.” <em>United States ex rel. Bilokumsky </em>v. <em>Tod, </em><span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#163" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U. S., at 163-154</a></span>.</p>
<p id="b1086-5">The second factor is a practical one. In the course of a year the average INS agent arrests almost 500 illegal aliens. Brief for Petitioner 38. Over 97.5% apparently agree to voluntary deportation without a formal hearing. <span class="citation" data-id="8916793"><a href="/opinion/8927000/lopez-mendoza-v-immigration-naturalization-service/#1071" aria-description="Citation for case: Lopez-Mendoza v. Immigration &amp; Naturalization Service">705 F. 2d, at 1071, n. 17</a></span>. Among the remainder who do request a formal hearing (apparently a dozen or so in all, per officer, per year) very few challenge the circumstances of their arrests. As noted by the Court of Appeals, “the BIA was able to find only two reported immigration cases since 1899 in which the [exclusionary] rule was applied to bar unlawfully seized evidence, only one other case in which the rule’s application was specifically addressed, and fewer than fifty BIA proceedings since 1952 in which a Fourth Amendment challenge to the introduction of evidence was even raised.” <span class="citation" data-id="8916793"><a href="/opinion/8927000/lopez-mendoza-v-immigration-naturalization-service/#1071" aria-description="Citation for case: Lopez-Mendoza v. Immigration &amp; Naturalization Service"><em>Id., </em>at 1071</a></span>. Every INS agent knows, therefore, that it is highly unlikely that any particular arrestee will end up challenging the lawfulness of his arrest in a formal deportation proceeding. When an occasional challenge is brought, the consequences from the point of view of the officer’s overall arrest and deportation record will be trivial. In these circumstances, the arresting officer is most unlikely to shape his conduct in anticipation of the exclusion of evidence at a formal deportation hearing.</p>
<p id="b1086-6">Third, and perhaps most important, the INS has its own comprehensive scheme for deterring Fourth Amendment violations by its officers. Most arrests of illegal aliens away from the border occur during farm, factory, or other workplace surveys. Large numbers of illegal aliens are often arrested at one time, and conditions are understandably chaotic. See Brief for Petitioner in <em>INS </em>v. <em>Delgado, </em>O. T. 1983, No. 82-1271, pp. 3-5. To safeguard the rights of those who are lawfully present at inspected workplaces the INS has developed rules restricting stop, interrogation, and arrest practices. <em>Id., </em>at 7, n. 7, 32-40, and n. 25. These <page-number citation-index="1" label="1045">*1045</page-number>regulations require that no one be detained without reasonable suspicion of illegal alienage, and that no one be arrested unless there is an admission of illegal alienage or other strong evidence thereof. New immigration officers receive instruction and examination in Fourth Amendment law, and others receive periodic refresher courses in law. Brief for Petitioner 39-40. Evidence seized through intentionally unlawful conduct is excluded by Department of Justice policy from the proceeding for which it was obtained. See Memorandum from Benjamin R. Civiletti to Heads of Offices, Boards, Bureaus and Divisions, Violations of Search and Seizure Law (Jan. 16, 1981). The INS also has in place a procedure for investigating and punishing immigration officers who commit Fourth Amendment violations. See Office of General Counsel, INS, U. S. Dept, of Justice, The Law of Arrest, Search, and Seizure for Immigration Officers 35 (Jan. 1983). The INS’s attention to Fourth Amendment interests cannot guarantee that constitutional violations will not occur, but it does reduce the likely deterrent value of the exclusionary rule. Deterrence must be measured at the margin.</p>
<p id="b1087-5">Finally, the deterrent value of the exclusionary rule in deportation proceedings is undermined by the availability of alternative remedies for institutional practices by the INS that might violate Fourth Amendment rights. The INS is a single agency, under central federal control, and engaged in operations of broad scope but highly repetitive character. The possibility of declaratory relief against the agency thus offers a means for challenging the validity of INS practices, when standing requirements for bringing such an action can be met. Cf. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984).</p>
<p id="b1087-6">Respondents contend that retention of the exclusionary rule is necessary to safeguard the Fourth Amendment rights of ethnic Americans, particularly the Hispanic-Americans lawfully in this country. We recognize that respondents raise here legitimate and important concerns. But application of the exclusionary rule to civil deportation proceedings <page-number citation-index="1" label="1046">*1046</page-number>can be justified only if the rule is likely to add significant protection to these Fourth Amendment rights. The exclusionary rule provides no remedy for completed wrongs; those lawfully in this country can be interested in its application only insofar as it may serve as an effective deterrent to future INS misconduct. For the reasons we have discussed we conclude that application of the rule in INS civil deportation proceedings, as in the circumstances discussed in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>“is unlikely to provide significant, much less substantial, additional deterrence.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#458" aria-description="Citation for case: United States v. Janis">428 U. S., at 458</a></span>. Important as it is to protect the Fourth Amendment rights of all persons, there is no convincing indication that application of the exclusionary rule in civil deportation proceedings will contribute materially to that end.</p>
<p id="b1088-5">On the other side of the scale, the social costs of applying the exclusionary rule in deportation proceedings are both unusual and significant. The first cost is one that is unique to continuing violations of the law. Applying the exclusionary rule in proceedings that are intended not to punish past transgressions but to prevent their continuance or renewal would require the courts to close their eyes to ongoing violations of the law. This Court has never before accepted costs of this character in applying the exclusionary rule.</p>
<p id="b1088-6">Presumably no one would argue that the exclusionary rule should be invoked to prevent an agency from ordering corrective action at a leaking hazardous waste dump if the evidence underlying the order had been improperly obtained, or to compel police to return contraband explosives or drugs to their owner if the contraband had been unlawfully seized. On the rare occasions that it has considered costs of this type the Court has firmly indicated that the exclusionary rule does not extend this far. See <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#54" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 54</a></span> (1951); <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#710" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 710</a></span> (1948). The rationale for these holdings is not difficult to find. “Both <em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span> </em>and <em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span> </em>concerned objects the possession of which, without more, constitutes a crime. The re<page-number citation-index="1" label="1047">*1047</page-number>possession of such <em>per se </em>contraband by Jeffers and Trupiano would have subjected them to criminal penalties. The return of the contraband would clearly have frustrated the express public policy against the possession of such objects.” <em>One 1958 Plymouth Sedan </em>v. <em>Pennsylvania, </em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#699" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693, 699</a></span> (1965) (footnote omitted). Precisely the same can be said here. Sandoval-Sanchez is a person whose unregistered presence in this country, without more, constitutes a crime.<footnotemark>3</footnotemark> His release within our borders would immediately subject him to criminal penalties. His release would clearly frustrate the express public policy against an alien’s unregistered presence in this country. Even the objective of deterring Fourth Amendment violations should not require such a result. The constable’s blunder may allow the criminal to go free, but we have never suggested that it allows the criminal to continue in the commission of an ongoing crime. When the crime in question involves unlawful presence in this country, the criminal may go free, but he should not go free within our borders.<footnotemark>4</footnotemark></p>
<p id="b1090-4"><page-number citation-index="1" label="1048">*1048</page-number>Other factors also weigh against applying the exclusionary rule in deportation proceedings. The INS currently operates a deliberately simple deportation hearing system, streamlined to permit the quick resolution of very large numbers of deportation actions, and it is against this backdrop that the costs of the exclusionary rule must be assessed. The costs of applying the exclusionary rule, like the benefits, must be measured at the margin.</p>
<p id="b1090-5">The average immigration judge handles about six deportation hearings per day. Brief for Petitioner 27, n. 16. Neither the hearing officers nor the attorneys participating in those hearings are likely to be well versed in the intricacies of Fourth Amendment law. The prospect of even occasional invocation of the exclusionary rule might significantly change and complicate the character of these proceedings. The BIA has described the practical problems as follows:</p>
<blockquote id="b1090-6">“Absent the applicability of the exclusionary rule, questions relating to deportability routinely involve simple factual allegations and matters of proof. When Fourth Amendment issues are raised at deportation hearings, the result is a diversion of attention from the main issues which those proceedings were created to resolve, both in terms of the expertise of the administrative decision makers and of the structure of the forum to accommodate inquiries into search and seizure questions. The result frequently seems to be a long, confused record in which the issues are not clearly defined and in which there is voluminous testimony .... The ensuing delays and inordinate amount of time spent on such cases at all levels has an adverse impact on the effective adminis<page-number citation-index="1" label="1049">*1049</page-number>tration of the immigration laws .... This is particularly true in a proceeding where delay may be the only ‘defense’ available and where problems already exist with the use of dilatory tactics.” <em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/" aria-description="Citation for case: SANDOVAL">Matter of Sandoval</a></span>, </em>17 I. &amp; N., at 80 (footnote omitted).</blockquote>
<p id="b1091-5">This sober assessment of the exclusionary rule’s likely costs, by the agency that would have to administer the rule in at least the administrative tiers of its application, cannot be brushed off lightly.</p>
<p id="b1091-6">The BIA’s concerns are reinforced by the staggering dimension of the problem that the INS confronts. Immigration officers apprehend over one million deportable aliens in this country every year. <span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/#85" aria-description="Citation for case: SANDOVAL">Id., at 85</a></span>. A single agent may arrest many illegal aliens every day. Although the investigatory burden does not justify the commission of constitutional violations, the officers cannot be expected to compile elaborate, contemporaneous, written reports detailing the circumstances of every arrest. At present an officer simply completes a “Record of Deportable Alien” that is introduced to prove the INS’s case at the deportation hearing; the officer rarely must attend the hearing. Fourth Amendment suppression hearings would undoubtedly require considerably more, and the likely burden on the administration of the immigration laws would be correspondingly severe.</p>
<p id="b1091-7">Finally, the INS advances the credible argument that applying the exclusionary rule to deportation proceedings might well result in the suppression of large amounts of information that had been obtained entirely lawfully. INS arrests occur in crowded and confused circumstances. Though the INS agents are instructed to follow procedures that adequately protect Fourth Amendment interests, agents will usually be able to testify only to the fact that they followed INS rules. The demand for a precise account of exactly what happened in each particular arrest would plainly preclude mass arrests, even when the INS is confronted, <page-number citation-index="1" label="1050">*1050</page-number>as it often is, with massed numbers of ascertainably illegal aliens, and even when the arrests can be and are conducted in full compliance with all Fourth Amendment requirements.</p>
<p id="b1092-5">In these circumstances we are persuaded that the <em>Jams </em>balance between costs and benefits comes out against applying the exclusionary rule in civil deportation hearings held by the INS. By all appearances the INS has already taken sensible and reasonable steps to deter Fourth Amendment violations by its officers, and this makes the likely additional deterrent value of the exclusionary rule small. The costs of applying the exclusionary rule in the context of civil deportation hearings are high. In particular, application of the exclusionary rule in cases such as Sandoval-Sanchez’, would compel the courts to release from custody persons who would then immediately resume their commission of a crime through their continuing, unlawful presence in this country. “There comes a point at which courts, consistent with their duty to administer the law, cannot continue to create barriers to law enforcement in the pursuit of a supervisory role that is properly the duty of the Executive and Legislative Branches.” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#459" aria-description="Citation for case: United States v. Janis">428 U. S., at 459</a></span>. That point has been reached here.</p>
<p id="b1092-6">y</p>
<p id="b1092-7">We do not condone any violations of the Fourth Amendment that may have occurred in the arrests of respondents Lopez-Mendoza or Sandoval-Sanchez. Moreover, no challenge is raised here to the INS’s own internal regulations. Cf. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984). Our conclusions concerning the exclusionary rule’s value might change, if there developed good reason to believe that Fourth Amendment violations by INS officers were widespread. Cf. <em>United States </em>v. <em>Leon, ante, </em>at 928 (Blackmun, J., concurring). Finally, we do not deal here with egregious violations of Fourth Amendment or other liberties that might transgress notions of fundamental fairness and undermine <page-number citation-index="1" label="1051">*1051</page-number>the probative value of the evidence obtained.<footnotemark>5</footnotemark> Cf. <em>Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952). At issue here is the exclusion of credible evidence gathered in connection -with peaceful arrests by INS officers. We hold that evidence derived from such arrests need not be suppressed in an INS civil deportation hearing.</p>
<p id="b1093-5">The judgment of the Court of Appeals is therefore</p>
<p id="b1093-6">
<em>Reversed.</em>
</p>
<footnote label="*">
<p id="b1076-9">The Chief Justice joins all but Part V of this opinion.</p>
</footnote>
<footnote label="1">
<p id="b1082-4"> The Court of Appeals brushed over Lopez-Mendoza’s failure to object to the evidence in an apparently unsettled footnote of its decision. The Court of Appeals was initially of the view that a motion to terminate a proceeding on the ground that the arrest of the respondent was unlawful is, “for all practical purposes,” the same as a motion to suppress evidence as the fruit of an unlawful arrest. Slip opinion, at 1765, n. 1 (Apr. 25, 1983). In the bound report of its opinion, however, the Court of Appeals takes a somewhat different view, stating in a revised version of the same footnote that “the only reasonable way to interpret the motion to terminate is as one that includes both a motion to suppress and a motion to dismiss.” <span class="citation" data-id="8916793"><a href="/opinion/8927000/lopez-mendoza-v-immigration-naturalization-service/#1060" aria-description="Citation for case: Lopez-Mendoza v. Immigration &amp; Naturalization Service">705 F. 2d 1059, 1060, n. 1</a></span> (1983).</p>
</footnote>
<footnote label="2">
<p id="b1083-7"> In <em>United States </em>v. <em>Wong Quong Wong, </em><span class="citation" data-id="9336336"><a href="/opinion/9340976/united-states-v-wong-quong-wong/" aria-description="Citation for case: United States v. Wong Quong Wong">94 F. 832</a></span> (Vt. 1899), a District Judge excluded letters seized from the appellant in a civil deportation proceeding. In <em>Ex parte Jackson, </em><span class="citation" data-id="8815099"><a href="/opinion/8830191/ex-parte-jackson/" aria-description="Citation for case: Ex parte Jackson">263 F. 110</a></span> (Mont.), appeal dism’d <em>sub nom. Andrews </em>v. <em>Jackson, </em><span class="citation" data-id="8817491"><a href="/opinion/8832507/andrews-v-jackson/" aria-description="Citation for case: Andrews v. Jackson">267 F. 1022</a></span> (CA9 1920), another District Judge granted habeas corpus relief on the ground that papers and pamphlets used against the habeas petitioner in a deportation proceeding had been unlawfully seized. <em>Wong Chung Che </em>v. <em>INS, </em><span class="citation" data-id="350514"><a href="/opinion/350514/wong-chung-che-and-wong-pui-tong-v-immigration-and-naturalization-service/" aria-description="Citation for case: Wong Chung Che and Wong Pui Tong v. Immigration and...">565 F. 2d 166</a></span> (CA11977), held that papers obtained by INS agents in an unlawful search are inadmissible in deportation proceedings.</p>
</footnote>
<footnote label="3">
<p id="b1089-5"> Sandoval-Sanchez was arrested on June 23, 1977. His deportation hearing was held on October 7, 1977. By that time he was under a duty to apply for registration as an alien. A failure to do so plainly constituted a continuing crime. <span class="citation no-link">8 U. S. C. §§ 1302</span>, 1306. Sandoval-Sanchez was not, of course, prosecuted for this crime, and we do not know whether or not he did make the required application. But it is safe to assume that the exclusionary rule would never be at issue in a deportation proceeding brought against an alien who entered the country unlawfully and then voluntarily admitted to his unlawful presence in an application for registration.</p>
<p id="b1089-6">Sandoval-Sanchez was also not prosecuted for his initial illegal entry into this country, an independent crime under <span class="citation no-link">8 U. S. C. § 1326</span>. We need not decide whether or not remaining in this country following an illegal entry is a continuing or a completed crime under § 1325. The question is academic, of course, since in either event the unlawful entry remains both punishable and continuing grounds for deportation. See <span class="citation no-link">8 U. S. C. § 1251</span>(a)(2).</p>
</footnote>
<footnote label="4">
<p id="b1089-7"> Similarly, in <em>Sure-Tan, Inc. </em>v. <em>NLRB, </em><span class="citation" data-id="9842062"><a href="/opinion/111223/sure-tan-inc-v-national-labor-relations-board/" aria-description="Citation for case: Sure-Tan, Inc. v. National Labor Relations Board">467 U. S. 883</a></span> (1984), the Court concluded that an employer can be guilty of an unfair labor practice in his dealings with an alien notwithstanding the alien’s illegal presence in this country. Retrospective sanctions against the employer may accord<page-number citation-index="1" label="1048">*1048</page-number>ingly be imposed by the National Labor Relations Board to further the public policy against unfair labor practices. But while he maintains the status of an illegal alien, the employee is plainly not entitled to the prospective relief — reinstatement and continued employment — that probably would be granted to other victims of similar unfair labor practices.</p>
</footnote>
<footnote label="5">
<p id="b1093-9"> We note that subsequent to its decision in <em>Matter of Sandoval, </em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/" aria-description="Citation for case: SANDOVAL">17 I. <em>&amp; </em>N. Dec. 70</a></span> (1979), the BIA held that evidence will be excluded if the circumstances surrounding a particular arrest and interrogation would render use of the evidence obtained thereby “fundamentally unfair” and in violation of due process requirements of the Fifth Amendment. <em>Matter of Toro, </em>17 I. &amp;. N. Dec. 340, 343 (1980). See also <em>Matter of Garcia, </em><span class="citation" data-id="6075297"><a href="/opinion/6208719/garcia/#321" aria-description="Citation for case: GARCIA">17 I. &amp; N. Dec. 319, 321</a></span> (1980) (suppression of admission of alienage obtained after request for counsel had been repeatedly refused); <em>Matter of Ramira-Cordova, </em>No. A21 095 659 (Feb. 21, 1980) (suppression of evidence obtained as a result of a nighttime warrantless entry into the aliens’ residence).</p>
</footnote>
</opinion>
```

---
