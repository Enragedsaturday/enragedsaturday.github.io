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

## GROUP: content/cases/Strickler v. Greene.md  (`case`, 5 assertions)

### content_page

```
---
title: "Strickler v. Greene"
type: case
citation: "527 U.S. 263 (1999)"
parallel_cite: "119 S. Ct. 1936; 144 L. Ed. 2d 286"
neutral_cite: 1999 U.S. LEXIS 4191
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-06-17
docket: 98-5864
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Strickler v. Greene
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118307/strickler-v-greene/"
  cluster_id: 118307
  opinion_id: 118307
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Giglio v. United States]]", "[[Smith v. Cain]]", "[[Kyles v. Whitley]]", "[[United States v. Bagley]]"]
aliases: []
tags: ["case", "brady", "materiality", "suppression", "prejudice"]
holding: "Canonical statement of the THREE Brady components: (1) the evidence must be favorable (exculpatory OR impeaching); (2) it must have been…"
lake:
  record_id: Strickler v. Greene
  status: verified
  projected_at: 2026-07-06
---

# Strickler v. Greene

*527 U.S. 263 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Strickler was convicted of capital murder. The prosecution had not disclosed police notes and letters showing that a key eyewitness, Anne Stoltzfus, had initially been unable to recall the events she later described with confidence at trial. Strickler raised a *[[Brady v. Maryland|Brady]]* claim in federal [[Common Legal Terms#habeas-corpus|habeas]].

## Issue
What a defendant must establish to prove a *[[Brady v. Maryland|Brady]]* violation.

## Rule
The Court set out the elements of a *[[Brady v. Maryland|Brady]]* violation. "There are three components of a true *Brady* violation: The evidence at issue must be favorable to the accused, either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadvertently; and prejudice must have ensued." — 527 U.S. at 281–282. ^pin-281

As to that prejudice (materiality) element, "strictly speaking, there is never a real '*Brady* violation' unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict." — *Id.* at 281. ^pin-281a

## Application
The undisclosed documents were favorable because they impeached Stoltzfus, and they had been suppressed by the State—so two components were established. But the Court found no reasonable probability of a different verdict given the other evidence of guilt, so the prejudice component was not met and Strickler's claim failed.

## Conclusion
The three-component *[[Brady v. Maryland|Brady]]* standard governs, but because Strickler did not show prejudice, relief was denied.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The canonical statement of the [[Brady v. Maryland]] elements, incorporating impeachment evidence ([[Giglio v. United States]]) and the reasonable-probability materiality standard of [[United States v. Bagley]] / [[Kyles v. Whitley]]; applied in [[Smith v. Cain]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Strickler v. Greene*, 527 U.S. 263 (1999) — https://www.courtlistener.com/opinion/118307/strickler-v-greene/ — pinpoints: 281, 282.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ee10de17827a83eb", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "527 U.S. 263 (1999)", "court": "U.S. Supreme Court", "neutral_cite": "1999 U.S. LEXIS 4191", "official_citation_present": true, "parallel_cite": "119 S. Ct. 1936; 144 L. Ed. 2d 286", "title": "Strickler v. Greene", "year": "1999"}}
{"assertion_id": "368bfccddb60d3b8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Canonical statement of the THREE Brady components: (1) the evidence must be favorable (exculpatory OR impeaching); (2) it must have been…", "title": "Strickler v. Greene"}}
{"assertion_id": "61d8d55bef2724e5", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Strickler v. Greene"}}
{"assertion_id": "0ac50723c7467e7f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1999-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Strickler v. Greene", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Strickler v. Greene", "varies_by_point": "false"}}
{"assertion_id": "ce3550bd916b0a28", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Strickler v. Greene"}}
```

### lake record — Strickler v. Greene

