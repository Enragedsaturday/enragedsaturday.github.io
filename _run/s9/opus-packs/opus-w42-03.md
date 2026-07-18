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

## GROUP: content/cases/Wilkes v. Wood.md  (`case`, 5 assertions)

### content_page

```
---
title: "Wilkes v. Wood"
type: case
citation: "19 How. St. Tr. 1153 (1763)"
parallel_cite: "98 Eng. Rep. 489; Lofft 1"
neutral_cite: "[1763] EWHC CP J95"
court: "Court of Common Pleas (England)"
court_level: other
circuit: ""
year: 1763
date_decided: 1763-12-06
docket: ""
authority_weight: Historical
treatment:
  field_i_validity: good_law
  as_of_content: 1763-12-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wilkes v. Wood
  varies_by_point: false
  scope_note: "Off-CL record (A16/A17): CL citator lanes intentionally not run. Validity rests on the O1 web-verified page treatment (legacy 'good', as of 2026-06-30) re-seeded post-elevation per the S1 A4 mapping; Wilkes' general-warrant condemnation is favorably restated by SCOTUS (Stanford v. Texas, Marcus, Torres v. Madrid). Authority weight remains Historical (English origin)."
  point_overrides: []
courtlistener:
  opinion_url: ""
  cluster_id: null
  opinion_id: null
  identity_checked: true
homes:
  - page: "[[Common Law Origins]]"
    role: "Key — Anchor (foundational origin)"
related: ["[[Entick v. Carrington]]", "[[Boyd v. United States]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "historical", "common-law-origins", "general-warrant", "fourth-amendment", "exemplary-damages", "english-origins"]
holding: "A general warrant authorizing officers to search for and seize the papers of unnamed persons suspected of seditious libel is unlawful and 'totally subversive of the liberty of the subject'; a jury may award exemplary damages against the officers both to compensate and to punish and deter the practice."
lake:
  record_id: Wilkes v. Wood
  status: verified_off_cl
  projected_at: 2026-07-07
off_cl_links:
  - source: BAILII
    url: "https://www.bailii.org/ew/cases/EWHC/CP/1763/J95.html"
    confirmed:
      caption: "Wilkes v Wood (John WILKES v Robert WOOD)"
      cite: "[1763] EWHC CP J95; 98 ER 489"
      court: Court of Common Pleas
      date: 1763-12-06
    checked_date: 2026-07-06
  - source: "Founders' Constitution"
    url: "https://press-pubs.uchicago.edu/founders/documents/amendIVs4.html"
    confirmed:
      caption: Wilkes v. Wood
      cite: "98 Eng. Rep. 489, 498-99"
      court: C.P.
      date: 1763-12-06
    checked_date: 2026-07-06
---

# Wilkes v. Wood

*19 How. St. Tr. 1153 (C.P. 1763)* · Court of Common Pleas (England) · **Historical** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After John Wilkes, a Member of Parliament, published issue No. 45 of *The North Briton* attacking the King's speech, a Secretary of State (the Earl of Halifax) issued a general warrant directing messengers to arrest the unnamed authors, printers, and publishers of the seditious libel and to seize their papers. Acting under it, officers ransacked Wilkes's house and carried off his papers. Wilkes sued Wood, the Under-Secretary of State who had supervised the search, in an action of trespass.

## Issue
Whether a general warrant — naming no offender and authorizing a search for and seizure of the papers of unidentified suspects — was lawful authority for the entry and seizure, and whether the jury could award exemplary damages.

## Rule
The general warrant was condemned as lawless and dangerous to liberty. Chief Justice Pratt (later Lord Camden) told the jury that "[i]f such a power is truly invested in a Secretary of State, and he can delegate this power, it certainly may affect the person and property of every man in this kingdom, and is totally subversive of the liberty of the subject." — 98 Eng. Rep. at 498–499. ^pin-498

The court also endorsed exemplary damages as both compensation and deterrent: "Damages are designed not only as a satisfaction to the injured person, but likewise as a punishment to the guilty, to deter from any such proceeding for the future, and as a proof of the detestation of the jury to the action itself." — 98 Eng. Rep. at 498–499. ^pin-498b

## Application
The warrant identified no offender and licensed officers to enter homes and seize papers at large — a discretion that, if lawful, would expose every subject's person and property to the Secretary of State's pleasure. Such a general warrant could not justify the trespass on Wilkes's house and the seizure of his papers. Because the intrusion was an affront to liberty as well as a personal injury, the jury was entitled to award damages beyond Wilkes's actual loss, as a punishment to the officers and a deterrent against repetition; it returned a verdict for Wilkes of £1,000.

## Conclusion
Verdict for Wilkes. General warrants of this kind are illegal and subversive of the liberty of the subject, and exemplary damages were a proper response to the official trespass.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Historical** (English origin; Court of Common Pleas).
- *Wilkes* and its companion [[Entick v. Carrington]] are the foundational English general-warrant cases that the Fourth Amendment was framed to enshrine; the U.S. Supreme Court has long treated them as authoritative on the Amendment's original meaning (see [[Boyd v. United States]], and the historical discussion accompanying [[Katz v. United States]]). *Wilkes* is also an early common-law root of punitive damages in civil-rights actions. Its core principles remain good law.

## Appears on
- [[Common Law Origins]] — *Key — Anchor (foundational origin)*

## Sources
- *Wilkes v. Wood*, 19 How. St. Tr. 1153 (C.P. 1763); 98 Eng. Rep. 489 (Lofft 1) — pinpoints: 98 Eng. Rep. at 498–499. No CourtListener record (English King's-era case); identity and quotations confirmed against Howell's State Trials and the English Reports (Lofft). *(Decided in the Court of Common Pleas, Pratt, C.J.)*

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5e2780e5808f6903", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "19 How. St. Tr. 1153 (1763)", "court": "Court of Common Pleas (England)", "neutral_cite": "[1763] EWHC CP J95", "official_citation_present": true, "parallel_cite": "98 Eng. Rep. 489; Lofft 1", "title": "Wilkes v. Wood", "year": "1763"}}
{"assertion_id": "80dfcd121bed2639", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A general warrant authorizing officers to search for and seize the papers of unnamed persons suspected of seditious libel is unlawful and 'totally subversive of the liberty of the subject'; a jury may award exemplary damages against the officers both to compensate and to punish and deter the practice.", "title": "Wilkes v. Wood"}}
{"assertion_id": "89bc583f8ca3c229", "dimension": "support", "kind": "home_role", "locator": {"home": "Common Law Origins"}, "payload": {"home": "Common Law Origins", "role": "Key — Anchor (foundational origin)", "title": "Wilkes v. Wood"}}
{"assertion_id": "388aceef3321a86d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1763-12-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Wilkes v. Wood", "field_i_validity": "good_law", "scope_note": "Off-CL record (A16/A17): CL citator lanes intentionally not run. Validity rests on the O1 web-verified page treatment (legacy 'good', as of 2026-06-30) re-seeded post-elevation per the S1 A4 mapping; Wilkes' general-warrant condemnation is favorably restated by SCOTUS (Stanford v. Texas, Marcus, Torres v. Madrid). Authority weight remains Historical (English origin).", "title": "Wilkes v. Wood", "varies_by_point": "false"}}
{"assertion_id": "5a5ec4067924c6f3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Historical", "title": "Wilkes v. Wood"}}
```

### lake record — Wilkes v. Wood

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wilkes v. Wood",
  "stub": false,
  "status": "verified_off_cl",
  "identity": {
    "case_name": "Wilkes v. Wood",
    "case_name_short": "Wilkes",
    "case_name_full": "John Wilkes v Robert Wood",
    "input_case_name": "Wilkes v. Wood",
    "court": "Court of Common Pleas (England)",
    "court_id": null,
    "court_level": "other",
    "circuit": null,
    "state": null,
    "date_decided": "1763-12-06",
    "year": 1763,
    "docket": null,
    "cluster_id": null,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": null,
    "identity_method": "off_cl",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "outside_cl_corpus_verified_by_off_cl_two_key"
  },
  "citations": {
    "official": {
      "cite": "19 How. St. Tr. 1153",
      "volume": 19,
      "reporter": "How. St. Tr.",
      "page": 1153,
      "type": "official",
      "selected_official": true,
      "source": "off_cl.adjudication"
    },
    "parallel": [
      {
        "cite": "98 Eng. Rep. 489",
        "volume": 98,
        "reporter": "Eng. Rep.",
        "page": 489,
        "type": "parallel",
        "selected_official": false,
        "source": "off_cl.adjudication"
      },
      {
        "cite": "Lofft 1",
        "volume": null,
        "reporter": "Lofft",
        "page": 1,
        "type": "parallel",
        "selected_official": false,
        "source": "off_cl.adjudication"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "[1763] EWHC CP J95",
        "volume": null,
        "reporter": null,
        "page": null,
        "type": "vendor_neutral",
        "selected_official": false,
        "source": "off_cl.adjudication"
      }
    ],
    "all": [
      {
        "cite": "19 How. St. Tr. 1153",
        "volume": 19,
        "reporter": "How. St. Tr.",
        "page": 1153,
        "type": "official",
        "selected_official": true,
        "source": "off_cl.adjudication"
      },
      {
        "cite": "98 Eng. Rep. 489",
        "volume": 98,
        "reporter": "Eng. Rep.",
        "page": 489,
        "type": "parallel",
        "selected_official": false,
        "source": "off_cl.adjudication"
      },
      {
        "cite": "Lofft 1",
        "volume": null,
        "reporter": "Lofft",
        "page": 1,
        "type": "parallel",
        "selected_official": false,
        "source": "off_cl.adjudication"
      },
      {
        "cite": "[1763] EWHC CP J95",
        "volume": null,
        "reporter": null,
        "page": null,
        "type": "vendor_neutral",
        "selected_official": false,
        "source": "off_cl.adjudication"
      }
    ],
    "display": "19 How. St. Tr. 1153 (C.P. 1763)",
    "official_selection": {
      "court_class": "english_historical",
      "selected": "19 How. St. Tr. 1153 (C.P. 1763)",
      "reason": "off_cl_adjudication"
    }
  },
  "pinpoints": [],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1763-12-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wilkes v. Wood",
    "varies_by_point": false,
    "scope_note": "Off-CL record (A16/A17): CL citator lanes intentionally not run. Validity rests on the O1 web-verified page treatment (legacy 'good', as of 2026-06-30) re-seeded post-elevation per the S1 A4 mapping; Wilkes' general-warrant condemnation is favorably restated by SCOTUS (Stanford v. Texas, Marcus, Torres v. Madrid). Authority weight remains Historical (English origin).",
    "point_overrides": [],
    "edges": [],
    "derivation": {}
  },
  "progeny": {
    "complete_query": null,
    "indexed_citing_opinions": null,
    "count_source": "off_cl_na",
    "per_sibling": [],
    "citation_count": null,
    "cache_path": null,
    "enumeration": null,
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [
    {
      "source": "BAILII",
      "url": "https://www.bailii.org/ew/cases/EWHC/CP/1763/J95.html",
      "confirmed": {
        "caption": "Wilkes v Wood (John WILKES v Robert WOOD)",
        "cite": "[1763] EWHC CP J95; 98 ER 489",
        "court": "Court of Common Pleas",
        "date": "1763-12-06"
      },
      "checked_date": "2026-07-06"
    },
    {
      "source": "Founders' Constitution",
      "url": "https://press-pubs.uchicago.edu/founders/documents/amendIVs4.html",
      "confirmed": {
        "caption": "Wilkes v. Wood",
        "cite": "98 Eng. Rep. 489, 498-99",
        "court": "C.P.",
        "date": "1763-12-06"
      },
      "checked_date": "2026-07-06"
    }
  ],
  "provenance": {
    "cl_source": null,
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-07T00:53:50Z",
    "date_modified": "2026-07-07T00:53:50Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "off-CL adjudication file: _run/o2-execute/offcl-wilkes-adjudication.json",
        "at": "2026-07-07T00:53:50Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json ('good' -> good_law) + O1 page frontmatter (as of 2026-06-30); re-seeded after verified_off_cl elevation (A17) — F-S2-31's revert applied only while the record was fail-closed",
        "at": "2026-07-06T00:00:00Z",
        "verifier": "orchestrator claude-fable-5 (user R14 Option 1 disposition 2026-07-06)"
      },
      "point_overrides": {
        "src": "verified_off_cl: no CL-derived point overrides",
        "at": "2026-07-07T00:53:50Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "verified_off_cl: no CL lead-opinion pinpoints",
        "at": "2026-07-07T00:53:50Z",
        "verifier": "orchestrator claude-fable-5"
      }
    }
  }
}

```

---

## GROUP: content/cases/Will v. Michigan Department of State Police.md  (`case`, 5 assertions)

### content_page

```
---
title: Will v. Michigan Department of State Police
type: case
citation: "491 U.S. 58 (1989)"
parallel_cite: "109 S. Ct. 2304; 105 L. Ed. 2d 45; 57 U.S.L.W. 4677; 50 Empl. Prac. Dec. (CCH) 39,067; 49 Fair Empl. Prac. Cas. (BNA) 1664"
neutral_cite: 1989 U.S. LEXIS 2975
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-06-15
docket: No. 87-1207
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
  opinion_url: "https://www.courtlistener.com/opinion/112293/will-v-michigan-department-of-state-police/"
  cluster_id: 112293
  opinion_id: null
  identity_checked: true
lake:
  record_id: Will v. Michigan Department of State Police
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Monell v. Department of Social Services]]"
  - "[[Monroe v. Pape]]"
  - "[[Hafer v. Melo]]"
tags:
  - case
  - section-1983
  - state-sovereign-immunity
  - eleventh-amendment
  - official-capacity
  - person
holding: "Neither a State, a state agency, nor a state official sued in his or her official capacity is a 'person' subject to suit for damages under 42 U.S.C. § 1983; because an official-capacity suit is in substance a suit against the State itself, § 1983's word 'person' does not reach it. The holding is limited to States and 'arms of the State' and leaves untouched both Monell municipal liability and official-capacity suits seeking prospective injunctive relief."
aliases:
  - Will v. Michigan Department of State Police
  - Will v. Michigan Dept. of State Police
  - "Will v. Michigan Department of State Police (1989)"
---

# Will v. Michigan Department of State Police

*491 U.S. 58 (1989)* (No. 87-1207) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112293 → combined opinion 112293 (White, J.; 491 U.S. 58, argued Dec. 5, 1988, decided June 15, 1989). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*71`). S9 promotes. -->

## Background
Ray Will sued in Michigan state court under 42 U.S.C. § 1983, alleging he had been denied a promotion in the Michigan Department of State Police for an improper reason — because his brother had been a student activist who was the subject of a "red squad" file. He named the Department of State Police and the Director of State Police in his official capacity. Because the suit was filed in state court, the Eleventh Amendment (which bars federal suits against States) did not apply, squarely presenting whether a State is a "person" amenable to § 1983 at all. The Michigan Supreme Court held that neither the State nor a state official acting in an official capacity is a "person" under § 1983, and the Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]] to resolve a conflict.

## Issue
Whether a State, or a state official acting in his or her official capacity, is a "person" within the meaning of 42 U.S.C. § 1983.

## Rule
Reading § 1983's term "person" against the traditional presumption that "person" does not include the sovereign, and against the rule that Congress must speak with unmistakable clarity before altering the federal-state balance, the Court found nothing in the statute's text or history subjecting the States themselves to § 1983 liability. It extended the same conclusion to official-capacity suits, which are in substance suits against the State: "We hold that neither a State nor its officials acting in their official capacities are 'persons' under § 1983." — 491 U.S. at 71. ^pin-71

## Application
An official-capacity action is not a suit against the official but against the official's office, and so is no different from a suit against the State — allowing it would let a plaintiff circumvent congressional intent by a pleading device. The Court took care to cabin the holding: it applies only to States and entities that are "arms of the State" for Eleventh Amendment purposes, and it leaves *[[Monell v. Department of Social Services|Monell]]* municipal liability intact. It also does not bar official-capacity suits for *prospective injunctive relief*, which under *[[Common Legal Terms#ex-parte|Ex parte]] Young* are not treated as suits against the State. Because Will had sued the State police department and its director in his official capacity for damages, his § 1983 claim could not proceed.

## Conclusion
The judgment of the Supreme Court of Michigan was **affirmed**. White, J., delivered the opinion of the Court. Brennan, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Marshall, Blackmun, and Stevens, JJ., joined.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Will* anchors the "who is a defendant" question in § 1983 litigation: States and their officials in official capacity are not suable "persons" for damages. Teach it against its bookends — *[[Monell v. Department of Social Services]]* (municipalities *are* persons), *[[Hafer v. Melo]]* (state officials sued in their *individual* capacities *are* persons), and the *[[Common Legal Terms#ex-parte|Ex parte]] Young* injunctive-relief exception — as the map of which government defendants § 1983 reaches.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Will v. Michigan Department of State Police*, 491 U.S. 58 (1989)](https://www.courtlistener.com/opinion/112293/will-v-michigan-department-of-state-police/) — pinpoint: 71 (White, J., for the Court; the CL opinion text carries the reporter star `*71` immediately before the paragraph containing the quoted holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3b7d64367110e4a0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "491 U.S. 58 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1989 U.S. LEXIS 2975", "official_citation_present": true, "parallel_cite": "109 S. Ct. 2304; 105 L. Ed. 2d 45; 57 U.S.L.W. 4677; 50 Empl. Prac. Dec. (CCH) 39,067; 49 Fair Empl. Prac. Cas. (BNA) 1664", "title": "Will v. Michigan Department of State Police", "year": "1989"}}
{"assertion_id": "2963d781cdb9773f", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Anchor", "title": "Will v. Michigan Department of State Police"}}
{"assertion_id": "abbe1b2e6294c555", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Neither a State, a state agency, nor a state official sued in his or her official capacity is a 'person' subject to suit for damages under 42 U.S.C. § 1983; because an official-capacity suit is in substance a suit against the State itself, § 1983's word 'person' does not reach it. The holding is limited to States and 'arms of the State' and leaves untouched both Monell municipal liability and official-capacity suits seeking prospective injunctive relief.", "title": "Will v. Michigan Department of State Police"}}
{"assertion_id": "538e78c3c8887d5f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Will v. Michigan Department of State Police"}}
{"assertion_id": "c7e77ced77cef180", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Will v. Michigan Department of State Police", "varies_by_point": "false"}}
```

### lake record — Will v. Michigan Department of State Police

