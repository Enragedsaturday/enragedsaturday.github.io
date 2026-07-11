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

## GROUP: _overhaul2/lake/cases/Harlow v. Fitzgerald.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Harlow v. Fitzgerald"
type: case
citation: "457 U.S. 800 (1982)"
parallel_cite: "102 S. Ct. 2727; 73 L. Ed. 2d 396"
neutral_cite: 1982 U.S. LEXIS 139
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1982
date_decided: 1982-06-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1982-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Harlow v. Fitzgerald
  varies_by_point: false
  scope_note: "Objective standard refined (not displaced) by later cases governing the clearly-established inquiry."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110763/harlow-v-fitzgerald/"
  cluster_id: 110763
  opinion_id: 9428863
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Anchor"
related: ["[[Saucier v. Katz]]", "[[Pearson v. Callahan]]", "[[City of Tahlequah v. Bond]]"]
aliases: []
tags: ["case", "qualified-immunity", "section-1983", "clearly-established-law", "objective-test"]
holding: "Reformulated qualified immunity as a purely OBJECTIVE test: officials performing discretionary functions are shielded from civil damages…"
lake:
  record_id: Harlow v. Fitzgerald
  status: verified
  projected_at: 2026-07-06
---

# Harlow v. Fitzgerald

*457 U.S. 800 (1982)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A. Ernest Fitzgerald, a former Air Force management analyst, sued senior aides to President Nixon, claiming he had been unlawfully discharged in retaliation for his whistleblowing testimony to Congress. The aides asserted [[Qualified Immunity|qualified immunity]]. (The suit was a *[[Bivens v. Six Unknown Named Agents|Bivens]]* action against federal officials, but the immunity standard the Court announced governs § 1983 suits against state officials as well.) The Court used the case to re-examine the standard for [[Qualified Immunity|qualified immunity]].

## Issue
What standard governs the [[Qualified Immunity|qualified immunity]] of government officials performing discretionary functions when they are sued for civil damages.

## Rule
[[Qualified Immunity|Qualified immunity]] is governed by a purely objective standard keyed to clearly established law. "[G]overnment officials performing discretionary functions generally are shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known." — 457 U.S. at 818. ^pin-818

The Court abandoned the older inquiry's subjective "good faith / malice" prong because it too often defeated summary judgment and exposed officials to the burdens of trial and discovery; immunity now turns on the objective legal reasonableness of the conduct measured against clearly established law.

## Application
Because the governing inquiry is objective, resolving the aides' immunity did not require probing their subjective intent; instead the question was whether their alleged conduct violated clearly established rights of which a reasonable official would have known. The Court therefore [[Reading and Citing Cases#vacated|vacated]] the denial of summary judgment and [[Reading and Citing Cases#on-remand|remanded]] for the lower court to apply the new objective standard.