```json
{
  "schema_version": "s2.v1",
  "record_id": "Strickler v. Greene",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Strickler v. Greene",
    "case_name_short": "Strickler",
    "case_name_full": "Strickler v. Greene, Warden",
    "input_case_name": "Strickler v. Greene",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-06-17",
    "year": 1999,
    "docket": "98-5864",
    "cluster_id": 118307,
    "lead_opinion_id": 118307,
    "sibling_ids": [
      118307,
      9433839,
      9433840
    ],
    "absolute_url": "/opinion/118307/strickler-v-greene/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "527 U.S. 263",
      "volume": "527",
      "reporter": "U.S.",
      "page": "263",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1936",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1936",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 286",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "286",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 4191",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4191",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "527 U.S. 263",
        "volume": "527",
        "reporter": "U.S.",
        "page": "263",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1936",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1936",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 286",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "286",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 4191",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4191",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "527 U.S. 263",
    "official_selection": {
      "court_class": "scotus",
      "selected": "527 U.S. 263",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-281",
      "page": null,
      "quote": "--- # Strickler v. Greene *527 U.S. 263 (1999)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Strickler was convicted of capital murder. The prosecution had not disclosed police notes and letters showing that a key eyewitness, Anne Stoltzfus, had initially been unable to recall the events she later described with confidence at trial. Strickler raised a *Brady* claim in federal habeas. ## Issue What a defendant must establish to prove a *Brady* violation. ## Rule The Court set out the elements of a *Brady* violation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-281a",
      "page": null,
      "quote": "strictly speaking, there is never a real '*Brady* violation' unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Strickler v. Greene",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Jevric",
          "cluster_id": 10873877,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 10309030,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. District Attorney for the Hampden District",
          "cluster_id": 9468079,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 9435476,
          "cite": [
            "2023 Ohio 3894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ardolino v. People",
          "cluster_id": 2595020,
          "cite": [
            "69 P.3d 73",
            "2003 WL 21057416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banks v. Dretke",
          "cluster_id": 131165,
          "cite": [
            "157 L. Ed. 2d 1166",
            "124 S. Ct. 1256",
            "540 U.S. 668",
            "2004 U.S. LEXIS 1621",
            "72 U.S.L.W. 4193",
            "17 Fla. L. Weekly Fed. S 153"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cone v. Bell",
          "cluster_id": 145883,
          "cite": [
            "173 L. Ed. 2d 701",
            "129 S. Ct. 1769",
            "556 U.S. 449",
            "2009 U.S. LEXIS 3298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owens v. Baltimore City State's Attorneys Office",
          "cluster_id": 2736472,
          "cite": [
            "767 F.3d 379",
            "2014 U.S. App. LEXIS 18294",
            "2014 WL 4723803"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LaMar",
          "cluster_id": 6890210,
          "cite": [
            "95 Ohio St. 3d 181",
            "767 N.E.2d 166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
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
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Pitsonbarger",
          "cluster_id": 2024743,
          "cite": [
            "793 N.E.2d 609",
            "205 Ill. 2d 444",
            "275 Ill. Dec. 838"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sykes v. Anderson",
          "cluster_id": 178987,
          "cite": [
            "625 F.3d 294",
            "2010 U.S. App. LEXIS 23204",
            "2010 WL 4453313"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sean Howell",
          "cluster_id": 771006,
          "cite": [
            "231 F.3d 615",
            "55 Fed. R. Serv. 1314",
            "2000 Daily Journal DAR 11612",
            "2000 Cal. Daily Op. Serv. 8736",
            "2000 U.S. App. LEXIS 27067",
            "2000 WL 1617019"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sullivan",
          "cluster_id": 2973136,
          "cite": [
            "431 F.3d 976",
            "2005 U.S. App. LEXIS 28073",
            "2005 WL 3466534"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyron Brown v. Lee Lucas",
          "cluster_id": 2675935,
          "cite": [
            "753 F.3d 606",
            "2014 WL 2198419",
            "2014 U.S. App. LEXIS 9771"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joe D'Ambrosio v. Carmen Marino",
          "cluster_id": 2658128,
          "cite": [
            "747 F.3d 378",
            "2014 WL 1243792",
            "2014 U.S. App. LEXIS 5588"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Linette Perez, United States of America v. Juancho Alcantera, United States of America v. Edmundo Batoon",
          "cluster_id": 776532,
          "cite": [
            "280 F.3d 318",
            "2002 WL 171241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kwame Ajamu v. City of Cleveland",
          "cluster_id": 4621394,
          "cite": [
            "925 F.3d 793"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard A. Pelullo, United States of America v. Leonard A. Pelullo",
          "cluster_id": 789362,
          "cite": [
            "399 F.3d 197",
            "2005 WL 433589"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LaMar",
          "cluster_id": 10686381,
          "cite": [
            "2002 Ohio 2128",
            "95 Ohio St. 3d 181"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aldrich v. Bock",
          "cluster_id": 2453961,
          "cite": [
            "327 F. Supp. 2d 743",
            "2004 U.S. Dist. LEXIS 14683",
            "2004 WL 1682907"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ortiz v. Barkley",
          "cluster_id": 1810562,
          "cite": [
            "558 F. Supp. 2d 444",
            "2008 U.S. Dist. LEXIS 43653",
            "2008 WL 2266313"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Cain",
          "cluster_id": 620666,
          "cite": [
            "181 L. Ed. 2d 571",
            "132 S. Ct. 627",
            "565 U.S. 73",
            "2012 U.S. LEXIS 576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunlap v. State",
          "cluster_id": 2508569,
          "cite": [
            "106 P.3d 376",
            "141 Idaho 50",
            "2004 Ida. LEXIS 194"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Spotz",
          "cluster_id": 2074443,
          "cite": [
            "896 A.2d 1191",
            "587 Pa. 1",
            "2006 Pa. LEXIS 659"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Lesko",
          "cluster_id": 2422962,
          "cite": [
            "15 A.3d 345",
            "609 Pa. 128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Albarran",
          "cluster_id": 2276132,
          "cite": [
            "57 Cal. Rptr. 3d 92",
            "149 Cal. App. 4th 214",
            "2007 Cal. Daily Op. Serv. 3495",
            "2007 Daily Journal DAR 4378",
            "2007 Cal. App. LEXIS 486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Chavez",
          "cluster_id": 2333628,
          "cite": [
            "213 S.W.3d 320",
            "2006 Tex. Crim. App. LEXIS 2294",
            "2006 WL 3391014"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118307 OR 9433839 OR 9433840) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQ1MDU2MDAwMDAwJnM9NjM1ODAyNCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118307+OR+9433839+OR+9433840%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118307 OR 9433839 OR 9433840)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yODYmcz03OTE5NDgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118307+OR+9433839+OR+9433840%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118307 OR 9433839 OR 9433840)",
        "reviewed": 146,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 146,
        "triage_read": 4,
        "triage_snippet_classified": 142
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118307 OR 9433839 OR 9433840)",
    "indexed_citing_opinions": 2221,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118307,
        "count": 1865,
        "count_source": "search"
      },
      {
        "opinion_id": 9433839,
        "count": 379,
        "count_source": "search"
      },
      {
        "opinion_id": 9433840,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4395,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/strickler-v-greene.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MzM5OTImcz0xMDYyNDU0NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118307+OR+9433839+OR+9433840%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118307,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 104321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 104547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 106440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 109380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 110797,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 118048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 118130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 118205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 683528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 1219071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 1348258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 1385494,
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
    "date_created": "2026-07-05T21:09:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:09:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:09:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:12:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:09:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Strickler v. Greene (truncated)

```
<div>
<center><b><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">527 U.S. 263</a></span> (1999)</b></center>
<center><h1>STRICKLER<br>
v.<br>
GREENE, WARDEN</h1></center>
<center>No. 98-5864.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 3, 1999.</center>
<center>Decided June 17, 1999.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FOURTH CIRCUIT
<p><span class="star-pagination">*264</span> <span class="star-pagination">*265</span> Stevens, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Scalia, Ginsburg, and Breyer, JJ., joined in full, in which Kennedy and Souter, JJ., joined as to Part III, and in which Thomas, J., joined as to Parts I and IV. Souter, J., filed an opinion concurring in part and dissenting in part, in which Kennedy, J., joined as to Part II, <i>post,</i> p. 296.</p>
<p><i>Miguel A. Estrada</i> argued the cause for petitioner. With him on the briefs were <i>Barbara L. Hartung, Mark E. Olive,</i>  and <i>John H. Blume.</i> </p>
<p><i>Pamela A. Rumpz,</i> Assistant Attorney General of Virginia, argued the cause for respondent. With her on the brief was <i>Mark L. Earley,</i> Attorney General.<sup>[*]</sup></p>
<p>Justice Stevens delivered the opinion of the Court.<sup>[]</sup></p>
<p>The District Court for the Eastern District of Virginia granted petitioner's application for a writ of habeas corpus and vacated his capital murder conviction and death sentence on the grounds that the Commonwealth had failed to disclose important exculpatory evidence and that petitioner had not, in consequence, received a fair trial. The Court of Appeals for the Fourth Circuit reversed because petitioner had not raised his constitutional claim at his trial or in state collateral proceedings. In addition, the Fourth Circuit concluded that petitioner's claim was, "in any event, without merit." App. 418, n. 8.<sup>[1]</sup> Finding the legal question presented by this <span class="star-pagination">*266</span> case considerably more difficult than the Fourth Circuit, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./525/809/">525 U. S. 809</a></span> (1998), to consider (1) whether the Commonwealth violated <i>Brady</i> v. <i>Maryland,</i>  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), and its progeny; (2) whether there was an acceptable "cause" for petitioner's failure to raise this claim in state court; and (3), if so, whether he suffered prejudice sufficient to excuse his procedural default.</p>
<p></p>
<h2>I</h2>
<p>In the early evening of January 5, 1990, Leanne Whitlock, an African-American sophomore at James Madison University, was abducted from a local shopping center and robbed and murdered. In separate trials, both petitioner and Ronald Henderson were convicted of all three offenses. Henderson was convicted of first-degree murder, a noncapital offense, whereas petitioner was convicted of capital murder and sentenced to death.<sup>[2]</sup></p>
<p>At both trials, a woman named Anne Stoltzfus testified in vivid detail about Whitlock's abduction. The exculpatory material that petitioner claims should have been disclosed before trial includes documents prepared by Stoltzfus, and notes of interviews with her, that impeach significant portions of her testimony. We begin, however, by noting that, even without the Stoltzfus testimony, the evidence in the record was sufficient to establish petitioner's guilt on the murder charge. Whether petitioner would have been convicted of capital murder and received the death sentence if she had not testified, or if she had been sufficiently impeached, is less clear. To put the question in context, we review the trial testimony at some length.</p>
<p><i>The Testimony at Trial</i> </p>
<p>At about 4:30 p.m. on January 5, 1990, Whitlock borrowed a 1986 blue Mercury Lynx from her boyfriend, John Dean, <span class="star-pagination">*267</span> who worked in the Valley Shopping Mall in Harrisonburg, Virginia. At about 6:30 or 6:45 p.m., she left her apartment, intending to return the car to Dean at the mall. She did not return the car and was not again seen alive by any of her friends or family.</p>
<p>Petitioner's mother testified that she had driven petitioner and Henderson to Harrisonburg on January 5. She also testified that petitioner always carried a hunting knife that had belonged to his father. Two witnesses, a friend of Henderson's and a security guard, saw petitioner and Henderson at the mall that afternoon. The security guard was informed around 3:30 p.m. that two men, one of whom she identified at trial as petitioner, were attempting to steal a car in the parking lot. She had them under observation during the remainder of the afternoon but lost sight of them at about 6:45.</p>
<p>At approximately 7:30 p.m., a witness named Kurt Massie saw the blue Lynx at a location in Augusta County about 25 miles from Harrisonburg and a short distance from the cornfield where Whitlock's body was later found. Massie identified petitioner as the driver of the vehicle; he also saw a white woman in the front seat and another man in the back. Massie noticed that the car was muddy, and that it turned off Route 340 onto a dirt road.</p>
<p>At about 8 p.m., another witness saw the Lynx at Buddy's Market, with two men sitting in the front seat. The witness did not see anyone else in the car. At approximately 9 p.m., petitioner and Henderson arrived at Dice's Inn, a bar in Staunton, Virginia, where they stayed for about four or five hours. They danced with several women, including four prosecution witnesses: Donna Kay Tudor, Nancy Simmons, Debra Sievers, and Carolyn Brown. While there, Henderson gave Nancy Simmons a watch that had belonged to Whitlock. Petitioner spent most of his time with Tudor, who was later arrested for grand larceny based on her possession of the blue Lynx.</p>
<p><span class="star-pagination">*268</span> These four women all testified that Tudor had arrived at Dice's at about 8 p.m. Three of them noticed nothing unusual about petitioner's appearance, but Tudor saw some blood on his jeans and a cut on his knuckle. Tudor also testified that she, Henderson, and petitioner left Dice's together after it closed to search for marijuana. Henderson was driving the blue Lynx, and petitioner and Tudor rode in back. Tudor related that petitioner was leaning toward Henderson and talking with him; she overheard a crude conversation that could reasonably be interpreted as describing the assault and murder of a black person with a "rock crusher." Tudor stated that petitioner made a statement that implied that he had killed someone, so the person "wouldn't give him no more trouble." App. 99. Tudor testified that while she, petitioner, and Henderson were driving around, petitioner took out his knife and threatened to stab Henderson because he was driving recklessly. Petitioner then began driving.</p>
<p>At about 4:30 or 5 a.m. on January 6, petitioner drove Henderson to Kenneth Workman's apartment in Timberville.<sup>[3]</sup> Henderson went inside to get something, and petitioner and Tudor drove off without waiting for him. Workman testified that Henderson had blood on his pants and stated he had killed a black person.</p>
<p>Petitioner and Tudor then drove to a motel in Blue Ridge. A day or two later they went to Virginia Beach, where they spent the rest of the week. Petitioner gave Tudor pearl earrings that Whitlock had been wearing when she was last seen. Tudor saw Whitlock's driver's license and bank card in the glove compartment of the car. Tudor testified that petitioner unsuccessfully attempted to use Whitlock's bank card when they were in Virginia Beach.</p>
<p>When petitioner and Tudor returned to Augusta County, they abandoned the blue Lynx. On January 11, the police identified the car as Dean's, and found petitioner's and Tudor's <span class="star-pagination">*269</span> fingerprints on both the inside and the outside of the car. They also found shoe impressions that matched the soles of shoes belonging to petitioner. Inside the car, they retrieved a jacket that contained identification papers belonging to Henderson.</p>
<p>The police also recovered a bag at petitioner's mother's house that Tudor testified she and petitioner had left when they returned from Virginia Beach. The bag contained, among other items, three identification cards belonging to Whitlock and a black "tank top" shirt that was later found to have human blood and semen stains on it. Tr. 707.</p>
<p>On January 13, a farmer called the police to advise them that he had found Henderson's wallet; a search of the area led to the discovery of Whitlock's frozen, nude, and battered body. A 69-pound rock, spotted with blood, lay nearby. Forensic evidence indicated that Whitlock's death was caused by "multiple blunt force injuries to the head." App. 109. The location of the rock and the human blood on the rock suggested that it had been used to inflict these injuries. Based on the contents of Whitlock's stomach, the medical examiner determined that she died fewer than six hours after she had last eaten.<sup>[4]</sup></p>
<p>A number of Caucasian hair samples were found at the scene, three of which were probably petitioner's. Given the weight of the rock, the prosecution argued that one of the killers must have held the victim down while the other struck her with the murder weapon.</p>
<p>Donna Tudor's estranged husband, Jay Tudor, was called by the defense and testified that in March she had told him that she was present at the murder scene and that petitioner did not participate in the murder. Jay Tudor's testimony was inconsistent in several respects with that of other witnesses. For example, he testified that several days elapsed <span class="star-pagination">*270</span> between the time that petitioner, Henderson, and Donna Tudor picked up Whitlock and the time of Whitlock's murder. <i>Anne Stoltzfus' Testimony</i> </p>
<p>Anne Stoltzfus testified that on two occasions on January 5 she saw petitioner, Henderson, and a blonde girl inside the Harrisonburg mall, and that she later witnessed their abduction of Whitlock in the parking lot. She did not call the police, but a week and a half after the incident she discussed it with classmates at James Madison University, where both she and Whitlock were students. One of them called the police. The next night a detective visited her, and the following morning she went to the police station and told her story to Detective Claytor, a member of the Harrisonburg City Police Department. Detective Claytor showed her photographs of possible suspects, and she identified petitioner and Henderson "with absolute certainty" but stated that she had a slight reservation about her identification of the blonde woman. <i>Id.,</i> at 56.</p>
<p>At trial, Stoltzfus testified that, at about 6 p.m. on January 5, she and her 14-year-old daughter were in the Music Land store in the mall looking for a compact disc. While she was waiting for assistance from a clerk, petitioner, whom she described as "Mountain Man," and the blonde girl entered.<sup>[5]</sup><span class="star-pagination">*271</span> Because petitioner was "revved up" and "very impatient," she was frightened and backed up, bumping into Henderson (whom she called "Shy Guy"), and thought she felt something hard in the pocket of his coat. <i>Id.,</i> at 36-37.</p>
<p>Stoltzfus left the store, intending to return later. At about 6:45, while heading back toward Music Land, she again encountered the threesome: "Shy Guy" walking by himself, followed by the girl, and then "Mountain Man" yelling "Donna, Donna, Donna." The girl bumped into Stoltzfus and then asked for directions to the bus stop.<sup>[6]</sup> The three then left.</p>
<p>At first Stoltzfus tried to follow them because of her concern about petitioner's behavior, but she "lost him" and then headed back to Music Land. The clerk had not returned, so she and her daughter went to their car. While driving to another store, they saw a shiny dark blue car. The driver was "beautiful," "well dressed and she was happy, she was singing . . . ." <i>Id.,</i> at 41. When the blue car was stopped behind a minivan at a stop sign, Stoltzfus saw petitioner for the third time.</p>
<p>She testified:</p>
<blockquote>"`Mountain Man' came tearing out of the Mall entrance door and went up to the driver of the van and . . . was just really mad and ran back and banged on back of the backside of the van and then went back to the Mall entrance wall where `Shy Guy' and `Blonde Girl' was standing . . . . [T]hen we left [and before the van and a white pickup truck could turn] `Mountain Man' came out again . . . ." <i>Id.,</i> at 42-43.</blockquote>
<p>After first going to the passenger side of the pickup truck, petitioner came back to the black girl's car, "pounded on" the passenger window, shook the car, yanked the door open and jumped in. When he motioned for "Blonde Girl" and "Shy <span class="star-pagination">*272</span> Guy" to get in, the driver stepped on the gas and "just laid on the horn" but she could not go because there were people walking in front of the car. The horn "blew a long time" and petitioner</p>
<blockquote>"started hitting her . . . on the left shoulder, her right shoulder and then it looked like to me that he started hitting her on the head and I was, I just became concerned and upset. So I beeped, honked my horn and then she stopped honking the horn and he stopped hitting her and opened the door again and the `Blonde Girl' got in the back and `Shy Guy' followed and got behind him." <i>Id.,</i> at 44-45.</blockquote>
<p>Stoltzfus pulled her car up parallel to the blue car, got out for a moment, got back in, and leaned over to ask repeatedly if the other driver was "O.K." The driver looked "frozen" and mouthed an inaudible response. Stoltzfus started to drive away and then realized "the only word that it could possibly be, was help." <i>Id.,</i> at 47. The blue car then drove slowly around her, went over the curb with its horn honking, and headed out of the mall. Stoltzfus briefly followed, told her daughter to write the license number on a "3x4 [inch] index card,"<sup>[7]</sup> and then left for home because she had an empty gas tank and "three kids at home waiting for supper." <i>Id.,</i> at 48-49.</p>
<p>At trial Stoltzfus identified Whitlock from a picture as the driver of the car and pointed to petitioner as "Mountain Man." When asked if pretrial publicity about the murder had influenced her identification, Stoltzfus replied "absolutely not." She explained:</p>
<blockquote>"[F]irst of all, I have an exceptionally good memory. I had very close contact with [petitioner] and he made an <span class="star-pagination">*273</span> emotional impression with me because of his behavior and I, he caught my attention and I paid attention. So I have absolutely no doubt of my identification." <i>Id.,</i>  at 58.</blockquote>
<p>The Commonwealth did not produce any other witnesses to the abduction. Stoltzfus' daughter did not testify.</p>
<p><i>The Stoltzfus Documents</i> </p>
<p>The materials that provide the basis of petitioner's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  claim consist of notes taken by Detective Claytor during his interviews with Stoltzfus, and letters written by Stoltzfus to Claytor. They cast serious doubt on Stoltzfus' confident assertion of her "exceptionally good memory." Because the content of the documents is critical to petitioner's procedural and substantive claims, we summarize their content.</p>
<p>Exhibit 1<sup>[8]</sup> is a handwritten note prepared by Detective Claytor after his first interview with Stoltzfus on January 19, 1990, just two weeks after the crime. The note indicates that she could not identify the black female victim. The only person Stoltzfus apparently could identify at this time was the white female. <i>Id.,</i> at 306.</p>
<p>Exhibit 2 is a document prepared by Detective Claytor some time after February 1. It contains a summary of his interviews with Stoltzfus conducted on January 19 and January 20, 1990.<sup>[9]</sup> At that time "she was not sure whether she could identify the white males but felt sure she could identify the white female."</p>
<p><span class="star-pagination">*274</span> Exhibit 3 is entitled "Observations" and includes a summary of the abduction.</p>
<p>Exhibit 4 is a letter written by Stoltzfus to Claytor three days after their first interview "to clarify some of my confusion for you." The letter states that she had not remembered being at the mall, but that her daughter had helped jog her memory. Her description of the abduction includes the comment: "I have a very vague memory that I'm not sure of. It seems as if the wild guy that I saw had come running through the door and up to a bus as the bus was pulling off. . . . Then the guy I saw came running up to the black girl's window. Were those 2 memories the same person?" <i>Id.,</i> at 316. In a postscript she noted that her daughter "doesn't remember seeing the 3 people get into the black girl's car . . . ." <i>Ibid.</i> </p>
<p>Exhibit 5 is a note to Claytor captioned "My Impressions of `The Car,' " which contains three paragraphs describing the size of the car and comparing it with Stoltzfus' Volkswagen Rabbit, but not mentioning the license plate number that she vividly recalled at the trial. <i>Id.,</i> at 317-318.</p>
<p>Exhibit 6 is a brief note from Stoltzfus to Claytor dated January 25, 1990, stating that after spending several hours with John Dean, Whitlock's boyfriend, "looking at current photos," she had identified Whitlock "beyond a shadow of a doubt."<sup>[10]</sup><i>Id.,</i> at 318. The District Court noted that by the time of trial her identification had been expanded to include a description of her clothing and her appearance as a college kid who was "singing" and "happy." <i>Id.,</i> at 387-388.</p>
<p>Exhibit 7 is a letter from Stoltzfus to Detective Claytor, dated January 16, 1990, in which she thanks him for his "patience with my sometimes muddled memories." She states that if the student at school had not called the police, "I never would have made any of the associations that you helped me make." <i>Id.,</i> at 321.</p>
<p><span class="star-pagination">*275</span> In Exhibit 8, which is undated and summarizes the events described in her trial testimony, Stoltzfus commented:</p>
<blockquote>"So where is the 3x4 card? . . . It would have been very nice if I could have remembered all this at the time and had simply gone to the police with the information. But I totally wrote this off as a trivial episode of college kids carrying on and proceeded with my own full-time college load at JMU. . . . Monday, January 15th. I was cleaning out my car and found the 3x4 card. I tore it into little pieces and put it in the bottom of a trash bag." <i>Id.,</i> at 326.</blockquote>
<p>There is a dispute between the parties over whether petitioner's counsel saw Exhibits 2, 7, and 8 before trial. The prosecuting attorney conceded that he himself never saw Exhibits 1, 3, 4, 5, and 6 until long after petitioner's trial, and they were not in the file he made available to petitioner.<sup>[11]</sup> For purposes of this case, therefore, we assume that petitioner proceeded to trial without having seen Exhibits 1, 3, 4, 5, and 6.<sup>[12]</sup></p>
<p><span class="star-pagination">*276</span> <i>State Proceedings</i> </p>
<p>Petitioner was tried in Augusta County, where Whitlock's body was found, on charges of capital murder, robbery, and abduction. Because the prosecutor maintained an open file policy, which gave petitioner's counsel access to all of the evidence in the Augusta County prosecutor's files,<sup>[13]</sup> petitioner's counsel did not file a pretrial motion for discovery of possible exculpatory evidence.<sup>[14]</sup> In closing argument, petitioner's lawyer effectively conceded that the evidence was sufficient to support the robbery and abduction charges, as well as the lesser offense of first-degree murder, but argued that the evidence was insufficient to prove that petitioner was guilty of capital murder. <i>Id.,</i> at 192-193.</p>
<p>The judge instructed the jury that petitioner could be found guilty of the capital charge if the evidence established beyond a reasonable doubt that he "jointly participated in the fatal beating" and "was an active and immediate participant <span class="star-pagination">*277</span> in the act or acts that caused the victim's death." <i>Id.,</i>  at 160-161. The jury found petitioner guilty of abduction, robbery, and capital murder. <i>Id.,</i> at 200-201. After listening to testimony and arguments presented during the sentencing phase, the jury made findings of "vileness" and "future dangerousness," and unanimously recommended the death sentence that the judge later imposed.</p>
<p>The Virginia Supreme Court affirmed the conviction and sentence. <i>Strickler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/" aria-description="Citation for case: Strickler v. Commonwealth">241 Va. 482</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d 227</a></span> (1991). It held that the trial court had properly instructed the jury on the "joint perpetrator" theory of capital murder and that the evidence, viewed most favorably in support of the verdict, amply supported the prosecution's theory that both petitioner and Henderson were active participants in the actual killing.<sup>[15]</sup></p>
<p>In December 1991, the Augusta County Circuit Court appointed new counsel to represent petitioner in state habeas corpus proceedings. State habeas counsel advanced an <span class="star-pagination">*278</span> ineffective-assistance-of-counsel claim based, in part, on trial counsel's failure to file a motion under <i>Brady</i> v. <i>Maryland,</i>  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), "to have the Commonwealth disclose to the defense all exculpatory evidence known to itor in its possession." App. 205-206. In answer to that claim, the Commonwealth asserted that such a motion was unnecessary because the prosecutor had maintained an open file policy.<sup>[16]</sup> The Circuit Court dismissed the petition, and the State Supreme Court affirmed. <i>Strickler</i> v. <i>Murray,</i> <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/" aria-description="Citation for case: Strickler v. Murray">249 Va. 120</a></span>, <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/" aria-description="Citation for case: Strickler v. Murray">452 S. E. 2d 648</a></span> (1995).</p>
<p><i>Federal Habeas Corpus Proceedings</i> </p>
<p>In March 1996, petitioner filed a federal habeas corpus petition in the Eastern District of Virginia. The District Court entered a sealed, <i>ex parte</i> order granting petitioner's counsel the right to examine and to copy all of the police and prosecution files in the case. Record, Doc. No. 20. That order led to petitioner's counsel's first examination of the Stoltzfus materials, described <i>supra,</i> at 273-275.</p>
<p>Based on the discovery of those exhibits, petitioner for the first time raised a direct claim that his conviction was invalid because the prosecution had failed to comply with the rule of <i>Brady</i> v. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Maryland</a></span></i><i>.</i> The District Court granted the Commonwealth's motion to dismiss all claims except for petitioner's contention that the Commonwealth violated <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i>  that he received ineffective assistance of counsel,<sup>[17]</sup> and that he was denied due process of law under the Fifth and Fourteenth Amendments. In its order denying the Commonwealth's motion to dismiss, the District Court found that petitioner had "demonstrated cause for his failure to raise this claim earlier [because] [d]efense counsel had no independent access to this material and the Commonwealth repeatedly withheld it throughout Petitioner's state habeas proceeding." App. 287.</p>
<p><span class="star-pagination">*279</span> After reviewing the Stoltzfus materials, and making the assumption that the three disputed exhibits had been available to the defense, the District Court concluded that the failure to disclose the other five was sufficiently prejudicial to undermine confidence in the jury's verdict. <i>Id.,</i> at 396. It granted summary judgment to petitioner and granted the writ.</p>
<p>The Court of Appeals vacated in part and remanded. It held that petitioner's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim was procedurally defaulted because the factual basis for the claim was available to him at the time he filed his state habeas petition. Given that he knew that Stoltzfus had been interviewed by Harrisonburg police officers, the court opined that "reasonably competent counsel would have sought discovery in state court" of the police files, and that in response to this "simple request, it is likely the state court would have ordered the production of the files." App. 421. Therefore, the Court of Appeals reasoned, it could not address the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim unless petitioner could demonstrate both cause and actual prejudice.</p>
<p>Under Fourth Circuit precedent a party "cannot establish cause to excuse his default if he should have known of such claims through the exercise of reasonable diligence." App. 423 (citing <i>Stockton</i> v. <i>Murray,</i> <span class="citation" data-id="683528"><a href="/opinion/683528/dennis-waldon-stockton-v-edward-murray/#925" aria-description="Citation for case: Dennis Waldon Stockton v. Edward Murray">41 F. 3d 920, 925</a></span> (1994)). Having already decided that the claim was available to reasonably competent counsel, the Fourth Circuit stated that the basis for finding procedural default also foreclosed a finding of cause. Moreover, the Court of Appeals reasoned, petitioner could not fault his trial lawyers' failure to make a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim because they reasonably relied on the prosecutor's open file policy. App. 423-424.<sup>[18]</sup></p>
<p>As an alternative basis for decision, the Court of Appeals also held that petitioner could not establish prejudice because <span class="star-pagination">*280</span> "the Stoltzfus materials would have provided little or no help .. . in either the guilt or sentencing phases of the trial." <i>Id.,</i> at 425. With respect to guilt, the court noted that Stoltzfus' testimony was not relevant to petitioner's argument that he was only guilty of first-degree murder rather than capital murder because Henderson, rather than he, actually killed Whitlock. With respect to sentencing, the court concluded that her testimony "was of no import" because the findings of future dangerousness and vileness rested on other evidence. Finally, the court noted that even if it could get beyond the procedural default, the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim would fail on the merits because of the absence of prejudice. App. 425, n. 11. The Court of Appeals, therefore, reversed the District Court's judgment and remanded the case with instructions to dismiss the petition.</p>
<p></p>
<h2>II</h2>
<p>The first question that our order granting certiorari directed the parties to address is whether the Commonwealth violated the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> rule. We begin our analysis by identifying the essential components of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation.</p>
<p>In <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> this Court held "that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. We have since held that the duty to disclose such evidence is applicable even though there has been no request by the accused, <i>United States</i> v. <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#107" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 107</a></span> (1976), and that the duty encompasses impeachment evidence as well as exculpatory evidence, <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#676" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 676</a></span> (1985). Such evidence is material "if there is a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different." <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley"><i>Id.,</i> at 682</a></span>; see also <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#433" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 433-434</a></span> (1995). Moreover, the rule encompasses evidence "known only to police <span class="star-pagination">*281</span> investigators and not to the prosecutor." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#438" aria-description="Citation for case: Kyles v. Whitley"><i>Id.,</i> at 438</a></span>. In order to comply with <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> therefore, "the individual prosecutor has a duty to learn of any favorable evidence known to the others acting on the government's behalf in this case, including the police." <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#437" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 437</a></span>.</p>
<p>These cases, together with earlier cases condemning the knowing use of perjured testimony,<sup>[19]</sup> illustrate the special role played by the American prosecutor in the search for truth in criminal trials. Within the federal system, for example, we have said that the United States Attorney is "the representative not of an ordinary party to a controversy, but of a sovereignty whose obligation to govern impartially is as compelling as its obligation to govern at all; and whose interest, therefore, in a criminal prosecution is not that it shall win a case, but that justice shall be done." <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935).</p>
<p>This special status explains both the basis for the prosecution's broad duty of disclosure and our conclusion that not every violation of that duty necessarily establishes that the outcome was unjust. Thus the term "<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> violation" is sometimes used to refer to any breach of the broad obligation to disclose exculpatory evidence<sup>[20]</sup>that is, to any suppression of so-called "<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> material"although, strictly speaking, there is never a real "<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> violation" unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict. There are three components of a true <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  violation: The evidence at issue must be favorable to the accused, <span class="star-pagination">*282</span> either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadvertently; and prejudice must have ensued.</p>
<p>Two of those components are unquestionably established by the record in this case. The contrast between (a) the terrifying incident that Stoltzfus confidently described in her testimony and (b) her initial perception of that event "as a trivial episode of college kids carrying on" that her daughter did not even notice, suffices to establish the impeaching character of the undisclosed documents.<sup>[21]</sup> Moreover, with respect to at least five of those documents, there is no dispute about the fact that they were known to the Commonwealth but not disclosed to trial counsel. It is the third componentwhether petitioner has established the prejudice necessary to satisfy the "materiality" inquirythat is the most difficult element of the claimed <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation in this case.</p>
<p>Because petitioner acknowledges that his <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim is procedurally defaulted, we must first decide whether that default is excused by an adequate showing of cause and prejudice. In this case, cause and prejudice parallel two of the three components of the alleged <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation itself. The suppression of the Stoltzfus documents constitutes one of the causes for the failure to assert a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in the state courts, and unless those documents were "material" for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes, their suppression did not give rise to sufficient prejudice to overcome the procedural default.</p>
<p></p>
<h2>III</h2>
<p>Respondent expressly disavows any reliance on the fact that petitioner's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim was not raised at trial. Brief <span class="star-pagination">*283</span> for Respondent 17-18, n. 6. He states that the Commonwealth has consistently argued "that the claim is defaulted because it could have been raised on state habeas corpus through the exercise of due diligence, but was not." <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Ibid.</a></span></i>  Despite this concession, it is appropriate to begin the analysis of the "cause" issue by explaining why petitioner's reasons for failing to raise his <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim at trial are acceptable under this Court's cases.</p>
<p>Three factors explain why trial counsel did not advance this claim: The documents were suppressed by the Commonwealth; the prosecutor maintained an open file policy;<sup>[22]</sup> and trial counsel were not aware of the factual basis for the claim. The first and second factors<i>i. e.,</i> the nondisclosure and the open file policyare both fairly characterized as conduct attributable to the Commonwealth that impeded trial counsel's access to the factual basis for making a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  claim.<sup>[23]</sup> As we explained in <i>Murray</i> v. <i>Carrier,</i> <span class="citation" data-id="9430624"><a href="/opinion/111727/murray-v-carrier/#488" aria-description="Citation for case: Murray v. Carrier">477 U. S. 478, 488</a></span> (1986), it is just such factors that ordinarily establish the existence of cause for a procedural default.<sup>[24]</sup></p>
<p><span class="star-pagination">*284</span> If it was reasonable for trial counsel to rely on, not just the presumption that the prosecutor would fully perform his duty to disclose all exculpatory materials, but also the implicit representation that such materials would be included in the open files tendered to defense counsel for their examination, we think such reliance by counsel appointed to represent petitioner in state habeas proceedings was equally reasonable. Indeed, in <i>Murray</i> we expressly noted that "the standard for cause should not vary depending on the timing of a procedural default." <i>Id.,</i> at 491.</p>
<p>Respondent contends, however, that the prosecution's maintenance of an open file policy that did not include all it was purported to contain is irrelevant because the factual basis for the assertion of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim was available to state habeas counsel. He presses two factors to support this assertion. First, he argues that an examination of Stoltzfus' trial testimony,<sup>[25]</sup> as well as a letter published in a local newspaper,<sup>[26]</sup> made it clear that she had had several interviews with Detective Claytor. Second, the fact that the Federal District Court entered an order allowing discovery of the Harrisonburg police files indicates that diligent counsel could <span class="star-pagination">*285</span> have obtained a similar order from the state court. We find neither factor persuasive.</p>
<p>Although it is true that petitioner's lawyersboth at trial and in post-trial proceedingsmust have known that Stoltzfus had had multiple interviews with the police, it by no means follows that they would have known that records pertaining to those interviews, or that the notes that Stoltzfus sent to the detective, existed and had been suppressed.<sup>[27]</sup> Indeed, if respondent is correct that Exhibits 2, 7, and 8 were in the prosecutor's "open file," it is especially unlikely that counsel would have suspected that additional impeaching evidence was being withheld. The prosecutor must have known about the newspaper articles and Stoltzfus' meetings with Claytor, yet he did not believe that his prosecution file was incomplete.</p>
<p>Furthermore, the fact that the District Court entered a broad discovery order even before federal habeas counsel had advanced a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim does not demonstrate that a state court also would have done so.<sup>[28]</sup> Indeed, as we understand Virginia law and respondent's position, petitioner would not have been entitled to such discovery in state habeas <span class="star-pagination">*286</span> proceedings without a showing of good cause.<sup>[29]</sup> Even pursuant to the broader discovery provisions afforded at trial, petitioner would not have had access to these materials under Virginia law, except as modified by <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i><sup>[30]</sup> Mere speculation that some exculpatory material may have been withheld is unlikely to establish good cause for a discovery request on collateral review. Nor, in our opinion, should such suspicion suffice to impose a duty on counsel to advance a claim for which they have no evidentiary support. Proper respect for state procedures counsels against a requirement that all possible claims be raised in state collateral proceedings, even when no known facts support them. The presumption, well established by "`tradition and experience,' " that prosecutors have fully "`discharged their official duties,' " <i>United States</i> v. <i>Mezzanatto,</i> <span class="citation" data-id="117889"><a href="/opinion/117889/united-states-v-mezzanatto/#210" aria-description="Citation for case: United States v. Mezzanatto">513 U. S. 196, 210</a></span> (1995), is inconsistent with the novel suggestion that conscientious defense counsel have a procedural obligation to assert constitutional <span class="star-pagination">*287</span> error on the basis of mere suspicion that some prosecutorial misstep may have occurred.</p>
<p>Respondent's position on the "cause" issue is particularly weak in this case because the state habeas proceedings confirmed petitioner's justification for his failure to raise a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. As already noted, when he alleged that trial counsel had been incompetent because they had not advanced such a claim, the warden responded by pointing out that there was no need for counsel to do so because they "were voluntarily given full disclosure of everything known to the government."<sup>[31]</sup> Given that representation, petitioner had no basis for believing the Commonwealth had failed to comply with <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> at trial.<sup>[32]</sup></p>
<p>Respondent also argues that our decisions in <i>Gray</i> v. <i>Netherland,</i> <span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/" aria-description="Citation for case: Gray v. Netherland">518 U. S. 152</a></span> (1996), and <i>McCleskey</i> v. <i>Zant,</i> <span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/" aria-description="Citation for case: McCleskey v. Zant">499 U. S. 467</a></span> (1991), preclude the conclusion that the cause for petitioner's default was adequate. In both of those cases, however, the petitioner was previously aware of the factual basis for his claim but failed to raise it earlier. See <i>Gray,</i> <span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/#161" aria-description="Citation for case: Gray v. Netherland">518 U. S., at 161</a></span>; <i>McCleskey,</i> <span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/#498" aria-description="Citation for case: McCleskey v. Zant">499 U. S., at 498-499</a></span>. In the context of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, a defendant cannot conduct the "reasonable <span class="star-pagination">*288</span> and diligent investigation" mandated by <i><span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/" aria-description="Citation for case: McCleskey v. Zant">McCleskey</a></span></i>  to preclude a finding of procedural default when the evidence is in the hands of the State.<sup>[33]</sup></p>
<p>The controlling precedents on "cause" are <i>Murray</i> v. <i>Carrier,</i> <span class="citation" data-id="9430624"><a href="/opinion/111727/murray-v-carrier/#488" aria-description="Citation for case: Murray v. Carrier">477 U. S., at 488</a></span>, and <i>Amadeo</i> v. <i>Zant,</i> <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/" aria-description="Citation for case: Amadeo v. Zant">486 U. S. 214</a></span> (1988). As we explained in the latter case:</p>
<blockquote>"If the District Attorney's memorandum was not reasonably discoverable because it was concealed by Putnam County officials, and if that concealment, rather than tactical considerations, was the reason for the failure of petitioner's lawyers to raise the jury challenge in the trial court, then petitioner established ample cause to excuse his procedural default under this Court's precedents." <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/#222" aria-description="Citation for case: Amadeo v. Zant"><i>Id.,</i> at 222</a></span>.<sup>[34]</sup></blockquote>
<p>There is no suggestion that tactical considerations played any role in petitioner's failure to raise his <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in state court. Moreover, under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> an inadvertent nondisclosure has the same impact on the fairness of the proceedings as deliberate concealment. "If the suppression of evidence results in constitutional error, it is because of the character of the evidence, not the character of the prosecutor." <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#110" aria-description="Citation for case: United States v. Agurs">427 U. S., at 110</a></span>.</p>
<p><span class="star-pagination">*289</span> In summary, petitioner has established cause for failing to raise a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim prior to federal habeas because (a) the prosecution withheld exculpatory evidence; (b) petitioner reasonably relied on the prosecution's open file policy as fulfilling the prosecution's duty to disclose such evidence; and (c) the Commonwealth confirmed petitioner's reliance on the open file policy by asserting during state habeas proceedings that petitioner had already received "everything known to the government."<sup>[35]</sup> We need not decide in this case whether any one or two of these factors would be sufficient to constitute cause, since the combination of all three surely suffices.</p>
<p></p>
<h2>IV</h2>
<p>The differing judgments of the District Court and the Court of Appeals attest to the difficulty of resolving the issue of prejudice. Unlike the Fourth Circuit, we do not believe that "the Stolzfus <i>[sic]</i> materials would have provided little or no help to Strickler in either the guilt or sentencing phases of the trial." App. 425. Without a doubt, Stoltzfus' testimony was prejudicial in the sense that it made petitioner's conviction more likely than if she had not testified, and discrediting her testimony might have changed the outcome of the trial.</p>
<p>That, however, is not the standard that petitioner must satisfy in order to obtain relief. He must convince us that "there is a reasonable probability" that the result of the trial would have been different if the suppressed documents had been disclosed to the defense. As we stressed in <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Kyles</a></span>:</i>  "[T]he adjective is important. The question is not whether the defendant would more likely than not have received a different verdict with the evidence, but whether in its absence <span class="star-pagination">*290</span> he received a fair trial, understood as a trial resulting in a verdict worthy of confidence." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 434</a></span>.</p>
<p>The Court of Appeals' negative answer to that question rested on its conclusion that, without considering Stoltzfus' testimony, the record contained ample, independent evidence of guilt, as well as evidence sufficient to support the findings of vileness and future dangerousness that warranted the imposition of the death penalty. The standard used by that court was incorrect. As we made clear in <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Kyles</a></span>,</i> the materiality inquiry is not just a matter of determining whether, after discounting the inculpatory evidence in light of the undisclosed evidence, the remaining evidence is sufficient to support the jury's conclusions. <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley"><i>Id.,</i> at 434-435</a></span>. Rather, the question is whether "the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence in the verdict." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley"><i>Id.,</i> at 435</a></span>.</p>
<p>The District Judge decided not to hold an evidentiary hearing to determine whether Exhibits 2, 7, and 8 had been disclosed to the defense, because he was satisfied that the "potentially devastating impeachment material" contained in the other five warranted the entry of summary judgment in petitioner's favor. App. 392. The District Court's conclusion that the admittedly undisclosed documents were sufficiently important to establish a violation of the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> rule was supported by the prosecutor's closing argument. That argument relied on Stoltzfus' testimony to demonstrate petitioner's violent propensities and to establish that he was the instigator and leader in Whitlock's abduction and, by inference, her murder. The prosecutor emphasized the importance of Stoltzfus' testimony in proving the abduction:</p>
<blockquote>"[W]e are lucky enough to have an eyewitness who saw [what] happened out there in that parking lot. [In a] lot of cases you don't. A lot of cases you can just theorize what happened in the actual abduction. But Mrs. Stoltzfus was there, she saw [what] happened." App. 169.</blockquote>
<p><span class="star-pagination">*291</span> Given the record evidence involving Henderson,<sup>[36]</sup> the District Court concluded that, without Stoltzfus' testimony, the jury might have been persuaded that Henderson, rather than petitioner, was the ringleader. He reasoned that a "reasonable probability of conviction" of first-degree, rather than capital, murder sufficed to establish the materiality of the undisclosed Stoltzfus materials and, thus, a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation. App. 396.</p>
<p>The District Court was surely correct that there is a reasonable <i>possibility</i> that either a total, or just a substantial, discount of Stoltzfus' testimony might have produced a different result, either at the guilt or sentencing phases. Petitioner did, for example, introduce substantial mitigating evidence about abuse he had suffered as a child at the hands of his stepfather.<sup>[37]</sup> As the District Court recognized, however, petitioner's burden is to establish a reasonable <i>probability</i>  of a different result. <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 434</a></span>.</p>
<p><span class="star-pagination">*292</span> Even if Stoltzfus and her testimony had been entirely discredited, the jury might still have concluded that petitioner was the leader of the criminal enterprise because he was the one seen driving the car by Kurt Massie near the location of the murder and the one who kept the car for the following week.<sup>[38]</sup> In addition, Tudor testified that petitioner threatened Henderson with a knife later in the evening.</p>
<p>More importantly, however, petitioner's guilt of capital murder did not depend on proof that he was the dominant partner: Proof that he was an equal participant with Henderson was sufficient under the judge's instructions.<sup>[39]</sup> Accordingly, the strong evidence that Henderson was a killer is entirely consistent with the conclusion that petitioner was also an actual participant in the killing.<sup>[40]</sup></p>
<p><span class="star-pagination">*293</span> Furthermore, there was considerable forensic and other physical evidence linking petitioner to the crime.<sup>[41]</sup> The weight and size of the rock,<sup>[42]</sup> and the character of the fatal injuries to the victim,<sup>[43]</sup> are powerful evidence supporting the conclusion that two people acted jointly to commit a brutal murder.</p>
<p>We recognize the importance of eyewitness testimony; Stoltzfus provided the only disinterested, narrative account of what transpired on January 5, 1990. However, Stoltzfus' vivid description of the events at the mall was not the only evidence that the jury had before it. Two other eyewitnesses, <span class="star-pagination">*294</span> the security guard and Henderson's friend, placed petitioner and Henderson at the Harrisonburg Valley Shopping Mall on the afternoon of Whitlock's murder. One eyewitness later saw petitioner driving Dean's car near the scene of the murder.</p>
<p>The record provides strong support for the conclusion that petitioner would have been convicted of capital murder and sentenced to death, even if Stoltzfus had been severely impeached. The jury was instructed on two predicates for capital murder: robbery with a deadly weapon and abduction with intent to defile.<sup>[44]</sup> On state habeas, the Virginia Supreme Court rejected as procedurally barred petitioner's challenge to this jury instruction on the ground that "abduction with intent to defile" was not a predicate for capital murder for a victim over the age of 12.<sup>[45]</sup> That issue is not before us. Even assuming, however, that this predicate was erroneous, armed robbery still would have supported the capital murder conviction.</p>
<p>Petitioner argues that the prosecution's evidence on armed robbery "flowed almost entirely from inferences from Stoltzfus' testimony," and especially from her statement that Henderson had a "hard object" under his coat at the mall. Brief for Petitioner 35. That argument, however, ignores the fact that petitioner's mother and Tudor provided direct evidence that petitioner had a knife with him on the day of the crime. <span class="star-pagination">*295</span> In addition, the prosecution contended in its closing argument that the rocknot the knifewas the murder weapon.<sup>[46]</sup> The prosecution did advance the theory that petitioner had a knife when he got in the car with Whitlock, but it did not specifically argue that petitioner used the knife during the robbery.<sup>[47]</sup></p>
<p>Petitioner also maintains that he suffered prejudice from the failure to disclose the Stoltzfus documents because her testimony impacted on the jury's decision to impose the death penalty. Her testimony, however, did not relate to his eligibility for the death sentence and was not relied upon by the prosecution at all during its closing argument at the penalty phase.<sup>[48]</sup> With respect to the jury's discretionary decision to impose the death penalty, it is true that Stoltzfus described petitioner as a violent, aggressive person, but that portrayal surely was not as damaging as either the evidence that he spent the evening of the murder dancing and drinking at Dice's or the powerful message conveyed by the 69pound <span class="star-pagination">*296</span> rock that was part of the record before the jury. Notwithstanding the obvious significance of Stoltzfus' testimony, petitioner has not convinced us that there is a reasonable probability that the jury would have returned a different verdict if her testimony had been either severely impeached or excluded entirely.</p>
<p>Petitioner has satisfied two of the three components of a constitutional violation under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>:</i> exculpatory evidence and nondisclosure of this evidence by the prosecution. Petitioner has also demonstrated cause for failing to raise this claim during trial or on state postconviction review. However, petitioner has not shown that there is a reasonable probability that his conviction or sentence would have been different had these materials been disclosed. He therefore cannot show materiality under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> or prejudice from his failure to raise the claim earlier. Accordingly, the judgment of the Court of Appeals is <i>Affirmed.</i>  Justice Souter, with whom Justice Kennedy joins as to Part II, concurring in part and dissenting in part.</p>
<p>I look at this case much as the Court does, starting with its view in Part III (which I join) that Strickler has shown cause to excuse the procedural default of his <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. Like the Court, I think it clear that the materials withheld were exculpatory as devastating ammunition for impeaching Stoltzfus.<sup>[1]</sup> See <i>ante,</i> at 282. Even on the question of prejudice <span class="star-pagination">*297</span> or materiality,<sup>[2]</sup> over which I ultimately part company with the majority, I am persuaded that Strickler has failed to establish a reasonable probability that, had the materials withheld been disclosed, he would not have been found guilty of capital murder. See <i>ante,</i> at 292-296. As the Court says, however, the prejudice enquiry does not stop at the conviction but goes to each step of the sentencing process: the jury's consideration of aggravating, death-qualifying facts, the jury's discretionary recommendation of a death sentence if it finds the requisite aggravating factors, and the judge's discretionary decision to follow the jury's recommendation. See <i>ante,</i> at 294-296. It is with respect to the penultimate step in determining the sentence that I think Strickler has carried his burden. I believe there is a reasonable probability (which I take to mean a significant possibility) that disclosure of the Stoltzfus materials would have led the jury to recommend life, not death, and I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>Before I get to the analysis of prejudice I should say something about the standard for identifying it, and about the unfortunate phrasing of the shorthand version in which the standard is customarily couched. The Court speaks in terms of the familiar, and perhaps familiarly deceptive, formulation: whether there is a "reasonable probability" of a different outcome if the evidence withheld had been disclosed. The Court rightly cautions that the standard intended <span class="star-pagination">*298</span> by these words does not require defendants to show that a different outcome would have been more likely than not with the suppressed evidence, let alone that without the materials withheld the evidence would have been insufficient to support the result reached. See <i>ante,</i> at 289-290; <i>Kyles</i>  v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 434-435</a></span> (1995). Instead, the Court restates the question (as I have done elsewhere) as whether "`the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence' " in the outcome. <i>Ante,</i> at 290 (quoting <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley"><i>Kyles, supra,</i> at 435</a></span>).</p>
<p>Despite our repeated explanation of the shorthand formulation in these words, the continued use of the term "probability" raises an unjustifiable risk of misleading courts into treating it as akin to the more demanding standard, "more likely than not." While any short phrases for what the cases are getting at will be "inevitably imprecise," <i>United States</i> v. <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#108" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 108</a></span> (1976), I think "significant possibility" would do better at capturing the degree to which the undisclosed evidence would place the actual result in question, sufficient to warrant overturning a conviction or sentence.</p>
<p>To see that this is so, we need to recall <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> `s evolution since the appearance of the rule as originally stated, that "suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87</a></span> (1963). <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> itself did not explain what it meant by "material" (perhaps assuming the term would be given its usual meaning in the law of evidence, see <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#703" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 703, n. 5</a></span> (1985) (Marshall, J., dissenting)). We first essayed a partial definition in <i>United States</i> v. <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs, supra</a></span></i><i>,</i> where we identified three situations arguably within the ambit of <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> and said that in the first, involving knowing use of perjured testimony, <span class="star-pagination">*299</span> reversal was required if there was "any reasonable likelihood" that the false testimony had affected the verdict. <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs, supra,</a></span></i> at 103 (citing <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972), in turn quoting <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 271</a></span> (1959)). We have treated "reasonable likelihood" as synonymous with "reasonable possibility" and thus have equated materiality in the perjured-testimony cases with a showing that suppression of the evidence was not harmless beyond a reasonable doubt. <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley"><i>Bagley, supra,</i> at 678-680</a></span>, and n. 9 (opinion of Blackmun, J.). See also <i>Brecht</i> v. <i>Abrahamson,</i> <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/#637" aria-description="Citation for case: Brecht v. Abrahamson">507 U. S. 619, 637</a></span> (1993) (defining harmless-beyond-areasonable-doubt standard as no "`reasonable possibility' that trial error contributed to the verdict"); <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 24</a></span> (1967) (same). In <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>,</i> we thought a less demanding standard appropriate when the prosecution fails to turn over materials in the absence of a specific request. Although we refrained from attaching a label to that standard, we explained it as falling between the more-likely-than-not level and yet another criterion, whether the reviewing court's "`conviction [was] sure that the error did not influence the jury, or had but very slight effect.' " <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112</a></span> (quoting <i>Kotteakos</i> v. <i>United States,</i> <span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/#764" aria-description="Citation for case: Kotteakos v. United States">328 U. S. 750, 764</a></span> (1946)). Finally, in <i>United States</i> v. <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley, supra</a></span></i><i>,</i> we embraced "reasonable probability" as the appropriate standard to judge the materiality of information withheld by the prosecution whether or not the defense had asked first. <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> took that phrase from <i>Strickland</i> v. <i>Washington,</i> <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#694" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668, 694</a></span> (1984), where it had been used for the level of prejudice needed to make out a claim of constitutionally ineffective assistance of counsel. <i><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span></i> in turn cited two cases for its formulation, <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span></i> (which did not contain the expression "reasonable probability") and <i>United States</i> v. <i>Valenzuela-Bernal,</i> <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#873" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S. 858, 873-874</a></span> (1982) (which held that sanctions against the Government for deportation of a potential defense witness were appropriate only <span class="star-pagination">*300</span> if there was a "reasonable likelihood" that the lost testimony "could have affected the judgment of the trier of fact").</p>
<p>The circuitous path by which the Court came to adopt "reasonable probability" of a different result as the rule of <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> materiality suggests several things. First, while "reasonable possibility" or "reasonable likelihood," the <i><span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/" aria-description="Citation for case: Kotteakos v. United States">Kotteakos</a></span></i> standard, and "reasonable probability" express distinct levels of confidence concerning the hypothetical effects of errors on decisionmakers' reasoning, the differences among the standards are slight. Second, the gap between all three of those formulations and "more likely than not" is greater than any differences among them. Third, because of that larger gap, it is misleading in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> cases to use the term "probability," which is naturally read as the cognate of "probably" and thus confused with "more likely than not," see <i>Morris</i> v. <i>Mathews,</i> <span class="citation" data-id="9430368"><a href="/opinion/111606/morris-v-mathews/#247" aria-description="Citation for case: Morris v. Mathews">475 U. S. 237, 247</a></span> (1986) (apparently treating "reasonable probability" as synonymous with "probably"); <span class="citation" data-id="9430368"><a href="/opinion/111606/morris-v-mathews/#254" aria-description="Citation for case: Morris v. Mathews"><i>id.,</i> at 254, n. 3</a></span> (Blackmun, J., concurring in judgment) (cautioning against confusing "reasonable probability" with more likely than not). We would be better off speaking of a "significant possibility" of a different result to characterize the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> materiality standard. Even then, given the soft edges of all these phrases,<sup>[3]</sup> the touchstone of the enquiry <span class="star-pagination">*301</span> must remain whether the evidentiary suppression "undermines our confidence" that the factfinder would have reached the same result.</p>
<p></p>
<h2>II</h2>
<p>Even keeping in mind these caveats about the appropriate level of materiality, applying the standard to the facts of this case does not give the Court easy answers, as the Court candidly acknowledges. See <i>ante,</i> at 289. Indeed, the Court concedes that discrediting Stoltzfus's testimony "might have changed the outcome of the trial," <i>ibid.,</i> and that the District Court was "surely correct" to find a "reasonable <i>possibility</i>  that either a total, or just a substantial, discount of Stoltzfus' testimony might have produced a different result, either at the guilt or sentencing phases," <i>ante,</i> at 291.</p>
<p>In the end, however, the Court finds the undisclosed evidence inadequate to undermine confidence in the jury's sentencing <span class="star-pagination">*302</span> recommendation, whereas I find it sufficient to do that. Since we apply the same standard to the same record, our differing conclusions largely reflect different assessments of the significance the jurors probably ascribed to the Stoltzfus testimony. My assessment turns on two points. First, I believe that in making the ultimate judgment about what should be done to one of several participants in a crime this appalling the jurors would very likely have given weight to the degree of initiative and leadership exercised by that particular defendant. Second, I believe that no other testimony comes close to the prominence and force of Stoltzfus's account in showing Strickler as the unquestionably dominant member of the trio involved in Whitlock's abduction and the aggressive and moving figure behind her murder.</p>
<p>Although Stoltzfus was not the prosecution's first witness, she was the first to describe Strickler in any detail, thus providing the frame for the remainder of the story the prosecution presented to the jury. From the start of Stoltzfus's testimony, Strickler was "Mountain Man" and his male companion "Shy Guy," labels whose repetition more than a dozen times (by the prosecutor as well as by Stoltzfus) must have left the jurors with a clear sense of the relative roles that Strickler and Henderson played in the crimes that followed Stoltzfus's observation. According to her, when she first saw Strickler she "just sort of instinctively backed up because I was frightened." App. 36. Unlike retiring "Shy Guy," Strickler was "revved up." <i>Id.,</i> at 39, 60. Even in describing her first encounter with Strickler inside the mall, Stoltzfus spoke of him as domineering, a "very impatient" character yelling at his female companion, "Blonde Girl," to join him. <i>Id.,</i> at 36, 38-39.</p>
<p>After describing in detail how "Mountain Man" and "Blonde Girl" were dressed, Stoltzfus said that "`Mountain Man' came tearing out of the Mall entrance door and went up to the driver of [a] van and . . . was just really mad and ran back and banged on back of the backside of the van" <span class="star-pagination">*303</span> while "Shy Guy" and "Blonde Girl" hung back. <i>Id.,</i> at 43. "Mountain Man" approached a pickup truck, then "pounded on" the front passenger side window of Whitlock's car, "shook and shook the car door," "banging and banging on the window" while Whitlock checked to see if the door was locked. <i>Ibid.</i> Finally, "he just really shook it hard and you could tell he was mad. Shook it really hard and the door opened and he jumped in . . . and faced her." <i>Id.,</i> at 43-44. While Whitlock tried to push him away, "Mountain Man" "motioned for `Blonde Girl' and `Shy Guy' to come" and the girl did as she was bidden. She "started to jump into the car," but "jumped back" when Whitlock stepped on the gas. <i>Id.,</i> at 44. Then "Mountain Man" started "hitting [Whitlock] on the left shoulder, her right shoulder and then . . . the head," finally "open[ing] the door again" so "the `Blonde Girl' got in the back and `Shy Guy' followed and got behind him." <i>Id.,</i> at 45. "Shy Guy" passed "Mountain Man" his tan coat, which "Mountain Man" "fiddled with" for "what seemed like a long time," then "sat back up and . . . faced" Whitlock while "the other two in the back seat sat back and relaxed." <i>Ibid.</i>  Stoltzfus then claimed that she got out of her car and went over to Whitlock's, whereupon unassertive "Shy Guy" "instinctively jumped, you know, laid over on the seat to hide from me." <i>Id.,</i> at 46. Stoltzfus pulled up next to Whitlock's car and repeatedly asked, "[A]re you O.K.[?]," but Whitlock responded only with eye contact; "she didn't smile, there was no expression," and "[j]ust very serious, looked down to her right," suggesting Strickler was holding a weapon on her. <i>Id.,</i> at 46, 47. Finally, Whitlock mouthed something, which Stoltzfus demonstrated for the jury and then explained she realized must have been the word, "help." <i>Id.,</i> at 47.</p>
<p>Without rejecting the very notion that jurors with discretion in sentencing would be influenced by the relative dominance of one accomplice among others in a shocking crime, I could not regard Stoltzfus's colorful testimony as anything but significant on the matter of sentence. It was Stoltzfus <span class="star-pagination">*304</span> alone who described Strickler as the initiator of the abduction, as the one who broke into Whitlock's car, who beckoned his companions to follow him, and who violently subdued the victim while "Shy Guy" sat in the back seat. The bare content of this testimony, important enough, was enhanced by one of the inherent hallmarks of reliability, as Stoltzfus confidently recalled detail after detail. The withheld documents would have shown, however, that many of the details Stoltzfus confidently mentioned on the stand (such as Strickler's appearance, Whitlock's appearance, the hour of day when the episode occurred, and her daughter's alleged notation of the license plate number of Whitlock's car) had apparently escaped her memory in her initial interviews with the police. Her persuasive account did not come, indeed, until after her recollection had been aided by further conversations with the police and with the victim's boyfriend. I therefore have to assess the likely havoc that an informed cross-examiner could have wreaked upon Stoltzfus as adequate to raise a significant possibility of a different recommendation, as sufficient to undermine confidence that the death recommendation would have been the choice. All it would have taken, after all, was one juror to hold out against death to preclude the recommendation actually given.</p>
<p>The Court does not, of course, deny that evidence of dominant role would probably have been considered by the jury; the Court, instead, doubts that this consideration, and the evidence bearing on it, would have figured so prominently in a juror's mind as to be a fulcrum of confidence. I am not convinced by the Court's reasons.</p>
<p>The Court emphasizes the brutal manner of the killing and Strickler's want of remorse as jury considerations diminishing the relative importance of Strickler's position as ringleader. See <i>ante,</i> at 295-296. Without doubt the jurors considered these to be important factors, and without doubt they may have been treated as sufficient to warrant death. But as the Court says, sufficiency of other evidence and the <span class="star-pagination">*305</span> facts it supports is not the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> standard, and the significance of both brutality and sangfroid must surely have been complemented by a certainty that without Strickler there would have been no abduction and no ensuing murder.</p>
<p>The Court concludes that Stoltzfus's testimony is unlikely to have had significant influence on the jury's sentencing recommendation because the prosecutor made no mention of her testimony in his closing statement at the sentencing proceeding. See <i>ante,</i> at 295. But although the Court is entirely right that the prosecution gave no prominence to the Stoltzfus testimony at the sentencing stage, the Commonwealth's closing actually did include two brief references to Strickler's behavior in "just grabbing a complete stranger and abducting her," 19 Record 919; see also <i>id.,</i> at 904, as relevant to the jury's determination of future dangerousness. And since Strickler's criminal record had no convictions involving actual violence, a point defense counsel stressed in his closing argument, see <i>id.,</i> at 913, the jurors may well have given weight to Stoltzfus's lively portrait of Strickler as the aggressive leader of the group when they came to assess his future dangerousness.</p>
<p>What is more important, common experience, supported by at least one empirical study, see Bowers, Sandys, &amp; Steiner, Foreclosed Impartiality in Capital Sentencing: Jurors' Predispositions, Guilt-Trial Experience, and Premature Decision Making, <span class="citation no-link">83 Cornell L. Rev. 1476</span>, 1486-1496 (1998), tells us that the evidence and arguments presented during the guilt phase of a capital trial will often have a significant effect on the jurors' choice of sentence. True, Stoltzfus's testimony directly discussed only the circumstances of Whitlock's abduction, but its impact on the jury was almost certainly broader, as the prosecutor recognized. After the jury rendered its verdict on guilt, for example, the defense moved for a judgment of acquittal on the capital murder charge based on insufficiency of the evidence. In the prosecutor's argument to the court he replied that</p>
<blockquote>
<span class="star-pagination">*306</span> "the evidence clearly shows that this man was the aggressor. He was the one that ran out. He was the one that grabbed Leanne Whitlock. When she struggled trying to get away from him . . . , he was the one that started beating her there in the car. And finally subdued her enough to make her drive away from the mall, so you start with the principle that he is the aggressor." 20 Record 15.</blockquote>
<p>Stoltzfus's testimony helped establish the "principle," as the prosecutor put it, that Strickler was "the aggressor," the dominant figure, in the whole sequence of criminal events, including the murder, not just in the abduction. If the defense could have called Stoltzfus's credibility into question, the jurors' belief that Strickler was the chief aggressor might have been undermined to the point that at least one of them would have hesitated to recommend death.</p>
<p>The Court suggests that the jury might have concluded that Strickler was the leader based on three other pieces of evidence: Kurt Massie's identification of Strickler as the driver of Whitlock's car on its way toward the field where she was killed; Donna Tudor's testimony that Strickler kept the car the following week; and Tudor's testimony that Strickler threatened Henderson with a knife later on the evening of the murder. But if we are going to look at other testimony we cannot stop here. The accuracy of both Massie's and Tudor's testimony was open to question,<sup>[4]</sup> and all of it was subject to some evidence that Henderson had taken a major role in the murder. The Court has quoted the District <span class="star-pagination">*307</span> Court's summation of evidence against him, <i>ante,</i> at 291, n. 36: Henderson's wallet was found near the body, his clothes were bloody, he presented a woman friend with the victim's watch at a postmortem celebration (which he left driving the victim's car), and he confessed to a friend that he had just killed an unidentified black person. Had this been the totality of the evidence, the jurors could well have had little certainty about who had been in charge. But they could have had no doubt about the leader if they believed Stoltzfus.</p>
<p>Ultimately, I cannot accept the Court's discount of Stoltzfus in the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> sentencing calculus for the reason I have repeatedly emphasized, the undeniable narrative force of what she said. Against this, it does not matter so much that other witnesses could have placed Strickler at the shopping mall on the afternoon of the murder, <i>ante,</i> at 293-294, or that the Stoltzfus testimony did not directly address the aggravating factors found, <i>ante,</i> at 295. What is important is that her evidence presented a gripping story, see E. Loftus &amp; J. Doyle, Eyewitness Testimony: Civil and Criminal 5 (3d ed. 1997) ("[R]esearch redoundingly proves that the story format is a powerful key to juror decision making"). Its message was that Strickler was the madly energetic leader of two morally apathetic accomplices, who were passive but for his direction. One cannot be reasonably confident that not a single juror would have had a different perspective after an impeachment that would have destroyed the credibility of that story. I would accordingly vacate the sentence and remand for reconsideration, and to that extent I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   <i>Gerald T. Zerkin</i> filed a brief for the National Association of Criminal Defense Lawyers et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>Kent S. Scheidegger</i> filed a brief for the Criminal Justice Legal Foundation as <i>amicus curiae</i> urging affirmance.</p>
<p>[]   Justice Thomas joins Parts I and IV of this opinion. Justice Kennedy joins Part III.</p>
<p>[1]  The opinion of the Court of Appeals is unreported. The judgment order is reported, <i>Strickler</i> v<i>. Pruett,</i> <span class="citation no-link">149 F. 3d 1170</span> (CA4 1998). The opinion of the District Court is also unreported.</p>
<p>[2]  Petitioner was tried in May 1990. Henderson fled the Commonwealth and was later apprehended in Oregon. He was tried in March 1991.</p>
<p>[3]  Workman was calledas a defense witness.</p>
<p>[4]  Whitlock's roommate testified that Whitlock had dinner at 6 p.m. on January 5, 1990, just before she left for the mall to return Dean's car.</p>
<p>[5]  She testified to their appearances in great detail. She stated that petitioner had "a kind of multi layer look." He wore a grey T-shirt with a Harley Davidson insignia on it. The prosecutor showed Stoltzfus the shirt, stained with blood and semen, that the police had discovered at petitioner's mother's house. He asked if it were the same shirt she saw petitioner wearing at the mall. She replied,"That could have been it." App. 37, 39. Henderson "had either a white or light colored shirt, probably a short sleeve knit shirt and his pants were neat. They weren't just old blue jeans. They may have been new blue jeans or it may have just been more dressy slacks of some sort." <i>Id.,</i> at 37. The woman "had blonde hair, it was kind of in a shaggy cut down the back. She had blue eyes, she had a real sweet smile, kind of a small mouth. Just a touch of freckles on her face."<i>Id.,</i> at 60.</p>
<p>[6]  Stoltzfus stated that the girl caught a button in Stoltzfus' "open weave sweater, which is why I remember her attire." <i>Id.,</i> at 39.</p>
<p>[7]  "I said to my fourteen[-year-]old daughter, write down the license number, you know, it was West Virginia, NKA 243 and I said help me to remember, `No Kids Alone 243,' and I said remember, 243 is my age." <i>Id.,</i>  at 48.</p>
<p>[8]  These materials were originally attached to an affidavit submitted with petitioner's motion for summary judgment on his federal petition for habeas corpus. Because both the District Court and the Court of Appeals referred to the documents by their exhibit numbers, we have done the same.</p>
<p>[9]  As the District Court pointed out, however, it omits reference to the fact that Stoltzfus originally said that she could not identify the victim a fact recorded in his handwritten notes. <i>Id.,</i> at 387.</p>
<p>[10]  Stoltzfus' trial testimony made no mention of her meeting with Dean.</p>
<p>[11]  The prosecutor recalled that Exhibits 2, 7, and 8 had been in his open file, <i>id.,</i> at 365-368, but the lawyer who represented Henderson at his trial swore that they were not in the file, <i>id.,</i> at 330; the recollection of petitioner's trial counsel was somewhat equivocal. Lead defense counsel was sure he had not seen the documents, <i>id.,</i> at 300, while petitioner's other lawyer signed an affidavit to the effect that he does "remember the information contained in [the documents]" but "cannot recall if I have seen these specific documents," <i>id.,</i> at 371.</p>
<p>[12]  Although the parties have not advanced an explanation for the nondisclosure of the documents, perhaps it was an inadvertent consequence of the fact that Harrisonburg is in Rockingham County and the trial was conducted by the Augusta County prosecutor. We note, however, that the prosecutor is responsible for "any favorable evidence known to the others acting on the government's behalf in the case, including the police." <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#437" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 437</a></span> (1995). Thus, the Commonwealth, through its prosecutor, is charged with knowledge of the Stoltzfus materials for purposes of <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963).</p>
<p>[13]  In the federal habeas proceedings, the prosecutor gave the following sworn answer to an interrogatory requesting him to state what materials were disclosed by him to defense counsel pursuant to <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>:</i> "I disclosed my entire prosecution file to Strickler's defense counsel prior to Strickler's trial by allowing him to inspect my entire prosecution file including, but not limited to, all police reports in the file and all witness statements in the file." App. 368. Petitioner's trial counsel had shared the prosecutor's understanding of the "open file" policy. In an affidavit filed in the state habeas proceeding, they stated that they "thoroughly investigated" petitioner's case. "In this we were aided by the prosecutor's office, which gave us full access to their files and the evidence they intended to present. We made numerous visits to their office to examine these files . . . . As a result of this cooperation, they introduced nothing at trial of which we were previously unaware." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#223" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 223</a></span>.</p>
<p>[14]  In its pleadings on state habeas, the Commonwealth explained: "From the inception of this case, the prosecutor's files were open to the petitioner's counsel. Each of the petitioner's attorneys made numerous visits to the prosecutor's offices and reviewed <i>all</i> the evidence the Commonwealth intended to present. . . . Given that counsel were voluntarily given full disclosure of everything known to the government, there was no need for a formal <i>[Brady]</i> motion." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#212" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 212-213</a></span>.</p>
<p>[15]  "The Commonwealth's theory of the case was that Strickler and Henderson had acted jointly to accomplish the actual killing. It contended at trial, and argues on appeal, that the physical evidence points to a violent struggle between the assailants and the victim, in which Strickler's hair had actually been torn out by the roots. Although Leanne had been beaten and kicked, none of her injuries would have been sufficient to immobilize her until her skull was crushed with the 69-pound rock. Because, the Commonwealth's argument goes, the rock had been dropped on her head at least twice, while she was on the ground, leaving two bloodstained depressions in the frozen earth, it would have been necessary that she be held down by one assailant while the other lifted the rock and dropped it on her head.
</p>
<p>"The weight and dimensions of the 69-pound bloodstained rock, which was introduced in evidence as an exhibit, made it apparent that a single person could not have lifted it and dropped or thrown it while simultaneously holding the victim down. The bloodstains on Henderson's jacket as well as on Strickler's clothing further tended to corroborate the Commonwealth's theory that the two men had been in the immediate presence of the victim's body when the fatal blows were struck and, hence, had jointly participated in the killing." <i>Strickler,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#494" aria-description="Citation for case: Strickler v. Commonwealth">241 Va., at 494</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#235" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d, at 235</a></span>.</p>
<p>[16]  See n. 14, <i>supra.</i> </p>
<p>[17]  Petitioner later voluntarily dismissed this claim. App. 384.</p>
<p>[18]  For reasons we do not entirely understand, the Court of Appeals thus concluded that, while it was reasonable for trial counsel to rely on the open file policy, it was unreasonable for postconviction counsel to do so.</p>
<p>[19]  See, <i>e. g., </i><i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935) <i>(per curiam)</i><i>; </i><i>Pyle</i> v. <i>Kansas,</i> <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/#216" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213, 216</a></span> (1942); <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269-270</a></span> (1959).</p>
<p>[20]  Consider, for example, this comment in the dissenting opinion in <i>Kyles</i>  v. <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Whitley</a></span></i><i>:</i> "It is petitioner's burden to show that in light of all the evidence, including that untainted by the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation, it is reasonably probable that a jury would have entertained a reasonable doubt regarding petitioner's guilt." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#460" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 460</a></span> (opinion of Scalia, J.).</p>
<p>[21]  We reject respondent's contention that these documents do not fall under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> because they were "inculpatory." Brief for Respondent 41. Our cases make clear that <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> `s disclosure requirements extend to materials that, whatever their other characteristics, may be used to impeach a witness. <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#676" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 676</a></span> (1985).</p>
<p>[22]  While the precise dimensions of an "open file policy" may vary from jurisdiction to jurisdiction, in this case it is clear that the prosecutor's use of the term meant that his entire prosecution file was made available to the defense. App. 368; see also n. 13, <i>supra.</i> </p>
<p>[23]  We certainly do not criticize the prosecution's use of the open file policy. We recognize that this practice may increase the efficiency and the fairness of the criminal process. We merely note that, if a prosecutor asserts that he complies with <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> through an open file policy, defense counsel may reasonably rely on that file to contain all materials the State is constitutionally obligated to disclose under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i> </p>
<p>[24]  "[W]e think that the existence of cause for a procedural default must ordinarily turn on whether the prisoner can show that some objective factor external to the defense impeded counsel's efforts to comply with the State's procedural rule. Without attempting an exhaustive catalog of such objective impediments to compliance with a procedural rule, we note that a showing that the factual or legal basis for a claim was not reasonably available to counsel, see <i>Reed</i> v<i>. Ross,</i> 468 U. S., at 16, or that `some interference by officials,' <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#486" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 486</a></span> (1953), made compliance impracticable, would constitute cause under this standard." <i>Murray,</i> <span class="citation" data-id="9430624"><a href="/opinion/111727/murray-v-carrier/#488" aria-description="Citation for case: Murray v. Carrier">477 U. S., at 488</a></span>; see also <i>Amadeo</i> v. <i>Zant,</i> <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/#221" aria-description="Citation for case: Amadeo v. Zant">486 U. S. 214, 221-222</a></span> (1988).</p>
<p>[25]  Stoltzfus testified to meeting with Claytor at least three times. App. 55-56.</p>
<p>[26]  In her letter, which appeared on July 18, 1990 (after petitioner's trial) in the Harrisonburg Daily News-Record, Stoltzfus stated: "It never occurred to me that I was witnessing an abduction. In fact, if it hadn't been for the intelligent, persistent, professional work of Detective Daniel Claytor, I still wouldn't realize it. What sounded like a coherent story at the trial was the result of an incredible effort by the police to fit a zillion little puzzle pieces into one big picture." <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/#250" aria-description="Citation for case: Amadeo v. Zant"><i>Id.,</i> at 250</a></span>. Stoltzfus also gave a pretrial interview to a reporter with the Roanoke Times that conflicted in some respects with her trial testimony, principally because she identified the blonde woman at the mall as Tudor. <i>Id.,</i> at 373.</p>
<p>[27]  The defense could not discover copies of these notes from Stoltzfus herself, because she refused to speak with defense counsel before trial. <i>Id.,</i> at 370.</p>
<p>[28]  The parties have been unable to provide, and the record does not illuminate, the factual basis on which the District Court entered the discovery order. It was granted <i>ex parte</i> and under seal and furnished broad access to any records relating to petitioner. District Court Record, Doc. No. 20. The Fourth Circuit has since found that federal district courts do not possess the authority to issue <i>ex parte</i> discovery orders in habeas proceedings. <i>In re Pruett,</i> <span class="citation" data-id="6961602"><a href="/opinion/7057802/in-re-pruett/#280" aria-description="Citation for case: In re Pruett">133 F. 3d 275, 280</a></span> (1997). We express no opinion on the Fourth Circuit's decision on this question. However, we note that it is unlikely that petitioner would have been granted in state court the sweeping discovery that led to the Stoltzfus materials, since Virginia law limits discovery available during state habeas. Indeed, it is not even clear that he had a right to such discovery in federal court. See n. 29<i>, infra.</i> </p>
<p>[29]  Virginia law provides that "no discovery shall be allowed in any proceeding for a writ of habeas corpus or in the nature of coram nobis without prior leave of the court, which may deny or limit discovery in any such proceeding." Va. Sup. Ct. Rule 4:1(b)(5)(3)(b) (1998); see also <i>Yeatts</i> v. <i>Murray,</i> <span class="citation" data-id="1219071"><a href="/opinion/1219071/yeatts-v-murray/#289" aria-description="Citation for case: Yeatts v. Murray">249 Va. 285, 289</a></span>, <span class="citation" data-id="1219071"><a href="/opinion/1219071/yeatts-v-murray/#21" aria-description="Citation for case: Yeatts v. Murray">455 S. E. 2d 18, 21</a></span> (1995). Respondent acknowledges that petitioner was not entitled to discovery under Virginia law. Brief for Respondent 25.</p>
<p>[30]  See Va. Sup. Ct. Rule 3A:11 (1998). This rule expressly excludes from defendants "the discovery or inspection of statements made by Commonwealth witnesses or prospective Commonwealth witnesses to agents of the Commonwealth or of reports, memoranda or other internal Commonwealth documents made by agents in connection with the investigation or prosecution of the case, except [for scientific reports of the accused or alleged victim]." The Virginia Supreme Court found that petitioner had been afforded all the discovery he was entitled to on direct review. "Limited discovery is permitted in criminal cases by the Rules of Court. . . . Strickler had the benefit of all the discovery to which he was entitled under the Rules. Those rights do not extend to general production of evidence, except in the limited areas prescribed by Rule 3A:11." <i>Strickler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#491" aria-description="Citation for case: Strickler v. Commonwealth">241 Va. 482, 491</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#233" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d 227, 233</a></span> (1991).</p>
<p>[31]  This statement is quoted in full at n. 14, <i>supra.</i> Respondent argues that this representation is not dispositive because it was made in his motion to dismiss and therefore cannot excuse the failure to include a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  claim in the petitioner's original state habeas pleading. We find the timing of the statement irrelevant, since the warden's response merely summarizes the Commonwealth's "open file" policy, instituted by the prosecution at the inception of the case.</p>
<p>[32]  Furthermore, in its opposition to petitioner's motion during state habeas review for funds for an investigator, the Commonwealth argued: "Strickler's Petition contains 139 separate habeas claims. By requesting appointment of an investigator `to procure the necessary factual basis to support certain of Petitioner's claims' (Motion, p. 1), Petitioner is implicitly conceding that he is not aware of factual support for the claims he has already made<i>.</i> Respondent agrees." App. 242.
</p>
<p>In light of these assertions, we fail to see how the Commonwealth believes petitioner could have shown "good cause" sufficient to get discovery on a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in state habeas.</p>
<p>[33]  We do not reach, because it is not raised in this case, the impact of a showing by the State that the defendant was aware of the existence of the documents in question and knew, or could reasonably discover, how to obtain them. Although <i><span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/" aria-description="Citation for case: Gray v. Netherland">Gray</a></span></i> involved a procedurally defaulted <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  claim, in that case, the Court found that the petitioner had made "no attempt to demonstrate cause or prejudice for his default." <i>Gray,</i> <span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/#162" aria-description="Citation for case: Gray v. Netherland">518 U. S., at 162</a></span>.</p>
<p>[34]  It is noteworthy that both of the reasons on which we relied in <i><span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/" aria-description="Citation for case: McCleskey v. Zant">McCleskey</a></span></i> to distinguish <i><span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/" aria-description="Citation for case: Amadeo v. Zant">Amadeo</a></span></i> also apply to this case: "This case differs from <i><span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/" aria-description="Citation for case: Amadeo v. Zant">Amadeo</a></span></i> in two crucial respects. First, there is no finding that the State concealed evidence. And second, even if the State intentionally concealed the 21-page document, the concealment would not establish cause here because, in light of McCleskey's knowledge of the information in the document, any initial concealment would not have prevented him from raising the claim in the first federal petition." <span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/#501" aria-description="Citation for case: McCleskey v. Zant">499 U. S., at 501-502</a></span>.</p>
<p>[35]  Because our opinion does not modify <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> we reject respondent's contention that we announce a "new rule" today. See <i>Bousley</i> v. <i>United States,</i> <span class="citation" data-id="9433629"><a href="/opinion/118205/bousley-v-united-states/" aria-description="Citation for case: Bousley v. United States">523 U. S. 614</a></span> (1998).</p>
<p>[36]  The District Court summarized the evidence against Henderson. "Henderson's clothes had blood on them that night. Henderson had property belonging to Whitlock and gave her watch to a woman, Simmons, while at a restaurant known as Dice's Inn. Tr. 541. Henderson left Dice's Inn driving Whitlock's car. Henderson's wallet was found in the vicinity of Whitlock's body and was possibly lost during his struggle with her. Significantly, Henderson confessed to a friend on the night of the murder that he had just killed an unidentified black person and that friend observed blood on Henderson's jeans." App. 395.</p>
<p>[37]  At sentencing, the trial court discussed the mitigation evidence: "On the charge of capital murder . . . it is difficult . . . to sit here and listen to the testimony of [petitioner's mother] and Mr. Strickler's two sisters and not feel a great, great deal of sympathy for, for any person who has a childhood and a life like Mr. Strickler has had. He was in no way responsible for the circumstances of his birth. He was brutalized from the minute he's, almost from the minute he was born and certainly with his . . . limitations and his ability with which he was born, it would have been extremely difficult for him to, to help himself. And difficult, when you look at a case like that to feel but anything but sympathy for him." Sentencing Hearing, 20 Record 57-58.</p>
<p>[38]  As the trial court stated at petitioner's sentencing hearing: "The facts in this case which support this jury verdict are one that Mr. Strickler was . . . in control of this situation. He was in control at the shopping center in Harrisonburg. He was in control when the car went into the field up here on the 340 north of Waynesboro. He was in control thereafter, he ended up with the car. There is no question who . . . was in control of this entire situation." <i>Id.,</i> at 22.</p>
<p>[39]  The judge gave the following instruction at petitioner's trial: "You may find the defendant guilty of capital murder if the evidence establishes that the defendant jointly participated in the fatal beating, if it is established beyond a reasonable doubt that the defendant was an active and immediate participant in the act or acts that caused the victim's death." <i>Strickler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#493" aria-description="Citation for case: Strickler v. Commonwealth">241 Va., at 493-494</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#234" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d, at 234-235</a></span>. The Virginia Supreme Court affirmed the propriety of this instruction on petitioner's direct appeal. <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#495" aria-description="Citation for case: Strickler v. Commonwealth"><i>Id.,</i> at 495</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#235" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d, at 235</a></span>.</p>
<p>[40]  It is also consistent with the fact that Henderson was convicted of first-degree murder but acquitted of capital murder after his jury, unlike petitioner's, was instructed that they could convict him of capital murder only if they found that he had "`inflict[ed] the fatal blows.' " Henderson's jury was instructed, "`One who is present aiding and abetting the actual killing, but who does not inflict the fatal blows that cause death is a principle [sic] in the second degree, and may not be found guilty of capital murder. Before you can find the defendant guilty of capital murder, the evidence must establish beyond a reasonable doubt that the defendant was an active and immediate participant in the acts that caused the death.' " 2 App. in No. 97-29 (CA4), p. 777.
</p>
<p>Henderson's trial took place before the Virginia Supreme Court affirmed the trial instruction, and the "joint perpetrator" theory it embodied, given at petitioner's trial. <i>Strickler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#494" aria-description="Citation for case: Strickler v. Commonwealth">241 Va., at 494</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#235" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d, at 235</a></span>. Petitioner's trial judge rejected one of petitioner's proffered instructions, which would have required the Commonwealth to prove that "the defendant was the person who actually delivered the blow that killed Leanne Whitlock." <i><span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/" aria-description="Citation for case: Strickler v. Commonwealth">Ibid.</a></span></i> Petitioner's trial judge recused himself from presiding over Henderson's trial, indicating that he had already formed his own opinion about what had happened the night of Whitlock's murder. 21 Record 2.</p>
<p>[41]  For example, the police recovered hairs on a bra and shirt found with Whitlock's body that "were microscopically alike in all identifiable characteristics" to petitioner's hair. App. 135. The shirt recovered from the car at Strickler's mother's house had human blood on it. Petitioner's fingerprints were found on the outside and inside of the car taken from Whitlock. <i>Id.,</i> at 128-129. Tudor testified that petitioner's pants had blood on them, and he had a cut on his knuckle. <i>Id.,</i> at 95.</p>
<p>[42]  The trial judge thought the shape of the rock so significant to the jury's conclusion that he instructed the lawyers to have "detailed, high quality photographs taken of [the rock] . . . and I want it put in the record of the case." Sentencing Hearing, 20 Record 53.</p>
<p>[43]  The Deputy Chief Medical Examiner, who performed the autopsy, testified that the object that produced the fractures in Whitlock's skull caused "severe lacerations to the brain," and any two of the four fractures would have been fatal. App. 112.</p>
<p>[44]  The trial court instructed the jury that, to convict petitioner of capital murder, it must find beyond a reasonable doubt that (1) "the defendant killed Leanne Whitlock"; (2) "the killing was willful, deliberate and premeditated"; and (3) "the killing occurred during the commission of robbery while the defendant was armed with a deadly weapon, or occurred during the commission of abduction with intent to extort money or a pecuniary benefit or with the intent to defile or was of a person during the commission of, or subsequent to, rape." <i>Strickler</i> v. <i>Murray,</i> <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/" aria-description="Citation for case: Strickler v. Murray">249 Va. 120</a></span>, 124 125, <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/#650" aria-description="Citation for case: Strickler v. Murray">452 S. E. 2d 648, 650</a></span> (1995).</p>
<p>[45]  In its motion to dismiss petitioner's state habeas petition, the Commonwealth conceded that the instruction on intent to defile was erroneously given in this case as a predicate for capital murder. App. 218.</p>
<p>[46]  In his closing argument, the prosecutor stated that there was "really no doubt about where it happened and what the murder weapon was. It was not a gun, it wasn't a knife. It was this thing here, it is to[o] big to be called a rock and to[o] small to be called a boulder." <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/#167" aria-description="Citation for case: Strickler v. Murray"><i>Id.,</i> at 167</a></span>.</p>
<p>[47]  The instructions given to the jury defined a deadly weapon as "any object or instrument that is likely to cause death or great bodily injury because of the manner and under the circumstance in which it is used." <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/#160" aria-description="Citation for case: Strickler v. Murray"><i>Id.,</i> at 160</a></span>.</p>
<p>[48]  The jury recommended death after finding the predicates of "future dangerousness" and "vileness." Neither of these predicates depended on Stoltzfus' testimony. The trial court instructed the jury, "Before the penalty can be fixed at death, the Commonwealth must prove beyond a reasonable doubt at least one of the following two alternatives. One, that after consideration of his history and background, there is a probability that he would commit criminal acts of violence that would constitute a continuing, continuing serious threat to society or two, that his conduct in committing the offense was outrageously or wantonly vile, horrible or inhuman and that it involved torture, depravity of mind or aggravated battery to the victim beyond the minimum necessary to accomplish the act of murder." Tr. 899-900.</p>
<p>[1]  The Court notes that the District Court did not resolve whether all eight of the Stoltzfus documents had been withheld, as Strickler claimed, or only five. For purposes of its decision granting summary judgment for Strickler, the District Court assumed that only five had not been disclosed. See <i>ante,</i> at 290, 279. The Court of Appeals also left the dispute unresolved, see App. 418, n. 8, though granting summary judgment for respondent based on a lack of prejudice would presumably have required that court to assume that all eight documents had been withheld. Because this Court affirms the grant of summary judgment for respondent based on lack of prejudice and because it relies on at least one of the disputed documents in its analysis, see <i>ante,</i> at 282, I understand it to have assumed that none of the eight documents was disclosed. I proceed based on that assumption as well. If one thought the difference between five and eight documents withheld would affect the determination of prejudice, a remand to resolve that factual question would be necessary.</p>
<p>[2]  In keeping with suggestions in a number of our opinions, see <i>Schlup</i> v. <i>Delo,</i> <span class="citation" data-id="9433081"><a href="/opinion/117893/schlup-v-delo/#327" aria-description="Citation for case: Schlup v. Delo">513 U. S. 298, 327, n. 45</a></span> (1995); <i>Sawyer</i> v. <i>Whitley,</i> <span class="citation" data-id="9432638"><a href="/opinion/112773/sawyer-v-whitley/#345" aria-description="Citation for case: Sawyer v. Whitley">505 U. S. 333, 345</a></span> (1992), the Court treats the prejudice enquiry as synonymous with the materiality determination under <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963). See <i>ante,</i> at 282, 288-289, 296. I follow the Court's lead.</p>
<p>[3]  Each of these phrases or standards has been used in a number of contexts. This Court has used "reasonable possibility," for example, in defining the level of threat of injury to competition needed to make out a claim under the Robinson-Patman Act, see, <i>e. g., </i><i>Brooke Group Ltd.</i> v. <i>Brown &amp; Williamson Tobacco Corp.,</i> <span class="citation" data-id="9432860"><a href="/opinion/112893/brooke-group-ltd-v-brown-williamson-tobacco-corp/#222" aria-description="Citation for case: Brooke Group Ltd. v. Brown &amp; Williamson Tobacco Corp.">509 U. S. 209, 222</a></span> (1993); the standard for judging whether a grand jury subpoena should be quashed under Federal Rule of Criminal Procedure 17(c), see <i>United States</i> v. <i>R. Enterprises, Inc.,</i> <span class="citation" data-id="9432185"><a href="/opinion/112523/unite