```json
{
  "schema_version": "s2.v1",
  "record_id": "Will v. Michigan Department of State Police",
  "status": "under_review",
  "identity": {
    "case_name": "Will v. Michigan Department of State Police",
    "case_name_short": "Will",
    "case_name_full": "WILL v. MICHIGAN DEPARTMENT OF STATE POLICE Et Al.",
    "input_case_name": "Will v. Michigan Department of State Police",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-06-15",
    "year": 1989,
    "docket": "No. 87-1207",
    "cluster_id": 112293,
    "lead_opinion_id": 9431737,
    "sibling_ids": [],
    "absolute_url": "/opinion/112293/will-v-michigan-department-of-state-police/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "491 U.S. 58",
      "volume": "491",
      "reporter": "U.S.",
      "page": "58",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 2304",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "2304",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 L. Ed. 2d 45",
        "volume": "105",
        "reporter": "L. Ed. 2d",
        "page": "45",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4677",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4677",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 Empl. Prac. Dec. (CCH) 39,067",
        "volume": "50",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "39,067",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Fair Empl. Prac. Cas. (BNA) 1664",
        "volume": "49",
        "reporter": "Fair Empl. Prac. Cas. (BNA)",
        "page": "1664",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 2975",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "2975",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "491 U.S. 58",
        "volume": "491",
        "reporter": "U.S.",
        "page": "58",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 2304",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "2304",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 L. Ed. 2d 45",
        "volume": "105",
        "reporter": "L. Ed. 2d",
        "page": "45",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 2975",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "2975",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4677",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4677",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 Empl. Prac. Dec. (CCH) 39,067",
        "volume": "50",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "39,067",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Fair Empl. Prac. Cas. (BNA) 1664",
        "volume": "49",
        "reporter": "Fair Empl. Prac. Cas. (BNA)",
        "page": "1664",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "491 U.S. 58",
    "official_selection": {
      "court_class": "scotus",
      "selected": "491 U.S. 58",
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
    "date_created": "2026-07-06T13:18:32Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "will-v-michigan-department-of-state-police--112293",
      "to_record_id": "Will v. Michigan Department of State Police",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Will v. Michigan Department of State Police

```
<opinion type="majority">
<author id="b92-4"><page-number citation-index="1" label="60">*60</page-number>Justice White</author>
<p id="AHF">delivered the opinion of the Court.</p>
<p id="b92-5">This case presents the question whether a State, or an official of the State while acting in his or her official capacity, is a “person” within the meaning of Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>.</p>
<p id="b92-6">Petitioner Ray Will filed suit in Michigan Circuit Court alleging various violations of the United States and Michigan Constitutions as grounds for a claim under §1983.<footnotemark>1</footnotemark> He alleged that he had been denied a promotion to a data systems analyst position with the Department of State Police for an improper reason, that is, because his brother had been a student activist and the subject of a “red squad” file maintained by respondent. Named as defendants were the Department of State Police and the Director of State Police in his official capacity, also a respondent here.<footnotemark>2</footnotemark></p>
<p id="b92-7">The Circuit Court remanded the case to the Michigan Civil Service Commission for a grievance hearing. While the grievance was pending, petitioner filed suit in the Michigan <page-number citation-index="1" label="61">*61</page-number>Court of Claims raising an essentially identical § 1983 claim. The Civil Service Commission ultimately found in petitioner’s favor, ruling that respondents had refused to promote petitioner because of “partisan considerations.” App. 46. On the basis of that finding, the state-court judge, acting in both the Circuit Court and the Court of Claims cases, concluded that petitioner had established a violation of the United States Constitution. The judge held that the Circuit Court action was barred under state law but that the Claims Court action could go forward. The judge also ruled that respondents were persons for purposes of § 1983.</p>
<p id="b93-5">The Michigan Court of Appeals vacated the judgment against the Department of State Police, holding that a State is not a person under § 1983, but remanded the case for determination of the possible immunity of the Director of State Police from liability for damages. The Michigan Supreme Court granted discretionary review and affirmed the Court of Appeals in part and reversed in part. <em>Smith </em>v. <em>Department of Pub. Health, </em><span class="citation" data-id="9583320"><a href="/opinion/1250599/smith-v-department-of-public-health/" aria-description="Citation for case: Smith v. Department of Public Health">428 Mich. 540</a></span>, <span class="citation" data-id="9583320"><a href="/opinion/1250599/smith-v-department-of-public-health/" aria-description="Citation for case: Smith v. Department of Public Health">410 N. W. 2d 749</a></span> (1987). The Supreme Court agreed that the State itself is not a person under § 1983, but held that a state official acting in his or her official capacity also is not such a person.</p>
<p id="b93-6">The Michigan Supreme Court’s holding that a State is not a person under § 1983 conflicts with a number of state- and federal-court decisions to the contrary.<footnotemark>3</footnotemark> We granted certio-rari to resolve the conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./485/1005/">485 U. S. 1005</a></span> (1988).</p>
<p id="b94-4"><page-number citation-index="1" label="62">*62</page-number>Prior to <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation multiple-matches"><a href="/c/U.%20S./436/668/">436 U. S. 668</a></span> (1978), the question whether a State is a person within the meaning of § 1983 had been answered by this Court in the negative. In <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#187" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167, 187-191</a></span> (1961), the Court had held that a municipality was not a person under § 1983. “[T]hat being the case,” we reasoned, § 1983 “could not have been intended to include States as parties defendant.” <em>Fitzpatrick </em>v. <em>Bitzer, </em><span class="citation" data-id="9426527"><a href="/opinion/109520/fitzpatrick-v-bitzer/#452" aria-description="Citation for case: Fitzpatrick v. Bitzer">427 U. S. 446, 452</a></span> (1976).</p>
<p id="b94-5">But in <em>Monell, </em>the Court overruled <em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>, </em>holding that a municipality was a person under § 1983. 436 U. S., at 690. Since then, various members of the Court have debated whether a State is a person within the meaning of § 1983, see <em>Hutto </em>v. <em>Finney, </em><span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/#700" aria-description="Citation for case: Hutto v. Finney">437 U. S. 678, 700-704</a></span> (1978) (Brennan, J., concurring); <span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/#708" aria-description="Citation for case: Hutto v. Finney"><em>id., </em>at 708, n. 6</a></span> (Powell, J., concurring in <page-number citation-index="1" label="63">*63</page-number>part and dissenting in part), but this Court has never expressly dealt with that issue.<footnotemark>4</footnotemark></p>
<p id="b95-5">Some courts, including the Michigan Supreme Court here, have construed our decision in <em>Quern </em>v. <em>Jordan, </em><span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/" aria-description="Citation for case: Quern v. Jordan">440 U. S. 332</a></span> (1979), as holding by implication that a State is not a person under § 1983. See <em>Smith </em>v. <em>Department of Pub. Health, supra, </em>at 581, <span class="citation" data-id="9583320"><a href="/opinion/1250599/smith-v-department-of-public-health/#767" aria-description="Citation for case: Smith v. Department of Public Health">410 N. W. 2d, at 767</a></span>. See also, <em>e. g., State </em>v. <em>Green, </em><span class="citation" data-id="9601929"><a href="/opinion/1363313/state-v-green/#1382" aria-description="Citation for case: State v. Green">633 P. 2d 1381, 1382</a></span> (Alaska 1981); <em>Woodbridge </em>v. <em>Worcester State Hospital, </em><span class="citation" data-id="2100692"><a href="/opinion/2100692/woodbridge-v-worcester-state-hospital/#44" aria-description="Citation for case: Woodbridge v. Worcester State Hospital">384 Mass. 38, 44-45, n. 7</a></span>, <span class="citation" data-id="2100692"><a href="/opinion/2100692/woodbridge-v-worcester-state-hospital/#786" aria-description="Citation for case: Woodbridge v. Worcester State Hospital">423 N. E. 2d 782, 786, n. 7</a></span> (1981); <em>Edgar </em>v. <em>State, </em><span class="citation" data-id="1365811"><a href="/opinion/1365811/edgar-v-state/#221" aria-description="Citation for case: Edgar v. State">92 Wash. 2d 217, 221</a></span>, <span class="citation" data-id="1365811"><a href="/opinion/1365811/edgar-v-state/#537" aria-description="Citation for case: Edgar v. State">595 P. 2d 534, 537</a></span> (1979), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/1077/">444 U. S. 1077</a></span> (1980). <em><span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/" aria-description="Citation for case: Quern v. Jordan">Quern</a></span> </em>held that §1983 does not override a State’s Eleventh Amendment immunity, a holding that the concurrence suggested was “patently dicta” to the effect that a State is not a person, <span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/#350" aria-description="Citation for case: Quern v. Jordan">440 U. S., at 350</a></span> (Brennan, J., concurring in judgment).</p>
<p id="b95-6">Petitioner filed the present § 1983 actions in Michigan state court, which places the question whether a State is a person under § 1983 squarely before us since the Eleventh Amend<page-number citation-index="1" label="64">*64</page-number>ment does not apply in state courts. <em>Maine </em>v. <em>Thiboutot, </em><span class="citation" data-id="9428027"><a href="/opinion/110322/maine-v-thiboutot/#9" aria-description="Citation for case: Maine v. Thiboutot">448 U. S. 1, 9, n. 7</a></span> (1980). For the reasons that follow, we reaffirm today what we had concluded prior to <em>Monell </em>and what some have considered implicit in <em><span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/" aria-description="Citation for case: Quern v. Jordan">Quern</a></span>: </em>that a State is not a person within the meaning of § 1983.</p>
<p id="b96-5">We observe initially that if a State is a “person” within the meaning of § 1983, the section is to be read as saying that “every person, including a State, who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia, subjects . . . .” That would be a decidedly awkward way of expressing an intent to subject the States to liability. At the very least, reading the statute in this way is not so clearly indicated that it provides reason to depart from the often-expressed understanding that “fin common usage, the term ‘person’ does not include the sovereign, [and] statutes employing the [word] are ordinarily construed to exclude it.’” <em>Wilson </em>v. <em>Omaha Tribe, </em><span class="citation" data-id="9427633"><a href="/opinion/110115/wilson-v-omaha-indian-tribe/#667" aria-description="Citation for case: Wilson v. Omaha Indian Tribe">442 U. S. 653, 667</a></span> (1979) (quoting <em>United States </em>v. <em>Cooper Corp., </em><span class="citation" data-id="9419152"><a href="/opinion/103494/united-states-v-cooper-corp/#604" aria-description="Citation for case: United States v. Cooper Corp.">312 U. S. 600, 604</a></span> (1941)). See also <em>United States </em>v. <em>Mine Workers, </em><span class="citation" data-id="9419944"><a href="/opinion/104385/united-states-v-united-mine-workers-of-america/#275" aria-description="Citation for case: United States v. United Mine Workers of America">330 U. S. 258, 275</a></span> (1947).</p>
<p id="b96-6">This approach is particularly applicable where it is claimed that Congress has subjected the States to liability to which they had not been subject before. In <em>Wilson </em>v. <em>Omaha <span class="citation" data-id="9427633"><a href="/opinion/110115/wilson-v-omaha-indian-tribe/" aria-description="Citation for case: Wilson v. Omaha Indian Tribe">Tribe, supra,</a></span> </em>we followed this rule in construing the phrase “white person” contained in <span class="citation no-link">25 U. S. C. § 194</span>, enacted as Act of June 30, 1834, <span class="citation no-link">4 Stat. 729</span>, as not including the “sovereign States of the Union.” <span class="citation" data-id="9427633"><a href="/opinion/110115/wilson-v-omaha-indian-tribe/#667" aria-description="Citation for case: Wilson v. Omaha Indian Tribe">442 U. S., at 667</a></span>. This common usage of the term “person” provides a strong indication that “person” as used in § 1983 likewise does not include a State.<footnotemark>5</footnotemark></p>
<p id="b97-4"><page-number citation-index="1" label="65">*65</page-number>The language of § 1983 also falls far short of satisfying the ordinary rule of statutory construction that if Congress intends to alter the “usual constitutional balance between the States and the Federal Government,” it must make its intention to do so “unmistakably clear in the language of the statute.” <em>Atascadero State Hospital </em>v. <em>Scanlon, </em><span class="citation" data-id="9430157"><a href="/opinion/111503/atascadero-state-hospital-v-scanlon/#242" aria-description="Citation for case: Atascadero State Hospital v. Scanlon">473 U. S. 234, 242</a></span> (1985); see also <em>Pennhurst State School and Hospital </em>v. <em>Halderman, </em><span class="citation" data-id="9429483"><a href="/opinion/111094/pennhurst-state-school-and-hospital-v-halderman/#99" aria-description="Citation for case: Pennhurst State School and Hospital v. Halderman">465 U. S. 89, 99</a></span> (1984). <em>Atascadero </em>was an Eleventh Amendment case, but a similar approach is applied in other contexts. Congress should make its intention “clear and manifest” if it intends to pre-empt the historic powers of the States, <em>Rice </em>v. <em>Santa Fe Elevator Corp., </em><span class="citation" data-id="9420000"><a href="/opinion/104425/rice-v-santa-fe-elevator-corp/#230" aria-description="Citation for case: Rice v. Santa Fe Elevator Corp.">331 U. S. 218, 230</a></span> (1947), or if it intends to impose a condition on the grant of federal moneys, <em>Pennhurst State School and Hospital </em>v. <em>Halderman, </em><span class="citation" data-id="9428284"><a href="/opinion/110458/pennhurst-state-school-and-hospital-v-halderman/#16" aria-description="Citation for case: Pennhurst State School and Hospital v. Halderman">451 U. S. 1, 16</a></span> (1981); <em>South Dakota </em>v. <em>Dole, </em><span class="citation" data-id="9431078"><a href="/opinion/111939/south-dakota-v-dole/#207" aria-description="Citation for case: South Dakota v. Dole">483 U. S. 203, 207</a></span> (1987). “In traditionally sensitive areas, such as legislation affecting the federal balance, the requirement of clear statement assures that the legislature has in fact faced, and intended to bring into issue, the critical matters involved in the judicial decision.” <em>United States </em>v. <em>Bass, </em><span class="citation" data-id="9424710"><a href="/opinion/108421/united-states-v-bass/#349" aria-description="Citation for case: United States v. Bass">404 U. S. 336, 349</a></span> (1971).</p>
<p id="b97-5">Our conclusion that a State is not a “person” within the meaning of § 1983 is reinforced by Congress’ purpose in en<page-number citation-index="1" label="66">*66</page-number>acting the statute. Congress enacted § 1 of the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, the precursor .to § 1983, shortly after the end of the Civil War “in response to the widespread deprivations of civil rights in the Southern States and the inability or unwillingness of authorities in those States to protect those rights or punish wrongdoers.” <em>Felder </em>v. <em>Casey, </em><span class="citation" data-id="9431388"><a href="/opinion/112121/felder-v-casey/#147" aria-description="Citation for case: Felder v. Casey">487 U. S. 131, 147</a></span> (1988). Although Congress did not establish federal courts as the exclusive forum to remedy these deprivations, <em>ibid., </em>it is plain that “Congress assigned to the federal courts a paramount role” in this endeavor, <em>Patsy </em>v. <em>Board of Regents of Florida, </em><span class="citation" data-id="9428841"><a href="/opinion/110753/patsy-v-board-of-regents-of-fla/#503" aria-description="Citation for case: Patsy v. Board of Regents of Fla.">457 U. S. 496, 503</a></span> (1982).</p>
<p id="b98-5">Section 1983 provides a federal forum to remedy many deprivations of civil liberties, but it does not provide a federal forum for litigants who seek a remedy against a State for alleged deprivations of civil liberties. The Eleventh Amendment bars such suits unless the State has waived its immunity, <em>Welch </em>v. <em>Texas Dept. of Highways and Public Transportation, </em><span class="citation" data-id="9431106"><a href="/opinion/111949/welch-v-texas-department-of-highways-public-transportation/#472" aria-description="Citation for case: Welch v. Texas Department of Highways &amp; Public...">483 U. S. 468, 472-473</a></span> (1987) (plurality opinion), or unless Congress has exercised its undoubted power under § 5 of the Fourteenth Amendment to override that immunity. That Congress, in passing § 1983, had no intention to disturb the States’ Eleventh Amendment immunity and so to alter the federal-state balance in that respect was made clear in our decision in <em><span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/" aria-description="Citation for case: Quern v. Jordan">Quern</a></span>. </em>Given that a principal purpose behind the enactment of § 1983 was to provide a federal forum for civil rights claims, and that Congress did not provide such a federal forum for civil rights claims against States, we cannot accept petitioner’s argument that Congress intended nevertheless to create a cause of action against States to be brought in state courts, which are precisely the courts Congress sought to allow civil rights claimants to avoid through § 1983.</p>
<p id="b98-6">This does not mean, as petitioner suggests, that we think that the scope of the Eleventh Amendment and the scope of § 1983 are not separate issues. Certainly they are. But in deciphering congressional intent as to the scope of § 1983, the <page-number citation-index="1" label="67">*67</page-number>scope of the Eleventh Amendment is a consideration, and we decline to adopt a reading of § 1983 that disregards it.<footnotemark>6</footnotemark></p>
<p id="b99-5">Our conclusion is further supported by our holdings that in enacting §1983, Congress did not intend to override well-established immunities or defenses under the common law. “One important assumption underlying the Court’s decisions in this area is that members of the 42d Congress were familiar with common-law principles, including defenses previously recognized in ordinary tort litigation, and that they likely intended these common-law principles to obtain, absent specific provisions to the contrary.” <em>Newport </em>v. <em>Fact Concerts, Inc., </em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/#258" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S. 247, 258</a></span> (1981). <em>Stump </em>v. <em>Sparkman, </em><span class="citation" data-id="9427113"><a href="/opinion/109820/stump-v-sparkman/#356" aria-description="Citation for case: Stump v. Sparkman">435 U. S. 349, 356</a></span> (1978); <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#247" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 247</a></span> (1974); <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 554</a></span> (1967); and <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 376</a></span> (1951), are also to this effect. The doctrine of sovereign immunity was a familiar doctrine at common law. “The principle is elementary that a State cannot be sued in its own courts without its consent.” <em>Railroad Co. </em>v. <em>Tennessee, </em><span class="citation" data-id="90132"><a href="/opinion/90132/railroad-co-v-tennessee/#339" aria-description="Citation for case: Railroad Co. v. Tennessee">101 U. S. 337, 339</a></span> (1880). It is an “established principle of jurisprudence” that the sovereign cannot be sued in its own courts without its consent. <em>Beers </em>v. <em>Arkansas, </em><span class="citation" data-id="87177"><a href="/opinion/87177/beers-ex-rel-platenius-v-arkansas/#529" aria-description="Citation for case: Beers Ex Rel. Platenius v. Arkansas">20 How. 527, 529</a></span> (1858). We cannot conclude that § 1983 was intended to disregard the well-established immunity of a State from being sued without its consent.<footnotemark>7</footnotemark></p>
<p id="b100-4"><page-number citation-index="1" label="68">*68</page-number>The legislative history of § 1983 does not suggest a different conclusion. Petitioner contends that the congressional debates on § 1 of the 1871 Act indicate that § 1983 was intended to extend to the full reach of the Fourteenth Amendment and thereby to provide a remedy “ ‘against all forms of official violation of federally protected rights.”’ Brief for Petitioner 16 (quoting <em>Monell, </em>436 U. S., at 700-701). He refers us to various parts of the vigorous debates accompanying the passage of § 1983 and revealing that it was the failure of the States to take appropriate action that was undoubtedly the motivating force behind § 1983. The inference must be drawn, it is urged, that Congress must have intended to subject the States themselves to liability. But the intent of Congress to provide a remedy for unconstitutional state action does not without more include the sovereign States among those persons against whom § 1983 actions would lie. Construing § 1983 as a remedy for “official violation of federally protected rights” does no more than confirm that the section is directed against state action — action “under color of” state law. It does not suggest that the State itself was a person that Congress intended to be subject to liability.</p>
<p id="b100-5">Although there were sharp and heated debates, the discussion of § 1 of the bill, which contained the present § 1983, was not extended. And although in other respects the impact on state sovereignty was much talked about, no one suggested that § 1 would subject the States themselves to a damages suit under federal law. <em>Quern, </em><span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/#343" aria-description="Citation for case: Quern v. Jordan">440 U. S., at 343</a></span>. There was complaint that § 1 would subject state officers to damages liability, but no suggestion that it would also expose the States themselves. Cong. Globe, 42d Cong., 1st Sess., <page-number citation-index="1" label="69">*69</page-number>366, 385 (1871). We find nothing substantial in the legislative history that leads us to believe that Congress intended that the word “person” in § 1983 included the States of the Union. And surely nothing in the debates rises to the clearly expressed legislative intent necessary to permit that construction.</p>
<p id="b101-5">Likewise, the Act of Feb. 25, 1871, §2, <span class="citation no-link">16 Stat. 431</span> (the “Dictionary Act”),<footnotemark>8</footnotemark> on which we relied in <em>Monell, supra, </em>at 688-689, does not counsel a contrary conclusion here. As we noted in <em><span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/" aria-description="Citation for case: Quern v. Jordan">Quern</a></span>, </em>that Act, while adopted prior to § 1 of the Civil Rights Act of 1871, was adopted after §2 of the Civil Rights Act of 1866, from which § 1 of the 1871 Act was derived. <span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/#341" aria-description="Citation for case: Quern v. Jordan">440 U. S., at 341, n. 11</a></span>. Moreover, we disagree with Justice Brennan that at the time the Dictionary Act was passed “the phrase ‘bodies politic and corporate’ was understood to include the States.” <em>Post, </em>at 78. Rather, an examination of authorities of the era suggests that the phrase was used to mean corporations, both private and public (municipal), and not to include the States.<footnotemark>9</footnotemark> In our view, the <page-number citation-index="1" label="70">*70</page-number>Dictionary Act, like § 1983 itself and its legislative history, fails to evidence a clear congressional intent that States be held liable.</p>
<p id="b102-5">Finally, <em>Monell </em>itself is not to the contrary. True, prior to <em>Monell </em>the Court had reasoned that -if municipalities were not persons then surely States also were not. <em>Fitzpatrick </em>v. <em>Bitzer, </em><span class="citation" data-id="9426527"><a href="/opinion/109520/fitzpatrick-v-bitzer/#452" aria-description="Citation for case: Fitzpatrick v. Bitzer">427 U. S., at 452</a></span>. And <em>Monell </em>overruled <em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span>, </em>undercutting that logic. But it does not follow that if municipalities are persons then so are States. States are protected by the Eleventh Amendment while municipalities are not, <em>Monell, </em>436 U. S., at 690, n. 54, and we consequently limited our holding in <em>Monell </em>“to local government units which are not considered part of the State for Eleventh Amendment purposes,” <em>ibid. </em>Conversely, our holding here does not cast any doubt on <em>Monell, </em>and applies only to States or governmental entities that are considered “arms of the State” for Eleventh Amendment purposes. See, <em>e. g., Mt. Healthy Bd. of Ed. </em>v. <em>Doyle, </em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/#280" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U. S. 274, 280</a></span> (1977).</p>
<p id="b102-6">Petitioner asserts, alternatively, that state officials should be considered “persons” under § 1983 even though acting in their official capacities. In this case, petitioner named as defendant not only the Michigan Department of State Police but also the Director of State Police in his official capacity.</p>
<p id="b103-4"><page-number citation-index="1" label="71">*71</page-number>Obviously, state officials literally are persons. But a suit against a state official in his or her official capacity is not a suit against the official but rather is a suit against the official’s office. <em>Brandon </em>v. <em>Holt, </em><span class="citation" data-id="9429823"><a href="/opinion/111304/brandon-v-holt/#471" aria-description="Citation for case: Brandon v. Holt">469 U. S. 464, 471</a></span> (1985). As such, it is no different from a suit against the State itself. See, <em>e. g., Kentucky </em>v. <em>Graham, </em><span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/#165" aria-description="Citation for case: Kentucky v. Graham">473 U. S. 159, 165-166</a></span> (1985); <em>Monell, supra, </em>at 690, n. 55. We see no reason to adopt a different rule in the present context, particularly when such a rule would allow petitioner to circumvent congressional intent by a mere pleading device.<footnotemark>10</footnotemark></p>
<p id="b103-5">We hold that neither a State nor its officials acting in their official capacities are “persons” under § 1983. The judgment of the Michigan Supreme Court is affirmed.</p>
<p id="b103-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b92-9"> Section 1983 provides as follows:</p>
<blockquote id="b92-10">“Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress. For the purposes of this section, any Act of Congress applicable exclusively to the District of Columbia shall be considered to be a statute of the District of Columbia.” <span class="citation no-link">42 U. S. C. § 1983</span>.</blockquote>
</footnote>
<footnote label="2">
<p id="b92-11"> Also named as defendants were the Michigan Department of Civil Service and the State Personnel Director, but those parties were subsequently dismissed by the state courts.</p>
</footnote>
<footnote label="3">
<p id="b93-7"> The courts in the following cases have taken the position that a State is a person under § 1983. See <em>Della Grotta </em>v. <em>Rhode Island, </em><span class="citation" data-id="463302"><a href="/opinion/463302/anthony-della-grotta-v-state-of-rhode-island/#349" aria-description="Citation for case: Anthony Della Grotta v. State of Rhode Island">781 F. 2d 343, 349</a></span> (CA1 1986); <em>Gay Student Services </em>v. <em>Texas A&amp;M University, </em><span class="citation" data-id="373013"><a href="/opinion/373013/gay-student-services-v-texas-a-m-university/#163" aria-description="Citation for case: Gay Student Services v. Texas a &amp; M University">612 F. 2d 160, 163-164</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/1034/">449 U. S. 1034</a></span> (1980); <em>Uberoi </em>v. <em>University of Colorado, </em><span class="citation" data-id="9562722"><a href="/opinion/1209164/uberoi-v-university-of-colorado/#900" aria-description="Citation for case: Uberoi v. University of Colorado">713 P. 2d 894, 900-901</a></span> (Colo. 1986); <em>Stanton </em>v. <em>Godfrey, </em><span class="citation" data-id="2042378"><a href="/opinion/2042378/stanton-v-godfrey/#107" aria-description="Citation for case: Stanton v. Godfrey">415 N. E. 2d 103, 107</a></span> (Ind. App. 1981); <em>Gumbhir </em>v. <em>Kansas State Bd. of </em>Pharmacy, <span class="citation" data-id="1381147"><a href="/opinion/1381147/gumbhir-v-kansas-state-board-of-pharmacy/#512" aria-description="Citation for case: Gumbhir v. Kansas State Board of Pharmacy">231 Kan. 507, 512-513</a></span>, <span class="citation" data-id="1381147"><a href="/opinion/1381147/gumbhir-v-kansas-state-board-of-pharmacy/#1084" aria-description="Citation for case: Gumbhir v. Kansas State Board of Pharmacy">646 P. 2d 1078, 1084</a></span> (1982), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./459/1103/">459 U. S. 1103</a></span> (1983); <em>Rahmah Navajo School Bd., Inc. </em>v. <em>Bureau of Revenue, </em>104 N. M. 302, 310, <span class="citation" data-id="1389862"><a href="/opinion/1389862/ramah-navajo-school-board-inc-v-bureau-of-revenue/#1251" aria-description="Citation for case: Ramah Navajo School Board, Inc. v. Bureau of Revenue">720 P. 2d 1243, 1251</a></span> (App.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./479/940/">479 U. S. 940</a></span> (1986).</p>
<p id="b93-8">A larger number of courts have agreed with the Michigan Supreme Court that a State is not a person under § 1983. See <em>Ruiz </em>v. <em>Estelle, </em><span class="citation" data-id="404985"><a href="/opinion/404985/david-r-ruiz-united-states-of-america-intervenor-appellee-v-w-j/#1137" aria-description="Citation for case: David R. Ruiz, United States of America,...">679 <page-number citation-index="1" label="62">*62</page-number>F. 2d 1115, 1137</a></span> (CA5), modified on other grounds, <span class="citation" data-id="408178"><a href="/opinion/408178/david-r-ruiz-united-states-of-america-intervenor-appellee-v-w-j/" aria-description="Citation for case: David R. Ruiz, United States of America,...">688 F. 2d 266</a></span> (1982), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./460/1042/">460 U. S. 1042</a></span> (1983); <em>Toledo, P. &amp; W. R. Co. </em>v. <em>Ilinois, </em><span class="citation multiple-matches"><a href="/c/F.%202d/744/1296/">744 F. 2d 1296</a></span>, 1298-1299, and n. 1 (CA7 1984), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./470/1051/">470 U. S. 1051</a></span> (1985); <em>Harris </em>v. <em>Missouri Court of Appeals, </em><span class="citation multiple-matches"><a href="/c/F.%202d/787/427/">787 F. 2d 427</a></span>, 429 (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./479/851/">479 U. S. 851</a></span> (1986); <em>Aubuchon </em>v. <em>Missouri, </em><span class="citation" data-id="382371"><a href="/opinion/382371/lois-cleon-shelton-aubuchon-v-state-of-missouri/#582" aria-description="Citation for case: Lois Cleon Shelton Aubuchon v. State of Missouri">631 F. 2d 581, 582</a></span> (CA8 1980) <em>(per curiam), </em>cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./450/915/">450 U. S. 915</a></span> (1981); <em>State </em>v. <em>Green, </em><span class="citation" data-id="9601929"><a href="/opinion/1363313/state-v-green/#1382" aria-description="Citation for case: State v. Green">633 P. 2d 1381, 1382</a></span> (Alaska 1981); <em>St. Mary’s Hospital and Health Center </em>v. <em>State, </em><span class="citation" data-id="1175642"><a href="/opinion/1175642/st-marys-hospital-health-center-v-state/#11" aria-description="Citation for case: St. Mary&#x27;s Hospital &amp; Health Center v. State">150 Ariz. 8, 11</a></span>, <span class="citation" data-id="1175642"><a href="/opinion/1175642/st-marys-hospital-health-center-v-state/#669" aria-description="Citation for case: St. Mary&#x27;s Hospital &amp; Health Center v. State">721 P. 2d 666, 669</a></span> (App. 1986); <em>Mezey </em>v. <em>State, </em><span class="citation" data-id="2176874"><a href="/opinion/2176874/mezey-v-state-of-california/#1065" aria-description="Citation for case: Mezey v. State of California">161 Cal. App. 3d 1060, 1065</a></span>, <span class="citation" data-id="2176874"><a href="/opinion/2176874/mezey-v-state-of-california/#43" aria-description="Citation for case: Mezey v. State of California">208 Cal. Rptr. 40, 43</a></span> (1984); <em>Hill </em>v. <em>Florida Dept. of Corrections, </em><span class="citation" data-id="1708682"><a href="/opinion/1708682/hill-v-dept-of-corrections/#132" aria-description="Citation for case: Hill v. Dept. of Corrections">513 So. 2d 129, 132</a></span> (Fla. 1987), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./484/1064/">484 U. S. 1064</a></span> (1988); <em>Merritt ex rel. Merritt </em>v. <em>State, </em><span class="citation" data-id="9548950"><a href="/opinion/1177005/merritt-for-merritt-v-state/#26" aria-description="Citation for case: Merritt for Merritt v. State">108 Idaho 20, 26</a></span>, <span class="citation" data-id="9548950"><a href="/opinion/1177005/merritt-for-merritt-v-state/#877" aria-description="Citation for case: Merritt for Merritt v. State">696 P. 2d 871, 877</a></span> (1985); <em>Woodbridge </em>v. <em>Worcester State Hospital, </em><span class="citation" data-id="2100692"><a href="/opinion/2100692/woodbridge-v-worcester-state-hospital/#44" aria-description="Citation for case: Woodbridge v. Worcester State Hospital">384 Mass. 38, 44-45, n. 7</a></span>, <span class="citation" data-id="2100692"><a href="/opinion/2100692/woodbridge-v-worcester-state-hospital/#786" aria-description="Citation for case: Woodbridge v. Worcester State Hospital">423 N. E. 2d 782, 786, n. 7</a></span> (1981); <em>Bird </em>v. <em>State Dept. of Public Safety, </em><span class="citation" data-id="1247197"><a href="/opinion/1247197/bird-v-state-department-of-public-safety/#43" aria-description="Citation for case: Bird v. State, Department of Public Safety">375 N. W. 2d 36, 43</a></span> (Minn. App. 1985); <em>Shaw </em>v. <em>St. Louis, </em><span class="citation" data-id="2446750"><a href="/opinion/2446750/shaw-v-city-of-st-louis/#576" aria-description="Citation for case: Shaw v. City of St. Louis">664 S. W. 2d 572, 576</a></span> (Mo. App. 1983), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./469/849/">469 U. S. 849</a></span> (1984); <em>Fuchilla </em>v. <em>Layman, </em>109 N. J. 319, 323-324, <span class="citation" data-id="9700978"><a href="/opinion/1957182/fuchilla-v-layman/#654" aria-description="Citation for case: Fuchilla v. Layman">537 A. 2d 652, 654</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./488/826/">488 U. S. 826</a></span> (1988); <em>Burkey </em>v. <em>Southern Ohio Correctional Facility, </em><span class="citation" data-id="3724494"><a href="/opinion/3973282/burkey-v-southern-ohio-correctional-facility/#170" aria-description="Citation for case: Burkey v. Southern Ohio Correctional Facility">38 Ohio App. 3d 170, 170-171</a></span>, <span class="citation" data-id="3724494"><a href="/opinion/3973282/burkey-v-southern-ohio-correctional-facility/#608" aria-description="Citation for case: Burkey v. Southern Ohio Correctional Facility">528 N. E. 2d 607, 608</a></span> (1988); <em>Gay </em>v. <em>State, </em><span class="citation" data-id="1675949"><a href="/opinion/1675949/gay-v-state/#157" aria-description="Citation for case: Gay v. State">730 S. W. 2d 154, 157-158</a></span> (Tex. App. 1987); <em>Edgar </em>v. <em>State, </em><span class="citation" data-id="1365811"><a href="/opinion/1365811/edgar-v-state/#221" aria-description="Citation for case: Edgar v. State">92 Wash. 2d 217, 221</a></span>, <span class="citation" data-id="1365811"><a href="/opinion/1365811/edgar-v-state/#537" aria-description="Citation for case: Edgar v. State">595 P. 2d 534, 537</a></span> (1979), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/1077/">444 U. S. 1077</a></span> (1980); <em>Boldt </em>v. <em>State, </em><span class="citation" data-id="2226867"><a href="/opinion/2226867/boldt-v-state/#584" aria-description="Citation for case: Boldt v. State">101 Wis. 2d 566, 584</a></span>, <span class="citation" data-id="2226867"><a href="/opinion/2226867/boldt-v-state/#143" aria-description="Citation for case: Boldt v. State">305 N. W. 2d 133, 143-144</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./454/973/">454 U. S. 973</a></span> (1981).</p>
</footnote>
<footnote label="4">
<p id="b95-7"><em> </em>Petitioner cites a number of cases from this Court that he asserts have “assumed” that a State is a person. Those cases include ones in which a State has been sued by name under § 1983, see, <em>e. g., Maine </em>v. <em>Thiboutot, </em><span class="citation" data-id="9428027"><a href="/opinion/110322/maine-v-thiboutot/" aria-description="Citation for case: Maine v. Thiboutot">448 U. S. 1</a></span> (1980); <em>Martinez </em>v. <em>California, </em><span class="citation" data-id="110169"><a href="/opinion/110169/martinez-v-california/" aria-description="Citation for case: Martinez v. California">444 U. S. 277</a></span> (1980), various eases awarding attorney’s fees against a State or a state agency, <em>Maine </em>v. <em><span class="citation" data-id="9428027"><a href="/opinion/110322/maine-v-thiboutot/" aria-description="Citation for case: Maine v. Thiboutot">Thiboutot, supra;</a></span> Hutto </em>v. <em>Finney, </em><span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">437 U. S. 678</a></span> (1978), and various cases discussing the waiver of Eleventh Amendment immunity by States, see, <em>e. g., Kentucky </em>v. <em>Graham, </em><span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/#167" aria-description="Citation for case: Kentucky v. Graham">473 U. S. 159, 167, n. 14</a></span> (1985); <em>Edelman </em>v. <em>Jordan, </em><span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651</a></span> (1974). But the Court did not address the meaning of person in any of those cases, and in none of the eases was resolution of that issue necessary to the decision. Petitioner’s argument evidently rests on the proposition that whether a State is a person under § 1983 is “jurisdictional” and “thus could have been raised by the Court on its own motion” in those cases. Brief for Petitioner 25, n. 15. Even assuming that petitioner’s premise and characterization of the cases is correct, “this Court has never considered itself bound [by prior <em>sub silentio </em>holdings] when a subsequent case finally brings the jurisdictional issue before us.” <em>Hagans </em>v. <em>Lavine, </em><span class="citation" data-id="9425636"><a href="/opinion/108987/hagans-v-lavine/#535" aria-description="Citation for case: Hagans v. Lavine">415 U. S. 528, 535, n. 5</a></span> (1974).</p>
</footnote>
<footnote label="5">
<p id="b96-7"><em> Jefferson County Pharmaceutical Assn. </em>v. <em>Abbott Laboratories, </em><span class="citation multiple-matches"><a href="/c/U.%20S./460/160/">460 U. S. 160</a></span> (1983), on which petitioner relies, is fully reconcilable with our holding in the present case. In <em>Jefferson County, </em>the Court held that States were persons that could be sued under the Robinson-Patman Act, <span class="citation no-link">15 U. S. C. §§ 13</span>(a) and 13(f). 460 U. S., at 155-157. But the plaintiff there was seeking only injunctive relief and not damages against the State <page-number citation-index="1" label="65">*65</page-number>defendant, the Board of Trustees of the University of Alabama; the District Court had dismissed the plaintiff’s damages claim as barred by the Eleventh Amendment. <em>Id., </em>at 153, n. 5. Had the present § 1983 action been brought in federal court, a similar disposition would have resulted. Of course, the Court would never be faced with a case such as <em>Jefferson County </em>that had been brought in a state court because the federal courts have exclusive jurisdiction over claims under the federal antitrust laws. <span class="citation no-link">15 U. S. C. §§ 15</span> and 26. Moreover, the Court in <em>Jefferson County </em>was careful to limit its holding to “state purchases for the purpose of competing against private enterprise ... in the retail market.” 460 U. S., at 154. It assumed without deciding “that Congress did not intend the Act to apply to state purchases for consumption in traditional governmental functions,” <em>ibid., </em>which presents a more difficult question because it may well “affec[t] the federal balance.” See <em>United States </em>v. <em>Bass, </em><span class="citation" data-id="9424710"><a href="/opinion/108421/united-states-v-bass/#349" aria-description="Citation for case: United States v. Bass">404 U. S. 336, 349</a></span> (1971).</p>
</footnote>
<footnote label="6">
<p id="b99-6">. Petitioner argues that Congress would not have considered the Eleventh Amendment in enacting § 1983 because in 1871 this Court had not yet held that the Eleventh Amendment barred federal-question cases against States in federal court. This argument is no more than an attempt to have this Court reconsider <em>Quern </em>v. <em>Jordan, </em><span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/" aria-description="Citation for case: Quern v. Jordan">440 U. S. 332</a></span> (1979), which we decline to do.</p>
</footnote>
<footnote label="7">
<p id="b99-12"> Our recognition in <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), that a municipality is a person under § 1983, is fully consistent with this reasoning. In <em>Owen </em>v. <em>City of Independence, </em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622</a></span> (1980), we noted that by the time of the enactment of § 1983, municipalities no longer retained the sovereign immunity they had previously shared with the States. “[B]y the end of the 19th century, courts <page-number citation-index="1" label="68">*68</page-number>regularly held that in imposing a specific duty on the municipality either in its charter or by statute, the State had impliedly withdrawn the city’s immunity from liability for the nonperformance or misperformance of its obligation,” <em>id., </em>at 646, and, as a result, municipalities had been held liable for damages “in a multitude of cases” involving previously immune activities, id., at 646-647.</p>
</footnote>
<footnote label="8">
<p id="b101-6">. The Dictionary Act provided that</p>
<blockquote id="b101-7">“in all acts hereafter passed . . . the word ‘person’ may extend and be applied to bodies politic and corporate . . . unless the context shows that such words were intended to be used in a more limited sense.” Act of Feb. 25, 1871, §2, <span class="citation no-link">16 Stat. 431</span>.</blockquote>
</footnote>
<footnote label="9">
<p id="b101-11"> See <em>United States </em>v. <em>Fox, </em><span class="citation" data-id="89471"><a href="/opinion/89471/united-states-v-fox/#321" aria-description="Citation for case: United States v. Fox">94 U. S. 315, 321</a></span> (1877); 1 B. Abbott, Dictionary of Terms and Phrases Used in American or English Jurisprudence 155 (1879) (“most exact expression” for “public corporation”); W. Anderson, A Dictionary of Law 127 (1893) (“most exact expression for a public corporation or corporation having powers of government”); Black’s Law Dictionary 143 (1891) (“body politic” is “term applied to a corporation, which is usually designated as a ‘body corporate and politic’ ” and “is particularly appropriate to a <em>public </em>corporation invested with powers and duties of government”); 1 A. Burrill, A Law Dictionary and Glossary 212 (2d ed. 1871) (“body politic” is “term applied to a corporation, which is usually designated as a <em>body corporate and politic”). </em>A public corporation, in ordinary usage, was another term for a municipal corporation, and included towns, cities, and counties, but not States. See 2 Abbott, <em>supra, </em><page-number citation-index="1" label="70">*70</page-number>at 347; Anderson, <em>supra, </em>at 264-265; Black, <em>supra, </em>at 278; 2 Burrill, <em>supra, </em>at 352.</p>
<p id="b102-8">Justice BRENNAN appears to confuse this precise definition of the phrase with its use “in a rather loose way,” see Black, <em>supra, </em>at 143, to refer to <em>the </em>state (as opposed to <em>a </em>State). This confusion is revealed most clearly in Justice Brennan’s reliance on the 1979 edition of Black’s Law Dictionary, which defines “body politic or corporate” as “[a] social compact by which the whole people covenants with each citizen, and each citizen with the whole people, that all shall be governed by certain laws for the common good.” <em>Post, </em>at 79. To the extent Justice Brennan’s citation of other authorities does not suffer from the same confusion, those authorities at best suggest that the phrase is ambiguous, which still renders the Dictionary Act incapable of supplying the necessary clear intent.</p>
</footnote>
<footnote label="10">
<p id="b103-9"> Of course a state official in his or her official capacity, when sued for injunctive relief, would be a person under § 1983 because “official-capacity actions for prospective relief are not treated as actions against the State.” <em>Kentucky </em>v. <em>Graham, </em><span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/#167" aria-description="Citation for case: Kentucky v. Graham">473 U. S., at 167, n. 14</a></span>; <em>Ex parte Young, </em><span class="citation" data-id="9418117"><a href="/opinion/96819/ex-parte-young/#159" aria-description="Citation for case: Ex Parte Young">209 U. S. 123, 159-160</a></span> (1908). This distinction is “commonplace in sovereign immunity doctrine,” L. Tribe, American Constitutional Law § 3-27, p. 190, n. 3 (2d ed. 1988), and would not have been foreign to the 19th-century Congress that enacted § 1983, see, <em>e. g., In re Ayers, </em><span class="citation" data-id="9417465"><a href="/opinion/92059/in-re-ayers/#506" aria-description="Citation for case: In Re Ayers">123 U. S. 443, 506-507</a></span> (1887); <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="90667"><a href="/opinion/90667/united-states-v-lee/#219" aria-description="Citation for case: United States v. Lee">106 U. S. 196, 219-222</a></span> (1882); <em>Board of Liquidation </em>v. <em>McComb, </em><span class="citation" data-id="89308"><a href="/opinion/89308/board-of-liquidation-v-mccomb/#541" aria-description="Citation for case: Board of Liquidation v. McComb">92 U. S. 531, 541</a></span> (1876); <em>Osborn </em>v. <em>Bank of United States, </em><span class="citation" data-id="85451"><a href="/opinion/85451/osborn-v-bank-of-united-states/" aria-description="Citation for case: Osborn v. Bank of United States">9 Wheat. 738</a></span> (1824). <em>City of Kenosha </em>v. <em>Bruno, </em><span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/#513" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507, 513</a></span> (1973), on which Justice Stevens relies, see <em>post, </em>at 93, n. 8, is not to the contrary. That case involved municipal liability under § 1983, and the fact that nothing in § 1983 suggests its “bifurcated application to municipal corporations depending on the nature of the relief sought against them,” <span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/#513" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S., at 513</a></span>, is not surprising, since by the time of the enactment of § 1983 municipalities were no longer protected by sovereign immunity. <em>Supra, </em>at 67-68, n. 7.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Wilson v. Arkansas.md  (`case`, 5 assertions)