## Conclusion
[[Qualified Immunity|Qualified immunity]] is determined by an objective "clearly established law" test, not by an official's subjective good faith; the judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]] for application of that standard.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Harlow*'s objective standard remains the foundation of qualified-immunity doctrine; later cases refine the "clearly established" inquiry (e.g., the level of generality and case-specificity stressed in [[City of Tahlequah v. Bond]]) without disturbing *Harlow*'s objective test.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *Harlow v. Fitzgerald*, 457 U.S. 800 (1982) — https://www.courtlistener.com/opinion/110763/harlow-v-fitzgerald/ — pinpoint: 818.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3a422119d3cec594", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Harlow v. Fitzgerald"}, "payload": {"all": [{"cite": "457 U.S. 800", "page": "800", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "457"}, {"cite": "102 S. Ct. 2727", "page": "2727", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "102"}, {"cite": "73 L. Ed. 2d 396", "page": "396", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "73"}, {"cite": "1982 U.S. LEXIS 139", "page": "139", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1982"}], "display": "457 U.S. 800", "official": {"cite": "457 U.S. 800", "page": "800", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "457"}, "official_selection_present": true, "record_id": "Harlow v. Fitzgerald"}}
{"assertion_id": "f9952464d1f2cbc3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-818", "record_id": "Harlow v. Fitzgerald"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-818", "pinpoint_status": "slip-only", "quote": "--- # Harlow v. Fitzgerald *457 U.S. 800 (1982)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A. Ernest Fitzgerald, a former Air Force management analyst, sued senior aides to President Nixon, claiming he had been unlawfully discharged in retaliation for his whistleblowing testimony to Congress. The aides asserted qualified immunity. (The suit was a *Bivens* action against federal officials, but the immunity standard the Court announced governs § 1983 suits against state officials as well.) The Court used the case to re-examine the standard for qualified immunity. ## Issue What standard governs the qualified immunity of government officials performing discretionary functions when they are sued for civil damages. ## Rule Qualified immunity is governed by a purely objective standard keyed to clearly established law.", "quote_fidelity": "mismatch", "record_id": "Harlow v. Fitzgerald", "star_marker": null}}
{"assertion_id": "6324d1261c707990", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Harlow v. Fitzgerald"}, "payload": {"as_of_content": "1982-06-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Harlow v. Fitzgerald", "scope_note": "Objective standard refined (not displaced) by later cases governing the clearly-established inquiry.", "varies_by_point": false}}
```

### lake record — Harlow v. Fitzgerald

```json
{
  "schema_version": "s2.v1",
  "record_id": "Harlow v. Fitzgerald",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Harlow v. Fitzgerald",
    "case_name_short": "Harlow",
    "case_name_full": "HARLOW Et Al. v. FITZGERALD",
    "input_case_name": "Harlow v. Fitzgerald",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1982-06-24",
    "year": 1982,
    "docket": null,
    "cluster_id": 110763,
    "lead_opinion_id": 9428863,
    "sibling_ids": [
      110763,
      9428863,
      9428864,
      9428865
    ],
    "absolute_url": "/opinion/110763/harlow-v-fitzgerald/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "457 U.S. 800",
      "volume": "457",
      "reporter": "U.S.",
      "page": "800",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "102 S. Ct. 2727",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 396",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "396",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1982 U.S. LEXIS 139",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "139",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "457 U.S. 800",
        "volume": "457",
        "reporter": "U.S.",
        "page": "800",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 S. Ct. 2727",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 396",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "396",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1982 U.S. LEXIS 139",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "139",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "457 U.S. 800",
    "official_selection": {
      "court_class": "scotus",
      "selected": "457 U.S. 800",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-818",
      "page": null,
      "quote": "--- # Harlow v. Fitzgerald *457 U.S. 800 (1982)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A. Ernest Fitzgerald, a former Air Force management analyst, sued senior aides to President Nixon, claiming he had been unlawfully discharged in retaliation for his whistleblowing testimony to Congress. The aides asserted qualified immunity. (The suit was a *Bivens* action against federal officials, but the immunity standard the Court announced governs \u00a7 1983 suits against state officials as well.) The Court used the case to re-examine the standard for qualified immunity. ## Issue What standard governs the qualified immunity of government officials performing discretionary functions when they are sued for civil damages. ## Rule Qualified immunity is governed by a purely objective standard keyed to clearly established law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1982-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Harlow v. Fitzgerald",
    "varies_by_point": false,
    "scope_note": "Objective standard refined (not displaced) by later cases governing the clearly-established inquiry.",
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennhurst State School and Hospital v. Halderman",
          "cluster_id": 111094,
          "cite": [
            "79 L. Ed. 2d 67",
            "104 S. Ct. 900",
            "465 U.S. 89",
            "1984 U.S. LEXIS 4",
            "52 U.S.L.W. 4155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Forsyth",
          "cluster_id": 111481,
          "cite": [
            "86 L. Ed. 2d 411",
            "105 S. Ct. 2806",
            "472 U.S. 511",
            "1985 U.S. LEXIS 113",
            "53 U.S.L.W. 4798",
            "2 Fed. R. Serv. 3d 221"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. McMillian",
          "cluster_id": 112693,
          "cite": [
            "117 L. Ed. 2d 156",
            "112 S. Ct. 995",
            "503 U.S. 1",
            "1992 U.S. LEXIS 1372"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Lacey v. Joseph Arpaio",
          "cluster_id": 807646,
          "cite": [
            "693 F.3d 896"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mireles v. Waco",
          "cluster_id": 112655,
          "cite": [
            "116 L. Ed. 2d 9",
            "112 S. Ct. 286",
            "502 U.S. 9",
            "1991 U.S. LEXIS 6225"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Seminole Tribe of Florida v. Florida",
          "cluster_id": 118011,
          "cite": [
            "134 L. Ed. 2d 252",
            "116 S. Ct. 1114",
            "517 U.S. 44",
            "1996 U.S. LEXIS 2165",
            "96 Cal. Daily Op. Serv. 2125",
            "96 Daily Journal DAR 3499",
            "64 U.S.L.W. 4167",
            "9 Fla. L. Weekly Fed. S 484",
            "34 Collier Bankr. Cas. 2d 1199",
            "42 ERC (BNA) 1289",
            "67 Empl. Prac. Dec. (CCH) 43,952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins Ex Rel. Robbins v. Oklahoma Ex Rel. Department of Human Services",
          "cluster_id": 170460,
          "cite": [
            "519 F.3d 1242",
            "70 Fed. R. Serv. 3d 175",
            "2008 U.S. App. LEXIS 5915",
            "2008 WL 747132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hunter v. Bryant",
          "cluster_id": 112671,
          "cite": [
            "116 L. Ed. 2d 589",
            "112 S. Ct. 534",
            "502 U.S. 224",
            "1991 U.S. LEXIS 7262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moss v. U.S. Secret Service",
          "cluster_id": 1450162,
          "cite": [
            "572 F.3d 962",
            "2009 U.S. App. LEXIS 15694",
            "2009 WL 2052985"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walker v. Schult",
          "cluster_id": 868764,
          "cite": [
            "717 F.3d 119",
            "2013 U.S. App. LEXIS 10397",
            "2013 WL 2249159"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cuoco v. Moritsugu",
          "cluster_id": 7080999,
          "cite": [
            "222 F.3d 99",
            "2000 WL 1041227"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Jones",
          "cluster_id": 117950,
          "cite": [
            "132 L. Ed. 2d 238",
            "115 S. Ct. 2151",
            "515 U.S. 304",
            "1995 U.S. LEXIS 3907"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110763 OR 9428863 OR 9428864 OR 9428865) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjg2Nzg3MjAwMDAwJnM9OTQwNjk2OCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110763+OR+9428863+OR+9428864+OR+9428865%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110763 OR 9428863 OR 9428864 OR 9428865)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTk4JnM9NzkwMzA0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110763+OR+9428863+OR+9428864+OR+9428865%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110763 OR 9428863 OR 9428864 OR 9428865)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzA4OTA1NjAwMDAwJnM9OTQ4NTYzNSZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110763+OR+9428863+OR+9428864+OR+9428865%29&type=o",
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
    "complete_query": "cites:(110763 OR 9428863 OR 9428864 OR 9428865)",
    "indexed_citing_opinions": 11839,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110763,
        "count": 10331,
        "count_source": "search"
      },
      {
        "opinion_id": 9428863,
        "count": 1355,
        "count_source": "search"
      },
      {
        "opinion_id": 9428864,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428865,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 22957,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/harlow-v-fitzgerald.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk3NDY4Mjgmcz03MTAzMjEwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110763+OR+9428863+OR+9428864+OR+9428865%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110763,
        "cited_id": 90311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 94400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 104906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 106334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 108610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 108802,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110059,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 350998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 356040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 366924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 370395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 382202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 389983,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 1507366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 2390269,
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
    "date_created": "2026-07-05T06:15:17Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:15:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:15:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:21:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:15:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Harlow v. Fitzgerald

```
<opinion type="majority">
<author id="b846-6">Justice Powell</author>
<p id="Ache">delivered the opinion of the Court.</p>
<p id="b846-7">The issue in this case is the scope of the immunity available to the senior aides and advisers of the President of the United States in a suit for damages based upon their official acts.</p>
<p id="b846-8">I</p>
<p id="b846-9">In this suit for civil damages petitioners Bryce Harlow and Alexander Butterfield are alleged to have participated in a conspiracy to violate the constitutional and statutory rights of the respondent A. Ernest Fitzgerald. Respondent avers that petitioners entered the conspiracy in their capacities as senior White House aides to former President Richard M. Nixon. As the alleged conspiracy is the same as that involved in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731, the facts need not be repeated in detail.</p>
<p id="b846-10">Respondent claims that Harlow joined the conspiracy in his role as the Presidential aide principally responsible for congressional relations.<footnotemark>1</footnotemark> At the conclusion of discovery the <page-number citation-index="1" label="803">*803</page-number>supporting evidence remained inferential. As evidence of Harlow’s conspiratorial activity respondent relies heavily on a series of conversations in which Harlow discussed Fitzgerald’s dismissal with Air Force Secretary Robert Seamans.<footnotemark>2</footnotemark> The other evidence most supportive of Fitzgerald’s claims consists of a recorded conversation in which the President later voiced a tentative recollection that Harlow was “all for canning” Fitzgerald.<footnotemark>3</footnotemark></p>
<p id="b847-5">Disputing Fitzgerald’s contentions, Harlow argues that exhaustive discovery has adduced no direct evidence of his in<page-number citation-index="1" label="804">*804</page-number>volvement in any wrongful activity.<footnotemark>4</footnotemark> He avers that Secretary Seamans advised him that considerations of efficiency required Fitzgerald’s removal by a reduction in force, despite anticipated adverse congressional reaction. Harlow asserts he had no reason to believe that a conspiracy existed. He contends that he took all his actions in good faith.<footnotemark>5</footnotemark></p>
<p id="b848-5">Petitioner Butterfield also is alleged to have entered the conspiracy not later than May 1969. Employed as Deputy Assistant to the President and Deputy Chief of Staff to H. R. Haldeman,<footnotemark>6</footnotemark> Butterfield circulated a White House memorandum in that month in which he claimed to have learned that Fitzgerald planned to “blow the whistle” on some “shoddy purchasing practices” by exposing these practices to public view.<footnotemark>7</footnotemark> Fitzgerald characterizes this memorandum as evi<page-number citation-index="1" label="805">*805</page-number>dence that Butterfield had commenced efforts to secure Fitzgerald’s retaliatory dismissal. As evidence that Butterfield participated in the conspiracy to conceal his unlawful discharge and prevent his reemployment, Fitzgerald cites communications between Butterfield and Haldeman in December 1969 and January 1970. After the President had promised at a press conference to inquire into Fitzgerald’s dismissal, Haldeman solicited Butterfield’s recommendations. In a subsequent memorandum emphasizing the importance of “loyalty,” Butterfield counseled against offering Fitzgerald another job in the administration at that time.<footnotemark>8</footnotemark></p>
<p id="b849-5">For his part, Butterfield denies that he was involved in any decision concerning Fitzgerald’s employment status until Haldeman sought his advice in December 1969 — more than a month after Fitzgerald’s termination had been scheduled and announced publicly by the Air Force. Butterfield states that he never communicated his views about Fitzgerald to any official of the Defense Department. He argues generally that nearly eight years of discovery have failed to turn up any evidence that he caused injury to Fitzgerald.<footnotemark>9</footnotemark></p>
<p id="b849-6">Together with their codefendant Richard Nixon, petitioners Harlow and Butterfield moved for summary judgment on February 12, 1980. In denying the motion the District Court upheld the legal sufficiency of Fitzgerald’s <em>Bivens (Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971)) claim under the First Amendment and his “inferred” statutory causes of action under <span class="citation no-link">5 U. S. C. §7211</span> (1976 ed., Supp. IV) and <span class="citation no-link">18 U. S. C. §1505</span>.<footnotemark>10</footnotemark> The court <page-number citation-index="1" label="806">*806</page-number>found that genuine issues of disputed fact remained for resolution at trial. It also ruled that petitioners were not entitled to absolute immunity. App. to Pet. for Cert. la-3a.</p>
<p id="b850-8">Independently of former President Nixon, petitioners invoked the collateral order doctrine and appealed the denial of their immunity defense to the Court of Appeals for. the District of Columbia Circuit. The Court of Appeals dismissed the appeal without opinion. <em><span class="citation no-link">Id.,</span> </em>at lla-12a. Never having determined the immunity available to the senior aides and advisers of the President of the United States, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./452/959/">452 U. S. 959</a></span> (1981).<footnotemark>11</footnotemark></p>
<p id="b850-9">H-1</p>
<p id="b850-3">As we reiterated today in <em>Nixon </em>v. Fitzgerald, <em>ante, </em>p. 731, our decisions consistently have held that government officials are entitled to some form of immunity from suits for damages. As recognized at common law, public officers require this protection to shield them from undue interference with their duties and' from potentially disabling threats of liability.</p>
<p id="b851-4"><page-number citation-index="1" label="807">*807</page-number>Our decisions have recognized immunity defenses of two kinds. For officials whose special functions or constitutional status requires complete protection from suit, we have recognized the defense of “absolute immunity.” The absolute immunity of legislators, in their legislative functions, see, <em>e. g., Eastland </em>v. <em>United States Servicemen’s Fund, </em><span class="citation" data-id="9426086"><a href="/opinion/109257/eastland-v-united-states-servicemens-fund/" aria-description="Citation for case: Eastland v. United States Servicemen&#x27;s Fund">421 U. S. 491</a></span> (1975), and of judges, in their judicial functions, see, <em>e. g., Stump </em>v. <em>Sparkman, </em><span class="citation" data-id="9427113"><a href="/opinion/109820/stump-v-sparkman/" aria-description="Citation for case: Stump v. Sparkman">435 U. S. 349</a></span> (1978), now is well settled. Our decisions also have extended absolute immunity to certain officials of the Executive Branch. These include prosecutors and similar officials, see <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#508" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 508-512</a></span> (1978), executive officers engaged in adjudicative functions, <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#513" aria-description="Citation for case: Butz v. Economou"><em>id., </em>at 513-517</a></span>, and the President of the United States, see <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731.</p>
<p id="b851-5">For executive officials in general, however, our cases make plain that qualified immunity represents the norm. In <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974), we acknowledged that high officials require greater protection than those with less complex discretionary responsibilities. Nonetheless, we held that a governor and his aides could receive the requisite protection from qualified or good-faith immunity. <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#247" aria-description="Citation for case: Scheuer v. Rhodes"><em>Id., </em>at 247-248</a></span>. In <em>Butz </em>v. <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Economou, supra,</a></span> </em>we extended the approach of <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>to high federal officials of the Executive Branch. Discussing in detail the considerations that also had underlain our decision in <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span>, </em>we explained that the recognition of a qualified immunity defense for high executives reflected an attempt to balance competing values: not only the importance of a damages remedy to protect the rights of citizens, <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#504" aria-description="Citation for case: Butz v. Economou">438 U. S., at 504-505</a></span>, but also “the need to protect officials who are required to exercise their discretion and the related public interest in encouraging the vigorous exercise of official authority.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou"><em>Id., </em>at 506</a></span>. Without discounting the adverse consequences of denying high officials an absolute immunity from private lawsuits alleging constitutional violations — consequences found sufficient in <em>Spalding </em>v. <em>Vilas, </em><span class="citation" data-id="94400"><a href="/opinion/94400/spalding-v-vilas/" aria-description="Citation for case: Spalding v. Vilas">161 U. S. 483</a></span> (1896), and <em>Barr </em>v. <em>Matteo, </em><span class="citation" data-id="9764526"><a href="/opinion/2390269/barr-v-matteo/" aria-description="Citation for case: Barr v. Matteo">360 U. S. 564</a></span> <page-number citation-index="1" label="808">*808</page-number>(1959), to warrant extension to such officials of absolute immunity from suits at common law — we emphasized our expectation that insubstantial suits need not proceed to trial:</p>
<blockquote id="b852-7">“Insubstantial lawsuits can be quickly terminated by federal courts alert to the possibilities of artful pleading. Unless the complaint states a compensable claim for relief... , it should not survive a motion to dismiss. Moreover, the Court recognized in <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>that damages suits concerning constitutional violations need not proceed to trial, but can be terminated on a properly supported motion for summary judgment based on the defense of immunity. ... In responding to such a motion, plaintiffs may not play dog in the manger; and firm application of the Federal Rules of Civil Procedure will ensure that federal officials are not harassed by frivolous lawsuits.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou">438 U. S., at 507-508</a></span> (citations omitted).</blockquote>
<p id="b852-8"><em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>continued to acknowledge that the special functions of some officials might require absolute immunity. But the Court held that “federal officials who seek absolute exemption from personal liability for unconstitutional conduct must bear the burden of showing that public policy requires an exemption of that scope.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou"><em>Id., </em>at 506</a></span>. This we reaffirmed today in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>at 747.</p>
<p id="b852-10">HH HH f-H</p>
<p id="b852-3">A</p>
<p id="b852-4">Petitioners argue that they are entitled to a blanket protection of absolute immunity as an incident of their offices as Presidential aides. In deciding this claim we do not write on an empty page. In <em>Butz </em>v. <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Economou, supra,</a></span> </em>the Secretary of Agriculture — a Cabinet official directly accountable to the President — asserted a defense of absolute official immunity from suit for civil damages. We rejected his claim. In so doing we did not question the power or the importance of the Secretary’s office. Nor did we doubt the importance to the <page-number citation-index="1" label="809">*809</page-number>President of loyal and efficient subordinates in executing his duties of office. Yet we found these factors, alone, to be insufficient to justify absolute immunity. “[T]he greater power of [high] officials,” we reasoned, “affords a greater potential for a regime of lawless conduct.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S., at 506</a></span>. Damages actions against high officials were therefore “an important means of vindicating constitutional guarantees.” <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Ibid.</a></span> </em>Moreover, we concluded that it would be “untenable to draw a distinction for purposes of immunity law between suits brought against state officials under [42 U. S. C.] § 1983 and suits brought directly under the Constitution against federal officials.” <em>Id., </em>at 504.</p>
<p id="b853-5">Having decided in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>that Members of the Cabinet ordinarily enjoy only qualified immunity from suit, we conclude today that it would be equally untenable to hold absolute immunity an incident of the office of every Presidential subordinate based in the White House. Members of the Cabinet are direct subordinates of the President, frequently with greater responsibilities, both to the President and to the Nation, than White House staff. The considerations that supported our decision in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>apply with equal force to this case. It is no disparagement of the offices held by petitioners to hold that Presidential aides, like Members of the Cabinet, generally are entitled only to a qualified immunity.</p>
<p id="b853-6">B</p>
<p id="b853-7">In disputing the controlling authority of <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>, </em>petitioners rely on the principles developed in <em>Gravel </em>v. <em>United States, </em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">408 U. S. 606</a></span> (1972).<footnotemark>12</footnotemark> In <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span> </em>we endorsed the view that “it is literally impossible... for Members of Congress to per<page-number citation-index="1" label="810">*810</page-number>form their legislative tasks without the help of aide's and assistants” and that “the day-to-day work of such aides is so critical to the Members’ performance that they must be treated as the latter’s alter egos . . . <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#616" aria-description="Citation for case: Gravel v. United States"><em>Id., </em>at 616-617</a></span>. Having done so, we held the Speech and Debate Clause derivatively applicable to the “legislative acts” of a Senator’s aide that would have been privileged if performed by the Senator himself. <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#621" aria-description="Citation for case: Gravel v. United States"><em>Id., </em>at 621-622</a></span>.</p>
<p id="b854-5">Petitioners contend that the rationale of <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span> </em>mandates a similar “derivative” immunity for the chief aides of the President of the United States. Emphasizing that the President must delegate a large measure of authority to execute the duties of his office, they argue that recognition of derivative absolute immunity is made essential by all the considerations that support absolute immunity for the President himself.</p>
<p id="b854-6">Petitioners’ argument is not without force. Ultimately, however, it sweeps too far. If the President’s aides are derivatively immune because they are essential to the functioning of the Presidency, so should the Members of the Cabinet — Presidential subordinates some of whose essential roles are acknowledged by the Constitution itself<footnotemark>13</footnotemark> — be absolutely immune. Yet we implicitly rejected such derivative immunity in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>.</em><footnotemark><em>14</em></footnotemark><em> </em>Moreover, in general our cases have followed a “functional” approach to immunity law. We have reeog-<page-number citation-index="1" label="811">*811</page-number>nized that the judicial, prosecutorial, and legislative functions require absolute immunity. But this protection has extended no further than its justification would warrant. In Gravel, for example, we emphasized that Senators and their aides were absolutely immune only when performing “acts legislative in nature,” and not when taking other acts even “in their official capacity.” <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#625" aria-description="Citation for case: Gravel v. United States">408 U. S., at 625</a></span>. See <em>Hutchinson </em>v. <em>Proxmire, </em><span class="citation" data-id="9427661"><a href="/opinion/110131/hutchinson-v-proxmire/#125" aria-description="Citation for case: Hutchinson v. Proxmire">443 U. S. 111, 125-133</a></span> (1979). Our cases involving judges<footnotemark>15</footnotemark> and prosecutors<footnotemark>16</footnotemark> have followed a similar line. The undifferentiated extension of absolute “derivative” immunity to the President’s aides therefore could not be reconciled with the “functional” approach that has characterized the immunity decisions of this Court, indeed including <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span> </em>itself.<footnotemark>17</footnotemark></p>
<p id="b855-5">C</p>
<p id="b855-6">Petitioners also assert an entitlement to immunity based on the “special functions” of White House aides. This form <page-number citation-index="1" label="812">*812</page-number>of argument accords with the analytical approach of our cases. For aides entrusted with discretionary authority in such sensitive areas as national security or foreign policy, absolute immunity might well be justified to protect the unhesitating performance of functions vital to the national interest.<footnotemark>18</footnotemark> But a “special functions” rationale does not warrant a blanket recognition of absolute immunity for all Presidential aides in the performance of all their, duties. This conclusion too follows from our decision in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>, </em>which establishes that an executive official’s claim to absolute immunity must be justified by reference to the public interest in the special functions of his office, not the mere fact of high station.<footnotemark>19</footnotemark></p>
<p id="b856-5"><em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>also identifies the location of the burden of proof. The burden of justifying absolute immunity rests on the official asserting the claim. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S., at 506</a></span>. We have not of course had occasion to identify how a Presidential aide might carry this burden. But the general requisites are familiar in our cases. In order to establish entitlement to absolute im<page-number citation-index="1" label="813">*813</page-number>munity a Presidential aide first must show that the responsibilities of his office embraced a function so sensitive as to require a total shield from liability.<footnotemark>20</footnotemark> He then must demonstrate that he was discharging the protected function when performing the act for which liability is asserted.<footnotemark>21</footnotemark></p>
<p id="b857-10">Applying these standards to the claims advanced by petitioners Harlow and Butterfield, we cannot conclude on the record before us that either has shown that “public policy requires [for any of the functions of his office] an exemption of [absolute] scope.” <em>Butz, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S., at 506</a></span>. Nor, assuming that petitioners did have functions for which absolute immunity would be warranted, could we now conclude that the acts charged in this lawsuit — if taken at all — would lie within the protected area. We do not, however, foreclose the possibility that petitioners, on remand, could satisfy the standards properly applicable to their claims.</p>
<p id="b857-11">
<em>&lt;</em>
</p>
<p id="b857-3">Even if they cannot establish that their official functions require absolute immunity, petitioners assert that public policy at least mandates an application of the qualified immunity standard that would permit the defeat of insubstantial claims without resort to trial. We agree.</p>
<p id="b857-4">A</p>
<p id="b857-5">The resolution of immunity questions inherently requires a balance between the evils inevitable in any available alterna<page-number citation-index="1" label="814">*814</page-number>tive. In situations of abuse of office, an action for damages may offer the only realistic avenue for vindication of constitutional guarantees. <em>Butz </em>v. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou"><em>Economou, supra, </em>at 506</a></span>; see <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#410" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S., at 410</a></span> (“For people in Bivens’ shoes, it is damages or nothing”). It is this recognition that has required the denial of absolute immunity to most public officers. At the same time, however, it cannot be disputed seriously that claims frequently run against the innocent as well as the guilty — at a cost not only to the defendant officials, but to society as a whole.<footnotemark>22</footnotemark> These social costs include the expenses of litigation, the diversion of official energy from pressing public issues, and the deterrence of able citizens from acceptance of public office. Finally, there is the danger that fear of being sued will “dampen the ardor of all but the most resolute, or the most irresponsible [public officials], in the unflinching discharge of their duties.” <em>Gregoire </em>v. <em>Biddle, </em><span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/#581" aria-description="Citation for case: Gregoire v. Biddle">177 F. 2d 579, 581</a></span> (CA2 1949), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./339/949/">339 U. S. 949</a></span> (1950).</p>
<p id="b858-5">In identifying qualified immunity as the best attainable accommodation of competing values, in <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou"><em>Butz, supra, </em>at 507-508</a></span>, as in <em>Scheuer, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#245" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S., at 245-248</a></span>, we relied on the assumption that this standard would permit “[ijnsubstan-tial lawsuits [to] be quickly terminated.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou">438 U. S., at 507-508</a></span>; see <em>Hanrahan </em>v. <em>Hampton, </em><span class="citation" data-id="9427946"><a href="/opinion/110275/hanrahan-v-hampton/#765" aria-description="Citation for case: Hanrahan v. Hampton">446 U. S. 754, 765</a></span> (1980) (Powell, J., concurring in part and dissenting in part).<footnotemark>23</footnotemark> Yet petitioners advance persuasive arguments that the dismissal of insubstantial lawsuits without trial — a factor presupposed in the balance of competing interests struck by <page-number citation-index="1" label="815">*815</page-number>our prior cases — requires an adjustment of the “good faith” standard established by our decisions.</p>
<p id="b859-5">B</p>
<p id="b859-6">Qualified or “good faith” immunity is an affirmative defense that must be pleaded by a defendant official. <em>Gomez </em>v. <em>Toledo, </em><span class="citation multiple-matches"><a href="/c/U.%20S./446/685/">446 U. S. 685</a></span> (1980).<footnotemark>24</footnotemark> Decisions of this Court have established that the “good faith” defense has both an “objective” and a “subjective” aspect. The objective element involves a presumptive knowledge of and respect for “basic, unquestioned constitutional, rights.” <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 322</a></span> (1975). The subjective component refers to “permissible intentions.” <em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">Ibid.</a></span> </em>Characteristically the Court has defined these elements by identifying the circumstances in which qualified immunity would <em>not </em>be available. Referring both to the objective and subjective elements, we have held that qualified immunity would be defeated if an official <em>“knew or reasonably should have known </em>that the action he took within his sphere of official responsibility would violate the constitutional rights of the [plaintiff], or if he took the action <em>with the malicious intention </em>to cause a deprivation of constitutional rights or other injury . . . .” <em>Ibid, </em>(emphasis added).<footnotemark>25</footnotemark></p>
<p id="b859-7">The subjective element of the good-faith defense frequently has proved incompatible with our admonition in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em><page-number citation-index="1" label="816">*816</page-number>that insubstantial claims should not proceed to trial. Rule 56 of the Federal Rules of Civil Procedure provides that disputed questions of fact ordinarily may not be decided on motions for summary judgment.<footnotemark>26</footnotemark> And an official’s subjective good faith has been considered to be a question of fact that some courts have regarded as inherently requiring resolution by a jury.<footnotemark>27</footnotemark></p>
<p id="b860-5">In the context of <em>Buts’ </em>attempted balancing of competing values, it now is clear that substantial costs attend the litigation of the subjective good faith of government officials. Not only are there the general costs of subjecting officials to the risks of trial — distraction of officials from their governmental duties, inhibition of discretionary action, and deterrence of able people from public service. There are special costs to “subjective” inquiries of this kind. Immunity generally is available only to officials performing discretionary functions. In contrast with the thought processes accompanying “ministerial” tasks, the judgments surrounding discretionary action almost inevitably are influenced by the decisionmaker’s experiences, values, and emotions. These variables explain in part why questions of subjective intent so rarely can be decided by summary judgment. Yet they also frame a back<page-number citation-index="1" label="817">*817</page-number>ground in which there often is no clear end to the relevant evidence. Judicial inquiry into subjective motivation therefore may entail broad-ranging discovery and the deposing of numerous persons, including an official’s professional colleagues.<footnotemark>28</footnotemark> Inquiries of this kind can be peculiarly disruptive of effective government.<footnotemark>29</footnotemark></p>
<p id="b861-5">Consistently with the balance at which we aimed in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>, </em>we conclude today that bare allegations of malice should not suffice to subject government officials either to the costs of <page-number citation-index="1" label="818">*818</page-number>trial or to the burdens of broad-reaching discovery. We therefore hold that government officials performing discretionary functions, generally are shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known. See <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#565" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555, 565</a></span> (1978); <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 322</a></span>.<footnotemark>30</footnotemark></p>
<p id="b862-5">Reliance on the objective reasonableness of an official’s conduct, as measured by reference to clearly established law,<footnotemark>31</footnotemark> should avoid excessive disruption of government and permit the resolution of many insubstantial claims on summary judgment. On summary judgment, the judge appropriately may determine, not only the currently applicable law, but whether that law was clearly established at the time an action occurred.<footnotemark>32</footnotemark> If the law at that time was not clearly established, an official could not reasonably be expected to anticipate subsequent legal developments, nor could he fairly be said to “know” that the law forbade conduct not previously identified as unlawful. Until this threshold immunity question is resolved, discovery should not be allowed. If the law was clearly established, the immunity defense ordinarily <page-number citation-index="1" label="819">*819</page-number>should fail, since a reasonably competent public official should know the law governing his conduct. Nevertheless, if the official pleading the defense claims extraordinary circumstances and can prove that he neither knew nor should have known of the relevant legal standard, the defense should be sustained. But again, the defense would turn primarily on objective factors.</p>
<p id="b863-5">By defining the limits of qualified immunity essentially in objective terms, we provide no license to lawless conduct. The public interest in deterrence of unlawful conduct and in compensation of victims remains protected by a test that focuses on the objective legal reasonableness of an official’s acts. Where an official could be expected to know that certain conduct would violate statutory or constitutional rights, he should be made to hesitate; and a person who suffers injury caused by such conduct may have a cause of action.<footnotemark>33</footnotemark> But where an official’s duties legitimately require action in which clearly established rights are not implicated, the public interest may be better served by action taken “with independence and without fear of consequences.” <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 554</a></span> (1967).<footnotemark>34</footnotemark></p>
<p id="b863-6">C</p>
<p id="b863-7">In this case petitioners have asked us to hold that the respondent’s pretrial showings were insufficient to survive their motion for summary judgment.<footnotemark>35</footnotemark> We think it appropri<page-number citation-index="1" label="820">*820</page-number>ate, however, to remand the ease to the District Court for its reconsideration of this issue in light of this opinion.<footnotemark>36</footnotemark> The trial court is more familiar with the record so far developed and also is better situated to make any such further findings as may be necessary.</p>
<p id="b864-5">V</p>
<p id="b864-6">The judgment of the Court of Appeals is vacated, and the case is remanded for further action consistent with this opinion.</p>
<p id="b864-7">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b846-13"> Harlow held this position from the beginning of the Nixon administration on January 20, 1969, through November 4, 1969. On the latter date he was designated as Counselor to the President, a position accorded Cabinet status. He served in that capacity until December 9, 1970, when he returned to private life. Harlow later resumed the duties of Counselor for <page-number citation-index="1" label="803">*803</page-number>the period from July 1,1973, through April 14,1974. Respondent appears to allege that Harlow continued in a conspiracy against him throughout the various changes of official assignment.</p>
</footnote>
<footnote label="2">
<p id="b847-7"> The record reveals that Secretary Seamans called Harlow in May 1969 to inquire about likely congressional reaction to a draft reorganization plan that would cause Fitzgerald’s dismissal. According to Seamans’ testimony, “[w]e [the Air Force] didn’t ask [Harlow] to pass judgment on the action itself. We just asked him what the impact would be in the relationship with the Congress.” App. 153a, 164a-165a (deposition of Robert Sea-mans). Through an aide Harlow responded that “this was a very sensitive item on the Hill and that it would be [his] recommendation that [the Air Force] not proceed to make such a change at that time.” <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Id.,</a></span> </em>at 152a. But the Air Force persisted. Seamans spoke to Harlow on at least one subsequent occasion diming the spring of 1969. The record also establishes that Secretary Seamans called Harlow on November 4,1969, shortly after the public announcement of Fitzgerald’s impending dismissal, and again in December 1969. See <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 186a.</p>
</footnote>
<footnote label="3">
<p id="b847-8"> See <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 284a (transcript of a recorded conversation between Richard Nixon and Ronald Ziegler, February 26,1973). In a conversation with the President on January 31, 1973, John Ehrliehman also recalled that Harlow had discussed the Fitzgerald case with the President. See <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 218a-221a (transcript of recorded conversation between Richard Nixon and John Ehrliehman, January 31,1973). In the same conversation the President himself asserted that he had spoken to Harlow about the Fitzgerald matter, see <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 218a, but the parties continue to dispute whether Mr. Nixon — at the most relevant moments in the discussion — was confusing Fitzgerald’s case with that of another dismissed employee. The President explicitly stated at one point that he previously had been confused. See <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 220a.</p>
</footnote>
<footnote label="4">
<p id="b848-6"> See Defendants Memorandum of Points and Authorities in Support of Their Motion for Summary Judgment in Civ. No. 74-178 (DC), p. 7 (Feb. 12, 1980).</p>
</footnote>
<footnote label="5">
<p id="b848-7"> In support of his version of events Harlow relies particularly on the deposition testimony of Air Force Secretary Seamans, who stated that he regarded abolition of Fitzgerald’s position as necessary “to improve the efficiency” of the Financial Management Office of the Air Force and that he never received any White House instruction regarding the Fitzgerald case. App. 159a-160a. Harlow also disputes the probative value of Richard Nixon’s recorded remark that Harlow had supported Fitzgerald’s firing. Harlow emphasizes the tentativeness of the President’s statement. To the President’s query whether Harlow was “all for canning [Fitzgerald], wasn’t he?”, White House Press Secretary Ronald Ziegler in fact gave a negative reply: “No, I think Bryce may have been the other way.” <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Id.,</a></span> </em>at 284a. The President did not respond to Ziegler’s comment.</p>
</footnote>
<footnote label="6">
<p id="b848-8"> The record establishes that Butterfield worked from an office immediately adjacent to the oval office. He had almost daily contact with the President until March 1973, when he left the White House to become Administrator of the Federal Aviation Administration.</p>
</footnote>
<footnote label="7">
<p id="b848-9"><em> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Id.,</a></span> </em>at 274a. Butterfield reported that this information had been referred to the Federal Bureau of Investigation. In the memorandum Butterfield reported that he had received the information “by word of several mouths, but allegedly from a senior AFL-CIO official originally .... Evidently, Fitzgerald attended a recent meeting of the National Democratic Coalition and, while there, revealed his intentions to a labor representative who, fortunately for us, was unsympathetic.” <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Ibid.</a></span></em></p>
</footnote>
<footnote label="8">
<p id="b849-7"><em> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Id.,</a></span> </em>at 99a-100a, 180a-181a. This memorandum, quoted in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>at 735-736, was not sent to the Defense Department.</p>
</footnote>
<footnote label="9">
<p id="b849-9"> See Memorandum in Support of Summary Judgment, <em>supra, </em>at 26. The history of Fitzgerald’s litigation is recounted in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731. Butterfield was named as a defendant in the initial civil action filed by Fitzgerald in 1974. Harlow was named for the first time in respondent’s second amended complaint of July 5, 1978.</p>
</footnote>
<footnote label="10">
<p id="b849-10"> The first of these statutes, <span class="citation no-link">5 U. S. C. § 7211</span> (1976 ed., Supp. IV), provides generally that “[t]he right of employees . . . to . . . furnish informa<page-number citation-index="1" label="806">*806</page-number>tion to either House of Congress, or to a committee or Member thereof, may not be interfered with or denied.” The second, <span class="citation no-link">18 U. S. C. § 1505</span>, is a criminal statute making it a crime to obstruct congressional testimony. Neither expressly creates a private right to sue for damages. Petitioners argue that the District Court erred in finding that a private cause of action could be inferred under either statute, and that “special factors” present in the context of the federal employer-employee relationship preclude the recognition of respondent’s <em>Bivens </em>action under the First Amendment. The legal sufficiency of respondent’s asserted causes of action is not, however, a question that we view as properly presented for our decision in the present posture of this case. See n. 36,. <em>infra.</em></p>
</footnote>
<footnote label="11">
<p id="b850-5"> As in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731, our jurisdiction has been challenged on the basis that the District Court’s order denying petitioners’ claim of absolute immunity was not an appealable final order and that the Court of Appeals’ dismissal of petitioners’ appeal establishes that this case was never “in” the Court of Appeals within the meaning of <span class="citation no-link">28 U. S. C. § 1254</span>. As the discussion in <em>Nixon </em>establishes our jurisdiction in this case as well, we need not consider those challenges in this opinion.</p>
</footnote>
<footnote label="12">
<p id="b853-8"> Petitioners also claim support from other cases that have followed <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span> </em>in holding that congressional employees are derivatively entitled to the legislative immunity provided to United States Senators and Representatives under the Speech and Debate Clause. See <em>Eastland </em>v. <em>United States Servicemen’s Fund, </em><span class="citation" data-id="9426086"><a href="/opinion/109257/eastland-v-united-states-servicemens-fund/" aria-description="Citation for case: Eastland v. United States Servicemen&#x27;s Fund">421 U. S. 491</a></span> (1975); <em>Doe </em>v. <em>McMillan, </em><span class="citation" data-id="9425326"><a href="/opinion/108802/doe-v-mcmillan/" aria-description="Citation for case: Doe v. McMillan">412 U. S. 306</a></span> (1973).</p>
</footnote>
<footnote label="13">
<p id="b854-7"> See U. S. Const., Art. II, §2 (“The President . . . may require the Opinion, in writing, of the principal Officer in each of the executive Departments, upon any Subject relating to the Duties of their respective Offices . . .”).</p>
</footnote>
<footnote label="14">
<p id="b854-8"> The Chief Justice, <em>post, </em>at 828, argues that senior Presidential aides work “more intimately with the President on a daily basis than does a Cabinet officer,” and that <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>therefore is not controlling. In recent years, however, such men as Henry Kissinger and James Schlesinger have served in both Presidential advisory and Cabinet positions. Kissinger held both posts simultaneously. In our viéw it is impossible to generalize about the role of “offices” in an individual President’s administration without reference to the functions that particular officeholders are assigned by the President. <em>Butz </em>v. <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Economou</a></span> </em>cannot be distinguished on this basis.</p>
</footnote>
<footnote label="15">
<p id="b855-7"> See, <em>e. g., Supreme Court of Virginia </em>v. <em>Consumers Union of United States, </em><span class="citation" data-id="110273"><a href="/opinion/110273/supreme-court-of-virginia-v-consumers-union-of-the-united-states-inc/#731" aria-description="Citation for case: Supreme Court of Virginia v. Consumers Union of the...">446 U. S. 719, 731-737</a></span> (1980); <em>Stump </em>v. <em>Sparkman, </em><span class="citation" data-id="9427113"><a href="/opinion/109820/stump-v-sparkman/#362" aria-description="Citation for case: Stump v. Sparkman">435 U. S. 349, 362</a></span> (1978).</p>
</footnote>
<footnote label="16">
<p id="b855-8"> In <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 430-431</a></span> (1976), this Court reserved the question whether absolute immunity would extend to “those aspects of the prosecutor’s responsibility that cast him in the role of an administrator or investigative officer.” Since that time the Courts of Appeals generally have ruled that prosecutors do not enjoy absolute immunity for acts taken in those capacities. See, <em>e. g., Mancini </em>v. <em>Lester, </em><span class="citation" data-id="382202"><a href="/opinion/382202/dominick-mancini-v-sherwin-lester-and-david-lucas/#992" aria-description="Citation for case: Dominick Mancini v. Sherwin Lester and David Lucas">630 F. 2d 990, 992</a></span> (CA3 1980); <em>Forsyth </em>v. <em>Kleindienst, </em><span class="citation" data-id="8909855"><a href="/opinion/8921097/forsyth-v-kleindienst/#1213" aria-description="Citation for case: Forsyth v. Kleindienst">599 F. 2d 1203, 1213-1214</a></span> (CA3 1979). This Court at least implicitly has drawn the same distinction in extending absolute immunity to executive officials when they are engaged in quasi-prosecutorial functions. See <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#515" aria-description="Citation for case: Butz v. Economou">438 U. S., at 515-517</a></span>.</p>
</footnote>
<footnote label="17">
<p id="b855-9"> Our decision today in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731, in no way abrogates this general rule. As we explained in that opinion, the recognition of absolute immunity for all of a President’s acts in office derives in principal part from factors unique to his constitutional responsibilities and station. Suits against other officials — including Presidential aides — generally do not invoke separation-of-powers considerations to the same extent as suits against the President himself.</p>
</footnote>
<footnote label="18">
<p id="b856-6"> Cf. <em>United States </em>v. <em>Nixon, </em><span class="citation" data-id="109101"><a href="/opinion/109101/united-states-v-nixon/#710" aria-description="Citation for case: United States v. Nixon">418 U. S. 683, 710-711</a></span> (1974) (“[C]ourts have traditionally shown the utmost deference to Presidential responsibilities” for foreign policy and military affairs, and claims of privilege in this area would receive a higher degree of deference than invocations of “a President’s generalized interest in confidentiality”); <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#364" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 364</a></span> (1967) (White, J., concurring) (“We should not require the warrant procedure and the magistrate’s judgment if the President of the United States <em>or his chief legal officer, the Attorney General, </em>has considered the requirements of national security and authorized electronic surveillance as reasonable”) (emphasis added).</p>
</footnote>
<footnote label="19">
<p id="b856-7"> <em>Gravel </em>v. <em>United States, </em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">408 U. S. 606</a></span> (1972), points to a similar conclusion. We fairly may assume that some aides are assigned to act as Presidential “alter egos,” <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#616" aria-description="Citation for case: Gravel v. United States"><em>id., </em>at 616-617</a></span>, in the exercise of functions for which absolute immunity is “essential for the conduct of the public business,” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou"><em>Butz, supra, </em>at 507</a></span>. Cf. <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#620" aria-description="Citation for case: Gravel v. United States"><em>Gravel, supra, </em>at 620</a></span> (derivative immunity extends only to acts within the “central role” of the Speech and Debate Clause in permitting free legislative speech and debate). By analogy to <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span>, </em>a derivative claim to Presidential immunity would be strongest in such “central” Presidential domains as foreign policy and national security, in which the President could not discharge his singularly vital mandate without delegating functions nearly as sensitive as his own.</p>
</footnote>
<footnote label="20">
<p id="b857-6"> Here as elsewhere the relevant judicial inquiries would encompass considerations of public policy, the importance of which should be confirmed either by reference to the common law or, more likely, our constitutional heritage and structure. See <em>Nixon </em>v. <em>Fitzgerald, ante, </em>at 747-748.</p>
</footnote>
<footnote label="21">
<p id="b857-7"> The need for such an inquiry is implicit in <em>Butz </em>v. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#508" aria-description="Citation for case: Butz v. Economou"><em>Economou, supra, </em>at 508-517</a></span>; see <em>Imbler </em>v. <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman"><em>Pachtman, supra, </em>at 430-431</a></span>. Cases involving immunity under the Speech and Debate Clause have inquired explicitly into whether particular acts and activities qualified for the protection of the Clause. See, <em>e. g., Hutchinson </em>v. <em>Proxmire, </em><span class="citation" data-id="9427661"><a href="/opinion/110131/hutchinson-v-proxmire/" aria-description="Citation for case: Hutchinson v. Proxmire">443 U. S. 111</a></span> (1979); <em>Doe </em>v. <em>McMillan, </em><span class="citation" data-id="9425326"><a href="/opinion/108802/doe-v-mcmillan/" aria-description="Citation for case: Doe v. McMillan">412 U. S. 306</a></span> (1973); <em>Gravel </em>v. <em>United States, supra.</em></p>
</footnote>
<footnote label="22">
<p id="b858-6"> See generally Schuck, Suing Our Servants: The Court, Congress, and the Liability of Public Officials for Damages, 1980 S. Ct. Rev. 281,-324-327.</p>
</footnote>
<footnote label="23">
<p id="b858-7"> The importance of this consideration hardly needs emphasis. This Court has noted the risk imposed upon political officials who must defend their actions and motives before a jury. See <em>Lake Country Estates, Inc. </em>v. <em>Tahoe Regional Planning Agency, </em><span class="citation" data-id="9427483"><a href="/opinion/110033/lake-country-estates-inc-v-tahoe-regional-planning-agency/#405" aria-description="Citation for case: Lake Country Estates, Inc. v. Tahoe Regional Planning Agency">440 U. S. 391, 405</a></span> (1979); <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#377" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 377-378</a></span> (1951). As the Court observed in <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Tenney</a></span>: </em>“In times of political passion, dishonest or vindictive motives are readily attributed . . . and as readily believed.” <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#378" aria-description="Citation for case: Tenney v. Brandhove"><em>Id., </em>at 378</a></span>.</p>
</footnote>
<footnote label="24">
<p id="b859-8"><em> </em>Although <em>Gomez </em>presented the question in the context of an action under <span class="citation no-link">42 U. S. C. § 1983</span>, the Court’s analysis indicates that “immunity” must also be pleaded as a defense in actions under the Constitution and laws of the United States. See 446 U. S., at 640. <em>Gomez </em>did not decide which party bore the burden of proof on the issue of good faith. Id., at 642 (Rehnquist, J., concurring).</p>
</footnote>
<footnote label="25">
<p id="b859-9"> In <em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">Wood</a></span> </em>the Court explicitly limited its holding to the circumstances in which a school board member, ’In the specific context of school discipline,” <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 322</a></span>, would be stripped of claimed immunity in an action under § 1983. Subsequent cases, however, have quoted the <em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">Wood</a></span> </em>formulation as a general statement of the qualified immunity standard. See, <em>e. g., Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#562" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555, 562-563, 566</a></span> (1978), quoted in <em>Baker </em>v. <em>McCollan, </em><span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#139" aria-description="Citation for case: Baker v. McCollan">443 U. S. 137, 139</a></span> (1979).</p>
</footnote>
<footnote label="26">
<p id="b860-6"> Rule 56(c) states that summary judgment “shall be rendered forthwith if the pleadings, depositions, answers to interrogatories, and admissions on file, together with the affidavits, if any, show that there is no genuine issue as to any material fact and that the moving party is entitled to a judgment as a matter of law.” In determining whether summary judgment is proper, a court ordinarily must look at the record in the light most favorable to the party opposing the motion, drawing all inferences most favorable to that party. <em>E. g., Poller </em>v. <em>Columbia Broadcasting System, Inc., 368 </em>U. S. 464, 473 (1962).</p>
</footnote>
<footnote label="27">
<p id="b860-7"><em> E. g., Landrum </em>v. <em>Moats, </em><span class="citation" data-id="356040"><a href="/opinion/356040/leslie-landrum-special-administratrix-of-the-estate-of-roy-lee-landrum/#1329" aria-description="Citation for case: Leslie Landrum, Special Administratrix of the Estate of...">576 F. 2d 1320, 1329</a></span> (CA8 1978); <em>Duchesne </em>v. <em>Sugarman, </em><span class="citation" data-id="350998"><a href="/opinion/350998/josephina-duchesne-as-administratrix-of-the-estate-of-pauline-perez-v-jule/#832" aria-description="Citation for case: Josephina Duchesne as Administratrix of the Estate of...">566 F. 2d 817, 832-833</a></span> (CA2 1977); cf. <em>Hutchinson </em>v. <em>Proxmire, </em><span class="citation" data-id="9427661"><a href="/opinion/110131/hutchinson-v-proxmire/#120" aria-description="Citation for case: Hutchinson v. Proxmire">443 U. S., at 120, n. 9</a></span> (questioning whether the existence of “actual malice,” as an issue of fact, may properly be decided on summary judgment in a suit alleging libel of a public figure).</p>
</footnote>
<footnote label="28">
<p id="b861-6"> In suits against a President’s closest aides, discovery of this kind frequently could implicate separation-of-powers concerns. As the Court recognized in <em>United States </em>v. <em>Nixon, </em><span class="citation" data-id="109101"><a href="/opinion/109101/united-states-v-nixon/" aria-description="Citation for case: United States v. Nixon">418 U. S., at 708</a></span>:</p>
<blockquote id="b861-7">“A President and those who assist him must be free to explore alternatives in the process of shaping policies and making decisions and to do so in a way many would be unwilling to express except privately. These are the considerations justifying a presumptive privilege for Presidential communications. The privilege is fundamental to the operation of Government and inextricably rooted in the separation of powers under the Constitution.”</blockquote>
</footnote>
<footnote label="29">
<p id="b861-8"> As Judge Gesell observed in his concurring opinion in <em>Halperin </em>v. <em>Kissinger, </em>196 U. S. App. D. C. 285, 307, <span class="citation" data-id="9842937"><a href="/opinion/370395/morton-halperin-v-henry-kissinger-morton-halperin-v-henry-kissinger/#1214" aria-description="Citation for case: Morton Halperin v. Henry Kissinger Morton Halperin v....">606 F. 2d 1192, 1214</a></span> (1979), aff’d in pertinent part by an equally divided Court, <span class="citation multiple-matches"><a href="/c/U.%20S./452/713/">452 U. S. 713</a></span> (1981):</p>
<blockquote id="b861-9">“We should not close our eyes to the fact that with increasing frequency in this jurisdiction and throughout the country plaintiffs are filing suits seeking damage awards against high government officials in their personal capacities based on alleged constitutional torts. Each such suit almost invariably results in these officials and their colleagues being subjected to extensive discovery into traditionally protected areas, such as their deliberations preparatory to the formulation of government policy and their intimate thought processes and communications at the presidential and cabinet levels. Such discover <em>[sic] </em>is wide-ranging, time-consuming, and not without considerable cost to the officials involved. It is not difficult for ingenious plaintiff’s counsel to create a material issue of fact on some element of the immunity defense where subtle questions of constitutional law and a decisionmaker’s mental processes are involved. A sentence from a casual document or a difference in recollection with regard to a particular policy conversation held long ago would usually, under the normal summary judgment standards, be sufficient [to force a trial]. . . . The effect of this development upon the willingness of individuals to serve their country is obvious.”</blockquote>
</footnote>
<footnote label="30">
<p id="b862-6"> This case involves no issue concerning the elements of the immunity available to state officials sued for constitutional violations under <span class="citation no-link">42 U. S. C. § 1983</span>. We have found previously, however, that it would be “untenable to draw a distinction for purposes of immunity law between suits brought against state officials under § 1983 and suits brought directly under the Constitution against federal officials.” <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#504" aria-description="Citation for case: Butz v. Economou">438 U. S., at 504</a></span>.</p>
<p id="b862-7">Our decision in no way diminishes the absolute immunity currently available to officials whose ftmctions have been held to require a protection of this scope.</p>
</footnote>
<footnote label="31">
<p id="b862-8"> This case involves no claim that Congress has expressed its intent to impose “no fault” tort liability on high federal officials for violations of particular statutes or the Constitution.</p>
</footnote>
<footnote label="32">
<p id="b862-9"> As in <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#565" aria-description="Citation for case: Procunier v. Navarette">434 U. S., at 565</a></span>, we need not define here the circumstances under which “the state of the law” should be “evaluated by reference to the opinions of this Court, of the Courts of Appeals, or of the local District Court.”</p>
</footnote>
<footnote label="33">
<p id="b863-8"> Cf. <em>Procunier </em>v. <span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#565" aria-description="Citation for case: Procunier v. Navarette"><em>Navarette, supra, </em>at 565</a></span>, quoting <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 322</a></span> ("Because they could not reasonably have been expected to be aware of a constitutional right that had not yet been declared, petitioners did not act with such disregard for the established law that their conduct ‘cannot reasonably be characterized as being in good faith”’).</p>
</footnote>
<footnote label="34">
<p id="b863-9"> We emphasize that our decision applies only to suits for civil <em>damages </em>arising from actions within the scope of an official’s duties and in “objective” good faith. We express no view as to the conditions in which injunc-tive or declaratory relief might be available.</p>
</footnote>
<footnote label="35">
<p id="b863-10"> In <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>, </em>we admonished that “insubstantial” suits against high public officials should not be allowed to proceed to trial. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou">438 U. S., at 507</a></span>. See Schuck, <em>supra </em>n. 22, at 324-327. We reiterate this admonition. Insub<page-number citation-index="1" label="820">*820</page-number>stantial lawsuits undermine the effectiveness of government as contemplated by our constitutional structure, and “firm application of the Federal Rules of Civil Procedure” is fully warranted in such cases. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#508" aria-description="Citation for case: Butz v. Economou">438 U. S., at 508</a></span>.</p>
</footnote>
<footnote label="36">
<p id="b864-11"> Petitioners also have urged us, prior to the remand, to rule on the legal sufficiency of respondent’s “implied” causes of action under <span class="citation no-link">5 U. S. C. §7211</span> (1976 ed., Supp. IV) and <span class="citation no-link">18 U. S. C. § 1505</span> and his <em>Bivens </em>claim under the First Amendment. We do not view petitioners’ argument on the statutory question as insubstantial. <em>Cf. Merrill Lynch, Pierce, Fenner &amp; Smith, Inc. </em>v. <em>Curran, </em><span class="citation" data-id="9428751"><a href="/opinion/110701/merrill-lynch-pierce-fenner-smith-inc-v-curran/#377" aria-description="Citation for case: Merrill Lynch, Pierce, Fenner &amp; Smith, Inc. v. Curran">456 U. S. 353, 377-378</a></span> (1982) (controlling question in implication of statutory causes of action is whether Congress affirmatively intended to create a damages remedy); <em>Middlesex County Sewerage Auth. </em>v. <em>National Sea Clammers Assn., </em><span class="citation" data-id="9428452"><a href="/opinion/110546/middlesex-county-sewerage-authority-v-national-sea-clammers-assn/" aria-description="Citation for case: Middlesex County Sewerage Authority v. National Sea...">453 U. S. 1</a></span> (1981) (same); <em>Texas Industries, Inc. </em>v. <em>Radcliff Materials, Inc., 451 U. S. 630, </em>638-639 (1981) (same). Nor is the <em>Bivens </em>question. Cf. <em>Bush v. Lucas, </em><span class="citation" data-id="389983"><a href="/opinion/389983/william-c-bush-v-william-r-lucas/#576" aria-description="Citation for case: William C. Bush v. William R. Lucas">647 F. 2d 573, 576</a></span> (CA5 1981) (holding that the “unique relationship between the Federal Government and its civil service employees is a special consideration which counsels hesitation in inferring a <em>Bivens </em>remedy”). As in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731, however, we took jurisdiction of the case only to resolve the immunity question under the collateral order doctrine. We therefore think it appropriate to leave these questions for fuller consideration by the District Court and, if necessary, by the Court of Appeals.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Harris v. New York.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Harris v. New York"
type: case
citation: "401 U.S. 222 (1971)"
parallel_cite: "91 S. Ct. 643; 28 L. Ed. 2d 1"
neutral_cite: 1971 U.S. LEXIS 75
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-02-24
docket: 206
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Harris v. New York
  varies_by_point: false
  scope_note: "Good law; the Miranda impeachment exception was extended in Oregon v. Hass and (for the Fourth Amendment) tracks Walder/Havens, but does not reach silence (Doyle) or defense witnesses (James v. Illinois)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108272/harris-v-new-york/"
  cluster_id: 108272
  opinion_id: 108272
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Limiting"
  - page: "[[Fruits & Attenuation]]"
    role: "Related (cross-doctrine)"
related: ["[[James v. Illinois]]", "[[United States v. Havens]]", "[[Doyle v. Ohio]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "impeachment", "exclusionary-rule"]
holding: "A statement taken in violation of Miranda, but otherwise voluntary, may be used to impeach the defendant's contrary trial testimony; Miranda's shield may not be turned into a license to commit perjury free from confrontation with prior inconsistent statements."
lake:
  record_id: Harris v. New York
  status: verified
  projected_at: 2026-07-06
---

# Harris v. New York

*401 U.S. 222 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Harris was charged with selling heroin. He had made statements to police that were inadmissible in the prosecution's case-in-chief because adequate [[Miranda and Custodial Interrogation|Miranda warnings]] had not been given. At trial Harris took the stand and gave testimony contradicting those statements. Over objection, the prosecution used the earlier statements on cross-examination to impeach his credibility. There was no claim the statements had been coerced or were involuntary.

## Issue
Whether a statement that is inadmissible in the prosecution's case-in-chief for want of [[Miranda and Custodial Interrogation|Miranda warnings]], but that is otherwise voluntary, may nonetheless be used to impeach the defendant's credibility when he testifies inconsistently at trial.

## Rule
Yes. "Having voluntarily taken the stand, petitioner was under an obligation to speak truthfully and accurately, and the prosecution here did no more than utilize the traditional truth-testing devices of the adversary process." — 401 U.S. at 225. ^pin-225

"The shield provided by *Miranda* cannot be perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances. We hold, therefore, that petitioner's credibility was appropriately impeached by use of his earlier conflicting statements." — *Id.* at 226. ^pin-226

The exception applies only where the statement is otherwise voluntary and trustworthy; a coerced statement could not be used even to impeach.

## Application
Harris's statements were voluntary; their only defect was the [[Miranda and Custodial Interrogation|Miranda warning]] lapse. When he testified to a contrary account, the State could confront him with the prior inconsistent statements to test his credibility before the jury. *[[Miranda v. Arizona|Miranda]]*'s exclusionary protection guards against using such statements as affirmative proof of guilt, but it does not license a defendant to take the stand and testify falsely immune from impeachment.

## Conclusion
The impeachment use of the un-Mirandized but voluntary statements was proper; the conviction was affirmed. This established the **impeachment exception** to *[[Miranda v. Arizona|Miranda]]*'s exclusionary rule.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The exception is bounded: it does not permit impeachment by **post-arrest silence** ([[Doyle v. Ohio]]) and does not extend to **defense witnesses** other than the defendant ([[James v. Illinois]]); the Fourth Amendment analog runs through [[United States v. Havens]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Limiting*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Harris v. New York*, 401 U.S. 222 (1971) — https://www.courtlistener.com/opinion/108272/harris-v-new-york/ — pinpoints: 225, 226.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9d73764907ebbe04", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Harris v. New York"}, "payload": {"all": [{"cite": "401 U.S. 222", "page": "222", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "401"}, {"cite": "91 S. Ct. 643", "page": "643", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "91"}, {"cite": "28 L. Ed. 2d 1", "page": "1", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "28"}, {"cite": "1971 U.S. LEXIS 75", "page": "75", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1971"}], "display": "401 U.S. 222", "official": {"cite": "401 U.S. 222", "page": "222", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "401"}, "official_selection_present": true, "record_id": "Harris v. New York"}}
{"assertion_id": "0ada526c55077e9d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-226", "record_id": "Harris v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-226", "pinpoint_status": "slip-only", "quote": "The shield provided by *Miranda* cannot be perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances. We hold, therefore, that petitioner's credibility was appropriately impeached by use of his earlier conflicting statements.", "quote_fidelity": "mismatch", "record_id": "Harris v. New York", "star_marker": null}}
{"assertion_id": "0ceed0a6a24f0a37", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-225", "record_id": "Harris v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-225", "pinpoint_status": "slip-only", "quote": "--- # Harris v. New York *401 U.S. 222 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Harris was charged with selling heroin. He had made statements to police that were inadmissible in the prosecution's case-in-chief because adequate Miranda warnings had not been given. At trial Harris took the stand and gave testimony contradicting those statements. Over objection, the prosecution used the earlier statements on cross-examination to impeach his credibility. There was no claim the statements had been coerced or were involuntary. ## Issue Whether a statement that is inadmissible in the prosecution's case-in-chief for want of Miranda warnings, but that is otherwise voluntary, may nonetheless be used to impeach the defendant's credibility when he testifies inconsistently at trial. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Harris v. New York", "star_marker": null}}
{"assertion_id": "3a70d6ce2c8d2558", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Harris v. New York"}, "payload": {"as_of_content": "1971-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Harris v. New York", "scope_note": "Good law; the Miranda impeachment exception was extended in Oregon v. Hass and (for the Fourth Amendment) tracks Walder/Havens, but does not reach silence (Doyle) or defense witnesses (James v. Illinois).", "varies_by_point": false}}
```

### lake record — Harris v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Harris v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Harris v. New York",
    "case_name_short": "Harris",
    "case_name_full": "Harris v. New York",
    "input_case_name": "Harris v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-02-24",
    "year": 1971,
    "docket": "206",
    "cluster_id": 108272,
    "lead_opinion_id": 108272,
    "sibling_ids": [
      108272,
      9424454,
      9424455
    ],
    "absolute_url": "/opinion/108272/harris-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "401 U.S. 222",
      "volume": "401",
      "reporter": "U.S.",
      "page": "222",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 643",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 1",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 75",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "75",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "401 U.S. 222",
        "volume": "401",
        "reporter": "U.S.",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 643",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 1",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 75",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "75",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "401 U.S. 222",
    "official_selection": {
      "court_class": "scotus",
      "selected": "401 U.S. 222",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-225",
      "page": null,
      "quote": "--- # Harris v. New York *401 U.S. 222 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Harris was charged with selling heroin. He had made statements to police that were inadmissible in the prosecution's case-in-chief because adequate Miranda warnings had not been given. At trial Harris took the stand and gave testimony contradicting those statements. Over objection, the prosecution used the earlier statements on cross-examination to impeach his credibility. There was no claim the statements had been coerced or were involuntary. ## Issue Whether a statement that is inadmissible in the prosecution's case-in-chief for want of Miranda warnings, but that is otherwise voluntary, may nonetheless be used to impeach the defendant's credibility when he testifies inconsistently at trial. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-226",
      "page": null,
      "quote": "The shield provided by *Miranda* cannot be perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances. We hold, therefore, that petitioner's credibility was appropriately impeached by use of his earlier conflicting statements.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Harris v. New York",
    "varies_by_point": false,
    "scope_note": "Good law; the Miranda impeachment exception was extended in Oregon v. Hass and (for the Fourth Amendment) tracks Walder/Havens, but does not reach silence (Doyle) or defense witnesses (James v. Illinois).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Hopson",
          "cluster_id": 4405826,
          "cite": [
            "219 Cal. Rptr. 3d 717",
            "396 P.3d 1054",
            "3 Cal. 5th 424",
            "2017 WL 2837126",
            "2017 Cal. LEXIS 4894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Richared E. Ladue",
          "cluster_id": 4489460,
          "cite": [
            "168 A.3d 430",
            "2017 VT 20",
            "2017 Vt. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
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
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Broom a/k/a Patrick Brown v. United States",
          "cluster_id": 2809687,
          "cite": [
            "118 A.3d 207",
            "2015 D.C. App. LEXIS 265",
            "2015 WL 3768885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt. v. Molina, M.",
          "cluster_id": 2753817,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Curtis Tyrell Cutler v. State of Indiana",
          "cluster_id": 2727954,
          "cite": [
            "983 N.E.2d 217",
            "2013 WL 633050",
            "2013 Ind. App. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Reid",
          "cluster_id": 5641509,
          "cite": [
            "19 N.Y.3d 382",
            "971 N.E.2d 353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen Murdock",
          "cluster_id": 622650,
          "cite": [
            "399 U.S. App. D.C. 153",
            "667 F.3d 1302",
            "2012 WL 414459",
            "2012 U.S. App. LEXIS 2599"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McCollum",
          "cluster_id": 6589541,
          "cite": [
            "79 Mass. App. Ct. 239",
            "945 N.E.2d 937",
            "2011 Mass. App. LEXIS 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Garvin",
          "cluster_id": 6580150,
          "cite": [
            "456 Mass. 778",
            "926 N.E.2d 169",
            "2010 Mass. LEXIS 216"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Simon",
          "cluster_id": 2483876,
          "cite": [
            "456 Mass. 280",
            "923 N.E.2d 58",
            "2010 Mass. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lawrence Samuel Jr. v. State",
          "cluster_id": 3130658,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane1_negative"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Faretta v. California",
          "cluster_id": 109309,
          "cite": [
            "45 L. Ed. 2d 562",
            "95 S. Ct. 2525",
            "422 U.S. 806",
            "1975 U.S. LEXIS 83"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Sykes",
          "cluster_id": 109717,
          "cite": [
            "53 L. Ed. 2d 594",
            "97 S. Ct. 2497",
            "433 U.S. 72",
            "1977 U.S. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mateo",
          "cluster_id": 2006639,
          "cite": [
            "811 N.E.2d 1053",
            "2 N.Y.3d 383",
            "779 N.Y.S.2d 399",
            "2 N.Y. 383",
            "2004 N.Y. LEXIS 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doyle v. Ohio",
          "cluster_id": 109491,
          "cite": [
            "49 L. Ed. 2d 91",
            "96 S. Ct. 2240",
            "426 U.S. 610",
            "1976 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Elstad",
          "cluster_id": 111364,
          "cite": [
            "84 L. Ed. 2d 222",
            "105 S. Ct. 1285",
            "470 U.S. 298",
            "1985 U.S. LEXIS 60",
            "53 U.S.L.W. 4244"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stansbury v. California",
          "cluster_id": 117843,
          "cite": [
            "128 L. Ed. 2d 293",
            "114 S. Ct. 1526",
            "511 U.S. 318",
            "1994 U.S. LEXIS 3293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rock v. Arkansas",
          "cluster_id": 111933,
          "cite": [
            "97 L. Ed. 2d 37",
            "107 S. Ct. 2704",
            "483 U.S. 44",
            "1987 U.S. LEXIS 2732",
            "55 U.S.L.W. 4925",
            "22 Fed. R. Serv. 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKaskle v. Wiggins",
          "cluster_id": 111095,
          "cite": [
            "79 L. Ed. 2d 122",
            "104 S. Ct. 944",
            "465 U.S. 168",
            "1984 U.S. LEXIS 24",
            "52 U.S.L.W. 4176"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Michael C.",
          "cluster_id": 110117,
          "cite": [
            "61 L. Ed. 2d 197",
            "99 S. Ct. 2560",
            "442 U.S. 707",
            "1979 U.S. LEXIS 133"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. State",
          "cluster_id": 1685186,
          "cite": [
            "163 S.W.3d 734",
            "2005 Tex. Crim. App. LEXIS 741",
            "2005 WL 1162528"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
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
        "journal_ref": "Harris v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108272 OR 9424454 OR 9424455) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjU3OTg0MDAwMDAwJnM9MjQyMTg2NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108272+OR+9424454+OR+9424455%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108272 OR 9424454 OR 9424455)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02ODYmcz0yMzU1MzQ0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108272+OR+9424454+OR+9424455%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108272 OR 9424454 OR 9424455)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 0,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108272 OR 9424454 OR 9424455)",
    "indexed_citing_opinions": 1928,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108272,
        "count": 1795,
        "count_source": "search"
      },
      {
        "opinion_id": 9424454,
        "count": 185,
        "count_source": "search"
      },
      {
        "opinion_id": 9424455,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2903,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/harris-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MDg0NTgmcz05NDgzMTAzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108272+OR+9424454+OR+9424455%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108272,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 107651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 108002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 260072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 277194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 279491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 280065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 282229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 282758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1173777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1246844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1290054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1433274,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1492401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1628518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1750859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1774823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1779353,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1885369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 1960473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 2017386,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 2029356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 2611284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108272,
        "cited_id": 2612058,
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
    "date_created": "2026-07-05T06:21:45Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:22:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:22:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:27:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:22:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Harris v. New York

```
<div>
<center><b><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U.S. 222</a></span> (1971)</b></center>
<center><h1>HARRIS<br>
v.<br>
NEW YORK.</h1></center>
<center>No. 206.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 17, 1970</center>
<center>Decided February 24, 1971</center>
CERTIORARI TO THE COURT OF APPEALS OF NEW YORK.
<p><i>Joel Martin Aurnou</i> argued the cause and filed a brief for petitioner.</p>
<p><i>James J. Duggan</i> argued the cause for respondent. With him on the brief was <i>Carl A. Vergari.</i></p>
<p><i>Sybil H. Landau</i> argued the cause for the District Attorney of New York County as <i>amicus curiae</i> urging affirmance. With her on the brief were <i>Frank S. Hogan, pro se,</i> and <i>Michael R. Juviler.</i></p>
<p>MR. CHIEF JUSTICE BURGER delivered the opinion of the Court.</p>
<p>We granted the writ in this case to consider petitioner's claim that a statement made by him to police under circumstances rendering it inadmissible to establish the prosecution's case in chief under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), may not be used to impeach his credibility.</p>
<p>The State of New York charged petitioner in a two-count indictment with twice selling heroin to an undercover <span class="star-pagination">*223</span> police officer. At a subsequent jury trial the officer was the State's chief witness, and he testified as to details of the two sales. A second officer verified collateral details of the sales, and a third offered testimony about the chemical analysis of the heroin.</p>
<p>Petitioner took the stand in his own defense. He admitted knowing the undercover police officer but denied a sale on January 4, 1966. He admitted making a sale of contents of a glassine bag to the officer on January 6 but claimed it was baking powder and part of a scheme to defraud the purchaser.</p>
<p>On cross-examination petitioner was asked seriatim whether he had made specified statements to the police immediately following his arrest on January 7statements that partially contradicted petitioner's direct testimony at trial. In response to the cross-examination, petitioner testified that he could not remember virtually any of the questions or answers recited by the prosecutor. At the request of petitioner's counsel the written statement from which the prosecutor had read questions and answers in his impeaching process was placed in the record for possible use on appeal; the statement was not shown to the jury.</p>
<p>The trial judge instructed the jury that the statements attributed to petitioner by the prosecution could be considered only in passing on petitioner's credibility and not as evidence of guilt. In closing summations both counsel argued the substance of the impeaching statements. The jury then found petitioner guilty on the second count of the indictment.<sup>[1]</sup> The New York Court of Appeals affirmed in a <i>per curiam</i> opinion, 25 N. Y. 2d 175, <span class="citation" data-id="5525131"><a href="/opinion/5677292/people-v-harris/" aria-description="Citation for case: People v. Harris">250 N. E. 2d 349</a></span> (1969).</p>
<p>At trial the prosecution made no effort in its case in chief to use the statements allegedly made by petitioner, <span class="star-pagination">*224</span> conceding that they were inadmissible under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The transcript of the interrogation used in the impeachment, but not given to the jury, shows that no warning of a right to appointed counsel was given before questions were put to petitioner when he was taken into custody. Petitioner makes no claim that the statements made to the police were coerced or involuntary.</p>
<p>Some comments in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion can indeed be read as indicating a bar to use of an uncounseled statement for any purpose, but discussion of that issue was not at all necessary to the Court's holding and cannot be regarded as controlling. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> barred the prosecution from making its case with statements of an accused made while in custody prior to having or effectively waiving counsel. It does not follow from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> that evidence inadmissible against an accused in the prosecution's case in chief is barred for all purposes, provided of course that the trustworthiness of the evidence satisfies legal standards.</p>
<p>In <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), the Court permitted physical evidence, inadmissible in the case in chief, to be used for impeachment purposes.</p>
<blockquote>"It is one thing to say that the Government cannot make an affirmative use of evidence unlawfully obtained. It is quite another to say that the defendant can turn the illegal method by which evidence in the Government's possession was obtained to his own advantage, and provide himself with a shield against contradiction of his untruths. Such an extension of the <i>Weeks</i> doctrine would be a perversion of the Fourth Amendment.</blockquote>
<blockquote>"[T]here is hardly justification for letting the defendant affirmatively resort to perjurious testimony in reliance on the Government's disability to challenge his credibility." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S., at 65</a></span>.</blockquote>
<p><span class="star-pagination">*225</span> It is true that Walder was impeached as to collateral matters included in his direct examination, whereas petitioner here was impeached as to testimony bearing more directly on the crimes charged. We are not persuaded that there is a difference in principle that warrants a result different from that reached by the Court in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span>.</i> Petitioner's testimony in his own behalf concerning the events of January 7 contrasted sharply with what he told the police shortly after his arrest. The impeachment process here undoubtedly provided valuable aid to the jury in assessing petitioner's credibility, and the benefits of this process should not be lost, in our view, because of the speculative possibility that impermissible police conduct will be encouraged thereby. Assuming that the exclusionary rule has a deterrent effect on proscribed police conduct, sufficient deterrence flows when the evidence in question is made unavailable to the prosecution in its case in chief.</p>
<p>Every criminal defendant is privileged to testify in his own defense, or to refuse to do so. But that privilege cannot be construed to include the right to commit perjury. See <i>United States</i> v. <i>Knox,</i> <span class="citation" data-id="9841978"><a href="/opinion/108002/united-states-v-knox/" aria-description="Citation for case: United States v. Knox">396 U. S. 77</a></span> (1969); cf. <i>Dennis</i> v. <i>United States,</i> <span class="citation" data-id="9423265"><a href="/opinion/107265/dennis-v-united-states/" aria-description="Citation for case: Dennis v. United States">384 U. S. 855</a></span> (1966). Having voluntarily taken the stand, petitioner was under an obligation to speak truthfully and accurately, and the prosecution here did no more than utilize the traditional truth-testing devices of the adversary process.<sup>[2]</sup> Had <span class="star-pagination">*226</span> inconsistent statements been made by the accused to some third person, it could hardly be contended that the conflict could not be laid before the jury by way of cross-examination and impeachment.</p>
<p>The shield provided by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cannot be perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances. We hold, therefore, that petitioner's credibility was appropriately impeached by use of his earlier conflicting statements.</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BLACK dissents.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>It is conceded that the question-and-answer statement used to impeach petitioner's direct testimony was, under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), constitutionally inadmissible as part of the State's direct case against petitioner. I think that the Constitution also denied the State the use of the statement on cross-examination to impeach the credibility of petitioner's testimony given in his own defense. The decision in <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), is not, as the Court today holds, dispositive to the contrary. Rather, that case supports my conclusion.</p>
<p>The State's case against Harris depended upon the jury's belief of the testimony of the undercover agent that petitioner "sold" the officer heroin on January 4 and again on January 6. Petitioner took the stand and flatly denied having sold anything to the officer on January 4. He countered the officer's testimony as to the January 6 sale with testimony that he had sold the officer two glassine bags containing what appeared to be heroin, but that actually the bags contained only baking powder intended to deceive the officer in order to obtain $12. <span class="star-pagination">*227</span> The statement contradicted petitioner's direct testimony as to the events of both days. The statement's version of the events on January 4 was that the officer had used petitioner as a middleman to buy some heroin from a third person with money furnished by the officer. The version of the events on January 6 was that petitioner had again acted for the officer in buying two bags of heroin from a third person for which petitioner received $12 and a part of the heroin. Thus, it is clear that the statement was used to impeach petitioner's direct testimony not on collateral matters but on matters directly related to the crimes for which he was on trial.<sup>[1]</sup></p>
<p><i>Walder</i> v. <i>United States</i> was not a case where tainted evidence was used to impeach an accused's direct testimony on matters directly related to the case against him. In <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> the evidence was used to impeach the accused's testimony on matters <i>collateral</i> to the crime charged. Walder had been indicted in 1950 for purchasing and possessing heroin. When his motion to suppress use of the narcotics as illegally seized was granted, the Government dismissed the prosecution. Two years later Walder was indicted for another narcotics violation completely unrelated to the 1950 one. Testifying in his own defense, he said on direct examination that he had never in his life possessed narcotics. On cross-examination he denied that law enforcement officers had seized narcotics from his home two years earlier. The Government was then permitted to introduce the testimony of one of the officers involved in the 1950 seizure, that when he had raided Walder's home at that time he had seized narcotics there. <span class="star-pagination">*228</span> The Court held that on facts where "the defendant went beyond a mere denial of complicity in the crimes of which he was charged and made the sweeping claim that he had never dealt in or possessed any narcotics," <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S., at 65</a></span>, the exclusionary rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), would not extend to bar the Government from rebutting this testimony with evidence, although tainted, that petitioner had in fact possessed narcotics two years before. The Court was careful, however, to distinguish the situation of an accused whose testimony, as in the instant case, was a "denial of complicity in the crimes of which he was charged," that is, where illegally obtained evidence was used to impeach the accused's direct testimony on matters directly related to the case against him. As to that situation, the Court said:</p>
<blockquote>"Of course, the Constitution guarantees a defendant the fullest opportunity to meet the accusation against him. He must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it, and therefore not available for its case in chief." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S., at 65</a></span>.</blockquote>
<p>From this recital of facts it is clear that the evidence used for impeachment in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> was related to the earlier 1950 prosecution and had no direct bearing on "the elements of the case" being tried in 1952. The evidence tended solely to impeach the credibility of the defendant's direct testimony that he had never in his life possessed heroin. But that evidence was completely unrelated to the indictment on trial and did not in any way interfere with his freedom to deny all elements of that case against him. In contrast, here, the evidence used for impeachment, a statement concerning the details of the very sales alleged in the indictment, was directly related to the case against petitioner.</p>
<p><span class="star-pagination">*229</span> While <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> did not identify the constitutional specifics that guarantee "a defendant the fullest opportunity to meet the accusation against him . . . [and permit him to] be free to deny all the elements of the case against him," in my view <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), identified the Fifth Amendment's privilege against self-incrimination as one of those specifics.<sup>[2]</sup><span class="star-pagination">*230</span> That privilege has been extended against the States. <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964). It is fulfilled only when an accused is guaranteed the right "to remain silent unless he chooses to speak in the <i>unfettered</i> exercise of his own will," <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan"><i>id.,</i> at 8</a></span> (emphasis added). The choice of whether to testify in one's own defense must therefore be "unfettered," since that choice is an exercise of the constitutional privilege, <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965). <i><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span></i> held that comment by the prosecution upon the accused's failure to take the stand or a court instruction that such silence is evidence of guilt is impermissible because it "fetters" that choice"[i]t cuts down on the privilege by making its assertion costly." <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/#614" aria-description="Citation for case: Griffin v. California"><i>Id.,</i> at 614</a></span>. For precisely the same reason the constitutional guarantee forbids the prosecution to use a tainted statement to impeach the accused who takes the stand: The prosecution's use of the tainted statement "cuts down on the privilege by making its assertion costly." <i><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Ibid.</a></span></i> Thus, the accused is denied an "unfettered" choice when the decision whether to take the stand is burdened by the risk that an illegally obtained prior statement may be introduced to impeach his direct testimony denying complicity in the crime charged against him.<sup>[3]</sup> We settled this proposition in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> where we said:</p>
<blockquote>"The privilege against self-incrimination protects the individual from being compelled to incriminate himself in <i>any</i> manner . . . . [S]tatements merely intended to be exculpatory by the defendant are often <i>used to impeach his testimony at trial</i> . . . . <i>These statements are incriminating in any meaningful sense of the word and may not be used without the full warnings and effective waiver required for</i> <span class="star-pagination">*231</span> <i>any other statement.</i>" 384 U. S., at 476-477 (emphasis added).</blockquote>
<p>This language completely disposes of any distinction between statements used on direct as opposed to cross-examination.<sup>[4]</sup> "An incriminating statement is as incriminating when used to impeach credibility as it is when used as direct proof of guilt and no constitutional distinction can legitimately be drawn." <i>People</i> v. <i>Kulis,</i> 18 N. Y. 2d 318, 324, <span class="citation" data-id="5522978"><a href="/opinion/5675346/people-v-kulis/#543" aria-description="Citation for case: People v. Kulis">221 N. E. 2d 541, 543</a></span> (1966) (dissenting opinion).</p>
<p>The objective of deterring improper police conduct is only part of the larger objective of safeguarding the integrity of our adversary system. The "essential mainstay" of that system, <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 460</a></span>, is the privilege against self-incrimination, which for <span class="star-pagination">*232</span> that reason has occupied a central place in our jurisprudence since before the Nation's birth. Moreover, "we may view the historical development of the privilege as one which groped for the proper scope of governmental power over the citizen. . . . All these policies point to one overriding thought: the constitutional foundation underlying the privilege is the respect a government . . . must accord to the dignity and integrity of its citizens." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> These values are plainly jeopardized if an exception against admission of tainted statements is made for those used for impeachment purposes. Moreover, it is monstrous that courts should aid or abet the law-breaking police officer. It is abiding truth that "[n]othing can destroy a government more quickly than its failure to observe its own laws, or worse, its disregard of the charter of its own existence." <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#659" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 659</a></span> (1961). Thus, even to the extent that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was aimed at deterring police practices in disregard of the Constitution, I fear that today's holding will seriously undermine the achievement of that objective. The Court today tells the police that they may freely interrogate an accused incommunicado and without counsel and know that although any statement they obtain in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cannot be used on the State's direct case, it may be introduced if the defendant has the temerity to testify in his own defense. This goes far toward undoing much of the progress made in conforming police methods to the Constitution. I dissent.</p>
<h2>NOTES</h2>
<p>[1]  No agreement was reached as to the first count. That count was later dropped by the State.</p>
<p>[2]  If, for example, an accused confessed fully to a homicide and led the police to the body of the victim under circumstances making his confession inadmissible, the petitioner would have us allow that accused to take the stand and blandly deny every fact disclosed to the police or discovered as a "fruit" of his confession, free from confrontation with his prior statements and acts. The voluntariness of the confession would, on this thesis, be totally irrelevant. We reject such an extravagant extension of the Constitution. Compare <i>Killough</i> v. <i>United States,</i> 114 U. S. App. D. C. 305, <span class="citation" data-id="9449118"><a href="/opinion/260072/james-w-killough-v-united-states/" aria-description="Citation for case: James W. Killough v. United States">315 F. 2d 241</a></span> (1962).</p>
<p>[1]  The trial transcript shows that petitioner testified that he remembered making a statement on January 7; that he remembered a few of the questions and answers; but that he did not "remember giving too many answers." When asked about his bad memory, petitioner, who had testified that he was a heroin addict, stated that "my joints was down and I needed drugs."</p>
<p>[2]  Three of the five judges of the Appellate Division in this case agreed that the State's use of petitioner's illegally obtained statement was an error of constitutional dimension. <i>People</i> v. <i>Harris,</i> 31 App. Div. 2d 828, 298 N. Y. S. 2d 245 (1969). However, one of the three held that the error did not play a meaningful role in the case and was therefore harmless under our decision in <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). He therefore joined in affirming the conviction with the two judges who were of the view that there was no constitutional question involved. 31 App. Div. 2d, at 830, 298 N. Y. S. 2d, at 249. I disagree that the error was harmless and subscribe to the reasoning of the dissenting judges, <i>id.,</i> at 831-832, 298 N. Y. S. 2d at 250:
</p>
<p>"Under the circumstances outlined above, I cannot agree that this error of constitutional dimension was `harmless beyond a reasonable doubt' (<i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 24</a></span>). An error is not harmless if `there is a reasonable possibility that the evidence complained of might have contributed to the conviction' (<i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/#86" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85, 86-87</a></span>). The burden of showing that a constitutional error is harmless rests with the People who, in this case, have not even attempted to assume that demonstration (<i>Chapman</i> v. <i>California, supra</i>). Surely it cannot be said with any certainty that the improper use of defendant's statement did not tip the scales against him, especially when his conviction rests on the testimony of the same undercover agent whose testimony was apparently less than convincing on the January 4 charge (cf. <i>Anderson</i> v. <i>Nelson,</i> <span class="citation" data-id="107651"><a href="/opinion/107651/anderson-v-nelson/#525" aria-description="Citation for case: Anderson v. Nelson">390 U. S. 523, 525</a></span>). On the contrary, it is difficult to see how defendant could not have been damaged severely by use of the inconsistent statement in a case which, in the final analysis, pitted his word against the officer's. The judgment should be reversed and a new trial granted."</p>
<p>The Court of Appeals affirmed <i>per curiam</i> on the authority of its earlier opinion in <i>People</i> v. <i>Kulis,</i> 18 N. Y. 2d 318, <span class="citation" data-id="5522978"><a href="/opinion/5675346/people-v-kulis/" aria-description="Citation for case: People v. Kulis">221 N. E. 2d 541</a></span> (1966). Chief Judge Fuld and Judge Keating dissented in <i><span class="citation" data-id="5522978"><a href="/opinion/5675346/people-v-kulis/" aria-description="Citation for case: People v. Kulis">Kulis</a></span></i> on the ground that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> precluded use of the statement for impeachment purposes, 18 N. Y. 2d, at 323, <span class="citation" data-id="5522978"><a href="/opinion/5675346/people-v-kulis/#542" aria-description="Citation for case: People v. Kulis">221 N. E. 2d, at 542</a></span>.</p>
<p>[3]  It is therefore unnecessary for me to consider petitioner's argument that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> has overruled the narrow exception of <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> admitting impeaching evidence on collateral matters.</p>
<p>[4]  Six federal courts of appeals and appellate courts of 14 States have reached the same result. <i>United States</i> v. <i>Fox,</i> <span class="citation" data-id="9454030"><a href="/opinion/282229/united-states-v-jack-solomon-fox-and-samuel-norber/" aria-description="Citation for case: United States v. Jack Solomon Fox and Samuel Norber">403 F. 2d 97</a></span> (CA2 1968); <i>United States</i> v. <i>Pinto,</i> <span class="citation" data-id="280065"><a href="/opinion/280065/united-states-of-america-ex-rel-james-edward-hill-v-warren-pinto/" aria-description="Citation for case: United States of America Ex Rel. James Edward Hill v....">394 F. 2d 470</a></span> (CA3 1968); <i>Breedlove</i> v. <i>Beto,</i> <span class="citation" data-id="282758"><a href="/opinion/282758/freddie-breedlove-v-dr-george-j-beto-director-texas-department-of/" aria-description="Citation for case: Freddie Breedlove v. Dr. George J. Beto, Director, Texas...">404 F. 2d 1019</a></span> (CA5 1968); <i>Groshart</i> v. <i>United States,</i> <span class="citation" data-id="9453474"><a href="/opinion/279491/jerry-warren-groshart-v-united-states/" aria-description="Citation for case: Jerry Warren Groshart v. United States">392 F. 2d 172</a></span> (CA9 1968); <i>Blair</i> v. <i>United States,</i> 130 U. S. App. D. C. 322, <span class="citation multiple-matches"><a href="/c/F.%202d/401/387/">401 F. 2d 387</a></span> (1968); <i>Wheeler</i> v. <i>United States,</i> <span class="citation" data-id="277194"><a href="/opinion/277194/billy-wayne-wheeler-and-johnnie-green-jr-v-united-states/" aria-description="Citation for case: Billy Wayne Wheeler and Johnnie Green, Jr. v. United States">382 F. 2d 998</a></span> (CA10 1967); <i>People</i> v. <i>Barry,</i> <span class="citation" data-id="2191430"><a href="/opinion/2191430/people-v-barry/" aria-description="Citation for case: People v. Barry">237 Cal. App. 2d 154</a></span>, <span class="citation" data-id="2191430"><a href="/opinion/2191430/people-v-barry/" aria-description="Citation for case: People v. Barry">46 Cal. Rptr. 727</a></span> (1965), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./386/1024/">386 U. S. 1024</a></span> (1967); <i>Velarde</i> v. <i>People,</i> <span class="citation" data-id="1173777"><a href="/opinion/1173777/velarde-v-people/" aria-description="Citation for case: Velarde v. People">171 Colo. 261</a></span>, <span class="citation" data-id="1173777"><a href="/opinion/1173777/velarde-v-people/" aria-description="Citation for case: Velarde v. People">466 P. 2d 919</a></span> (1970); <i>State</i> v. <i>Galasso,</i> <span class="citation" data-id="1628518"><a href="/opinion/1628518/state-v-galasso/" aria-description="Citation for case: State v. Galasso">217 So. 2d 326</a></span> (Fla. 1968); <i>People</i> v. <i>Luna,</i> <span class="citation" data-id="2029356"><a href="/opinion/2029356/the-people-v-luna/" aria-description="Citation for case: The PEOPLE v. Luna">37 Ill. 2d 299</a></span>, <span class="citation" data-id="2029356"><a href="/opinion/2029356/the-people-v-luna/" aria-description="Citation for case: The PEOPLE v. Luna">226 N. E. 2d 586</a></span> (1967); <i>Franklin</i> v. <i>State,</i> <span class="citation" data-id="1492401"><a href="/opinion/1492401/franklin-v-state/" aria-description="Citation for case: Franklin v. State">6 Md. App. 572</a></span>, <span class="citation" data-id="1492401"><a href="/opinion/1492401/franklin-v-state/" aria-description="Citation for case: Franklin v. State">252 A. 2d 487</a></span> (1969); <i>People</i> v. <i>Wilson,</i> <span class="citation" data-id="2017386"><a href="/opinion/2017386/people-v-wilson/" aria-description="Citation for case: People v. Wilson">20 Mich. App. 410</a></span>, <span class="citation" data-id="2017386"><a href="/opinion/2017386/people-v-wilson/" aria-description="Citation for case: People v. Wilson">174 N. W. 2d 79</a></span> (1969); <i>State</i> v. <i>Turnbow,</i> 67 N. M. 241, <span class="citation" data-id="2611284"><a href="/opinion/2611284/state-v-turnbow/" aria-description="Citation for case: State v. Turnbow">354 P. 2d 533</a></span> (1960); <i>State</i> v. <i>Catrett,</i> <span class="citation" data-id="6701707"><a href="/opinion/6814852/state-v-riera/" aria-description="Citation for case: State v. Riera">276 N. C. 86</a></span>, <span class="citation" data-id="1290054"><a href="/opinion/1290054/state-v-catrett/" aria-description="Citation for case: State v. Catrett">171 S. E. 2d 398</a></span> (1970); <i>State</i> v. <i>Brewton,</i> <span class="citation" data-id="9628725"><a href="/opinion/1433274/state-v-brewton/" aria-description="Citation for case: State v. Brewton">247 Ore. 241</a></span>, <span class="citation" data-id="9628725"><a href="/opinion/1433274/state-v-brewton/" aria-description="Citation for case: State v. Brewton">422 P. 2d 581</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./387/943/">387 U. S. 943</a></span> (1967); <i>Commonwealth</i> v. <i>Padgett,</i> <span class="citation" data-id="1885369"><a href="/opinion/1885369/commonwealth-v-padgett/" aria-description="Citation for case: Commonwealth v. Padgett">428 Pa. 229</a></span>, <span class="citation" data-id="1885369"><a href="/opinion/1885369/commonwealth-v-padgett/" aria-description="Citation for case: Commonwealth v. Padgett">237 A. 2d 209</a></span> (1968); <i>Spann</i> v. <i>State,</i> <span class="citation" data-id="1779353"><a href="/opinion/1779353/spann-v-state/" aria-description="Citation for case: Spann v. State">448 S. W. 2d 128</a></span> (Tex. Cr. App. 1969); <i>Cardwell</i> v. <i>Commonwealth,</i> <span class="citation" data-id="9845193"><a href="/opinion/1246844/cardwell-v-commonwealth/" aria-description="Citation for case: Cardwell v. Commonwealth">209 Va. 412</a></span>, <span class="citation" data-id="9845193"><a href="/opinion/1246844/cardwell-v-commonwealth/" aria-description="Citation for case: Cardwell v. Commonwealth">164 S. E. 2d 699</a></span> (1968); <i>Gaertner</i> v. <i>State,</i> <span class="citation" data-id="1750859"><a href="/opinion/1750859/gaertner-v-state/" aria-description="Citation for case: Gaertner v. State">35 Wis. 2d 159</a></span>, <span class="citation" data-id="1750859"><a href="/opinion/1750859/gaertner-v-state/" aria-description="Citation for case: Gaertner v. State">150 N. W. 2d 370</a></span> (1967); see also <i>Kelly</i> v. <i>King,</i> <span class="citation" data-id="1774823"><a href="/opinion/1774823/kelly-v-king/" aria-description="Citation for case: Kelly v. King">196 So. 2d 525</a></span> (Miss. 1967). Only three state appellate courts have agreed with New York. <i>State</i> v. <i>Kimbrough,</i> 109 N. J. Super. 57, <span class="citation" data-id="1960473"><a href="/opinion/1960473/state-v-kimbrough/" aria-description="Citation for case: State v. Kimbrough">262 A. 2d 232</a></span> (1970); <i>State</i> v. <i>Butler,</i> <span class="citation" data-id="6754227"><a href="/opinion/6864451/state-v-butler/" aria-description="Citation for case: State v. Butler">19 Ohio St. 2d 55</a></span>, <span class="citation" data-id="6754227"><a href="/opinion/6864451/state-v-butler/" aria-description="Citation for case: State v. Butler">249 N. E. 2d 818</a></span> (1969); <i>State</i> v. <i>Grant,</i> <span class="citation" data-id="2612058"><a href="/opinion/2612058/state-v-grant/" aria-description="Citation for case: State v. Grant">77 Wash. 2d 47</a></span>, <span class="citation" data-id="2612058"><a href="/opinion/2612058/state-v-grant/" aria-description="Citation for case: State v. Grant">459 P. 2d 639</a></span> (1969).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Harris v. United States (1968).json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Harris v. United States (1968)"
type: case
citation: "390 U.S. 234 (1968)"
parallel_cite: "88 S. Ct. 992; 19 L. Ed. 2d 1067"
neutral_cite: 1968 U.S. LEXIS 2283
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-03-05
docket: 92
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-03-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Harris v. United States (1968)"
  varies_by_point: false
  scope_note: "Per curiam. The plain-view-seizure formulation remains settled law; it was later structured (no-inadvertence requirement) by Horton v. California. Distinct case from the 1947 Harris v. United States (search incident to arrest), which Chimel v. California overruled."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107625/harris-v-united-states/"
  cluster_id: 107625
  opinion_id: 107625
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Coolidge v. New Hampshire]]", "[[Horton v. California]]", "[[Texas v. Brown]]", "[[South Dakota v. Opperman]]", "[[Cooper v. California]]"]
aliases: ["Harris v. United States"]
tags: ["case", "fourth-amendment", "plain-view", "impound", "protective-measure", "automobile"]
holding: "Objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and admissible; a protective measure taken to secure a lawfully impounded car is not a search."
lake:
  record_id: "Harris v. United States (1968)"
  status: verified
  projected_at: 2026-07-09
---

# Harris v. United States (1968)

*390 U.S. 234 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Identity / disambiguation:** this is the 1968 [[Common Legal Terms#per-curiam|per curiam]] (plain-view seizure from a lawfully impounded car). It is a **different case** from *Harris v. United States*, 331 U.S. 145 (1947) (a sweeping search-incident-to-arrest holding **overruled** by [[Chimel v. California]]), and from *[[United States v. Harris (1971)|United States v. Harris]]*, 401 U.S. 1027 (1971) (reversed party). The year-suffix filename and bare-name `alias` keep the links from colliding.

## Background
Harris's car was seen leaving a robbery; it was traced and he was arrested entering it near his home. Police impounded the car as evidence and towed it to the precinct lot. Because it had begun to rain and the windows were open and a door unlocked, the arresting officer — following a department regulation to secure impounded vehicles — went to the lot to tag the car, roll up the windows, and lock the doors. Opening the passenger door to secure that window, he saw the robbery victim's automobile registration card lying face up on the door sill in plain view, and later seized it. The card was admitted at trial.

## Issue
Whether the officer discovered the registration card by means of an illegal search when he saw it in plain view while securing a lawfully impounded car.

## Rule
No. A measure taken to protect an impounded car is not a search: "the discovery of the card was not the result of a search of the car, but of a measure taken to protect the car while it was in police custody. Nothing in the Fourth Amendment requires the police to obtain a warrant in these narrow circumstances." — 390 U.S. at 236. ^pin-236

And plain-view objects are seizable: "It has long been settled that objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and may be introduced in evidence." — [*Id.*](https://www.courtlistener.com/opinion/107625/harris-v-united-states/#:~:text=It%20has%20long%20been%20settled) ^pin-236a

## Application
The officer was lawfully securing a car properly impounded as evidence; the precise findings below were that the card was discovered while protecting the car, not while searching it. Once the door was lawfully opened to secure the window, the victim's registration card was "plainly visible," so it was subject to seizure. The Court expressly noted it was **not** deciding the admissibility of evidence found pursuant to the inventory regulation itself — only that this protective discovery was lawful.

## Conclusion
Affirmed (per curiam). The card was lawfully seen and seized in plain view during a lawful protective measure; there was no illegal search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- The plain-view-seizure articulation is settled and was later given its structure by [[Coolidge v. New Hampshire]] and [[Horton v. California]] (which dropped the inadvertence requirement). The inventory-search question *Harris* reserved was answered separately in [[South Dakota v. Opperman]].

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Harris v. United States*, 390 U.S. 234 (1968) — https://www.courtlistener.com/opinion/107625/harris-v-united-states/ — pinpoint: 236.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ee879ac08fb4b3e3", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Harris v. United States (1968)"}, "payload": {"all": [{"cite": "390 U.S. 234", "page": "234", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "390"}, {"cite": "88 S. Ct. 992", "page": "992", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "19 L. Ed. 2d 1067", "page": "1067", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "19"}, {"cite": "1968 U.S. LEXIS 2283", "page": "2283", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}], "display": "390 U.S. 234", "official": {"cite": "390 U.S. 234", "page": "234", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "390"}, "official_selection_present": true, "record_id": "Harris v. United States (1968)"}}
{"assertion_id": "25146016438438de", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-236a", "record_id": "Harris v. United States (1968)"}, "payload": {"fragment": "#:~:text=It%20has%20long%20been%20settled", "page": null, "pin_id": "pin-236a", "pinpoint_status": "star-verified", "quote": "It has long been settled that objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and may be introduced in evidence.", "quote_fidelity": "matched", "record_id": "Harris v. United States (1968)", "star_marker": "236"}}
{"assertion_id": "f9b9a9360a798112", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-236", "record_id": "Harris v. United States (1968)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-236", "pinpoint_status": "slip-only", "quote": "--- # Harris v. United States (1968) *390 U.S. 234 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> > **Identity / disambiguation:** this is the 1968 per curiam (plain-view seizure from a lawfully impounded car). It is a **different case** from *Harris v. United States*, 331 U.S. 145 (1947) (a sweeping search-incident-to-arrest holding **overruled** by [[Chimel v. California]]), and from *United States v. Harris*, 401 U.S. 1027 (1971) (reversed party). The year-suffix filename and bare-name `alias` keep the links from colliding. ## Background Harris's car was seen leaving a robbery; it was traced and he was arrested entering it near his home. Police impounded the car as evidence and towed it to the precinct lot. Because it had begun to rain and the windows were open and a door unlocked, the arresting officer — following a department regulation to secure impounded vehicles — went to the lot to tag the car, roll up the windows, and lock the doors. Opening the passenger door to secure that window, he saw the robbery victim's automobile registration card lying face up on the door sill in plain view, and later seized it. The card was admitted at trial. ## Issue Whether the officer discovered the registration card by means of an illegal search when he saw it in plain view while securing a lawfully impounded car. ## Rule No. A measure taken to protect an impounded car is not a search:", "quote_fidelity": "mismatch", "record_id": "Harris v. United States (1968)", "star_marker": null}}
{"assertion_id": "10350838b874f36c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Harris v. United States (1968)"}, "payload": {"as_of_content": "1968-03-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Harris v. United States (1968)", "scope_note": "Per curiam. The plain-view-seizure formulation remains settled law; it was later structured (no-inadvertence requirement) by Horton v. California. Distinct case from the 1947 Harris v. United States (search incident to arrest), which Chimel v. California overruled.", "varies_by_point": false}}
```

### lake record — Harris v. United States (1968)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Harris v. United States (1968)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Harris v. United States",
    "case_name_short": "Harris",
    "case_name_full": "Harris v. United States",
    "input_case_name": "Harris v. United States (1968)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-03-05",
    "year": 1968,
    "docket": "92",
    "cluster_id": 107625,
    "lead_opinion_id": 107625,
    "sibling_ids": [
      107625,
      9423622,
      9423623
    ],
    "absolute_url": "/opinion/107625/harris-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 107608,
        "score": 20,
        "case_name": "Haynes v. United States"
      },
      {
        "cluster_id": 107623,
        "score": 20,
        "case_name": "United States v. Habig"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "390 U.S. 234",
      "volume": "390",
      "reporter": "U.S.",
      "page": "234",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 992",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "992",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 1067",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "1067",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 2283",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "2283",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "390 U.S. 234",
        "volume": "390",
        "reporter": "U.S.",
        "page": "234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 992",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "992",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 1067",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "1067",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 2283",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "2283",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "390 U.S. 234",
    "official_selection": {
      "court_class": "scotus",
      "selected": "390 U.S. 234",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-236",
      "page": null,
      "quote": "--- # Harris v. United States (1968) *390 U.S. 234 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> > **Identity / disambiguation:** this is the 1968 per curiam (plain-view seizure from a lawfully impounded car). It is a **different case** from *Harris v. United States*, 331 U.S. 145 (1947) (a sweeping search-incident-to-arrest holding **overruled** by [[Chimel v. California]]), and from *United States v. Harris*, 401 U.S. 1027 (1971) (reversed party). The year-suffix filename and bare-name `alias` keep the links from colliding. ## Background Harris's car was seen leaving a robbery; it was traced and he was arrested entering it near his home. Police impounded the car as evidence and towed it to the precinct lot. Because it had begun to rain and the windows were open and a door unlocked, the arresting officer \u2014 following a department regulation to secure impounded vehicles \u2014 went to the lot to tag the car, roll up the windows, and lock the doors. Opening the passenger door to secure that window, he saw the robbery victim's automobile registration card lying face up on the door sill in plain view, and later seized it. The card was admitted at trial. ## Issue Whether the officer discovered the registration card by means of an illegal search when he saw it in plain view while securing a lawfully impounded car. ## Rule No. A measure taken to protect an impounded car is not a search:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-236a",
      "page": null,
      "quote": "It has long been settled that objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and may be introduced in evidence.",
      "star_marker": "236",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 4774,
      "fragment": "#:~:text=It%20has%20long%20been%20settled",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-03-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Harris v. United States (1968)",
    "varies_by_point": false,
    "scope_note": "Per curiam. The plain-view-seizure formulation remains settled law; it was later structured (no-inadvertence requirement) by Horton v. California. Distinct case from the 1947 Harris v. United States (search incident to arrest), which Chimel v. California overruled.",
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
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
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
        "journal_ref": "Harris v. United States (1968):lane1_negative"
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
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesus Rodriguez v. State",
          "cluster_id": 2920356,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lang",
          "cluster_id": 6109,
          "cite": [
            "8 F.3d 268",
            "38 Fed. R. Serv. 579",
            "1993 U.S. App. LEXIS 30076",
            "1993 WL 478488"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. $10,000 in United States Currency",
          "cluster_id": 8946555,
          "cite": [
            "780 F.2d 213",
            "1986 U.S. App. LEXIS 21660"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jerome F. Blakeney",
          "cluster_id": 446901,
          "cite": [
            "753 F.2d 152",
            "243 U.S. App. D.C. 334",
            "1985 U.S. App. LEXIS 27774"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stewart v. State",
          "cluster_id": 1531281,
          "cite": [
            "681 S.W.2d 774",
            "1984 Tex. App. LEXIS 6422"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Clement Kolodziej",
          "cluster_id": 418003,
          "cite": [
            "706 F.2d 590",
            "1983 U.S. App. LEXIS 27009"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Milan Bagaric, Mile Markich, Ante Ljubas, Vinko Logarusic, Ranko Primorac, and Drago Sudar",
          "cluster_id": 417774,
          "cite": [
            "706 F.2d 42",
            "1983 U.S. App. LEXIS 28806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dees",
          "cluster_id": 1518524,
          "cite": [
            "639 S.W.2d 149",
            "1982 Mo. App. LEXIS 3679"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sims",
          "cluster_id": 1518614,
          "cite": [
            "639 S.W.2d 105",
            "1982 Mo. App. LEXIS 3686"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane1_negative"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frazier v. Cupp",
          "cluster_id": 107913,
          "cite": [
            "22 L. Ed. 2d 684",
            "89 S. Ct. 1420",
            "394 U.S. 731",
            "1969 U.S. LEXIS 1870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stoker v. State",
          "cluster_id": 2464243,
          "cite": [
            "788 S.W.2d 1",
            "1989 Tex. Crim. App. LEXIS 167",
            "1989 WL 107536"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold B. Dorman v. United States",
          "cluster_id": 293653,
          "cite": [
            "435 F.2d 385",
            "140 U.S. App. D.C. 313",
            "1970 U.S. App. LEXIS 9785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sharon Olabisiomotosho v. City of Houston City of Houston P. J. Bartlett K. L. Richards Rene Bertrand",
          "cluster_id": 765388,
          "cite": [
            "185 F.3d 521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine Tramunti",
          "cluster_id": 326798,
          "cite": [
            "513 F.2d 1087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Reisman",
          "cluster_id": 5678745,
          "cite": [
            "29 N.Y.2d 278",
            "277 N.E.2d 396",
            "327 N.Y.S.2d 342",
            "1971 N.Y. LEXIS 943"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Superior Court",
          "cluster_id": 1435013,
          "cite": [
            "478 P.2d 449",
            "3 Cal. 3d 807",
            "91 Cal. Rptr. 729",
            "45 A.L.R. 3d 559",
            "1970 Cal. LEXIS 249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. State",
          "cluster_id": 1914341,
          "cite": [
            "419 So. 2d 563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bowden",
          "cluster_id": 2123427,
          "cite": [
            "399 N.E.2d 482",
            "379 Mass. 472",
            "1980 Mass. LEXIS 944"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Silva",
          "cluster_id": 2120427,
          "cite": [
            "318 N.E.2d 895",
            "366 Mass. 402",
            "1974 Mass. LEXIS 732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Servis v. Commonwealth",
          "cluster_id": 1349258,
          "cite": [
            "371 S.E.2d 156",
            "6 Va. App. 507",
            "5 Va. Law Rep. 37",
            "1988 Va. App. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Seagull",
          "cluster_id": 1157235,
          "cite": [
            "632 P.2d 44",
            "95 Wash. 2d 898",
            "1981 Wash. LEXIS 1130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Diecidue, Larry Neil Miller, Frank Boni, Jr., A/K/A \"Mustache Frankie,\" Manuel Gispert, Anthony Antone, and Homer Rex Davis",
          "cluster_id": 368882,
          "cite": [
            "603 F.2d 535",
            "4 Fed. R. Serv. 1294",
            "1979 U.S. App. LEXIS 11494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harris v. United States (1968):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107625 OR 9423622 OR 9423623) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODU2ODk2MDAwMDAmcz0xMTg3MTY3JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107625+OR+9423622+OR+9423623%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107625 OR 9423622 OR 9423623)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjYmcz0xMzA3NjAyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107625+OR+9423622+OR+9423623%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107625 OR 9423622 OR 9423623)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 2,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107625 OR 9423622 OR 9423623)",
    "indexed_citing_opinions": 1248,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107625,
        "count": 1158,
        "count_source": "search"
      },
      {
        "opinion_id": 9423622,
        "count": 111,
        "count_source": "search"
      },
      {
        "opinion_id": 9423623,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1768,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/harris-v-united-states-1968.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2NDQ2MzQmcz00NDQ2MzkxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107625+OR+9423622+OR+9423623%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107625,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107625,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107625,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107625,
        "cited_id": 106771,
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
    "date_created": "2026-07-05T06:27:40Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:28:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:28:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:34:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:28:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Harris v. United States (1968)

```
<div>
<center><b><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U.S. 234</a></span> (1968)</b></center>
<center><h1>HARRIS<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 92.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 18, 1968.</center>
<center>Decided March 5, 1968.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><i>Paul H. Weinstein</i> argued the cause for petitioner. With him on the brief was <i>Laurence Levitan.</i></p>
<p><i>Francis X. Beytagh, Jr.,</i> argued the cause for the United States. On the brief were <i>Acting Solicitor General Spritzer, Assistant Attorney General Vinson, Beatrice Rosenberg</i> and <i>Julia P. Cooper.</i></p>
<p>PER CURIAM.</p>
<p>Petitioner was charged with robbery under the District of Columbia Code. D. C. Code Ann. § 22-2901. At his trial in the United States District Court for the District of Columbia, petitioner moved to suppress an automobile registration card belonging to the robbery victim, which the Government sought to introduce in evidence. The trial court, after a hearing, ruled that the card was admissible. Petitioner was convicted of the crime charged and sentenced to imprisonment for a period of <span class="star-pagination">*235</span> two to seven years. On appeal, a panel of the United States Court of Appeals for the District of Columbia Circuit reversed, holding that the card had been obtained by means of an unlawful search. The Government's petition for rehearing <i>en banc</i> was, however, granted, and the full Court of Appeals affirmed petitioner's conviction, with two judges dissenting. We granted certiorari to consider the problem presented under the Fourth Amendment. <span class="citation" data-id="8958920"><a href="/opinion/8967537/jackson-v-district-court-of-appeal-of-california-fourth-appellate/" aria-description="Citation for case: Jackson v. District Court of Appeal of California, Fourth...">386 U. S. 1003</a></span> (1967). We affirm.</p>
<p>Petitioner's automobile had been seen leaving the site of the robbery. The car was traced and petitioner was arrested as he was entering it, near his home. After a cursory search of the car, the arresting officer took petitioner to a police station. The police decided to impound the car as evidence, and a crane was called to tow it to the precinct. It reached the precinct about an hour and a quarter after petitioner. At this moment, the windows of the car were open and the door unlocked. It had begun to rain.</p>
<p>A regulation of the Metropolitan Police Department requires the officer who takes an impounded vehicle in charge to search the vehicle thoroughly, to remove all valuables from it, and to attach to the vehicle a property tag listing certain information about the circumstances of the impounding. Pursuant to this regulation, and without a warrant, the arresting officer proceeded to the lot to which petitioner's car had been towed, in order to search the vehicle, to place a property tag on it, to roll up the windows, and to lock the doors. The officer entered on the driver's side, searched the car, and tied a property tag on the steering wheel. Stepping out of the car, he rolled up an open window on one of the back doors. Proceeding to the front door on the passenger side, the officer opened the door in order to secure the window and door. He then saw the registration card, which lay face up on the metal stripping over which <span class="star-pagination">*236</span> the door closes. The officer returned to the precinct, brought petitioner to the car, and confronted petitioner with the registration card. Petitioner disclaimed all knowledge of the card. The officer then seized the card and brought it into the precinct. Returning to the car, he searched the trunk, rolled up the windows, and locked the doors.</p>
<p>The sole question for our consideration is whether the officer discovered the registration card by means of an illegal search. We hold that he did not. The admissibility of evidence found as a result of a search under the police regulation is not presented by this case. The precise and detailed findings of the District Court, accepted by the Court of Appeals, were to the effect that the discovery of the card was not the result of a search of the car, but of a measure taken to protect the car while it was in police custody. Nothing in the Fourth Amendment requires the police to obtain a warrant in these narrow circumstances.</p>
<p>Once the door had lawfully been opened, the registration card, with the name of the robbery victim on it, was plainly visible. It has long been settled that objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and may be introduced in evidence. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42-43</a></span> (1963); <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/" aria-description="Citation for case: United States v. Lee">274 U. S. 559</a></span> (1927); <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924).</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE MARSHALL took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE DOUGLAS, concurring.</p>
<p>Though <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>, is not mentioned in the Court's opinion, I assume it has survived <span class="star-pagination">*237</span> because in the present case (1) the car was lawfully in police custody, and the police were responsible for protecting the car; (2) while engaged in the performance of their duty to protect the car, and not engaged in an inventory or other search of the car, they came across incriminating evidence.</p>
</div>
```

---

## GROUP: _overhaul2/lake/cases/Hayes v. Florida.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Hayes v. Florida"
type: case
citation: "470 U.S. 811 (1985)"
parallel_cite: "105 S. Ct. 1643; 84 L. Ed. 2d 705; 53 U.S.L.W. 4382"
neutral_cite: 1985 U.S. LEXIS 1523
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-03-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hayes v. Florida
  varies_by_point: false
  scope_note: "Good law; transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest. The Court left open (dicta) that brief field fingerprinting on reasonable suspicion, carried out with dispatch, might be permissible."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111382/hayes-v-florida/"
  cluster_id: 111382
  opinion_id: 9429967
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Limiting"
related: ["[[Davis v. Mississippi]]", "[[Florida v. Royer]]", "[[United States v. Hensley]]", "[[Terry v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "fingerprinting", "investigative-detention", "arrest"]
holding: "Transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest requiring probable cause (brief field fingerprinting on reasonable suspicion left open)."
lake:
  record_id: Hayes v. Florida
  status: verified
  projected_at: 2026-07-06
---

# Hayes v. Florida

*470 U.S. 811 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a series of burglary-rapes, officers without probable cause or a warrant went to Hayes's home, and — when he balked — effectively told him he would be arrested if he did not accompany them. They transported him to the station and fingerprinted him; the prints matched those at a crime scene and were used to convict him. Hayes moved to suppress, relying on *[[Davis v. Mississippi]]*.

## Issue
Whether the Fourth Amendment permits police, without probable cause or judicial authorization, to transport a suspect from his home to the station and detain him there for fingerprinting.

## Rule
No — such a station-house detention is an arrest requiring probable cause: "the line is crossed when the police, without probable cause or a warrant, forcibly remove a person from his home or other place in which he is entitled to be and transport him to the police station, where he is detained, although briefly, for investigative purposes. We adhere to the view that such seizures, at least where not under judicial supervision, are sufficiently like arrests to invoke the traditional rule that arrests may constitutionally be made only on probable cause." — 470 U.S. at 816. ^pin-816

The Court reserved a narrower field practice: "There is thus support in our cases for the view that the Fourth Amendment would permit seizures for the purpose of fingerprinting, if there is reasonable suspicion that the suspect has committed a criminal act, if there is a reasonable basis for believing that fingerprinting will establish or negate the suspect's connection with that crime, and if the procedure is carried out with dispatch." — *Id.* at 817. ^pin-817

## Application
Officers had neither probable cause nor a warrant nor judicial authorization, yet — under threat of arrest — removed Hayes from his home, transported him to the station, and detained him to take his prints. That conduct crossed the line into a [[Common Legal Terms#de-facto|de facto]] arrest requiring probable cause, so the fingerprints were the fruit of an unlawful seizure and had to be suppressed. The Court emphasized that its holding did not foreclose a brief *field* detention to take fingerprints where officers have reasonable suspicion and proceed with dispatch — but no such limited, on-site procedure occurred here.

## Conclusion
The warrantless station-house fingerprinting detention was an arrest without probable cause; the fingerprints were suppressed and the conviction reversed. *Hayes* reaffirms [[Davis v. Mississippi]] and marks the transport-to-the-station line while flagging the open question of brief field fingerprinting on reasonable suspicion.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Reaffirms and applies [[Davis v. Mississippi]]; consistent with the de-facto-arrest analysis of [[Florida v. Royer]] and the *[[Terry v. Ohio|Terry]]*-stop reach discussed in [[United States v. Hensley]] and [[Terry v. Ohio]].

## Appears on
- [[Seizure of the Person]] — *Limiting*

## Sources
- *Hayes v. Florida*, 470 U.S. 811 (1985) — https://www.courtlistener.com/opinion/111382/hayes-v-florida/ — pinpoints: 816, 817.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2d9d4f6fd5d0f3e3", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hayes v. Florida"}, "payload": {"all": [{"cite": "470 U.S. 811", "page": "811", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "470"}, {"cite": "105 S. Ct. 1643", "page": "1643", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "84 L. Ed. 2d 705", "page": "705", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "1985 U.S. LEXIS 1523", "page": "1523", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4382", "page": "4382", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "470 U.S. 811", "official": {"cite": "470 U.S. 811", "page": "811", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "470"}, "official_selection_present": true, "record_id": "Hayes v. Florida"}}
{"assertion_id": "a4a3e32184f7da69", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-817", "record_id": "Hayes v. Florida"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-817", "pinpoint_status": "slip-only", "quote": "There is thus support in our cases for the view that the Fourth Amendment would permit seizures for the purpose of fingerprinting, if there is reasonable suspicion that the suspect has committed a criminal act, if there is a reasonable basis for believing that fingerprinting will establish or negate the suspect's connection with that crime, and if the procedure is carried out with dispatch.", "quote_fidelity": "mismatch", "record_id": "Hayes v. Florida", "star_marker": null}}
{"assertion_id": "c707e64724e797d9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-816", "record_id": "Hayes v. Florida"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-816", "pinpoint_status": "slip-only", "quote": "--- # Hayes v. Florida *470 U.S. 811 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a series of burglary-rapes, officers without probable cause or a warrant went to Hayes's home, and — when he balked — effectively told him he would be arrested if he did not accompany them. They transported him to the station and fingerprinted him; the prints matched those at a crime scene and were used to convict him. Hayes moved to suppress, relying on *Davis v. Mississippi*. ## Issue Whether the Fourth Amendment permits police, without probable cause or judicial authorization, to transport a suspect from his home to the station and detain him there for fingerprinting. ## Rule No — such a station-house detention is an arrest requiring probable cause:", "quote_fidelity": "mismatch", "record_id": "Hayes v. Florida", "star_marker": null}}
{"assertion_id": "e99712aef1e65026", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hayes v. Florida"}, "payload": {"as_of_content": "1985-03-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hayes v. Florida", "scope_note": "Good law; transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest. The Court left open (dicta) that brief field fingerprinting on reasonable suspicion, carried out with dispatch, might be permissible.", "varies_by_point": false}}
```

### lake record — Hayes v. Florida

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hayes v. Florida",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hayes v. Florida",
    "case_name_short": "Hayes",
    "case_name_full": "Hayes v. Florida",
    "input_case_name": "Hayes v. Florida",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-20",
    "year": 1985,
    "docket": null,
    "cluster_id": 111382,
    "lead_opinion_id": 9429967,
    "sibling_ids": [
      111382,
      9429967,
      9429968
    ],
    "absolute_url": "/opinion/111382/hayes-v-florida/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "470 U.S. 811",
      "volume": "470",
      "reporter": "U.S.",
      "page": "811",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1643",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 705",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "705",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4382",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4382",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 1523",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "1523",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "470 U.S. 811",
        "volume": "470",
        "reporter": "U.S.",
        "page": "811",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1643",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 705",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "705",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 1523",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "1523",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4382",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4382",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "470 U.S. 811",
    "official_selection": {
      "court_class": "scotus",
      "selected": "470 U.S. 811",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-816",
      "page": null,
      "quote": "--- # Hayes v. Florida *470 U.S. 811 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a series of burglary-rapes, officers without probable cause or a warrant went to Hayes's home, and \u2014 when he balked \u2014 effectively told him he would be arrested if he did not accompany them. They transported him to the station and fingerprinted him; the prints matched those at a crime scene and were used to convict him. Hayes moved to suppress, relying on *Davis v. Mississippi*. ## Issue Whether the Fourth Amendment permits police, without probable cause or judicial authorization, to transport a suspect from his home to the station and detain him there for fingerprinting. ## Rule No \u2014 such a station-house detention is an arrest requiring probable cause:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-817",
      "page": null,
      "quote": "There is thus support in our cases for the view that the Fourth Amendment would permit seizures for the purpose of fingerprinting, if there is reasonable suspicion that the suspect has committed a criminal act, if there is a reasonable basis for believing that fingerprinting will establish or negate the suspect's connection with that crime, and if the procedure is carried out with dispatch.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-03-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hayes v. Florida",
    "varies_by_point": false,
    "scope_note": "Good law; transporting a suspect to the station for fingerprinting without consent, a warrant, or probable cause is a seizure tantamount to arrest. The Court left open (dicta) that brief field fingerprinting on reasonable suspicion, carried out with dispatch, might be permissible.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Financial Casualty & Surety, Inc.",
          "cluster_id": 4380249,
          "cite": [
            "10 Cal. App. 5th 369",
            "216 Cal. Rptr. 3d 173",
            "2017 Cal. App. LEXIS 294"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Allen Decker v. State of Indiana",
          "cluster_id": 2745993,
          "cite": [
            "19 N.E.3d 368",
            "2014 Ind. App. LEXIS 515",
            "2014 WL 5461790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cabral",
          "cluster_id": 8727521,
          "cite": [
            "965 F. Supp. 2d 161",
            "2013 WL 1684162",
            "2013 U.S. Dist. LEXIS 53890"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Branham v. Commonwealth",
          "cluster_id": 1057965,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Porter v. State",
          "cluster_id": 1759540,
          "cite": [
            "255 S.W.3d 234",
            "2008 WL 553648"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Corbin v. State",
          "cluster_id": 1636551,
          "cite": [
            "91 S.W.3d 383",
            "2002 Tex. App. LEXIS 7528",
            "2002 WL 31374687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Elmer Pace and Linda Pace v. City of Des Moines, Iowa, and Brian Danner",
          "cluster_id": 767420,
          "cite": [
            "201 F.3d 1050",
            "2000 U.S. App. LEXIS 388",
            "2000 WL 31713"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Shareef",
          "cluster_id": 154170,
          "cite": [
            "100 F.3d 1491",
            "1996 U.S. App. LEXIS 29483",
            "1996 WL 657885"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane1_negative"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl James v. Wilkes Barre City",
          "cluster_id": 812864,
          "cite": [
            "700 F.3d 675",
            "2012 U.S. App. LEXIS 24592",
            "2012 WL 5954632"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katherine Gardenhire and Walter Gardenhire v. Donald Schubert, in His Individual and Official Capacity as Chief of Police",
          "cluster_id": 767858,
          "cite": [
            "205 F.3d 303",
            "2000 U.S. App. LEXIS 3126",
            "2000 WL 232311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "David Evans v. Patrick Baker",
          "cluster_id": 813710,
          "cite": [
            "703 F.3d 636"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaupp v. Texas",
          "cluster_id": 127919,
          "cite": [
            "155 L. Ed. 2d 814",
            "123 S. Ct. 1843",
            "538 U.S. 626",
            "2003 U.S. LEXIS 3670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jaime Soto, Also Known as Leonel Guerra",
          "cluster_id": 602824,
          "cite": [
            "988 F.2d 1548",
            "1993 U.S. App. LEXIS 5415",
            "1993 WL 77475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Thomas Cherry",
          "cluster_id": 450747,
          "cite": [
            "759 F.2d 1196",
            "81 A.L.R. Fed. 303",
            "1985 U.S. App. LEXIS 29511"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
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
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Lopez-Medina",
          "cluster_id": 795541,
          "cite": [
            "461 F.3d 724",
            "71 Fed. R. Serv. 50",
            "2006 U.S. App. LEXIS 21682",
            "2006 WL 2454962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner v. City of Taylor",
          "cluster_id": 2972481,
          "cite": [
            "412 F.3d 629",
            "2005 WL 1398522"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnny L. Marshall v. Secretary, Florida Department of Corrections",
          "cluster_id": 4237860,
          "cite": [
            "828 F.3d 1277",
            "2016 U.S. App. LEXIS 12812",
            "2016 WL 3742164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Commonwealth",
          "cluster_id": 1206381,
          "cite": [
            "354 S.E.2d 79",
            "4 Va. App. 53",
            "3 Va. Law Rep. 2081",
            "1987 Va. App. LEXIS 165"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Juarez v. State",
          "cluster_id": 1562920,
          "cite": [
            "758 S.W.2d 772",
            "1988 Tex. Crim. App. LEXIS 172",
            "1988 WL 98938"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cynthia Kernats v. Thomas O'Sullivan",
          "cluster_id": 678542,
          "cite": [
            "35 F.3d 1171",
            "1994 U.S. App. LEXIS 25789",
            "1994 WL 503404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry Espinosa",
          "cluster_id": 463815,
          "cite": [
            "782 F.2d 888",
            "1986 U.S. App. LEXIS 21494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sornberger v. City Of Knoxville",
          "cluster_id": 792982,
          "cite": [
            "434 F.3d 1006",
            "2006 U.S. App. LEXIS 1394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur Maez",
          "cluster_id": 521939,
          "cite": [
            "872 F.2d 1444",
            "1989 U.S. App. LEXIS 5092",
            "1989 WL 36532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hayes v. Florida:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111382 OR 9429967 OR 9429968) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MTcwMzM2MDAwMDAmcz01OTEyMDAmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111382+OR+9429967+OR+9429968%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111382 OR 9429967 OR 9429968)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTkmcz0xODkxNTA0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111382+OR+9429967+OR+9429968%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111382 OR 9429967 OR 9429968)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111382 OR 9429967 OR 9429968)",
    "indexed_citing_opinions": 357,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111382,
        "count": 319,
        "count_source": "search"
      },
      {
        "opinion_id": 9429967,
        "count": 44,
        "count_source": "search"
      },
      {
        "opinion_id": 9429968,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 604,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hayes-v-florida.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3MTMyMzQmcz05NTA0MjM2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111382+OR+9429967+OR+9429968%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111382,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 1226554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 1677682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111382,
        "cited_id": 2223532,
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
    "date_created": "2026-07-05T06:34:43Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:34:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:34:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:38:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:34:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hayes v. Florida

```
<opinion type="majority">
<author id="b868-6">Justice White</author>
<p id="AG2">delivered the opinion of the Court.</p>
<p id="b868-7">The issue before us in this case is whether the Fourth Amendment to the Constitution of the United States, applicable to the States by virtue of the Fourteenth Amendment, was properly applied by the District Court of Appeal of Florida, Second District, to allow police to transport a suspect to the station house for fingerprinting, without his consent and without probable cause or prior judicial authorization.</p>
<p id="b868-8">A series of burglary-rapes occurred in Punta Gorda, Florida, in 1980. Police found latent fingerprints on the doorknob of the bedroom of one of the victims, fingerprints they believed belonged to the assailant. The police also found a herringbone pattern tennis shoe print near the victim’s front porch. Although they had little specific information to tie petitioner Hayes to the crime, after police interviewed him along with 30 to 40 other men who generally fit the description of the assailant, the investigators came to consider petitioner a principal suspect. They decided to visit petitioner’s home to obtain his fingerprints or, if he was uncooperative, to arrest him. They did not seek a warrant authorizing this procedure.</p>
<p id="b868-9">Arriving at petitioner’s house, the officers spoke to petitioner on his front porch. When he expressed reluctance voluntarily to accompany them to the station for fingerprinting, one of the investigators explained that they would therefore arrest him. Petitioner, in the words of the investigator, then “blurted out” that he would rather go with the officers to the station than be arrested. App. 20. While the officers were on the front porch, they also seized a pair of herringbone pattern tennis shoes in plain view.</p>
<p id="b869-4"><page-number citation-index="1" label="813">*813</page-number>Petitioner was then taken to the station house, where he was fingerprinted. When police determined that his prints matched those left at the scene of the crime, petitioner was placed under formal arrest. Before trial, petitioner moved to suppress the fingerprint evidence, claiming it was the fruit of an illegal detention. The trial court denied the motion and admitted the evidence without expressing a reason. Petitioner was convicted of the burglary and sexual battery committed at the scene where the latent fingerprints were found.</p>
<p id="b869-5">The District Court of Appeal of Florida, Second District, affirmed the conviction. <span class="citation" data-id="1677682"><a href="/opinion/1677682/hayes-v-state/" aria-description="Citation for case: Hayes v. State">439 So. 2d 896</a></span> (1983). The court declined to find consent, reasoning that in view of the threatened arrest it was, “at best, highly questionable” that Hayes voluntarily accompanied the officers to the station. <span class="citation" data-id="1677682"><a href="/opinion/1677682/hayes-v-state/#898" aria-description="Citation for case: Hayes v. State"><em>Id., </em>at 898</a></span>. The court also expressly found that the officers did not have probable cause to arrest petitioner until after they obtained his fingerprints. <span class="citation" data-id="1677682"><a href="/opinion/1677682/hayes-v-state/#899" aria-description="Citation for case: Hayes v. State"><em>Id., </em>at 899</a></span>. Nevertheless, although finding neither consent nor probable cause, the court held, analogizing to the stop-and-frisk rule of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), that the officers could transport petitioner to the station house and take his fingerprints on the basis of their reasonable suspicion that he was involved in the crime. <span class="citation" data-id="1677682"><a href="/opinion/1677682/hayes-v-state/#899" aria-description="Citation for case: Hayes v. State">439 So. 2d, at 899, 904</a></span>.</p>
<p id="b869-6">The Florida Supreme Court denied review by a four-to-three decision, <span class="citation no-link">447 So. 2d 886</span> (1983). We granted certiorari to review this application of <em>Terry, </em><span class="citation multiple-matches"><a href="/c/U.%20S./469/816/">469 U. S. 816</a></span> (1984), and we now reverse.</p>
<p id="b869-7">We agree with petitioner that <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), requires reversal of the judgment below. In <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>, </em>in the course of investigating a rape, police officers brought petitioner Davis to police headquarters on December 3, 1965. He was fingerprinted and briefly questioned before being released. He was later charged and convicted of the rape. An issue there was whether the fingerprints taken on December 3 were the inadmissible fruits of an illegal detention. Concededly, the police at that time were without prob<page-number citation-index="1" label="814">*814</page-number>able cause for an arrest, there was no warrant, and Davis had not consented to being taken to the station house. The State nevertheless contended that the Fourth Amendment did not forbid an investigative detention for the purpose of fingerprinting, even in the absence of probable cause or a warrant. We rejected that submission, holding that Davis’ detention for the purpose of fingerprinting was subject to the constraints of the Fourth Amendment and exceeded the permissible limits of those temporary seizures authorized by <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra.</a></span> </em>This was so even though fingerprinting, because it involves neither repeated harassment nor any of the probing into private life and thoughts that often marks interrogation and search, represents a much less serious intrusion upon personal security than other types of searches and detentions. <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#727" aria-description="Citation for case: Davis v. Mississippi">394 U. S., at 727</a></span>. Nor was it a sufficient answer to the Fourth Amendment issue to recognize that fingerprinting is an inherently more reliable and effective crime-solving mechanism than other types of evidence such as lineups and confessions. <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Ibid.</a></span> </em>The Court indicated that perhaps under narrowly confined circumstances, a detention for fingerprinting on less than probable cause might comply with the Fourth Amendment, but found it unnecessary to decide that question since no effort was made to employ the procedures necessary to satisfy the Fourth Amendment. <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">Id., at 728</a></span>. Rather, Davis had been detained at police headquarters without probable cause to arrest and without authorization by a judicial officer.</p>
<p id="b870-5">Here, as in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>, </em>there was no probable cause to arrest, no consent to the journey to the police station, and no judicial authorization for such a detention for fingerprinting purposes.<footnotemark>1</footnotemark> Unless later cases have undermined <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span> </em>or <page-number citation-index="1" label="815">*815</page-number>we now disavow that decision, the judgment below must be reversed.</p>
<p id="b871-5">None of our later cases have undercut the holding in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span> </em>that transportation to and investigative detention at the station house without probable cause or judicial authorization together violate the Fourth Amendment. Indeed, some 10 years later, in <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), we refused to extend <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra,</a></span> </em>to authorize investigative interrogations at police stations on less than probable cause, even though proper warnings under <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), had been given. We relied on and reaffirmed the holding in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span> </em>that in the absence of probable cause or a warrant investigative detentions at the police station for fingerprinting purposes could not be squared with the Fourth Amendment, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 213-216</a></span>, while at the same time repeating the possibility that the Amendment might permit a narrowly circumscribed procedure for fingerprinting detentions on less than probable cause. Since that time, we have several times revisited and explored the reach of <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>most recently in <em>United States </em>v. <em>Sharpe, ante, </em>p. 675, and <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">469 U. S. 221</a></span> (1985). But none of these cases have sustained against Fourth Amendment challenge the involuntary removal of a suspect from his home to a police station and his detention there for investigative purposes, whether for interrogation or fingerprinting, absent probable cause or judicial authorization.</p>
<p id="b871-6">Nor are we inclined to forswear <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>. </em>There is no doubt that at some point in the investigative process, police pro<page-number citation-index="1" label="816">*816</page-number>cedures can qualitatively and quantitatively be so intrusive with respect to a suspect’s freedom of movement and privacy interests as to trigger the full protection of the Fourth and Fourteenth Amendments. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York"><em>Dunaway, supra, </em>at 212</a></span>; <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#499" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 499</a></span> (1983) (plurality opinion). And our view continues to be that the line is crossed when the police, without probable cause or a warrant, forcibly remove a person from his home or other place in which he is entitled to be and transport him to the police station, where he is detained, although briefly, for investigative purposes. We adhere to the view that such seizures, at least where not under judicial supervision, are sufficiently like arrests to invoke the traditional rule that arrests may constitutionally be made only on probable cause.<footnotemark>2</footnotemark></p>
<p id="b872-5">None of the foregoing implies that a brief detention in the field for the purpose of fingerprinting, where there is only reasonable suspicion not amounting to probable cause, is necessarily impermissible under the Fourth Amendment. In addressing the reach of a <em>Terry </em>stop in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972), we observed that “[a] brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be most reasonable in light of the facts known to the officer at the time.” Also, just this Term, we concluded that if there are articulable facts supporting a reasonable suspicion that a person has committed a criminal offense, that person may be stopped in order to identify him, to question him briefly, or to detain him briefly while attempting to obtain additional information. <em>United States </em>v. <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#229" aria-description="Citation for case: United States v. Hensley"><em>Hensley, supra, </em>at 229, 232, 234</a></span>. Cf. <em>United States </em><page-number citation-index="1" label="817">*817</page-number>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975). There is thus support in our cases for the view that the Fourth Amendment would permit seizures for the purpose of fingerprinting, if there is reasonable suspicion that the suspect has committed a criminal act, if there is a reasonable basis for believing that fingerprinting will establish or negate the suspect’s connection with that crime, and if the procedure is carried out with dispatch. Cf. <em>United States </em>v. <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place, supra.</a></span> </em>Of course, neither reasonable suspicion nor probable cause would suffice to permit the officers to make a warrantless entry into a person’s house for the purpose of obtaining fingerprint identification. <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980).</p>
<p id="b873-5">We also do not abandon the suggestion in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span> </em>and <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>that under circumscribed procedures, the Fourth Amendment might permit the judiciary to authorize the seizure of a person on less than probable cause and his removal to the police station for the purpose of fingerprinting. We do not, of course, have such a case before us.<footnotemark>3</footnotemark> We do note, however, that some States, in reliance on the suggestion in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>, </em>have enacted procedures for judicially authorized seizures for the purpose of fingerprinting. The state courts are not in accord on the validity of these efforts to insulate investigative seizures from Fourth Amendment invalidation. Compare <em>People </em>v. <em>Madson, </em><span class="citation" data-id="1226554"><a href="/opinion/1226554/people-v-madson/#31" aria-description="Citation for case: People v. Madson">638 P. 2d 18, 31-32</a></span> (Colo. 1981), with <em>State </em>v. <em>Evans, </em><span class="citation" data-id="9740420"><a href="/opinion/2223532/state-v-evans/#438" aria-description="Citation for case: State v. Evans">215 Neb. 433, 438-439</a></span>, <span class="citation" data-id="9740420"><a href="/opinion/2223532/state-v-evans/#792" aria-description="Citation for case: State v. Evans">338 N. W. 2d 788, 792-793</a></span> (1983), and <em>In re an Investigation into Death of Abe A., </em>56 N. Y. 2d 288, 295-296, <span class="citation" data-id="5534665"><a href="/opinion/5685680/in-re-of-an-investigation-into-the-death-of-jon-l/#269" aria-description="Citation for case: In re of an Investigation into the Death of Jon L.">437 N. E. 2d 265, 269</a></span> (1982).</p>
<p id="b873-6">As we have said, absent probable cause and a warrant, <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), requires the <page-number citation-index="1" label="818">*818</page-number>reversal of the judgment of the Florida District Court of Appeal.</p>
<p id="b874-5">
<em>It is so ordered.</em>
</p>
<judges id="b874-6">Justice Blackmun concurs in the judgment.</judges>
<judges id="b874-7">Justice Powell took no part in the consideration or decision in this case.</judges>
<footnote label="1">
<p id="b870-6"> The Florida District Court of Appeal judged this case on the basis of its determination that the police were without probable cause to arrest and that Hayes did not voluntarily agree to accompany the officers to the police station. Although the State invites us to review the record and hold either that there was probable cause to arrest or that Hayes voluntarily <page-number citation-index="1" label="815">*815</page-number>went with the officers to the station, we decline to become involved in these fact-bound issues. We also put aside the State’s suggestion that the inevitable discovery exception to the exclusionary rule, see <em>Nix </em>v. <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams"><em>Williams, 467 </em>U. S. 431</a></span> (1984), applies in this case. This argument was not presented to or passed upon by any of the state courts and is presented here for the first time. We thus address only the issue decided by the Florida court and presented in the petition for certiorari.</p>
</footnote>
<footnote label="2">
<p id="b872-6"> Thus, in <em>United States </em>v. <em>Sharpe, ante, </em>p. 675, where we recently sustained a 20-minute investigatory stop on a highway, we pointed out that the pertinent facts in <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>, </em>where we invalidated the detention, were “that (1) the defendant was taken from a private dwelling; (2) he was transported unwillingly to the police station; and (3) he there was subjected to custodial interrogation resulting in a confession.” <em>Ante, </em>at 684, n. 4.</p>
</footnote>
<footnote label="3">
<p id="b873-7"> Nor is there any suggestion in this case that there were any exigent circumstances making necessary the removal of Hayes to the station house for the purpose of fingerprinting.</p>
</footnote>
</opinion>
```

---