[...TRUNCATED 5006 of 125006 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Taylor v. Alabama.md  (`case`, 6 assertions)

### content_page

```
---
title: "Taylor v. Alabama"
type: case
citation: "457 U.S. 687 (1982)"
parallel_cite: "102 S. Ct. 2664; 73 L. Ed. 2d 314"
neutral_cite: 1982 U.S. LEXIS 138
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1982
date_decided: 1982-06-23
docket: 81-5152
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1982-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Taylor v. Alabama
  varies_by_point: false
  scope_note: "Applies the Brown v. Illinois attenuation factors; the confession was conceded voluntary for Fifth Amendment purposes yet still suppressed as a Fourth Amendment fruit. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110760/taylor-v-alabama/"
  cluster_id: 110760
  opinion_id: 110760
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Progeny (attenuation)"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[Brown v. Illinois]]", "[[Dunaway v. New York]]", "[[Wong Sun v. United States]]", "[[Davis v. Mississippi]]", "[[Kaupp v. Texas]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "attenuation", "illegal-arrest", "confession"]
holding: "A confession obtained after a warrantless arrest made without probable cause must be suppressed as the fruit of the illegal arrest where no significant intervening event broke the causal chain; Miranda warnings, the passage of a few hours, and a later ex parte warrant did not attenuate the taint."
lake:
  record_id: Taylor v. Alabama
  status: verified
  projected_at: 2026-07-09
---

# Taylor v. Alabama

*457 U.S. 687 (1982)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Taylor was arrested without a warrant or probable cause for a grocery-store robbery, on an uncorroborated, second-hand tip. Held at the station, he was given [[Miranda and Custodial Interrogation|Miranda warnings]], questioned on several occasions over about six hours, fingerprinted, and put in a lineup. While he was in custody police matched his prints to prints from the scene and filed an arrest warrant *[[Common Legal Terms#ex-parte|ex parte]]*. After a brief visit with his girlfriend, he signed a confession. He moved to suppress it as the fruit of his illegal arrest. The confession was conceded "voluntary" for Fifth Amendment purposes.

## Issue
Whether a confession obtained after an arrest made without probable cause must be suppressed as a fruit of the illegal arrest, or whether [[Miranda and Custodial Interrogation|Miranda warnings]], the lapse of several hours, a visitor, and a later-filed warrant sufficiently attenuated the taint.

## Rule
The confession must be suppressed unless the taint is purged. "[A] confession obtained through custodial interrogation after an illegal arrest should be excluded unless intervening events break the causal connection between the illegal arrest and the confession so that the confession is 'sufficiently an act of free will to purge the primary taint.'" — 457 U.S. at 690 (quoting *Brown v. Illinois*, 422 U.S. 590, 602). ^pin-690

A Fifth Amendment finding of voluntariness is "merely a threshold requirement for Fourth Amendment analysis"; were [[Miranda and Custodial Interrogation|Miranda warnings]] "viewed as a talisman that cured all Fourth Amendment violations," the guarantee would shrink to a "form of words." — [*Id.* at 690](https://www.courtlistener.com/opinion/110760/taylor-v-alabama/#:~:text=merely%20a%20threshold%20requirement%20for) (quoting *Brown*, 422 U.S. at 601, 603). ^pin-690b

## Application
The case was "a virtual replica of both *Brown* and *Dunaway*." "Petitioner was arrested without probable cause in the hope that something would turn up, and he confessed shortly thereafter without any meaningful intervening event." — *Id.* at 691. ^pin-691

The roughly six-hour interval was not significant where Taylor remained in custody, unrepresented, repeatedly questioned, fingerprinted, and placed in a lineup; the three [[Miranda and Custodial Interrogation|Miranda warnings]] did not break the chain; and the brief, emotionally fraught visit with his girlfriend did not free his will. The *[[Common Legal Terms#ex-parte|ex parte]]* arrest warrant filed mid-interrogation rested on fingerprints that "were themselves the fruit of petitioner's illegal arrest," so it could not supply [[Fruits and Attenuation|attenuation]]. The State failed to carry its burden of showing admissibility.

## Conclusion
The confession was the unattenuated fruit of the illegal arrest and should have been suppressed; the judgment of the Alabama Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Taylor* applies the [[Brown v. Illinois]] [[Fruits and Attenuation|attenuation]] factors and follows [[Dunaway v. New York]], reaffirming that a Fifth Amendment–voluntary confession can still be a suppressible Fourth Amendment fruit; the tainted fingerprints trace to [[Davis v. Mississippi]]. [[Kaupp v. Texas]] later applied the same analysis [[Common Legal Terms#per-curiam|per curiam]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny ([[Fruits and Attenuation|attenuation]])*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Taylor v. Alabama*, 457 U.S. 687 (1982) — https://www.courtlistener.com/opinion/110760/taylor-v-alabama/ — pinpoints: 690, 691, 692–693.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e293e3c38bf165f7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "457 U.S. 687 (1982)", "court": "U.S. Supreme Court", "neutral_cite": "1982 U.S. LEXIS 138", "official_citation_present": true, "parallel_cite": "102 S. Ct. 2664; 73 L. Ed. 2d 314", "title": "Taylor v. Alabama", "year": "1982"}}
{"assertion_id": "378f38ddb2758809", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Progeny (attenuation)", "title": "Taylor v. Alabama"}}
{"assertion_id": "a63a453b2e4ff868", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Related (cross-doctrine)", "title": "Taylor v. Alabama"}}
{"assertion_id": "bb982866476aae3c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession obtained after a warrantless arrest made without probable cause must be suppressed as the fruit of the illegal arrest where no significant intervening event broke the causal chain; Miranda warnings, the passage of a few hours, and a later ex parte warrant did not attenuate the taint.", "title": "Taylor v. Alabama"}}
{"assertion_id": "94fe82238ac5b93c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1982-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Taylor v. Alabama", "field_i_validity": "good_law", "scope_note": "Applies the Brown v. Illinois attenuation factors; the confession was conceded voluntary for Fifth Amendment purposes yet still suppressed as a Fourth Amendment fruit. Good law.", "title": "Taylor v. Alabama", "varies_by_point": "false"}}
{"assertion_id": "b16b4e5ba0a1fe2a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Taylor v. Alabama"}}
```

### lake record — Taylor v. Alabama

```json
{
  "schema_version": "s2.v1",
  "record_id": "Taylor v. Alabama",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Taylor v. Alabama",
    "case_name_short": "Taylor",
    "case_name_full": "Taylor v. Alabama",
    "input_case_name": "Taylor v. Alabama",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1982-06-23",
    "year": 1982,
    "docket": "81-5152",
    "cluster_id": 110760,
    "lead_opinion_id": 110760,
    "sibling_ids": [
      110760,
      9428855,
      9428856
    ],
    "absolute_url": "/opinion/110760/taylor-v-alabama/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "457 U.S. 687",
      "volume": "457",
      "reporter": "U.S.",
      "page": "687",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "102 S. Ct. 2664",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2664",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 314",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1982 U.S. LEXIS 138",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "138",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "457 U.S. 687",
        "volume": "457",
        "reporter": "U.S.",
        "page": "687",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 S. Ct. 2664",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2664",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 314",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1982 U.S. LEXIS 138",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "138",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "457 U.S. 687",
    "official_selection": {
      "court_class": "scotus",
      "selected": "457 U.S. 687",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-690",
      "page": null,
      "quote": "for Fifth Amendment purposes. ## Issue Whether a confession obtained after an arrest made without probable cause must be suppressed as a fruit of the illegal arrest, or whether Miranda warnings, the lapse of several hours, a visitor, and a later-filed warrant sufficiently attenuated the taint. ## Rule The confession must be suppressed unless the taint is purged.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-690b",
      "page": null,
      "quote": "merely a threshold requirement for Fourth Amendment analysis",
      "star_marker": "690",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9078,
      "fragment": "#:~:text=merely%20a%20threshold%20requirement%20for",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-691",
      "page": null,
      "quote": "a virtual replica of both *Brown* and *Dunaway*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1982-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Taylor v. Alabama",
    "varies_by_point": false,
    "scope_note": "Applies the Brown v. Illinois attenuation factors; the confession was conceded voluntary for Fifth Amendment purposes yet still suppressed as a Fourth Amendment fruit. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Rong He",
          "cluster_id": 4455505,
          "cite": [
            "2017 NY Slip Op 9172",
            "156 A.D.3d 907",
            "68 N.Y.S.3d 130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Weems v. State",
          "cluster_id": 1629131,
          "cite": [
            "167 S.W.3d 350",
            "2005 WL 486548"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Swazine Swindle",
          "cluster_id": 790194,
          "cite": [
            "407 F.3d 562",
            "2005 U.S. App. LEXIS 8245",
            "2005 WL 1110925"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
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
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cantu",
          "cluster_id": 22035,
          "cite": [
            "230 F.3d 148",
            "2000 WL 1481157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2364279,
          "cite": [
            "843 S.W.2d 252",
            "1992 Tex. App. LEXIS 3034",
            "1992 WL 357865"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Harris",
          "cluster_id": 112413,
          "cite": [
            "109 L. Ed. 2d 13",
            "110 S. Ct. 1640",
            "495 U.S. 14",
            "1990 U.S. LEXIS 2037",
            "58 U.S.L.W. 4457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. State",
          "cluster_id": 1575568,
          "cite": [
            "829 S.W.2d 191",
            "1992 Tex. Crim. App. LEXIS 62",
            "1992 WL 55274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez-Llamas v. Oregon",
          "cluster_id": 145628,
          "cite": [
            "165 L. Ed. 2d 557",
            "126 S. Ct. 2669",
            "548 U.S. 331",
            "2006 U.S. LEXIS 5177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wicker v. State",
          "cluster_id": 1733045,
          "cite": [
            "667 S.W.2d 137",
            "1984 Tex. Crim. App. LEXIS 610"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. State",
          "cluster_id": 2434027,
          "cite": [
            "724 S.W.2d 780",
            "1986 Tex. Crim. App. LEXIS 1216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harry Seidman",
          "cluster_id": 758049,
          "cite": [
            "156 F.3d 542",
            "159 L.R.R.M. (BNA) 2211",
            "1998 U.S. App. LEXIS 21924",
            "1998 WL 574761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 5687957,
          "cite": [
            "66 N.Y.2d 398",
            "488 N.E.2d 439",
            "497 N.Y.S.2d 618",
            "1985 N.Y. LEXIS 17918"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abram v. State",
          "cluster_id": 1096122,
          "cite": [
            "606 So. 2d 1015",
            "1992 WL 223914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Armenta",
          "cluster_id": 1125086,
          "cite": [
            "948 P.2d 1280"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmy Dewitt Webster, Sr., Candido Daniel Santiago, Barry Weinreich, Joe Buhajla, Arthur Byron Murphy, and Clarence Royalston",
          "cluster_id": 445460,
          "cite": [
            "750 F.2d 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lanier v. State",
          "cluster_id": 1832223,
          "cite": [
            "450 So. 2d 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Green",
          "cluster_id": 739711,
          "cite": [
            "111 F.3d 515",
            "1997 WL 175484"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cipriano",
          "cluster_id": 1844552,
          "cite": [
            "429 N.W.2d 781",
            "431 Mich. 315"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lenin M. Jerez and Carlos M. Solis",
          "cluster_id": 737426,
          "cite": [
            "108 F.3d 684"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Manbeck, United States of America v. Kenneth Herring, United States of America v. Mark Huiet Sale, United States of America v. Lorenz Josephus Proden, United States of America v. Kermit Theodore Brogden, United States of America v. John Wesley Flannel, United States of America v. Gary Gallopo, United States of America v. John Benjamin Barton, Jr., Jessie Lee Mallory, and Arthur Duncan, United States of America v. John O'hare, Eddie Brantley, Thomas Earnest Folske, Thomas Sams Hightower, Timothy Allen Laxton, Harrell Lewis, Jr., and John Isidore Stevens, United States of America v. Aaron Douglas Staetter, John Michael Iyoob, James Anthony Hastings, and Gregory Michael Scott, United States of America v. David Martin Summerville",
          "cluster_id": 441989,
          "cite": [
            "744 F.2d 360",
            "1984 U.S. App. LEXIS 18698"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Little v. State",
          "cluster_id": 1562842,
          "cite": [
            "758 S.W.2d 551",
            "1988 Tex. Crim. App. LEXIS 50",
            "1988 WL 23631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Iduarte",
          "cluster_id": 1487736,
          "cite": [
            "268 S.W.3d 544",
            "2008 Tex. Crim. App. LEXIS 1626",
            "2008 WL 4724143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110760 OR 9428855 OR 9428856) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzY3NzEyMDAwMDAmcz0xMTIwOTI0JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110760+OR+9428855+OR+9428856%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110760 OR 9428855 OR 9428856)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzImcz0xMDI1NzM1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110760+OR+9428855+OR+9428856%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110760 OR 9428855 OR 9428856)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110760 OR 9428855 OR 9428856)",
    "indexed_citing_opinions": 413,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110760,
        "count": 373,
        "count_source": "search"
      },
      {
        "opinion_id": 9428855,
        "count": 59,
        "count_source": "search"
      },
      {
        "opinion_id": 9428856,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 633,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/taylor-v-alabama.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU1Mjk2MDUmcz00NDIxNDc4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110760+OR+9428855+OR+9428856%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110760,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 108538,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 372011,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 374894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 1596133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 1596287,
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
    "date_created": "2026-07-05T21:12:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:13:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:13:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:18:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:13:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Taylor v. Alabama

```
<div>
<center><b><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">457 U.S. 687</a></span> (1982)</b></center>
<center><h1>TAYLOR<br>
v.<br>
ALABAMA</h1></center>
<center>No. 81-5152.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 23, 1982.</center>
<center>Decided June 23, 1982.</center>
CERTIORARI TO THE SUPREME COURT OF ALABAMA
<p><span class="star-pagination">*688</span> <i>Robert M. Beno</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Thomas R. Allison,</i> Assistant Attorney General of Alabama, argued the cause for respondent. With him on the brief was <i>Charles A. Graddick,</i> Attorney General.<sup>[*]</sup></p>
<p><i>Fred E. Inbau, Wayne W. Schmidt, James P. Manak, Patrick F. Healy, William K. Lambie, Richard J. Brzeczek, Frank G. Carrington, Courtney A. Evans, Robert K. Corbin,</i> Attorney General of Arizona, and <i>Steven J. Twist,</i> Chief Assistant Attorney General, <i>Tyrone C. Fahner,</i> Attorney General of Illinois, and <i>Melbourne Noel,</i> Chief Assistant Attorney General, and <i>William L. Parker, Jr.,</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging affirmance.</p>
<p>JUSTICE MARSHALL delivered the opinion of the Court.</p>
<p>This case presents the narrow question whether petitioner's confession should have been suppressed as the fruit of an illegal arrest. The Supreme Court of Alabama held that the evidence was properly admitted. Because the decision below is inconsistent with our decisions in <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), and <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), we reverse.</p>
<p></p>
<h2>I</h2>
<p>In 1978, a grocery store in Montgomery, Ala., was robbed. There had been a number of robberies in this area, and the police had initiated an intensive manhunt in an effort to apprehend the robbers. An individual who was at that time incarcerated on unrelated charges told a police officer that "he had heard that [petitioner] Omar Taylor was involved in the robbery." App. 4. This individual had never before given similar information to this officer, did not tell the officer where he had heard this information, and did not provide any details of the crime. This tip was insufficient to give <span class="star-pagination">*689</span> the police probable cause to obtain a warrant or to arrest petitioner.</p>
<p>Nonetheless, on the basis of this information, two officers arrested petitioner without a warrant. They told petitioner that he was being arrested in connection with the grocery-store robbery, searched him, and took him to the station for questioning. Petitioner was given the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). At the station, he was fingerprinted, readvised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, questioned, and placed in a lineup. The victims of the robbery were unable to identify him in the lineup. The police told petitioner that his fingerprints matched those on some grocery items that had been handled by one of the participants in the robbery. After a short visit with his girlfriend and a male companion, petitioner signed a waiver-of-rights form and executed a written confession. The form and the signed confession were admitted into evidence.</p>
<p>Petitioner objected to the admission of this evidence at his trial. He argued that his warrantless arrest was not supported by probable cause, that he had been involuntarily transported to the police station, and that the confession must be suppressed as the fruit of this illegal arrest. The trial court overruled this objection, and petitioner was convicted. On appeal, the Alabama Court of Criminal Appeals reversed, <span class="citation multiple-matches"><a href="/c/So.%202d/399/875/">399 So. 2d 875</a></span> (1980), holding that the facts of this case are virtually indistinguishable from those presented to this Court in <i>Dunaway</i> v. <i>New <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">York, supra</a></span></i><i>,</i> and that the confession should not have been admitted into evidence. The Alabama Supreme Court reversed the Court of Criminal Appeals, <span class="citation" data-id="1596133"><a href="/opinion/1596133/taylor-v-state/" aria-description="Citation for case: Taylor v. State">399 So. 2d 881</a></span> (1981), and we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./454/963/">454 U. S. 963</a></span> (1981).</p>
<p></p>
<h2>II</h2>
<p>In <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois, supra</a></span></i><i>,</i> and <i>Dunaway</i> v. <i>New <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">York, supra</a></span></i><i>,</i> the police arrested suspects without probable cause. The suspects were transported to police headquarters, advised of their <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and interrogated. They confessed <span class="star-pagination">*690</span> within two hours of their arrest. This Court held that the confessions were not admissible at trial, reasoning that a confession obtained through custodial interrogation after an illegal arrest should be excluded unless intervening events break the causal connection between the illegal arrest and the confession so that the confession is " `sufficiently an act of free will to purge the primary taint.' " <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois, supra,</a></span></i> at 602 (quoting <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 486</a></span> (1963)). See also <i>Dunaway</i> v. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#217" aria-description="Citation for case: Dunaway v. New York"><i>New York, supra,</i> at 217</a></span>. This Court identified several factors that should be considered in determining whether a confession has been purged of the taint of the illegal arrest: "[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct." <i>Brown</i> v. <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois"><i>Illinois, supra,</i> at 603-604</a></span> (citations and footnote omitted); <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 218</a></span>. The State bears the burden of proving that a confession is admissible. <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Ibid.</a></span></i></p>
<p>In <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> this Court firmly established that the fact that the confession may be "voluntary" for purposes of the Fifth Amendment, in the sense that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were given and understood, is not by itself sufficient to purge the taint of the illegal arrest. In this situation, a finding of "voluntariness" for purposes of the Fifth Amendment is merely a threshold requirement for Fourth Amendment analysis. See <i>Dunaway</i> v. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#217" aria-description="Citation for case: Dunaway v. New York"><i>New York, supra,</i> at 217</a></span>. The reason for this approach is clear: "[t]he exclusionary rule, . . . when utilized to effectuate the Fourth Amendment, serves interests and policies that are distinct from those it serves under the Fifth" Amendment. <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 601</a></span>. If <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were viewed as a talisman that cured all Fourth Amendment violations, then the constitutional guarantee against unlawful searches and seizures would be reduced to a mere " `form of words.' " <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 603 (quoting <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#648" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 648</a></span> (1961)).</p>
<p>This case is a virtual replica of both <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>.</i> <span class="star-pagination">*691</span> Petitioner was arrested without probable cause in the hope that something would turn up, and he confessed shortly thereafter without any meaningful intervening event. The State's arguments to the contrary are unpersuasive. The State begins by focusing on the temporal proximity of the arrest and the confession. It observes that the length of time between the illegal arrest and the confession was six hours in this case, while in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> the incriminating statements were obtained within two hours. However, a difference of a few hours is not significant where, as here, petitioner was in police custody, unrepresented by counsel, and he was questioned on several occasions, fingerprinted, and subjected to a lineup. The State has not even demonstrated the amount of this time that was spent in interrogation, arguing only that petitioner "had every opportunity to consider his situation, to organize his thoughts, to contemplate his constitutional rights, and to exercise his free will." Brief for Respondent 11.</p>
<p>The State points to several intervening events that it argues are sufficient to break the connection between the illegal arrest and petitioner's confession. It observes that petitioner was given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings three times. As our foregoing discussion of <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> demonstrates, however, the State's reliance on the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings is misplaced. The State also observes that petitioner visited with his girlfriend and a male companion before he confessed. This claim fares no better. According to the officer and petitioner, these two visitors were outside the interrogation room where petitioner was being questioned. After petitioner signed a waiver-of-rights form, he was allowed to meet with these visitors. The State fails to explain how this 5-to 10-minute visit, after which petitioner immediately recanted his former statements that he knew nothing about the robbery and signed the confession, could possibly have contributed to his ability to consider carefully and objectively his options and to exercise his free will. This suggestion <span class="star-pagination">*692</span> is particularly dubious in light of petitioner's uncontroverted testimony that his girlfriend was emotionally upset at the time of this visit.<sup>[1]</sup> If any inference could be drawn, it would be that this visit had just the opposite effect.</p>
<p>The State points to an arrest warrant filed after petitioner had been arrested and while he was being interrogated as another significant "intervening event." While petitioner was in custody, the police determined that the fingerprints on some grocery items matched those that they had taken from petitioner immediately after his arrest. Based on this comparison, an arrest warrant was filed. The filing of this warrant, however, is irrelevant to whether the confession was the fruit of the illegal arrest. This case is not like <i>Johnson</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424879"><a href="/opinion/108538/johnson-v-louisiana/" aria-description="Citation for case: Johnson v. Louisiana">406 U. S. 356</a></span> (1972), where the defendant was brought before a committing Magistrate who advised him of his rights and set bail. Here, the arrest warrant was filed <i>ex parte,</i> based on the comparison of the fingerprints found at the scene of the crime and petitioner's fingerprints, which had been taken immediately after his arrest. The initial fingerprints, <span class="star-pagination">*693</span> which were themselves the fruit of petitioner's illegal arrest, see <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), and which were used to extract the confession from petitioner, cannot be deemed sufficient "attenuation" to break the connection between the illegal arrest and the confession merely because they also formed the basis for an arrest warrant that was filed while petitioner was being interrogated.<sup>[2]</sup></p>
<p>Finally, the State argues that the police conduct here was not flagrant or purposeful, and that we should not follow our decisions in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> for that reason. However, we fail to see any relevant distinction between the conduct here and that in <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>.</i> In this case, as in <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> the police effectuated an investigatory arrest without probable cause, based on an uncorroborated informant's tip, and involuntarily transported petitioner to the station for interrogation in the hope that something would turn up. The fact that the police did not physically abuse petitioner, or that the confession they obtained may have been "voluntary" for purposes of the Fifth Amendment, does not cure the illegality of the initial arrest. Alternatively, the State contends that the police conduct here argues for adopting a "good faith" exception to the exclusionary rule. To date, we have not recognized such an exception, and we decline to do so here.</p>
<p><span class="star-pagination">*694</span> In sum, petitioner's confession was the fruit of his illegal arrest. Under our decisions in <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois</a></span></i> and <i>Dunaway</i> v. <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">New York</a></span></i><i>,</i> the confession clearly should not have been admitted at his trial. Accordingly, we reverse the decision of the Alabama Supreme Court and remand this case for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE O'CONNOR, with whom THE CHIEF JUSTICE, JUSTICE POWELL, and JUSTICE REHNQUIST join, dissenting.</p>
<p>The Court holds today that Omar Taylor's detailed confession was the fruit of an illegal arrest, and consequently, should be suppressed. Because I conclude that neither the facts nor the law supports the Court's analysis, I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>In the course of their investigation of the Moseley robbery, Montgomery police questioned Charles Martin, who was being held on unrelated rape and robbery charges. Martin stated that "he had heard that Omar Taylor was involved in the robbery of Moseley's Grocery," Tr. 6, but the police made no attempt to establish either Martin's credibility as an informant or the reliability of the information he provided.<sup>[1]</sup></p>
<p>Based only on this tip, which did not provide probable cause, Sergeants Alford and Rutland arrested Taylor a little before 3 p.m. on January 4, 1979. At that time, they told him why he was being arrested and advised him of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, but asked him no questions regarding the robbery. Tr. 20, 24. When they arrived at the police station, the officers turned Taylor over to detectives.</p>
<p>After Taylor had been fingerprinted and signed a form <span class="star-pagination">*695</span> acknowledging his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, Detective Wilson questioned him for about 15 minutes, Tr. 48, and placed him in a lineup before one of the victims, Mrs. Moseley. <i>Id.,</i> at 37-38. At the lineup, which lasted about an hour, <i>id.,</i> at 48, Mrs. Moseley was unable to identify the petitioner. Following the lineup, Detective Wilson told Taylor that his fingerprints matched the fingerprints removed from grocery items handled by one of the robbers. Nevertheless, the petitioner denied knowledge of the robbery.</p>
<p>Toward 9 p.m. that evening, Detective Hicks readvised Taylor of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, Tr. 25, and Taylor once again read and signed a form setting forth his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Tr. 28, 125. At no time did Taylor ask for a lawyer or indicate that he did not want to talk to police. <i>Id.,</i> at 28-29, 35, 40. During his 5- to 10-minute interview with Taylor, Detective Hicks confronted him with the fingerprint evidence. <i>Id.,</i> at 36. Hicks urged the petitioner to cooperate with the police, but carefully refrained from making him any promises, stating that at most he could inform the judge of the petitioners cooperation. <i>Id.,</i> at 31, 34. Taylor continued to deny involvement in the robbery. <i>Id.,</i> at 35-36.</p>
<p>Following this conversation, both the petitioner's girlfriend and his neighbor came to the police station and requested to speak with him. When Taylor indicated that he wanted to speak with his friends, Detective Hicks left them alone in his office for several minutes.<sup>[2]</sup> After that meeting, <span class="star-pagination">*696</span> the petitioner confessed to the crime, and signed a detailed written confession.<sup>[3]</sup></p>
<p>Before trial, the petitioner moved to suppress his confession, <span class="star-pagination">*697</span> arguing that it was the product of an illegal arrest, and that it had been obtained in violation of his Fifth and Sixth Amendment rights. The trial judge assumed that the arrest was illegal,<sup>[4]</sup> but found that the confession was voluntary, consistent with the Fifth and Sixth Amendments, and that "there were enough intervening factors between the arrest and confession" to overcome the taint of the illegal arrest. <i>Id.,</i> at 116. Accordingly, he admitted the confession.</p>
<p></p>
<h2>II</h2>
<p>Although the Court misapprehends the facts of the present case, it has stated correctly the controlling substantive law. In the Court's words, "a confession obtained through custodial interrogation after an illegal arrest should be excluded unless intervening events break the causal connection between the illegal arrest and the confession so that the confession is `sufficiently an act of free will to purge the primary taint.' " <i>Ante,</i> at 690 (quoting <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 602</a></span> (1975)).</p>
<p>In <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</i> this Court emphasized that "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings are an important factor . . . in determining whether the confession [was] obtained by exploitation of an illegal arrest." <i>Id.,</i> at 603.<sup>[5]</sup> The Court did not discount the significance <span class="star-pagination">*698</span> of other factors, however, noting that "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings, <i>alone</i> and <i>per se,</i> cannot always make the act sufficiently a product of free will to break, for Fourth Amendment purposes, the causal connection between the illegality and the confession." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> Brown</i> holds, therefore, that not only <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, but also "[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, and, particularly, the purpose and flagrancy of the official misconduct are all relevant." <i>Id.,</i> at 603-604 (footnotes and citations omitted).</p>
<p>In light of those factors, the <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> Court reviewed the record and found that "Brown's first statement was separated from his illegal arrest by less than two hours, and [that] there was no intervening event of significance whatsoever." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 604</a></span>. Moreover, the police conduct in arresting Brown was particularly egregious. The "impropriety of the arrest was obvious," and the "manner in which Brown's arrest was effected gives the appearance of having been calculated to cause surprise, fright, and confusion." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 605</a></span>. The Court held that as a consequence the confession should have been suppressed.</p>
<p>Four Terms later, in <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#204" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 204</a></span> (1979), this Court reaffirmed the <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> rule that in order to use at trial statements obtained following an arrest on less than probable cause</p>
<blockquote>"the prosecution must show not only that the statements meet the Fifth Amendment voluntariness standard, but also that the causal connection between the statements and the illegal arrest is broken sufficiently to purge the primary taint of the illegal arrest."</blockquote>
<p>Finding the facts in <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> to be "virtually a replica of the situation in <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York"><i>Brown," id.,</i> at 218</a></span>, the Court held that the petitioner's confession should have been suppressed. Critical to the Court's holding was its observation that the petitioner <span class="star-pagination">*699</span> "confessed without any intervening event of significance." <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Ibid.</a></span></i> See <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#219" aria-description="Citation for case: Dunaway v. New York"><i>id.,</i> at 219</a></span> ("No intervening events broke the connection between petitioner's illegal detention and his confession").</p>
<p></p>
<h2>III</h2>
<p>Our task is to apply the law as articulated in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> to the facts of this case.</p>
<p>The first significant consideration is that following his unlawful arrest, Taylor was warned on three separate occasions that he</p>
<blockquote>"had a right to remain silent, [and] anything he said could be used against him in a court of law[;] he had the right to have an attorney present, [and] if he could not afford one, the State would appoint one for him[;] he could answer questions but he could stop answering at any time." Tr. 23.</blockquote>
<p>Under <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> these warnings must be counted as "an important factor . . . in determining whether the confession [was] obtained by exploitation of an illegal arrest," <i>Brown</i> v. <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois"><i>Illinois, supra,</i> at 603</a></span>, though they are, standing alone, insufficient to prove that the primary taint of an illegal arrest had been purged.</p>
<p>Second, in contrast to the facts in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</i> the facts in the present case show that the petitioner was not subjected to intimidating police misconduct. In <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</i> police had broken into the petitioner's house and searched it. When the petitioner later came home, two officers pointed their guns at him and arrested him, leading the Court to conclude that "[t]he manner in which [the petitioner's] arrest was effected gives the appearance of having been calculated to cause surprise, fright, and confusion." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 605</a></span>. By contrast, nothing in the record before us indicates that the petitioner's arrest was violent, or designed to "cause surprise, fright, and confusion." Instead, Montgomery officers approached <span class="star-pagination">*700</span> Taylor, asked him his name, and told him that he was under arrest for the Moseley robbery. They then searched him, advised him of his rights, and took him to the police station.</p>
<p>Third, while in both <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> there was "no intervening event of significance whatsoever," <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 604</a></span>, in the present case Taylor's girlfriend and neighbor came to the police station and asked to speak with him. Before meeting with his two friends, the petitioner steadfastly had denied involvement in the Moseley robbery. Immediately following the meeting, the petitioner gave a complete and detailed confession of his participation in the armed robbery. This meeting between the petitioner and his two friends, as described by the police in their testimony at the suppression hearing, plainly constituted an intervening circumstance.</p>
<p>Finally, the record reveals that the petitioner spent most of the time between his arrest and confession by himself.<sup>[6]</sup> In <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> and <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</i> by contrast, the defendants were interrogated continuously before they made incriminating statements.</p>
<p>In sum, when these four factors are considered together,<sup>[7]</sup> it is obvious that there is no sufficient basis on which to overturn the trial court's finding that "there were enough intervening factors" to overcome the taint of the illegal arrest. In fact, I believe it is clear that the State carried its burden of proof. The petitioner was warned of his rights to remain silent <span class="star-pagination">*701</span> and to have a lawyer present, and there is no dispute that he understood those rights or that he waived them voluntarily and without coercion. After receiving three sets of such warnings, he met with his girlfriend and neighbor, <i>at his request.</i> Following that meeting, at which no police officers were present, the petitioner decided to confess to his participation in the robbery. The petitioner's confession was not proximately caused by his illegal arrest, but was the product of a decision based both on knowledge of his constitutional rights and on the discussion with his friends. Accordingly, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Arthur F. Mathews</i> and <i>James E. Coleman, Jr.,</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging reversal.</p>
<p>[1]  According to petitioner, his girlfriend became upset upon hearing the officer advise petitioner to cooperate. App. 16. Contrary to the allegations in the dissent, at no point did the officer contradict petitioner's version of his girlfriend's emotional state or petitioner's statement that his girlfriend was present at the time the officer advised him to cooperate. In fact, the testimony from both petitioner and the officer with respect to this visit are consistent. The officer testified only that he advised petitioner to cooperate between the time petitioner signed a rights form at the commencement of this interrogation period and the time that petitioner signed the statement of confession. Tr. 31, 136-137. He also testified that during this same interval, he allowed the short visit between petitioner and his girlfriend. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Ibid.</a></span></i> The District Court made no findings of fact with respect to these incidents. In any event, even assuming the accuracy of the dissent's version of the facts, compare <i>post,</i> at 695, and n. 2, with Tr. 31, 136-137, the dissent offers no explanation for its conclusion that this 5-to 10-minute visit should be viewed as an intervening event that purges the taint of the illegal arrest.</p>
<p>[2]  Petitioner also raises an ambiguous objection to the admission of fingerprint evidence at his trial. The trial court granted petitioner's motion to suppress the initial fingerprints as the fruit of his illegal arrest under <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), and granted the State's motion to take petitioner's fingerprints at trial. The nature of petitioner's objection to the admission of any fingerprint evidence at trial is unclear, and it is also uncertain whether an objection to the procedure used for taking the second set of fingerprints has been properly preserved for our review. In any event, we need not reach this issue because we reverse the decision on the ground that the confession should not have been admitted. To the extent that petitioner still may challenge the fingerprinting procedure employed below, the state courts should be given the opportunity to address this challenge in the first instance.</p>
<p>[1]  The police, however, suspected Martin of complicity in the Moseley robbery, Tr. 15. It later developed that Martin had instigated, planned, and participated in the robbery.</p>
<p>[2]  The Court's rather different account of this meeting apparently stems from a decision to accept the testimony most favorable to the holding it wants to reach. That decision, however, runs counter to the longstanding practice of federal appellate courts to uphold the denial of the motion to suppress if, in the absence of any express findings by the district court, there is any reasonable view of the evidence to support it. See <i>United States</i> v. <i>Payton,</i> <span class="citation" data-id="374894"><a href="/opinion/374894/united-states-v-william-charles-payton/#923" aria-description="Citation for case: United States v. William Charles Payton">615 F. 2d 922, 923</a></span> (CA1), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./446/969/">446 U. S. 969</a></span> (1980); <i>United States</i> v. <i>Vicknair,</i> <span class="citation" data-id="372011"><a href="/opinion/372011/united-states-v-vicknair/#376" aria-description="Citation for case: United States v. Vicknair">610 F. 2d 372, 376, n. 4</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/823/">449 U. S. 823</a></span> (1980). In the present case, the officer testified that Taylor's "girlfriend came to us and said she wanted to talk to Omar, and we told Omar she was outside and he wanted to talk to her. And at that time, we let him talk to her." Tr. 35. Detective Hicks specifically denied that he had urged Taylor to talk to his girlfriend. <i>Id.,</i> at 35, 133-134. The detective acknowledged that he had told the petitioner that he could inform the judge of the petitioner's cooperation, but he expressly denied making any other statements to Taylor or his girlfriend about "cooperation." <i>Id.,</i> at 31, 134.
</p>
<p>The petitioner, of course, had a vastly different version. He testified that the police had brought his girlfriend into the room and told him, in her presence, that he was facing 10 years to life in prison, but that if he cooperated they might be able to arrange a suspended sentence or probation. Upon hearing that remark, the petitioner's girlfriend became upset and began to cry, at which point the police left the petitioner alone with his friends. <i>Id.,</i> at 52. As we noted above, the police expressly denied making any such statements. More importantly, upon comparing the two versions, it becomes clear that in an effort to support its holding, the Court has parsed through the petitioner's story and plucked those tidbits that the police did not expressly contradict. This method of setting forth the facts of a case on appellate review hardly comports with the rule that an appellate court must adopt any reasonable view of the evidence that supports the trial court's ruling.</p>
<p>Since there is nothing unreasonable about the police account of the meeting between the petitioner and his friends, that version is the one we must accept on review. At the hearing, Detective Hicks testified that after Taylor asked to speak with his friends, the police left them alone together. There is no suggestion, other than the petitioner's discredited version of the meeting, that the police said anything to the petitioners girlfriend, or that she became upset. Thus, the Court errs in stating that the petitioner's girlfriend became upset because of statements made by the police, and in intimating that the police created a coercive atmosphere in which the petitioner could not carefully consider his options and, on the basis of his friends' advice, decide to confess to the robbery.</p>
<p>[3]  In that confession, the petitioner stated that Charles Martin approached him with guns and a plan to rob Moseley's Grocery. Taylor's role in the robbery was to distract Mr. Moseley by buying some groceries. Just before his accomplices pulled out their guns, Taylor put down the groceries and walked outside to see whether an approaching car was a police car. When he saw that it was not a police car, he began to reenter the store, but stopped when he saw the robbery taking place. Thereafter he fled, met his cofelons at a preassigned place, and took his share of the money. <i>Id.,</i> at 128-132.</p>
<p>[4]  In fact, the State did not seriously contend that the arrest had been based on probable cause. See <i>id.,</i> at 8, 10.</p>
<p>[5]  The holding in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> was derived from this Court's seminal decision in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), in which we rejected a "but for" test for determining whether to suppress evidence gathered following a Fourth Amendment violation.
</p>
<p>"We need not hold that all evidence is `fruit of the poisonous tree' simply because it would not have come to light but for the illegal actions of the police. Rather, the more apt question in such a case is `whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.' Maguire, Evidence of Guilt, 221 (1959)." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 487-488</a></span>.</p>
<p>[6]  The petitioner confessed some six hours after his arrest. As JUSTICE STEVENS noted in his concurring opinion in <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> the "temporal relationship between the arrest and the confession may be an ambiguous factor," <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#220" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 220</a></span>, for a lengthy detention could be used to exploit an illegal arrest at least as easily as a brief detention. In the present case, there seems to be nothing remarkable, one way or the other, about the length of detention.</p>
<p>[7]  The Court has taken each circumstance out of context and examined it to see whether it alone would be enough to purge the taint of the illegal arrest. The Court's failure to consider the circumstances of this case as a whole may have contributed to its erroneous conclusion.</p>

