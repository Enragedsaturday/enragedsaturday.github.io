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

## GROUP: content/use-of-force-and-liability/Absolute Immunity.md  (`doctrine`, 5 assertions)

### content_page

```
---
weight: 50
title: "Absolute Immunity"
aliases:
  - "Absolute Immunity"
  - "10-use-of-force-liability/Absolute-Immunity"
  - "absolute-immunity"
  - "Prosecutorial Immunity"
topic: "Absolute immunity (functional approach)"
type: doctrine
jurisdiction: "Federal — 42 U.S.C. § 1983 defense; SCOTUS baseline"
status: draft
related:
  - "[[Qualified Immunity]]"
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Brady and Giglio]]"
---

# Absolute Immunity

*Was the defendant performing a function the common law shielded completely — or only acting as an investigator or witness's employer, where mere [[Qualified Immunity|qualified immunity]] applies?*

> [!rule] Black-letter rule
> **Absolute immunity attaches to a *function*, not an *office*.** A **prosecutor** is **absolutely immune** from § 1983 damages for conduct "**intimately associated with the judicial phase**" of the case (the advocacy function), *[[Imbler v. Pachtman|Imbler v. Pachtman]]*, 424 U.S. 409 (1976); a **witness** — including a **police officer** — is absolutely immune for **trial testimony**, *[[Briscoe v. LaHue|Briscoe v. LaHue]]*, 460 U.S. 325 (1983), and for **grand-jury testimony**, *[[Rehberg v. Paulk|Rehberg v. Paulk]]*, 566 U.S. 356 (2012). But the same actors get only **qualified** immunity when performing **investigative or administrative** functions. *[[Buckley v. Fitzsimmons|Buckley v. Fitzsimmons]]*, 509 U.S. 259 (1993).
> ^rule-absolute-immunity

## The Brief

**The functional approach, in one idea.** Whether an official gets **absolute** or merely **qualified** immunity (see [[Qualified Immunity]]) does **not** turn on the person's title. It turns on the **function** being performed. The common law gave complete protection to a handful of roles (the judge deciding, the prosecutor advocating, the witness testifying) because subjecting those functions to damages suits would distort the judicial process itself. Courts therefore ask a **function question**, not a **status question**, and the same person can hold absolute immunity for one act and only [[Qualified Immunity|qualified immunity]] for another.

**Prosecutors: absolute for advocacy, qualified for investigation.** A prosecutor is **absolutely immune** for activities "intimately associated with the judicial phase of the criminal process" (initiating a prosecution, presenting the State's case, and the advocacy decisions in between), even against an allegation of knowingly using false testimony. *[[Imbler v. Pachtman|Imbler v. Pachtman]]*, 424 U.S. 409 (1976). But when the prosecutor steps out of the advocate's role and acts as an **investigator or administrator** (for example, giving legal advice to police, holding a press conference, or fabricating evidence during the investigative phase before probable cause), the protection drops to **qualified** immunity. *[[Buckley v. Fitzsimmons|Buckley v. Fitzsimmons]]*, 509 U.S. 259 (1993). *[[Buckley v. Fitzsimmons|Buckley]]* is the case that makes the functional line concrete: same office, different function, different immunity.

**Witnesses: absolute at trial and before the grand jury.** A trial witness (including a **police officer**) cannot be sued under § 1983 for giving **testimony**, even allegedly perjurious testimony, because the remedy for perjury is prosecution, not a civil suit against the witness. *[[Briscoe v. LaHue|Briscoe v. LaHue]]*, 460 U.S. 325 (1983). That protection extends to a **grand-jury** witness, and a plaintiff may not evade it by recasting the testimony as part of a conspiracy. *[[Rehberg v. Paulk|Rehberg v. Paulk]]*, 566 U.S. 356 (2012). The limit tracks the same functional logic: immunity attaches to the act of **testifying**, not to everything the officer did in the case. A prosecutor who personally vouches for facts as a **complaining witness** (attesting to an affidavit) acts as a witness-declarant, not an advocate, and gets only **qualified** immunity for that act. *Kalina v. Fletcher*, 522 U.S. 118 (1997).

**Judges and legislators.** The same functional approach gives **judges** absolute immunity for **judicial acts** (even erroneous or malicious ones), losing it only for acts taken in the clear absence of all jurisdiction or for non-judicial administrative acts; **legislators** are absolutely immune for legislative acts. These are the functional siblings of prosecutorial and witness immunity, resting on the identical rationale: shield the core adjudicative and legislative functions, not the office-holder as such.

**The contrast that matters: absolute versus qualified.** Absolute immunity is a **complete bar** to the damages suit regardless of malice or the strength of the plaintiff's proof; the clearly-established-law inquiry never runs. [[Qualified Immunity|Qualified immunity]], by contrast, is **defeasible** — it yields to particularized, on-point precedent or an obvious case (see [[Qualified Immunity]]). Because absolute immunity is so powerful, the Court reads it **narrowly** and confines it to the protected function; the boundary between a prosecutor's **advocacy** and **investigative** roles is a recurring, closely watched fault line. *Price v. Montgomery County* drew a statement respecting the denial of [[Reading and Citing Cases#certiorari-cert|certiorari]] on exactly that seam.

**Burden and remedy.** The **official** invoking absolute immunity bears the burden of showing the challenged conduct was a **protected function** (the Court presumes qualified, not absolute, immunity is the norm and requires a strong historical and functional justification to go further). Where it applies, the consequence is dismissal: **no damages**, and the merits are never reached. Where the function is investigative, administrative, or complaining-witness conduct, the actor is left with **qualified** immunity, litigated on [[Qualified Immunity]].

**Common pitfalls.**
- **Asking about the office, not the function.** A prosecutor is not "absolutely immune" full stop; immunity follows the **advocacy** function and drops to qualified for **investigation** (*[[Buckley v. Fitzsimmons|Buckley]]*).
- **Assuming a police officer can never claim absolute immunity.** For **testimony** (trial or grand jury), the officer is a witness and is absolutely immune (*[[Briscoe v. LaHue|Briscoe]]*; *[[Rehberg v. Paulk|Rehberg]]*) — though only [[Qualified Immunity|qualified immunity]] covers the underlying investigation.
- **Trying to plead around witness immunity.** Recasting testimony as a "conspiracy" does not defeat it (*[[Rehberg v. Paulk|Rehberg]]*).
- **Confusing absolute with [[Qualified Immunity|qualified immunity]].** Absolute immunity is a complete bar with **no** clearly-established inquiry; [[Qualified Immunity|qualified immunity]] is defeasible (see [[Qualified Immunity]]).
- **Overlooking the complaining-witness line.** A prosecutor who personally attests to facts acts as a witness-declarant and gets only [[Qualified Immunity|qualified immunity]] for that act (*Kalina v. Fletcher*).

## Key cases

| Case | Holding | Opinion |
|---|---|---|
| *[[Imbler v. Pachtman]]*, 424 U.S. 409 (1976) | **Anchor.** A prosecutor is **absolutely immune** from § 1983 damages for conduct "intimately associated with the judicial phase"; the **advocacy** function. | [opinion](https://www.courtlistener.com/opinion/109387/imbler-v-pachtman/) |
| *[[Buckley v. Fitzsimmons]]*, 509 U.S. 259 (1993) | **Function, not office.** A prosecutor acting as an **investigator or administrator** (e.g., fabricating evidence before probable cause, or speaking to the press) gets only **qualified** immunity. | [opinion](https://www.courtlistener.com/opinion/112894/buckley-v-fitzsimmons/) |
| *[[Briscoe v. LaHue]]*, 460 U.S. 325 (1983) | **Witness immunity.** A trial witness (including a **police officer**) is **absolutely immune** from § 1983 liability for testimony, even if allegedly perjurious. | [opinion](https://www.courtlistener.com/opinion/110885/briscoe-v-lahue/) |
| *[[Rehberg v. Paulk]]*, 566 U.S. 356 (2012) | **Grand-jury witness.** Absolute immunity extends to **grand-jury** testimony, and a plaintiff cannot evade it by recasting the testimony as a conspiracy. | [opinion](https://www.courtlistener.com/opinion/626447/rehberg-v-paulk/) |

## Sources
- *Imbler v. Pachtman*, 424 U.S. 409 (1976) — https://www.courtlistener.com/opinion/109387/imbler-v-pachtman/
- *Buckley v. Fitzsimmons*, 509 U.S. 259 (1993) — https://www.courtlistener.com/opinion/112894/buckley-v-fitzsimmons/
- *Briscoe v. LaHue*, 460 U.S. 325 (1983) — https://www.courtlistener.com/opinion/110885/briscoe-v-lahue/
- *Rehberg v. Paulk*, 566 U.S. 356 (2012) — https://www.courtlistener.com/opinion/626447/rehberg-v-paulk/

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2a640396c8b70bd7", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Imbler v. Pachtman", "table_line": 35}, "payload": {"case": "Imbler v. Pachtman", "cells": ["*[[Imbler v. Pachtman]]*, 424 U.S. 409 (1976)", "**Anchor.** A prosecutor is **absolutely immune** from § 1983 damages for conduct \"intimately associated with the judicial phase\"; the **advocacy** function.", "[opinion](https://www.courtlistener.com/opinion/109387/imbler-v-pachtman/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "98f935831f90fbdb", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Buckley v. Fitzsimmons", "table_line": 36}, "payload": {"case": "Buckley v. Fitzsimmons", "cells": ["*[[Buckley v. Fitzsimmons]]*, 509 U.S. 259 (1993)", "**Function, not office.** A prosecutor acting as an **investigator or administrator** (e.g., fabricating evidence before probable cause, or speaking to the press) gets only **qualified** immunity.", "[opinion](https://www.courtlistener.com/opinion/112894/buckley-v-fitzsimmons/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "cc02f4232798f981", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Rehberg v. Paulk", "table_line": 38}, "payload": {"case": "Rehberg v. Paulk", "cells": ["*[[Rehberg v. Paulk]]*, 566 U.S. 356 (2012)", "**Grand-jury witness.** Absolute immunity extends to **grand-jury** testimony, and a plaintiff cannot evade it by recasting the testimony as a conspiracy.", "[opinion](https://www.courtlistener.com/opinion/626447/rehberg-v-paulk/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "ef2401824b7eef6e", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Briscoe v. LaHue", "table_line": 37}, "payload": {"case": "Briscoe v. LaHue", "cells": ["*[[Briscoe v. LaHue]]*, 460 U.S. 325 (1983)", "**Witness immunity.** A trial witness (including a **police officer**) is **absolutely immune** from § 1983 liability for testimony, even if allegedly perjurious.", "[opinion](https://www.courtlistener.com/opinion/110885/briscoe-v-lahue/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "38dca448ad328d65", "dimension": "support", "kind": "proposition", "locator": {"callout": "^rule-absolute-immunity"}, "payload": {"anchor": "^rule-absolute-immunity", "statement": "[!rule] Black-letter rule\n**Absolute immunity attaches to a *function*, not an *office*.** A **prosecutor** is **absolutely immune** from § 1983 damages for conduct \"**intimately associated with the judicial phase**\" of the case (the advocacy function), *[[Imbler v. Pachtman|Imbler v. Pachtman]]*, 424 U.S. 409 (1976); a **witness** — including a **police officer** — is absolutely immune for **trial testimony**, *[[Briscoe v. LaHue|Briscoe v. LaHue]]*, 460 U.S. 325 (1983), and for **grand-jury testimony**, *[[Rehberg v. Paulk|Rehberg v. Paulk]]*, 566 U.S. 356 (2012). But the same actors get only **qualified** immunity when performing **investigative or administrative** functions. *[[Buckley v. Fitzsimmons|Buckley v. Fitzsimmons]]*, 509 U.S. 259 (1993)."}}
```

