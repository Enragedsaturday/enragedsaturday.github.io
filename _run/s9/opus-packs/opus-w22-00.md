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

## GROUP: _overhaul2/lake/cases/Wilkes v. Wood.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "dcdc0ac54389adc2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Wilkes v. Wood"}, "payload": {"all": [{"cite": "19 How. St. Tr. 1153", "page": 1153, "reporter": "How. St. Tr.", "selected_official": true, "source": "off_cl.adjudication", "type": "official", "volume": 19}, {"cite": "98 Eng. Rep. 489", "page": 489, "reporter": "Eng. Rep.", "selected_official": false, "source": "off_cl.adjudication", "type": "parallel", "volume": 98}, {"cite": "Lofft 1", "page": 1, "reporter": "Lofft", "selected_official": false, "source": "off_cl.adjudication", "type": "parallel", "volume": null}, {"cite": "[1763] EWHC CP J95", "page": null, "reporter": null, "selected_official": false, "source": "off_cl.adjudication", "type": "vendor_neutral", "volume": null}], "display": "19 How. St. Tr. 1153 (C.P. 1763)", "official": {"cite": "19 How. St. Tr. 1153", "page": 1153, "reporter": "How. St. Tr.", "selected_official": true, "source": "off_cl.adjudication", "type": "official", "volume": 19}, "official_selection_present": true, "record_id": "Wilkes v. Wood"}}
{"assertion_id": "0a6a290d6932c8cd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Wilkes v. Wood"}, "payload": {"as_of_content": "1763-12-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Wilkes v. Wood", "scope_note": "Off-CL record (A16/A17): CL citator lanes intentionally not run. Validity rests on the O1 web-verified page treatment (legacy 'good', as of 2026-06-30) re-seeded post-elevation per the S1 A4 mapping; Wilkes' general-warrant condemnation is favorably restated by SCOTUS (Stanford v. Texas, Marcus, Torres v. Madrid). Authority weight remains Historical (English origin).", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Will v. Michigan Department of State Police.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "aaa2c56a9c1dacbf", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Will v. Michigan Department of State Police"}, "payload": {"all": [{"cite": "491 U.S. 58", "page": "58", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "491"}, {"cite": "109 S. Ct. 2304", "page": "2304", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "105 L. Ed. 2d 45", "page": "45", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "1989 U.S. LEXIS 2975", "page": "2975", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}, {"cite": "57 U.S.L.W. 4677", "page": "4677", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "57"}, {"cite": "50 Empl. Prac. Dec. (CCH) 39,067", "page": "39,067", "reporter": "Empl. Prac. Dec. (CCH)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "50"}, {"cite": "49 Fair Empl. Prac. Cas. (BNA) 1664", "page": "1664", "reporter": "Fair Empl. Prac. Cas. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "49"}], "display": "491 U.S. 58", "official": {"cite": "491 U.S. 58", "page": "58", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "491"}, "official_selection_present": true, "record_id": "Will v. Michigan Department of State Police"}}
{"assertion_id": "ae0df58e54b87326", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Will v. Michigan Department of State Police"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Will v. Michigan Department of State Police", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Wilson v. Arkansas.json  (`lake-record`, 5 assertions)

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
{"assertion_id": "734ea3dd24002b33", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Wilson v. Arkansas"}, "payload": {"all": [{"cite": "514 U.S. 927", "page": "927", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "514"}, {"cite": "115 S. Ct. 1914", "page": "1914", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "115"}, {"cite": "131 L. Ed. 2d 976", "page": "976", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "131"}, {"cite": "1995 U.S. LEXIS 3464", "page": "3464", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1995"}], "display": "514 U.S. 927", "official": {"cite": "514 U.S. 927", "page": "927", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "514"}, "official_selection_present": true, "record_id": "Wilson v. Arkansas"}}
{"assertion_id": "2fb2c2eb53522595", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-934a", "record_id": "Wilson v. Arkansas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-934a", "pinpoint_status": "slip-only", "quote": "This is not to say, of course, that every entry must be preceded by an announcement. The Fourth Amendment's flexible requirement of reasonableness should not be read to mandate a rigid rule of announcement that ignores countervailing law enforcement interests.", "quote_fidelity": "mismatch", "record_id": "Wilson v. Arkansas", "star_marker": null}}
{"assertion_id": "9b15fccab2d64a5e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-929", "record_id": "Wilson v. Arkansas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-929", "pinpoint_status": "slip-only", "quote": "principle — that officers ordinarily must announce their presence and authority before entering a dwelling — forms part of the Fourth Amendment reasonableness inquiry. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Wilson v. Arkansas", "star_marker": null}}
{"assertion_id": "a8320b3977d99f2d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-934", "record_id": "Wilson v. Arkansas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-934", "pinpoint_status": "slip-only", "quote": "in some circumstances an officer's unannounced entry into a home might be unreasonable under the Fourth Amendment.", "quote_fidelity": "mismatch", "record_id": "Wilson v. Arkansas", "star_marker": null}}
{"assertion_id": "5bf45e4911b0f385", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Wilson v. Arkansas"}, "payload": {"as_of_content": "1995-05-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Wilson v. Arkansas", "scope_note": "Knock-and-announce as part of reasonableness; refined by Richards v. Wisconsin (1997). Hudson v. Michigan (2006) held a violation does not trigger suppression. Good law.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Wilson v. Layne.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Wilson v. Layne"
type: case
citation: "526 U.S. 603 (1999)"
parallel_cite: "119 S. Ct. 1692; 143 L. Ed. 2d 818"
neutral_cite: 1999 U.S. LEXIS 3633
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-05-24
docket: 98-83
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-05-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wilson v. Layne
  varies_by_point: false
  scope_note: "Good law: media ride-along into a home during warrant execution violates the 4A; officers had QI on the then-undeveloped law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118289/wilson-v-layne/"
  cluster_id: 118289
  opinion_id: 9433801
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Scope Manner and Related Issues]]"
    role: "Related (cross-doctrine)"