</div>
```

---

## GROUP: content/cases/Texas v. Brown.md  (`case`, 5 assertions)

### content_page

```
---
title: "Texas v. Brown"
type: case
citation: "460 U.S. 730 (1983)"
parallel_cite: "103 S. Ct. 1535; 75 L. Ed. 2d 502; 51 U.S.L.W. 4361"
neutral_cite: 1983 U.S. LEXIS 143
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-04-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-04-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Texas v. Brown
  varies_by_point: false
  scope_note: "Plurality opinion; its 'immediately apparent = probable cause' reading is settled and was confirmed for plain view in Arizona v. Hicks and Horton v. California."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110901/texas-v-brown/"
  cluster_id: 110901
  opinion_id: 9429131
  identity_checked: false
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
related: ["[[Coolidge v. New Hampshire]]", "[[Arizona v. Hicks]]", "[[Horton v. California]]", "[[Minnesota v. Dickerson]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-view"]
holding: "'Immediately apparent' means probable cause, not certainty ('an unhappy choice of words'); shining a flashlight into a car interior is not a search."
lake:
  record_id: Texas v. Brown
  status: under_review
  projected_at: 2026-07-06
---

# Texas v. Brown

*460 U.S. 730 (1983) (plurality)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At a routine driver's-license checkpoint an officer asked Brown for his license and, at the same time, shined a flashlight into the car. He saw Brown withdraw his hand from his pocket holding an opaque, knotted green party balloon — a packaging he knew from experience to be used for narcotics — and saw plastic vials, loose white powder, and an open bag of balloons in the glove compartment. The balloon held heroin.