### lake record — Briscoe v. LaHue

```json
{
  "schema_version": "s2.v1",
  "record_id": "Briscoe v. LaHue",
  "status": "under_review",
  "identity": {
    "case_name": "Briscoe v. LaHue",
    "case_name_short": "Briscoe",
    "case_name_full": "BRISCOE Et Al. v. LaHUE Et Al.",
    "input_case_name": "Briscoe v. LaHue",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-03-07",
    "year": 1983,
    "docket": "No. 81-1407",
    "cluster_id": 110885,
    "lead_opinion_id": 9429107,
    "sibling_ids": [],
    "absolute_url": "/opinion/110885/briscoe-v-lahue/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "460 U.S. 325",
      "volume": "460",
      "reporter": "U.S.",
      "page": "325",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1108",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1108",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 96",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "96",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4247",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4247",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 146",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "146",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "460 U.S. 325",
        "volume": "460",
        "reporter": "U.S.",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1108",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1108",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 96",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "96",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 146",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "146",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4247",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4247",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "460 U.S. 325",
    "official_selection": {
      "court_class": "scotus",
      "selected": "460 U.S. 325",
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
    "date_created": "2026-07-06T13:47:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:47:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:47:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "briscoe-v-lahue--110885",
      "to_record_id": "Briscoe v. LaHue",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### lake record — Buckley v. Fitzsimmons

```json
{
  "schema_version": "s2.v1",
  "record_id": "Buckley v. Fitzsimmons",
  "status": "under_review",
  "identity": {
    "case_name": "Buckley v. Fitzsimmons",
    "case_name_short": "Buckley",
    "case_name_full": "BUCKLEY v. FITZSIMMONS Et Al.",
    "input_case_name": "Buckley v. Fitzsimmons",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-06-24",
    "year": 1993,
    "docket": "No. 91-7849",
    "cluster_id": 112894,
    "lead_opinion_id": 9432862,
    "sibling_ids": [],
    "absolute_url": "/opinion/112894/buckley-v-fitzsimmons/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "509 U.S. 259",
      "volume": "509",
      "reporter": "U.S.",
      "page": "259",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "113 S. Ct. 2606",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2606",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 209",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "209",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 4400",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4400",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "509 U.S. 259",
        "volume": "509",
        "reporter": "U.S.",
        "page": "259",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 2606",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2606",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 209",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "209",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 4400",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4400",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "509 U.S. 259",
    "official_selection": {
      "court_class": "scotus",
      "selected": "509 U.S. 259",
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
    "date_created": "2026-07-06T13:53:46Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "buckley-v-fitzsimmons--112894",
      "to_record_id": "Buckley v. Fitzsimmons",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

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

### lake record — Rehberg v. Paulk

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rehberg v. Paulk",
  "status": "under_review",
  "identity": {
    "case_name": "Rehberg v. Paulk",
    "case_name_short": "Rehberg",
    "case_name_full": "Rehberg v. Paulk",
    "input_case_name": "Rehberg v. Paulk",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-04-02",
    "year": 2012,
    "docket": "No. 10-788",
    "cluster_id": 626447,
    "lead_opinion_id": 626447,
    "sibling_ids": [],
    "absolute_url": "/opinion/626447/rehberg-v-paulk/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "566 U.S. 356",
      "volume": "566",
      "reporter": "U.S.",
      "page": "356",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 1497",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 593",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "593",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 2711",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "2711",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 1497",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 593",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "593",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "566 U.S. 356",
        "volume": "566",
        "reporter": "U.S.",
        "page": "356",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 2711",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "2711",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "566 U.S. 356",
    "official_selection": {
      "court_class": "scotus",
      "selected": "566 U.S. 356",
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
    "date_created": "2026-07-06T13:47:34Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "rehberg-v-paulk--626447",
      "to_record_id": "Rehberg v. Paulk",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

---

## GROUP: content/use-of-force-and-liability/Civil Asset Forfeiture.md  (`doctrine`, 9 assertions)

### content_page

```
---
weight: 80
title: "Civil Asset Forfeiture"
aliases:
  - "Civil Asset Forfeiture"
  - "10-use-of-force-liability/Civil-Asset-Forfeiture"
  - "civil-asset-forfeiture"
  - "Excessive Fines"
topic: "Civil asset forfeiture and its constitutional limits"
type: doctrine
jurisdiction: "Federal — U.S. Const. amends. IV, V, VIII; SCOTUS baseline"
status: draft
related:
  - "[[Seizure of Property]]"
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[The Exclusionary Rule]]"
---

# Civil Asset Forfeiture

*The government wants to keep property tied to crime through a civil in rem action — what constitutional limits apply?*

> [!rule] Black-letter rule
> **Civil in rem forfeiture** (a suit against the *property*, not the owner) of assets connected to crime is constrained on three fronts: (1) the **Eighth Amendment's Excessive Fines Clause** — a punitive forfeiture may not be **grossly disproportional** to the gravity of the offense, and the Clause is **incorporated** against the States; (2) **procedural due process** — notice, a hearing, and timeliness; and (3) it is **not** limited by any constitutionally required **innocent-owner defense** (statutes may supply one, but the Constitution does not). *[[Austin v. United States|Austin v. United States]]*, 509 U.S. 602 (1993); *[[United States v. Bajakajian|United States v. Bajakajian]]*, 524 U.S. 321 (1998); *[[Timbs v. Indiana|Timbs v. Indiana]]*, 586 U.S. 146 (2019).
> ^rule-civil-forfeiture

## The Brief

**What civil forfeiture is.** In a **civil in rem** forfeiture, the government proceeds against the **property itself** on the legal fiction that the thing is "guilty" of facilitating crime, so it need not convict (or even charge) the owner. That structure is what makes the constitutional limits matter: the protections come from the **Eighth Amendment**, **procedural due process**, and (by statute, not the Constitution) an **innocent-owner** defense. The initial seizure of the property is a Fourth Amendment event (see [[Seizure of Property]]); this page is about **keeping** it.

### Excessive Fines (Eighth Amendment)

**Forfeiture that punishes is a "fine."** Civil in rem forfeiture is subject to the **Excessive Fines Clause** when it serves in part to **punish**, rather than being purely remedial. *[[Austin v. United States|Austin v. United States]]*, 509 U.S. 602 (1993). The operative limit is **gross disproportionality**: a punitive forfeiture is unconstitutional if the amount is **grossly disproportional to the gravity of the offense**. *[[United States v. Bajakajian|United States v. Bajakajian]]*, 524 U.S. 321 (1998) (striking the forfeiture of $357,144 for failing to **report** transporting currency — the first forfeiture the Court held excessive). And the Clause is **incorporated** against the States through the Fourteenth Amendment, so state and local forfeitures are bound by it too. *[[Timbs v. Indiana|Timbs v. Indiana]]*, 586 U.S. 146 (2019) (forfeiture of a $42,000 Land Rover for a low-level drug sale). Together these set the proportionality ceiling on both federal and state forfeitures.

### Procedural due process

**Real property gets pre-seizure process; timeliness is judged flexibly.** Absent **[[Exigent Circumstances and Hot Pursuit|exigent circumstances]]**, the government must give **notice and a hearing before seizing real property** for forfeiture, because a home cannot abscond. *[[United States v. James Daniel Good Real Property|United States v. James Daniel Good Real Property]]*, 510 U.S. 43 (1993) (contrast the movable-property rule of *Calero-Toledo v. Pearson Yacht Leasing Co.*, 416 U.S. 663 (1974), where a boat's mobility justified seizure without prior notice). The **timeliness** of the government's forfeiture action is measured by the **speedy-trial balancing factors** (length of and reason for delay, the claimant's assertion of rights, and prejudice), not a fixed deadline. *[[United States v. $8,850 in Currency|United States v. $8,850]]*, 461 U.S. 555 (1983). There is no separate constitutional right to a speedy ruling on an administrative **remission** petition; the forfeiture proceeding itself supplies the process due. *[[United States v. Von Neumann|United States v. Von Neumann]]*, 474 U.S. 242 (1986). Most recently, due process does **not** require a separate **preliminary hearing** on the **timeliness** of a civil forfeiture; the claimant's remedy is a timely forfeiture proceeding, tested by those same balancing factors. *[[Culley v. Marshall|Culley v. Marshall]]*, 601 U.S. 377 (2024).

### The innocent owner

**The Constitution does not require an innocent-owner defense.** An owner's **lack of knowledge** that her property was used for crime does **not**, by itself, bar forfeiture. *[[Bennis v. Michigan|Bennis v. Michigan]]*, 516 U.S. 442 (1996) (forfeiting a wife's interest in a car her husband used to solicit prostitution). Many forfeiture statutes now **provide** an innocent-owner defense (federal forfeiture does, by statute), but *[[Bennis v. Michigan|Bennis]]* holds that the **Constitution** does not compel one. The teaching point: the protection an innocent owner enjoys usually comes from the **statute**, and its scope is a statutory question, not a constitutional guarantee.

**Common pitfalls.**
- **Assuming a conviction is required.** Civil in rem forfeiture proceeds against the **property** and needs no conviction of the owner.
- **Ignoring the Excessive Fines ceiling.** A punitive forfeiture grossly disproportional to the offense is unconstitutional (*[[United States v. Bajakajian|Bajakajian]]*), in state courts too (*[[Timbs v. Indiana|Timbs]]*).
- **Seizing real property without pre-seizure process.** Absent [[Exigent Circumstances and Hot Pursuit|exigency]], notice and a hearing come first (*[[United States v. James Daniel Good Real Property|James Daniel Good]]*).
- **Expecting a constitutional innocent-owner defense.** *[[Bennis v. Michigan|Bennis]]* holds there is none; look to the **statute**.
- **Demanding a separate early hearing on timeliness.** *[[Culley v. Marshall|Culley]]* rejects a preliminary-hearing requirement; the forfeiture proceeding itself is the process due.

## Key cases

| Case | Holding | Opinion |
|---|---|---|
| *[[Austin v. United States]]*, 509 U.S. 602 (1993) | **Excessive Fines applies.** Civil in rem forfeiture is subject to the Eighth Amendment's Excessive Fines Clause when it functions as **punishment**. | [opinion](https://www.courtlistener.com/opinion/112904/austin-v-united-states/) |
| *[[United States v. Bajakajian]]*, 524 U.S. 321 (1998) | **Gross disproportionality.** A punitive forfeiture is excessive if **grossly disproportional** to the gravity of the offense; the first forfeiture struck down on that ground. | [opinion](https://www.courtlistener.com/opinion/118234/united-states-v-bajakajian/) |
| *[[Timbs v. Indiana]]*, 586 U.S. 146 (2019) | **Incorporation.** The Excessive Fines Clause is **incorporated** against the States, so state and local forfeitures are bound by the proportionality limit. | [opinion](https://www.courtlistener.com/opinion/4591916/timbs-v-indiana/) |
| *[[United States v. James Daniel Good Real Property]]*, 510 U.S. 43 (1993) | **Pre-seizure process.** Absent [[Exigent Circumstances and Hot Pursuit\|exigent circumstances]], the government must give **notice and a hearing before seizing real property** for forfeiture. | [opinion](https://www.courtlistener.com/opinion/112914/united-states-v-james-daniel-good-real-property/) |
| *[[United States v. $8,850 in Currency]]*, 461 U.S. 555 (1983) | **Timeliness.** Whether a delay in filing a forfeiture violates due process is judged by the **speedy-trial balancing factors**, not a fixed deadline. | [opinion](https://www.courtlistener.com/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/) |
| *[[United States v. Von Neumann]]*, 474 U.S. 242 (1986) | **Remission.** No separate due-process right to a speedy ruling on a **remission** petition; the forfeiture proceeding supplies the process due. | [opinion](https://www.courtlistener.com/opinion/111551/united-states-v-von-neumann/) |
| *[[Culley v. Marshall]]*, 601 U.S. 377 (2024) | **No preliminary hearing.** Due process does **not** require a separate preliminary hearing on the timeliness of a civil forfeiture. | [opinion](https://www.courtlistener.com/opinion/10600097/culley-v-marshall/) |
| *[[Bennis v. Michigan]]*, 516 U.S. 442 (1996) | **No constitutional innocent-owner defense.** An owner's lack of knowledge of the property's criminal use does not, by itself, bar forfeiture. | [opinion](https://www.courtlistener.com/opinion/118005/bennis-v-michigan/) |

## Sources
- *Austin v. United States*, 509 U.S. 602 (1993) — https://www.courtlistener.com/opinion/112904/austin-v-united-states/
- *United States v. Bajakajian*, 524 U.S. 321 (1998) — https://www.courtlistener.com/opinion/118234/united-states-v-bajakajian/
- *Timbs v. Indiana*, 586 U.S. 146 (2019) — https://www.courtlistener.com/opinion/4591916/timbs-v-indiana/
- *United States v. James Daniel Good Real Property*, 510 U.S. 43 (1993) — https://www.courtlistener.com/opinion/112914/united-states-v-james-daniel-good-real-property/
- *United States v. $8,850 in Currency*, 461 U.S. 555 (1983) — https://www.courtlistener.com/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/
- *United States v. Von Neumann*, 474 U.S. 242 (1986) — https://www.courtlistener.com/opinion/111551/united-states-v-von-neumann/
- *Culley v. Marshall*, 601 U.S. 377 (2024) — https://www.courtlistener.com/opinion/10600097/culley-v-marshall/
- *Bennis v. Michigan*, 516 U.S. 442 (1996) — https://www.courtlistener.com/opinion/118005/bennis-v-michigan/
- *Calero-Toledo v. Pearson Yacht Leasing Co.*, 416 U.S. 663 (1974) — https://www.courtlistener.com/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "83d901412cb23e89", "dimension": "existence", "kind": "case_cite", "locator": {"case": "United States v. Von Neumann", "table_line": 42}, "payload": {"case": "United States v. Von Neumann", "cells": ["*[[United States v. Von Neumann]]*, 474 U.S. 242 (1986)", "**Remission.** No separate due-process right to a speedy ruling on a **remission** petition; the forfeiture proceeding supplies the process due.", "[opinion](https://www.courtlistener.com/opinion/111551/united-states-v-von-neumann/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "87049e68e8d62859", "dimension": "existence", "kind": "case_cite", "locator": {"case": "United States v. James Daniel Good Real Property", "table_line": 40}, "payload": {"case": "United States v. James Daniel Good Real Property", "cells": ["*[[United States v. James Daniel Good Real Property]]*, 510 U.S. 43 (1993)", "**Pre-seizure process.** Absent [[Exigent Circumstances and Hot Pursuit\\|exigent circumstances]], the government must give **notice and a hearing before seizing real property** for forfeiture.", "[opinion](https://www.courtlistener.com/opinion/112914/united-states-v-james-daniel-good-real-property/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "9607e7a04ab1f48c", "dimension": "existence", "kind": "case_cite", "locator": {"case": "United States v. $8,850 in Currency", "table_line": 41}, "payload": {"case": "United States v. $8,850 in Currency", "cells": ["*[[United States v. $8,850 in Currency]]*, 461 U.S. 555 (1983)", "**Timeliness.** Whether a delay in filing a forfeiture violates due process is judged by the **speedy-trial balancing factors**, not a fixed deadline.", "[opinion](https://www.courtlistener.com/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "9e6f599b7c69b121", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Culley v. Marshall", "table_line": 43}, "payload": {"case": "Culley v. Marshall", "cells": ["*[[Culley v. Marshall]]*, 601 U.S. 377 (2024)", "**No preliminary hearing.** Due process does **not** require a separate preliminary hearing on the timeliness of a civil forfeiture.", "[opinion](https://www.courtlistener.com/opinion/10600097/culley-v-marshall/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "add1e41edd0bb956", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Austin v. United States", "table_line": 37}, "payload": {"case": "Austin v. United States", "cells": ["*[[Austin v. United States]]*, 509 U.S. 602 (1993)", "**Excessive Fines applies.** Civil in rem forfeiture is subject to the Eighth Amendment's Excessive Fines Clause when it functions as **punishment**.", "[opinion](https://www.courtlistener.com/opinion/112904/austin-v-united-states/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "cf440ab27ebba1ca", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Timbs v. Indiana", "table_line": 39}, "payload": {"case": "Timbs v. Indiana", "cells": ["*[[Timbs v. Indiana]]*, 586 U.S. 146 (2019)", "**Incorporation.** The Excessive Fines Clause is **incorporated** against the States, so state and local forfeitures are bound by the proportionality limit.", "[opinion](https://www.courtlistener.com/opinion/4591916/timbs-v-indiana/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "f412f49edf3a5bde", "dimension": "existence", "kind": "case_cite", "locator": {"case": "United States v. Bajakajian", "table_line": 38}, "payload": {"case": "United States v. Bajakajian", "cells": ["*[[United States v. Bajakajian]]*, 524 U.S. 321 (1998)", "**Gross disproportionality.** A punitive forfeiture is excessive if **grossly disproportional** to the gravity of the offense; the first forfeiture struck down on that ground.", "[opinion](https://www.courtlistener.com/opinion/118234/united-states-v-bajakajian/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "fe2f1392dd12ebd3", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Bennis v. Michigan", "table_line": 44}, "payload": {"case": "Bennis v. Michigan", "cells": ["*[[Bennis v. Michigan]]*, 516 U.S. 442 (1996)", "**No constitutional innocent-owner defense.** An owner's lack of knowledge of the property's criminal use does not, by itself, bar forfeiture.", "[opinion](https://www.courtlistener.com/opinion/118005/bennis-v-michigan/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "1797626fa7d2ab96", "dimension": "support", "kind": "proposition", "locator": {"callout": "^rule-civil-forfeiture"}, "payload": {"anchor": "^rule-civil-forfeiture", "statement": "[!rule] Black-letter rule\n**Civil in rem forfeiture** (a suit against the *property*, not the owner) of assets connected to crime is constrained on three fronts: (1) the **Eighth Amendment's Excessive Fines Clause** — a punitive forfeiture may not be **grossly disproportional** to the gravity of the offense, and the Clause is **incorporated** against the States; (2) **procedural due process** — notice, a hearing, and timeliness; and (3) it is **not** limited by any constitutionally required **innocent-owner defense** (statutes may supply one, but the Constitution does not). *[[Austin v. United States|Austin v. United States]]*, 509 U.S. 602 (1993); *[[United States v. Bajakajian|United States v. Bajakajian]]*, 524 U.S. 321 (1998); *[[Timbs v. Indiana|Timbs v. Indiana]]*, 586 U.S. 146 (2019)."}}
```

### lake record — Austin v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Austin v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Austin v. United States",
    "case_name_short": "Austin",
    "case_name_full": "Austin v. United States",
    "input_case_name": "Austin v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-06-28",
    "year": 1993,
    "docket": "92-6073",
    "cluster_id": 112904,
    "lead_opinion_id": 9432892,
    "sibling_ids": [],
    "absolute_url": "/opinion/112904/austin-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "509 U.S. 602",
      "volume": "509",
      "reporter": "U.S.",
      "page": "602",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "113 S. Ct. 2801",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 488",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 4407",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4407",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 224465",
        "volume": "1993",
        "reporter": "WL",
        "page": "224465",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "509 U.S. 602",
        "volume": "509",
        "reporter": "U.S.",
        "page": "602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 2801",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 488",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 4407",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4407",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 224465",
        "volume": "1993",
        "reporter": "WL",
        "page": "224465",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "509 U.S. 602",
    "official_selection": {
      "court_class": "scotus",
      "selected": "509 U.S. 602",
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
    "date_created": "2026-07-07T13:22:16Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "austin-v-united-states--112904",
      "to_record_id": "Austin v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### lake record — Bennis v. Michigan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bennis v. Michigan",
  "status": "under_review",
  "identity": {
    "case_name": "Bennis v. Michigan",
    "case_name_short": "Bennis",
    "case_name_full": "Bennis v. Michigan",
    "input_case_name": "Bennis v. Michigan",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-03-04",
    "year": 1996,
    "docket": "94-8729",
    "cluster_id": 118005,
    "lead_opinion_id": 9433258,
    "sibling_ids": [],
    "absolute_url": "/opinion/118005/bennis-v-michigan/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "516 U.S. 442",
      "volume": "516",
      "reporter": "U.S.",
      "page": "442",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 994",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "134 L. Ed. 2d 68",
        "volume": "134",
        "reporter": "L. Ed. 2d",
        "page": "68",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 1565",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "1565",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "516 U.S. 442",
        "volume": "516",
        "reporter": "U.S.",
        "page": "442",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 994",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "134 L. Ed. 2d 68",
        "volume": "134",
        "reporter": "L. Ed. 2d",
        "page": "68",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 1565",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "1565",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "516 U.S. 442",
    "official_selection": {
      "court_class": "scotus",
      "selected": "516 U.S. 442",
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
    "date_created": "2026-07-07T13:24:15Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:24:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:24:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:24:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:24:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "bennis-v-michigan--118005",
      "to_record_id": "Bennis v. Michigan",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### lake record — Culley v. Marshall

```json
{
  "schema_version": "s2.v1",
  "record_id": "Culley v. Marshall",
  "status": "under_review",
  "identity": {
    "case_name": "Culley v. Marshall",
    "case_name_short": "Culley",
    "case_name_full": "",
    "input_case_name": "Culley v. Marshall",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2024,
    "docket": "22-585",
    "cluster_id": 10600097,
    "lead_opinion_id": 11066685,
    "sibling_ids": [],
    "absolute_url": "/opinion/10600097/culley-v-marshall/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "601 U.S. 377",
      "volume": "601",
      "reporter": "U.S.",
      "page": "377",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "601 U.S. 377",
        "volume": "601",
        "reporter": "U.S.",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "601 U.S. 377",
    "official_selection": {
      "court_class": "scotus",
      "selected": "601 U.S. 377",
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
    "date_created": "2026-07-06T12:11:55Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "culley-v-marshall--10600097",
      "to_record_id": "Culley v. Marshall",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### lake record — Timbs v. Indiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Timbs v. Indiana",
  "status": "under_review",
  "identity": {
    "case_name": "Timbs v. Indiana",
    "case_name_short": "Timbs",
    "case_name_full": "Tyson TIMBS, Petitioner v. INDIANA",
    "input_case_name": "Timbs v. Indiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2019-02-20",
    "year": 2019,
    "docket": "No. 17-1091",
    "cluster_id": 4591916,
    "lead_opinion_id": 9888039,
    "sibling_ids": [],
    "absolute_url": "/opinion/4591916/timbs-v-indiana/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "586 U.S. 146",
      "volume": "586",
      "reporter": "U.S.",
      "page": "146",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "139 S. Ct. 682",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "203 L. Ed. 2d 11",
        "volume": "203",
        "reporter": "L. Ed. 2d",
        "page": "11",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2019 U.S. LEXIS 1350",
        "volume": "2019",
        "reporter": "U.S. LEXIS",
        "page": "1350",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "586 U.S. 146",
        "volume": "586",
        "reporter": "U.S.",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 S. Ct. 682",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2019 U.S. LEXIS 1350",
        "volume": "2019",
        "reporter": "U.S. LEXIS",
        "page": "1350",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "203 L. Ed. 2d 11",
        "volume": "203",
        "reporter": "L. Ed. 2d",
        "page": "11",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "586 U.S. 146",
    "official_selection": {
      "court_class": "scotus",
      "selected": "586 U.S. 146",
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
    "date_created": "2026-07-06T13:41:50Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "timbs-v-indiana--4591916",
      "to_record_id": "Timbs v. Indiana",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### lake record — United States v. $8,850 in Currency

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. $8,850 in Currency",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Eight Thousand Eight Hundred & Fifty Dollars",
    "case_name_short": "$8,850",
    "case_name_full": "United States v. Eight Thousand Eight Hundred and Fifty Dollars ($8,850) in United States Currency",
    "input_case_name": "United States v. $8,850 in Currency",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-05-23",
    "year": 1983,
    "docket": "No. 81-1062",
    "cluster_id": 110936,
    "lead_opinion_id": 9429199,
    "sibling_ids": [],
    "absolute_url": "/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "461 U.S. 555",
      "volume": "461",
      "reporter": "U.S.",
      "page": "555",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2005",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2005",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 143",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4587",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4587",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 34",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "461 U.S. 555",
        "volume": "461",
        "reporter": "U.S.",
        "page": "555",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2005",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2005",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 143",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 34",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4587",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4587",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "461 U.S. 555",
    "official_selection": {
      "court_class": "scotus",
      "selected": "461 U.S. 555",
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
    "date_created": "2026-07-06T13:41:57Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-8-850-in-currency--110936",
      "to_record_id": "United States v. $8,850 in Currency",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### lake record — United States v. Bajakajian

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Bajakajian",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Bajakajian",
    "case_name_short": "Bajakajian",
    "case_name_full": "United States v. Bajakajian",
    "input_case_name": "United States v. Bajakajian",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-06-22",
    "year": 1998,
    "docket": "No. 96-1487",
    "cluster_id": 118234,
    "lead_opinion_id": 9433683,
    "sibling_ids": [],
    "absolute_url": "/opinion/118234/united-states-v-bajakajian/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "524 U.S. 321",
      "volume": "524",
      "reporter": "U.S.",
      "page": "321",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 2028",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "2028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 L. Ed. 2d 314",
        "volume": "141",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 4172",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "4172",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "524 U.S. 321",
        "volume": "524",
        "reporter": "U.S.",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 2028",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "2028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 L. Ed. 2d 314",
        "volume": "141",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 4172",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "4172",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "524 U.S. 321",
    "official_selection": {
      "court_class": "scotus",
      "selected": "524 U.S. 321",
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
    "date_created": "2026-07-06T13:16:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-bajakajian--118234",
      "to_record_id": "United States v. Bajakajian",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### lake record — United States v. James Daniel Good Real Property

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. James Daniel Good Real Property",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. James Daniel Good Real Property",
    "case_name_short": "James Daniel Good ",
    "case_name_full": "UNITED STATES v. JAMES DANIEL GOOD REAL PROPERTY Et Al.",
    "input_case_name": "United States v. James Daniel Good Real Property",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-12-13",
    "year": 1993,
    "docket": "No. 92-1180",
    "cluster_id": 112914,
    "lead_opinion_id": 9432907,
    "sibling_ids": [],
    "absolute_url": "/opinion/112914/united-states-v-james-daniel-good-real-property/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "510 U.S. 43",
      "volume": "510",
      "reporter": "U.S.",
      "page": "43",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "114 S. Ct. 492",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 L. Ed. 2d 490",
        "volume": "126",
        "reporter": "L. Ed. 2d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "7 Fla. L. Weekly Fed. S 665",
        "volume": "7",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "665",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Daily Journal DAR 15706",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "15706",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "62 U.S.L.W. 4013",
        "volume": "62",
        "reporter": "U.S.L.W.",
        "page": "4013",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 7941",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "7941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Cal. Daily Op. Serv. 9143",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 505539",
        "volume": "1993",
        "reporter": "WL",
        "page": "505539",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "510 U.S. 43",
        "volume": "510",
        "reporter": "U.S.",
        "page": "43",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 492",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 L. Ed. 2d 490",
        "volume": "126",
        "reporter": "L. Ed. 2d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 7941",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "7941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "7 Fla. L. Weekly Fed. S 665",
        "volume": "7",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "665",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Daily Journal DAR 15706",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "15706",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Cal. Daily Op. Serv. 9143",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "62 U.S.L.W. 4013",
        "volume": "62",
        "reporter": "U.S.L.W.",
        "page": "4013",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 505539",
        "volume": "1993",
        "reporter": "WL",
        "page": "505539",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "510 U.S. 43",
    "official_selection": {
      "court_class": "scotus",
      "selected": "510 U.S. 43",
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
    "date_created": "2026-07-06T13:16:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-james-daniel-good-real-property--112914",
      "to_record_id": "United States v. James Daniel Good Real Property",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### lake record — United States v. Von Neumann

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Von Neumann",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Von Neumann",
    "case_name_short": "Von Neumann",
    "case_name_full": "United States v. Von Neumann",
    "input_case_name": "United States v. Von Neumann",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-01-14",
    "year": 1986,
    "docket": "No. 84-1144",
    "cluster_id": 111551,
    "lead_opinion_id": 9430249,
    "sibling_ids": [],
    "absolute_url": "/opinion/111551/united-states-v-von-neumann/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "474 U.S. 242",
      "volume": "474",
      "reporter": "U.S.",
      "page": "242",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 610",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 2d 587",
        "volume": "88",
        "reporter": "L. Ed. 2d",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4065",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 39",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "39",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "474 U.S. 242",
        "volume": "474",
        "reporter": "U.S.",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 610",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 2d 587",
        "volume": "88",
        "reporter": "L. Ed. 2d",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 39",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "39",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4065",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "474 U.S. 242",
    "official_selection": {
      "court_class": "scotus",
      "selected": "474 U.S. 242",
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
    "date_created": "2026-07-06T13:41:55Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-von-neumann--111551",
      "to_record_id": "United States v. Von Neumann",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

---