### content_page

```
---
title: "Wilson v. Arkansas"
type: case
citation: "514 U.S. 927 (1995)"
parallel_cite: "115 S. Ct. 1914; 131 L. Ed. 2d 976"
neutral_cite: 1995 U.S. LEXIS 3464
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1995
date_decided: 1995-05-22
docket: 94-5707
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1995-05-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wilson v. Arkansas
  varies_by_point: false
  scope_note: "Knock-and-announce as part of reasonableness; refined by Richards v. Wisconsin (1997). Hudson v. Michigan (2006) held a violation does not trigger suppression. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117936/wilson-v-arkansas/"
  cluster_id: 117936
  opinion_id: 117936
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Key — Anchor"
related: ["[[Richards v. Wisconsin]]", "[[Hudson v. Michigan]]"]
aliases: ["Wilson"]
tags: ["case", "fourth-amendment", "knock-and-announce", "warrant-execution", "reasonableness"]
holding: "The common-law **knock-and-announce** principle — that officers must announce their presence and authority before forcibly entering a…"
lake:
  record_id: Wilson v. Arkansas
  status: verified
  projected_at: 2026-07-06
---

# Wilson v. Arkansas

*514 U.S. 927 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Sharlene Wilson sold narcotics to a police informant; at one buy she waved a semiautomatic pistol in the informant's face and threatened to kill her. Police obtained warrants to search Wilson's home and to arrest her and her cohabitant Jacobs (who had a record of arson and firebombing). Executing the search warrant, officers found the main door open, opened an unlocked screen door, and entered while identifying themselves as police and announcing the warrant. They seized drugs, paraphernalia, a gun, and ammunition. Wilson moved to suppress, arguing the officers had failed to knock and announce before entering; the Arkansas Supreme Court held the Fourth Amendment imposes no such requirement.

## Issue
Whether the common-law "knock and announce" principle — that officers ordinarily must announce their presence and authority before entering a dwelling — forms part of the Fourth Amendment reasonableness inquiry.

## Rule
Yes. "[W]e hold that this common-law 'knock and announce' principle forms a part of the reasonableness inquiry under the Fourth Amendment." — 514 U.S. at 929. ^pin-929

Accordingly, "in some circumstances an officer's unannounced entry into a home might be unreasonable under the Fourth Amendment." — *Id.* at 934. ^pin-934

The requirement is flexible, not absolute: "This is not to say, of course, that every entry must be preceded by an announcement. The Fourth Amendment's flexible requirement of reasonableness should not be read to mandate a rigid rule of announcement that ignores countervailing law enforcement interests." — *Id.* ^pin-934a

Threats of violence, risk of escape, or likely destruction of evidence may make an unannounced entry reasonable.

## Application
On these facts the Court announced that [[Knock-and-Announce|knock-and-announce]] is part of the reasonableness inquiry but did not itself decide whether the officers' entry was reasonable; it reversed and [[Reading and Citing Cases#on-remand|remanded]] because the state courts had wrongly held the principle irrelevant and so never weighed the countervailing circumstances. The Court flagged the facts the lower courts should consider — that Wilson had brandished a pistol and threatened to kill the informant, and that her cohabitant had a record of arson and firebombing — as potentially supporting law-enforcement interests in an unannounced entry.

## Conclusion
The [[Knock-and-Announce|knock-and-announce]] principle is part of Fourth Amendment reasonableness; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] to determine whether the unannounced entry was reasonable under the circumstances.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Wilson* was refined by [[Richards v. Wisconsin]] (1997), which set the "reasonable suspicion" standard for dispensing with announcement (danger, futility, or destruction of evidence). [[Hudson v. Michigan]] (2006) held that a [[Knock-and-Announce|knock-and-announce]] violation does not by itself trigger the exclusionary rule — limiting the remedy, not the underlying requirement.

## Appears on
- [[Knock-and-Announce]] — *Key — Anchor*

## Sources
- *Wilson v. Arkansas*, 514 U.S. 927 (1995) — https://www.courtlistener.com/opinion/117936/wilson-v-arkansas/ — pinpoints: 929, 934.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d91f50e922b752c3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "514 U.S. 927 (1995)", "court": "U.S. Supreme Court", "neutral_cite": "1995 U.S. LEXIS 3464", "official_citation_present": true, "parallel_cite": "115 S. Ct. 1914; 131 L. Ed. 2d 976", "title": "Wilson v. Arkansas", "year": "1995"}}
{"assertion_id": "5989d153c9a19d4d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The common-law **knock-and-announce** principle — that officers must announce their presence and authority before forcibly entering a…", "title": "Wilson v. Arkansas"}}
{"assertion_id": "f465320ae6eadc6a", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock-and-Announce"}, "payload": {"home": "Knock-and-Announce", "role": "Key — Anchor", "title": "Wilson v. Arkansas"}}
{"assertion_id": "ba36dc148537e03c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Wilson v. Arkansas"}}
{"assertion_id": "f96f3c846eb9a6d5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1995-05-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Wilson v. Arkansas", "field_i_validity": "good_law", "scope_note": "Knock-and-announce as part of reasonableness; refined by Richards v. Wisconsin (1997). Hudson v. Michigan (2006) held a violation does not trigger suppression. Good law.", "title": "Wilson v. Arkansas", "varies_by_point": "false"}}
```