## Issue
Whether seizure of the balloon was justified under the [[Plain View Doctrine|plain-view doctrine]] — in particular, what "immediately apparent" requires — and whether using a flashlight to look into the car's interior was itself a search.

## Rule
Illuminating a car's interior is not a search: the officer's "action in shining his flashlight to illuminate the interior of Brown's car trenched upon no right secured to the latter by the Fourth Amendment." — 460 U.S. at 739–40. ^pin-739

"Immediately apparent" does not mean certainty. The plurality explained that "the use of the phrase 'immediately apparent' was very likely an unhappy choice of words, since it can be taken to imply that an unduly high degree of certainty as to the incriminatory character of evidence is necessary for an application of the 'plain view' doctrine." — *Id.* at 741. ^pin-741

The standard is probable cause: the doctrine "does not demand any showing that such a belief be correct or more likely true than false. A 'practical, nontechnical' probability that incriminating evidence is involved is all that is required." — *Id.* at 742. ^pin-742

## Application
On these facts the officer had a lawful vantage point at the lawful checkpoint, used a flashlight (no search) to see into the car, and — drawing on his experience that knotted party balloons are used to carry narcotics, reinforced by the vials, powder, and bag of balloons in plain view — had probable cause to believe the balloon contained contraband. That practical probability satisfied "immediately apparent," so the warrantless seizure of the balloon was justified under the [[Plain View Doctrine|plain-view doctrine]].