related: ["[[Hanlon v. Berger]]", "[[Harlow v. Fitzgerald]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "media-ride-along", "warrant-execution", "clearly-established"]
holding: "Bringing the media or other third parties into a home during the execution of a warrant, when not in aid of the warrant, violates the Fourth Amendment — but the officers had qualified immunity because that right was not clearly established."
lake:
  record_id: Wilson v. Layne
  status: verified
  projected_at: 2026-07-06
---

# Wilson v. Layne

*526 U.S. 603 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In April 1992, deputy U.S. Marshals and county deputies executing arrest warrants for Dominic Wilson invited a *Washington Post* reporter and photographer to accompany them into the home of Dominic's parents, Charles and Geraldine Wilson, during the early-morning entry. The parents were roused from bed; Charles Wilson, in his underwear, was subdued on the floor while the journalists observed and photographed (the photos were never published). Dominic was not there. The Wilsons sued the officers under *[[Bivens v. Six Unknown Named Agents|Bivens]]* and § 1983.

## Issue
Whether police violate the Fourth Amendment by bringing media into a home during the execution of a warrant, and if so, whether the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Rule
Such a media intrusion violates the Fourth Amendment: "We hold that it is a violation of the Fourth Amendment for police to bring members of the media or other third parties into a home during the execution of a warrant when the presence of the third parties in the home was not in aid of the execution of the warrant." — 526 U.S. at 614. ^pin-614

But [[Qualified Immunity|qualified immunity]] still protects the officers unless the right was clearly established at the time. "We hold that it was not unreasonable for a police officer in April 1992 to have believed that bringing media observers along during the execution of an arrest warrant (even in a home) was lawful." — *Id.* at 615. ^pin-615

## Application
Inviting the journalists served no purpose in executing the arrest warrant — they did not aid the search for Dominic — so their presence inside the home exceeded what the warrant authorized and violated the Fourth Amendment. On immunity, however, in 1992 the constitutional question was not "open and shut": no judicial decision had held that a media ride-along became unlawful when it entered a home, and the practice was common. Because the contours of the right were not sufficiently clear that a reasonable officer would have understood the entry to be unlawful, the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
Affirmed. The media's presence in the home violated the Fourth Amendment, but the officers received [[Qualified Immunity|qualified immunity]] because the right was not clearly established in April 1992.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Decided the same day as its [[Common Legal Terms#per-curiam|per curiam]] companion [[Hanlon v. Berger]], which applied the same Fourth Amendment holding and [[Qualified Immunity|qualified immunity]] to a media ride-along onto a ranch. *Wilson* is a leading application of the [[Harlow v. Fitzgerald]] "clearly established" standard. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Scope Manner and Related Issues]] — *Related (cross-doctrine)*

## Sources
- *Wilson v. Layne*, 526 U.S. 603 (1999) — https://www.courtlistener.com/opinion/118289/wilson-v-layne/ — pinpoints: 614, 615.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c6fea08efab2a250", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Wilson v. Layne"}, "payload": {"all": [{"cite": "526 U.S. 603", "page": "603", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "526"}, {"cite": "119 S. Ct. 1692", "page": "1692", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "119"}, {"cite": "143 L. Ed. 2d 818", "page": "818", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "143"}, {"cite": "1999 U.S. LEXIS 3633", "page": "3633", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1999"}], "display": "526 U.S. 603", "official": {"cite": "526 U.S. 603", "page": "603", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "526"}, "official_selection_present": true, "record_id": "Wilson v. Layne"}}
{"assertion_id": "4dc2f8f8adfb9b80", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-615", "record_id": "Wilson v. Layne"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-615", "pinpoint_status": "slip-only", "quote": "We hold that it was not unreasonable for a police officer in April 1992 to have believed that bringing media observers along during the execution of an arrest warrant (even in a home) was lawful.", "quote_fidelity": "mismatch", "record_id": "Wilson v. Layne", "star_marker": null}}
{"assertion_id": "54bbc7e366bc1527", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-614", "record_id": "Wilson v. Layne"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-614", "pinpoint_status": "slip-only", "quote": "--- # Wilson v. Layne *526 U.S. 603 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In April 1992, deputy U.S. Marshals and county deputies executing arrest warrants for Dominic Wilson invited a *Washington Post* reporter and photographer to accompany them into the home of Dominic's parents, Charles and Geraldine Wilson, during the early-morning entry. The parents were roused from bed; Charles Wilson, in his underwear, was subdued on the floor while the journalists observed and photographed (the photos were never published). Dominic was not there. The Wilsons sued the officers under *Bivens* and § 1983. ## Issue Whether police violate the Fourth Amendment by bringing media into a home during the execution of a warrant, and if so, whether the officers were entitled to qualified immunity. ## Rule Such a media intrusion violates the Fourth Amendment:", "quote_fidelity": "mismatch", "record_id": "Wilson v. Layne", "star_marker": null}}
{"assertion_id": "1ef214ed03e3fee6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Wilson v. Layne"}, "payload": {"as_of_content": "1999-05-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Wilson v. Layne", "scope_note": "Good law: media ride-along into a home during warrant execution violates the 4A; officers had QI on the then-undeveloped law.", "varies_by_point": false}}
```

### lake record — Wilson v. Layne

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wilson v. Layne",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wilson v. Layne",
    "case_name_short": "Wilson",
    "case_name_full": "WILSON Et Al. v. LAYNE, DEPUTY UNITED STATES MARSHAL, Et Al.",
    "input_case_name": "Wilson v. Layne",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-05-24",
    "year": 1999,
    "docket": "98-83",
    "cluster_id": 118289,
    "lead_opinion_id": 9433801,
    "sibling_ids": [
      118289,
      9433801,
      9433802
    ],
    "absolute_url": "/opinion/118289/wilson-v-layne/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "526 U.S. 603",
      "volume": "526",
      "reporter": "U.S.",
      "page": "603",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1692",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1692",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 818",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "818",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 3633",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3633",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "526 U.S. 603",
        "volume": "526",
        "reporter": "U.S.",
        "page": "603",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1692",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1692",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 818",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "818",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 3633",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3633",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "526 U.S. 603",
    "official_selection": {
      "court_class": "scotus",
      "selected": "526 U.S. 603",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-614",
      "page": null,
      "quote": "--- # Wilson v. Layne *526 U.S. 603 (1999)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In April 1992, deputy U.S. Marshals and county deputies executing arrest warrants for Dominic Wilson invited a *Washington Post* reporter and photographer to accompany them into the home of Dominic's parents, Charles and Geraldine Wilson, during the early-morning entry. The parents were roused from bed; Charles Wilson, in his underwear, was subdued on the floor while the journalists observed and photographed (the photos were never published). Dominic was not there. The Wilsons sued the officers under *Bivens* and \u00a7 1983. ## Issue Whether police violate the Fourth Amendment by bringing media into a home during the execution of a warrant, and if so, whether the officers were entitled to qualified immunity. ## Rule Such a media intrusion violates the Fourth Amendment:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-615",
      "page": null,
      "quote": "We hold that it was not unreasonable for a police officer in April 1992 to have believed that bringing media observers along during the execution of an arrest warrant (even in a home) was lawful.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-05-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wilson v. Layne",
    "varies_by_point": false,
    "scope_note": "Good law: media ride-along into a home during warrant execution violates the 4A; officers had QI on the then-undeveloped law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. City of Hous.",
          "cluster_id": 7329084,
          "cite": [
            "297 F. Supp. 3d 748"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Thompson, Jr. v. Commonwealth of Virginia",
          "cluster_id": 4452532,
          "cite": [
            "878 F.3d 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pirk",
          "cluster_id": 7327733,
          "cite": [
            "282 F. Supp. 3d 585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yee",
          "cluster_id": 3062319,
          "cite": [
            "177 So. 3d 72",
            "2015 Fla. App. LEXIS 15198",
            "2015 WL 5965213"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Quiroz v. Short",
          "cluster_id": 7311906,
          "cite": [
            "85 F. Supp. 3d 1092",
            "2015 WL 1395786",
            "2015 U.S. Dist. LEXIS 42278"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reichle v. Howards",
          "cluster_id": 801500,
          "cite": [
            "182 L. Ed. 2d 985",
            "132 S. Ct. 2088",
            "566 U.S. 658",
            "2012 U.S. LEXIS 4132"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hartman v. Moore",
          "cluster_id": 145662,
          "cite": [
            "164 L. Ed. 2d 441",
            "126 S. Ct. 1695",
            "547 U.S. 250",
            "2006 U.S. LEXIS 3450"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 2336338,
          "cite": [
            "68 S.W.3d 644",
            "2002 Tex. Crim. App. LEXIS 17",
            "2002 WL 122735"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keith A. Hill v. Borough of Kutztown and Gennaro Marino, Mayor of Kutztown, in His Individual and Official Capacity",
          "cluster_id": 795079,
          "cite": [
            "455 F.3d 225",
            "2006 U.S. App. LEXIS 18708",
            "98 Fair Empl. Prac. Cas. (BNA) 942",
            "2006 WL 2061145"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terri Vinyard v. Steve Wilson",
          "cluster_id": 76029,
          "cite": [
            "311 F.3d 1340",
            "2002 U.S. App. LEXIS 23576",
            "2002 WL 31521208"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony C. Greene v. Jack Barber, Edward Hillyer, Victor Gillis, William Hegarty, and the City of Grand Rapids, Michigan",
          "cluster_id": 779855,
          "cite": [
            "310 F.3d 889",
            "2002 U.S. App. LEXIS 23228",
            "2002 WL 31487268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Lee",
          "cluster_id": 7082005,
          "cite": [
            "227 F.3d 1214",
            "2000 Daily Journal DAR 10557",
            "2000 Cal. Daily Op. Serv. 7958",
            "2000 U.S. App. LEXIS 23778",
            "2000 WL 1407125"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cousins v. Lockyer",
          "cluster_id": 1459853,
          "cite": [
            "568 F.3d 1063",
            "2009 U.S. App. LEXIS 12708",
            "2009 WL 1652208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rubin Sira v. R. Morton, C. Artuz, D. Selsky, and G. Goord",
          "cluster_id": 787387,
          "cite": [
            "380 F.3d 57",
            "2004 WL 1837779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holloman Ex Rel. Holloman v. Harland",
          "cluster_id": 76571,
          "cite": [
            "370 F.3d 1252",
            "2004 WL 1178465"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118289 OR 9433801 OR 9433802) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDI3NzYwMDAwMDAwJnM9NzMxMTkwNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118289+OR+9433801+OR+9433802%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118289 OR 9433801 OR 9433802)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00ODEmcz0xNDYzMTcyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118289+OR+9433801+OR+9433802%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118289 OR 9433801 OR 9433802)",
        "reviewed": 53,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 53,
        "triage_read": 0,
        "triage_snippet_classified": 53
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118289 OR 9433801 OR 9433802)",
    "indexed_citing_opinions": 1451,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118289,
        "count": 1241,
        "count_source": "search"
      },
      {
        "opinion_id": 9433801,
        "count": 228,
        "count_source": "search"
      },
      {
        "opinion_id": 9433802,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2687,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wilson-v-layne.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTk3NzImcz0xMDEyNTAyMyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118289+OR+9433801+OR+9433802%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118289,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 109207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 110339,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 112594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 579234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 678500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 719620,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 724925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 748210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 752970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 1769461,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 2178648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 2281316,
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
    "date_created": "2026-07-06T04:29:07Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:29:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:29:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:33:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:29:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wilson v. Layne

```
<opinion type="majority">
<author id="b719-9">CHIEF Justice Rehnquist</author>
<p id="AMm8">delivered the opinion of the Court.</p>
<p id="b719-10">While executing an arrest warrant in a private home, police officers invited representatives of the media to accompany them. We hold that such a “media ride-along” does violate the Fourth Amendment, but that because the state <page-number citation-index="1" label="606">*606</page-number>of the law was not clearly established at the time the search in this ease took place, the officers are entitled to the defense of qualified immunity.</p>
<p id="b720-5">I</p>
<p id="b720-6">In early 1992, the Attorney General of the United States approved “Operation Gunsmoke,” a special national fugitive apprehension program in which United States Marshals worked with state and local police to apprehend dangerous criminals. The “Operation Gunsmoke” policy statement explained that the operation was to concentrate on “armed individuals wanted on federal and/or state and local warrants for serious drug and other violent felonies.” App. 15. This effective program ultimately resulted in over 3,000 arrests in 40 metropolitan areas. Brief for Federal Respondents Layne et al. 2.</p>
<p id="b720-7">One of the dangerous as “Operation Gunsmoke” was Dominic Wilson, the son of petitioners Charles and Geraldine Wilson. Dominic Wilson had violated his probation on previous felony charges of robbery, theft, and assault with intent to rob, and the police computer listed “caution indicators” that he was likely to be armed, to resist arrest, and to “assaul[t] police.” App. 40. The computer also listed his address as 909 North StoneStreet Avenue in Rockville, Maryland. Unknown to the police, this was actually the home of petitioners, Dominic Wilson’s parents. Thus, in April 1992, the Circuit Court for Montgomery County issued three arrest warrants for Dominic Wilson, one for each of his probation violations. The warrants were each addressed to “any duly authorized peace officer,” and commanded such officers to arrest him and bring him “immediately” before the Circuit Court to answer an indictment as to his probation violation. The warrants made no mention of media presence or assistance.<footnotemark>1</footnotemark></p>
<p id="b721-4"><page-number citation-index="1" label="607">*607</page-number>In the early morning hours of April 16,1992, a Gunsmoke team of Deputy United States Marshals and Montgomery County Police officers assembled to execute the Dominie Wilson warrants. The team was accompanied by a reporter and a photographer from the Washington Post, who had been invited by the Marshals to accompany them on their mission as part of a Marshals Service ride-along policy.</p>
<p id="b721-5">At around 6:45 a.m., the officers, with media representatives in tow, entered the dwelling at 909 North StoneStreet Avenue in the Lincoln Park neighborhood of Rockville. Petitioners Charles and Geraldine Wilson were still in bed when they heard the officers enter the home. Petitioner Charles Wilson, dressed only in a pair of briefs, ran into the living room to investigate. Discovering at least five men in street clothes with guns in his living room, he angrily demanded that they state their business, and repeatedly cursed the officers. Believing him to be an angry Dominic Wilson, the officers quickly subdued him on the floor. Geraldine Wilson next entered the living room to investigate, wearing only a nightgown. She observed her husband being restrained by the armed officers.</p>
<p id="b721-6">When their protective sweep was completed, the officers learned that Dominic Wilson was not in the house, and they departed. During the time that the officers were in the home, the Washington Post photographer took numerous pictures. The print reporter was also apparently in the living room observing the confrontation between the police and <page-number citation-index="1" label="608">*608</page-number>Charles Wilson. At no time, however, were the reporters involved in the execution of the arrest warrant. Brief for Federal Respondents Layne et al. 4. The Washington Post never published its photographs of the incident.</p>
<p id="b722-5">Petitioners sued the law enforcement personal capacities for money damages under <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971) (the U. S. Marshals Service respondents), and Rev. Stat. §1979, <span class="citation no-link">42 U. S. C. § 1983</span> (the Montgomery County Sheriff’s Department respondents). They contended that the officers’ actions in bringing members of the media to observe and record the attempted execution of the arrest warrant violated their Fourth Amendment rights. The District Court denied respondents’ motion for summary judgment on the basis of qualified immunity.</p>
<p id="b722-6">On interlocutory appeal to the Court of Appeals, a panel reversed and held that respondents were entitled to qualified immunity. The case was twice reheard en banc, where a divided Court of Appeals again upheld the defense of qualified immunity. The Court of Appeals declined to decide whether the actions of the police violated the Fourth Amendment. It concluded instead that because no court had held (at the time of the search) that media presence during a police entry into a residence violated the Fourth Amendment, the right allegedly violated by respondents was not “clearly established” and thus qualified immunity was proper. <span class="citation multiple-matches"><a href="/c/F.%203d/141/111/">141 F. 3d 111</a></span> (CA4 1998). Five judges dissented, arguing that the officers’ actions did violate the Fourth Amendment, and that the clearly established protections of the Fourth Amendment were violated in this case. <em>Id., </em>at 119 (opinion of Murnaghan, J.)</p>
<p id="b722-7">Recognizing a split <em>among </em>the Circuits on we granted certiorari in this case and another raising the same question, <em>Hanlon </em>v. <em>Berger, </em><span class="citation" data-id="9174292"><a href="/opinion/9179569/hanlon-v-berger/" aria-description="Citation for case: Hanlon v. Berger">525 U. S. 981</a></span> (1998), and now affirm the Court of Appeals, although by different reasoning.</p>
<p id="b723-8"><page-number citation-index="1" label="609">*609</page-number>I — H</p>
<p id="b723-3">Petitioners sued the federal officials under <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>and the state officials under §1983. Both <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>and §1983 allow a plaintiff to seek money damages from government officials who have violated his Fourth Amendment rights. See § 1983; <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#397" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of..."><em>Bivens, supra, </em>at 397</a></span>. But government officials performing discretionary functions generally are granted a qualified immunity and are “shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982).</p>
<p id="b723-4">Although this case involves suits under both §1983 and <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span>, </em>the qualified immunity analysis is identical under either cause of action. See, <em>e.g., Graham </em>v. <em>Connor, </em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 394, n. 9</a></span> (1989); <em>Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#340" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 340, n. 2</a></span> (1986). A court evaluating a claim of qualified immunity “must first determine whether the plaintiff has alleged the deprivation of an actual constitutional right at all, and if so, proceed to determine whether that right was clearly established at the time of the alleged violation.” <em>Conn </em>v. <em>Gabbert, ante, </em>at 290. This order of procedure is designed to “spare a defendant not only unwarranted liability, but unwarranted demands customarily imposed upon those defending a long drawn out lawsuit.” <em>Siegert </em>v. <em>Gilley, </em><span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/#232" aria-description="Citation for case: Siegert v. Gilley">500 U. S. 226, 232</a></span> (1991). Deciding the constitutional question before addressing the qualified immunity question also promotes clarity in the legal standards for official conduct, to the benefit of both the officers and the general public. See <em>County of Sacramento </em>v. <em>Lewis, </em><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#840" aria-description="Citation for case: County of Sacramento v. Lewis">523 U. S. 833, 840-842, n. 5</a></span> (1998). We now turn to the Fourth Amendment question.</p>
<p id="b723-5">In 1604, an English court made the now-famous observation that “the house of every one is to him as his castle and fortress, as well for his defence against injury and violence, as for his repose.” <em>Semayne’s Case, </em>5 Co. Rep. 91a, 91b, 77 <page-number citation-index="1" label="610">*610</page-number>Eng. Rep. 194, 195 (K. B.). In his Commentaries on the Laws of England, William Blaekstone noted that</p>
<blockquote id="b724-5">“the law of England has so particular and tender a regal’d to the immunity of a man’s house, that it stiles it his castle, and will never suffer it to be violated with impunity: agreeing herein with the sentiments of antient Rome .... For this reason no doors can in general be broken open to execute any civil process; though, in criminal causes, the public safety supersedes the private.” 4 Commentaries 223 (1765-1769).</blockquote>
<p id="b724-6">The Fourth Amendment embodies this centuries-old principle of respect for the privacy of the home: “The right of the people to be secure in their persons, <em>houses, </em>papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” U. S. Const., Arndt. 4 (emphasis added). See also <em>United States </em>v. <em>United States Dist. Court for Eastern Dist. of Mich., </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972) (“[FJhysical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed”).</p>
<p id="b724-7">Our decisions have applied these basic principles Fourth Amendment to situations, like the one in this case, in which police enter a home under the authority of an arrest warrant in order to take into custody the suspect named in the warrant. In <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 602</a></span> (1980), we noted that although clear in its protection of the home, the common-law tradition at the time of the drafting of the Fourth Amendment was ambivalent on the question whether police could enter a home without a warrant. We were ultimately persuaded that the “overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic” meant that absent a warrant or exigent circumstances, police could not <page-number citation-index="1" label="611">*611</page-number>enter a home to make an arrest. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#601" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 601</a></span>, 603-604: We decided that “an arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#603" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 603</a></span>.</p>
<p id="b725-4">Here, of course, the officers had such a warrant, and they were undoubtedly entitled to enter the Wilson home in order to execute the arrest warrant for Dominic Wilson. But it does not necessarily follow that they were entitled to bring a newspaper reporter and a photographer with them. In <em>Horton </em>v. <em>California, </em><span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#140" aria-description="Citation for case: Horton v. California">496 U. S. 128, 140</a></span> (1990), we held “[i]f the scope of the search exceeds that permitted by the terms of a validly issued warrant or the character of the relevant exception from the warrant requirement, the subsequent seizure is unconstitutional without more.” While this does not mean that every police action while inside a home must be explicitly authorized by the text of the warrant, see <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#705" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 705</a></span> (1981) (Fourth Amendment allows temporary detainer of homeowner while police search the home pursuant to warrant), the Fourth Amendment does require that police actions in execution of a warrant be related to the objectives of the authorized intrusion, see <em>Arizona </em>v. <em>Hicks, </em><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#325" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 325</a></span> (1987). See also <em>Maryland </em>v. <em>Garrison, </em><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#87" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 87</a></span> (1987) (“[T]he purposes justifying a police search strictly limit the permissible extent of the search”).</p>
<p id="b725-5">Certainly the presence of reporters inside the home was not related to the objectives of the authorized intrusion. Respondents concede that the reporters did not engage in the execution of the warrant, and did not assist the police in their task. The reporters therefore were not present for any reason related to the justification for police entry into the home — the apprehension of Dominic Wilson.</p>
<p id="b725-6">This is not a case in which the presence of the third parties directly aided in the execution of the warrant. Where the police enter a home under the authority of a warrant to <page-number citation-index="1" label="612">*612</page-number>search for stolen property, the presence of third parties for the purpose of identifying the stolen property has long been approved by this Court and our common-law tradition. See, <em>e. g., Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, 1067 (K. B. 1765) (in search for stolen goods ease, “Tt]he owner must swear that the goods are lodged in such a place. He must attend at the execution of the warrant to shew them to the officer, who must see that they answer the description”) (quoted with approval in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#628" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 628</a></span> (1886)).</p>
<p id="b726-5">Respondents argue presence Post reporters in the Wilsons’ home nonetheless served a number of legitimate law enforcement purposes. They first assert that officers should be able to exercise reasonable discretion about when it would “further their law enforcement mission to permit members of the news media to accompany them in executing a warrant.” Brief for Federal Respondents Layne et al. 15. But this claim ignores the importance of the right of residential privacy at the core of the Fourth Amendment. It may well be that media ride-alongs further the law enforcement objectives of the police in a general sense, but that is not the same as furthering the purposes of the search. Were such generalized “law enforcement objectives” themselves sufficient to trump the Fourth Amendment, the protections guaranteed by that Amendment’s text would be significantly watered down.</p>
<p id="b726-6">Respondents next argue presence could serve the law enforcement purpose of publicizing the government’s efforts to combat crime, and facilitate accurate reporting on law enforcement activities. There is certainly language in our opinions interpreting the First Amendment which points to the importance of “the press” in informing the general public about the administration of criminal justice. In <em>Cox Broadcasting Corp. </em>v. <em>Cohn, </em><span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#491" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S. 469, 491-492</a></span> (1975), for example, we said “in a society in which each individual has but limited time and resources with which to <page-number citation-index="1" label="613">*613</page-number>observe at first hand the operations of his government, he relies necessarily upon the press to bring to him in convenient form the facts of those operations.” See also <em>Richmond Newspapers, Inc. </em>v. <em>Virginia, </em><span class="citation" data-id="9428077"><a href="/opinion/110339/richmond-newspapers-inc-v-virginia/#572" aria-description="Citation for case: Richmond Newspapers, Inc. v. Virginia">448 U. S. 555, 572-573</a></span> (1980). No one could gainsay the truth of these observations, or the importance of the First Amendment in protecting press freedom from abridgment by the government. But the Fourth Amendment also protects a very important right, and in the present case it is in terms of that right that the media ride-alongs must be judged.</p>
<p id="b727-5">Surely the possibility of good public relations for the police is simply not enough, standing alone, to justify the ride-along intrusion into a private home. And even the need for accurate reporting on police issues in general bears no direct relation to the constitutional justification for the police intrusion into a home in order to execute a felony arrest warrant.</p>
<p id="b727-6">Finally, respondents argue that the presence of third parties could serve in some situations to minimize police abuses and protect suspects, and also to protect the safety of the officers. While it might be reasonable for police officers to themselves videotape home entries as part of a “quality control” effort to ensure that the rights of homeowners are being respected, or even to preserve evidence, cf. <em>Ohio </em>v. <em>Robinette, </em><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#35" aria-description="Citation for case: Ohio v. Robinette">519 U.S. 33, 35</a></span> (1996) (noting the use of a “mounted video camera” to record the details of a routine traffic stop), such a situation is significantly different from the media presence in this case. The Washington Post reporters in the Wilsons’ home were working on a story for their own purposes. They were not present for the purpose of protecting the officers, much less the Wilsons. A private photographer was acting for private purposes, as evidenced in part by the fact that the newspaper and not the police retained the photographs. Thus, although the presence of third parties during the execution of a warrant may in some circumstances be constitutionally permissible, see supra, at 611-612, the presence of these third parties was not.</p>
<p id="b728-6"><page-number citation-index="1" label="614">*614</page-number>The reasons advanced by respondents, taken in their entirety, fall short of justifying the presence of media inside a home. We hold that it is a violation of the Fourth Amendment for police to bring members of the media or other third parties into a home during the execution of a warrant when the presence of the third parties in the home was not in aid of the execution of the warrant.<footnotemark>2</footnotemark></p>
<p id="b728-7">HH</p>
<p id="b728-1">Since the police action in this ease violated petitioners Fourth Amendment right, we now must decide whether this right was clearly established at the time of the search. See <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/#232" aria-description="Citation for case: Siegert v. Gilley"><em>Siegert, 500 </em>U. S., at 232-233</a></span>. As noted above, Part II, <em>supra, </em>government officials performing discretionary functions generally are granted a qualified immunity and are “shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow </em>v. <em>Fitzgerald, 457 </em>U. S., at 818. What this means in practice is that “whether an official protected by qualified immunity may be held personally liable for an allegedly unlawful official action generally turns on the ‘objective legal reasonableness’ of the action, assessed in light of the legal rules that were ‘clearly established’ at the time it was taken.” <em>Anderson </em>v. <em>Creighton, </em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#639" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 639</a></span> (1987) (citing <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#819" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Harlow, supra, </em>at 819</a></span>); see also <em>Graham </em>v. <em>Connor, </em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#397" aria-description="Citation for case: Graham v. Connor">490 U. S., at 397</a></span>.</p>
<p id="b728-2">In <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Anderson</a></span>, </em>we explained that what “clearly established” means in this context depends largely “upon the level of generality at which the relevant ‘legal rule’ is to be identified.” <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#639" aria-description="Citation for case: Anderson v. Creighton">483 U. S., at 639</a></span>. “[Cjlearly established” for purposes of <page-number citation-index="1" label="615">*615</page-number>qualified immunity means that “[t]he contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right. This is not to say that an official action is protected by qualified immunity unless the very action in question has previously been held unlawful, but it is to say that in the light of preexisting law the unlawfulness must be apparent.” <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton"><em>Id., </em>at 640</a></span> (citations omitted); see also <em>United States </em>v. <em>Lanier, </em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#270" aria-description="Citation for case: United States v. Lanier">520 U. S. 259, 270</a></span> (1997).</p>
<p id="b729-5">It could plausibly be asserted that any violation of the Fourth Amendment is “clearly established,” since it is clearly established that the protections of the Fourth Amendment apply to the actions of police. Some variation of this theory of qualified immunity is urged upon us by petitioners, Brief for Petitioners 37, and seems to have been at the core of the dissenting opinion in the Court of Appeals, see 141 F. 3d, at 123. However, as we explained in <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Anderson</a></span>, </em>the right allegedly violated must be defined at the appropriate level of specificity before a court can determine if it was clearly established. <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton">483 U. S., at 641</a></span>. In this case, the appropriate question is the objective inquiry whether a reasonable officer could have believed that bringing members of the media into a home during the execution of an arrest warrant was lawful, in light of clearly established law and the information the officers possessed. Cf. <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">ibid.</a></span></em></p>
<p id="b729-6">a police officer in April 1992 to have believed that bringing media observers along during the execution of an arrest warrant (even in a home) was lawful. First, the constitutional question presented by this ease is by no means open and shut. The Fourth Amendment protects the rights of homeowners from entry without a warrant, but there was a warrant here. The question is whether the invitation to the media exceeded the scope of the search authorized by the warrant. Accurate media coverage of police activities serves an important public purpose, and it is not obvious from the general principles <page-number citation-index="1" label="616">*616</page-number>of the Fourth Amendment that the conduct of the officers in this case violated the Amendment.</p>
<p id="b730-5">Second, although media ride-alongs one had apparently become a common police practice,<footnotemark>3</footnotemark> in 1992 there were no judicial opinions holding that this practice became unlawful when it entered a home. The only published decision directly on point was a state intermediate court decision which, though it did not engage in an extensive Fourth Amendment analysis, nonetheless held that such conduct was not unreasonable. <em>Prahl </em>v. <em>Brosamle, </em><span class="citation" data-id="2178204"><a href="/opinion/2178204/bruheim-v-little/" aria-description="Citation for case: Bruheim v. Little">98 Wis. 2d 180</a></span>, 154—155, <span class="citation" data-id="2178648"><a href="/opinion/2178648/prahl-v-brosamle/#782" aria-description="Citation for case: Prahl v. Brosamle">295 N. W. 2d 768, 782</a></span> (App. 1980). From the federal courts, the parties have only identified two unpublished District Court decisions dealing with media entry into homes, each of which upheld the search on unorthodox non-Fourth Amendment right to privacy theories. <em>Moncrief </em>v. <em>Hanton, </em>10 Media L. Rptr. 1620 (ND <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#1984" aria-description="Citation for case: Ohio v. Robinette">Ohio 1984</a></span>); <em>Higbee </em>v. <em>Times-Advocate, </em>5 Media L. Rptr. 2372 (SD Cal. 1980). These cases, of course, cannot “clearly establish” that media entry into homes during a police ride-along violates the Fourth Amendment.</p>
<p id="b730-6">At a slightly higher level of <em>Bills </em>v. <em>Aseltine, </em><span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine">958 F. 2d 697</a></span> (CA6 1992), in which the Court of Appeals for the Sixth Circuit held that there were material issues of fact precluding summary judgment on the question whether police exceeded the scope of a search warrant by allowing a private security guard to participate in the search to identify stolen property other than that described in the warrant. <span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/#709" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine"><em>Id., </em>at 709</a></span>. <em><span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine">Bills</a></span>, </em>which was decided a mere five weeks before the events of this case, did anticipate today's holding that police may not bring along third parties during an entry into a private home pursuant <page-number citation-index="1" label="617">*617</page-number>to a warrant for purposes unrelated to those justifying the warrant. <span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/#706" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine"><em>Id., </em>at 706</a></span>. However, we cannot say that even in light of <em><span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine">Bills</a></span>, </em>the law on third-party entry into homes was clearly established in April 1992. Petitioners have not brought to our attention any eases of controlling authority in their jurisdiction at the time of the incident that clearly established the rule on which they seek to rely, nor have they identified a consensus of eases of persuasive authority such that a reasonable officer could not have believed that his actions were lawful.</p>
<p id="b731-5">Finally, important to our conclusion was the reliance by the United States marshals in this case on a Marshals Service ride-along policy that explicitly contemplated that media who engaged in ride-alongs might enter private homes with their cameras as part of fugitive apprehension arrests.<footnotemark>4</footnotemark> The Montgomery County Sheriff’s Department also at this time had a ride-along program that did not expressly prohibit media entry into private homes. Deposition of Sheriff Raymond M. Eight, in No. PJM-94-1718, p. 8. Such a policy, of course, could not make reasonable a belief that was contrary to a decided body of case law. But here the state of the law as to third parties accompanying police on home entries was at best undeveloped, and it was not unreasonable for law enforcement officers to look and rely on their formal ride-along policies.</p>
<p id="b731-6">Given such an undeveloped state of the law, the officers in this case cannot have been “expected to predict the future course of constitutional law.” <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#562" aria-description="Citation for case: Procunier v. Navarette">434 <page-number citation-index="1" label="618">*618</page-number>U. S. 555, 562</a></span> (1978). See also <em>Wood </em>v. Strickland, <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#321" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 321</a></span> (1975); <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#557" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 557</a></span> (1967). Between the time of the events of this case and today’s decision, a split among the Federal Circuits in fact developed on the question whether media ride-alongs that enter homes subject the police to <em>money </em>damages. See 141 F. 3d, at 118-119; <em>Ayeni </em>v. <em>Mottola, </em><span class="citation" data-id="678500"><a href="/opinion/678500/tawa-ayeni-v-james-mottola/" aria-description="Citation for case: Tawa Ayeni v. James Mottola">35 F. 3d 680</a></span> (CA2 1994), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./514/1062/">514 U. S. 1062</a></span> (1995); <em>Parker </em>v. <em>Boyer, </em><span class="citation multiple-matches"><a href="/c/F.%203d/93/445/">93 F. 3d 445</a></span> (CA8 1996), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./519/1148/">519 U. S. 1148</a></span> (1997); <em>Berger </em>v. <em>Hanlon, </em><span class="citation" data-id="6959019"><a href="/opinion/7055408/berger-v-hanlon/" aria-description="Citation for case: Berger v. Hanlon">129 F. 3d 505</a></span> (CA9 1997), cert. granted, <span class="citation multiple-matches"><a href="/c/U.%20S./525/981/">525 U. S. 981</a></span> (1998). If judges thus disagree on a constitutional question, it is unfair to subject police to money damages for picking the losing side of the controversy.</p>
<p id="b732-5">For the foregoing reasons,</p>
<p id="AoRV">Appeals is affirmed.</p>
<p id="b732-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b720-8"> The warrants were identical in all relevant respects. By way of example, one of them read as follows:</p>
<p id="b721-7"><page-number citation-index="1" label="607">*607</page-number>“The State of Maryland, to any duly authorized peace officer, greeting: you are hereby commanded to take Dominic Jerome Wilson if he/she shall be found in your bailiwick, and have him immediately before the Circuit Court for Montgomery County, now in session, at the Judicial Center, in Rockville, to answer an indictment, or information, or criminal appeals unto the State of Maryland, of and concerning a certain charge of Robbery [Violation of Probation] by him committed, as hath been presented, and so forth. Hereof fail not at your peril, and have you then and there this writ. Witness.” App. 36-37.</p>
</footnote>
<footnote label="2">
<p id="b728-3"> Even though such actions might violate the Fourth Amendment, if the police are lawfully present, the violation of the Fourth Amendment is the presence of the media and not the presence of the police in the home. We have no occasion here to decide whether the exclusionary rule would apply to any evidence discovered or developed by the media representatives.</p>
</footnote>
<footnote label="3">
<p id="b730-7"> See, <em>e. g., Florida Publishing Co. </em>v. <em>Fletcher, </em><span class="citation" data-id="1769461"><a href="/opinion/1769461/florida-pub-co-v-fletcher/#919" aria-description="Citation for case: Florida Pub. Co. v. Fletcher">340 So. 2d 914, 919</a></span> (1976) (it '“is a widespread practice of long-standing’” for media to accompany officers into homes), cert, denied, <span class="citation multiple-matches"><a href="/c/U.%20S./431/930/">431 U. S. 930</a></span> (1977); Zoglin, Live on the “Vice Beat, Time, Dec. 22, 1986, p. 60 (noting “the increasingly common practice of letting TV crews tag along on drug raids”).</p>
</footnote>
<footnote label="4">
<p id="b731-7"> A booklet distributed to marshals recommended that “fugitive apprehension cases . . . normally offer the best possibilities for ride-alongs.” App. 4-5. In its discussion of the best way to make ride-alongs useful to the media and portray the Marshals Service in a favorable light, the booklet noted that reporters were likely to want to be able to shoot “good action footage, not just a mop-up scene.” It advised agents that “[i]f the arrest is planned to take place inside a house or building, agree ahead of time on when the camera can enter and who will give the signal.” <em>Id., </em>at 7.</p>
</footnote>
</opinion>
```

---