### lake record — Wilson v. Arkansas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wilson v. Arkansas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wilson v. Arkansas",
    "case_name_short": "Wilson",
    "case_name_full": "Wilson v. Arkansas",
    "input_case_name": "Wilson v. Arkansas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1995-05-22",
    "year": 1995,
    "docket": "94-5707",
    "cluster_id": 117936,
    "lead_opinion_id": 117936,
    "sibling_ids": [
      117936
    ],
    "absolute_url": "/opinion/117936/wilson-v-arkansas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "514 U.S. 927",
      "volume": "514",
      "reporter": "U.S.",
      "page": "927",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "115 S. Ct. 1914",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "1914",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 L. Ed. 2d 976",
        "volume": "131",
        "reporter": "L. Ed. 2d",
        "page": "976",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1995 U.S. LEXIS 3464",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "3464",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "514 U.S. 927",
        "volume": "514",
        "reporter": "U.S.",
        "page": "927",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 S. Ct. 1914",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "1914",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 L. Ed. 2d 976",
        "volume": "131",
        "reporter": "L. Ed. 2d",
        "page": "976",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. LEXIS 3464",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "3464",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "514 U.S. 927",
    "official_selection": {
      "court_class": "scotus",
      "selected": "514 U.S. 927",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-929",
      "page": null,
      "quote": "principle \u2014 that officers ordinarily must announce their presence and authority before entering a dwelling \u2014 forms part of the Fourth Amendment reasonableness inquiry. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-934",
      "page": null,
      "quote": "in some circumstances an officer's unannounced entry into a home might be unreasonable under the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-934a",
      "page": null,
      "quote": "This is not to say, of course, that every entry must be preceded by an announcement. The Fourth Amendment's flexible requirement of reasonableness should not be read to mandate a rigid rule of announcement that ignores countervailing law enforcement interests.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1995-05-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wilson v. Arkansas",
    "varies_by_point": false,
    "scope_note": "Knock-and-announce as part of reasonableness; refined by Richards v. Wisconsin (1997). Hudson v. Michigan (2006) held a violation does not trigger suppression. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "James Sunny Burton v. State",
          "cluster_id": 3092638,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dennis Russell Callaghan",
          "cluster_id": 2933574,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Singleton",
          "cluster_id": 793669,
          "cite": [
            "441 F.3d 290",
            "2006 U.S. App. LEXIS 7201",
            "2006 WL 724800"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard J. Rizzi",
          "cluster_id": 792946,
          "cite": [
            "434 F.3d 669",
            "2006 U.S. App. LEXIS 450",
            "2006 WL 39266"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1790339,
          "cite": [
            "177 S.W.3d 8"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre J. Scroggins",
          "cluster_id": 785508,
          "cite": [
            "361 F.3d 1075",
            "2004 WL 574495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. David Lynn Hatfield",
          "cluster_id": 785869,
          "cite": [
            "365 F.3d 332",
            "2004 U.S. App. LEXIS 8123",
            "2004 WL 869674"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane1_negative"
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
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
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
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
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
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
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
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyoming v. Houghton",
          "cluster_id": 118277,
          "cite": [
            "143 L. Ed. 2d 408",
            "119 S. Ct. 1297",
            "526 U.S. 295",
            "1999 U.S. LEXIS 2347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richards v. Wisconsin",
          "cluster_id": 118103,
          "cite": [
            "137 L. Ed. 2d 615",
            "117 S. Ct. 1416",
            "520 U.S. 385",
            "1997 U.S. LEXIS 2794"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 1539942,
          "cite": [
            "974 A.2d 1057",
            "200 N.J. 1",
            "2009 N.J. LEXIS 804"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Henning",
          "cluster_id": 1060855,
          "cite": [
            "975 S.W.2d 290",
            "1998 Tenn. LEXIS 370",
            "1998 WL 324318"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Majors",
          "cluster_id": 1057596,
          "cite": [
            "318 S.W.3d 850",
            "2010 WL 11507501",
            "2010 Tenn. LEXIS 722"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Fred Snow, Marcus Snow, Rahad Ross",
          "cluster_id": 795598,
          "cite": [
            "462 F.3d 55",
            "2006 U.S. App. LEXIS 22613"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gomez",
          "cluster_id": 2613548,
          "cite": [
            "932 P.2d 1",
            "122 N.M. 777",
            "1997 NMSC 006"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramirez",
          "cluster_id": 118180,
          "cite": [
            "140 L. Ed. 2d 191",
            "118 S. Ct. 992",
            "523 U.S. 65",
            "1998 U.S. LEXIS 1600"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 4867542,
          "cite": [
            "592 U.S. 306",
            "141 S. Ct. 989",
            "209 L. Ed. 2d 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland Ex Rel. Overdorff v. Harrington",
          "cluster_id": 161659,
          "cite": [
            "268 F.3d 1179",
            "2001 U.S. App. LEXIS 22593",
            "2001 WL 1251670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert Woods v. City of Chicago, Officer Makowski, Chicago Police Officer 16971, Officer Alanis, Chicago Police Officer 5001",
          "cluster_id": 771403,
          "cite": [
            "234 F.3d 979",
            "55 Fed. R. Serv. 912",
            "2000 U.S. App. LEXIS 31315",
            "2000 WL 1801038"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Banks",
          "cluster_id": 131146,
          "cite": [
            "157 L. Ed. 2d 343",
            "124 S. Ct. 521",
            "540 U.S. 31",
            "2003 U.S. LEXIS 8966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
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
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
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
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of West Covina v. Perkins",
          "cluster_id": 118255,
          "cite": [
            "142 L. Ed. 2d 636",
            "119 S. Ct. 678",
            "525 U.S. 234",
            "1999 U.S. LEXIS 507"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Eason",
          "cluster_id": 1863783,
          "cite": [
            "2001 WI 98",
            "629 N.W.2d 625",
            "245 Wis. 2d 206",
            "2001 Wisc. LEXIS 443"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
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
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michalik v. Hermann",
          "cluster_id": 39242,
          "cite": [
            "422 F.3d 252",
            "2005 WL 1971273"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Fields Christopher Crawley",
          "cluster_id": 740479,
          "cite": [
            "113 F.3d 313",
            "1997 U.S. App. LEXIS 10728"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roger Trent v. Steven Wade",
          "cluster_id": 2774855,
          "cite": [
            "776 F.3d 368",
            "2015 WL 394096"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Arkansas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117936) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDYwODE5MjAwMDAwJnM9Mjg2NjU2OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117936%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(117936)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTYmcz0xOTc3NzImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28117936%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117936)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117936)",
    "indexed_citing_opinions": 592,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117936,
        "count": 592,
        "count_source": "search"
      }
    ],
    "citation_count": 925,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wilson-v-arkansas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjczMDYxNjcmcz00ODk0NDA3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28117936%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117936,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 1428666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 2148687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 2220027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 2225575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 2410364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117936,
        "cited_id": 5514070,
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
    "date_created": "2026-07-06T04:24:50Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:25:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:25:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:29:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:25:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wilson v. Arkansas

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1003-4">
<span citation-index="1" class="star-pagination" label="929"> 
   *929
   </span>
  Justice Thomas
 </author>
<p id="AJqY">
  delivered the opinion of the Court.
 </p>
<p id="b1003-5">
  At the time of the framing, the common law of search and seizure recognized a law enforcement officer’s authority to break open the doors of a dwelling, but generally indicated that he first ought to announce his presence and authority. In this case, we hold that this common-law “knock and announce” principle forms a part of the reasonableness inquiry under the Fourth Amendment.
 </p>
<p id="b1003-6">
  I
 </p>
<p id="b1003-7">
  During November and December 1992, petitioner Sharlene Wilson made a series of narcotics sales to an informant acting at the direction of the Arkansas State Police. In late November, the informant purchased marijuana and methamphetamine at the home that petitioner shared with Bryson Jacobs. On December 30, the informant telephoned petitioner at her home and arranged to meet her at a local store to buy some marijuana. According to testimony presented below, petitioner produced a semiautomatic pistol at this meeting and waved it in the informant’s face, threatening to kill her if she turned out to be working for the police. Petitioner then sold the informant a bag of marijuana.
 </p>
<p id="b1003-8">
  The next day, police officers applied for and obtained warrants to search petitioner’s home and to arrest both petitioner and Jacobs. Affidavits filed in support of the warrants set forth the details of the narcotics transactions and stated that Jacobs had previously been convicted of arson and firebombing. The search was conducted later that afternoon. Police officers found the main door to petitioner’s home open. While opening an unlocked screen door and entering the residence, they identified themselves as police officers and stated that they had a warrant. Once inside the home, the officers seized marijuana, methamphetamine, valium, narcotics paraphernalia, a gun, and ammunition. They also found petitioner in the bathroom, flushing marijuana down the toilet. Petitioner and Jacobs were arrested and
  <span citation-index="1" class="star-pagination" label="930"> 
   *930
   </span>
  charged with delivery of marijuana, delivery of methamphetamine, possession of drug paraphernalia, and possession of marijuana.
 </p>
<p id="b1004-5">
  Before trial, petitioner filed a motion to suppress the evidence seized during the search. Petitioner asserted that the search was invalid on various grounds, including that the officers had failed to “knock and announce” before entering her home. The trial court summarily denied the suppression motion. After a jury trial, petitioner was convicted of all charges and sentenced to 32 years in prison.
 </p>
<p id="b1004-6">
  The Arkansas Supreme Court affirmed petitioner’s conviction on appeal. <span class="citation" data-id="2410364"><a href="/opinion/2410364/wilson-v-state/" aria-description="Citation for case: Wilson v. State">317 Ark. 548</a></span>, <span class="citation" data-id="2410364"><a href="/opinion/2410364/wilson-v-state/" aria-description="Citation for case: Wilson v. State">878 S. W. 2d 755</a></span> (1994). The court noted that “the officers entered the home
  <em>
   while they were identifying
  </em>
  themselves,” but it rejected petitioner’s argument that “the Fourth Amendment requires officers to knock and announce prior to entering the residence.”
  <span class="citation" data-id="2410364"><a href="/opinion/2410364/wilson-v-state/#553" aria-description="Citation for case: Wilson v. State"><em>
   Id.,
  </em>
  at 553</a></span>, <span class="citation" data-id="2410364"><a href="/opinion/2410364/wilson-v-state/#758" aria-description="Citation for case: Wilson v. State">878 S. W. 2d, at 758</a></span> (emphasis added). Finding “no authority for [petitioner’s] theory that the knock and announce principle is required by the Fourth Amendment,” the court concluded that neither Arkansas law nor the Fourth Amendment required suppression of the evidence.
  <em>
   <span class="citation" data-id="2410364"><a href="/opinion/2410364/wilson-v-state/" aria-description="Citation for case: Wilson v. State">Ibid.</a></span>
  </em>
</p>
<p id="b1004-7">
  We granted certiorari to resolve the conflict among the lower courts as to whether the common-law knock and announce principle forms a part of the Fourth Amendment reasonableness inquiry.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  <span class="citation multiple-matches"><a href="/c/U.%20S./513/1014/">513 U. S. 1014</a></span> (1995). We hold that it does, and accordingly reverse and remand.
 </p>
<p id="AX6v">
<span citation-index="1" class="star-pagination" label="931"> 
   *931
   </span>
  II
 </p>
<p id="b1005-4">
  The Fourth Amendment to the Constitution protects “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” In evaluating the scope of this right, we have looked to the traditional protections against unreasonable searches and seizures afforded by the common law at the time of the framing. See
  <em>
   California
  </em>
  v.
  <em>
   Hodari D.,
  </em>
  <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#624" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621, 624</a></span> (1991);
  <em>
   United States
  </em>
  v.
  <em>
   Watson,
  </em>
  <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 418-420</a></span> (1976);
  <em>
   Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span> (1925). “Although the underlying command of the Fourth Amendment is always that searches and seizures be reasonable,”
  <em>
   New Jersey
  </em>
  v.
  <em>
   T. L.
  </em>
  Q, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 337</a></span> (1985), our effort to give content to this term may be guided by the meaning ascribed to it by the Framers of the Amendment. An examination of the common law of search and seizure leaves no doubt that the reasonableness of a search of a dwelling may depend in part on whether law enforcement officers announced their presence and authority prior to entering.
 </p>
<p id="b1005-5">
  Although the common law generally protected a man’s house as-“his castle of defence and asylum,” 3 W. Blackstone, Commentaries *288 (hereinafter Blackstone), common-law courts long have held that “when the King is party, the sheriff (if the doors be not open) may break the party’s house, either to arrest him, or to do other execution of the K[ing]’s process, if otherwise he cannot enter.”
  <em>
   Semayne’s Case,
  </em>
  5 Co. Rep. 91a, 91b, 77 Eng. Rep. 194, 195 (K. B. 1603). To this rule, however, common-law courts appended an important qualification:
 </p>
<blockquote id="b1005-6">
  “But before he breaks it, he ought to signify the cause of his coming, and to make request to open doors . . . , for the law without a default in the owner abhors the destruction or breaking of any house (which is for the habitation and safety of man) by which great damage and inconvenience might ensue to the party, when no
  <span citation-index="1" class="star-pagination" label="932"> 
   *932
   </span>
  default is in him; for perhaps he did not know of the process, of which, if he had notice, it is to be presumed that he would obey it . . .
  <em>
   Ibid.,
  </em>
  77 Eng. Rep., at 195-196.
 </blockquote>
<p id="b1006-5">
  See also
  <em>
   Case of Richard Curtis,
  </em>
  Fost. 135, 137, 168 Eng. Rep. 67, 68 (Crown 1757) (“[N]o precise form of words is required in a case of this kind. It is sufficient that the party hath notice, that the officer cometh not as a mere trespasser, but claiming to act under a proper authority . . .”);
  <em>
   Lee
  </em>
  v.
  <em>
   Gansell,
  </em>
  Lofft 374, 381-382, 98 Eng. Rep. 700, 705 (K. B. 1774) (“[A]s to the outer door, the law is now clearly taken” that it is privileged; but the door may be broken “when the due notification and demand has been made and refused”).
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b1006-6">
  Several prominent founding-era commentators agreed on this basic principle. According to Sir Matthew Hale, the “constant practice” at common law was that “the officer may break open the door, if he be sure the offender is there, if after acquainting them of the business, and demanding the prisoner, he refuses to open the door.” See 1 M. Hale, Pleas of the Crown *582. William Hawkins propounded a similar principle: “the law doth never allow” an officer to break open the door of a dwelling “but in cases of necessity,” that is, unless he “first signify to those in the house the cause of his coming, and request them to give him admittance.” 2 W. Hawkins, Pleas of the Crown, ch. 14, § 1, p. 138 (6th ed. 1787).
  <span citation-index="1" class="star-pagination" label="933"> 
   *933
   </span>
  Sir William Blackstone stated simply that the sheriff may “justify breaking open doors, if the possession be not quietly delivered.” 3 Blackstone *412.
 </p>
<p id="b1007-5">
  The common-law knock and announce principle was woven quickly into the fabric of early American law. Most of the States that ratified the Fourth Amendment had enacted constitutional provisions or statutes generally incorporating English common law, see,
  <em>
   e. g.,
  </em>
  N. J. Const. of 1776, §22, in 5 Federal and State Constitutions 2598 (F. Thorpe ed. 1909) (“[T]he common law of England... shall still remain in force, until [it] shall be altered by a future law of the Legislature”); N. Y. Const. of 1777, Art. 35, in
  <em>
   id.,
  </em>
  at 2635 (“[S]uch parts of the common law of England ... as ... did form the law of [New York on April 19, 1775] shall be and continue the law of this State, subject to such alterations and provisions as the legislature of this State shall, from time to time, make concerning the same”); Ordinances of May 1776, ch. 5, § 6, in 9 Statutes at Large of Virginia 127 (W. Hening ed. 1821) (“[T]he common law of England ... shall be the rule of decision, and shall be considered as in full force, until the same shall be altered by the legislative power of this colony”), and a few States had enacted statutes specifically embracing the common-law view that the breaking of the door of a dwelling was permitted once admittance was refused, see,
  <em>
   e. g.,
  </em>
  Act of Nov. 8, 1782, ch. 15, ¶ 6, in Acts and Laws of Massachusetts 193 (1782); Act of Apr. 13, 1782, ch. 39, §3, in 1 Laws of the State of New York 480 (1886); Act of June 24, 1782, ch. 317, § 18, in Acts of the General Assembly of New-Jersey (1784) (reprinted in The First Laws of the State of <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#293" aria-description="Citation for case: New Jersey v. T. L. O.">New Jersey 293-294</a></span> (J. Cushing comp. 1981)); Act of Dec. 23, 1780, ch. 925, § 5, in 10 Statutes at Large of Pennsylvania 255 (J. Mitchell &amp; H. Flanders comp. 1904). Early American courts similarly embraced the common-law knock and announce principle. See,
  <em>
   e. g., Walker
  </em>
  v.
  <em>
   Fox,
  </em>
  <span class="citation" data-id="7379976"><a href="/opinion/7459035/walker-v-fox/#405" aria-description="Citation for case: Walker v. Fox">32 Ky. 404, 405</a></span> (1834);
  <em>
   Burton
  </em>
  v.
  <em>
   Wilkinson,
  </em>
  <span class="citation" data-id="6573334"><a href="/opinion/6693443/burton-v-wilkinson/#189" aria-description="Citation for case: Burton v. Wilkinson">18 Vt. 186, 189</a></span> (1846);
  <em>
   Howe
  </em>
  v.
  <em>
   Butterfield,
  </em>
  <span class="citation" data-id="6409284"><a href="/opinion/6535565/howe-v-butterfield/#305" aria-description="Citation for case: Howe v. Butterfield">58 Mass. 302, 305</a></span> (1849). See generally Blakey, The
  <span citation-index="1" class="star-pagination" label="934"> 
   *934
   </span>
  Rule of Announcement and Unlawful Entry, <span class="citation no-link">112 U. Pa. L. Rev. 499</span>, 504-508 (1964) (collecting cases).
 </p>
<p id="b1008-5">
  Our own cases have acknowledged that the common-law principle of announcement is “embedded in Anglo-American law,”
  <em>
   Miller
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#313" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 313</a></span> (1958), but we have never squarely held that this principle is an element of the reasonableness inquiry under the Fourth Amendment.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  We now so hold. Given the longstanding common-law endorsement of the practice of announcement, we have little doubt that the Framers of the Fourth Amendment thought that the method of an officer’s entry into a dwelling was among the factors to be considered in assessing the reasonableness of a search or seizure. Contrary to the decision below, we hold that in some circumstances an officer’s unannounced entry into a home might be unreasonable under the Fourth Amendment.
 </p>
<p id="b1008-6">
  This is not to say, of course, that every entry must be preceded by an announcement. The Fourth Amendment’s flexible requirement of reasonableness should not be read to mandate a rigid rule of announcement that ignores countervailing law enforcement interests. As even petitioner concedes, the common-law principle of announcement was never stated as an inflexible rule requiring announcement under all circumstances. See
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#38" aria-description="Citation for case: Ker v. California">374 U. S. 23, 38</a></span> (1963) (plurality opinion) (“[I]t has been recognized from the early common law that... breaking is permissible in executing an arrest under certain circumstances”); see also,
  <em>
   e. g.,
  </em>
<span citation-index="1" class="star-pagination" label="935"> 
   *935
   </span>
<em>
   White &amp; Wiltsheire,
  </em>
  2 Rolle 137, 138, 81 Eng. Rep. 709, 710 (K. B. 1619) (upholding the sheriff’s breaking of the door of the plaintiff’s dwelling after the sheriff’s bailiffs had been imprisoned in plaintiff’s dwelling while they attempted an earlier execution of the seizure);
  <em>
   Pugh
  </em>
  v.
  <em>
   Griffith,
  </em>
  7 Ad. &amp; E. 827, 840-841, 112 Eng. Rep. 681, 686 (K. B. 1838) (holding that “the necessity of a demand ... is obviated, because there was nobody on whom a demand could be made” and noting that
  <em>
   White &amp; Wiltsheire
  </em>
  leaves open the possibility that there may be “other occasions where the outer door may be broken” without prior demand).
 </p>
<p id="b1009-5">
  Indeed, at the time of the framing, the common-law admonition that an officer “ought to signify the cause of his coming,”
  <em>
   Semayne’s Case,
  </em>
  5 Co. Rep., at 91b, 77 Eng. Rep., at 195, had not been extended conclusively to the context of felony arrests. See Blakey,
  <em>
   supra,
  </em>
  at 503 (“The full scope of the application of the rule in criminal cases . . . was never judicially settled”);
  <em>
   Launock
  </em>
  v.
  <em>
   Brown,
  </em>
  2 B. &amp; Ald. 592, 593, 106 Eng. Rep. 482, 483 (K. B. 1819) (“It is not at present necessary for us to decide how far, in the case of a person charged with felony, it would be necessary , to make a previous demand of admittance before you could justify breaking open the outer door of his house”); W. Murfree, Law of Sheriffs and Other Ministerial Officers § 1163, p. 631 (1st ed. 1884) (“[Although there has been some doubt on the question, the better opinion seems to be that, in cases of felony, no demand of admittance is necessary, especially as, in many cases, the delay incident to it would enable the prisoner to escape”). The common-law principle gradually was applied to cases involving felonies, but at the same time the courts continued to recognize that under certain circumstances the presumption in favor of announcement necessarily would give way to contrary considerations.
 </p>
<p id="b1009-6">
  Thus, because the common-law rule was justified in part by the belief that announcement generally would avoid “the destruction or breaking of any house ... by which great
  <span citation-index="1" class="star-pagination" label="936"> 
   *936
   </span>
  damage and inconvenience might ensue,”
  <em>
   Semayne’s Case, supra,
  </em>
  at 91b, 77 Eng. Rep., at 196, courts acknowledged that the presumption in favor of announcement would yield under circumstances presenting a threat of physical violence. See,
  <em>
   e. g., Read
  </em>
  v.
  <span class="citation" data-id="6573620"><a href="/opinion/6693710/read-v-case/#170" aria-description="Citation for case: Read v. Case"><em>
   Case, 4
  </em>
  Conn. 166, 170</a></span> (1822) (plaintiff who “had resolved ... to resist even to the shedding of blood .. . was not within the reason and spirit of the rule requiring notice”);
  <em>
   Mahomed
  </em>
  v.
  <em>
   The Queen, 4
  </em>
  Moore 289, 247, 13 Eng. Rep. 293, 296 (P. C. 1843) (“While he was firing pistols at them, were they to knock at the door, and to ask him to be pleased to open it for them? The law in its wisdom only requires this ceremony to be observed when it possibly may be attended with some advantage, and may render the breaking open of the outer door unnecessary”). Similarly, courts held that an officer may dispense with announcement in cases where a prisoner escapes from him and retreats to his dwelling. See,
  <em>
   e. g., ibid.; Allen
  </em>
  v.
  <em>
   Martin,
  </em>
  <span class="citation" data-id="5514070"><a href="/opinion/5667090/allen-v-martin/#304" aria-description="Citation for case: Allen v. Martin">10 Wend. 300, 304</a></span> (N. Y. Sup. Ct. 1833). Proof of “demand and refusal” was deemed unnecessary in such cases because it would be a “senseless ceremony” to require an officer in pursuit of a recently escaped arrestee to make an announcement prior to breaking the door to retake him.
  <span class="citation" data-id="5514070"><a href="/opinion/5667090/allen-v-martin/#304" aria-description="Citation for case: Allen v. Martin"><em>
   Id.,
  </em>
  at 304</a></span>. Finally, courts have indicated that unannounced entry may be justified where police officers have reason to believe that evidence would likely be destroyed if advance notice were given. See
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#40" aria-description="Citation for case: Ker v. California"><em>
   Ker, supra,
  </em>
  at 40-41</a></span> (plurality opinion);
  <em>
   People
  </em>
  v.
  <em>
   Maddox,
  </em>
  <span class="citation" data-id="9627819"><a href="/opinion/1428666/people-v-maddox/#305" aria-description="Citation for case: People v. Maddox">46 Cal. 2d 301, 305-306</a></span>, <span class="citation" data-id="9627819"><a href="/opinion/1428666/people-v-maddox/#9" aria-description="Citation for case: People v. Maddox">294 P. 2d 6, 9</a></span> (1956).
 </p>
<p id="b1010-4">
  We need not attempt a comprehensive catalog of the relevant countervailing factors here. For now, we leave to the lower courts the task of determining the circumstances under which an unannounced entry is reasonable under the Fourth Amendment. We simply hold that although a search or seizure of a dwelling might be constitutionally defective if police officers enter without prior announcement, law enforcement interests may also establish the reasonableness of an unannounced entry.
 </p>
<p id="Afp">
<span citation-index="1" class="star-pagination" label="937"> 
   *937
   </span>
  III
 </p>
<p id="b1011-4">
  Respondent contends that the judgment below should be affirmed because the unannounced entry in this case was justified for two reasons. First, respondent argues that police officers reasonably believed that a prior announcement would have placed them in peril, given their knowledge that petitioner had threatened a government informant with a semiautomatic weapon and that Mr. Jacobs had previously been convicted of arson and firebombing. Second, respondent suggests that prior announcement would have produced an unreasonable risk that petitioner would destroy easily disposable narcotics evidence.
 </p>
<p id="b1011-5">
  These considerations may well provide the necessary justification for the unannounced entry in this case. Because the Arkansas Supreme Court did not address their sufficiency, however, we remand to allow the state courts to make any necessary findings of fact and to make the determination of reasonableness in the first instance. The judgment of the Arkansas Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b1011-6">
<em>
   It is so ordered.
  </em>
</p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1004-8">
   See,
   <em>
    e.g., People
   </em>
   v.
   <em>
    Gonzalez,
   </em>
   <span class="citation" data-id="2148687"><a href="/opinion/2148687/people-v-gonzalez/#1048" aria-description="Citation for case: People v. Gonzalez">211 Cal. App. 3d 1043, 1048</a></span>, <span class="citation" data-id="2148687"><a href="/opinion/2148687/people-v-gonzalez/#848" aria-description="Citation for case: People v. Gonzalez">259 Cal. Rptr. 846, 848</a></span> (1989) (“Announcement and demand for entry at the time of service of a search warrant [are] part of Fourth Amendment reasonableness”);
   <em>
    People
   </em>
   v.
   <em>
    Saeckao,
   </em>
   <span class="citation" data-id="2220027"><a href="/opinion/2220027/people-v-saechao/#531" aria-description="Citation for case: People v. Saechao">129 Ill. 2d 522, 531</a></span>, <span class="citation" data-id="2220027"><a href="/opinion/2220027/people-v-saechao/#749" aria-description="Citation for case: People v. Saechao">544 N. E. 2d 745, 749</a></span> (1989) (“[T]he presence or absence of such an announcement is an important consideration in determining whether subsequent entry to arrest or search is constitutionally reasonable”) (internal quotation marks omitted);
   <em>
    Commonwealth
   </em>
   v.
   <em>
    Goggin,
   </em>
   <span class="citation" data-id="2225575"><a href="/opinion/2225575/commonwealth-v-goggin/#202" aria-description="Citation for case: Commonwealth v. Goggin">412 Mass. 200, 202</a></span>, <span class="citation" data-id="2225575"><a href="/opinion/2225575/commonwealth-v-goggin/#787" aria-description="Citation for case: Commonwealth v. Goggin">587 N. E. 2d 785, 787</a></span> (1992) (“Our knock and announce rule is one of common law which is not constitutionally compelled”).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b1006-7">
   This “knock and announce” principle appears to predate even
   <em>
    Semayne’s Case,
   </em>
   which is usually cited as the judicial source of the common-law standard.
   <em>
    Semayne’s Case
   </em>
   itself indicates that the doctrine may be traced to a statute enacted in 1275, and that at that time the statute was “but an affirmance of the common law.” 5 Co. Rep., at 91b, 77 Eng. Rep., at 196 (referring to 3 Edw. I, ch. 17, in 1 Statutes at Large from Magna Carta to Hen. 6 (O. Ruffhead ed. 1769) (providing that if any person takes the beasts of another and causes them “to be driven into a Castle or Fortress,” if the sheriff makes “solem[n] deman[d]” for deliverance of the beasts, and if the person “did not cause the Beasts to be delivered incontinent,” the King “shall cause the said Castle or Fortress to be beaten down without Recovery”)).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b1008-7">
   In
   <em>
    <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>,
   </em>
   our discussion focused on the statutory requirement of announcement found in <span class="citation no-link">18 U. S. C. § 3109</span> (1958 ed.), not on the constitutional requirement of reasonableness. See <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#306" aria-description="Citation for case: Miller v. United States">357 U. S., at 306, 308, 313</a></span>. See also
   <em>
    Sabbath
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/#591" aria-description="Citation for case: Sabbath v. United States">391 U. S. 585, 591, n. 8</a></span> (1968) (suggesting that both the “common law” rule of announcement and entry and its “exceptions” were codified in § 3109);
   <em>
    Ker
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#40" aria-description="Citation for case: Ker v. California">374 U. S. 23,40-41</a></span> (1963) (plurality opinion) (reasoning that an unannounced entry was reasonable under the “exigent circumstances” of that case, without addressing the antecedent question whether the lack of announcement might render a search unreasonable under other circumstances).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b1011-7">
   Respondent and its
   <em>
    amici
   </em>
   also ask us to affirm the denial of petitioner’s suppression motion on an alternative ground: that exclusion is not a constitutionally compelled remedy where the unreasonableness of a search stems from the failure of announcement. Analogizing to the “independent source” doctrine applied in
   <em>
    Segura
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#805" aria-description="Citation for case: Segura v. United States">468 U. S. 796, 805, 813-816</a></span> (1984), and the “inevitable discovery” rule adopted in
   <em>
    Nix
   </em>
   v.
   <em>
    Williams,
   </em>
   <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#440" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 440-448</a></span> (1984), respondent and its
   <em>
    amici
   </em>
   argue that any evidence seized after an unreasonable, unannounced entry is causally disconnected from the constitutional violation and that exclusion goes beyond the goal of precluding any benefit to the government flowing from the constitutional violation. Because this remedial issue was not addressed by the court below and is not within the narrow question on which we granted certiorari, we decline to address these arguments.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Wong Sun v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Wong Sun v. United States"
type: case
citation: "371 U.S. 471 (1963)"
parallel_cite: "83 S. Ct. 407; 9 L. Ed. 2d 441"
neutral_cite: 1963 U.S. LEXIS 2431
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1963
date_decided: 1963-01-14
docket: 36
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1963-01-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wong Sun v. United States
  varies_by_point: false
  scope_note: "Foundational fruit-of-the-poisonous-tree / attenuation case; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106515/wong-sun-v-united-states/"
  cluster_id: 106515
  opinion_id: 106515
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Anchor"
related: ["[[Brown v. Illinois]]", "[[Utah v. Strieff]]", "[[Nix v. Williams]]"]
aliases: ["Wong Sun"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "attenuation"]
holding: "'Fruit of the poisonous tree': derivative evidence is suppressed if come at by exploitation of the primary illegality, not merely 'but…"
lake:
  record_id: Wong Sun v. United States
  status: verified
  projected_at: 2026-07-06
---

# Wong Sun v. United States

*371 U.S. 471 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal narcotics agents, acting without probable cause, broke into James Wah Toy's living quarters and arrested him; in his bedroom Toy made statements implicating "Johnny" Yee. Agents went to Yee, who surrendered heroin and implicated Toy and Wong Sun. Both were arrested without probable cause, arraigned, and released on their own recognizance. Several days later, each voluntarily returned and gave an unsigned statement. Toy and Wong Sun moved to suppress the statements and the heroin as fruits of the unlawful police conduct.

## Issue
Whether verbal statements and physical evidence obtained as a consequence of an unlawful arrest must be excluded as "fruit of the poisonous tree," and how to determine when the connection to the illegality is too attenuated to require suppression.

## Rule
Not every consequence of police illegality is suppressed; "but for" causation is not the test. The Court rejected the idea that all evidence is "'fruit of the poisonous tree' simply because it would not have come to light but for the illegal actions of the police." Instead, "the more apt question … is 'whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.'" — 371 U.S. at 487–488. ^pin-488

Where the link between the illegality and the evidence is sufficiently weakened, the taint dissipates: evidence is admissible when "the connection between the arrest and the statement had 'become so attenuated as to dissipate the taint.'" — *Id.* at 491. ^pin-491

## Application
Applying that test to each defendant's evidence, the Court reached different results. Toy's bedroom statements were come at by exploitation of the agents' unlawful entry — they followed immediately on the illegal break-in and were not purged of the primary taint — so they were suppressed; and the heroin Yee surrendered, traced through Toy's tainted statements, was inadmissible against Toy for the same reason. Wong Sun's statement was different: he had been released on his own recognizance after arraignment and returned voluntarily several days later, so the connection between his unlawful arrest and his statement had become so attenuated as to dissipate the taint, and the statement was admissible. (Wong Sun's conviction was nonetheless reversed because of corroboration concerns.)

## Conclusion
Evidence obtained by exploiting an unlawful arrest is suppressed as [[Common Legal Terms#fruit-of-the-poisonous-tree|fruit of the poisonous tree]], but evidence sufficiently attenuated from the illegality is admissible. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Wong Sun* is the foundational fruit-of-the-poisonous-tree case; its [[Fruits and Attenuation|attenuation]] inquiry was given concrete factors in [[Brown v. Illinois]] and applied to an intervening arrest warrant in [[Utah v. Strieff]]. The related independent-source and inevitable-discovery limits appear in [[Nix v. Williams]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor*

## Sources
- *Wong Sun v. United States*, 371 U.S. 471 (1963) — https://www.courtlistener.com/opinion/106515/wong-sun-v-united-states/ — pinpoints: 487–488, 491.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "beb162111d8785e8", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "371 U.S. 471 (1963)", "court": "U.S. Supreme Court", "neutral_cite": "1963 U.S. LEXIS 2431", "official_citation_present": true, "parallel_cite": "83 S. Ct. 407; 9 L. Ed. 2d 441", "title": "Wong Sun v. United States", "year": "1963"}}
{"assertion_id": "5acd2a271a5f510e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "'Fruit of the poisonous tree': derivative evidence is suppressed if come at by exploitation of the primary illegality, not merely 'but…", "title": "Wong Sun v. United States"}}
{"assertion_id": "8ebff6df412320ad", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Anchor", "title": "Wong Sun v. United States"}}
{"assertion_id": "ad40b47f8c286a69", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Wong Sun v. United States"}}
{"assertion_id": "c920751ce6342c90", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1963-01-14", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Wong Sun v. United States", "field_i_validity": "good_law", "scope_note": "Foundational fruit-of-the-poisonous-tree / attenuation case; good law.", "title": "Wong Sun v. United States", "varies_by_point": "false"}}
```

### lake record — Wong Sun v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wong Sun v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wong Sun v. United States",
    "case_name_short": "Wong Sun",
    "case_name_full": "WONG SUN Et Al. v. UNITED STATES",
    "input_case_name": "Wong Sun v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1963-01-14",
    "year": 1963,
    "docket": "36",
    "cluster_id": 106515,
    "lead_opinion_id": 106515,
    "sibling_ids": [
      106515,
      9422515,
      9422516
    ],
    "absolute_url": "/opinion/106515/wong-sun-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "371 U.S. 471",
      "volume": "371",
      "reporter": "U.S.",
      "page": "471",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "83 S. Ct. 407",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "407",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 441",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "441",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1963 U.S. LEXIS 2431",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "2431",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "371 U.S. 471",
        "volume": "371",
        "reporter": "U.S.",
        "page": "471",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 S. Ct. 407",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "407",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 441",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "441",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1963 U.S. LEXIS 2431",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "2431",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "371 U.S. 471",
    "official_selection": {
      "court_class": "scotus",
      "selected": "371 U.S. 471",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-488",
      "page": null,
      "quote": "and how to determine when the connection to the illegality is too attenuated to require suppression. ## Rule Not every consequence of police illegality is suppressed;",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-491",
      "page": null,
      "quote": "the connection between the arrest and the statement had 'become so attenuated as to dissipate the taint.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1963-01-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wong Sun v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational fruit-of-the-poisonous-tree / attenuation case; good law.",
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
        "journal_ref": "Wong Sun v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Serrano (A173250)",
          "cluster_id": 10135658,
          "cite": [
            "324 Or. App. 453",
            "527 P.3d 54"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gumkowski",
          "cluster_id": 4880252,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane1_negative"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wade",
          "cluster_id": 107486,
          "cite": [
            "18 L. Ed. 2d 1149",
            "87 S. Ct. 1926",
            "388 U.S. 218",
            "1967 U.S. LEXIS 1085"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McMann v. Richardson",
          "cluster_id": 108138,
          "cite": [
            "25 L. Ed. 2d 763",
            "90 S. Ct. 1441",
            "397 U.S. 759",
            "1970 U.S. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
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
        "journal_ref": "Wong Sun v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "110OAG40",
          "cluster_id": 10638768,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane3_recency"
      },
      {
        "citing_case": {
          "name": "Maryland Attorney General Opinion 110OAG40",
          "cluster_id": 10848272,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wong Sun v. United States:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106515 OR 9422515 OR 9422516) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjIwMDg2NDAwMDAwJnM9NDg4MDI1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106515+OR+9422515+OR+9422516%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106515 OR 9422515 OR 9422516)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY4JnM9MTExMjE0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106515+OR+9422515+OR+9422516%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106515 OR 9422515 OR 9422516)",
        "reviewed": 147,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 147,
        "triage_read": 4,
        "triage_snippet_classified": 143
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106515 OR 9422515 OR 9422516)",
    "indexed_citing_opinions": 8572,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106515,
        "count": 7826,
        "count_source": "search"
      },
      {
        "opinion_id": 9422515,
        "count": 934,
        "count_source": "search"
      },
      {
        "opinion_id": 9422516,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 12874,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wong-sun-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0ODYzNDQmcz0xMDY1MTU1NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28106515+OR+9422515+OR+9422516%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106515,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 94334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 94447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 94565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 94573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 103663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 233231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 234904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 235392,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 236713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 237954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 242778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 246074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 246966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 248139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 251634,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 253508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1424394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1428666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1478266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1507600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106515,
        "cited_id": 1512100,
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
    "date_created": "2026-07-06T04:43:58Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:44:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:44:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:46:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:44:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wong Sun v. United States

```
<div>
<center><b><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471</a></span> (1963)</b></center>
<center><h1>WONG SUN ET AL.<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 36.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 29 and April 2, 1962.</center>
<center>Restored to calendar for reargument June 4, 1962.</center>
<center>Reargued October 8, 1962.</center>
<center>Decided January 14, 1963.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*472</span> <i>Edward Bennett Williams,</i> acting under appointment by the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./368/973/">368 U. S. 973</a></span>, reargued the cause and filed a supplemental brief for petitioners. <i>Sol A. Abrams</i> also filed a brief for petitioners.</p>
<p><i>J. William Doolittle</i> reargued the cause for the United States. On the brief were <i>Solicitor General Cox, Assistant Attorney General Miller, Beatrice Rosenberg</i> and <i>J. F. Bishop.</i></p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>The petitioners were tried without a jury in the District Court for the Northern District of California under a two-count indictment for violation of the Federal Narcotics <span class="star-pagination">*473</span> Laws, <span class="citation no-link">21 U. S. C. § 174</span>.<sup>[1]</sup> They were acquitted under the first count which charged a conspiracy, but convicted under the second count which charged the substantive offense of fraudulent and knowing transportation and concealment of illegally imported heroin. The Court of Appeals for the Ninth Circuit, one judge dissenting, affirmed the convictions. <span class="citation" data-id="9447810"><a href="/opinion/253508/wong-sun-and-james-wah-toy-v-united-states/" aria-description="Citation for case: Wong Sun and James Wah Toy v. United States">288 F. 2d 366</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./368/817/">368 U. S. 817</a></span>. We heard argument in the 1961 Term and reargument this Term. <span class="citation multiple-matches"><a href="/c/U.%20S./370/908/">370 U. S. 908</a></span>.</p>
<p>About 2 a. m. on the morning of June 4, 1959, federal narcotics agents in San Francisco, after having had one Hom Way under surveillance for six weeks, arrested him and found heroin in his possession. Hom Way, who had not before been an informant, stated after his arrest that he had bought an ounce of heroin the night before from one known to him only as "Blackie Toy," proprietor of a laundry on Leavenworth Street.</p>
<p>About 6 a. m. that morning six or seven federal agents went to a laundry at 1733 Leavenworth Street. The sign <span class="star-pagination">*474</span> above the door of this establishment said "Oye's Laundry." It was operated by the petitioner James Wah Toy. There is, however, nothing in the record which identifies James Wah Toy and "Blackie Toy" as the same person. The other federal officers remained nearby out of sight while Agent Alton Wong, who was of Chinese ancestry, rang the bell. When petitioner Toy appeared and opened the door, Agent Wong told him that he was calling for laundry and dry cleaning. Toy replied that he didn't open until 8 o'clock and told the agent to come back at that time. Toy started to close the door. Agent Wong thereupon took his badge from his pocket and said, "I am a federal narcotics agent." Toy immediately "slammed the door and started running" down the hallway through the laundry to his living quarters at the back where his wife and child were sleeping in a bedroom. Agent Wong and the other federal officers broke open the door and followed Toy down the hallway to the living quarters and into the bedroom. Toy reached into a nightstand drawer. Agent Wong thereupon drew his pistol, pulled Toy's hand out of the drawer, placed him under arrest and handcuffed him. There was nothing in the drawer and a search of the premises uncovered no narcotics.</p>
<p>One of the agents said to Toy ". . . [Hom Way] says he got narcotics from you." Toy responded, "No. I haven't been selling any narcotics at all. However, I do know somebody who has." When asked who that was, Toy said, "I only know him as Johnny. I don't know his last name." However, Toy described a house on Eleventh Avenue where he said Johnny lived; he also described a bedroom in the house where he said "Johnny kept about a piece"<sup>[2]</sup> of heroin and where he and Johnny had smoked some of the drug the night before. The agents <span class="star-pagination">*475</span> left immediately for Eleventh Avenue and located the house. They entered and found one Johnny Yee in the bedroom. After a discussion with the agents, Yee took from a bureau drawer several tubes containing in all just less than one ounce of heroin, and surrendered them. Within the hour Yee and Toy were taken to the Office of the Bureau of Narcotics. Yee there stated that the heroin had been brought to him some four days earlier by petitioner Toy and another Chinese known to him only as "Sea Dog."</p>
<p>Toy was questioned as to the identity of "Sea Dog" and said that "Sea Dog" was Wong Sun. Some agents, including Agent Alton Wong, took Toy to Wong Sun's neighborhood where Toy pointed out a multifamily dwelling where he said Wong Sun lived. Agent Wong rang a downstairs door bell and a buzzer sounded, opening the door. The officer identified himself as a narcotics agent to a woman on the landing and asked "for Mr. Wong." The woman was the wife of petitioner Wong Sun. She said that Wong Sun was "in the back room sleeping." Alton Wong and some six other officers climbed the stairs and entered the apartment. One of the officers went into the back room and brought petitioner Wong Sun from the bedroom in handcuffs. A thorough search of the apartment followed, but no narcotics were discovered.</p>
<p>Petitioner Toy and Johnny Yee were arraigned before a United States Commissioner on June 4 on a complaint charging a violation of <span class="citation no-link">21 U. S. C. § 174</span>. Later that day, each was released on his own recognizance. Petitioner Wong Sun was arraigned on a similar complaint filed the next day and was also released on his own recognizance.<sup>[3]</sup><span class="star-pagination">*476</span> Within a few days, both petitioners and Yee were interrogated at the office of the Narcotics Bureau by Agent William Wong, also of Chinese ancestry.<sup>[4]</sup> The agent advised each of the three of his right to withhold information which might be used against him, and stated to each that he was entitled to the advice of counsel, though it does not appear that any attorney was present during the questioning of any of the three. The officer also explained to each that no promises or offers of immunity or leniency were being or could be made.</p>
<p>The agent interrogated each of the three separately. After each had been interrogated the agent prepared a statement in English from rough notes. The agent read petitioner Toy's statement to him in English and interpreted certain portions of it for him in Chinese. Toy also read the statement in English aloud to the agent, said there were corrections to be made, and made the corrections in his own hand. Toy would not sign the statement, however; in the agent's words "he wanted to know first if the other persons involved in the case had signed theirs." Wong Sun had considerable difficulty understanding the <span class="star-pagination">*477</span> statement in English and the agent restated its substance in Chinese. Wong Sun refused to sign the statement although he admitted the accuracy of its contents.<sup>[5]</sup></p>
<p>Hom Way did not testify at petitioners' trial. The Government offered Johnny Yee as its principal witness but excused him after he invoked the privilege against self-incrimination and flatly repudiated the statement he had given to Agent William Wong. That statement was not offered in evidence nor was any testimony elicited from him identifying either petitioner as the source of the heroin in his possession, or otherwise tending to support the charges against the petitioners.</p>
<p>The statute expressly provides that proof of the accused's possession of the drug will support a conviction under the statute unless the accused satisfactorily explains the possession. The Government's evidence tending to prove the petitioners' possession (the petitioners offered no exculpatory testimony) consisted of four items which the trial court admitted over timely objections that they were inadmissible as "fruits" of unlawful arrests or of attendant searches: (1) the statements made orally by petitioner Toy in his bedroom at the time of his arrest; (2) the heroin surrendered to the agents by Johnny Yee; (3) petitioner Toy's pretrial unsigned statement; and (4) petitioner Wong Sun's similar statement. The dispute below and here has centered around the correctness of the rulings of the trial judge allowing these items in evidence.</p>
<p>The Court of Appeals held that the arrests of both petitioners were illegal because not based on " `probable cause' within the meaning of the Fourth Amendment" nor "reasonable grounds" within the meaning of the Narcotic <span class="star-pagination">*478</span> Control Act of 1956.<sup>[6]</sup> The Court said as to Toy's arrest, "There is no showing in this case that the agent knew Hom Way to be reliable," and, furthermore, found "nothing in the circumstances occurring at Toy's premises that would provide sufficient justification for his arrest without a warrant." <span class="citation" data-id="9447810"><a href="/opinion/253508/wong-sun-and-james-wah-toy-v-united-states/#369" aria-description="Citation for case: Wong Sun and James Wah Toy v. United States">288 F. 2d, at 369, 370</a></span>. As to Wong Sun's arrest, the Court said "there is no showing that Johnnie Yee was a reliable informer." The Court of Appeals nevertheless held that the four items of proof were not the "fruits" of the illegal arrests and that they were therefore properly admitted in evidence.</p>
<p>The Court of Appeals rejected two additional contentions of the petitioners. The first was that there was insufficient evidence to corroborate the petitioners' unsigned admissions of possession of narcotics. The court held that the narcotics in evidence surrendered by Johnny Yee, together with Toy's statements in his bedroom at the time of arrest corroborated petitioners' admissions. The second contention was that the confessions were <span class="star-pagination">*479</span> inadmissible because they were not signed. The Court of Appeals held on this point that the petitioners were not prejudiced, since the agent might properly have testified to the substance of the conversations which produced the statements.</p>
<p>We believe that significant differences between the cases of the two petitioners require separate discussion of each. We shall first consider the case of petitioner Toy.</p>
<p></p>
<h2>I.</h2>
<p>The Court of Appeals found there was neither reasonable grounds nor probable cause for Toy's arrest. Giving due weight to that finding, we think it is amply justified by the facts clearly shown on this record. It is basic that an arrest with or without a warrant must stand upon firmer ground than mere suspicion, see <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#101" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 101</a></span>, though the arresting officer need not have in hand evidence which would suffice to convict. The quantum of information which constitutes probable causeevidence which would "warrant a man of reasonable caution in the belief" that a felony has been committed, <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, 162must be measured by the facts of the particular case. The history of the use, and not infrequent abuse, of the power to arrest cautions that a relaxation of the fundamental requirements of probable cause would "leave law-abiding citizens at the mercy of the officers' whim or caprice."<sup>[7]</sup><i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span>.</p>
<p>Whether or not the requirements of reliability and particularity of the information on which an officer may act are more stringent where an arrest warrant is absent, they surely cannot be less stringent than where an arrest warrant is obtained. Otherwise, a principal incentive now <span class="star-pagination">*480</span> existing for the procurement of arrest warrants would be destroyed.<sup>[8]</sup> The threshold question in this case, therefore, is whether the officers could, on the information which impelled them to act, have procured a warrant for the arrest of Toy. We think that no warrant would have issued on evidence then available.</p>
<p>The narcotics agents had no basis in experience for confidence in the reliability of Hom Way's information; he had never before given information. And yet they acted upon his imprecise suggestion that a person described only as "Blackie Toy," the proprietor of a laundry somewhere on Leavenworth Street, had sold one ounce of heroin. We have held that identification of the suspect by a reliable informant may constitute probable cause for arrest where the information given is sufficiently accurate to lead the officers directly to the suspect. <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. That rule does not, however, fit this case. For aught that the record discloses, Hom Way's accusation merely invited the officers to roam the length of Leavenworth Street (some 30 blocks) in search of one "Blackie Toy's" laundryand whether by chance or other <span class="star-pagination">*481</span> means (the record does not say) they came upon petitioner Toy's laundry, which bore not his name over the door, but the unrevealing label "Oye's." Not the slightest intimation appears on the record, or was made on oral argument, to suggest that the agents had information giving them reason to equate "Blackie" Toy and James Wah Toy<i>e. g.,</i> that they had the criminal record of a Toy, or that they had consulted some other kind of official record or list, or had some information of some kind which had narrowed the scope of their search to this particular Toy.</p>
<p>It is conceded that the officers made no attempt to obtain a warrant for Toy's arrest. The simple fact is that on the sparse information at the officers' command, no arrest warrant could have issued consistently with Rules 3 and 4 of the Federal Rules of Criminal Procedure. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span>.<sup>[9]</sup> The arrest warrant procedure serves to insure that the deliberate, impartial judgment of a judicial officer will be interposed <span class="star-pagination">*482</span> between the citizen and the police, to assess the weight and credibility of the information which the complaining officer adduces as probable cause. Cf. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270</a></span>. To hold that an officer may act in his own, unchecked discretion upon information too vague and from too untested a source to permit a judicial officer to accept it as probable cause for an arrest warrant, would subvert this fundamental policy.</p>
<p>The Government contends, however, that any defects in the information which somehow took the officers to petitioner Toy's laundry were remedied by events which occurred after they arrived. Specifically, it is urged that Toy's flight down the hall when the supposed customer at the door revealed that he was a narcotics agent adequately corroborates the suspicion generated by Hom Way's accusation. Our holding in <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span>, is relevant here, and exposes the fallacy of this contention. We noted in that case that the lawfulness of an officer's entry to arrest without a warrant "must be tested by criteria identical with those embodied in <span class="citation no-link">18 U. S. C. § 3109</span>, which deals with entry to execute a search warrant." 357 U. S., at 306. That statute requires that an officer must state his authority and his purpose at the threshold, and be refused admittance, before he may break open the door. We held that when an officer insufficiently or unclearly identifies his office or his mission, the occupant's flight from the door must be regarded as ambiguous conduct. We expressly reserved the question "whether the unqualified requirements of the rule admit of an exception justifying noncompliance in exigent circumstances." 357 U. S., at 309. In the instant case, Toy's flight from the door afforded no surer an inference of guilty knowledge than did the suspect's conduct in the <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span></i> case. Agent Wong did eventually disclose that he was a narcotics officer. However, he affirmatively misrepresented his mission at the <span class="star-pagination">*483</span> outset, by stating that he had come for laundry and dry cleaning. And before Toy fled, the officer never adequately dispelled the misimpression engendered by his own ruse. Cf. <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <i>Gatewood</i> v. <i>United States,</i> <span class="citation" data-id="9444040"><a href="/opinion/233231/gatewood-v-united-states/" aria-description="Citation for case: Gatewood v. United States">209 F. 2d 789</a></span>.</p>
<p>Moreover, he made no effort at that time, nor indeed at any time thereafter, to ascertain whether the man at the door was the "Blackie Toy" named by Hom Way. Therefore, this is not the case we hypothesized in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span></i> where "without an express announcement of purpose, the facts known to officers would justify them in being virtually certain" that the person at the door knows their purpose. 357 U. S., at 310. Toy's refusal to admit the officers and his flight down the hallway thus signified a guilty knowledge no more clearly than it did a natural desire to repel an apparently unauthorized intrusion.<sup>[10]</sup> Here, as in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>,</i> <span class="star-pagination">*484</span> the Government claims no extraordinary circumstances such as the imminent destruction of vital evidence, or the need to rescue a victim in perilsee 357 U. S., at 309 which excused the officer's failure truthfully to state his mission before he broke in.</p>
<p>A contrary holding here would mean that a vague suspicion could be transformed into probable cause for arrest by reason of ambiguous conduct which the arresting officers themselves have provoked. Cf. <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#104" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 104</a></span>. That result would have the same essential vice as a proposition we have consistently rejectedthat a search unlawful at its inception may be validated by what it turns up. <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>; <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#595" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 595</a></span>. Thus we conclude that the Court of Appeals' finding that the officers' uninvited entry into Toy's living quarters was unlawful and that the bedroom arrest which followed was likewise unlawful, was fully justified on the evidence. It remains to be seen what consequences flow from this conclusion.</p>
<p></p>
<h2>II.</h2>
<p>It is conceded that Toy's declarations in his bedroom are to be excluded if they are held to be "fruits" of the agents' unlawful action.</p>
<p>In order to make effective the fundamental constitutional guarantees of sanctity of the home and inviolability of the person, <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, this Court held nearly half a century ago that evidence seized during an unlawful search could not constitute proof against the victim of the search. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. The exclusionary prohibition extends as well to the indirect as the direct products of such invasions. <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> 251 <span class="star-pagination">*485</span> U. S. 385. Mr. Justice Holmes, speaking for the Court in that case, in holding that the Government might not make use of information obtained during an unlawful search to subpoena from the victims the very documents illegally viewed, expressed succinctly the policy of the broad exclusionary rule:</p>
<blockquote>"The essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be used at all. Of course this does not mean that the facts thus obtained become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any others, but the knowledge gained by the Government's own wrong cannot be used by it in the way proposed." 251 U. S., at 392.</blockquote>
<p>The exclusionary rule has traditionally barred from trial physical, tangible materials obtained either during or as a direct result of an unlawful invasion. It follows from our holding in <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>, that the Fourth Amendment may protect against the overhearing of verbal statements as well as against the more traditional seizure of "papers and effects." Similarly, testimony as to matters observed during an unlawful invasion has been excluded in order to enforce the basic constitutional policies. <i>McGinnis</i> v. <i>United States,</i> <span class="citation" data-id="6912304"><a href="/opinion/7011844/mcginnis-v-united-states/" aria-description="Citation for case: McGinnis v. United States">227 F. 2d 598</a></span>. Thus, verbal evidence which derives so immediately from an unlawful entry and an unauthorized arrest as the officers' action in the present case is no less the "fruit" of official illegality than the more common tangible fruits of the unwarranted intrusion.<sup>[11]</sup> See <span class="star-pagination">*486</span> <i>Nueslein</i> v. <i>District of Columbia,</i> <span class="citation" data-id="1512100"><a href="/opinion/1512100/nueslein-v-district-of-columbia/" aria-description="Citation for case: Nueslein v. District of Columbia">115 F. 2d 690</a></span>. Nor do the policies underlying the exclusionary rule invite any logical distinction between physical and verbal evidence. Either in terms of deterring lawless conduct by federal officers, <i>Rea</i> v. <i>United States,</i> <span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span>, or of closing the doors of the federal courts to any use of evidence unconstitutionally obtained, <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>, the danger in relaxing the exclusionary rules in the case of verbal evidence would seem too great to warrant introducing such a distinction.</p>
<p>The Government argues that Toy's statements to the officers in his bedroom, although closely consequent upon the invasion which we hold unlawful, were nevertheless admissible because they resulted from "an intervening independent act of a free will." This contention, however, takes insufficient account of the circumstances. Six or seven officers had broken the door and followed on Toy's heels into the bedroom where his wife and child were sleeping. He had been almost immediately handcuffed and arrested. Under such circumstances it is unreasonable to infer that Toy's response was sufficiently an act of free will to purge the primary taint of the unlawful invasion.<sup>[12]</sup></p>
<p><span class="star-pagination">*487</span> The Government also contends that Toy's declarations should be admissible because they were ostensibly exculpatory rather than incriminating. There are two answers to this argument. First, the statements soon turned out to be incriminating, for they led directly to the evidence which implicated Toy. Second, when circumstances are shown such as those which induced these declarations, it is immaterial whether the declarations be termed "exculpatory."<sup>[13]</sup> Thus we find no substantial reason to omit Toy's declarations from the protection of the exclusionary rule.</p>
<p></p>
<h2>III.</h2>
<p>We now consider whether the exclusion of Toy's declarations requires also the exclusion of the narcotics taken from Yee, to which those declarations led the police. The prosecutor candidly told the trial court that "we wouldn't have found those drugs except that Mr. Toy helped us to." Hence this is not the case envisioned by this Court where the exclusionary rule has no application because the Government learned of the evidence "from an independent source," <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>; nor is this a case in which the connection between the lawless conduct of the police and the discovery of the challenged evidence has "become so attenuated as to dissipate the taint." <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span>. We need not hold that all evidence <span class="star-pagination">*488</span> is "fruit of the poisonous tree" simply because it would not have come to light but for the illegal actions of the police. Rather, the more apt question in such a case is "whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint." Maguire, Evidence of Guilt, 221 (1959). We think it clear that the narcotics were "come at by the exploitation of that illegality" and hence that they may not be used against Toy.</p>
<p></p>
<h2>IV.</h2>
<p>It remains only to consider Toy's unsigned statement. We need not decide whether, in light of the fact that Toy was free on his own recognizance when he made the statement, that statement was a fruit of the illegal arrest. Cf. <i>United States</i> v. <i>Bayer,</i> <span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/" aria-description="Citation for case: United States v. Bayer">331 U. S. 532</a></span>. Since we have concluded that his declarations in the bedroom and the narcotics surrendered by Yee should not have been admitted in evidence against him, the only proofs remaining to sustain his conviction are his and Wong Sun's unsigned statements. Without scrutinizing the contents of Toy's ambiguous recitals, we conclude that no reference to Toy in Wong Sun's statement constitutes admissible evidence corroborating any admission by Toy. We arrive at this conclusion upon two clear lines of decisions which converge to require it. One line of our decisions establishes that criminal confessions and admissions of guilt require extrinsic corroboration; the other line of precedents holds that an out-of-court declaration made after arrest may not be used at trial against one of the declarant's partners in crime.</p>
<p>It is a settled principle of the administration of criminal justice in the federal courts that a conviction must rest upon firmer ground than the uncorroborated admission or <span class="star-pagination">*489</span> confession of the accused.<sup>[14]</sup> We observed in <i>Smith</i> v. <i>United States,</i> <span class="citation" data-id="105256"><a href="/opinion/105256/smith-v-united-states/#153" aria-description="Citation for case: Smith v. United States">348 U. S. 147, 153</a></span>, that the requirement of corroboration is rooted in "a long history of judicial experience with confessions and in the realization that sound law enforcement requires police investigations which extend beyond the words of the accused." In <i>Opper</i> v. <i>United States,</i> <span class="citation" data-id="105249"><a href="/opinion/105249/opper-v-united-states/#89" aria-description="Citation for case: Opper v. United States">348 U. S. 84, 89-90</a></span>, we elaborated the reasons for the requirement:</p>
<blockquote>"In our country the doubt persists that the zeal of the agencies of prosecution to protect the peace, the self-interest of the accomplice, the maliciousness of an enemy or the aberration or weakness of the accused under the strain of suspicion may tinge or warp the facts of the confession. Admissions, retold at a trial, are much like hearsay, that is, statements not made at the pending trial. They had neither the compulsion of the oath nor the test of cross-examination."</blockquote>
<p>It is true that in <i>Smith</i> v. <i>United States, supra</i><i>,</i> we held that although "corroboration is necessary for all elements of the offense established by admissions alone," extrinsic proof was sufficient which "merely fortifies the truth of the confession, without independently establishing the crime charged . . . ." 348 U. S., at 156.<sup>[15]</sup><span class="star-pagination">*490</span> However, Wong Sun's unsigned confession does not furnish competent corroborative evidence. The second governing principle, likewise well settled in our decisions, is that an out-of-court declaration made after arrest may not be used at trial against one of the declarant's partners in crime. While such a statement is "admissible against the others where it is in furtherance of the criminal undertaking. . . all such responsibility is at an end when the conspiracy ends." <i>Fiswick</i> v. <i>United States,</i> <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#217" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211, 217</a></span>. We have consistently refused to broaden that very narrow exception to the traditional hearsay rule which admits statements of a codefendant made in furtherance of a conspiracy or joint undertaking.<sup>[16]</sup> See <i>Krulewitch</i> v. <i>United States,</i> <span class="citation" data-id="9420292"><a href="/opinion/104646/krulewitch-v-united-states/#443" aria-description="Citation for case: Krulewitch v. United States">336 U. S. 440, 443-445</a></span>. And where postconspiracy declarations have been admitted, we have carefully ascertained that limiting instructions kept the jury from considering the contents with respect to the guilt of anyone but the declarant. <i>Lutwak</i> v. <i>United States,</i> <span class="citation" data-id="9420873"><a href="/opinion/105079/lutwak-v-united-states/#618" aria-description="Citation for case: Lutwak v. United States">344 U. S. 604, 618-619</a></span>; <i>Delli Paoli</i> v. <i>United States,</i> <span class="citation" data-id="9421359"><a href="/opinion/105440/delli-paoli-v-united-states/#236" aria-description="Citation for case: Delli Paoli v. United States">352 U. S. 232, 236-237</a></span>. We have never ruled squarely on the question presented here, whether a codefendant's statement might serve to corroborate even where it will not suffice to convict.<sup>[17]</sup> We see <span class="star-pagination">*491</span> no warrant for a different result so long as the rule which regulates the use of out-of-court statements is one of admissibility, rather than simply of weight, of the evidence. The import of our previous holdings is that a co-conspirator's hearsay statements may be admitted against the accused for no purpose whatever, unless made during and in furtherance of the conspiracy. Thus as to Toy the only possible source of corroboration is removed and his conviction must be set aside for lack of competent evidence to support it.</p>
<p></p>
<h2>V.</h2>
<p>We turn now to the case of the other petitioner, Wong Sun. We have no occasion to disagree with the finding of the Court of Appeals that his arrest, also, was without probable cause or reasonable grounds. At all events no evidentiary consequences turn upon that question. For Wong Sun's unsigned confession was not the fruit of that arrest, and was therefore properly admitted at trial. On the evidence that Wong Sun had been released on his own recognizance after a lawful arraignment, and had returned voluntarily several days later to make the statement, we hold that the connection between the arrest and the statement had "become so attenuated as to dissipate the taint." <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span>. The fact that the statement was unsigned, whatever bearing this may have upon its weight and credibility. does not render it inadmissible; Wong Sun understood and adopted its substance, though he could not comprehend the English words. The petitioner has never suggested any impropriety in the interrogation itself which would require the exclusion of this statement.</p>
<p>We must then consider the admissibility of the narcotics surrendered by Yee. Our holding, <i>supra,</i> that this <span class="star-pagination">*492</span> ounce of heroin was inadmissible against Toy does not compel a like result with respect to Wong Sun. The exclusion of the narcotics as to Toy was required solely by their tainted relationship to information unlawfully obtained from Toy, and not by any official impropriety connected with their surrender by Yee. The seizure of this heroin invaded no right of privacy of person or premises which would entitle Wong Sun to object to its use at his trial. Cf. <i>Goldstein</i> v. <i>United States,</i> <span class="citation" data-id="9419243"><a href="/opinion/103663/goldstein-v-united-states/" aria-description="Citation for case: Goldstein v. United States">316 U. S. 114</a></span>.<sup>[18]</sup></p>
<p>However, for the reasons that Wong Sun's statement was incompetent to corroborate Toy's admissions contained in Toy's own statement, any references to Wong Sun in Toy's statement were incompetent to corroborate Wong Sun's admissions. Thus, the only competent source of corroboration for Wong Sun's statement was the heroin itself. We cannot be certain, however, on this state of the record, that the trial judge may not also have considered the contents of Toy's statement as a source of corroboration. Petitioners raised as one ground of objection to the introduction of the statements the claim that each statement, "even if it were a purported admission or confession or declaration against interest of a defendant . . . would not be binding upon the other defendant." The trial judge, in allowing the statements in, apparently overruled all of petitioners' objections, including this one. Thus we presume that he considered all portions of both statements as bearing upon the guilt of both petitioners.</p>
<p>We intimate no view one way or the other as to whether the trial judge might have found in the narcotics alone sufficient evidence to corroborate Wong Sun's admissions <span class="star-pagination">*493</span> that he delivered heroin to Yee and smoked heroin at Yee's house around the date in question. But because he might, as the factfinder, have found insufficient corroboration from the narcotics alone, we cannot be sure that the scales were not tipped in favor of conviction by reliance upon the inadmissible Toy statement. This is particularly important because of the nature of the offense involved here.</p>
<p>Surely, under the narcotics statute, the discovery of heroin raises a presumption that someonegenerally the possessorviolated the law. As to him, once possession alone is proved, the other elements of the offensetransportation and concealment with knowledge of the illegal importation of the drugneed not be separately demonstrated, much less corroborated. <span class="citation no-link">21 U. S. C. § 174</span>. Thus particular care ought to be taken in this area, when the crucial element of the accused's possession is proved solely by his own admissions, that the requisite corroboration be found among the evidence which is properly before the trier of facts. We therefore hold that petitioner Wong Sun is also entitled to a new trial.</p>
<p>The judgment of the Court of Appeals is reversed and the case is remanded to the District Court for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>[For concurring opinion of MR. JUSTICE DOUGLAS, see <i>post,</i> p. 497.]</p>
<p>[For dissenting opinion of MR. JUSTICE CLARK, see <i>post,</i> p. 498.]</p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT.</h2>
<p></p>
<h2>Statement of JAMES WAH TOY taken on June 5, 1959, concerning his knowledge of WONG SUN's narcotic trafficking</h2>
<p>I have know WONG SUN for about 3 months. I know him as SEA DOG which is what everyone calls him. <span class="star-pagination">*494</span> I first met him in Marysville, California, during a Chinese holiday. I drove him back to San Francisco on that occasion. Sometimes he asks me to drive him home and to different places in San Francisco.</p>
<p>Sometime during April or May of this year, he asked me to drive him out to JOHNNY YEE's house, at 11th and Balboa Streets. He asked me to call JOHNNY and tell him we were coming. When we got there we went into the house and WONG SUN took a paper package out of his pocket and put it on the table. Then both WONG SUN and JOHNNY YEE opened the package. I don't know how much heroin was in it, but I know it was more than 10 spoons. I asked them if I could have some for myself and they said yes. I took a little bit and went across the room and smoked it in a cigarette.</p>
<p>WONG SUN and JOHNNY YEE talked for about 10 or 15 minutes, but they were talking in low tones so that I could not hear what they were saying. I didn't see any money change hands, because I wasn't paying too much attention. WONG SUN and I then left the house and drove. I drove WONG SUN to his home and he gave me $15.00. He said the money was for driving him out there.</p>
<p>I have driven WONG SUN out to JOHNNY YEE's house about 5 times altogether. Each time WONG SUN gave me $10 or $15 for doing it and also, Johnny gave me a little heroinenough to put in 3 or 4 cigarettes. The last time I drove WONG SUN out to YEE's house was last Tuesday, May 26, 1959. On Wednesday night June 3, 1959, at about 10:00 p. m., I called JOHNNY YEE and told him that "I'm coming out pretty soonI don't have anything." He said okay, so I drove out there. When I got there I went in the house and Johnny gave me a paper of heroin. The bindle had about enough for 5 or 6 cigarettes. I didn't give him any money and he didn't ask for any. He gives it to me just out of friendship. He has given me heroin like this quite a few times. I don't remember how many times. I have known HOM WEI <span class="star-pagination">*495</span> about 2 or 3 years but I have never dealt in narcotics with him. I have known ED FONG about 1 year and I have never dealt in narcotics with him, either. I have heard people that I know in the Hop Sing Tong Club talk about HOM WEI dealing in narcotics but nothing about ED FONG. I do not know JOHN MOW LIM or BILL FONG. The only connection I have now is JOHNNY YEE.</p>
<p>I have carefully read the foregoing statement, which was made of my own free will, without promise of reward or immunity and not under duress. I have been given ample opportunity to make corrections have initialed or signed each page as evidence thereof and hereby state that this statement is true to the best of my knowledge and belief.</p>
                         ______________________________
                                  JAMES WAH TOY
<p></p>
<h2>.....</h2>
<p>JAMES WAH TOY did not wish to sign this statement at this time. He stated he may change his mind at a later date. However, I read this statement to him and in addition he read it also and stated that the contents thereof were true to the best of his knowledge. Corrections made were by JAMES WAH TOY without his initials.</p>
                    /s/ WILLIAM WONG
                        William Wong. Narcotic Agent
<p></p>
<h2>STATEMENT OF WONG SUN</h2>
<p>I met JAMES TOY approximately the middle of March, this year, at Marysville, California, during a Chinese celebration. We returned to San Francisco together and we discussed the possible sale of heroin. I told JAMES that I could get a piece of heroin for $450 from a person known as BILL.</p>
<p>Shortly after returning to San Francisco, JAMES told me he wanted me to get a piece. I asked him who it was <span class="star-pagination">*496</span> for and he told me it was for JOHNNY. He gave me $450 and I obtained a piece of heroin from BILL. I did this on approximately 8 occasions, however, at least one of these times the heroin was not for JOHNNYfor another friend of JAMES TOY. JOHNNY would pay JAMES $600 for each piece.</p>
<p>On several occasions after I had obtained the piece for JAMES I would drive with him to JOHNNY's house, 606 11th Avenue, and we would go upstairs to the bedroom. There, all three of us would smoke some of the heroin and JAMES would give the piece to JOHNNY. I also went with JAMES on approximately 3 other occasions when he did not take any heroin and then we smoked at JOHNNY's and we would also get some for our own use.</p>
<p>About 4 days before I was arrested (arrested on June 4, 1959) JAMES called me at home about 7 o'clock in the evening and told me to come by. I went to the laundry and JAMES told me to get a piece. I called BILL and arranged to meet him. JAMES gave me $450 which I gave to BILL when I met him. BILL called me about one hour later at the laundry and I met him. He gave me one piece, which I gave to JAMES, and JAMES immediately thereafter called JOHNNY. We drove to 606 11th Ave. at approximately midnight and JAMES gave the piece to JOHNNY. It was contained in a rubber contraceptive in a small brown paper bag.</p>
<p>Again on June 3rd, the night before I was arrested, I met JAMES at the laundry, prior to 11 o'clock in the evening, and JAMES telephoned JOHNNY at EV6-9336. Then we went out to JOHNNY's and smoked heroin and also had one paper for our own use later. We were there approximately 1/2 hour and then left.</p>
<p>The laundry mentioned is OYE's LAUNDRY, 1733 Leavenworth Street, which is run by JAMES TOY. I do not know JOHNNY's last name and know him only <span class="star-pagination">*497</span> through JAMES TOY. As well as the few times at JOHNNY's home, I have seen JOHNNY on a number of occasions at the laundry.</p>
<p>I have carefully read the foregoing statement, consisting of 2 pages which was made of my own free will, without promise of reward or immunity and not under duress. I have been given ample opportunity to make corrections, have initialed or signed each page as evidence thereof and hereby state that this statement is true to the best of my knowledge and belief.</p>
                             ______________________________
                                          WONG SUN
<p></p>
<h2>.....</h2>
<p>WONG SUN, being unable to read English, did not sign this statement. However, I read this statement to him and he stated that the contents thereof were true to the best of his knowledge.</p>
                     /s/ WILLIAM WONG
                         William Wong, Narcotic Agent
<p>MR. JUSTICE DOUGLAS, concurring.</p>
<p>While I join the Court's opinion I do so because nothing the Court holds is inconsistent with my belief that there having been time to get a warrant, probable cause alone could not have justified the arrest of petitioner Toy without a warrant.</p>
<p>I adhere to the views I expressed in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#273" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 273</a></span>. What I said in the <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> case had been earlier stated by Mr. Justice Jackson, writing for the Court in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (another narcotics case):</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection <span class="star-pagination">*498</span> consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers." Pp. 13-14. And see <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/#615" aria-description="Citation for case: Chapman v. United States">365 U. S. 610, 615-616</a></span>.</blockquote>
<p>The Court finds it unnecessary to reach that constitutional question. I mention it only to reiterate that the <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span></i> case represents the law and is in no way eroded by what we fail to decide today.</p>
<p>MR. JUSTICE CLARK, with whom MR. JUSTICE HARLAN, MR. JUSTICE STEWART and MR. JUSTICE WHITE join. dissenting.</p>
<p>The Court has made a Chinese puzzle out of this simple case involving four participants: Hom Way, Blackie Toy, Johnny Yee and "Sea Dog" Sun. In setting aside the convictions of Toy and Sun it has dashed to pieces the heretofore recognized standards of probable cause necessary to secure an arrest warrant or to make an arrest without one. Instead of dealing with probable cause as involving "probabilities," "the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act," <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949), the Court sets up rigid, mechanical standards, applying the 20-20 vision of hindsight in an area where the ambiguity and immediacy inherent in unexpected arrest are present. While probable cause must be based on more than mere suspicion, <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#104" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 104</a></span> (1959), it does <span class="star-pagination">*499</span> not require proof sufficient to establish guilt. <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#312" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 312</a></span> (1959). The sole requirement heretofore has been that the knowledge in the hands of the officers at the time of arrest must support a "man of reasonable caution in the belief" that the subject had committed narcotic offenses. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925). That decision is faced initially not in the courtroom but at the scene of arrest where the totality of the circumstances facing the officer is weighed against his split-second decision to make the arrest. This is an everyday occurrence facing law enforcement officers, and the unrealistic, enlarged standards announced here place an unnecessarily heavy hand upon them. I therefore dissent.</p>
<p></p>
<h2>I.</h2>
<p>The first character in this affair is Hom Way, who was arrested in possession of narcotics and told the officers early that morning that he had purchased an ounce of heroin on the previous night from Blackie Toy, who operated a laundry on Leavenworth Street. Narcotics agents, armed with this information from a person they had known for six weeks and who was under arrest for possession of narcotics, immediately sought out Blackie Toy, the second character. The laundry was located without difficulty (as far as the record shows) from the information furnished by Hom Way. The Court gratuitously reads into the record its supposition that Hom Way "merely invited the officers to roam the length of Leavenworth Street (some 30 blocks) in search of one `Blackie Toy's' laundry . . . ." On the contrary, the identification of "Blackie" and the directions to his laundry were sufficiently accurate for the officerstwo of whom were of Chinese ancestryto find Blackie at his laundry within an hour. I cannot say in the face of this record that this was a "roaming" performance <span class="star-pagination">*500</span> up and down Leavenworth Street. To me it was efficient police work by officers familiar with San Francisco and the habits and practices of its Chinese-American inhabitants. Indeed, the information was much more explicit than that approved by this Court in <i>Draper</i> v. <i>United States, supra</i><i>.</i></p>
<p>There are other indicia of reliability, however. Here the informer, believed by the officers to be reliable,<sup>[*]</sup> was under arrest when he implicated himself in the purchase of an ounce of heroin the previous night. Since he was in possession of narcotics and his information related to a narcotics sale in which he was the buyer, the officers had good reason to rely on Hom Way's knowledge. See <i>Rodgers</i> v. <i>United States,</i> <span class="citation" data-id="248139"><a href="/opinion/248139/e-nadine-rodgers-v-united-states/" aria-description="Citation for case: E. Nadine Rodgers v. United States">267 F. 2d 79</a></span> (C. A. 9th Cir. 1959), and <i>Thomas</i> v. <i>United States,</i> <span class="citation" data-id="251634"><a href="/opinion/251634/patrick-fagan-thomas-v-united-states/" aria-description="Citation for case: Patrick Fagan Thomas v. United States">281 F. 2d 132</a></span> (C. A. 8th Cir.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./364/904/">364 U. S. 904</a></span> (1960). As to his credibility, he was confronted with prosecution for possession of narcotics and well knew that any discrepancies in his story might go hard with him. Furthermore, the statement was a declaration against interest which stripped Hom Way of any explanation for his possession of narcotics and made certain the presumption of <span class="citation no-link">21 U. S. C. § 174</span>. I do not see what stronger and more reliable information one could have to establish probable cause for the arrest without warrant of Blackie Toy.</p>
<p>But even assuming there was no probable cause at this point, the Government produced additional evidence to support the lawfulness of Blackie's arrest. In broad daylight, about 6:30 on the same morning that Hom Way was arrested, one of the officers of Chinese ancestry, Agent Alton Wong, knocked on Blackie Toy's laundry door. When Wong told him that he wanted laundry, Blackie <span class="star-pagination">*501</span> opened the door and advised him to return at 8 a. m. Wong testified that he then "pulled out [his] badge" and announced that he was a narcotics agent. Blackie slammed the door in Wong's face and ran down the hall of the laundry. Wong broke through the door after himcalling again that he was "a narcotics Treasury agent." Only when Blackie reached the family bedroom was Wong able to arrest him, as he reached into a nightstand drawer, apparently looking for narcotics. Agent Wong immediately confronted him with Hom Way's accusation that Blackie Toy had sold him narcotics. Blackie denied selling narcotics, but he did not deny knowing Hom Way and later admitted knowing him. There is no basis in <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span> (1958), for the Court's conclusion that Blackie's flight "signified . . . a natural desire [by Toy] to repel an apparently unauthorized intrusion. . . ." As I see it this is incredible in the light of the record. Nor is there any support in the record that "before Toy fled, the officer never adequately dispelled the misimpression engendered by his own ruse." On the contrary the officer's showing of his badge and announcement that he was a narcotics agent immediately put Blackie in flight behind the slamming door. To conclude otherwise takes all prizes as a <i>non sequitur.</i> As he pursued, Wong continued to identify himself as a narcotics agent. I ask, how could he more clearly announce himself and his purpose?</p>
<p>This Court has often held unexplained flightas here from an officer to be strong evidence of guilt. <i>E. g., </i><i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931); <i>Brinegar</i> v. <i>United States, supra,</i> at p. 166, n. 7; see <i>Henry</i> v. <i>United States, supra</i><i>,</i> where the Court was careful to distinguish its facts from those of "fleeing men or men acting furtively." <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States">361 U. S., at 103</a></span>. Moreover, as the Government has always emphasized, this is particularly true in narcotics cases where delay may have serious consequences, <i>i. e.,</i> the hiding <span class="star-pagination">*502</span> or destruction of the drugs. This Court noted without disapproval in <i>Miller</i> v. <i>United States, supra</i><i>,</i> the state decisions holding that "justification for noncompliance [with the rule] exists in exigent circumstances, as, for example, when the officers may in good faith believe . . . that the person to be arrested is fleeing or attempting to destroy evidence. <i>People</i> v. <i>Maddox,</i> <span class="citation" data-id="9627819"><a href="/opinion/1428666/people-v-maddox/" aria-description="Citation for case: People v. Maddox">46 Cal. 2d 301</a></span>, <span class="citation" data-id="9627819"><a href="/opinion/1428666/people-v-maddox/" aria-description="Citation for case: People v. Maddox">294 P. 2d 6</a></span>." 357 U. S., at 309. And the Court continued, "It may be that, without an express announcement of purpose, the facts known to officers would justify them in being virtually certain that the petitioner already knows their purpose so that an announcement would be a useless gesture. Cf. <i>People</i> v. <i>Martin,</i> <span class="citation" data-id="1139982"><a href="/opinion/1139982/people-v-martin/" aria-description="Citation for case: People v. Martin">45 Cal. 2d 755</a></span>, <span class="citation" data-id="1139982"><a href="/opinion/1139982/people-v-martin/" aria-description="Citation for case: People v. Martin">290 P. 2d 855</a></span>; Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 798, 802 (1924)." <span class="citation no-link"><i>Id.,</i> at 310</span>.</p>
<p>The Court places entire reliance on the decision in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>.</i> I submit that it is inapposite. That case involved interpretation of the law of the District of Columbia. <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#306" aria-description="Citation for case: Miller v. United States"><i>Id.,</i> at 306</a></span>. The arrest was at night, and the door was broken in just as the defendant began to close it. Thus there was no flight but only what the officer believed to be an attempt to bar their entrance. The only identification given by the officers occurred before the defendant opened the door, when "in a low voice" through the closed door they answered the defendant's query as to who was there by saying, "Police." <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#303" aria-description="Citation for case: Miller v. United States"><i>Id.,</i> at 303</a></span>. The facts in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span></i> differ significantly from this case both in the clarity of identification by the officers and in the character and extent of the defendant's conduct. For that reason, the conclusions that Blackie's flight is evidence to support probable cause and that the officers gave sufficient notice to permit lawful entry are supported rather than weakened by the Court's decision in <i><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>.</i></p>
<p>The information from Hom Way and Blackie Toy's unexplained flight cannot be viewed "in two separate. logic-tight compartments. . . . [T]ogether they composed <span class="star-pagination">*503</span> a picture meaningful to a trained, experienced observer." <i>Christensen</i> v. <i>United States,</i> 104 U. S. App. D.C. 35, 36, <span class="citation" data-id="9446395"><a href="/opinion/246074/george-a-christensen-v-united-states/#193" aria-description="Citation for case: George A. Christensen v. United States">259 F. 2d 192, 193</a></span> (1958). I submit that the officers as reasonable men properly concluded that the petitioner was the "Blackie Toy" who Hom Way informed them had committed a felony and that his immediate arrestas he ran through his hallwas lawful and was imperative in order to prevent his escape. In view of this there is no "poisonous tree" whose fruits we must evaluate, and Blackie's declaration at the time of the arrest and the narcotics found in Yee's possession are admissible in evidence. The trial court found that evidence sufficiently corroborative of Toy's confession, and the Court of Appeals affirmed. For the same reasons discussed, <i>infra,</i> as to Wong Sun, I see no occasion to overturn these consistent findings of two courts.</p>
<p></p>
<h2>II.</h2>
<p>As to "Sea Dog," Wong Sun, there is no disagreement that his confession and the narcotics found in Yee's possession were admissible in evidence against him. The question remains as to whether there was sufficient independent evidence to corroborate the confession. Such evidence "does not have to prove the offense beyond a reasonable doubt, or even by a preponderance . . . ." <i>Smith</i> v. <i>United States,</i> <span class="citation" data-id="105256"><a href="/opinion/105256/smith-v-united-states/#156" aria-description="Citation for case: Smith v. United States">348 U. S. 147, 156</a></span> (1954). The requirement is satisfied "if the corroboration merely fortifies the truth of the confession, without independently establishing the crime charged . . . ." <i>Ibid.;</i> see also <i>Opper</i> v. <i>United States,</i> <span class="citation" data-id="105249"><a href="/opinion/105249/opper-v-united-states/" aria-description="Citation for case: Opper v. United States">348 U. S. 84</a></span> (1954). Wong Sun's confession stated in part that about four days before his arrest he and Toy delivered an ounce of heroin to Yee and that on the night before his arrestthe night of June 3, 1959 he and Toy smoked some heroin at Yee's house. On June 4, 1959, the officers found at Yee's residence quantities of heroin totaling "just less than one ounce." In light <span class="star-pagination">*504</span> of this evidence, I am unable to say that the trial court and the Court of Appeals erred in holding that Wong Sun's confession was sufficiently corroborated.</p>
<p>The Court does not reach a contrary conclusion as to corroboration, but it grants Wong Sun a new trial on the ground that the trial court "may" also "have considered the contents of Toy's statement as a source of corroboration" of it. This point was not raised as a question here nor was it discussed in the briefs. Despite this the Court goes to some lengths to develop a chain of inferences in finding prejudicial error. This might be plausible where the case was tried to a jury, as were all the cases cited by the Court. Indeed, I find no case where such presumption of error was applied, as here, to a trial before a judge. The Court admits that the heroin found in Johnny Yee's possession might itself be sufficient corroboration, but it reverses on the excuse that the judge "may" have considered Toy's confession as well. I see no reason for this assumption where a federal judge is the trier of the fact, and I would therefore affirm the judgment as to both petitioners.</p>
<h2>NOTES</h2>
<p>[1]  <span class="citation no-link">21 U. S. C. § 174</span>:
</p>
<p>"Whoever fraudulently or knowingly imports or brings any narcotic drug into the United States or any territory under its control or jurisdiction, contrary to law, or receives, conceals, buys, sells, or in any manner facilitates the transportation, concealment, or sale of any such narcotic drug after being imported or brought in, knowing the same to have been imported or brought into the United States contrary to law, or conspires to commit any of such acts in violation of the laws of the United States, shall be imprisoned not less than five or more than twenty years and, in addition, may be fined not more than $20,000. For a second or subsequent offense (as determined under section 7237 (c) of the Internal Revenue Code of 1954), the offender shall be imprisoned not less than ten or more than forty years and, in addition, may be fined not more than $20,000.</p>
<p>"Whenever on trial for a violation of this section the defendant is shown to have or to have had possession of the narcotic drug, such possession shall be deemed sufficient evidence to authorize conviction unless the defendant explains the possession to the satisfaction of the jury."</p>
<p>[2]  A "piece" is approximately one ounce.</p>
<p>[3]  The Record of the arraignment proceedings recites that arrest warrants were issued, on the arraignment dates, for the arrest of both petitioners and Yee. It was conceded in the trial court, however, that no arrest warrants were outstanding at the time of the actual arrests on June 4.
</p>
<p>The Record also states that bond was initially fixed for each of the petitioners and for Yee in the amount of $5,000, on the recommendation of the United States Attorney. Later on the respective arraignment days, again on motion of the United States Attorney, it was ordered that each of the three be released on his own recognizance.</p>
<p>[4]  Because neither statement was ever signed, the blanks in which the dates were to have been inserted were never filled in. The heading of Toy's statement suggests that it was made on June 5, although Agent William Wong at the trial suggested he had only talked informally with Toy on that date, the formal statement not being made until June 9. The agent also testified that Wong Sun's statement was made June 9, although a rubber-stamp date beneath the agent's own signature at the foot of the statement reads, "June 15, 1959."</p>
<p>[5]  The full texts of both statements are set forth in an Appendix to this opinion.</p>
<p>[6]  <span class="citation no-link">26 U. S. C. § 7607</span>:
</p>
<p>"The Commissioner, Deputy Commissioner, Assistant to the Commissioner, and agents, of the Bureau of Narcotics of the Department of the Treasury, and officers of the customs (as defined in section 401 (1) of the Tariff Act of 1930, as amended; <span class="citation no-link">19 U. S. C., sec. 1401</span> (1)), may</p>
<p>"(1) carry firearms, execute and serve search warrants and arrest warrants, and serve subpenas and summonses issued under the authority of the United States, and</p>
<p>"(2) make arrests without warrant for violations of any law of the United States relating to narcotic drugs (as defined in section 4731) or marihuana (as defined in section 4761) where the violation is committed in the presence of the person making the arrest or where such person has reasonable grounds to believe that the person to be arrested has committed or is committing such violation."</p>
<p>The terms "probable cause" for purposes of the Fourth Amendment and "reasonable grounds" as used in the statute, mean substantially the same. <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#310" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 310, n. 3</a></span>; <i>United States</i> v. <i>Walker,</i> <span class="citation" data-id="242778"><a href="/opinion/242778/the-united-states-of-america-v-farris-walker/#526" aria-description="Citation for case: The United States of America v. Farris Walker">246 F. 2d 519, 526</a></span>.</p>
<p>[7]  See <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 485-487</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#16" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 16-17</a></span>. See generally Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 673, 695-701 (1924).</p>
<p>[8]  Our discussion implies no view whether a search warrant should be obtained where a search is conducted incident to a valid arrest, cf. <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, for nothing in this case turns on the presence or absence of a search warrant. Since the officers had obtained an arrest warrant in <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>,</i> the question before us here was not there presented. As to the question before us, see <i>Wrightson</i> v. <i>United States,</i> <span class="citation" data-id="9444624"><a href="/opinion/236713/samuel-wrightson-v-united-states/" aria-description="Citation for case: Samuel Wrightson v. United States">222 F. 2d 556</a></span>, 559-560:
</p>
<p>"But, if officers can arrest without a warrant and never be required to disclose the facts upon which they based their belief of probable causeif, in other words, they have an untouchable power to arrest without a warrant,why would they ever bother to get a warrant? And the same obvious conclusion follows if the courts, when an arrest is attacked as illegal, will assume, without facts, that an arrest without a warrant was for probable cause. To strike down all factual requirements in respect to probable cause for arrests without a warrant, while maintaining them for the issuance of a warrant, would be to blast one of the support columns of justice by law."</p>
<p>[9]  We noted in <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> that Rules 3 and 4 of the Federal Rules of Criminal Procedure provide that an arrest warrant shall issue only upon a sworn complaint setting forth "the essential facts constituting the offense charged," and showing "that there is probable cause to believe that an offense has been committed and that the defendant has committed it . . . ." The Fourth Amendment, from which the requirements of the Rules derive, provides that ". . . no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and <i>particularly describing</i> . . . the persons or things to be seized." (Emphasis added.) The requirement applies both to arrest and search warrants. A description of a suspect merely as "Blackie Toy," operator of a laundry somewhere on Leavenworth Street, hardly is information "particularly describing . . . the person . . . to be seized." Such information is no better than the wholesale or "dragnet" search warrant, which we have condemned. See, <i>e. g., </i><i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span>; see generally Kaplan, Search and Seizure: A No-Man's Land in the Criminal Law, <span class="citation no-link">49 Calif. L. Rev. 474</span>, 480-482 (1961).</p>
<p>[10]  Although the question presented here is only whether the petitioner's flight justified an inference of guilt sufficient to generate probable cause for his arrest, and not whether his flight would serve to corroborate proof of his guilt at trial, the two questions are inescapably related. Thus it is relevant to the present case that we have consistently doubted the probative value in criminal trials of evidence that the accused fled the scene of an actual or supposed crime. In <i>Alberty</i> v. <i>United States,</i> <span class="citation" data-id="94447"><a href="/opinion/94447/alberty-v-united-states/#511" aria-description="Citation for case: Alberty v. United States">162 U. S. 499, 511</a></span>, this Court said:
</p>
<p>". . . it is not universally true that a man, who is conscious that he has done a wrong, `will pursue a certain course not in harmony with the conduct of a man who is conscious of having done an act which is innocent, right and proper;' since it is a matter of common knowledge that men who are entirely innocent do sometimes fly from the scene of a crime through fear of being apprehended as the guilty parties, or from an unwillingness to appear as witnesses. Nor is it true as an accepted axiom of criminal law that `the wicked flee when no man pursueth, but the righteous are as bold as a lion.' "</p>
<p>See also <i>Hickory</i> v. <i>United States,</i> <span class="citation" data-id="94334"><a href="/opinion/94334/hickory-v-united-states/" aria-description="Citation for case: Hickory v. United States">160 U. S. 408</a></span>; <i>Allen</i> v. <i>United States,</i> <span class="citation" data-id="94565"><a href="/opinion/94565/allen-v-united-states/" aria-description="Citation for case: Allen v. United States">164 U. S. 492</a></span>; <i>Starr</i> v. <i>United States,</i> <span class="citation" data-id="94573"><a href="/opinion/94573/starr-v-united-states/" aria-description="Citation for case: Starr v. United States">164 U. S. 627</a></span>; and for the views of two Courts of Appeals see <i>Vick</i> v. <i>United States,</i> <span class="citation" data-id="234904"><a href="/opinion/234904/earl-e-vick-v-united-states/#233" aria-description="Citation for case: Earl E. Vick v. United States">216 F. 2d 228, 233</a></span> (C. A. 5th Cir.) ("One motive is about as likely as another. Appellant may be guilty, but his conviction cannot rest upon mere conjecture and suspicion"); cf. <i>Cooper</i> v. <i>United States,</i> <span class="citation" data-id="235392"><a href="/opinion/235392/cooper-v-united-states/#41" aria-description="Citation for case: Cooper v. United States">218 F. 2d 39, 41</a></span> (C. A. D. C. Cir.) ("After all, innocent people caught in a web of circumstances frequently become terror-stricken"). But cf. <i>United States</i> v. <i>Heitner,</i> <span class="citation" data-id="1507600"><a href="/opinion/1507600/united-states-v-heitner/" aria-description="Citation for case: United States v. Heitner">149 F. 2d 105</a></span> (C. A. 2d Cir.).</p>
<p>[11]  See Kamisar, Illegal Searches or Seizures and Contemporaneous Incriminating Statements: A Dialogue on a Neglected Area of Criminal Procedure, 1961 U. of Ill. Law Forum 78, 84-96. But compare Maguire, Evidence of Guilt (1959), 187-190.</p>
<p>[12]  See Lord Devlin's comment: "It is probable that even today, when there is much less ignorance about these matters than formerly, there is still a general belief that you must answer all questions put to you by a policeman, or at least that it will be the worse for you if you do not." Devlin, The Criminal Prosecution in England (1958), 32. Even in the absence of such oppressive circumstances, and where an exclusionary rule rests principally on nonconstitutional grounds, we have sometimes refused to differentiate between voluntary and involuntary declarations. See Hogan and Snee, The McNabb-Mallory Rule: Its Rise, Rationale and Rescue, 47 Geo. L. J. 1, 26-27 (1958). For illustrative situations where a voluntary act of the accused has been held insufficient to cure the otherwise unlawful acquisition of evidence, see <i>Bynum</i> v. <i>United States,</i> <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d 465</a></span> (holding inadmissible fingerprints made by defendant after unlawful arrest); <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="1424394"><a href="/opinion/1424394/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">189 F. Supp. 776</a></span> (excluding narcotics voluntarily surrendered by accused in the course of an unauthorized search). The Ninth Circuit Court of Appeals from which the instant case comes has recognized in an analogous context, that "all declarations and statements under the compulsion of the things so seized, are affected by the vice of primary illegality. . . ." <i>Takahashi</i> v. <i>United States,</i> <span class="citation" data-id="1478266"><a href="/opinion/1478266/takahashi-v-united-states/#122" aria-description="Citation for case: Takahashi v. United States">143 F. 2d 118, 122</a></span>.</p>
<p>[13]  Moreover, we held in <i>Opper</i> v. <i>United States,</i> <span class="citation" data-id="105249"><a href="/opinion/105249/opper-v-united-states/#92" aria-description="Citation for case: Opper v. United States">348 U. S. 84, 92</a></span>, that even where exculpatory statements are voluntary and thus clearly admissible, they require at least the degree of corroboration required of incriminating statements.</p>
<p>[14]  For the history and development of the corroboration requirement, see 7 Wigmore, Evidence (3d ed. 1940), §§ 2070-2071; Note, Proof of the Corpus Delicti Aliunde the Defendant's Confession, 103 U. of Pa. L. Rev. 638-649 (1955). For the present scope and application of the rule, see 2 Underhill, Criminal Evidence (5th ed. 1956), §§ 402-403. For a comprehensive collection of cases, see Annot., 45 A. L. R. 2d 1316 (1956).</p>
<p>[15]  Where the crime involves physical damage to person or property, the prosecution must generally show that the injury for which the accused confesses responsibility did in fact occur, and that some person was criminally culpable. A notable example is the principle that an admission of homicide must be corroborated by tangible evidence of the death of the supposed victim. See 7 Wigmore, Evidence (3d ed. 1940), § 2072, n. 5. There need in such a case be no link, outside the confession, between the injury and the accused who admits having inflicted it. But where the crime involves no tangible <i>corpus delicti,</i> we have said that "the corroborative evidence must implicate the accused in order to show that a crime has been committed." 348 U. S., at 154. Finally, we have said that one uncorroborated admission by the accused does not, standing alone, corroborate an unverified confession. <i>United States</i> v. <i>Calderon,</i> <span class="citation" data-id="105257"><a href="/opinion/105257/united-states-v-calderon/#165" aria-description="Citation for case: United States v. Calderon">348 U. S. 160, 165</a></span>.</p>
<p>[16]  See Developments in the LawCriminal Conspiracy, <span class="citation no-link">72 Harv. L. Rev. 922</span>, 989-990 (1959).</p>
<p>[17]  Cf. Williams, The Proof of Guilt (1958), 135: "Even where . . . the evidence of an accomplice becomes admissible against his fellows, it remains suspect evidence, because of the tainted source from which it comes. The accomplice may no longer have anything to fear or hope from the way in which he gives his evidence; yet he may mistakenly entertain such a fear or hope, or he may wish by his evidence against others to gratify some spite against them."</p>
<p>[18]  This case is not like <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>, where the person challenging the seizure of evidence was lawfully on the premises at the time of the search. Nor is it like <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>, where we held that a landlord could not lawfully consent to a search of his tenant's premises. See generally Edwards, Standing to Suppress Unreasonably Seized Evidence, 47 N. W. U. L. Rev. 471 (1952).</p>
<p>[*]  One of the officers testified at the trial that he had known Hom Way for six weeks. In response to the question whether Hom Way was a reliable informer, the officer replied, "I believe so, yes, sir."</p>

</div>
```

---