## Conclusion
The seizure of the balloon was lawful; the Texas court's suppression was reversed. The "immediately apparent" element of plain view requires only probable cause, and shining a flashlight into a car is not a search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality).
- The probable-cause reading of "immediately apparent" was confirmed in [[Arizona v. Hicks]] (plain view requires probable cause) and the three-element plain-view test was restated in [[Horton v. California]]; the "immediately apparent" / probable-cause logic also governs the plain-feel rule of [[Minnesota v. Dickerson]].

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*

## Sources
- *Texas v. Brown*, 460 U.S. 730 (1983) (plurality) — https://www.courtlistener.com/opinion/110901/texas-v-brown/ — pinpoints: 739–40, 741, 742.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6142475f3717281f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "460 U.S. 730 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 143", "official_citation_present": true, "parallel_cite": "103 S. Ct. 1535; 75 L. Ed. 2d 502; 51 U.S.L.W. 4361", "title": "Texas v. Brown", "year": "1983"}}
{"assertion_id": "2b255873742640c0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "'Immediately apparent' means probable cause, not certainty ('an unhappy choice of words'); shining a flashlight into a car interior is not a search.", "title": "Texas v. Brown"}}
{"assertion_id": "8ccf4865406a7b6b", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key — Progeny / Refinement", "title": "Texas v. Brown"}}
{"assertion_id": "16f327cbb1abb713", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Texas v. Brown"}}
{"assertion_id": "9c0fa3b52b6c1b20", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-04-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Texas v. Brown", "field_i_validity": "good_law", "scope_note": "Plurality opinion; its 'immediately apparent = probable cause' reading is settled and was confirmed for plain view in Arizona v. Hicks and Horton v. California.", "title": "Texas v. Brown", "varies_by_point": "false"}}
```

### lake record — Texas v. Brown

```json
{
  "schema_version": "s2.v1",
  "record_id": "Texas v. Brown",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Texas v. Brown",
    "case_name_short": "Brown",
    "case_name_full": "Texas v. Brown",
    "input_case_name": "Texas v. Brown",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-04-19",
    "year": 1983,
    "docket": null,
    "cluster_id": 110901,
    "lead_opinion_id": 9429131,
    "sibling_ids": [
      110901,
      9429131,
      9429132,
      9429133,
      9429134
    ],
    "absolute_url": "/opinion/110901/texas-v-brown/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "460 U.S. 730",
      "volume": "460",
      "reporter": "U.S.",
      "page": "730",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1535",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 502",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "502",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4361",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4361",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 143",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "460 U.S. 730",
        "volume": "460",
        "reporter": "U.S.",
        "page": "730",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1535",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 502",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "502",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 143",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4361",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4361",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "460 U.S. 730",
    "official_selection": {
      "court_class": "scotus",
      "selected": "460 U.S. 730",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-739",
      "page": null,
      "quote": "requires \u2014 and whether using a flashlight to look into the car's interior was itself a search. ## Rule Illuminating a car's interior is not a search: the officer's",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-741",
      "page": null,
      "quote": "Immediately apparent",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-742",
      "page": null,
      "quote": "does not demand any showing that such a belief be correct or more likely true than false. A 'practical, nontechnical' probability that incriminating evidence is involved is all that is required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-04-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Texas v. Brown",
    "varies_by_point": false,
    "scope_note": "Plurality opinion; its 'immediately apparent = probable cause' reading is settled and was confirmed for plain view in Arizona v. Hicks and Horton v. California.",
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
        "journal_ref": "Texas v. Brown:lane1_negative"
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
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tanguay",
          "cluster_id": 4598184,
          "cite": [
            "918 F.3d 1"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
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
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532255,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532252,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4409778,
          "cite": [
            "2017 COA 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane1_negative"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Hicks",
          "cluster_id": 111834,
          "cite": [
            "94 L. Ed. 2d 347",
            "107 S. Ct. 1149",
            "480 U.S. 321",
            "1987 U.S. LEXIS 1056",
            "55 U.S.L.W. 4258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saldano v. State",
          "cluster_id": 1591817,
          "cite": [
            "70 S.W.3d 873",
            "2002 Tex. Crim. App. LEXIS 49",
            "2002 WL 385848"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Harris",
          "cluster_id": 820744,
          "cite": [
            "185 L. Ed. 2d 61",
            "133 S. Ct. 1050",
            "568 U.S. 237",
            "2013 U.S. LEXIS 1121"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
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
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Altria Group, Inc. v. Good",
          "cluster_id": 145925,
          "cite": [
            "172 L. Ed. 2d 398",
            "129 S. Ct. 538",
            "555 U.S. 70",
            "2008 U.S. LEXIS 9127",
            "77 U.S.L.W. 4021"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chaplaincy of Full Gospel Churches v. England",
          "cluster_id": 186744,
          "cite": [
            "454 F.3d 290",
            "372 U.S. App. D.C. 94",
            "65 Fed. R. Serv. 3d 808",
            "2006 U.S. App. LEXIS 16952",
            "103 Fair Empl. Prac. Cas. (BNA) 171"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Brown:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110901 OR 9429131 OR 9429132 OR 9429133 OR 9429134) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY5NTc3NjAwMDAwJnM9NDI0MTkyNSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110901+OR+9429131+OR+9429132+OR+9429133+OR+9429134%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110901 OR 9429131 OR 9429132 OR 9429133 OR 9429134)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTEmcz01NjcyMTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110901+OR+9429131+OR+9429132+OR+9429133+OR+9429134%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110901 OR 9429131 OR 9429132 OR 9429133 OR 9429134)",
        "reviewed": 83,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 83,
        "triage_read": 2,
        "triage_snippet_classified": 81
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110901 OR 9429131 OR 9429132 OR 9429133 OR 9429134)",
    "indexed_citing_opinions": 1905,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110901,
        "count": 1645,
        "count_source": "search"
      },
      {
        "opinion_id": 9429131,
        "count": 303,
        "count_source": "search"
      },
      {
        "opinion_id": 9429132,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429133,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429134,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3147,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/texas-v-brown.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNzE3Nzkmcz0xMDM2MjY3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110901+OR+9429131+OR+9429132+OR+9429133+OR+9429134%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110901,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 102505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 296598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 303966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 313647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 316481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 328010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 329736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 329973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 330213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 338727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 359737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 374770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 391014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 399010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 401019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 403902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1193476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1208933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1239224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1362880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1526891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1631203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1687759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1710492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1739285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 1774097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 2222769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 2418802,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110901,
        "cited_id": 2448737,
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
    "date_created": "2026-07-05T21:24:55Z",
    "date_modified": "2026-07-06T08:56:23Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:25:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:25:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:28:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:25:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Texas v. Brown

```
<opinion type="majority">
<author id="b794-9">Justice Rehnquist</author>
<p id="A7s">announced the judgment of the Court and delivered an opinion, in which The Chief Justice, Justice White, and Justice O’Connor joined.</p>
<p id="b794-10">Respondent Clifford James Brown was convicted in the District Court of Tarrant County, Tex., for possession of heroin in violation of state law. The Texas Court of Criminal Appeals reversed his conviction, holding that certain evidence should have been suppressed because it was obtained in violation of the Fourth Amendment to the United States Constitution.<footnotemark>1</footnotemark> <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/" aria-description="Citation for case: Brown v. State">617 S. W. 2d 196</a></span>. That court rejected the <page-number citation-index="1" label="733">*733</page-number>State’s contention that the so-called “plain view” doctrine justified the police seizure. Because of apparent uncertainty concerning the scope and applicability of this doctrine, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./457/1116/">457 U. S. 1116</a></span>, and now reverse the judgment of the Court of Criminal Appeals.</p>
<p id="b795-5">On a summer evening in June 1979, Tom Maples, an officer of the Fort Worth police force, assisted in setting up a routine driver’s license checkpoint on East Allen Street in that city. Shortly before midnight Maples stopped an automobile driven by respondent Brown, who was alone. Standing alongside the driver’s window of Brown’s car, Maples asked him for his driver’s license. At roughly the same time, Maples shined his flashlight into the car and saw Brown withdraw his right hand from his right pants pocket. Caught between the two middle fingers of the hand was an opaque, green party balloon, knotted about one-half inch from the tip. Brown let the balloon fall to the seat beside his leg, and then reached across the passenger seat and opened the glove compartment.</p>
<p id="b796-4"><page-number citation-index="1" label="734">*734</page-number>Because of his previous experience in arrests for drug offenses, Maples testified that he was aware that narcotics frequently were packaged in balloons like the one in Brown’s hand. When he saw the balloon, Maples shifted his position in order to obtain a better view of the interior of the glove compartment. He noticed that it contained several small plastic vials, quantities of loose white powder, and an open bag of party balloons. After rummaging briefly through the glove compartment, Brown told Maples that he had no driver’s license in his possession. Maples then instructed him to get out of the car and stand at its rear. Brown complied, and, before following him to the rear of the car, Maples reached into the car and picked up the green balloon; there seemed to be a sort of powdery substance within the tied-off portion of the balloon.</p>
<p id="b796-5">Maples then displayed the balloon to a fellow officer who indicated that he “understood the situation.” The two officers then advised Brown that he was under arrest.<footnotemark>2</footnotemark> They <page-number citation-index="1" label="735">*735</page-number>also conducted an on-the-scene inventory of Brown’s car, discovering several plastic bags containing a green leafy substance and a large bottle of milk sugar. These items, like the balloon, were seized by the officers. At the suppression hearing conducted by the District Court, a police department chemist testified that he had examined the substance in the balloon seized by Maples and determined that it was heroin. He also testified that narcotics frequently were packaged in ordinary party balloons.</p>
<p id="b797-5">The Court of Criminal Appeals, discussing the Fourth Amendment issue, observed that “ ‘plain view <em>alone </em>is never enough to justify the warrantless seizure of evidence.’ ” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 200</a></span>, quoting <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 468</a></span> (1971) (opinion of Stewart, J., joined by Douglas, Brennan, and Marshall, JJ.) It further concluded that “Officer Maples had to <em>know </em>that ‘incriminatory evidence was before him when he seized the balloon.’” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 200</a></span> (emphasis supplied), quoting <em>DeLao </em>v. <em>State, </em><span class="citation" data-id="9769560"><a href="/opinion/2418802/delao-v-state/#291" aria-description="Citation for case: DeLao v. State">550 S. W. 2d 289, 291</a></span> (Tex. Crim. App. 1977). On the State’s petition for rehearing, three judges dissented, stating their view that “[t]he issue turns on whether an officer, relying on years of practical experience and knowledge commonly accepted, has probable cause to seize the balloon in plain view.” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#201" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 201</a></span>.</p>
<p id="b797-6">Because the “plain view” doctrine generally is invoked in conjunction with other Fourth Amendment principles, such as those relating to warrants, probable cause, and search incident to arrest, we rehearse briefly these better understood principles of Fourth Amendment law. That Amendment secures the persons, houses, papers, and effects of the people against unreasonable searches and seizures, and requires the existence of probable cause before a warrant shall issue. Our cases hold that procedure by way of a warrant is preferred, although in a wide range of diverse situations we have recognized flexible, common-sense exceptions to this requirement. See, <em>e. g., Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967) <page-number citation-index="1" label="736">*736</page-number>(hot pursuit); <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51-52</a></span> (1951) (exigent circumstances); <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982) (automobile search); <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), and <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981) (search of person and surrounding area incident to arrest); <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973) (search at border or “functional equivalent”); <em>Zap </em>v. <em>United States, </em><span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#630" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 630</a></span> (1946) (consent). We have also held to be permissible intrusions less severe than full-scale searches or seizures without the necessity of a warrant. See, <em>e. g., Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968) (stop and frisk); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975) (seizure for questioning); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979) (roadblock). One frequently mentioned “exception to the warrant requirement,” <em>Coolidge </em>v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#456" aria-description="Citation for case: Coolidge v. New Hampshire"><em>New Hampshire, supra, </em>at 456</a></span>, is the so-called “plain view” doctrine, relied upon by the State in this case.</p>
<p id="b798-5">While conceding that the green balloon seized by Officer Maples was clearly visible to him, the Court of Criminal Appeals held that the State might not avail itself of the “plain view” doctrine. That court said:</p>
<blockquote id="b798-6">“For the plain view doctrine to apply, not only must the officer be legitimately in a position to view the object, but it must be immediately apparent to the police that they have evidence before them. This ‘immediately apparent’ aspect is central to the plain view exception and is here relied upon by appellant. [Citation omitted.] In this case then, Officer Maples had to know that ‘incriminatory evidence was before him when he seized the balloon.’” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 200</a></span>.</blockquote>
<p id="b798-7">The Court of Criminal Appeals based its conclusion primarily on the plurality portion of the opinion of this Court in <em>Coolidge </em>v. <em>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra.</a></span> </em>In the <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality’s view, the “plain view” doctrine permits the warrantless seizure by police of private possessions where three require<page-number citation-index="1" label="737">*737</page-number>ments are satisfied.<footnotemark>3</footnotemark> First, the police officer must lawfully make an “initial intrusion” or otherwise properly be in a position from which he can view a particular area. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 465-468</a></span>. Second, the officer must discover incriminating evidence “inadvertently,” which is to say, he may not “know in advance the location of [certain] evidence and intend to seize it,” relying on the plain-view doctrine only as a pretext. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#470" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 470</a></span>. Finally, it must be “immediately apparent” to the police that the items they observe may be evidence of a crime, contraband, or otherwise subject to seizure. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#466" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 466</a></span>. While the lower courts generally have applied the <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality’s discussion of “plain view,” it has never been expressly adopted by a majority of this Court. On the contrary, the plurality’s formulation was sharply criticized at the time, see, <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#506" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 506</a></span> (Black, J., dissenting); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#516" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 516-521</a></span> (White, J., dissenting). While not a binding precedent, as the considered opinion of four Members of this Court it should obviously be the point of reference for further discussion of the issue.</p>
<p id="b799-5">The <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality observed: “it is important to keep in mind that, in the vast majority of cases, <em>any </em>evidence seized by the police will be in plain view, at least at the moment of seizure,” simply as “the normal concomitant of any search, legal or illegal.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire"><em>Id., </em>at 465</a></span>. The question whether property in plain view of the police may be seized therefore must turn on the legality of the intrusion that enables them to perceive and physically seize the property in question. The <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality, while following this approach to “plain <page-number citation-index="1" label="738">*738</page-number>view,” characterized it as an independent exception to the warrant requirement. At least from an analytical perspective, this description may be somewhat inaccurate. We recognized in <em>Payton </em>v. <em>New, York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980), the well-settled rule that “objects such as weapons or contraband found in a public place may be seized by the police without a warrant. The seizure of property in plain view involves no invasion of privacy and is presumptively reasonable, assuming that there is probable cause to associate the property with criminal activity.” A different situation is presented, however, when the property in open view is “‘situated on private premises to which access is not otherwise available for the seizing officer.’” <em>Ibid., </em>quoting <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#354" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 354</a></span> (1977). As these cases indicate, “plain view” provides grounds for seizure of an item when an officer’s access to an object has some prior justification under the Fourth Amendment.<footnotemark>4</footnotemark> “Plain view” is perhaps better understood, therefore, not as an independent “exception” to the Warrant <page-number citation-index="1" label="739">*739</page-number>Clause, but simply as an extension of whatever the prior justification for an officer’s “access to an object” may be.</p>
<p id="b801-5">The principle is grounded on the recognition that when a police officer has observed an object in “plain view,” the owner’s remaining interests in the object are merely those of possession and ownership, see <em>Coolidge </em>v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#515" aria-description="Citation for case: Coolidge v. New Hampshire"><em>New Hampshire, supra, </em>at 515</a></span> (White, J., dissenting). Likewise, it reflects the fact that requiring police to obtain a warrant once they have obtained a first-hand perception of contraband, stolen property, or incriminating evidence generally would be a “needless inconvenience,” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 468</a></span>, that might involve danger to the police and public. <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Ibid.</a></span> </em>We have said previously that “the permissibility of a particular law enforcement practice is judged by balancing its intrusion on . . . Fourth Amendment interests against its promotion of legitimate governmental interests.” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 654</a></span>. In light of the private and governmental interests just outlined, our decisions have come to reflect the rule that if, while lawfully engaged in an activity in a particular place, police officers perceive a suspicious object, they may seize it immediately. See <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927); <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span> (1931); <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465</a></span> (1932); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968); <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> (1969). This rule merely reflects an application of the Fourth Amendment’s central requirement of reasonableness to the law governing seizures of property.</p>
<p id="b801-6">Applying these principles, we conclude that Officer Maples properly seized the green balloon from Brown’s automobile. The Court of Criminal Appeals stated that it did not “question . . . the validity of the officer’s initial stop of appellant’s vehicle as a part of a license check,” <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d, at 200</a></span>, and we agree. <em>Delaware </em>v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 654-655</a></span>. It is likewise beyond dispute that Maples’ action in shining his <page-number citation-index="1" label="740">*740</page-number>flashlight to illuminate the interior of Brown’s car trenched upon no right secured to the latter by the Fourth Amendment. The Court said in <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U. S. 559, 563</a></span> (1927): “[The] use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution.” Numerous other courts have agreed that the use of artificial means to illuminate a darkened area simply does not constitute a search, and thus triggers no Fourth Amendment protection.<footnotemark>5</footnotemark></p>
<p id="b802-5">Likewise, the fact that Maples “changed [his] position” and “bent down at an angle so [he] could see what was inside” Brown’s car, App. 16, is irrelevant to Fourth Amendment analysis. The general public could peer into the interior of Brown’s automobile from any number of angles; there is no reason Maples should be precluded from observing as an officer what would be entirely visible to him as a private citizen. There is no legitimate expectation of privacy, <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring); <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#739" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 739-745</a></span> (1979), shielding that portion of the interior of an automobile which may be viewed from outside the vehicle by either inquisitive passersby or diligent police officers. In short, the conduct that enabled Maples to observe the interior of Brown’s car and of his open glove compartment was not a search within the meaning of the Fourth Amendment.</p>
<p id="b803-4"><page-number citation-index="1" label="741">*741</page-number>Thus there can be no dispute here as to the presence of the first of the three requirements held necessary by the <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality to invoke the “plain view” doctrine.<footnotemark>6</footnotemark> But the Court of Criminal Appeals, as we have noted, felt the State’s case ran aground on the requirement that the incriminating nature of the items be “immediately apparent” to the police officer. To the Court of Criminal Appeals, this apparently meant that the officer must be possessed of near certainty as to the seizable nature of the items. Decisions by this Court since <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>indicate that the use of the phrase “immediately apparent” was very likely an unhappy choice of words, since it can be taken to imply that an unduly high degree of certainty as to the incriminatory character of evidence is necessary for an application of the “plain view” doctrine.</p>
<p id="b803-5">In <em>Colorado </em>v. <em>Bannister, </em><span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/#3" aria-description="Citation for case: Colorado v. Bannister">449 U. S. 1, 3-4</a></span> (1980), we applied what was in substance the plain-view doctrine to an officer’s seizure of evidence from an automobile. <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/#4" aria-description="Citation for case: Colorado v. Bannister"><em>Id., </em>at 4, n. 4</a></span>. The officer noticed that the occupants of the automobile matched a description of persons suspected of a theft and that auto parts in the open glove compartment of the car similarly resembled ones reported stolen. The Court held that these facts supplied the officer with “probable cause,” <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/#4" aria-description="Citation for case: Colorado v. Bannister"><em>id., </em>at 4</a></span>, and therefore, that he could seize the incriminating items from the car without a warrant. Plainly, the Court did not view the “immediately apparent” language of <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>as establishing any requirement that a police officer “know” that certain items are contraband or evidence of a crime. Indeed, <em>Colorado </em>v. <em><span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">Bannister, supra,</a></span> </em>was merely an application of the rule, set forth in <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), that “[t]he seizure of property in plain view involves no invasion of privacy and <em>is presumptively reasonable, assuming that there is probable cause to associate the property </em><page-number citation-index="1" label="742">*742</page-number><em>with criminal activity.” Id., </em>at 587 (emphasis added). We think this statement of the rule from <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton, supra,</a></span> </em>requiring probable cause for seizure in the ordinary case,<footnotemark>7</footnotemark> is consistent with the Fourth Amendment and we reaffirm it here.</p>
<p id="b804-4">As the Court frequently has remarked, probable cause is a flexible, common-sense standard. It merely requires that the facts available to the officer would “warrant a man of reasonable caution in the belief,” <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/#162" aria-description="Citation for case: Work v. United States Ex Rel. Rives">267 U. S. 182, 162</a></span> (1925), that certain items may be contraband or stolen property or useful as evidence of a crime; it does not demand any showing that such a belief be correct or more likely true than false. A “practical, nontechnical” probability that incriminating evidence is involved is all that is required. <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949). Moreover, our observation in <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981), regarding “particularized suspicion,” is equally applicable to the probable-cause requirement:</p>
<blockquote id="b804-5">“The process does not deal with hard certainties, but with probabilities. Long before the law of probabilities was articulated as such, practical people formulated certain common-sense conclusions about human behavior; jurors as factfinders are permitted to do the same — and so are law enforcement officers. Finally, the evidence thus collected must be seen and weighed not in terms of library analysis by scholars, but as understood by those versed in the field of law enforcement.”</blockquote>
<p id="b804-6">With these considerations in mind it is plain that Officer Maples possessed probable cause to believe that the balloon in Brown’s hand contained an illicit substance. Maples testified that he was aware, both from his participation in previous narcotics arrests and from discussions with other officers,</p>
<p id="b805-4"><page-number citation-index="1" label="743">*743</page-number>that balloons tied in the manner of the one possessed by Brown were frequently used to carry narcotics. This testimony was corroborated by that of a police department chemist who noted that it was “common” for balloons to be used in packaging narcotics. In addition, Maples was able to observe the contents of the glove compartment of Brown’s car, which revealed further suggestions that Brown was engaged in activities that might involve possession of illicit substances. The fact that Maples could not see through the opaque fabric of the balloon is all but irrelevant: the distinctive character of the balloon itself spoke volumes as to its contents — particularly to the trained eye of the officer.</p>
<p id="b805-5">In addition to its statement that for seizure of objects in plain view to be justified the basis upon which they might be seized had to be “immediately apparent,” and the requirement that the initial intrusion be lawful, both of which requirements we hold were satisfied here, the <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>plurality also stated that the police must discover incriminating evidence “inadvertently,” which is to say, they may not “know in advance the location of [certain] evidence and intend to seize it,” relying on the plain-view doctrine only as a pretense. 430 U. S., at 470. Whatever may be the final disposition of the “inadvertence” element of “plain view,”<footnotemark>8</footnotemark> it clearly was no bar to the seizure here. The circumstances of this meeting between Maples and Brown give no suggestion that the roadblock was a pretext whereby evidence of narcotics violation might be uncovered in “plain view” in the course of a check for driver’s licenses. Here, although the officers no doubt had an expectation that some of the cars they halted on East Allen Street — which was part of a “medium” area of narcotics traffic, App. 33 — would contain narcotics or para<page-number citation-index="1" label="744">*744</page-number>phernalia, there is no indication in the record that they had anything beyond this generalized expectation. Likewise, there is no indication that Maples had any reason to believe that any particular object would be in Brown’s glove compartment or elsewhere in his automobile. The “inadvertence” requirement of “plain view,” properly understood, was no bar to the seizure here.</p>
<p id="b806-5">Maples lawfully viewed the green balloon in the interior of Brown’s car, and had probable cause to believe that it was subject to seizure under the Fourth Amendment. The judgment of the Texas Court of Criminal Appeals is accordingly reversed, and the case is remanded for further proceedings.</p>
<p id="b806-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b794-12"> Brown argues that the decision below rested on an independent and adequate state ground, and therefore that this Court lacks jurisdiction. <em>Fox Film Corp. </em>v. <em>Muller, </em><span class="citation" data-id="102505"><a href="/opinion/102505/fox-film-corp-v-muller/#210" aria-description="Citation for case: Fox Film Corp. v. Muller">296 U. S. 207, 210</a></span> (1935). The position is untenable. The opinion of the Texas Court of Criminal Appeals rests squarely on the interpretation of the Fourth Amendment to the United States Constitution in <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), and on Texas cases interpreting that decision, <em>e. g., Howard </em>v. <em>State, </em><span class="citation" data-id="9661682"><a href="/opinion/1631203/howard-v-state/" aria-description="Citation for case: Howard v. State">599 S. W. 2d 597</a></span> (Tex. Crim. App. 1979); <em>DeLao </em>v. <em>State, </em><span class="citation" data-id="9769560"><a href="/opinion/2418802/delao-v-state/" aria-description="Citation for case: DeLao v. State">550 S. W. 2d 289</a></span> (Tex. Crim. App. 1977); <em>Duncan </em>v. <em>State, </em><span class="citation" data-id="9647768"><a href="/opinion/1526891/duncan-v-state/" aria-description="Citation for case: Duncan v. State">549 S. W. 2d 730</a></span> (Tex. Crim. App. 1977); and <em>Nicholas </em>v. <em>State, </em><span class="citation" data-id="9775167"><a href="/opinion/2448737/nicholas-v-state/" aria-description="Citation for case: Nicholas v. State">502 S. W. 2d 169</a></span> (Tex. Crim. App. 1973). The only men<page-number citation-index="1" label="733">*733</page-number>tion of the Texas Constitution occurs in a summary of Brown’s contentions at the outset of the lower court’s opinion.</p>
<p id="b795-7">Brown relies principally on <em>Howard </em>v. <em>State, supra, </em>and <em>Duncan </em>v. <em>State, supra. </em>Neither decision supports the proposition that the Texas Court of Criminal Appeals based its decision upon state law. In <em>Howard, </em>the State argued that the plain-view doctrine justified the seizure of a closed translucent medicine jar from an automobile. The Court of Criminal Appeals rejected the claim, relying on <em>Coolidge </em>v. <em>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra,</a></span> </em>and stating that the State’s arguments “cannot be squared with the Supreme Court’s interpretation of the plain view doctrine.” <span class="citation" data-id="9661682"><a href="/opinion/1631203/howard-v-state/#602" aria-description="Citation for case: Howard v. State">599 S. W. 2d, at 602</a></span>. The court also relied on <em>Thomas </em>v. <em>State, </em><span class="citation" data-id="9680885"><a href="/opinion/1774097/thomas-v-state/" aria-description="Citation for case: Thomas v. State">572 S. W. 2d 507</a></span> (Tex. Crim. App. 1976), which it characterized as “[fjollowing the teachings of <em>Coolidge </em>v. <em>New Hampshire.” </em><span class="citation" data-id="9661682"><a href="/opinion/1631203/howard-v-state/#602" aria-description="Citation for case: Howard v. State">599 S. W. 2d, at 602</a></span>. An additional opinion of the court on the State’s motion for rehearing merely elaborated upon the application of the plain-view doctrine set forth in the court’s original opinion. Similarly, in <em><span class="citation" data-id="9647768"><a href="/opinion/1526891/duncan-v-state/" aria-description="Citation for case: Duncan v. State">Duncan</a></span>, </em>the Court of Criminal Appeals rejected the State’s reliance on the plain-view theory, citing to <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>for a statement of the applicable law, as well as to <em>Nicholas </em>v. <em>State, supra. </em>Like the court’s other decisions in the area, <em><span class="citation" data-id="9775167"><a href="/opinion/2448737/nicholas-v-state/" aria-description="Citation for case: Nicholas v. State">Nicholas</a></span> </em>relied only on <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span>.</em></p>
</footnote>
<footnote label="2">
<p id="b796-6"> It is not clear on the record before us when Brown was arrested. The Court of Criminal Appeals stated, at one point in its opinion, that it did not question “the propriety of the arrest since appellant failed to produce a driver’s license.” ■ <span class="citation" data-id="9675660"><a href="/opinion/1739285/brown-v-state/#200" aria-description="Citation for case: Brown v. State">617 S. W. 2d 196,200</a></span>. This statement might be read to suggest that Brown was arrested upon his failure to produce a license, instead of at some point following seizure of the balloon from the car. The transcript of the suppression hearing, however, indicates rather clearly that Brown was not formally arrested until after seizure of the balloon. App. 28-31. In the face of such indications, we decline to interpret the above-quoted clause from the Court of Criminal Appeals’ opinion as evidencing a belief that an arrest occurred prior to seizure of the balloon. Rather, we think it likely that the court was simply reasoning that Brown’s arrest, whenever it may have taken place, was justified because of his failure to produce a driver’s license.</p>
<p id="b796-7">We do not address the argument that seizure of the balloon would have been justified under <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), which permits warrantless searches of the passenger compartment of an automobile incident to an arrest, because of the absence of clear factual findings regarding the time at which, and the reason for which, Brown was arrested and because the lower court was not able to consider that decision.</p>
</footnote>
<footnote label="3">
<p id="b799-6"> The plurality also remarked that “plain view <em>alone </em>is never enough to justify the warrantless seizure of evidence.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 468</a></span>. The court below appeared to understand this phrase to impose an independent limitation upon the scope of the plain-view doctrine articulated in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span>. </em>The context in which the plurality used the phrase, however, indicates that it was merely a rephrasing of its conclusion, discussed below, that in order for the plain-view doctrine to apply, a police officer must be engaged in a lawful intrusion or must otherwise legitimately occupy the position affording him a “plain view.”</p>
</footnote>
<footnote label="4">
<p id="b800-5"> Thus, police may perceive an object while executing a search warrant, or they may come across an item while acting pursuant to some exception to the Warrant Clause, <em>e. g., Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). Alternatively, police may need no justification under the Fourth Amendment for their access to an item, such as when property is left in a public place, see <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980).</p>
<p id="b800-6">It is important to distinguish “plain view,” as used in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>to justify <em>seizure </em>of an object, from an officer’s mere observation of an item left in plain view. Whereas the latter generally involves no Fourth Amendment search, see <em>infra, </em>at 740; <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the former generally does implicate the Amendment’s limitations upon seizures of personal property. The information obtained as a result of observation of an object in plain sight may be the basis for probable cause or reasonable suspicion of illegal activity. In turn, these levels of suspicion may, in some cases, see, <em>e. g., Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra;</a></span> United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), justify police conduct affording them access to a particular item.</p>
</footnote>
<footnote label="5">
<p id="b802-6"><em> E. g., United States </em>v. <em>Chesher, </em><span class="citation" data-id="9469232"><a href="/opinion/403902/united-states-v-lawrence-gilbert-chesher/#1356" aria-description="Citation for case: United States v. Lawrence Gilbert Chesher">678 F. 2d 1353, 1356-1357, n. 2</a></span> (CA9 1982); <em>United States </em>v. <em>Ocampo, </em><span class="citation" data-id="391014"><a href="/opinion/391014/united-states-v-daniel-ocampo-theodoro-hernandez-jose-otero-and/#427" aria-description="Citation for case: United States v. Daniel Ocampo, Theodoro Hernandez, Jose...">650 F. 2d 421, 427</a></span> (CA2 1981); <em>United States </em>v. <em>Pugh, </em><span class="citation" data-id="350948"><a href="/opinion/350948/united-states-v-larry-wayne-pugh/#627" aria-description="Citation for case: United States v. Larry Wayne Pugh">566 F. 2d 626, 627, n. 2</a></span> (CA8 1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./435/1010/">435 U. S. 1010</a></span> (1978); <em>United States </em>v. <em>Coplen, </em><span class="citation" data-id="338727"><a href="/opinion/338727/united-states-v-tommy-joe-coplen-united-states-of-america-v-henry/" aria-description="Citation for case: United States v. Tommy Joe Coplen, United States of...">541 F. 2d 211</a></span> (CA9 1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1073/">429 U. S. 1073</a></span> (1977); <em>United States </em>v. <em>Lara, </em><span class="citation" data-id="328010"><a href="/opinion/328010/united-states-v-ruben-garza-lara/" aria-description="Citation for case: United States v. Ruben Garza Lara">517 F. 2d 209</a></span> (CA5 1975); <em>United States </em>v. <em>Johnson, </em><span class="citation" data-id="9461232"><a href="/opinion/323153/united-states-v-kenneth-wayne-johnson-united-states-of-america-v-derrick/" aria-description="Citation for case: United States v. Kenneth Wayne Johnson, United States of...">506 F. 2d 674</a></span> (CA8 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./421/917/">421 U. S. 917</a></span> (1975); <em>United States </em>v. <em>Booker, </em><span class="citation" data-id="9458318"><a href="/opinion/303966/united-states-v-robert-lee-booker/#992" aria-description="Citation for case: United States v. Robert Lee Booker">461 F. 2d 990, 992</a></span> (CA6 1972); <em>United States </em>v. <em>Hanahan, </em><span class="citation" data-id="296598"><a href="/opinion/296598/united-states-v-robert-michael-hanahan/" aria-description="Citation for case: United States v. Robert Michael Hanahan">442 F. 2d 649</a></span> (CA7 1971); <em>People </em>v. <em>Waits, </em><span class="citation" data-id="9557787"><a href="/opinion/1193476/people-v-waits/" aria-description="Citation for case: People v. Waits">196 Colo. 35</a></span>, <span class="citation" data-id="9557787"><a href="/opinion/1193476/people-v-waits/" aria-description="Citation for case: People v. Waits">580 P. 2d 391</a></span> (1978); <em>Redd </em>v. <em>State, </em><span class="citation" data-id="5596513"><a href="/opinion/5744734/redd-v-state/" aria-description="Citation for case: Redd v. State">240 Ga. 753</a></span>, <span class="citation" data-id="5596513"><a href="/opinion/5744734/redd-v-state/" aria-description="Citation for case: Redd v. State">243 S. E. 2d 16</a></span> (1978); <em>State </em>v. <em>Chattley, </em><span class="citation" data-id="2332441"><a href="/opinion/2332441/state-v-chattley/" aria-description="Citation for case: State v. Chattley">390 A. 2d 472</a></span> (Me. 1978); <em>State </em>v. <em>Vohnoutka, </em><span class="citation" data-id="2222769"><a href="/opinion/2222769/state-v-vohnoutka/" aria-description="Citation for case: State v. Vohnoutka">292 N. W. 2d 756</a></span> (Minn. 1980); <em>Dick </em>v. <em>State, </em><span class="citation" data-id="1362880"><a href="/opinion/1362880/dick-v-state/" aria-description="Citation for case: Dick v. State">596 P. 2d 1265</a></span> (Okla. Crim. App. 1979); <em>State </em>v. <em>Miller, </em><span class="citation" data-id="1208933"><a href="/opinion/1208933/state-v-miller/" aria-description="Citation for case: State v. Miller">45 Ore. App. 407</a></span>, <span class="citation" data-id="1208933"><a href="/opinion/1208933/state-v-miller/" aria-description="Citation for case: State v. Miller">608 P. 2d 595</a></span> (1980); <em>Albo </em>v. <em>State, </em><span class="citation" data-id="1687759"><a href="/opinion/1687759/albo-v-state/" aria-description="Citation for case: Albo v. State">379 So. 2d 648</a></span> (Fla. 1980).</p>
</footnote>
<footnote label="6">
<p id="b803-6"> While seizure of the balloon required a warrantless, physical intrusion into Brown’s automobile, this was proper, assuming that the remaining requirements of the plain-view doctrine were satisfied. <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982).</p>
</footnote>
<footnote label="7">
<p id="b804-7"> We need not address whether, in some circumstances, a degree of suspicion lower than probable cause would be sufficient basis for a seizure in certain cases.</p>
</footnote>
<footnote label="8">
<p id="b805-6"> See <em>State </em>v. <em>King, </em><span class="citation" data-id="9671244"><a href="/opinion/1710492/state-v-king/#655" aria-description="Citation for case: State v. King">191 N. W. 2d 650, 655</a></span> (Iowa 1971); <em>United States </em>v. <em>Santana, </em><span class="citation" data-id="313647"><a href="/opinion/313647/united-states-v-gilberto-santana/#369" aria-description="Citation for case: United States v. Gilberto Santana">485 F. 2d 365, 369-370</a></span> (CA2 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/931/">415 U. S. 931</a></span> (1974); <em>United States </em>v. <em>Bradshaw, </em><span class="citation" data-id="9460223"><a href="/opinion/316481/united-states-v-william-garland-bradshaw/#1101" aria-description="Citation for case: United States v. William Garland Bradshaw">490 F. 2d 1097, 1101, n. 3</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/895/">419 U. S. 895</a></span> (1974); <em>North </em>v. <em>Superior Court, </em><span class="citation" data-id="9577161"><a href="/opinion/1239224/north-v-superior-court/#306" aria-description="Citation for case: North v. Superior Court">8 Cal. 3d 301, 306-307</a></span>, <span class="citation" data-id="9577161"><a href="/opinion/1239224/north-v-superior-court/#1308" aria-description="Citation for case: North v. Superior Court">502 P. 2d 1305, 1308</a></span> (1972).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Texas v. Cobb.md  (`case`, 5 assertions)

### content_page

```
---
title: "Texas v. Cobb"
type: case
citation: "532 U.S. 162 (2001)"
parallel_cite: "121 S. Ct. 1335; 149 L. Ed. 2d 321"
neutral_cite: 2001 U.S. LEXIS 2696
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-04-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-04-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Texas v. Cobb
  varies_by_point: false
  scope_note: "Good law; defines the scope of the Sixth Amendment right by the Blockburger same-elements test."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118417/texas-v-cobb/"
  cluster_id: 118417
  opinion_id: 9434063
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[McNeil v. Wisconsin]]", "[[Massiah v. United States]]", "[[Brewer v. Williams]]", "[[Montejo v. Louisiana]]", "[[Maine v. Moulton]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel"]
holding: "The Sixth Amendment right to counsel is offense-specific; it attaches only to the charged offense and does not extend to other,…"
lake:
  record_id: Texas v. Cobb
  status: verified
  projected_at: 2026-07-06
---

# Texas v. Cobb

*532 U.S. 162 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Cobb was indicted for burglary of a home and was appointed counsel on that charge. A woman and her infant daughter had disappeared from the home. While free on bond and represented on the burglary, Cobb later confessed to his father, who told police; after [[Miranda and Custodial Interrogation|Miranda warnings]] and a waiver, Cobb confessed to murdering the woman and child. He argued the murder confession was taken in violation of his Sixth Amendment right to counsel, which had attached on the factually related burglary.

## Issue
Whether the Sixth Amendment right to counsel, once it has attached to a charged offense, also extends to other uncharged offenses that are factually related to the charged one.

## Rule
The right to counsel is charge-specific: "the Sixth Amendment right is 'offense specific.'" — 532 U.S. at 164. ^pin-164

It therefore does not automatically reach other, uncharged offenses merely because they are factually intertwined with the charged crime. The scope of an "offense" is fixed by the *Blockburger* same-elements test: "where the same act or transaction constitutes a violation of two distinct statutory provisions, the test to be applied to determine whether there are two offenses or only one, is whether each provision requires proof of a fact which the other does not." — *Id.* at 173. ^pin-173

## Application
Because Cobb had been charged only with burglary, his Sixth Amendment right had attached to that offense alone. Capital murder and burglary each require proof of an element the other does not, so under *Blockburger* they are separate offenses; the murder was not the "same offense" as the charged burglary. The right to counsel on the burglary therefore did not bar police from questioning Cobb about the uncharged murders, and his Miranda-waived confession was admissible.

## Conclusion
The Sixth Amendment right to counsel did not extend to the uncharged murders; the Texas court's reversal was itself reversed. A defendant's attachment of counsel on one charge does not insulate him from interrogation on distinct, uncharged offenses.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Cobb* applies and confines the offense-specific rule of [[McNeil v. Wisconsin]]; it is read alongside [[Massiah v. United States]] and [[Brewer v. Williams]] (deliberate elicitation after attachment) and [[Montejo v. Louisiana]] (waiver of the attached right).

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Texas v. Cobb*, 532 U.S. 162 (2001) — https://www.courtlistener.com/opinion/118417/texas-v-cobb/ — pinpoints: 164, 173.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "49d510bfe8f0ff5e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "532 U.S. 162 (2001)", "court": "U.S. Supreme Court", "neutral_cite": "2001 U.S. LEXIS 2696", "official_citation_present": true, "parallel_cite": "121 S. Ct. 1335; 149 L. Ed. 2d 321", "title": "Texas v. Cobb", "year": "2001"}}
{"assertion_id": "064f3dcaf0a439ec", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Amendment right to counsel is offense-specific; it attaches only to the charged offense and does not extend to other,…", "title": "Texas v. Cobb"}}
{"assertion_id": "9537f99ed211b93c", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "Texas v. Cobb"}}
{"assertion_id": "d4ba1ab381e9b148", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Texas v. Cobb"}}
{"assertion_id": "e049b82ef12ad056", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2001-04-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Texas v. Cobb", "field_i_validity": "good_law", "scope_note": "Good law; defines the scope of the Sixth Amendment right by the Blockburger same-elements test.", "title": "Texas v. Cobb", "varies_by_point": "false"}}
```

### lake record — Texas v. Cobb

```json
{
  "schema_version": "s2.v1",
  "record_id": "Texas v. Cobb",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Texas v. Cobb",
    "case_name_short": "Cobb",
    "case_name_full": "Texas v. Cobb",
    "input_case_name": "Texas v. Cobb",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-04-17",
    "year": 2001,
    "docket": null,
    "cluster_id": 118417,
    "lead_opinion_id": 9434063,
    "sibling_ids": [
      118417,
      9434063,
      9434064,
      9434065
    ],
    "absolute_url": "/opinion/118417/texas-v-cobb/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "532 U.S. 162",
      "volume": "532",
      "reporter": "U.S.",
      "page": "162",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "121 S. Ct. 1335",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1335",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 321",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 2696",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "2696",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "532 U.S. 162",
        "volume": "532",
        "reporter": "U.S.",
        "page": "162",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1335",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1335",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 321",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 2696",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "2696",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "532 U.S. 162",
    "official_selection": {
      "court_class": "scotus",
      "selected": "532 U.S. 162",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-164",
      "page": null,
      "quote": "--- # Texas v. Cobb *532 U.S. 162 (2001)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Cobb was indicted for burglary of a home and was appointed counsel on that charge. A woman and her infant daughter had disappeared from the home. While free on bond and represented on the burglary, Cobb later confessed to his father, who told police; after Miranda warnings and a waiver, Cobb confessed to murdering the woman and child. He argued the murder confession was taken in violation of his Sixth Amendment right to counsel, which had attached on the factually related burglary. ## Issue Whether the Sixth Amendment right to counsel, once it has attached to a charged offense, also extends to other uncharged offenses that are factually related to the charged one. ## Rule The right to counsel is charge-specific:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-173",
      "page": null,
      "quote": "is fixed by the *Blockburger* same-elements test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-04-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Texas v. Cobb",
    "varies_by_point": false,
    "scope_note": "Good law; defines the scope of the Sixth Amendment right by the Blockburger same-elements test.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Fernandes",
          "cluster_id": 9414986,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Handa",
          "cluster_id": 4505766,
          "cite": [
            "892 F.3d 95"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
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
        "journal_ref": "Texas v. Cobb:lane1_negative"
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
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "DUTTON v. CITY OF MIDWEST CITY",
          "cluster_id": 2813680,
          "cite": [
            "2015 OK 51",
            "353 P.3d 532",
            "2015 Okla. LEXIS 75",
            "2015 WL 3998977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "in Re Mark Athans, Omar Martinez and Prestige Surgical Assistants, LLC",
          "cluster_id": 2980932,
          "cite": [
            "458 S.W.3d 675",
            "2015 Tex. App. LEXIS 1499",
            "2015 WL 673416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Taylor",
          "cluster_id": 7306221,
          "cite": [
            "17 F. Supp. 3d 162",
            "2014 WL 1653194",
            "2014 U.S. Dist. LEXIS 57397"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Basciano",
          "cluster_id": 2470094,
          "cite": [
            "763 F. Supp. 2d 303",
            "2011 U.S. Dist. LEXIS 2901",
            "2011 WL 114865"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tlasek",
          "cluster_id": 6589376,
          "cite": [
            "77 Mass. App. Ct. 298",
            "930 N.E.2d 170",
            "2010 Mass. App. LEXIS 999"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pecina v. State",
          "cluster_id": 2292956,
          "cite": [
            "326 S.W.3d 249",
            "2010 Tex. App. LEXIS 5631",
            "2010 WL 2825663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Samuel Constanza Alvarado",
          "cluster_id": 793566,
          "cite": [
            "440 F.3d 191",
            "2006 U.S. App. LEXIS 6055",
            "2006 WL 598152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ronald R. Scarberry v. State of Iowa",
          "cluster_id": 792613,
          "cite": [
            "430 F.3d 956",
            "2005 U.S. App. LEXIS 25648",
            "2005 WL 3159221"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane1_negative"
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
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 1476684,
          "cite": [
            "859 A.2d 364",
            "181 N.J. 391",
            "2004 N.J. LEXIS 1080"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
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
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
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
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quiroz",
          "cluster_id": 4282819,
          "cite": [
            "55 M.J. 334",
            "2001 CAAF LEXIS 1020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lotter",
          "cluster_id": 8285182,
          "cite": [
            "917 N.W.2d 850",
            "301 Neb. 125"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
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
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gregory",
          "cluster_id": 2621432,
          "cite": [
            "147 P.3d 1201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. DePriest",
          "cluster_id": 2517841,
          "cite": [
            "163 P.3d 896",
            "63 Cal. Rptr. 3d 896",
            "42 Cal. 4th 1",
            "2007 Cal. LEXIS 8291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thornton",
          "cluster_id": 2552553,
          "cite": [
            "161 P.3d 3",
            "61 Cal. Rptr. 3d 461",
            "41 Cal. 4th 391",
            "2007 Cal. LEXIS 6759"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tommie T. Childs",
          "cluster_id": 776249,
          "cite": [
            "277 F.3d 947",
            "2002 U.S. App. LEXIS 760",
            "2002 WL 63798"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Fayed",
          "cluster_id": 4741522,
          "cite": [
            "9 Cal. 5th 147",
            "260 Cal. Rptr. 3d 761",
            "460 P.3d 1149"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaemmerling v. Lappin",
          "cluster_id": 187263,
          "cite": [
            "553 F.3d 669",
            "384 U.S. App. D.C. 240",
            "2008 U.S. App. LEXIS 26507",
            "2008 WL 5396823"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hitt",
          "cluster_id": 47622,
          "cite": [
            "473 F.3d 146",
            "2006 WL 3616560"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson, Ex Parte Ronald",
          "cluster_id": 2949202,
          "cite": [
            "442 S.W.3d 325",
            "2014 Tex. Crim. App. LEXIS 969",
            "2014 WL 4627231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sapp",
          "cluster_id": 2689898,
          "cite": [
            "2004 Ohio 7008",
            "105 Ohio St. 3d 104",
            "822 N.E.2d 1239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cobb v. State",
          "cluster_id": 1588789,
          "cite": [
            "85 S.W.3d 258",
            "2002 Tex. Crim. App. LEXIS 111",
            "2002 WL 1059741"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warner v. State",
          "cluster_id": 2586068,
          "cite": [
            "2006 OK CR 40",
            "144 P.3d 838",
            "2006 WL 2788641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Trujillo",
          "cluster_id": 2588337,
          "cite": [
            "146 P.3d 1259",
            "51 Cal. Rptr. 3d 718",
            "40 Cal. 4th 165",
            "2006 Daily Journal DAR 16081",
            "2006 Cal. Daily Op. Serv. 11289",
            "2006 Cal. LEXIS 14358"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Toles",
          "cluster_id": 162347,
          "cite": [
            "297 F.3d 959",
            "2002 U.S. App. LEXIS 12481",
            "2002 WL 1365590"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Vasquez",
          "cluster_id": 2484061,
          "cite": [
            "456 Mass. 350",
            "923 N.E.2d 524",
            "2010 Mass. LEXIS 120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
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
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mayes",
          "cluster_id": 1440035,
          "cite": [
            "63 S.W.3d 615",
            "2001 Mo. LEXIS 99",
            "2001 WL 1609093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Texas v. Cobb:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118417 OR 9434063 OR 9434064 OR 9434065) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDc2NTQ0MDAwMDAwJnM9Nzg0NDYyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118417+OR+9434063+OR+9434064+OR+9434065%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118417 OR 9434063 OR 9434064 OR 9434065)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MCZzPTMwMTM0NzEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118417+OR+9434063+OR+9434064+OR+9434065%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118417 OR 9434063 OR 9434064 OR 9434065)",
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
    "complete_query": "cites:(118417 OR 9434063 OR 9434064 OR 9434065)",
    "indexed_citing_opinions": 305,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118417,
        "count": 268,
        "count_source": "search"
      },
      {
        "opinion_id": 9434063,
        "count": 47,
        "count_source": "search"
      },
      {
        "opinion_id": 9434064,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434065,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 504,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/texas-v-cobb.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyNzExMTEmcz00ODg3NTY2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118417+OR+9434063+OR+9434064+OR+9434065%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118417,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 108114,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 108987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 109695,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 110428,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 112127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 112622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 112906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 117863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 606691,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 734234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 746894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 752877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 1778701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 1960321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 2009182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 2025446,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 2239111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118417,
        "cited_id": 2278126,
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
    "date_created": "2026-07-05T21:28:38Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:28:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:28:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:33:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:28:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Texas v. Cobb

```
<opinion type="majority">
<author id="b258-6">Chief Justice Rehnquist</author>
<p id="Aij">delivered the opinion of the Court.</p>
<p id="b258-7">The Texas Court of Criminal Appeals held that a criminal defendant's Sixth Amendment right to counsel attaches not only to the offense with which he is charged, but to other offenses “closely related factually” to the charged offense. We hold that our decision in <em>McNeil </em>v. <em>Wisconsin, </em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">501 U. S. 171</a></span> (1991), meant what it said, and that the Sixth Amendment right is “offense specific.”</p>
<p id="b258-8">In December 1993, Lindsey Owings reported to the Walker County, Texas, Sheriff’s Office that the home he <page-number citation-index="1" label="165">*165</page-number>shared with his wife, Margaret, and their 16-month-old daughter, Kori Rae, had been burglarized. He also informed police that his wife and daughter were missing. Respondent Raymond Levi Cobb lived across the street from the Owings. Acting on an anonymous tip that respondent was involved in the burglary, Walker County investigators questioned him about the events. He denied involvement. In July 1994, while under arrest for an unrelated offense, respondent was again questioned about the incident. Respondent then gave a written statement confessing to the burglary, but he denied knowledge relating to the disappearances. Respondent was subsequently indicted for the burglary, and Hal Ridley was appointed in August 1994 to represent respondent on that charge.</p>
<p id="b259-5">Shortly after Ridley’s appointment, investigators asked and received his permission to question respondent about the disappearances. Respondent continued to deny involvement. Investigators repeated this process in September 1995, again with Ridley’s permission and again with the same result.</p>
<p id="b259-6">In November 1995, respondent, free on bond in the burglary ease, was living with his father in Odessa, Texas. At that time, respondent’s father contacted the Walker County Sheriff’s Office to report that respondent had confessed to him that he killed Margaret Owings in the course of the burglary. Walker County investigators directed respondent’s father to the Odessa police station, where he gave a statement. Odessa police then faxed the statement to Walker County, where investigators secured a warrant for respondent’s arrest and faxed it back to Odessa. Shortly thereafter, Odessa police took respondent into custody and administered warnings pursuant to <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span> (1966). Respondent waived these rights.</p>
<p id="b259-7">After a short time, respondent confessed to murdering both Margaret and Kori Rae. Respondent explained that when Margaret confronted him as he was attempting to re<page-number citation-index="1" label="166">*166</page-number>move the Qwings’ stereo, he stabbed her in the stomach with a knife he was carrying. Respondent told police that he dragged her body to a wooded area a few hundred yards from the house. Respondent then stated:</p>
<blockquote id="b260-5">“ ‘I went back to her house and I saw the baby laying on its bed. I took the baby out there and it was sleeping the whole time. I laid the baby down on the ground four or five feet away from its mother. I went back to my house and got a flat edge shovel. That’s all I could find. Then I went back over to where they were and I started digging a hole between them. After I got the hole dug, the baby was awake. It started going toward its mom and it fell in the hole. I put the lady in the hole and I covered them up. I remember stabbing a different knife I had in the ground where they were. I was crying right then.’ ” App. to Pet. for Cert. A-9 to A-10.</blockquote>
<p id="b260-6">Respondent later led police to the location where he had buried the victims’ bodies.</p>
<p id="b260-7">Respondent was convicted of capital murder for murdering more than one person in the course of a single criminal transaction. See <span class="citation no-link">Tex. Penal Code Ann. § 19.03</span>(a)(7)(A) (1994). He was sentenced to death. On appeal to the Court of Criminal Appeals of Texas, respondent argued, <em>inter alia, </em>that his confession should have been suppressed because it was obtained in violation of his Sixth Amendment right to counsel. Relying on <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), respondent contended that his right to counsel had attached when Ridley was appointed in the burglary case and that Odessa police were therefore required to secure Ridley’s permission before proceeding with the interrogation.</p>
<p id="b260-8">The Court of Criminal Appeals reversed respondent’s conviction by a divided vote and remanded for a new trial. The court held that “once the right to counsel attaches to <page-number citation-index="1" label="167">*167</page-number>the offense charged, it also attaches to any other offense that is very closely related factually to the offense charged.” <span class="citation" data-id="9692380"><a href="/opinion/1891478/cobb-v-state/#3" aria-description="Citation for case: Cobb v. State">2000 WL 275644, *3</a></span> (2000) (citations omitted). Finding the capital murder charge to be “factually interwoven with the burglary,” the court concluded that respondent’s Sixth Amendment right to counsel had attached on the capital murder charge even though respondent had not yet been charged with that offense. <em>Id., </em>at *4. The court further found that respondent had asserted that right by accepting Ridley’s appointment in the burglary case. See <em>ibid. </em>Accordingly, it deemed the confession inadmissible and found that its introduction had not been harmless error. See <em>id., </em>at *4-*5. Three judges dissented, finding <em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>to be distinguishable and concluding that respondent had made a valid unilateral waiver of his right to counsel before confessing. See 2000 WL, at *5-*13 (opinion of McCormick, P. J.).</p>
<p id="b261-5">The State sought review in this Court, and we granted certiorari to consider first whether the Sixth Amendment right to counsel extends to crimes that are “factually related” to those that have actually been charged, and second whether respondent made a valid unilateral waiver of that right in this case. <span class="citation multiple-matches"><a href="/c/U.%20S./530/1260/">530 U. S. 1260</a></span> (2000). Because we answer the first question in the negative, we do not reach the second.</p>
<p id="b261-6">The Sixth Amendment provides that “[i]n all criminal prosecutions, the aeeused shall enjoy the right... to have the Assistance, of Counsel for his defence.” In <em>McNeil </em>v. <em>Wisconsin, </em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">501 U. S. 171</a></span> (1991), we explained when this right arises:</p>
<blockquote id="b261-7">“The Sixth Amendment right [to counsel]... is offense specific. It cannot be invoked once for all future prosecutions, for it does not attach until a prosecution is commenced, that is, at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, in<page-number citation-index="1" label="168">*168</page-number>formation, or arraignment.” <span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/#175" aria-description="Citation for case: McNeil v. Wisconsin"><em>Id., </em>at 175</a></span> (citations and internal quotation marks omitted).</blockquote>
<p id="b262-5">Accordingly, we held that a defendant’s statements regarding offenses for which he had not been charged were admissible notwithstanding the attachment of his Sixth Amendment right to counsel on other charged offenses. See <span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/#176" aria-description="Citation for case: McNeil v. Wisconsin"><em>id., </em>at 176</a></span>.</p>
<p id="b262-6">Some state courts and Federal Courts of Appeals, however, have read into <em>McNeil’s </em>offense-specific definition an exception for crimes that aré “factually related” to a charged offense.<footnotemark>1</footnotemark> Several of these courts have interpreted <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U.S. 387</a></span> (1977), and <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U.S. 159</a></span> (1985)—both of which were decided well before <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">McNeil</a></span></em>—to support this view, which respondent now invites us to approve. We decline to do so.</p>
<p id="b262-7">In <em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">Brewer</a></span>, </em>a suspect in the abduction and murder of a 10-year-old girl had fled from the scene of the erime in Des Moines, Iowa, some 160 miles east to Davenport, Iowa, where he surrendered to police. An arrest warrant was issued in Des Moines on a charge of abduction, and the suspect was arraigned on that warrant before a Davenport judge. Des Moines police traveled to Davenport, took the man into custody, and began the drive back to Des Moines. Along the way, one of the officers persuaded the suspect to lead police to the victim’s body. The suspect ultimately was convicted of the girl’s murder. This Court upheld the federal habeas court’s conclusion that police had violated the suspect’s Sixth Amendment right to counsel. We held that the officer’s comments to the suspect constituted in<page-number citation-index="1" label="169">*169</page-number>terrogation and that the suspect had not validly waived his right to counsel by responding to the officer. See <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#405" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 405-406</a></span>.</p>
<p id="b263-5">Respondent suggests that <em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">Brewer</a></span> </em>implicitly held that the right to counsel attached to the factually related murder when the suspect was arraigned on the abduction charge. See Brief for Respondent 4. The Court’s opinion, however, simply did not address the significance of the fact that the suspect had been arraigned only on the abduction charge, nor did the parties in any way argue this question. Constitutional rights are not defined by inferences from opinions which did not address the question at issue. Cf. <em>Hagans </em>v. <em>Lavine, </em><span class="citation" data-id="9425636"><a href="/opinion/108987/hagans-v-lavine/#535" aria-description="Citation for case: Hagans v. Lavine">415 U.S. 528, 535, n. 5</a></span> (1974) (“[W]hen questions of jurisdiction have been passed on in prior decisions <em>sub silentio, </em>this Court has never considered itself bound when a subsequent case finally brings the jurisdictional issue before us”).</p>
<p id="b263-6"><em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton</a></span> </em>is similarly unhelpful to respondent. That case involved two individuals indicted for a series of thefts, one of whom had secretly agreed to cooperate with the police investigation of his codefendant, Moulton. At the suggestion of police, the informant recorded several telephone calls and one face-to-face conversation he had with Moulton during which the two discussed their criminal exploits and possible alibis. In the course of those conversations, Moul-ton made various incriminating statements regarding both the thefts for which he had been charged and additional crimes. In a superseding indictment, Moulton was charged with the original crimes as well as burglary, arson, and three additional thefts. At trial, the State introduced portions of the recorded face-to-face conversation, and Moulton ultimately was convicted of three of the originally charged thefts plus one count of burglary. Moulton appealed his convictions to the Supreme Judicial Court of Maine, arguing that introduction of the recorded conversation violated <page-number citation-index="1" label="170">*170</page-number>his Sixth Amendment right to counsel. That court agreed, holding;</p>
<blockquote id="b264-5">“‘Those statements may be admissible in the investigation or prosecution of charges for which, at the time the recordings were made, adversary proceedings had not yet commenced. But as to the charges for which Moul-ton’s right to counsel had already attached, his incriminating statements should have been ruled inadmissible at trial, given the circumstances in which they were acquired.’ ” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 168</a></span> (quoting <em>State </em>v. Moulton, <span class="citation" data-id="2009182"><a href="/opinion/2009182/state-v-moulton/#161" aria-description="Citation for case: State v. Moulton">481 A. 2d 155, 161</a></span> (1984)).</blockquote>
<p id="b264-6">We affirmed.</p>
<p id="b264-7">Respondent contends that, in affirming reversal of both the theft and burglary charges, the <em>Moulton </em>Court must have concluded that Moulton’s Sixth Amendment right to counsel attached to the burglary charge. See Brief for Respondent 13-14; see also Brief for the National Association of Criminal Defense Lawyers et al. as <em>Amici Curiae </em>22-23. But the <em>Moulton </em>Court did not address the question now before us, and to the extent <em>Moulton </em>spoke to the matter at all, it expressly referred to the offense-specific nature of the Sixth Amendment right to counsel:</p>
<blockquote id="b264-8">“The police have an interest in the thorough investigation of crimes for which <em>formal charges </em>have already been filed. They also have an interest in investigating new or additional crimes. Investigations of either type of crime may require surveillance of individuals already under indictment. Moreover, law enforcement officials investigating an individual suspected of committing one crime and <em>formally charged </em>with having committed another crime obviously seek to discover evidence useful at a trial of either crime. In seeking evidence pertaining to <em>'pending charges, </em>however, the Government’s investigative powers are limited by the Sixth Amendment rights of the accused.... On the other hand, to exclude <page-number citation-index="1" label="171">*171</page-number>evidence pertaining to charges as to which the Sixth Amendment right to counsel had not attached at the time the evidence was obtained, simply because other charges were pending at that time, would unnecessarily frustrate the public’s interest in the investigation of criminal activities'.” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#179" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 179-180</a></span> (emphasis added; footnote omitted).</blockquote>
<p id="b265-5">See also <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#168" aria-description="Citation for case: Maine v. Moulton"><em>id., </em>at 168</a></span> (“[T]he purpose of their meeting was to discuss the <em>pending charges”); id., </em>at 177 (“[T]he police knew... that Moulton and [the informant] were meeting for the express purpose of discussing the <em>pending charges </em>...” (emphasis added)). Thus, respondent’s reliance on <em>Moulton </em>is misplaced and, in light of the language employed there and subsequently in <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">McNeil</a></span>, </em>puzzling.</p>
<p id="b265-6">Respondent predicts that the offense-specific rule will prove “disastrous” to suspects’ constitutional rights and will “permit law enforcement officers almost complete and total license to conduct unwanted and uncounseled interrogations.” Brief for Respondent 8-9. Besides offering no evidence that such a parade of horribles has occurred in those jurisdictions that have not enlarged upon <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">McNeil</a></span>, </em>he fails to appreciate the significance of two critical considerations. First, there can be no doubt that a suspect must be apprised of his rights against compulsory self-incrimination and to consult with an attorney before authorities may conduct custodial interrogation. See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>; <em>Dickerson </em>v. <em>United States, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#435" aria-description="Citation for case: Dickerson v. United States">530 U.S. 428, 435</a></span> (2000) (quoting Miranda.). In the present ease, police scrupulously followed <em>Miranda’s, </em>dictates when questioning respondent.<footnotemark>2</footnotemark> Second, it is critical to recognize that the Con<page-number citation-index="1" label="172">*172</page-number>stitution does not negate society’s interest in the ability of police to talk to witnesses and suspects, even those who have been charged with other offenses.</p>
<blockquote id="b266-5">“Since the ready ability to obtain uncoereed confessions is not an evil but an unmitigated good, society would be the loser. Admissions of guilt resulting from valid <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waivers ‘are more than merely “desirable”; they are essential to society’s compelling interest in finding, convicting, and punishing those who violate the law.’ ” <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">McNeil</a></span>, </em>501U. S., at 181 (quoting <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#426" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 426</a></span> (1986)).</blockquote>
<p id="b266-6">See also <em>Moulton, supra, </em>at 180 (“[T]o exclude evidence pertaining to charges as to which the Sixth Amendment right to counsel had not attached at the time the evidence was obtained, simply because other charges were pending at that time, would unnecessarily frustrate the public’s interest in the investigation of criminal activities”).</p>
<p id="b266-7">Although it is clear that the Sixth Amendment right to counsel attaches only to charged offenses, we have reeog-<page-number citation-index="1" label="173">*173</page-number>nized in other contexts that the definition of an “offense” is not necessarily limited to the four corners of a charging instrument. In <em>Blockburger </em>v. <em>United States, </em><span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/" aria-description="Citation for case: Blockburger v. United States">284 U. S. 299</a></span> (1932), we explained that “where the same act or transaction constitutes a violation of two distinct statutory provisions, the test to be applied to determine whether there are two offenses or only one, is whether each provision requires proof of a fact which the other does not.” <span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/#304" aria-description="Citation for case: Blockburger v. United States"><em>Id., </em>at 304</a></span>. We have since applied the <em><span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/" aria-description="Citation for case: Blockburger v. United States">Blockburger</a></span> </em>test to delineate the scope of the Fifth Amendment’s Double Jeopardy Clause, which prevents multiple or successive prosecutions for the “same offence.” See, <em>e. g., Brown </em>v. <em>Ohio, </em><span class="citation" data-id="9426874"><a href="/opinion/109695/brown-v-ohio/#164" aria-description="Citation for case: Brown v. Ohio">432 U. S. 161, 164-166</a></span> (1977). We see no constitutional difference between the meaning of the term “offense” in the contexts of double jeopardy and of the right to counsel. Accordingly, we hold that when the Sixth Amendment right to counsel attaches, it does encompass offenses that, even if not formally charged, would be considered the same offense under the <em>Block-burger </em>test.<footnotemark>3</footnotemark></p>
<p id="b267-5">While simultaneously conceding that its own test “lacks the precision for which police officers may hope,” <em>post, </em>at 186, the dissent suggests that adopting Blockburger’s definition of “offense” will prove difficult to administer. But it is the dissent’s vague iterations of the “ ‘closely related to’ ” or “‘inextricably intertwined with’” test, <em>post, </em>at 186, that would defy simple application. The dissent seems to presuppose that officers will possess complete knowledge of the circumstances surrounding an incident, such that the officers will be able to tailor their investigation to avoid addressing factually related offenses. Such an assumption, however, ignores the reality that police often are not yet aware of the <page-number citation-index="1" label="174">*174</page-number>exact sequence and scope of events they are investigating— indeed, that is why police must investigate in the first place. Deterred by the possibility of violating the Sixth Amendment, police likely would refrain from questioning certain defendants altogether.</p>
<p id="b268-5">It remains only to apply these principles to the facts at hand. At the time he confessed to Odessa police, respondent had been indicted for burglary of the Owings residence, but he had not been charged in the murders of Margaret and Kori Rae. As defined by Texas law, burglary and capital murder are not the same offense under <em><span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/" aria-description="Citation for case: Blockburger v. United States">Blockburger</a></span>. </em>Compare <span class="citation no-link">Tex. Penal Code Ann. § 30.02</span>(a) (1994) (requiring entry into or continued concealment in a habitation or building) with § 19.03(a)(7)(A) (requiring murder of more than one person during a single criminal transaction). Accordingly, the Sixth Amendment right to counsel did not bar police from interrogating respondent regarding the murders, and respondent’s confession was therefore admissible.</p>
<p id="b268-6">The judgment of the Court of Criminal Appeals of Texas is reversed.</p>
<p id="b268-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b262-8"> See, <em>e.g., United States </em>v. <em>Covarrubias, 179 </em>F. 3d 1219, 1223-1224 (CA9 1999); <em>United States </em>v. <em>Melgar, </em><span class="citation" data-id="752877"><a href="/opinion/752877/united-states-v-jose-aldalberto-melgar-aka-jose-aldalberto/#1013" aria-description="Citation for case: United States v. Jose Aldalberto Melgar, A/K/A Jose...">139 F. 3d 1005, 1013</a></span> (CA4 1998); <em>United States </em>v. <em>Doherty, </em><span class="citation" data-id="9490677"><a href="/opinion/746894/united-states-v-ross-allen-doherty/#776" aria-description="Citation for case: United States v. Ross Allen Doherty">126 F. 3d 769, 776</a></span> (CA6 1997); <em>United States </em>v. <em>Arnold, </em><span class="citation" data-id="9489990"><a href="/opinion/734234/united-states-v-dean-martin-arnold/#41" aria-description="Citation for case: United States v. Dean Martin Arnold">106 F. 3d 37, 41</a></span> (CA3 1997); <em>United States </em>v. <em>Williams, </em><span class="citation" data-id="606691"><a href="/opinion/606691/united-states-v-frankie-b-williams/#457" aria-description="Citation for case: United States v. Frankie B. Williams">993 F. 2d 451, 457</a></span> (CA5 1993); <em>Commonwealth </em>v. <em>Rainwater, </em><span class="citation" data-id="6451287"><a href="/opinion/6577408/commonwealth-v-rainwater/#556" aria-description="Citation for case: Commonwealth v. Rainwater">425 Mass. 540,556</a></span>, <span class="citation" data-id="6451287"><a href="/opinion/6577408/commonwealth-v-rainwater/#1229" aria-description="Citation for case: Commonwealth v. Rainwater">681 N. E. 2d 1218, 1229</a></span> (1997); <em>In re Pack, </em><span class="citation" data-id="2278126"><a href="/opinion/2278126/in-re-the-interest-of-pack/#354" aria-description="Citation for case: In Re the Interest of Pack">420 Pa. Super. 347, 354-356</a></span>, <span class="citation" data-id="2278126"><a href="/opinion/2278126/in-re-the-interest-of-pack/#1010" aria-description="Citation for case: In Re the Interest of Pack">616 A. 2d 1006,1010-1011</a></span> (1992).</p>
</footnote>
<footnote label="2">
<p id="b265-7"> Curiously, while predicting disastrous consequences for the core values underlying the Sixth Amendment, see <em>post, </em>at 179-183 (opinion of Breyek, J.), the dissenters give short shrift to the Fifth Amendment’s role (as expressed in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em>Dickerson) </em>in protecting a defendant’s right to consult with counsel before talking to police. Even though the Sixth Amendment right to counsel has not attached to uncharged offenses, <page-number citation-index="1" label="172">*172</page-number>defendants retain the ability under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to refuse any police questioning, and, indeed, charged defendants presumably have met with counsel and have had the opportunity to discuss whether it is advisable to invoke those Fifth Amendment rights. Thus, in all but the rarest of cases, the Court’s decision today will have no impact whatsoever upon a defendant’s ability to protect his Sixth Amendment right.</p>
<p id="b266-9">It is also worth noting that, contrary to the dissent’s suggestion, see <em>post, </em>at 177-178, 179, there is no “background principle” of our Sixth Amendment jurisprudence establishing that there may be no contact between a defendant and police without counsel present. The dissent would expand the Sixth Amendment right to the assistance of counsel in a criminal prosecution into a rule which “‘exists to prevent lawyers from taking advantage of uncounseled laypersons and to preserve the integrity of the lawyer-client relationship.’ ” <em>Post, </em>at 181 (quoting ABA Aim. Model Rule of Profesional Conduct 4.2 (4th ed. 1999)). Every profession is competent to define the standards of conduct for its members, but such standards are obviously not controlling in interpretation of constitutional provisions. The Sixth Amendment right to counsel is personal to the defendant and specific to the offense.</p>
</footnote>
<footnote label="3">
<p id="b267-6"> In this sense, we could just as easily describe the Sixth Amendment as “prosecution specific,” insofar as it prevents discussion of charged offenses as well as offenses that, under <em><span class="citation" data-id="101824"><a href="/opinion/101824/blockburger-v-united-states/" aria-description="Citation for case: Blockburger v. United States">Blockburger</a></span>, </em>could not be the subject of a later prosecution. And, indeed, the text of the Sixth Amendment confines its scope to “all criminal <em>prosecutions.”</em></p>
</footnote>
</opinion>
```

---
