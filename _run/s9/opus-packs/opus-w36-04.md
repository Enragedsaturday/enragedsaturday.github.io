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

## GROUP: content/cases/Saucier v. Katz.md  (`case`, 6 assertions)

### content_page

```
---
title: "Saucier v. Katz"
type: case
citation: "533 U.S. 194 (2001)"
parallel_cite: "121 S. Ct. 2151; 150 L. Ed. 2d 272"
neutral_cite: 2001 U.S. LEXIS 4664
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-06-18
docket: 99-1977
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 2001-06-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Saucier v. Katz
  varies_by_point: true
  scope_note: "Pearson v. Callahan (2009) held that Saucier's two-step sequence is no longer mandatory; Saucier's two-part qualified-immunity test survives."
  point_overrides:
    - point: legacy-limited-saucier-v-katz
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Pearson v. Callahan
          cluster_id: 145918
          cite: 555 U.S. 223
          field_ii: limited
      scope_note: "Pearson v. Callahan (2009) held that Saucier's two-step sequence is no longer mandatory; Saucier's two-part qualified-immunity test survives."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118449/saucier-v-katz-et-al/"
  cluster_id: 118449
  opinion_id: 118449
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Pearson v. Callahan]]", "[[Harlow v. Fitzgerald]]", "[[Graham v. Connor]]", "[[Rivas-Villegas v. Cortesluna]]"]
aliases: []
tags: ["case", "qualified-immunity", "section-1983", "two-step-sequence", "clearly-established", "excessive-force"]
holding: "Established the (then-mandatory) two-step qualified-immunity sequence: (1) taken in the light most favorable to the plaintiff, do the…"
lake:
  record_id: Saucier v. Katz
  status: verified
  projected_at: 2026-07-06
---

# Saucier v. Katz

*533 U.S. 194 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — sequence no longer mandatory per [[Pearson v. Callahan]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Saucier, a military police officer providing security at a base where Vice President Gore was speaking, removed Katz — an animal-rights protester who tried to display a banner — and allegedly shoved him roughly while putting him into a van. Katz sued under *[[Bivens v. Six Unknown Named Agents|Bivens]]* for excessive force. Saucier asserted [[Qualified Immunity|qualified immunity]]; the Ninth Circuit denied it, treating the qualified-immunity inquiry as identical to the Fourth Amendment excessive-force merits.

## Issue
How a court must analyze [[Qualified Immunity|qualified immunity]] in an excessive-force case, and whether that inquiry collapses into the Fourth Amendment merits.

## Rule
A court analyzes [[Qualified Immunity|qualified immunity]] in a fixed sequence. "A court required to rule upon the qualified immunity issue must consider, then, this threshold question: Taken in the light most favorable to the party asserting the injury, do the facts alleged show the officer's conduct violated a constitutional right? This must be the initial inquiry." — *Saucier v. Katz*, 533 U.S. at 201. ^pin-201

"[I]f a violation could be made out on a favorable view of the parties' submissions, the next, sequential step is to ask whether the right was clearly established. . . . [in] light of the specific context of the case, not as a broad general proposition." — *Id.* ^pin-201a

*(This sequence was held no longer mandatory by [[Pearson v. Callahan]] (2009); the two-part test itself remains good law.)*

## Application
Applying its two-step framework, the Court held that even assuming a constitutional violation could be shown, Saucier was entitled to [[Qualified Immunity|qualified immunity]]: in the context he confronted — securing an event for the Vice President — a reasonable officer could have believed that hustling Katz into the van was a lawful amount of force, so the asserted right was not clearly established at the specific level required. The excessive-force merits did not merge with, and could not substitute for, the distinct clearly-established inquiry.

## Conclusion
[[Qualified Immunity|Qualified immunity]] is analyzed in sequence, and Saucier was entitled to it; the Ninth Circuit was reversed.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**. **Limited by** [[Pearson v. Callahan]] (2009), which held that *Saucier*'s two-step sequence "should no longer be regarded as mandatory," freeing courts to decide the prongs in either order. *Saucier*'s two-part qualified-immunity test (constitutional violation; clearly established) remains good law and is regularly applied (e.g., [[Rivas-Villegas v. Cortesluna]]).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Saucier v. Katz*, 533 U.S. 194 (2001) — https://www.courtlistener.com/opinion/118449/saucier-v-katz/ — pinpoint: 201 (CL carries an unpaginated case-text import; pinpoint per the U.S. Reports).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8433125f4779f671", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "533 U.S. 194 (2001)", "court": "U.S. Supreme Court", "neutral_cite": "2001 U.S. LEXIS 4664", "official_citation_present": true, "parallel_cite": "121 S. Ct. 2151; 150 L. Ed. 2d 272", "title": "Saucier v. Katz", "year": "2001"}}
{"assertion_id": "1c72934f91daf525", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Saucier v. Katz"}}
{"assertion_id": "7eec19efac543fe8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Established the (then-mandatory) two-step qualified-immunity sequence: (1) taken in the light most favorable to the plaintiff, do the…", "title": "Saucier v. Katz"}}
{"assertion_id": "3cc9dd4a79c51b13", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-saucier-v-katz"}, "payload": {"by": [{"cite": "555 U.S. 223", "cluster_id": "145918", "field_ii": "limited", "name": "Pearson v. Callahan"}], "field_i_validity": "caution", "point": "legacy-limited-saucier-v-katz", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "Saucier v. Katz"}}
{"assertion_id": "49d88a8e29d57bed", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2001-06-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Saucier v. Katz", "field_i_validity": "caution", "scope_note": "Pearson v. Callahan (2009) held that Saucier's two-step sequence is no longer mandatory; Saucier's two-part qualified-immunity test survives.", "title": "Saucier v. Katz", "varies_by_point": "true"}}
{"assertion_id": "f22dc04a21e6881a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Saucier v. Katz"}}
```

### lake record — Saucier v. Katz

```json
{
  "schema_version": "s2.v1",
  "record_id": "Saucier v. Katz",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "SAUCIER v. KATZ Et Al.",
    "case_name_short": "Katz",
    "case_name_full": "Donald Saucier v. Elliot M. Katz and in Defense of Animals",
    "input_case_name": "Saucier v. Katz",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-06-18",
    "year": 2001,
    "docket": "99-1977",
    "cluster_id": 118449,
    "lead_opinion_id": 118449,
    "sibling_ids": [
      118449,
      9434118,
      9434119,
      9434120
    ],
    "absolute_url": "/opinion/118449/saucier-v-katz-et-al/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 118448,
        "score": 120,
        "case_name": "Donald Saucier v. Elliot M. Katz and in Defense of Animals"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "533 U.S. 194",
      "volume": "533",
      "reporter": "U.S.",
      "page": "194",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "121 S. Ct. 2151",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "2151",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "150 L. Ed. 2d 272",
        "volume": "150",
        "reporter": "L. Ed. 2d",
        "page": "272",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 4664",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "4664",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "533 U.S. 194",
        "volume": "533",
        "reporter": "U.S.",
        "page": "194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 2151",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "2151",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "150 L. Ed. 2d 272",
        "volume": "150",
        "reporter": "L. Ed. 2d",
        "page": "272",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 4664",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "4664",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "533 U.S. 194",
    "official_selection": {
      "court_class": "scotus",
      "selected": "533 U.S. 194",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-201",
      "page": null,
      "quote": "--- # Saucier v. Katz *533 U.S. 194 (2001)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **limited** *(as of 2026-06-30)* \u2014 sequence no longer mandatory per [[Pearson v. Callahan]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Saucier, a military police officer providing security at a base where Vice President Gore was speaking, removed Katz \u2014 an animal-rights protester who tried to display a banner \u2014 and allegedly shoved him roughly while putting him into a van. Katz sued under *Bivens* for excessive force. Saucier asserted qualified immunity; the Ninth Circuit denied it, treating the qualified-immunity inquiry as identical to the Fourth Amendment excessive-force merits. ## Issue How a court must analyze qualified immunity in an excessive-force case, and whether that inquiry collapses into the Fourth Amendment merits. ## Rule A court analyzes qualified immunity in a fixed sequence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-201a",
      "page": null,
      "quote": "[I]f a violation could be made out on a favorable view of the parties' submissions, the next, sequential step is to ask whether the right was clearly established. . . . [in] light of the specific context of the case, not as a broad general proposition.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "2001-06-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Saucier v. Katz",
    "varies_by_point": true,
    "scope_note": "Pearson v. Callahan (2009) held that Saucier's two-step sequence is no longer mandatory; Saucier's two-part qualified-immunity test survives.",
    "point_overrides": [
      {
        "point": "legacy-limited-saucier-v-katz",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Pearson v. Callahan",
            "cluster_id": 145918,
            "cite": "555 U.S. 223",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Pearson v. Callahan (2009) held that Saucier's two-step sequence is no longer mandatory; Saucier's two-part qualified-immunity test survives."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": "555 U.S. 223",
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
          "name": "Vincent v. The Money Store",
          "cluster_id": 2641986,
          "cite": [
            "736 F.3d 88",
            "2013 WL 5989446"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Saucier v. Katz:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118449 OR 9434118 OR 9434119 OR 9434120) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      },
      "lane2_top_cited": {
        "query": "cites:(118449 OR 9434118 OR 9434119 OR 9434120)",
        "reviewed": 1,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(118449 OR 9434118 OR 9434119 OR 9434120)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118449 OR 9434118 OR 9434119 OR 9434120)",
    "indexed_citing_opinions": 1,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118449,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434118,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9434119,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434120,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 14,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/saucier-v-katz.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 1,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118449,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 111481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 112594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 195798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 302266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 548937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 558137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 628034,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 683167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 766536,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 768361,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118449,
        "cited_id": 1268548,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T18:38:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:38:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:38:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:38:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Saucier v. Katz

```
<p class="case_cite"><span class="citation" data-id="1268548"><a href="/opinion/1268548/cedric-kushner-promotions-ltd-v-king/" aria-description="Citation for case: Cedric Kushner Promotions, Ltd. v. King">533 U.S. 158</a></span><br><span class="citation" data-id="1268548"><a href="/opinion/1268548/cedric-kushner-promotions-ltd-v-king/" aria-description="Citation for case: Cedric Kushner Promotions, Ltd. v. King">121 S.Ct. 2087</a></span><br><span class="citation" data-id="1268548"><a href="/opinion/1268548/cedric-kushner-promotions-ltd-v-king/" aria-description="Citation for case: Cedric Kushner Promotions, Ltd. v. King">150 L.Ed.2d 198</a></span><br></p>
    <p class="parties">NOTICE: This opinion is subject to formal revision before publication in the preliminary print of the United States Reports. Readers are requested to notify the Reporter of Decisions, Supreme Court of the United States, Washington, D. C. 20543, of any typographical or other formal errors, in order that corrections may be made before the preliminary print goes to press.<br>DONALD SAUCIER, PETITIONER<br>v.<br>ELLIOT M. KATZ and IN DEFENSE OF ANIMALS</p>
    <p class="docket">No. 99-1977.</p>
    <p class="court">SUPREME COURT OF THE UNITED STATES</p>
    <p class="date">Argued March 20, 2001<br>Decided June 18, 2001</p>
    <div class="prelims">
      <p>Syllabus</p>
      <p>Respondent Katz, president of respondent In Defense of Animals, filed a suit pursuant to Bivens v. Six Unknown Fed. Narcotics Agents, <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span>, against, inter alios, petitioner Saucier, a military policeman. Katz alleged, among other things, that Saucier had violated his Fourth Amendment rights by using excessive force in arresting him while he protested during Vice President Gore's speech at a San Francisco army base. The District Court declined to grant Saucier summary judgment on qualified immunity grounds. In affirming, the Ninth Circuit made a two-part qualified immunity inquiry. First, it found that the law governing Saucier's conduct was clearly established when the incident occurred. It therefore moved to a second step: to determine if a reasonable officer could have believed, in light of the clearly established law, that his conduct was lawful. The court concluded that this step and the merits of a Fourth Amendment excessive force claim are identical, since both concern the objective reasonableness of the officer's conduct in light of the circumstances the officer faced at the scene. Thus, it found, summary judgment based on qualified immunity was inappropriate.</p>
      <p>Held:   1. A qualified immunity ruling requires an analysis not susceptible of fusion with the question whether unreasonable force was used in making the arrest. The Ninth Circuit's approach cannot be reconciled with Anderson v. Creighton, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">483 U.S. 635</a></span>. A qualified immunity defense must be considered in proper sequence. A ruling should be made early in the proceedings so that the cost and expenses of trial are avoided where the defense is dispositive. Such immunity is an entitlement not to stand trial, not a defense from liability. Mitchell v. Forsyth, <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#526" aria-description="Citation for case: Mitchell v. Forsyth">472 U.S. 511, 526</a></span>. The initial inquiry is whether a constitutional right would have been violated on the facts alleged, for if no right would have been violated, there is no need for further inquiry into immunity. However, if a violation could be made out on a favorable view of the parties' submissions, the next, sequential step is whether the right was clearly established. This inquiry must be undertaken in light of the case's specific context, not as a broad general proposition. The relevant, dispositive inquiry is whether it would be clear to a reasonable officer that the conduct was unlawful in the situation he confronted. See Wilson v. Layne, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#615" aria-description="Citation for case: Wilson v. Layne">526 U.S. 603, 615</a></span>. The Ninth Circuit's approach-to deny summary judgment if a material issue of fact remains on the excessive force claim-could undermine the goal of qualified immunity to avoid excessive disruption of government and permit the resolution of many insubstantial claims on summary judgment. Harlow v. Fitzgerald, <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U.S. 800, 818</a></span>. If the law did not put the officer on notice that his conduct would be clearly unlawful, summary judgment based on qualified immunity is appropriate. The Ninth Circuit concluded that qualified immunity is duplicative in an excessive force case, thus eliminating the need for the second step. In holding that qualified immunity applied in the Fourth Amendment context just as it would for any other official misconduct claim, the Anderson Court rejected the argument that there is no distinction between the reasonableness standard for warrantless searches and the qualified immunity inquiry. In an attempt to distinguish Anderson, Katz claims that the subsequent Graham v. Connor, <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span>, decision set forth an excessive force analysis indistinguishable from qualified immunity, thus rendering the separate immunity inquiry superfluous and inappropriate in such cases. Contrary to his arguments, the immunity and excessive force inquiries remain distinct after Graham. Graham sets forth factors relevant to the merits of a constitutional excessive force claim, which include the severity of the crime, whether the suspect poses a threat to the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">Id., at 396</a></span>. If an officer reasonably, but mistakenly, believed that a suspect was likely to fight back, for instance, the officer would be justified in using more force than in fact was needed. The qualified immunity inquiry's concern, on the other hand, is to acknowledge that reasonable mistakes can be made as to the legal constraints on particular police conduct. An officer might correctly perceive all of the relevant facts, but have a mistaken understanding as to whether a particular amount of force is legal in those circumstances. Pp. 4-11.</p>
      <p>2. Petitioner was entitled to qualified immunity. Assuming that a constitutional violation occurred under the facts alleged, the question is whether this general prohibition was the source for clearly established law that was contravened in the circumstances. In the circumstances presented to petitioner, which included the duty to protect the Vice President's safety and security from persons unknown in number, there was no clearly established rule prohibiting him from acting as he did. This conclusion is confirmed by the uncontested fact that the force used-dragging Katz from the area and shoving him while placing him into a van-was not so excessive that respondent suffered hurt or injury. Pp. 11-14.</p>
      <p><span class="citation multiple-matches"><a href="/c/F.3d/194/962/">194 F.3d 962</a></span>, reversed and remanded.</p>
      <p>ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT</p>
      <p>Kennedy, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Scalia, and Thomas, JJ., joined, and in which Souter, J., joined as to Parts I and II.</p>
      <p>Opinion of the Court</p>
      <p>Justice Kennedy delivered the opinion of the Court.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p>In this case a citizen alleged excessive force was used to arrest him. The arresting officer asserted the defense of qualified immunity. The matter we address is whether the requisite analysis to determine qualified immunity is so intertwined with the question whether the officer used excessive force in making the arrest that qualified immunity and constitutional violation issues should be treated as one question, to be decided by the trier of fact. The Court of Appeals held the inquiries do merge into a single question. We now reverse and hold that the ruling on qualified immunity requires an analysis not susceptible of fusion with the question whether unreasonable force was used in making the arrest. I   In autumn of 1994, the Presidio Army Base in San Francisco was the site of an event to celebrate conversion of the base to a national park. Among the speakers was Vice President Albert Gore, Jr., who attracted several hundred observers from the military and the general public. Some in attendance were not on hand to celebrate, however. Respondent Elliot Katz was concerned that the Army's Letterman Hospital would be used for conducting experiments on animals. (Katz was president of a group called In Defense of Animals. Although both he and the group are respondents here, the issues we discuss center upon Katz, and we refer to him as "respondent"). To voice opposition to the possibility that the hospital might be used for experiments, respondent brought with him a cloth banner, approximately 4 by 3 feet, that read "Please Keep Animal Torture Out of Our National Parks." In the past, as respondent was aware, members of the public had been asked to leave the military base when they engaged in certain activities, such as distributing handbills; and he kept the banner concealed under his jacket as he walked through the base.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p>The area designated for the speakers contained seating for the general public, separated from the stage by a waist-high fence. Respondent sat in the front row of the public seating area. At about the time Vice President Gore began speaking, respondent removed the banner from his jacket, started to unfold it, and walked toward the fence and speakers' platform.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p>Petitioner Donald Saucier is a military police officer who was on duty that day. He had been warned by his superiors of the possibility of demonstrations, and respondent had been identified as a potential protestor. Petitioner and Sergeant Steven Parker-also a military police officer, but not a party to the suit-recognized respondent and moved to intercept him as he walked toward the fence. As he reached the barrier and began placing the banner on the other side, the officers grabbed respondent from behind, took the banner, and rushed him out of the area. Each officer had one of respondent's arms, half-walking, half-dragging him, with his feet "barely touching the ground." App. 24. Respondent was wearing a visible, knee-high leg brace, although petitioner later testified he did not remember noticing it at the time. Saucier and Parker took respondent to a nearby military van, where, respondent claims, he was shoved or thrown inside. Id., at 25. The reason for the shove remains unclear. It seems agreed that respondent placed his feet somewhere on the outside of the van, perhaps the bumper, but there is a dispute whether he did so to resist. As a result of the shove, respondent claims, he fell to the floor of the van, where he caught himself just in time to avoid any injury. The officers drove respondent to a military police station, held him for a brief time, and then released him. Though the details are not clear, it appears that at least one other protestor was also placed into the van and detained for a brief time. Id., at 27.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p>Respondent brought this action in the United States District Court for the Northern District of California against petitioner and other officials pursuant to Bivens v. Six Unknown Fed. Narcotics Agents, <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span> (1971), alleging, inter alia, that defendants had violated respondent's Fourth Amendment rights by using excessive force to arrest him. The District Court granted the defendants' motions for summary judgment on the grounds of qualified immunity on all claims other than the excessive force claim against Saucier. It held a dispute on a material fact existed concerning whether excessive force was used to remove respondent from the crowd and place him into the van. App. to Pet. for Cert. 27a. The District Court held that the law governing excessive force claims was clearly established at the time of the arrest, and that "[i]n the Fourth Amendment context, the qualified immunity inquiry is the same as the inquiry made on the merits." <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.,</a></span> at 29a-30a. As a result, it ruled, petitioner was not entitled to summary judgment. <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.,</a></span> at 30a.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p>In the United States Court of Appeals for the Ninth Circuit petitioner filed an interlocutory appeal from the denial of qualified immunity. <span class="citation multiple-matches"><a href="/c/F.3d/194/962/">194 F.3d 962</a></span> (1999). The Court of Appeals affirmed, noting at the outset its two-part analysis for qualified immunity questions. First, the Court of Appeals considers "whether the law governing the official's conduct was clearly established." Id., at 967. If it was not, that ends the matter, and the official is entitled to immunity. If, however, the law was clearly established when the conduct occurred, the Court of Appeals' second step is to determine if a reasonable officer could have believed, in light of the clearly established law, that his conduct was lawful. Ibid. As to the first step of its analysis, the court observed that Graham v. Connor, <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span> (1989), sets forth the objective reasonableness test for evaluating excessive force claims, a principle the Court of Appeals concluded was clearly established for qualified immunity purposes. The court then concluded that the second step of the qualified immunity inquiry and the merits of the Fourth Amendment excessive force claim are identical, since both concern the objective reasonableness of the officer's conduct in light of the circumstances the officer faced on the scene. 194 F.3d, at 968. On this reasoning, summary judgment based on qualified immunity was held inappropriate. Id., at 968-969.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p>Saucier, represented by the Government of the United States, sought review here, arguing the Court of Appeals erred in its view that the qualified immunity inquiry is the same as the constitutional inquiry and so becomes superfluous or duplicative when excessive force is alleged. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.S./531/991/">531 U.S. 991</a></span> (2000).</p>
    </div>
    <p>II</p>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p>The Court of Appeals ruled first that the right was clearly established; and second that the reasonableness inquiry into excessive force meant that it need not consider aspects of qualified immunity, leaving the whole matter to the jury. 194 F.3d, at 967. This approach cannot be reconciled with Anderson v. Creighton, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">483 U.S. 635</a></span> (1987), however, and was in error in two respects. As we shall explain, the first inquiry must be whether a constitutional right would have been violated on the facts alleged; second, assuming the violation is established, the question whether the right was clearly established must be considered on a more specific level than recognized by the Court of Appeals.</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p>In a suit against an officer for an alleged violation of a constitutional right, the requisites of a qualified immunity defense must be considered in proper sequence. Where the defendant seeks qualified immunity, a ruling on that issue should be made early in the proceedings so that the costs and expenses of trial are avoided where the defense is dispositive. Qualified immunity is "an entitlement not to stand trial or face the other burdens of litigation." Mitchell v. Forsyth, <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#526" aria-description="Citation for case: Mitchell v. Forsyth">472 U.S. 511, 526</a></span> (1985). The privilege is "an immunity from suit rather than a mere defense to liability; and like an absolute immunity, it is effectively lost if a case is erroneously permitted to go to trial." <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">Ibid.</a></span> As a result, "we repeatedly have stressed the importance of resolving immunity questions at the earliest possible stage in litigation." Hunter v. Bryant, <span class="citation" data-id="9432435"><a href="/opinion/112671/hunter-v-bryant/#227" aria-description="Citation for case: Hunter v. Bryant">502 U.S. 224, 227</a></span> (1991) (per curiam).</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p>A court required to rule upon the qualified immunity issue must consider, then, this threshold question: Taken in the light most favorable to the party asserting the injury, do the facts alleged show the officer's conduct violated a constitutional right? This must be the initial inquiry. Siegert v. Gilley, <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/#232" aria-description="Citation for case: Siegert v. Gilley">500 U.S. 226, 232</a></span> (1991). In the course of determining whether a constitutional right was violated on the premises alleged, a court might find it necessary to set forth principles which will become the basis for a holding that a right is clearly established. This is the process for the law's elaboration from case to case, and it is one reason for our insisting upon turning to the existence or nonexistence of a constitutional right as the first inquiry. The law might be deprived of this explanation were a court simply to skip ahead to the question whether the law clearly established that the officer's conduct was unlawful in the circumstances of the case.</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p>If no constitutional right would have been violated were the allegations established, there is no necessity for further inquiries concerning qualified immunity. On the other hand, if a violation could be made out on a favorable view of the parties' submissions, the next, sequential step is to ask whether the right was clearly established. This inquiry, it is vital to note, must be undertaken in light of the specific context of the case, not as a broad general proposition; and it too serves to advance understanding of the law and to allow officers to avoid the burden of trial if qualified immunity is applicable.</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p>In this litigation, for instance, there is no doubt that Graham v. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Connor, supra,</a></span> clearly establishes the general proposition that use of force is contrary to the Fourth Amendment if it is excessive under objective standards of reasonableness. Yet that is not enough. Rather, we emphasized in Anderson "that the right the official is alleged to have violated must have been 'clearly established' in a more particularized, and hence more relevant, sense: The contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right." <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 640</a></span>. The relevant, dispositive inquiry in determining whether a right is clearly established is whether it would be clear to a reasonable officer that his conduct was unlawful in the situation he confronted. See Wilson v. Layne, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#615" aria-description="Citation for case: Wilson v. Layne">526 U.S. 603, 615</a></span> (1999) ("[A]s we explained in Anderson, the right allegedly violated must be defined at the appropriate level of specificity before a court can determine if it was clearly established").</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p>The approach the Court of Appeals adopted-to deny summary judgment any time a material issue of fact remains on the excessive force claim-could undermine the goal of qualified immunity to "avoid excessive disruption of government and permit the resolution of many insubstantial claims on summary judgment." Harlow v. Fitzgerald, <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U.S. 800, 818</a></span> (1982). If the law did not put the officer on notice that his conduct would be clearly unlawful, summary judgment based on qualified immunity is appropriate. See Malley v. Briggs, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U.S. 335, 341</a></span> (1986) (qualified immunity protects "all but the plainly incompetent or those who knowingly violate the law").</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p>This is not to say that the formulation of a general rule is beside the point, nor is it to insist the courts must have agreed upon the precise formulation of the standard. Assuming, for instance, that various courts have agreed that certain conduct is a constitutional violation under facts not distinguishable in a fair way from the facts presented in the case at hand, the officer would not be entitled to qualified immunity based simply on the argument that courts had not agreed on one verbal formulation of the controlling standard.</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p>The Court of Appeals concluded that qualified immunity is merely duplicative in an excessive force case, eliminating the need for the second step where a constitutional violation could be found based on the allegations. In Anderson, a warrantless search case, we rejected the argument that there is no distinction between the reasonableness standard for warrantless searches and the qualified immunity inquiry. We acknowledged there was some "surface appeal" to the argument that, because the Fourth Amendment's guarantee was a right to be free from "unreasonable" searches and seizures, it would be inconsistent to conclude that an officer who acted unreasonably under the constitutional standard nevertheless was entitled to immunity because he " 'reasonably' acted unreasonably." <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#643" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 643</a></span>. This superficial similarity, however, could not overcome either our history of applying qualified immunity analysis to Fourth Amendment claims against officers or the justifications for applying the doctrine in an area where officers perform their duties with considerable uncertainty as to "whether particular searches or seizures comport with the Fourth Amendment." <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#644" aria-description="Citation for case: Anderson v. Creighton">Id., at 644</a></span>. With respect, moreover, to the argument made in Anderson that an exception should be made for Fourth Amendment cases, we observed "the heavy burden this argument must sustain to be successful," since "the doctrine of qualified immunity reflects a balance that has been struck 'across the board.' " <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Id.,</a></span> at 642 (quoting Harlow v. <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#821" aria-description="Citation for case: Harlow v. Fitzgerald">Fitzgerald, supra, at 821</a></span>). We held that qualified immunity applied in the Fourth Amendment context just as it would for any other claim of official misconduct. <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#644" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 644</a></span>.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p>Faced, then, with the heavy burden of distinguishing Anderson and of carving out an exception to the typical qualified immunity analysis applied in other Fourth Amendment contexts, the primary submission by respondent in defense of the Court of Appeals' decision is that our decision in Graham v. Connor, <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span> (1989), somehow changes matters. Graham, in respondent's view, sets forth an excessive force analysis indistinguishable from qualified immunity, rendering the separate immunity inquiry superfluous and inappropriate. Respondent asserts that, like the qualified immunity analysis applicable in other contexts, the excessive force test already affords officers latitude for mistaken beliefs as to the amount of force necessary, so that "Graham has addressed for the excessive force area most of the concerns expressed in Anderson." Brief for Respondents 7. Respondent points out that Graham did not address the interaction of excessive force claims and qualified immunity, since the issue was not raised, see <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#399" aria-description="Citation for case: Graham v. Connor">490 U.S., at 399, n. 12</a></span>; and respondent seeks to distinguish Anderson on the theory that the issue of probable cause implicates evolving legal standards and resulting legal uncertainty, a subject raising recurrent questions of qualified immunity. By contrast, respondent says, excessive force is governed by the standard established in Graham, a standard providing ample guidance for particular situations. Finally, respondent adopts the suggestion made by one Court of Appeals that the relevant distinction is that probable cause is an ex post inquiry, whereas excessive force, like qualified immunity, should be evaluated from an ex ante perspective. See Finnegan v. Fountain, <span class="citation" data-id="548937"><a href="/opinion/548937/patricia-finnegan-v-richard-fountain/#824" aria-description="Citation for case: Patricia Finnegan v. Richard Fountain">915 F.2d 817, 824, n. 11</a></span> (CA2 1990).</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p>These arguments or attempted distinctions cannot bear the weight respondent seeks to place upon them. Graham did not change the qualified immunity framework explained in Anderson. The inquiries for qualified immunity and excessive force remain distinct, even after Graham.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p>In Graham, we held that claims of excessive force in the context of arrests or investigatory stops should be analyzed under the Fourth Amendment's "objective reasonableness standard," not under substantive due process principles. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#388" aria-description="Citation for case: Graham v. Connor">490 U.S., at 388, 394</a></span>. Because "police officers are often forced to make split-second judgments-in circumstances that are tense, uncertain, and rapidly evolving-about the amount of force that is necessary in a particular situation," <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#397" aria-description="Citation for case: Graham v. Connor">id., at 397</a></span>, the reasonableness of the officer's belief as to the appropriate level of force should be judged from that on-scene perspective. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">Id., at 396</a></span>. We set out a test that cautioned against the "20/20 vision of hindsight" in favor of deference to the judgment of reasonable officers on the scene. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#393" aria-description="Citation for case: Graham v. Connor">Id., at 393, 396</a></span>. Graham sets forth a list of factors relevant to the merits of the constitutional excessive force claim, "requir[ing] careful attention to the facts and circumstances of each particular case, including the severity of the crime at issue, whether the suspect poses an immediate threat to the safety of the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">Id., at 396</a></span>. If an officer reasonably, but mistakenly, believed that a suspect was likely to fight back, for instance, the officer would be justified in using more force than in fact was needed.</p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p>The qualified immunity inquiry, on the other hand, has a further dimension. The concern of the immunity inquiry is to acknowledge that reasonable mistakes can be made as to the legal constraints on particular police conduct. It is sometimes difficult for an officer to determine how the relevant legal doctrine, here excessive force, will apply to the factual situation the officer confronts. An officer might correctly perceive all of the relevant facts but have a mistaken understanding as to whether a particular amount of force is legal in those circumstances. If the officer's mistake as to what the law requires is reasonable, however, the officer is entitled to the immunity defense.</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p>Graham does not always give a clear answer as to whether a particular application of force will be deemed excessive by the courts. This is the nature of a test which must accommodate limitless factual circumstances. This reality serves to refute respondent's claimed distinction between excessive force and other Fourth Amendment contexts; in both spheres the law must be elaborated from case to case. Qualified immunity operates in this case, then, just as it does in others, to protect officers from the sometimes "hazy border between excessive and acceptable force," Priester v. Riviera Beach, <span class="citation multiple-matches"><a href="/c/F.3d/208/919/">208 F.3d 919</a></span>, 926-927 (CA11 2000), and to ensure that before they are subjected to suit, officers are on notice their conduct is unlawful.</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p>Graham and Anderson refute the excessive force/probable cause distinction on which much of respondent's position seems to depend. The deference owed officers facing suits for alleged excessive force is not different in some qualitative respect from the probable cause inquiry in Anderson. Officers can have reasonable, but mistaken, beliefs as to the facts establishing the existence of probable cause or exigent circumstances, for example, and in those situations courts will not hold that they have violated the Constitution. Yet, even if a court were to hold that the officer violated the Fourth Amendment by conducting an unreasonable, warrantless search, Anderson still operates to grant officers immunity for reasonable mistakes as to the legality of their actions. The same analysis is applicable in excessive force cases, where in addition to the deference officers receive on the underlying constitutional claim, qualified immunity can apply in the event the mistaken belief was reasonable.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p>The temporal perspective of the inquiry, whether labeled as ex ante or ex post, offers no meaningful distinction between excessive force and other Fourth Amendment suits. Graham recognized as much, reviewing several of our probable cause and search warrant cases, then stating that "[w]ith respect to a claim of excessive force, the same standard of reasonableness at the moment applies." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U.S., at 396</a></span> (discussing use of force under Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span> (1968); probable cause to arrest under Hill v. California, <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U.S. 797</a></span> (1971); and search warrant requirements under Maryland v. Garrison, <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">480 U.S. 79</a></span> (1987)); see also Hunter v. Bryant, <span class="citation" data-id="9432435"><a href="/opinion/112671/hunter-v-bryant/#228" aria-description="Citation for case: Hunter v. Bryant">502 U.S., at 228</a></span> ("Probable cause existed if 'at the moment the arrest was made . . . the facts and circumstances within their knowledge and of which they had reasonably trustworthy information were sufficient to warrant a prudent man in believing' " a crime had been committed (quoting Beck v. Ohio, <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U.S. 89, 91</a></span> (1964))). Excessive force claims, like most other Fourth Amendment issues, are evaluated for objective reasonableness based upon the information the officers had when the conduct occurred.</p>
    </div>
    <p>III</p>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p>The case was presented to the Court of Appeals on the assumption that respondent's seizure and brief detention did not violate clearly established First Amendment privileges and did not violate the Fourth Amendment right to be free from arrest without probable cause, as distinct from the force used to detain. The sole question, then, is whether the force used violated a clearly established Fourth Amendment protection so that petitioner was not entitled to immunity.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p>Our instruction to the district courts and courts of appeal to concentrate at the outset on the definition of the constitutional right and to determine whether, on the facts alleged, a constitutional violation could be found is important. As we have said, the procedure permits courts in appropriate cases to elaborate the constitutional right with greater degrees of specificity. Because we granted certiorari only to determine whether qualified immunity was appropriate, however, and because of the limits imposed upon us by the questions on which we granted review, we will assume a constitutional violation could have occurred under the facts alleged based simply on the general rule prohibiting excessive force, then proceed to the question whether this general prohibition against excessive force was the source for clearly established law that was contravened in the circumstances this officer faced. There was no contravention under this standard. Though it is doubtful that the force used was excessive, we need not rest our conclusion on that determination. The question is what the officer reasonably understood his powers and responsibilities to be, when he acted, under clearly established standards.</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p>Respondent's excessive force claim for the most part depends upon the "gratuitously violent shove" allegedly received when he was placed into the van, although respondent notes as well that the alleged violation resulted from the "totality of the circumstances," including the way he was removed from the speaking area. See Brief for Respondents 3, n. 2.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p>These circumstances, however, disclose substantial grounds for the officer to have concluded he had legitimate justification under the law for acting as he did. In Graham we noted that "[o]ur Fourth Amendment jurisprudence has long recognized that the right to make an arrest or investigatory stop necessarily carries with it the right to use some degree of physical coercion or threat thereof to effect it." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U.S., at 396</a></span>. A reasonable officer in petitioner's position could have believed that hurrying respondent away from the scene, where the Vice President was speaking and respondent had just approached the fence designed to separate the public from the speakers, was within the bounds of appropriate police responses.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p>Petitioner did not know the full extent of the threat respondent posed or how many other persons there might be who, in concert with respondent, posed a threat to the security of the Vice President. There were other potential protestors in the crowd, and at least one other individual was arrested and placed into the van with respondent. In carrying out the detention, as it has been assumed the officers had the right to do, petitioner was required to recognize the necessity to protect the Vice President by securing respondent and restoring order to the scene. It cannot be said there was a clearly established rule that would prohibit using the force petitioner did to place respondent into the van to accomplish these objectives.</p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p>As for the shove respondent received when he was placed into the van, those same circumstances show some degree of urgency. We have approved the observation that "[n]ot every push or shove, even if it may later seem unnecessary in the peace of a judge's chambers, violates the Fourth Amendment." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Ibid.</a></span> (citations omitted). Pushes and shoves, like other police conduct, must be judged under the Fourth Amendment standard of reasonableness.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p>In the circumstances presented to this officer, which included the duty to protect the safety and security of the Vice President of the United States from persons unknown in number, neither respondent nor the Court of Appeals has identified any case demonstrating a clearly established rule prohibiting the officer from acting as he did, nor are we aware of any such rule. Our conclusion is confirmed by the uncontested fact that the force was not so excessive that respondent suffered hurt or injury. On these premises, petitioner was entitled to qualified immunity, and the suit should have been dismissed at an early stage in the proceedings.</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p>The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p>It is so ordered.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p>Ginsburg, J., filed an opinion concurring in the judgment, in which Stevens and Breyer, JJ., joined.</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p>Souter, J., filed an opinion concurring in part and dissenting in part.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p>Justice Ginsburg, with whom Justice Stevens and Justice Breyer join, concurring in the judgment.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p>In Graham v. Connor, <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span> (1989), the Court announced and described an "objective reasonableness" standard to govern all claims that law enforcement officers, in violation of the Fourth Amendment, used excessive force in the course of an arrest. Measuring material facts of this case that are not subject to genuine dispute against the Graham standard, I conclude that officer Saucier's motion for summary judgment should have been granted. I therefore concur in the Court's judgment. However, I would not travel the complex route the Court lays out for lower courts.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p>Application of the Graham objective reasonableness standard is both necessary, under currently governing precedent, and, in my view, sufficient to resolve cases of this genre. The Court today tacks on to a Graham inquiry a second, overlapping objective reasonableness inquiry purportedly demanded by qualified immunity doctrine. The two-part test today's decision imposes holds large potential to confuse. Endeavors to bring the Court's abstract instructions down to earth, I suspect, will bear out what lower courts have already observed-paradigmatically, the determination of police misconduct in excessive force cases and the availability of qualified immunity both hinge on the same question: Taking into account the particular circumstances confronting the defendant officer, could a reasonable officer, identically situated, have believed the force employed was lawful? See, e.g., Roy v. Inhabitants of City of Lewiston, <span class="citation" data-id="195798"><a href="/opinion/195798/roy-v-inhabitants-of-the-city-of-lewiston/#695" aria-description="Citation for case: Roy v. Inhabitants of the City of Lewiston">42 F.3d 691, 695</a></span> (CA1 1994); Rowland v. Perry, <span class="citation" data-id="6932940"><a href="/opinion/7030840/rowland-v-perry/#173" aria-description="Citation for case: Rowland v. Perry">41 F.3d 167, 173</a></span> (CA4 1994). Nothing more and nothing else need be answered in this case.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p>* All claims that law enforcement officers have used excessive force in the course of an arrest, Graham made explicit, are to be judged "under the Fourth Amendment and its 'reasonableness' standard, rather than under a 'substantive due process' approach." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#395" aria-description="Citation for case: Graham v. Connor">490 U.S., at 395</a></span>. Underlying intent or motive are not relevant to the inquiry; rather, "the question is whether the officers' actions are 'objectively reasonable' in light of the facts and circumstances confronting them." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#397" aria-description="Citation for case: Graham v. Connor">Id., at 397</a></span>. The proper perspective in judging an excessive force claim, Graham explained, is that of "a reasonable officer on the scene" and "at the moment" force was employed. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">Id., at 396</a></span>. "Not every push or shove," the Court cautioned, "even if it may later seem unnecessary in the peace of a judge's chambers, violates the Fourth Amendment." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Ibid.</a></span> (citation omitted). "The calculus of reasonableness" must allow for the reality that "police officers are often forced to make split-second judgments" about the force a particular situation warrants "in circumstances that are tense, uncertain, and rapidly evolving." <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">Id., at 396-397</a></span>.</p>
    </div>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p>Under Graham's instructions, the question in this case is whether officer Saucier, in light of the facts and circumstances confronting him, could have reasonably believed he acted lawfully. Here, as in the mine run of exces- sive force cases, no inquiry more complex than that is warranted.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p>Inspecting this case under Graham's lens, and without doubling the "objectively reasonable" inquiry, I agree that Katz's submissions were too slim to put officer Saucier to the burden of trial. As the Court points out, it is not genuinely in doubt that "[a] reasonable officer in [Saucier's] position could have believed that hurrying [Katz] away from the scene ... was within the bounds of appropriate police responses." Ante, at 13. Katz's excessive force claim thus depended on the "gratuitously violent shove" he allegedly received. Ante, at 12-13; see Brief for Respondents 3, n. 2 (conceding that "the gratuitous violent shove" was essential to Katz's excessive force claim).</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p>Yet Katz failed to proffer proof, after pretrial discovery, that Saucier, as distinguished from his fellow officer Parker,<a class="footnote" href="#fn1" id="fn1_ref">1</a> had a hand in the allegedly violent shove.<a class="footnote" href="#fn2" id="fn2_ref">2</a> Saucier, in his deposition, denied participating in any shove, see App. 39-40, while Katz, in his deposition, said, without elaborating: "They [Parker and Saucier] pretty much threw me in. Just shoved me in," id., at 25. But critically, at no point did Katz say, specifically, that Saucier himself, and not only Parker, pushed or shoved.</p>
    </div>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p>Katz's reluctance directly to charge Saucier with pushing or shoving is understandable in view of a television news videotape of the episode Katz presented as an exhibit to his complaint. See App. to Pet. for Cert. 27a. The videotape shows that the shove, described by Katz as gratuitously violent, came from the officer on the right side of the police van, not from the officer positioned on the left side. It is undisputed that the officer on the right is Parker, the officer on the left, Saucier. See Pet. for Cert. 27-28, and n. 19; Brief for Petitioner 50, n. 26. Mindful of Graham's cautionary observation that "[n]ot every push or shove, even if it may later seem unnecessary in the peace of a judge's chambers, violates the Fourth Amendment," <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor">490 U.S., at 396</a></span> (citation omitted), and in view of Katz's failure to deny that the shove alleged to establish excessive force came from Parker alone, not from Saucier, I am persuaded that Katz tendered no triable excessive force claim against Saucier.<a class="footnote" href="#fn3" id="fn3_ref">3</a></p>
    </div>
    <p>II</p>
    <div class="num" id="p41">
      <span class="num">41</span>
      <p>In the Court's opinion, Graham is inadequate to control adjudication of excessive force cases. Graham must be overlaid, the Court maintains, by a sequential qualified immunity inquiry. Ante, at 5. The Court instructs lower courts first to undertake what appears to be an unadorned Graham inquiry, i.e., to consider initially whether the parties' submissions, viewed favorably to the plaintiff, could show that the officer's conduct violated the Fourth Amendment. Ante, at 5, 6. If the plaintiff prevails on that "threshold question," ante, at 5, the trial court is then to proceed to the "dispositive [qualified immunity] inquiry," asking "whether it would be clear to a reasonable officer that the conduct was unlawful in the situation he confronted," ante, at 6.<a class="footnote" href="#fn4" id="fn4_ref">4</a></p>
    </div>
    <div class="num" id="p42">
      <span class="num">42</span>
      <p>In the instant case, however, the Court finds that procedural impediments stop it from considering first "whether a constitutional right would have been violated on the facts alleged." Ante, at 5, 12. The Court therefore "assume[s] a constitutional violation could have occurred," ante, at 12-i.e., it supposes a trier could have found that officer Saucier used force excessive under Graham's definition. Even so, the Court reasons, qualified immunity would shield Saucier because he could have "concluded he had legitimate justification under the law for acting as he did." Ante, at 13.</p>
    </div>
    <div class="num" id="p43">
      <span class="num">43</span>
      <p>Skipping ahead of the basic Graham (constitutional violation) inquiry it admonished lower courts to undertake at the outset, the Court failed to home in on the duplication inherent in its two-step scheme. As lower courts dealing with excessive force cases on the ground have recognized, however, this Court's decisions invoke "the same 'objectively reasonable' standard in describing both the constitutional test of liability [citing Graham, <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#397" aria-description="Citation for case: Graham v. Connor">490 U.S., at 397</a></span>], and the ... standard for qualified immunity [citing Anderson v. Creighton, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#639" aria-description="Citation for case: Anderson v. Creighton">483 U.S. 635, 639</a></span> (1987)]." Roy, <span class="citation" data-id="195798"><a href="/opinion/195798/roy-v-inhabitants-of-the-city-of-lewiston/#695" aria-description="Citation for case: Roy v. Inhabitants of the City of Lewiston">42 F.3d, at 695</a></span>; see Street v. Parham, <span class="citation" data-id="558137"><a href="/opinion/558137/willie-j-street-v-terry-parham-ken-snider-and-mike-hill-sheriff-of/#540" aria-description="Citation for case: Willie J. Street v. Terry Parham, Ken Snider, and Mike...">929 F.2d 537, 540</a></span> (CA10 1991) (describing excessive force case as one "where the determination of liability and the availability of qualified immunity depend on the same findings"). In other words, an officer who uses force that is objectively reasonable "in light of the facts and circumstances confronting [him]," Graham, <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#397" aria-description="Citation for case: Graham v. Connor">490 U.S., at 397</a></span>, simultaneously meets the standard for qualified immunity, see ante, at 6, and the standard the Court set in Graham for a decision on the merits in his favor. Conversely, an officer whose conduct is objectively unreasonable under Graham should find no shelter under a sequential qualified immunity test.</p>
    </div>
    <div class="num" id="p44">
      <span class="num">44</span>
      <p>Double counting "objective reasonableness," the Court appears to suggest, ante, at 4-5, is demanded by Anderson, which twice restated that qualified immunity shields the conduct of officialdom "across the board." <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#642" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 642</a></span>, 645 (quoting Harlow v. Fitzgerald, 457 U. S 800, 821 (1982) (Brennan, J., concurring)); see also Anderson, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#643" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 643</a></span> ("we have been unwilling to complicate qualified immunity analysis by making the scope or extent of immunity turn on the precise nature of various officials' duties or the precise character of the particular rights alleged to have been violated"). As I see it, however, excessive force cases are not meet for Anderson's two-part test.</p>
    </div>
    <div class="num" id="p45">
      <span class="num">45</span>
      <p>Anderson presented the question whether the particular search conducted without a warrant was supported by probable cause and exigent circumstances. The answer to such a question is often far from clear.<a class="footnote" href="#fn5" id="fn5_ref">5</a> Law in the area is constantly evolving and, correspondingly, variously interpreted. As aptly observed by the Second Circuit, "even learned and experienced jurists have had difficulty in defining the rules that govern a determination of probable cause ... . As he tries to find his way in this thicket, the police officer must not be held to act at his peril." Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics, <span class="citation" data-id="9457921"><a href="/opinion/302266/webster-bivens-v-six-unknown-named-agents-of-the-federal-bureau-of/#1348" aria-description="Citation for case: Webster Bivens v. Six Unknown Named Agents of the Federal...">456 F.2d 1339, 1348</a></span> (1972) (on remand). In this light, Anderson reasoned: "Law enforcement officers whose judgments in making these difficult determinations [whether particular searches or seizures comport with the Fourth Amendment] are objectively legally reasonable should no more be held personally liable in damages than should officials making analogous determinations in other areas of law." <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#644" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 644</a></span> (emphasis added).</p>
    </div>
    <div class="num" id="p46">
      <span class="num">46</span>
      <p>As the foregoing discussion indicates, however, "excessive force" typically is not an "analogous determination." The constitutional issue whether an officer's use of force was reasonable in given circumstances routinely can be answered simply by following Graham's directions. In inquiring, under Graham, whether an officer's use of force was within a range of reasonable options, the decisionmaker is also (and necessarily) answering the question whether a reasonable officer "could have believed" his use of force "to be lawful," Anderson, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#638" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 638</a></span>. See Street, <span class="citation" data-id="558137"><a href="/opinion/558137/willie-j-street-v-terry-parham-ken-snider-and-mike-hill-sheriff-of/#541" aria-description="Citation for case: Willie J. Street v. Terry Parham, Ken Snider, and Mike...">929 F.2d, at 541, n. 2</a></span> (because of difficulty of deciding probable-cause issues, the conduct of an officer may be objectively reasonable even if cause did not exist, but "in excessive force cases, once a factfinder has determined that the force used was unnecessary under the circumstances, any question of objective reasonableness has also been foreclosed").</p>
    </div>
    <div class="num" id="p47">
      <span class="num">47</span>
      <p>The Court fears that dispensing with the duplicative qualified immunity inquiry will mean "leaving the whole matter to the jury." Ante, at 4. Again, experience teaches otherwise. Lower courts, armed with Graham's directions, have not shied away from granting summary judgment to defendant officials in Fourth Amendment excessive force cases where the challenged conduct is objectively reasonable based on relevant, undisputed facts. See, e.g., Wilson v. Spain, <span class="citation" data-id="9492989"><a href="/opinion/768361/robert-wilson-v-david-spain-mike-jones/#716" aria-description="Citation for case: Robert Wilson v. David Spain, Mike Jones">209 F.3d 713, 716</a></span> (CA8 2000) ("address[ing] in one fell swoop both [defendant's] qualified immunity and the merits of [plaintiff's] Fourth Amendment [excessive force] claim" and concluding officer's conduct was objectively reasonable in the circumstances, so summary judgment for officer was proper); Roy, <span class="citation" data-id="195798"><a href="/opinion/195798/roy-v-inhabitants-of-the-city-of-lewiston/#695" aria-description="Citation for case: Roy v. Inhabitants of the City of Lewiston">42 F.3d, at 695</a></span> (under single objective reasonableness test, district court properly granted summary judgment for defendant);<a class="footnote" href="#fn6" id="fn6_ref">6</a> Wardlaw v. Pickett, <span class="citation" data-id="628034"><a href="/opinion/628034/william-c-wardlaw-v-william-r-pickett-deputy-united-states-marshal/#1303" aria-description="Citation for case: William C. Wardlaw v. William R. Pickett, Deputy United...">1 F.3d 1297, 1303-1304</a></span> (CADC 1993) (same). Indeed, this very case, as I earlier explained, see supra, at 2-4, fits the summary judgment bill. Of course, if an excessive force claim turns on which of two conflicting stories best captures what happened on the street, Graham will not permit summary judgment in favor of the defendant official. And that is as it should be. When a plaintiff proffers evidence that the official subdued her with a chokehold even though she complied at all times with his orders, while the official proffers evidence that he used only stern words, a trial must be had. In such a case, the Court's two-step procedure is altogether inutile.</p>
    </div>
    <div class="num" id="p48">
      <span class="num">48</span>
      <p>* * *</p>
    </div>
    <div class="num" id="p49">
      <span class="num">49</span>
      <p>For the reasons stated, I concur in the Court's judgment, but not in the two-step inquiry the Court has ordered. Once it has been determined that an officer violated the Fourth Amendment by using "objectively unreasonable" force as that term is explained in Graham v. Connor, there is simply no work for a qualified immunity inquiry to do.</p>
    </div>
    <div class="footnotes">
      <div class="footnote">
        <p>NOTES:</p>
      </div>
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> Though named as a defendant, Parker was never served with the complaint, and therefore did not become a party to this litigation. See Brief for Petitioner 3, n. 4.</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> See Fed. Rule Civ. Proc. 56(e) ("When a motion for summary judgment is made and supported as provided in this rule, an adverse party may not rest upon the mere allegations or denials of the adverse party's pleading, but the adverse party's response ... must set forth specific facts showing that there is a genuine issue for trial.").</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> As the Court observes, there is a dispute whether Katz was resisting arrest at the time he was placed in the van. Ante, at 3. That dispute is irrelevant, however, in view of the absence of any indication that Saucier employed excessive force in removing Katz from the site of the celebration and placing him in the van. See Rowland v. Perry, <span class="citation" data-id="6932940"><a href="/opinion/7030840/rowland-v-perry/#174" aria-description="Citation for case: Rowland v. Perry">41 F.3d 167, 174</a></span> (CA4 1994) ("[d]isputed versions of the facts alone are not enough to warrant denial of summary judgment").</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> The Court's observation that "neither respondent nor the Court of Appeals ha[s] identified any case demonstrating a clearly established rule prohibiting the officer from acting as he did," ante, at 14, must be read in light of our previous caution that "the very action in question [need not have] previously been held unlawful" for a plaintiff to defeat qualified immunity, Anderson v. Creighton, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U.S. 635, 640</a></span> (1987).</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> Wilson v. Layne, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">526 U.S. 603</a></span> (1999), is a prototypical case. There, the Court accorded qualified immunity to police who permitted the media to accompany them on a search of a house. The constitutionality of the ride-along practice was unsettled at the time of the incident-in-suit in Wilson, and remained so until this Court spoke.</p>
      </div>
      <div class="footnote" id="fn6">
        <a class="footnote" href="#fn6_ref">6</a>
        <p> Upholding summary judgment for a police officer who shot an armed, intoxicated, belligerently behaving arrestee, the First Circuit in Roy elaborated: "[T]he Supreme Court intends to surround the police who make these on-the-spot choices in dangerous situations with a fairly wide zone of protection in close cases. Decisions from this circuit and other circuits are consistent with that view. And in close cases, a jury does not automatically get to second-guess these life and death decisions, even though the plaintiff has an expert and a plausible claim that the situation could better have been handled differently." <span class="citation" data-id="195798"><a href="/opinion/195798/roy-v-inhabitants-of-the-city-of-lewiston/#695" aria-description="Citation for case: Roy v. Inhabitants of the City of Lewiston">42 F.3d, at 695</a></span> (footnote omitted).</p>
      </div>
    </div>
    <div class="num" id="p50">
      <span class="num">50</span>
      <p>Justice Souter, concurring in part and dissenting in part.</p>
    </div>
    <div class="num" id="p51">
      <span class="num">51</span>
      <p>I join Parts I and II of the Court's opinion, but would remand the case for application of the qualified immunity standard.</p>
    </div>
    
```

---

## GROUP: content/cases/Spinelli v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Spinelli v. United States"
type: case
citation: "393 U.S. 410 (1969)"
parallel_cite: "89 S. Ct. 584; 21 L. Ed. 2d 637"
neutral_cite: 1969 U.S. LEXIS 2701
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-01-27
docket: 8
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1969-01-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Spinelli v. United States
  varies_by_point: false
  scope_note: "Refined the Aguilar two-prong informant-tip test; the rigid Aguilar-Spinelli framework was abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107831/spinelli-v-united-states/"
  cluster_id: 107831
  opinion_id: 107831
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Related (cross-doctrine)"
related: ["[[Aguilar v. Texas]]", "[[Illinois v. Gates]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "informants", "warrants", "historical"]
holding: "Refined Aguilar's two-prong informant-tip test: a tip is first measured against the basis-of-knowledge and veracity prongs, and innocent corroboration cannot cure a deficient tip — later abandoned by Illinois v. Gates' totality test."
lake:
  record_id: Spinelli v. United States
  status: verified
  projected_at: 2026-07-06
---

# Spinelli v. United States

*393 U.S. 410 (1969)* · U.S. Supreme Court · **Historical** · Treatment: **abrogated** *(as of 2026-06-30)* — abrogated by [[Illinois v. Gates]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Spinelli was convicted under the Travel Act for crossing from Illinois into St. Louis to conduct gambling (bookmaking). The FBI's warrant affidavit recited that agents had tracked his movements on several days, that he was known as a bookmaker, that an apartment he frequented contained two telephones with specified numbers, and that a "confidential reliable informant" had reported he was running a bookmaking operation using those two phones. The affidavit gave no facts showing why the informant was reliable or how he knew what he claimed.

## Issue
How the two-pronged test of [[Aguilar v. Texas]] — the informant's basis of knowledge and his veracity — applies when an informant's tip is partly corroborated by independent police investigation, and whether this affidavit established probable cause.

## Rule
The tip is first assessed under *[[Aguilar v. Texas|Aguilar]]*, and only then is corroboration considered. "The informer's report must first be measured against *Aguilar*'s standards so that its probative value can be assessed. If the tip is found inadequate under *Aguilar*, the other allegations which corroborate the information contained in the hearsay report should then be considered." — 393 U.S. at 415. ^pin-415

Corroboration suffices only if the corroborated tip is as trustworthy as one that would pass *[[Aguilar v. Texas|Aguilar]]* unaided. Applying that analysis here, "the informant's tip — even when corroborated to the extent indicated — was not sufficient to provide the basis for a finding of probable cause." — *Id.* at 418. ^pin-418

## Application
The affidavit failed both *[[Aguilar v. Texas|Aguilar]]* prongs: the bare assertion that the informant was "reliable" offered the magistrate no reason supporting that conclusion (veracity), and the tip recited no underlying circumstances showing how the informant learned that Spinelli was bookmaking (basis of knowledge). The independent FBI work — surveillance and the existence of two phones — corroborated only innocent detail (that Spinelli could have used those phones), unlike the minutely detailed, self-verifying corroboration in *[[Draper v. United States]]*. Because neither the tip nor its corroboration was as probative as a tip passing *[[Aguilar v. Texas|Aguilar]]* alone, probable cause was lacking.

## Conclusion
The warrant was not supported by probable cause; the conviction resting on the seized evidence was reversed. *Spinelli* (with *[[Aguilar v. Texas|Aguilar]]*) built the rigid two-prong informant framework later abandoned in [[Illinois v. Gates]].

## Treatment & subsequent history
- **Status:** abrogated *(as of 2026-06-30)* — **Historical** (tier 6).
- The structured two-prong "basis of knowledge" + "veracity" framework of [[Aguilar v. Texas]] and *Spinelli* was **abandoned by [[Illinois v. Gates]]** (1983) in favor of a **totality-of-the-circumstances** test. Under *[[Illinois v. Gates|Gates]]* the two prongs survive only as relevant, non-dispositive considerations.

## Appears on
- [[Probable Cause]] — *Key — Progeny / Refinement*
- [[Probable Cause in the Affidavit]] — *Related (cross-doctrine)*

## Sources
- *Spinelli v. United States*, 393 U.S. 410 (1969) — https://www.courtlistener.com/opinion/107831/spinelli-v-united-states/ — pinpoints: 415, 418.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "01213cc0e324304d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "393 U.S. 410 (1969)", "court": "U.S. Supreme Court", "neutral_cite": "1969 U.S. LEXIS 2701", "official_citation_present": true, "parallel_cite": "89 S. Ct. 584; 21 L. Ed. 2d 637", "title": "Spinelli v. United States", "year": "1969"}}
{"assertion_id": "6b2fc8a38f1246b7", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause in the Affidavit"}, "payload": {"home": "Probable Cause in the Affidavit", "role": "Related (cross-doctrine)", "title": "Spinelli v. United States"}}
{"assertion_id": "93482a9f15892900", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Key — Progeny / Refinement", "title": "Spinelli v. United States"}}
{"assertion_id": "a3d6e3aa07a533b2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Refined Aguilar's two-prong informant-tip test: a tip is first measured against the basis-of-knowledge and veracity prongs, and innocent corroboration cannot cure a deficient tip — later abandoned by Illinois v. Gates' totality test.", "title": "Spinelli v. United States"}}
{"assertion_id": "03b3526f6a5d9df7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1969-01-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Spinelli v. United States", "field_i_validity": "superseded", "scope_note": "Refined the Aguilar two-prong informant-tip test; the rigid Aguilar-Spinelli framework was abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983).", "title": "Spinelli v. United States", "varies_by_point": "false"}}
{"assertion_id": "f727b0fa7aee5ede", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Spinelli v. United States"}}
```

### lake record — Spinelli v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Spinelli v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Spinelli v. United States",
    "case_name_short": "Spinelli",
    "case_name_full": "Spinelli v. United States",
    "input_case_name": "Spinelli v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-01-27",
    "year": 1969,
    "docket": "8",
    "cluster_id": 107831,
    "lead_opinion_id": 107831,
    "sibling_ids": [
      107831,
      9423895,
      9423896,
      9423897,
      9423898,
      9423899
    ],
    "absolute_url": "/opinion/107831/spinelli-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "393 U.S. 410",
      "volume": "393",
      "reporter": "U.S.",
      "page": "410",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 584",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "584",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 L. Ed. 2d 637",
        "volume": "21",
        "reporter": "L. Ed. 2d",
        "page": "637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 2701",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2701",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "393 U.S. 410",
        "volume": "393",
        "reporter": "U.S.",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 584",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "584",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 L. Ed. 2d 637",
        "volume": "21",
        "reporter": "L. Ed. 2d",
        "page": "637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 2701",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2701",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "393 U.S. 410",
    "official_selection": {
      "court_class": "scotus",
      "selected": "393 U.S. 410",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-415",
      "page": null,
      "quote": "had reported he was running a bookmaking operation using those two phones. The affidavit gave no facts showing why the informant was reliable or how he knew what he claimed. ## Issue How the two-pronged test of [[Aguilar v. Texas]] \u2014 the informant's basis of knowledge and his veracity \u2014 applies when an informant's tip is partly corroborated by independent police investigation, and whether this affidavit established probable cause. ## Rule The tip is first assessed under *Aguilar*, and only then is corroboration considered.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-418",
      "page": null,
      "quote": "the informant's tip \u2014 even when corroborated to the extent indicated \u2014 was not sufficient to provide the basis for a finding of probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1969-01-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Spinelli v. United States",
    "varies_by_point": false,
    "scope_note": "Refined the Aguilar two-prong informant-tip test; the rigid Aguilar-Spinelli framework was abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": "462 U.S. 213",
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:abrogated"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jesse Jon Harbach",
          "cluster_id": 9493041,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Guardado",
          "cluster_id": 9391153,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Costa",
          "cluster_id": 4744366,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Marmon",
          "cluster_id": 10133414,
          "cite": [
            "303 Or. App. 469",
            "463 P.3d 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barreto",
          "cluster_id": 4690114,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4476634,
          "cite": [
            "96 N.E.3d 719",
            "93 Mass. App. Ct. 6"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Luna",
          "cluster_id": 4449164,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. (And",
          "cluster_id": 7171453,
          "cite": [
            "94 N.E.3d 435",
            "92 Mass. App. Ct. 1107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jordan",
          "cluster_id": 4406528,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Ramos",
          "cluster_id": 2827409,
          "cite": [
            "88 Mass. App. Ct. 68"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Courtney Bishop",
          "cluster_id": 2655823,
          "cite": [
            "431 S.W.3d 22",
            "2014 WL 888198",
            "2014 Tenn. LEXIS 189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alabama v. White",
          "cluster_id": 112454,
          "cite": [
            "110 L. Ed. 2d 301",
            "110 S. Ct. 2412",
            "496 U.S. 325",
            "1990 U.S. LEXIS 3053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Unger",
          "cluster_id": 1916834,
          "cite": [
            "749 N.W.2d 272",
            "278 Mich. App. 210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Idaho v. Wright",
          "cluster_id": 112488,
          "cite": [
            "111 L. Ed. 2d 638",
            "110 S. Ct. 3139",
            "497 U.S. 805",
            "1990 U.S. LEXIS 3461",
            "30 Fed. R. Serv. 24",
            "58 U.S.L.W. 5036"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiteley v. Warden, Wyoming State Penitentiary",
          "cluster_id": 108297,
          "cite": [
            "28 L. Ed. 2d 306",
            "91 S. Ct. 1031",
            "401 U.S. 560",
            "1971 U.S. LEXIS 65",
            "58 Ohio Op. 2d 434"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harris",
          "cluster_id": 108379,
          "cite": [
            "29 L. Ed. 2d 723",
            "91 S. Ct. 2075",
            "403 U.S. 573",
            "1971 U.S. LEXIS 18"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Salinas",
          "cluster_id": 1423352,
          "cite": [
            "829 P.2d 1068",
            "119 Wash. 2d 192",
            "1992 Wash. LEXIS 146"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Janis",
          "cluster_id": 109539,
          "cite": [
            "49 L. Ed. 2d 1046",
            "96 S. Ct. 3021",
            "428 U.S. 433",
            "1976 U.S. LEXIS 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. Mississippi",
          "cluster_id": 107912,
          "cite": [
            "22 L. Ed. 2d 676",
            "89 S. Ct. 1394",
            "394 U.S. 721",
            "1969 U.S. LEXIS 1869"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desist v. United States",
          "cluster_id": 107875,
          "cite": [
            "22 L. Ed. 2d 248",
            "89 S. Ct. 1030",
            "394 U.S. 244",
            "1969 U.S. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Nelson",
          "cluster_id": 107877,
          "cite": [
            "22 L. Ed. 2d 281",
            "89 S. Ct. 1082",
            "394 U.S. 286",
            "1969 U.S. LEXIS 2161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 110754,
          "cite": [
            "73 L. Ed. 2d 202",
            "102 S. Ct. 2579",
            "457 U.S. 537",
            "1982 U.S. LEXIS 134",
            "50 U.S.L.W. 4742"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zurcher v. Stanford Daily",
          "cluster_id": 109876,
          "cite": [
            "56 L. Ed. 2d 525",
            "98 S. Ct. 1970",
            "436 U.S. 547",
            "1978 U.S. LEXIS 98"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107831 OR 9423895 OR 9423896 OR 9423897 OR 9423898 OR 9423899) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEzOTcxMjAwMDAwJnM9MjE1NzkxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107831+OR+9423895+OR+9423896+OR+9423897+OR+9423898+OR+9423899%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(107831 OR 9423895 OR 9423896 OR 9423897 OR 9423898 OR 9423899)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNzkmcz0xODkxNjM4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107831+OR+9423895+OR+9423896+OR+9423897+OR+9423898+OR+9423899%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107831 OR 9423895 OR 9423896 OR 9423897 OR 9423898 OR 9423899)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 1,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107831 OR 9423895 OR 9423896 OR 9423897 OR 9423898 OR 9423899)",
    "indexed_citing_opinions": 4302,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107831,
        "count": 3864,
        "count_source": "search"
      },
      {
        "opinion_id": 9423895,
        "count": 545,
        "count_source": "search"
      },
      {
        "opinion_id": 9423896,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423897,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423898,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423899,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6224,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/spinelli-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NzAxOSZzPTk0OTMwNDEmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28107831+OR+9423895+OR+9423896+OR+9423897+OR+9423898+OR+9423899%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107831,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 107058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 107325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 277169,
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
    "date_created": "2026-07-05T20:16:44Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: abrogated -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:16:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:16:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:16:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Spinelli v. United States

```
<div>
<center><b><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U.S. 410</a></span> (1969)</b></center>
<center><h1>SPINELLI<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 8.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 16-17, 1968.</center>
<center>Decided January 27, 1969.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT.
<p><span class="star-pagination">*411</span> <i>Irl B. Baris</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Joseph J. Connolly</i> argued the cause for the United States, <i>pro hac vice.</i> With him on the brief were <i>Solicitor General Griswold, Assistant Attorney General Vinson, Beatrice Rosenberg,</i> and <i>Sidney M. Glazer.</i></p>
<p>MR. JUSTICE HARLAN delivered the opinion of the Court.</p>
<p>William Spinelli was convicted under <span class="citation no-link">18 U. S. C. § 1952</span><sup>[1]</sup> of traveling to St. Louis, Missouri, from a nearby Illinois suburb with the intention of conducting gambling activities proscribed by Missouri law. See <span class="citation no-link">Mo. Rev. Stat. § 563.360</span> (1959). At every appropriate stage in the proceedings in the lower courts, the petitioner challenged the constitutionality of the warrant which authorized the FBI search that uncovered the evidence necessary for his conviction. At each stage, Spinelli's challenge was treated in a different way. At a pretrial suppression hearing, the United States District Court for the Eastern District of Missouri held that Spinelli <span class="star-pagination">*412</span> lacked standing to raise a Fourth Amendment objection. A unanimous panel of the Court of Appeals for the Eighth Circuit rejected the District Court's ground, a majority holding further that the warrant was issued without probable cause. After an <i>en banc</i> rehearing, the Court of Appeals sustained the warrant and affirmed the conviction by a vote of six to two. <span class="citation" data-id="9452981"><a href="/opinion/277169/william-spinelli-v-united-states/" aria-description="Citation for case: William Spinelli v. United States">382 F. 2d 871</a></span>. Both the majority and dissenting <i>en banc</i> opinions reflect a most conscientious effort to apply the principles we announced in <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), to a factual situation whose basic characteristics have not been at all uncommon in recent search warrant cases. Believing it desirable that the principles of <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> should be further explicated, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./390/942/">390 U. S. 942</a></span>, our writ being later limited to the question of the constitutional validity of the search and seizure.<sup>[2]</sup> <span class="citation multiple-matches"><a href="/c/U.%20S./391/933/">391 U. S. 933</a></span>. For reasons that follow we reverse.</p>
<p>In <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> a search warrant had issued upon an affidavit of police officers who swore only that they had "received reliable information from a credible person and do believe" that narcotics were being illegally stored on the described premises. While recognizing that the constitutional requirement of probable cause can be satisfied by hearsay information, this Court held the <span class="star-pagination">*413</span> affidavit inadequate for two reasons. First, the application failed to set forth any of the "underlying circumstances" necessary to enable the magistrate independently to judge of the validity of the informant's conclusion that the narcotics were where he said they were. Second, the affiant-officers did not attempt to support their claim that their informant was " `credible' or his information `reliable.' " The Government is, however, quite right in saying that the FBI affidavit in the present case is more ample than that in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>.</i> Not only does it contain a report from an anonymous informant, but it also contains a report of an independent FBI investigation which is said to corroborate the informant's tip. We are, then, required to delineate the manner in which <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s two-pronged test should be applied in these circumstances.</p>
<p>In essence, the affidavit, reproduced in full in the Appendix to this opinion, contained the following allegations:<sup>[3]</sup></p>
<p>1. The FBI had kept track of Spinelli's movements on five days during the month of August 1965. On four of these occasions, Spinelli was seen crossing one of two bridges leading from Illinois into St. Louis, Missouri, between 11 a. m. and 12:15 p. m. On four of the five days, Spinelli was also seen parking his car in a lot used by residents of an apartment house at 1108 Indian Circle Drive in St. Louis, between 3:30 p. m. and 4:45 p. m.<sup>[4]</sup><span class="star-pagination">*414</span> On one day, Spinelli was followed further and seen to enter a particular apartment in the building.</p>
<p>2. An FBI check with the telephone company revealed that this apartment contained two telephones listed under the name of Grace P. Hagen, and carrying the numbers WYdown 4-0029 and WYdown 4-0136.</p>
<p>3. The application stated that "William Spinelli is known to this affiant and to federal law enforcement agents and local law enforcement agents as a bookmaker, an associate of bookmakers, a gambler, and an associate of gamblers."</p>
<p>4. Finally, it was stated that the FBI "has been informed by a confidential reliable informant that William Spinelli is operating a handbook and accepting wagers and disseminating wagering information by means of the telephones which have been assigned the numbers WYdown 4-0029 and WYdown 4-0136."</p>
<p>There can be no question that the last item mentioned, detailing the informant's tip, has a fundamental place in this warrant application. Without it, probable cause could not be established. The first two items reflect only innocent-seeming activity and data. Spinelli's travels to and from the apartment building and his entry into a particular apartment on one occasion could hardly be taken as bespeaking gambling activity; and there is surely nothing unusual about an apartment containing two separate telephones. Many a householder indulges himself in this petty luxury. Finally, the allegation that Spinelli was "known" to the affiant and to other federal and local law enforcement officers as a gambler and an associate of gamblers is but a bald and unilluminating assertion of suspicion that is entitled to no weight in appraising the magistrate's decision. <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#46" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41, 46</a></span> (1933).</p>
<p><span class="star-pagination">*415</span> So much indeed the Government does not deny. Rather, following the reasoning of the Court of Appeals, the Government claims that the informant's tip gives a suspicious color to the FBI's reports detailing Spinelli's innocent-seeming conduct and that, conversely, the FBI's surveillance corroborates the informant's tip, thereby entitling it to more weight. It is true, of course, that the magistrate is obligated to render a judgment based upon a common-sense reading of the entire affidavit. <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965). We believe, however, that the "totality of circumstances" approach taken by the Court of Appeals paints with too broad a brush. Where, as here, the informer's tip is a necessary element in a finding of probable cause, its proper weight must be determined by a more precise analysis.</p>
<p>The informer's report must first be measured against <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s standards so that its probative value can be assessed. If the tip is found inadequate under <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> the other allegations which corroborate the information contained in the hearsay report should then be considered. At this stage as well, however, the standards enunciated in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> must inform the magistrate's decision. He must ask: Can it fairly be said that the tip, even when certain parts of it have been corroborated by independent sources, is as trustworthy as a tip which would pass <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s tests without independent corroboration? <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> is relevant at this stage of the inquiry as well because the tests it establishes were designed to implement the long-standing principle that probable cause must be determined by a "neutral and detached magistrate," and not by "the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). A magistrate cannot be said to have properly discharged his constitutional duty if he relies on an informer's tip whicheven <span class="star-pagination">*416</span> when partially corroboratedis not as reliable as one which passes <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s requirements when standing alone.</p>
<p>Applying these principles to the present case, we first consider the weight to be given the informer's tip when it is considered apart from the rest of the affidavit. It is clear that a Commissioner could not credit it without abdicating his constitutional function. Though the affiant swore that his confidant was "reliable," he offered the magistrate no reason in support of this conclusion. Perhaps even more important is the fact that <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s other test has not been satisfied. The tip does not contain a sufficient statement of the underlying circumstances from which the informer concluded that Spinelli was running a bookmaking operation. We are not told how the FBI's source received his informationit is not alleged that the informant personally observed Spinelli at work or that he had ever placed a bet with him. Moreover, if the informant came by the information indirectly, he did not explain why his sources were reliable. Cf. <i>Jaben</i> v. <i>United States,</i> <span class="citation" data-id="9423037"><a href="/opinion/107058/jaben-v-united-states/" aria-description="Citation for case: Jaben v. United States">381 U. S. 214</a></span> (1965). In the absence of a statement detailing the manner in which the information was gathered, it is especially important that the tip describe the accused's criminal activity in sufficient detail that the magistrate may know that he is relying on something more substantial than a casual rumor circulating in the underworld or an accusation based merely on an individual's general reputation.</p>
<p>The detail provided by the informant in <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), provides a suitable benchmark. While Hereford, the Government's informer in that case, did not state the way in which he had obtained his information, he reported that Draper had gone to Chicago the day before by train and that he would return to Denver by train with three ounces of heroin on one of two specified mornings. Moreover, <span class="star-pagination">*417</span> Hereford went on to describe, with minute particularity, the clothes that Draper would be wearing upon his arrival at the Denver station. A magistrate, when confronted with such detail, could reasonably infer that the informant had gained his information in a reliable way.<sup>[5]</sup> Such an inference cannot be made in the present case. Here, the only facts supplied were that Spinelli was using two specified telephones and that these phones were being used in gambling operations. This meager report could easily have been obtained from an offhand remark heard at a neighborhood bar.</p>
<p>Nor do we believe that the patent doubts <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> raises as to the report's reliability are adequately resolved by a consideration of the allegations detailing the FBI's independent investigative efforts. At most, these allegations indicated that Spinelli could have used the telephones specified by the informant for some purpose. This cannot by itself be said to support both the inference that the informer was generally trustworthy and that he had made his charge against Spinelli on the basis of information obtained in a reliable way. Once again, <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> provides a relevant comparison. Independent police work in that case corroborated much more than one small detail that had been provided by the informant. There, the police, upon meeting the inbound Denver train on the second morning specified by informer Hereford, saw a man whose dress corresponded precisely to Hereford's detailed description. It was then apparent that the informant had not been fabricating his report out of whole cloth; since the report was of the sort which in common experience may be recognized as having been <span class="star-pagination">*418</span> obtained in a reliable way, it was perfectly clear that probable cause had been established.</p>
<p>We conclude, then, that in the present case the informant's tipeven when corroborated to the extent indicated was not sufficient to provide the basis for a finding of probable cause. This is not to say that the tip was so insubstantial that it could not properly have counted in the magistrate's determination. Rather, it needed some further support. When we look to the other parts of the application, however, we find nothing alleged which would permit the suspicions engendered by the informant's report to ripen into a judgment that a crime was probably being committed. As we have already seen, the allegations detailing the FBI's surveillance of Spinelli and its investigation of the telephone company records contain no suggestion of criminal conduct when taken by themselvesand they are not endowed with an aura of suspicion by virtue of the informer's tip. Nor do we find that the FBI's reports take on a sinister color when read in light of common knowledge that bookmaking is often carried on over the telephone and from premises ostensibly used by others for perfectly normal purposes. Such an argument would carry weight in a situation in which the premises contain an unusual number of telephones or abnormal activity is observed, cf. <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#302" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 302</a></span> (1967), but it does not fit this case where neither of these factors is present.<sup>[6]</sup> All that remains to be considered is the flat statement that Spinelli was "known" to the FBI and others as a gambler. But just as a simple assertion of police suspicion is not itself a sufficient basis for a magistrate's finding of probable cause, we do not believe it may be used to give <span class="star-pagination">*419</span> additional weight to allegations that would otherwise be insufficient.</p>
<p>The affidavit, then, falls short of the standards set forth in <i>Aguilar, Draper,</i> and our other decisions that give content to the notion of probable cause.<sup>[7]</sup> In holding as we have done, we do not retreat from the established propositions that only the probability, and not a prima facie showing, of criminal activity is the standard of probable cause, <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964); that affidavits of probable cause are tested by much less rigorous standards than those governing the admissibility of evidence at trial, <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#311" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 311</a></span> (1967); that in judging probable cause issuing magistrates are not to be confined by niggardly limitations or by restrictions on the use of their common sense, <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965); and that their determination of probable cause should be paid great deference by reviewing courts, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270-271</a></span> (1960). But we cannot sustain this warrant without diluting important safeguards that assure that the judgment of a disinterested judicial officer will interpose itself between the police and the citizenry.<sup>[8]</sup></p>
<p><span class="star-pagination">*420</span> The judgment of the Court of Appeals is reversed and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE MARSHALL took no part in the consideration or decision of this case.</p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT.</h2>
<p></p>
<h2>AFFIDAVIT IN SUPPORT OF SEARCH WARRANT.</h2>
<p>I, Robert L. Bender, being duly sworn, depose and say that I am a Special Agent of the Federal Bureau of Investigation, and as such am authorized to make searches and seizures.</p>
<p>That on August 6, 1965, at approximately 11:44 a. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation driving a 1964 Ford convertible, Missouri license HC3-649, onto the Eastern approach of the Veterans Bridge leading from East St. Louis, Illinois, to St. Louis, Missouri.</p>
<p>That on August 11, 1965, at approximately 11:16 a. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation driving a 1964 Ford convertible, Missouri license HC3-649, onto the Eastern approach of the Eads Bridge leading from East St. Louis, Illinois, to St. Louis, Missouri.</p>
<p>Further, at approximately 11:18 a. m. on August 11, 1965, I observed William Spinelli driving the aforesaid Ford convertible from the Western approach of the Eads Bridge into St. Louis, Missouri.</p>
<p>Further, at approximately 4:40 p. m. on August 11, 1965, I observed the aforesaid Ford convertible, bearing Missouri license HC3-649, parked in a parking lot used by residents of The Chieftain Manor Apartments, approximately one block east of 1108 Indian Circle Drive.</p>
<p>On August 12, 1965, at approximately 12:07 p. m., <span class="star-pagination">*421</span> William Spinelli was observed by an Agent of the Federal Bureau of Investigation driving the aforesaid 1964 Ford convertible onto the Eastern approach of the Veterans Bridge from East St. Louis, Illinois, in the direction of St. Louis, Missouri.</p>
<p>Further, on August 12, 1965, at approximately 3:46 p. m., I observed William Spinelli driving the aforesaid 1964 Ford convertible onto the parking lot used by the residents of The Chieftain Manor Apartments approximately one block east of 1108 Indian Circle Drive.</p>
<p>Further, on August 12, 1965, at approximately 3:49 p. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation entering the front entrance of the two-story apartment building located at 1108 Indian Circle Drive, this building being one of The Chieftain Manor Apartments.</p>
<p>On August 13, 1965, at approximately 11:08 a. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation driving the aforesaid Ford convertible onto the Eastern approach of the Eads Bridge from East St. Louis, Illinois, heading towards St. Louis, Missouri.</p>
<p>Further, on August 13, 1965, at approximately 11:11 a. m., I observed William Spinelli driving the aforesaid Ford convertible from the Western approach of the Eads Bridge into St. Louis, Missouri.</p>
<p>Further, on August 13, 1965, at approximately 3:45 p. m., I observed William Spinelli driving the aforesaid 1964 Ford convertible onto the parking area used by residents of The Chieftain Manor Apartments, said parking area being approximately one block from 1108 Indian Circle Drive.</p>
<p>Further, on August 13, 1965, at approximately 3:55 p. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation entering the corner apartment located on the second floor in the southwest corner, known as Apartment F, of the two-story <span class="star-pagination">*422</span> apartment building known and numbered as 1108 Indian Circle Drive.</p>
<p>On August 16, 1965, at approximately 3:22 p. m., I observed William Spinelli driving the aforesaid Ford convertible onto the parking lot used by the residents of The Chieftain Manor Apartments approximately one block east of 1108 Indian Circle Drive.</p>
<p>Further, an Agent of the F. B. I. observed William Spinelli alight from the aforesaid Ford convertible and walk toward the apartment building located at 1108 Indian Circle Drive.</p>
<p>The records of the Southwestern Bell Telephone Company reflect that there are two telephones located in the southwest corner apartment on the second floor of the apartment building located at 1108 Indian Circle Drive under the name of Grace P. Hagen. The numbers listed in the Southwestern Bell Telephone Company records for the aforesaid telephones are WYdown 4-0029 and WYdown 4-0136.</p>
<p>William Spinelli is known to this affiant and to federal law enforcement agents and local law enforcement agents as a bookmaker, an associate of bookmakers, a gambler, and an associate of gamblers.</p>
<p>The Federal Bureau of Investigation has been informed by a confidential reliable informant that William Spinelli is operating a handbook and accepting wagers and disseminating wagering information by means of the telephones which have been assigned the numbers WYdown 4-0029 and WYdown 4-0136.</p>
              /s/ Robert L. Bender,
                  Robert L. Bender,
                   Special Agent, Federal Bureau
                     of Investigation.
<p>Subscribed and sworn to before me this 18th day of August, 1965, at St. Louis, Missouri.</p>
                              /s/ William R. O'Toole.
<p><span class="star-pagination">*423</span> MR. JUSTICE WHITE, concurring.</p>
<p>An investigator's affidavit that he has seen gambling equipment being moved into a house at a specified address will support the issuance of a search warrant. The oath affirms the honesty of the statement and negatives the lie or imagination. Personal observation attests to the facts assertedthat there is gambling equipment on the premises at the named address.</p>
<p>But if the officer simply avers, without more, that there is gambling paraphernalia on certain premises, the warrant should not issue, even though the belief of the officer is an honest one, as evidenced by his oath, and even though the magistrate knows him to be an experienced, intelligent officer who has been reliable in the past. This much was settled in <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933), where the Court held insufficient an officer's affidavit swearing he had cause to believe that there was illegal liquor on the premises for which the warrant was sought. The unsupported assertion or belief of the officer does not satisfy the requirement of probable cause. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#269" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 269</a></span> (1960); <i>Grau</i> v. <i>United States,</i> <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">287 U. S. 124</a></span> (1932); <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 29</a></span> (1927).</p>
<p>What is missing in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> and like cases is a statement of the basis for the affiant's believing the facts contained in the affidavitthe good "cause" which the officer in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> said he had. If an officer swears that there is gambling equipment at a certain address, the possibilities are (1) that he has seen the equipment; (2) that he has observed or perceived facts from which the presence of the equipment may reasonably be inferred; and (3) that he has obtained the information from someone else. If (1) is true, the affidavit is good. But in (2), the affidavit is insufficient unless the perceived facts are given, for it is the magistrate, not the <span class="star-pagination">*424</span> officer, who is to judge the existence of probable cause. <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span> (1958); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). With respect to (3), where the officer's information is hearsay, no warrant should issue absent good cause for crediting that hearsay. Because an affidavit asserting, without more, the location of gambling equipment at a particular address does not claim personal observation of any of the facts by the officer, and because of the likelihood that the information came from an unidentified third party, affidavits of this type are unacceptable.</p>
<p>Neither should the warrant issue if the officer states that there is gambling equipment in a particular apartment and that his information comes from an informant, named or unnamed, since the honesty of the informant and the basis for his report are unknown. Nor would the missing elements be completely supplied by the officer's oath that the informant has often furnished reliable information in the past. This attests to the honesty of the informant, but <i>Aguilar</i> v. <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra</a></span></i><i>,</i> requires something moredid the information come from observation, or did the informant in turn receive it from another? Absent additional facts for believing the informant's report, his assertion stands no better than the oath of the officer to the same effect. Indeed, if the affidavit of an officer, known by the magistrate to be honest and experienced, stating that gambling equipment is located in a certain building is unacceptable, it would be quixotic if a similar statement from an honest informant were found to furnish probable cause. A strong argument can be made that both should be acceptable under the Fourth Amendment, but under our cases neither is. The past reliability of the informant can no more furnish probable cause for believing his <span class="star-pagination">*425</span> current report than can previous experience with the officer himself.</p>
<p>If the affidavit rests on hearsayan informant's report what is necessary under <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> is one of two things: the informant must declare either (1) that he has himself seen or perceived the fact or facts asserted; or (2) that his information is hearsay, but there is good reason for believing itperhaps one of the usual grounds for crediting hearsay information. The first presents few problems: since the report, although hearsay, purports to be first-hand observation, remaining doubt centers on the honesty of the informant, and that worry is dissipated by the officer's previous experience with the informant. The other basis for accepting the informant's report is more complicated. But if, for example, the informer's hearsay comes from one of the actors in the crime in the nature of admission against interest, the affidavit giving this information should be held sufficient.</p>
<p>I am inclined to agree with the majority that there are limited special circumstances in which an "honest" informant's report, if sufficiently detailed, will in effect verify itselfthat is, the magistrate when confronted with such detail could reasonably infer that the informant had gained his information in a reliable way. See <i>ante,</i> at 417. Detailed information may sometimes imply that the informant himself has observed the facts. Suppose an informant with whom an officer has had satisfactory experience states that there is gambling equipment in the living room of a specified apartment and describes in detail not only the equipment itself but also the appointments and furnishings in the apartment. Detail like this, if true at all, must rest on personal observation either of the informant or of someone else. If the latter, we know nothing of the third person's honesty or <span class="star-pagination">*426</span> sources; he may be making a wholly false report. But it is arguable that on these facts it was the informant himself who has perceived the facts, for the information reported is not usually the subject of casual, day-to-day conversation. Because the informant is honest and it is probable that he has viewed the facts, there is probable cause for the issuance of a warrant.</p>
<p>So too in the special circumstances of <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), the kind of information related by the informant is not generally sent ahead of a person's arrival in a city except to those who are intimately connected with making careful arrangements for meeting him. The informant, posited as honest, somehow had the reported facts, very likely from one of the actors in the plan, or as one of them himself. The majority's suggestion is that a warrant could have been obtained based only on the informer's report. I am inclined to agree, although it seems quite plain that if it may be so easily inferred from the affidavit that the informant has himself observed the facts or has them from an actor in the event, no possible harm could come from requiring a statement to that effect, thereby removing the difficult and recurring questions which arise in such situations.</p>
<p>Of course, <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> itself did not proceed on this basis. Instead, the Court pointed out that when the officer saw a person getting off the train at the specified time, dressed and conducting himself precisely as the informant had predicted, all but the critical fact with respect to possessing narcotics had then been verified and for that reason the officer had "reasonable grounds" to believe also that Draper was carrying narcotics. Unquestionably, verification of arrival time, dress, and gait reinforced the honesty of the informanthe had not reported a made-up story. But if what <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> stands for is that the existence of the tenth and critical fact <span class="star-pagination">*427</span> is made sufficiently probable to justify the issuance of a warrant by verifying nine other facts coming from the same source, I have my doubts about that case.</p>
<p>In the first place, the proposition is not that the tenth fact may be logically inferred from the other nine or that the tenth fact is usually found in conjunction with the other nine. No one would suggest that just anyone getting off the 10:30 train dressed as Draper was, with a brisk walk and carrying a zipper bag, should be arrested for carrying narcotics. The thrust of <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> is not that the verified facts have independent significance with respect to proof of the tenth. The argument instead relates to the reliability of the source: because an informant is right about some things, he is more probably right about other facts, usually the critical, unverified facts.</p>
<p>But the Court's cases have already rejected for Fourth Amendment purposes the notion that the past reliability of an officer is sufficient reason for believing his current assertions. Nor would it suffice, I suppose, if a reliable informant states there is gambling equipment in Apartment 607 and then proceeds to describe in detail Apartment 201, a description which is verified before applying for the warrant. He was right about 201, but that hardly makes him more believable about the equipment in 607. But what if he states that there are narcotics locked in a safe in Apartment 300, which is described in detail, and the apartment manager verifies everything but the contents of the safe? I doubt that the report about the narcotics is made appreciably more believable by the verification. The informant could still have gotten his information concerning the safe from others about whom nothing is known or could have inferred the presence of narcotics from circumstances which a magistrate would find unacceptable.</p>
<p>The tension between <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> and the <i>Nathanson-Aguilar</i> line of cases is evident from the course followed <span class="star-pagination">*428</span> by the majority opinion. First, it is held that the report from a reliable informant that Spinelli is using two telephones with specified numbers to conduct a gambling business plus Spinelli's reputation in police circles as a gambler does not add up to probable cause. This is wholly consistent with <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> and <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span>:</i> the informant did not reveal whether he had personally observed the facts or heard them from another and, if the latter, no basis for crediting the hearsay was presented. Nor were the facts, as MR. JUSTICE HARLAN says, of such a nature that they normally would be obtainable only by the personal observation of the informant himself. The police, however, did not stop with the informant's report. Independently, they established the existence of two phones having the given numbers and located them in an apartment house which Spinelli was regularly frequenting away from his home. There remained little question but that Spinelli was using the phones, and it was a fair inference that the use was not for domestic but for business purposes. The informant had claimed the business involved gambling. Since his specific information about Spinelli using two phones with particular numbers had been verified, did not his allegation about gambling thereby become sufficiently more believable if the <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> principle is to be given any scope at all? I would think so, particularly since the information from the informant which was verified was not neutral, irrelevant information but was material to proving the gambling allegation: two phones with different numbers in an apartment used away from home indicates a business use in an operation, like bookmaking, where multiple phones are needed. The <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> approach would reasonably justify the issuance of a warrant in this case, particularly since the police had some awareness of Spinelli's past activities. The majority, however, <span class="star-pagination">*429</span> while seemingly embracing <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>,</i> confines that case to its own facts. Pending full-scale reconsideration of that case, on the one hand, or of the <i>Nathanson-Aguilar</i> cases on the other, I join the opinion of the Court and the judgment of reversal, especially since a vote to affirm would produce an equally divided Court.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>In my view, this Court's decision in <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), was bad enough. That decision went very far toward elevating the magistrate's hearing for issuance of a search warrant to a full-fledged trial, where witnesses must be brought forward to attest personally to all the facts alleged. But not content with this, the Court today expands <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> to almost unbelievable proportions. Of course, it would strengthen the probable-cause presentation if eyewitnesses could testify that they saw the defendant commit the crime. It would be stronger still if these witnesses could explain in detail the nature of the sensual perceptions on which they based their "conclusion" that the person they had seen was the defendant and that he was responsible for the events they observed. Nothing in our Constitution, however, requires that the facts be established with that degree of certainty and with such elaborate specificity before a policeman can be authorized by a disinterested magistrate to conduct a carefully limited search.</p>
<p>The Fourth Amendment provides that "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." In this case a search warrant was issued supported by an oath and particularly describing the place to be searched and the things to be seized. The supporting oath was <span class="star-pagination">*430</span> three printed pages and the full text of it is included in an Appendix to the Court's opinion. The magistrate, I think properly, held the information set forth sufficient facts to show "probable cause" that the defendant was violating the law. Six members of the Court of Appeals also agreed that the affidavit was sufficient to show probable cause. A majority of this Court today holds, however, that the magistrate and all of these judges were wrong. In doing so, they substitute their own opinion for that of the local magistrate and the circuit judges, and reject the <i>en banc</i> factual conclusion of the Eighth Circuit and reverse the judgment based upon that factual conclusion. I cannot join in any such disposition of an issue so vital to the administration of justice, and dissent as vigorously as I can.</p>
<p>I repeat my belief that the affidavit given the magistrate was more than ample to show probable cause of the petitioner's guilt. The affidavit meticulously set out facts sufficient to show the following:</p>
<p>1. The petitioner had been shown going to and coming from a room in an apartment which contained two telephones listed under the name of another person. Nothing in the record indicates that the apartment was of that large and luxurious type which could only be occupied by a person to whom it would be a "petty luxury" to have two separate telephones, with different numbers, both listed under the name of a person who did not live there.</p>
<p>2. The petitioner's car had been observed parked in the apartment's parking lot. This fact was, of course, highly relevant in showing that the petitioner was extremely interested in some enterprise which was located in the apartment.</p>
<p>3. The FBI had been informed by a reliable informant that the petitioner was accepting wagering information by telephonesthe particular telephones located in the <span class="star-pagination">*431</span> apartment the defendant had been repeatedly visiting. Unless the Court, going beyond the requirements of the Fourth Amendment, wishes to require magistrates to hold trials before issuing warrants, it is not necessary as the Court holdsto have the affiant explain "the underlying circumstances from which the informer concluded that Spinelli was running a bookmaking operation." <i>Ante,</i> at 416.</p>
<p>4. The petitioner was known by federal and local law enforcement agents as a bookmaker and an associate of gamblers. I cannot agree with the Court that this knowledge was only a "bald and unilluminating assertion of suspicion that is entitled to no weight in appraising the magistrate's decision." <i>Ante,</i> at 414. Although the statement is hearsay that might not be admissible in a regular trial, everyone knows, unless he shuts his eyes to the realities of life, that this is a relevant fact which, together with other circumstances, might indicate a factual probability that gambling is taking place.</p>
<p>The foregoing facts should be enough to constitute probable cause for anyone who does not believe that the only way to obtain a search warrant is to prove beyond a reasonable doubt that a defendant is guilty. Even <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> on which the Court relies, cannot support the contrary result, at least as that decision was written before today's massive escalation of it. In <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> the Court dealt with an affidavit that stated only:</p>
<blockquote>"Affiants have received reliable information from a credible person and do believe that heroin . . . and other narcotics and narcotic paraphernalia are being kept at the above described premises for the purpose of sale and use contrary to the provisions of the law." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109</a></span>.</blockquote>
<p>The Court held, over the dissent of Mr. Justice Clark, MR. JUSTICE STEWART, and myself, that this unsupported conclusion of an unidentified informant provided no basis <span class="star-pagination">*432</span> for the magistrate to make an independent judgment as to the persuasiveness of the facts relied upon to show probable cause. Here, of course, we have much more, and the Court in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> was careful to point out that additional information of the kind presented in the affidavit before us now would be highly relevant:</p>
<blockquote>"If the fact and results of such a surveillance had been appropriately presented to the magistrate, this would, of course, present an entirely different case." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109, n. 1</a></span>.</blockquote>
<p>In the present case even the two-judge minority of the court below recognized, as this Court seems to recognize today, that this additional information took the case beyond the rule of <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>.</i> Six of the other circuit judges disagreed with the two dissenting judges, finding that all the circumstances considered together could support a reasonable judgment that gambling probably was taking place. I fully agree with this carefully considered opinion of the court below.</p>
<p>I regret to say I consider today's decision an indefensible departure from the principles of our former cases. Less than four years ago we reaffirmed these principles in <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965):</p>
<blockquote>"If the teachings of the Court's cases are to be followed and the constitutional policy served, affidavits for search warrants . . . must be tested and interpreted by magistrates and courts in a commonsense and realistic fashion. . . . Technical requirements of elaborate specificity once exacted under common law pleadings have no proper place in this area."</blockquote>
<p>See also <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span> (1931).</p>
<p>Departures of this kind are responsible for considerable uneasiness in our lower courts, and I must say I <span class="star-pagination">*433</span> am deeply troubled by the statements of Judge Gibson in the court below:</p>
<blockquote>"I am, indeed, disturbed by decision after decision of our courts which place increasingly technical burdens upon law enforcement officials. I am disturbed by these decisions that appear to relentlessly chip away at the ever narrowing area of effective police operation. I believe the holdings in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> and <i>Rugendorf</i> v. <i>United States,</i> <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span> (1964) are sufficient to protect the privacy of individuals from hastily conceived intrusions, and I do not think the limitations and requirements on the issuance of search warrants should be expanded by setting up over-technical requirements approaching the now discarded pitfalls of common law pleadings. Moreover, if we become increasingly technical and rigid in our demands upon police officers, I fear we make it increasingly easy for criminals to operate, detected but unpunished. I feel the significant movement of the law beyond its present state is unwarranted, unneeded, and dangerous to law enforcement efficiency." (Dissenting from panel opinion.)</blockquote>
<p>The Court of Appeals in this case took a sensible view of the Fourth Amendment, and I would wholeheartedly affirm its decision.</p>
<p><i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, decided in 1961, held for the first time that the Fourth Amendment and the exclusionary rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914) are now applicable to the States. That Amendment provides that search warrants shall not be issued without probable cause. The existence of probable cause is a factual matter that calls for the determination of a factual question. While no statistics are immediately available, questions of probable cause to issue search <span class="star-pagination">*434</span> warrants and to make arrests are doubtless involved in many thousands of cases in state courts. All of those probable-cause state cases are now potentially reviewable by this Court. It is, of course, physically impossible for this Court to review the evidence in all or even a substantial percentage of those cases. Consequently, whether desirable or not, we must inevitably accept most of the fact findings of the state courts, particularly when, as here in a federal case, both the trial and appellate courts have decided the facts the same way. It cannot be said that the trial judge and six members of the Court of Appeals committed flagrant error in finding from evidence that the magistrate had probable cause to issue the search warrant here. It seems to me that this Court would best serve itself and the administration of justice by accepting the judgment of the two courts below. After all, they too are lawyers and judges, and much closer to the practical, everyday affairs of life than we are.</p>
<p>Notwithstanding the Court's belief to the contrary, I think that in holding as it does, the Court does:</p>
<blockquote>"retreat from the established propositions that only the probability, and not a prima facie showing, of criminal activity is the standard of probable cause, <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964); that affidavits of probable cause are tested by much less rigorous standards than those governing the admissibility of evidence at trial, <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#311" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 311</a></span> (1967); that in judging probable cause issuing magistrates are not to be confined by niggardly limitations or by restrictions on the use of their common sense, <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965); and that their determination of probable cause should be paid great deference by reviewing courts, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270-271</a></span> (1960)." <i>Ante,</i> at 419.</blockquote>
<p><span class="star-pagination">*435</span> In fact, I believe the Court is moving rapidly, through complex analyses and obfuscatory language, toward the holding that no magistrate can issue a warrant unless according to some unknown standard of proof he can be persuaded that the suspect defendant is actually guilty of a crime. I would affirm this conviction.</p>
<p>MR. JUSTICE FORTAS, dissenting.</p>
<p>My Brother HARLAN's opinion for the Court is animated by a conviction which I share that "[t]he security of one's privacy against arbitrary intrusion by the policewhich is at the core of the Fourth Amendment is basic to a free society." <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949).</p>
<p>We may well insist upon a sympathetic and even an indulgent view of the latitude which must be accorded to the police for performance of their vital task; but only a foolish or careless people will deduce from this that the public welfare requires or permits the police to disregard the restraints on their actions which historic struggles for freedom have developed for the protection of liberty and dignity of citizens against arbitrary state power.</p>
<p>As Justice Jackson (dissenting) stated in <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#180" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 180-181</a></span> (1949):</p>
<blockquote>"[The provisions of the Fourth Amendment] are not mere second-class rights but belong in the catalog of indispensable freedoms. Among deprivations of rights, none is so effective in cowing a population, crushing the spirit of the individual and putting terror in every heart. Uncontrolled search and seizure is one of the first and most effective weapons in the arsenal of every arbitrary government. And one need only briefly to have dwelt and worked among a people possessed of many admirable qualities but deprived of these rights to know that the <span class="star-pagination">*436</span> human personality deteriorates and dignity and self-reliance disappear where homes, persons and possessions are subject at any hour to unheralded search and seizure by the police."</blockquote>
<p>History<sup>[1]</sup> teaches us that this protection requires that the judgment of a judicial officer be interposed between the police, hot in pursuit of their appointed target, and the citizen;<sup>[2]</sup> that the judicial officer must judge and not merely rubber-stamp; and that his judgment must be based upon judicially reliable facts adequate to demonstrate that the search is justified by the probability that it will yield the fruits or instruments of crimeor, as this Court has only recently ruled, tangible evidence of its commission.<sup>[3]</sup> The exceptions to the requirement of a search warrant have always been narrowly restricted<sup>[4]</sup> because of this Court's long-standing awareness of the fundamental role of the magistrate's judgment in the preservation of a proper balance between individual freedom and state power. See <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#700" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 700</a></span> (1948).</p>
<p>Today's decision deals, not with the necessity of obtaining a warrant prior to search, but with the difficult problem of the nature of the showing that must be made <span class="star-pagination">*437</span> before the magistrate to justify his issuance of a search warrant. While I do not subscribe to the criticism of the majority expressed by my Brother BLACK in dissent, I believewith all respectthat the majority is in error in holding that the affidavit supporting the warrant in this case is constitutionally inadequate.</p>
<p>The affidavit is unusually long and detailed. In fact, it recites so many minute and detailed facts developed in the course of the investigation of Spinelli that its substance is somewhat obscured. It is paradoxical that this very fullness of the affidavit may be the source of the constitutional infirmity that the majority finds. Stated in language more direct and less circumstantial than that used by the FBI agent who executed the affidavit, it sets forth that the FBI has been informed that Spinelli is accepting wagers by means of telephones numbered WY 4-0029 and WY 4-0136; that Spinelli is known to the affiant agent and to law enforcement agencies as a bookmaker; that telephones numbered WY 4-0029 and WY 4-0136 are located in a certain apartment; that Spinelli was placed under surveillance and his observed movements were such as to show his use of that apartment and to indicate that he frequented the apartment on a regular basis.</p>
<p><i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), holds that the reference in an affidavit to information described only as received from "a confidential reliable informant," standing alone, is not an adequate basis for issuance of a search warrant. The majority agrees that the "FBI affidavit in the present case is more ample than that in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i>" but concludes that it is nevertheless constitutionally inadequate. The majority states that the present affidavit fails to meet the "two-pronged test" of <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> because (a) it does not set forth the basis for the assertion that the informer is "reliable" and (b) it fails to state the "underlying circumstances" upon which the <span class="star-pagination">*438</span> informant based his conclusion that Spinelli was engaged in bookmaking.</p>
<p>The majority acknowledges, however, that its reference to a "two-pronged test" should not be understood as meaning that an affidavit deficient in these respects is necessarily inadequate to support a search warrant. Other facts and circumstances may be attested which will supply the evidence of probable cause needed to support the search warrant. On this general statement we are agreed. Our difference is that I believe such facts and circumstances are present in this case, and the majority arrives at the opposite conclusion.</p>
<p><i>Aguilar</i> expressly recognized that if, in that case, the affidavit's conclusory report of the informant's story had been supplemented by "the fact and results of . . . a surveillance. . . this would, of course, present an entirely different case." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109, n. 1</a></span>. In the present case, as I view it, the affidavit showed not only relevant surveillance, entitled to some probative weight for purposes of the issuance of a search warrant, but also additional, specific facts of significance and adequate reliability: that Spinelli was using two telephone numbers, identified by an "informant" as being used for bookmaking, in his illegal operations; that these telephones were in an identified apartment; and that Spinelli, a known bookmaker,<sup>[5]</sup> frequented the apartment. Certainly, this is enough.</p>
<p>A policeman's affidavit should not be judged as an entry in an essay contest. It is not "abracadabra."<sup>[6]</sup><span class="star-pagination">*439</span> As the majority recognizes, a policeman's affidavit is entitled to common-sense evaluation. So viewed, I conclude that the judgment of the Court of Appeals for the Eighth Circuit should be affirmed.</p>
<p>MR. JUSTICE STEWART, dissenting.</p>
<p>For substantially the reasons stated by my Brothers BLACK and FORTAS, I believe the warrant in this case was supported by a sufficient showing of probable cause. I would therefore affirm the judgment.</p>
<h2>NOTES</h2>
<p>[1]  The relevant portion of the statute reads:
</p>
<p>"(a) Whoever travels in interstate or foreign commerce or uses any facility in interstate . . . commerce . . . with intent to</p>
<p>.....</p>
<p>"(3) otherwise promote, manage, establish, carry on . . . any unlawful activity, and thereafter performs or attempts to perform any of the acts specified in subparagraphs (1), (2), and (3), shall be fined not more than $10,000 or imprisoned for not more than five years, or both.</p>
<p>"(b) As used in this section `unlawful activity' means (1) any business enterprise involving gambling . . . in violation of the laws of the State in which they are committed or of the United States . . . ."</p>
<p>[2]  We agree with the Court of Appeals that Spinelli has standing to raise his Fourth Amendment claim. The issue arises because at the time the FBI searched the apartment in which Spinelli was alleged to be conducting his bookmaking operation, the petitioner was not on the premises. Instead, the agents did not execute their search warrant until Spinelli was seen to leave the apartment, lock the door, and enter the hallway. At that point, petitioner was arrested, the key to the apartment was demanded of him, and the search commenced. Since petitioner would plainly have standing if he had been arrested inside the apartment, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 267</a></span> (1960), it cannot matter that the agents preferred to delay the arrest until petitioner stepped into the hallwayespecially when the FBI only managed to gain entry into the apartment by requiring petitioner to surrender his key.</p>
<p>[3]  It is, of course, of no consequence that the agents might have had additional information which could have been given to the Commissioner. "It is elementary that in passing on the validity of a warrant, the reviewing court may consider <i>only</i> information brought to the magistrate's attention." <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 109, n. 1</a></span> (emphasis in original). Since the Government does not argue that whatever additional information the agents may have possessed was sufficient to provide probable cause for the arrest, thereby justifying the resultant search as well, we need not consider that question.</p>
<p>[4]  No report was made as to Spinelli's movements during the period between his arrival in St. Louis at noon and his arrival at the parking lot in the late afternoon. In fact, the evidence at trial indicated that Spinelli frequented the offices of his stockbroker during this period.</p>
<p>[5]  While <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> involved the question whether the police had probable cause for an arrest without a warrant, the analysis required for an answer to this question is basically similar to that demanded of a magistrate when he considers whether a search warrant should issue.</p>
<p>[6]  A box containing three uninstalled telephones was found in the apartment, but only after execution of the search warrant.</p>
<p>[7]  In those cases in which this Court has found probable cause established, the showing made was much more substantial than the one made here. Thus, in <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#104" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 104</a></span> (1965), FBI agents observed repeated deliveries of loads of sugar in 60-pound bags, smelled the odor of fermenting mash, and heard " `sounds similar to that of a motor or a pump coming from the direction of' Ventresca's house." Again, in <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#303" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 303-304</a></span> (1967), the informant reported that McCray " `was selling narcotics and had narcotics on his person now in the vicinity of 47th and Calumet.' " When the police arrived at the intersection, they observed McCray engaging in various suspicious activities. <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#302" aria-description="Citation for case: McCray v. Illinois">386 U. S., at 302</a></span>.</p>
<p>[8]  In the view we have taken of this case, it becomes unnecessary to decide whether the search warrant was properly executed, or whether it sufficiently described the things that were seized.</p>
<p>[1]  "The knock at the door, whether by day or by night, as a prelude to a search, without authority of law but solely on the authority of the police, did not need the commentary of recent history to be condemned as inconsistent with the conception of human rights enshrined in the history and the basic constitutional documents of English-speaking peoples." <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#28" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 28</a></span> (1949). See <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#69" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 69-70</a></span> (1950) (Frankfurter, J., dissenting). See generally with respect to the history of the Fourth Amendment N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution (1937).</p>
<p>[2]  See <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948).</p>
<p>[3]  <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967).</p>
<p>[4]  See <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#311" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 311</a></span> (1967) (concurring opinion).</p>
<p>[5]  Although Spinelli's reputation standing alone would not, of course, justify the search, this Court has held that such a reputation may make the informer's report "much less subject to scepticism than would be such a charge against one without such a history." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960).</p>
<p>[6]  See <i>Time, Inc.</i> v. <i>Hill,</i> <span class="citation" data-id="9423311"><a href="/opinion/107325/time-inc-v-hill/#418" aria-description="Citation for case: Time, Inc. v. Hill">385 U. S. 374, 418</a></span> (1967) (dissent) (relating to jury instructions).</p>

</div>
```

---

## GROUP: content/cases/Thornton v. United States.md  (`case`, 7 assertions)

### content_page

```
---
title: "Thornton v. United States"
type: case
citation: "541 U.S. 615 (2004)"
parallel_cite: "124 S. Ct. 2127; 158 L. Ed. 2d 905"
neutral_cite: 2004 U.S. LEXIS 3681
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-05-24
docket: 03-5165
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 2004-05-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Thornton v. United States
  varies_by_point: true
  scope_note: "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest)."
  point_overrides:
    - point: legacy-limited-thornton-v-united-states
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Arizona v. Gant
          cluster_id: 145887
          cite: 556 U.S. 332
          field_ii: limited
      scope_note: "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest)."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/134746/thornton-v-united-states/"
  cluster_id: 134746
  opinion_id: 9434613
  identity_checked: true
homes:
  - page: "[[SIA Vehicles]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[New York v. Belton]]", "[[Arizona v. Gant]]", "[[Chimel v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile", "vehicle-search", "recent-occupant"]
holding: "New York v. Belton's rule permitting a vehicle search incident to an occupant's arrest applies even when the officer first makes contact after the arrestee has exited the vehicle — i.e., to a 'recent occupant' (later cabined by Arizona v. Gant's two-justification test)."
lake:
  record_id: Thornton v. United States
  status: verified
  projected_at: 2026-07-09
---

# Thornton v. United States

*541 U.S. 615 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — limited by [[Arizona v. Gant]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Nichols, in an unmarked car, noticed Marcus Thornton slow down to avoid driving next to him, and a license check showed the tags did not match the vehicle. Before Nichols could pull him over, Thornton parked and got out of his car. Nichols stopped him, obtained consent to a patdown, and found drugs in Thornton's pockets. Nichols arrested Thornton, handcuffed him, placed him in the patrol car, and then searched the passenger compartment of Thornton's vehicle, finding a handgun under the driver's seat. Thornton argued [[New York v. Belton]] did not apply because he was already outside the car when the officer first made contact.

## Issue
Whether *[[New York v. Belton|Belton]]*'s rule — allowing a search of a vehicle's passenger compartment incident to the lawful custodial arrest of an occupant — applies when the officer does not initiate contact until after the arrestee has stepped out of the vehicle (a "recent occupant").

## Rule
Yes. "[W]e . . . conclude that *Belton* governs even when an officer does not make contact until the person arrested has left the vehicle." — 541 U.S. at 617. ^pin-617

A "recent occupant" does not lose that status by having exited first: "[W]hile an arrestee's status as a 'recent occupant' may turn on his temporal or spatial relationship to the car at the time of the arrest and search, it certainly does not turn on whether he was inside or outside the car at the moment that the officer first initiated contact with him." — *Id.* at 622. ^pin-622

Thus: "So long as an arrestee is the sort of 'recent occupant' of a vehicle such as petitioner was here, officers may search that vehicle incident to the arrest." — *Id.* at 623–624. ^pin-623

## Application
Thornton had just driven and parked the car, stepping out only moments before Officer Nichols approached him, so he was a "recent occupant." The officer-safety and evidence-preservation concerns underlying *[[New York v. Belton|Belton]]* were no less present because Thornton exited before contact — the situation was equally volatile. A "contact initiation" rule turning on whether the suspect was in or out of the car when the officer first signaled would invite exactly the ad hoc, fact-specific inquiries *[[New York v. Belton|Belton]]* sought to avoid. The warrantless search of the passenger compartment incident to Thornton's arrest was therefore permissible, and the handgun was admissible.

## Conclusion
*[[New York v. Belton|Belton]]* applies to recent occupants; the vehicle search incident to Thornton's arrest was valid, and the judgment was affirmed.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Limited by [[Arizona v. Gant]] (2009):** *[[Arizona v. Gant|Gant]]* cabined the broad, automatic vehicle-search rule of *[[New York v. Belton|Belton]]* and *Thornton*. After *[[Arizona v. Gant|Gant]]*, a vehicle search incident to a recent occupant's arrest is permitted only when (1) the arrestee is unsecured and within reaching distance of the passenger compartment at the time of the search, or (2) it is reasonable to believe the vehicle contains evidence of the offense of arrest. On *Thornton*'s own facts the search would fail *[[Arizona v. Gant|Gant]]*'s first prong (Thornton was handcuffed in the patrol car) but could be analyzed under the second.

## Appears on
- [[SIA Vehicles]] — *Key — Progeny / Refinement*
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Thornton v. United States*, 541 U.S. 615 (2004) — https://www.courtlistener.com/opinion/134746/thornton-v-united-states/ — pinpoints: 617, 622, 623–624.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "71950f92236b3e8f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "541 U.S. 615 (2004)", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 3681", "official_citation_present": true, "parallel_cite": "124 S. Ct. 2127; 158 L. Ed. 2d 905", "title": "Thornton v. United States", "year": "2004"}}
{"assertion_id": "00c672bc8f347f84", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Vehicles"}, "payload": {"home": "SIA Vehicles", "role": "Key — Progeny / Refinement", "title": "Thornton v. United States"}}
{"assertion_id": "cb9989f6209ae264", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Related (cross-doctrine)", "title": "Thornton v. United States"}}
{"assertion_id": "f021359b0b86b58a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "New York v. Belton's rule permitting a vehicle search incident to an occupant's arrest applies even when the officer first makes contact after the arrestee has exited the vehicle — i.e., to a 'recent occupant' (later cabined by Arizona v. Gant's two-justification test).", "title": "Thornton v. United States"}}
{"assertion_id": "11fc7324bbd0e9a2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Thornton v. United States"}}
{"assertion_id": "a0715d7bc56421a3", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-thornton-v-united-states"}, "payload": {"by": [{"cite": "556 U.S. 332", "cluster_id": "145887", "field_ii": "limited", "name": "Arizona v. Gant"}], "field_i_validity": "caution", "point": "legacy-limited-thornton-v-united-states", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "Thornton v. United States"}}
{"assertion_id": "d28a45dd89022b98", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-05-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Thornton v. United States", "field_i_validity": "caution", "scope_note": "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest).", "title": "Thornton v. United States", "varies_by_point": "true"}}
```

### lake record — Thornton v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Thornton v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Thornton v. United States",
    "case_name_short": "Thornton",
    "case_name_full": "Thornton v. United States",
    "input_case_name": "Thornton v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-05-24",
    "year": 2004,
    "docket": "03-5165",
    "cluster_id": 134746,
    "lead_opinion_id": 9434613,
    "sibling_ids": [
      134746,
      9434613,
      9434614,
      9434615,
      9434616
    ],
    "absolute_url": "/opinion/134746/thornton-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "541 U.S. 615",
      "volume": "541",
      "reporter": "U.S.",
      "page": "615",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 2127",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 905",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "905",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 3681",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "3681",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "541 U.S. 615",
        "volume": "541",
        "reporter": "U.S.",
        "page": "615",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2127",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 905",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "905",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 3681",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "3681",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "541 U.S. 615",
    "official_selection": {
      "court_class": "scotus",
      "selected": "541 U.S. 615",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-617",
      "page": null,
      "quote": "). ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-622",
      "page": null,
      "quote": "recent occupant",
      "star_marker": "620",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 12831,
      "fragment": "#:~:text=%5Bwa%5Ds%20its-,recent%20occupant",
      "fragment_validated_at": "2026-07-09T23:46:10Z"
    },
    {
      "id": "pin-623",
      "page": null,
      "quote": "So long as an arrestee is the sort of 'recent occupant' of a vehicle such as petitioner was here, officers may search that vehicle incident to the arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "2004-05-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Thornton v. United States",
    "varies_by_point": true,
    "scope_note": "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest).",
    "point_overrides": [
      {
        "point": "legacy-limited-thornton-v-united-states",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Arizona v. Gant",
            "cluster_id": 145887,
            "cite": "556 U.S. 332",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest)."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": "556 U.S. 332",
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
          "name": "State of Indiana v. Justin Crager",
          "cluster_id": 4547157,
          "cite": [
            "113 N.E.3d 657"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
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
        "journal_ref": "Thornton v. United States:lane1_negative"
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
        "journal_ref": "Thornton v. United States:lane1_negative"
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
        "journal_ref": "Thornton v. United States:lane1_negative"
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
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hill v. State",
          "cluster_id": 1619349,
          "cite": [
            "303 S.W.3d 863",
            "2009 WL 3821453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monterio Desha Hill v. State",
          "cluster_id": 2855208,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Grooms v. United States",
          "cluster_id": 2621071,
          "cite": [
            "129 S. Ct. 1981",
            "556 U.S. 1231",
            "77 U.S.L.W. 3632",
            "173 L. Ed. 2d 1288",
            "2009 U.S. LEXIS 3469"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Megginson v. United States",
          "cluster_id": 2621069,
          "cite": [
            "129 S. Ct. 1982",
            "556 U.S. 1230",
            "77 U.S.L.W. 3631",
            "173 L. Ed. 2d 1288",
            "2009 U.S. LEXIS 3471"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vennus v. State",
          "cluster_id": 1496491,
          "cite": [
            "282 S.W.3d 70",
            "2009 Tex. Crim. App. LEXIS 977",
            "2009 WL 1066947"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams, 22924 (4-3-2009)",
          "cluster_id": 3956380,
          "cite": [
            "2009 Ohio 1627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bailey v. United States",
          "cluster_id": 820749,
          "cite": [
            "185 L. Ed. 2d 19",
            "133 S. Ct. 1031",
            "568 U.S. 186",
            "2013 U.S. LEXIS 1075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Robert Joseph Vance",
          "cluster_id": 4472492,
          "cite": [
            "790 N.W.2d 775",
            "2010 Iowa Sup. LEXIS 116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950015,
          "cite": [
            "423 S.W.3d 399",
            "2014 WL 714730",
            "2014 Tex. Crim. App. LEXIS 237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 2454018,
          "cite": [
            "253 P.3d 84",
            "171 Wash. 2d 292"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael A. Robinson",
          "cluster_id": 788500,
          "cite": [
            "390 F.3d 853",
            "65 Fed. R. Serv. 1188",
            "2004 U.S. App. LEXIS 24893",
            "2004 WL 2735246"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Valdez",
          "cluster_id": 2637812,
          "cite": [
            "224 P.3d 751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kory Ray Smith",
          "cluster_id": 788425,
          "cite": [
            "389 F.3d 944",
            "2004 U.S. App. LEXIS 24343",
            "2004 WL 2660594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peter Evans v. City of Zebulon, Georgia",
          "cluster_id": 76954,
          "cite": [
            "407 F.3d 1272",
            "2005 U.S. App. LEXIS 8071",
            "2005 WL 1076603"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vinton",
          "cluster_id": 187527,
          "cite": [
            "594 F.3d 14",
            "389 U.S. App. D.C. 199",
            "2010 U.S. App. LEXIS 2450",
            "2010 WL 392347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mora v. City of Gaithersburg, Md.",
          "cluster_id": 1025190,
          "cite": [
            "519 F.3d 216",
            "2008 U.S. App. LEXIS 4561",
            "2008 WL 565711"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rowell",
          "cluster_id": 2570155,
          "cite": [
            "188 P.3d 95",
            "144 N.M. 371",
            "2008 NMSC 041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wurie",
          "cluster_id": 870435,
          "cite": [
            "728 F.3d 1",
            "2013 U.S. App. LEXIS 9937",
            "2013 WL 2129119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Evans",
          "cluster_id": 5810664,
          "cite": [
            "200 Cal. App. 4th 735",
            "133 Cal. Rptr. 3d 323",
            "2011 Cal. App. LEXIS 1382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Baker",
          "cluster_id": 2600016,
          "cite": [
            "2010 UT 18",
            "229 P.3d 650",
            "651 Utah Adv. Rep. 25",
            "2010 Utah LEXIS 17",
            "2010 WL 841271"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Diaz",
          "cluster_id": 2367386,
          "cite": [
            "51 Cal. 4th 84",
            "244 P.3d 501",
            "119 Cal. Rptr. 3d 105",
            "2011 Cal. LEXIS 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(134746 OR 9434613 OR 9434614 OR 9434615 OR 9434616) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjMwNTk1MjAwMDAwJnM9MjA0NDUxNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28134746+OR+9434613+OR+9434614+OR+9434615+OR+9434616%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(134746 OR 9434613 OR 9434614 OR 9434615 OR 9434616)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MCZzPTEwNTc0NTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28134746+OR+9434613+OR+9434614+OR+9434615+OR+9434616%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(134746 OR 9434613 OR 9434614 OR 9434615 OR 9434616)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 0,
        "triage_snippet_classified": 21
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(134746 OR 9434613 OR 9434614 OR 9434615 OR 9434616)",
    "indexed_citing_opinions": 409,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 134746,
        "count": 365,
        "count_source": "search"
      },
      {
        "opinion_id": 9434613,
        "count": 51,
        "count_source": "search"
      },
      {
        "opinion_id": 9434614,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434615,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434616,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 660,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/thornton-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMzM1MDcmcz0xMDY0MjU2OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28134746+OR+9434613+OR+9434614+OR+9434615+OR+9434616%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 134746,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 112014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 112719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 133277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 195782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 347138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 360135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 360237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 371215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 382105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 382713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 382715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 509334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 520415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 607884,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 666017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 716780,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 721372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 762479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 768295,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 777993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 781516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 867520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 1102464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 1263396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 1391930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 1687668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T21:42:17Z",
    "date_modified": "2026-07-09T23:46:37Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:42:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:42:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:42:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Thornton v. United States

```
<opinion type="majority">
<author id="b715-4"><page-number citation-index="1" label="617">*617</page-number>Chief Justice Rehnquist</author>
<p id="ANk">delivered the opinion of the Court except as to footnote 4.</p>
<p id="b715-5">In <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), we held that when a police officer has made a lawful custodial arrest of an occupant of an automobile, the Fourth Amendment allows the officer to search the passenger compartment of that vehicle as a contemporaneous incident of arrest. We have granted certiorari twice before to determine whether <em>Bel-ton’s </em>rule is limited to situations where the officer makes contact with the occupant while the occupant is inside the vehicle, or whether it applies as well when the officer first makes contact with the arrestee after the latter has stepped out of his vehicle. We did not reach the merits in either of those two cases. <em>Arizona </em>v. <em>Gant, </em><span class="citation" data-id="133277"><a href="/opinion/133277/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">540 U. S. 963</a></span> (2003) (vacating and remanding for reconsideration in light of <em>State </em>v. <em>Dean, </em><span class="citation" data-id="867520"><a href="/opinion/867520/state-v-dean/" aria-description="Citation for case: State v. Dean">206 Ariz. 158</a></span>, <span class="citation" data-id="867520"><a href="/opinion/867520/state-v-dean/" aria-description="Citation for case: State v. Dean">76 P. 3d 429</a></span> (2003) (en bane)); <em>Florida </em>v. <em>Thomas, </em><span class="citation" data-id="118437"><a href="/opinion/118437/florida-v-thomas/" aria-description="Citation for case: Florida v. Thomas">532 U. S. 774</a></span> (2001) (dismissing for lack of jurisdiction). We now reach that question and conclude that <em>Bel-ton </em>governs even when an officer does not make contact until the person arrested has left the vehicle.</p>
<p id="b715-6">Officer Deion Nichols of the Norfolk, Virginia, Police Department, who was in uniform but driving an unmarked police car, first noticed petitioner Marcus Thornton when petitioner slowed down so as to avoid driving next to him. Nichols suspected that petitioner knew he was a police officer and for some reason did not want to pull next to him. His suspicions aroused, Nichols pulled off onto a side street <page-number citation-index="1" label="618">*618</page-number>and petitioner passed him. After petitioner passed him, Nichols ran a check on petitioner’s license tags, which revealed that the tags had been issued to a 1982 Chevy two-door and not to a Lincoln Town Car, the model of car petitioner was driving. Before Nichols had an opportunity to pull him over, petitioner drove into a parking lot, parked, and got out of the vehicle. Nichols saw petitioner leave his vehicle as he pulled in behind him. He parked the patrol car, accosted petitioner, and asked him for his driver’s license. He also told him that his license tags did not match the vehicle that he was driving.</p>
<p id="b716-4">Petitioner appeared nervous. He began rambling and licking his lips; he was sweating. Concerned for his safety, Nichols asked petitioner if he had any narcotics or weapons on him or in his vehicle. Petitioner said no. Nichols then asked petitioner if he could pat him down, to which petitioner agreed. Nichols felt a bulge in petitioner’s left front pocket and again asked him if he had any illegal narcotics on him. This time petitioner stated that he did, and he reached into his pocket and pulled out two individual bags, one containing three bags of marijuana and the other containing a large amount of crack cocaine. Nichols handcuffed petitioner, informed him that he was under arrest, and placed him in the back seat of the patrol car. He then searched petitioner’s vehicle and found a BryCo 9-millimeter handgun under the driver’s seat.</p>
<p id="b716-5">A grand jury charged petitioner with possession with intent to distribute cocaine base, <span class="citation no-link">84 Stat. 1260</span>, <span class="citation no-link">21 U. S. C. § 841</span>(a)(1), possession of a firearm after having been previously convicted of a crime punishable by a term of imprisonment exceeding one year, <span class="citation no-link">18 U. S. C. § 922</span>(g)(1), and possession of a firearm in furtherance of a drug trafficking crime, § 924(c)(1). Petitioner sought to suppress, <em>inter alia, </em>the firearm as the fruit of an unconstitutional search. After a hearing, the District Court denied petitioner’s motion to suppress, holding that the automobile search was valid under <page-number citation-index="1" label="619">*619</page-number><em>New York </em>v. <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton, supra,</a></span> </em>and alternatively that Nichols could have conducted an inventory search of the automobile. A jury convicted petitioner on all three counts; he was sentenced to 180 months’ imprisonment and 8 years of supervised release.</p>
<p id="b717-4">Petitioner appealed, challenging only the District Court’s denial of the suppression motion. He argued that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>was limited to situations where the officer initiated contact with an arrestee while he was still an occupant of the car. The United States Court of Appeals for the Fourth Circuit affirmed. <span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/" aria-description="Citation for case: United States v. Marcus Thornton">325 F. 3d 189</a></span> (2003). It held that “the historical rationales for the search incident to arrest doctrine — ‘the need to disarm the suspect in order to take him into custody’ and ‘the need to preserve evidence for later use at trial,’ ” <em><span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/" aria-description="Citation for case: United States v. Marcus Thornton">id.,</a></span> </em>at 195 (quoting <em>Knowles </em>v. <em>Iowa, </em><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#116" aria-description="Citation for case: Knowles v. Iowa">525 U. S. 113, 116</a></span> (1998)), did not require <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to be limited solely to situations in which suspects were still in their vehicles when approached by the police. Noting that petitioner conceded that he was in “close proximity, both temporally and spatially,” to his vehicle, the court concluded that the car was within petitioner’s immediate control, and thus Nichols’ search was reasonable under <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>.</em><footnotemark><em>1</em></footnotemark><em> </em><span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/#196" aria-description="Citation for case: United States v. Marcus Thornton">325 F. 3d, at 196</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./540/980/">540 U. S. 980</a></span> (2003), and now affirm.</p>
<p id="b717-5">In <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>an officer overtook a speeding vehicle on the New York Thruway and ordered its driver to pull over. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#455" aria-description="Citation for case: New York v. Belton">453 U. S., at 455</a></span>. Suspecting that the occupants possessed marijuana, the officer directed them to get out of the car and arrested them for unlawful possession. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#454" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 454-455</a></span>. He searched them and then searched the passenger compartment of the car. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#455" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 455</a></span>. We considered the constitutionally permissible scope of a search in these circumstances- and sought to lay down a workable rule governing that situation.</p>
<p id="b718-4"><page-number citation-index="1" label="620">*620</page-number>We first referred to <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), a case where the arrestee was arrested in his home, and we had described the scope of a search incident to a lawful arrest as the person of the arrestee and the area immediately surrounding him. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S., at 457</a></span> (citing <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><em>Chimel, supra, </em>at 763</a></span>). This rule was justified by the need to remove any weapon the arrestee might seek to use to resist arrest or to escape, and the need to prevent the concealment or destruction of evidence. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#457" aria-description="Citation for case: New York v. Belton">453 U. S., at 457</a></span>. Although easily stated, the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>principle had proved difficult to apply in specific cases. We pointed out that in <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), a case dealing with the scope of the search of the arrestee’s person, we had rejected a suggestion that “ ‘there must be litigated in each case the issue of whether or not there was present one of the reasons supporting the authority’ ” to conduct such a search. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S., at 459</a></span> (quoting <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><em>Robinson, supra, </em>at 235</a></span>). Similarly, because “courts ha[d] found no workable definition of ‘the area within the immediate control of the arrestee’ when that area arguably includefd] the interior of an automobile and the arrestee [wa]s its recent occupant,” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>, we sought to set forth a clear rule for police officers and citizens alike. We therefore held that “when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile.” <em>Ibid, </em>(footnote omitted).</p>
<p id="b718-5">In so holding, we placed no reliance on the fact that the officer in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>ordered the occupants out of the vehicle, or initiated contact with them while they remained within it. Nor do we find such a factor persuasive in distinguishing the current situation, as it bears no logical relationship to <em>Bel-toris </em>rationale. There is simply no basis to conclude that the span of the area generally within the arrestee’s immediate control is determined by whether the arrestee exited the <page-number citation-index="1" label="621">*621</page-number>vehicle at the officer’s direction, or whether the officer initiated contact with him while he remained in the car. We recognized as much, albeit in dicta, in <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), where officers observed a speeding car swerve into a ditch. The driver exited and the officers met him at the rear of his car. Although there was no indication that the officers initiated contact with the driver while he was still in the vehicle, we observed that “[i]t is clear . . . that if the officers had arrested [respondent] . . . they could have searched the passenger compartment under <em>New York </em>v. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1035" aria-description="Citation for case: Michigan v. Long"><em>Belton.” Id., </em>at 1035-1036</a></span>, and n. 1.</p>
<p id="b719-5">In all relevant aspects, the arrest of a suspect who is next to a vehicle presents identical concerns regarding officer safety and the destruction of evidence as the arrest of one who is inside the vehicle. An officer may search a suspect’s vehicle under <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>only if the suspect is arrested. See <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa"><em>Knowles, supra, </em>at 117-118</a></span>. A custodial arrest is fluid and “[t]he danger to the police officer flows from <em>the fact of the arrest, </em>and its attendant proximity, stress, and uncertainty,” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson"><em>Robinson, supra, </em>at 234-235</a></span>, and n. 5 (emphasis added). See <em>Washington </em>v. <em>Chrisman, </em><span class="citation" data-id="9428641"><a href="/opinion/110636/washington-v-chrisman/#7" aria-description="Citation for case: Washington v. Chrisman">455 U. S. 1, 7</a></span> (1982) (“Every arrest must be presumed to present a risk of danger to the arresting officer”). The stress is no less merely because the arrestee exited his car before the officer initiated contact, nor is an arrestee less likely to attempt to lunge for a weapon or to destroy evidence if he is outside of, but still in control of, the vehicle. In either case, the officer faces a highly volatile situation. It would make little sense to apply two different rules to what is, at bottom, the same situation.</p>
<p id="b719-6">In some circumstances it may be safer and more effective for officers to conceal their presence from a suspect until he has left his vehicle. Certainly that is a judgment officers should be free to make. But under the strictures of petitioner’s proposed “contact initiation” rule, officers who do so would be unable to search the car’s passenger compartment <page-number citation-index="1" label="622">*622</page-number>in the event of a custodial arrest, potentially compromising their safety and placing incriminating evidence at risk of concealment or destruction. The Fourth Amendment does not require such a gamble.</p>
<p id="b720-5">Petitioner argues, however, that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>will fail to provide a “bright-line” rule if it applies to more than vehicle “occupants.” Brief for Petitioner 29-34. But <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>allows police to search the passenger compartment of a vehicle incident to a lawful custodial arrest of both “occupant[s]” and “recent occupant[s].” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>. Indeed, the respondent in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>was not inside the car at the time of the arrest and search; he was standing on the highway. In any event, while an arrestee’s status as a “recent occupant” may turn on his temporal or spatial relationship to the car at the time of the arrest and search,<footnotemark>2</footnotemark> it certainly does not turn on whether he was inside or outside the car at the moment that the officer first initiated contact with him.</p>
<p id="b720-6">To be sure, not all contraband in the passenger compartment is likely to be readily accessible to a “recent occupant.” It is unlikely in this case that petitioner could have reached under the driver’s seat for his gun once he was outside of his automobile. But the firearm and the passenger compartment in general were no more inaccessible than were the contraband and the passenger compartment in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>. </em>The <page-number citation-index="1" label="623">*623</page-number>need for a clear rule, readily understood by police officers and not depending on differing estimates of what items were or were not within reach of an arrestee at any particular moment, justifies the sort of generalization which <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>enunciated.<footnotemark>3</footnotemark> Once an officer determines that there is probable cause to make an arrest, it is reasonable to allow officers to ensure their safety and to preserve evidence by searching the entire passenger compartment.</p>
<p id="b721-5">Rather than clarifying the constitutional limits of a <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>search, petitioner’s “contact initiation” rule would obfuscate them. Under petitioner’s proposed rule, an officer approaching a suspect who has just alighted from his vehicle would have to determine whether he actually confronted or signaled confrontation with the suspect while he remained in the car, or whether the suspect exited his vehicle unaware of, and for reasons unrelated to, the officer’s presence. This determination would be inherently subjective and highly fact specific, and would require precisely the sort of ad hoc determinations on the part of officers in the field and reviewing courts that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>sought to avoid. <em>Id,., </em>at 459-460. Experience has shown that such a rule is impracticable, and we refuse to adopt it. So long as an arrestee is the sort of “re<page-number citation-index="1" label="624">*624</page-number>cent occupant” of a vehicle such as petitioner was here, officers may search that vehicle incident to the arrest.<footnotemark>4</footnotemark></p>
<p id="AUct">The judgment of the Court of Appeals is affirmed.</p>
<p id="b722-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b717-6"> The Court of Appeals did not reach the District Court’s alternative holding that Nichols could have conducted a lawful inventory search. <span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/#196" aria-description="Citation for case: United States v. Marcus Thornton">325 F. 3d, at 196</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b720-7"> Petitioner argues that if we reject his proposed “contact initiation” rule, we should limit the scope of <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to “recent occupant[s]” who are within “reaching distance” of the car. Brief for Petitioner 35-36. We decline to address petitioner’s argument, however, as it is outside the question on which we granted certiorari, see this Court’s Rule 14.1(a), and was not addressed by the Court of Appeals, see <em>Peralta </em>v. <em>Heights Medical Center, Inc., </em><span class="citation" data-id="112014"><a href="/opinion/112014/peralta-v-heights-medical-center-inc/#86" aria-description="Citation for case: Peralta v. Heights Medical Center, Inc.">485 U. S. 80, 86</a></span> (1988). We note that it is unlikely that petitioner would even meet his own standard as he apparently conceded in the Court of Appeals that he was in “close proximity, both temporally and spatially,” to his vehicle when he was approached by Nichols. <span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/#196" aria-description="Citation for case: United States v. Marcus Thornton">325 F. 3d 189, 196</a></span> (CA4 2003).</p>
</footnote>
<footnote label="3">
<p id="b721-6"> Justice Stevens contends that <em>Belton’s </em>bright-line rule “is not needed for cases in which the arrestee is first accosted when he is a pedestrian, because <em>Chimel </em>[v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969),] itself provides all the guidance that is necessary.” <em>Post, </em>at 636 (dissenting opinion). Under Justice Stevens’ approach, however, even if the car itself was within the arrestee’s reaching distance under <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>police officers and courts would still have to determine whether a particular object within the passenger compartment was also within an arrestee’s reaching distance under <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>. </em>This is exactly the type of unworkable and fact-specific inquiry that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>rejected by holding that the entire passenger compartment may be searched when “ ‘the area within the immediate control of the arrestee’ . . . arguably includes the interior of an automobile and the arrestee is its recent occupant.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b722-8"> Whatever the merits of Justice Scalia's opinion concurring in the judgment, this is the wrong case in which to address them. Petitioner has never argued that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>should be limited “to cases where it is reasonable to believe evidence relevant to the crime of arrest might be found in the vehicle,” <em>post, </em>at 632, nor did any court below consider Justice Scalia’s reasoning. See <em>Pennsylvania Dept. of Corrections </em>v. <em>Yeskey, </em><span class="citation" data-id="118228"><a href="/opinion/118228/pennsylvania-department-of-corrections-v-yeskey/#212" aria-description="Citation for case: Pennsylvania Department of Corrections v. Yeskey">524 U. S. 206, 212-213</a></span> (1998) (“ ‘Where issues are neither raised before nor considered by the Court of Appeals, this Court will not ordinarily consider them’ ” (quoting <em>Adickes </em>v. <em>S. H. Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#147" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 147, n. 2</a></span> (1970))). The question presented — “[w]hether the bright-line rule announced in <em>New York </em>v. <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>is confined to situations in which the police initiate contact with the occupant of a vehicle while that person is in the vehicle,” Pet. for Cert. — does not fairly encompass Justice Scalia’s analysis. See this Court’s Rule 14.1(a) (“Only the questions set out in the petition, or fairly included therein, will be considered by the Court”). And the United States has never had an opportunity to respond to such an approach. See <em>Yee </em>v. <em>Escondido, </em><span class="citation" data-id="9432511"><a href="/opinion/112719/yee-v-city-of-escondido/#536" aria-description="Citation for case: Yee v. City of Escondido">503 U. S. 519, 536</a></span> (1992). Under these circumstances, it would be imprudent to overrule, for all intents and purposes, our established constitutional precedent, which governs police authority in a common occurrence such as automobile searches pursuant to arrest, and we decline to do so at this time.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Agurs.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Agurs"
type: case
citation: "427 U.S. 97 (1976)"
parallel_cite: "96 S. Ct. 2392; 49 L. Ed. 2d 342"
neutral_cite: 1976 U.S. LEXIS 72
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-06-24
docket: 75-491
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1976-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Agurs
  varies_by_point: true
  scope_note: "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework."
  point_overrides:
    - point: legacy-limited-united-states-v-agurs
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: United States v. Bagley
          cluster_id: 111514
          cite: 473 U.S. 667
          field_ii: limited
      scope_note: "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109506/united-states-v-agurs/"
  cluster_id: 109506
  opinion_id: 109506
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[United States v. Bagley]]", "[[Kyles v. Whitley]]", "[[Giglio v. United States]]", "[[Mooney v. Holohan]]"]
aliases: []
tags: ["case", "brady", "giglio", "materiality", "disclosure", "no-request", "due-process"]
holding: "The prosecution's duty to disclose exculpatory evidence exists even when the defense makes no request, but a nondisclosure is a constitutional violation only when the omission is material — defined (in the no-request situation) as evidence that creates a reasonable doubt that did not otherwise exist. (Materiality standard later unified under Bagley's 'reasonable probability' test.)"
lake:
  record_id: United States v. Agurs
  status: verified
  projected_at: 2026-07-09
---

# United States v. Agurs

*427 U.S. 97 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Linda Agurs was convicted of second-degree murder for stabbing James Sewell during an altercation in a hotel room; her defense was self-defense. After trial, defense counsel learned that Sewell had a prior criminal record — including convictions for assault and carrying a deadly weapon — which the prosecutor had not disclosed and which counsel argued would have supported the self-defense theory. The defense had made no specific pretrial request for the victim's record. The Court of Appeals ordered a new trial; the Government sought review.

## Issue
Whether, and under what standard of materiality, the prosecution's failure to disclose [[Brady and Giglio|exculpatory]] evidence violates due process when the defense made no request (or only a general request) for it.

## Rule
The duty to disclose can arise without a request, but only material omissions are constitutional error — **a standard later limited by** [[United States v. Bagley]]. The Court rejected any rule that the prosecutor must disclose anything that "might" affect the verdict: "the prosecutor will not have violated his constitutional duty of disclosure unless his omission is of sufficient significance to result in the denial of the defendant's right to a fair trial." — 427 U.S. at 108. ^pin-108

For the no-request situation, the Court fixed materiality to the justice of the verdict: "if the omitted evidence creates a reasonable doubt that did not otherwise exist, constitutional error has been committed. This means that the omission must be evaluated in the context of the entire record." — [427 U.S. at 112](https://www.courtlistener.com/opinion/109506/united-states-v-agurs/#:~:text=if%20the%20omitted%20evidence%20creates%20a%20reasonable%20doubt%20that%20did%20not%20otherwise%20exist%2C). ^pin-112

## Application
Measured against that standard, the prosecutor's failure to disclose Sewell's prior assault-and-weapons record was not a constitutional violation. The record of the victim's violent character, viewed against the entire trial record — Agurs had inflicted multiple stab wounds while suffering none herself, undercutting self-defense — did not create a reasonable doubt about guilt that did not otherwise exist. Because the undisclosed evidence was not material in that sense, the prosecutor's nondisclosure (absent any request) did not deny Agurs a fair trial, and a new trial was not warranted.

## Conclusion
Reversed. The undisclosed evidence did not create a reasonable doubt that did not otherwise exist, so the nondisclosure was not a due-process violation; the prosecutor's duty to volunteer obviously [[Brady and Giglio|exculpatory]] evidence is bounded by materiality.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS** (Stevens, J.; Marshall, J., joined by Brennan, J., dissenting).
- **Materiality standard superseded by** [[United States v. Bagley]] (1985): Agurs had set different materiality tests for its three situations (knowing use of perjury; specific request; no/general request); *[[United States v. Bagley|Bagley]]* adopted a single "reasonable probability" standard for all undisclosed *[[Brady v. Maryland|Brady]]*/*[[Giglio v. United States|Giglio]]* evidence, absorbing Agurs's no-request "reasonable doubt that did not otherwise exist" formula. The **surviving** holding — that the disclosure duty attaches to obviously [[Brady and Giglio|exculpatory]] evidence even without a request — remains good law and is built into [[Brady v. Maryland]]/[[Kyles v. Whitley]] doctrine. Agurs's situation 1 traces to the knowing-perjury line of [[Mooney v. Holohan]] and [[Giglio v. United States]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Agurs*, 427 U.S. 97 (1976) — https://www.courtlistener.com/opinion/109506/united-states-v-agurs/ — pinpoints: 108, 112.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "85d66479affd8bd5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "427 U.S. 97 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 72", "official_citation_present": true, "parallel_cite": "96 S. Ct. 2392; 49 L. Ed. 2d 342", "title": "United States v. Agurs", "year": "1976"}}
{"assertion_id": "3898a7fe6d32e2eb", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "United States v. Agurs"}}
{"assertion_id": "ffa495623e7130d4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The prosecution's duty to disclose exculpatory evidence exists even when the defense makes no request, but a nondisclosure is a constitutional violation only when the omission is material — defined (in the no-request situation) as evidence that creates a reasonable doubt that did not otherwise exist. (Materiality standard later unified under Bagley's 'reasonable probability' test.)", "title": "United States v. Agurs"}}
{"assertion_id": "1b517d0683f7a870", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-united-states-v-agurs"}, "payload": {"by": [{"cite": "473 U.S. 667", "cluster_id": "111514", "field_ii": "limited", "name": "United States v. Bagley"}], "field_i_validity": "caution", "point": "legacy-limited-united-states-v-agurs", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "United States v. Agurs"}}
{"assertion_id": "a3f8efaa846775ef", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-06-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Agurs", "field_i_validity": "caution", "scope_note": "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework.", "title": "United States v. Agurs", "varies_by_point": "true"}}
{"assertion_id": "e8ce4b11bdfb5059", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Agurs"}}
```

### lake record — United States v. Agurs

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Agurs",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Agurs",
    "case_name_short": "Agurs",
    "case_name_full": "United States v. Agurs",
    "input_case_name": "United States v. Agurs",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-06-24",
    "year": 1976,
    "docket": "75-491",
    "cluster_id": 109506,
    "lead_opinion_id": 109506,
    "sibling_ids": [
      109506,
      9426498,
      9426499
    ],
    "absolute_url": "/opinion/109506/united-states-v-agurs/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "427 U.S. 97",
      "volume": "427",
      "reporter": "U.S.",
      "page": "97",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 2392",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2392",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 342",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "342",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 72",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "72",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "427 U.S. 97",
        "volume": "427",
        "reporter": "U.S.",
        "page": "97",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 2392",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2392",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 342",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "342",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 72",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "72",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "427 U.S. 97",
    "official_selection": {
      "court_class": "scotus",
      "selected": "427 U.S. 97",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-108",
      "page": null,
      "quote": "--- # United States v. Agurs *427 U.S. 97 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **limited** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Linda Agurs was convicted of second-degree murder for stabbing James Sewell during an altercation in a hotel room; her defense was self-defense. After trial, defense counsel learned that Sewell had a prior criminal record \u2014 including convictions for assault and carrying a deadly weapon \u2014 which the prosecutor had not disclosed and which counsel argued would have supported the self-defense theory. The defense had made no specific pretrial request for the victim's record. The Court of Appeals ordered a new trial; the Government sought review. ## Issue Whether, and under what standard of materiality, the prosecution's failure to disclose exculpatory evidence violates due process when the defense made no request (or only a general request) for it. ## Rule The duty to disclose can arise without a request, but only material omissions are constitutional error \u2014 **a standard later limited by** [[United States v. Bagley]]. The Court rejected any rule that the prosecutor must disclose anything that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-112",
      "page": null,
      "quote": "if the omitted evidence creates a reasonable doubt that did not otherwise exist, constitutional error has been committed. This means that the omission must be evaluated in the context of the entire record.",
      "star_marker": "112",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23248,
      "fragment": "#:~:text=if%20the%20omitted%20evidence%20creates%20a%20reasonable%20doubt%20that%20did%20not%20otherwise%20exist%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1976-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Agurs",
    "varies_by_point": true,
    "scope_note": "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework.",
    "point_overrides": [
      {
        "point": "legacy-limited-united-states-v-agurs",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "United States v. Bagley",
            "cluster_id": 111514,
            "cite": "473 U.S. 667",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": "473 U.S. 667",
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
          "name": "State of Louisiana v. Brhian Thomas",
          "cluster_id": 10618702,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bateman",
          "cluster_id": 9413757,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Caldwell",
          "cluster_id": 4881045,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Strickland v. Washington",
          "cluster_id": 111170,
          "cite": [
            "80 L. Ed. 2d 674",
            "104 S. Ct. 2052",
            "466 U.S. 668",
            "1984 U.S. LEXIS 79"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": [
            "87 L. Ed. 2d 481",
            "105 S. Ct. 3375",
            "473 U.S. 667",
            "1985 U.S. LEXIS 130",
            "53 U.S.L.W. 5084"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cronic",
          "cluster_id": 111169,
          "cite": [
            "80 L. Ed. 2d 657",
            "104 S. Ct. 2039",
            "466 U.S. 648",
            "1984 U.S. LEXIS 78",
            "52 U.S.L.W. 4560"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Phillips",
          "cluster_id": 110645,
          "cite": [
            "71 L. Ed. 2d 78",
            "102 S. Ct. 940",
            "455 U.S. 209",
            "1982 U.S. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Trombetta",
          "cluster_id": 111206,
          "cite": [
            "81 L. Ed. 2d 413",
            "104 S. Ct. 2528",
            "467 U.S. 479",
            "1984 U.S. LEXIS 103",
            "52 U.S.L.W. 4744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Youngblood",
          "cluster_id": 112156,
          "cite": [
            "102 L. Ed. 2d 281",
            "109 S. Ct. 333",
            "488 U.S. 51",
            "1988 U.S. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Ritchie",
          "cluster_id": 111822,
          "cite": [
            "94 L. Ed. 2d 40",
            "107 S. Ct. 989",
            "480 U.S. 39",
            "1987 U.S. LEXIS 558",
            "55 U.S.L.W. 4180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dominguez Benitez",
          "cluster_id": 136986,
          "cite": [
            "159 L. Ed. 2d 157",
            "124 S. Ct. 2333",
            "542 U.S. 74",
            "2004 U.S. LEXIS 4177",
            "17 Fla. L. Weekly Fed. S 379",
            "72 U.S.L.W. 4478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Briscoe v. LaHue",
          "cluster_id": 110885,
          "cite": [
            "75 L. Ed. 2d 96",
            "103 S. Ct. 1108",
            "460 U.S. 325",
            "1983 U.S. LEXIS 146",
            "51 U.S.L.W. 4247"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coleman",
          "cluster_id": 2115945,
          "cite": [
            "701 N.E.2d 1063",
            "183 Ill. 2d 366",
            "233 Ill. Dec. 789",
            "1998 Ill. LEXIS 938"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Valenzuela-Bernal",
          "cluster_id": 110797,
          "cite": [
            "73 L. Ed. 2d 1193",
            "102 S. Ct. 3440",
            "458 U.S. 858",
            "1982 U.S. LEXIS 159",
            "50 U.S.L.W. 5108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ruiz",
          "cluster_id": 121166,
          "cite": [
            "153 L. Ed. 2d 586",
            "122 S. Ct. 2450",
            "536 U.S. 622",
            "2002 U.S. LEXIS 4650"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cole",
          "cluster_id": 2590164,
          "cite": [
            "95 P.3d 811",
            "17 Cal. Rptr. 3d 532",
            "33 Cal. 4th 1158",
            "2004 Cal. Daily Op. Serv. 7469",
            "2004 Daily Journal DAR 10101",
            "2004 Cal. LEXIS 7573"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mabry v. Johnson",
          "cluster_id": 111208,
          "cite": [
            "81 L. Ed. 2d 437",
            "104 S. Ct. 2543",
            "467 U.S. 504",
            "1984 U.S. LEXIS 105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Whiteside",
          "cluster_id": 111603,
          "cite": [
            "89 L. Ed. 2d 123",
            "106 S. Ct. 988",
            "475 U.S. 157",
            "1986 U.S. LEXIS 8",
            "54 U.S.L.W. 4194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109506 OR 9426498 OR 9426499) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjEwMDY0MDAwMDAwJnM9NDg0NjM4MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109506+OR+9426498+OR+9426499%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109506 OR 9426498 OR 9426499)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NDQmcz0xNjk5OTE2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109506+OR+9426498+OR+9426499%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109506 OR 9426498 OR 9426499)",
        "reviewed": 119,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 119,
        "triage_read": 2,
        "triage_snippet_classified": 117
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109506 OR 9426498 OR 9426499)",
    "indexed_citing_opinions": 4292,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109506,
        "count": 3847,
        "count_source": "search"
      },
      {
        "opinion_id": 9426498,
        "count": 518,
        "count_source": "search"
      },
      {
        "opinion_id": 9426499,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6542,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-agurs.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MTA5NDUmcz0xMDYxNTM4MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109506+OR+9426498+OR+9426499%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109506,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 104321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 104681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 105566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 107354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 107361,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 108613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 109024,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 253599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 276039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 277986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 279213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 279966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 285114,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 285177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 290286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 295841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 305106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 307051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 307845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 313335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 316285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 316953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 317641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 320391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 325310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 325594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 330049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 330694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 1361490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 1474384,
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
    "date_created": "2026-07-05T22:00:04Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:00:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:00:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:00:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Agurs

```
<div>
<center><b><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U.S. 97</a></span> (1976)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
AGURS.</h1></center>
<center>No. 75-491.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 28, 1976.</center>
<center>Decided June 24, 1976.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><span class="star-pagination">*98</span> <i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Bork, Assistant Attorney General Thornburgh, John F. Cooney, Jerome M. Feit,</i> and <i>Robert H. Plaxico.</i></p>
<p><i>Edwin J. Bradley</i> argued the cause for respondent. With him on the brief were <i>Michael E. Geltner, William Greenhalgh,</i> and <i>Sherman L. Cohn.</i></p>
<p>MR. JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>After a brief interlude in an inexpensive motel room, respondent repeatedly stabbed James Sewell, causing his death. She was convicted of second-degree murder. The question before us is whether the prosecutor's failure <span class="star-pagination">*99</span> to provide defense counsel with certain background information about Sewell, which would have tended to support the argument that respondent acted in self-defense, deprived her of a fair trial under the rule of <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span>.</p>
<p>The answer to the question depends on (1) a review of the facts, (2) the significance of the failure of defense counsel to request the material, and (3) the standard by which the prosecution's failure to volunteer exculpatory material should be judged.</p>
<p></p>
<h2>I</h2>
<p>At about 4:30 p. m. on September 24, 1971, respondent, who had been there before, and Sewell, registered in a motel as man and wife. They were assigned a room without a bath. Sewell was wearing a bowie knife in a sheath, and carried another knife in his pocket. Less than two hours earlier, according to the testimony of his estranged wife, he had had $360 in cash on his person.</p>
<p>About 15 minutes later three motel employees heard respondent screaming for help. A forced entry into their room disclosed Sewell on top of respondent struggling for possession of the bowie knife. She was holding the knife; his bleeding hand grasped the blade; according to one witness he was trying to jam the blade into her chest. The employees separated the two and summoned the authorities. Respondent departed without comment before they arrived. Sewell was dead on arrival at the hospital.</p>
<p>Circumstantial evidence indicated that the parties had completed an act of intercourse, that Sewell had then gone to the bathroom down the hall, and that the struggle occurred upon his return. The contents of his pockets were in disarray on the dresser and no money was found; the jury may have inferred that respondent took Sewell's money and that the fight started when Sewell re-entered the room and saw what she was doing.</p>
<p><span class="star-pagination">*100</span> On the following morning respondent surrendered to the police. She was given a physical examination which revealed no cuts or bruises of any kind, except needle marks on her upper arm. An autopsy of Sewell disclosed that he had several deep stab wounds in his chest and abdomen, and a number of slashes on his arms and hands, characterized by the pathologist as "defensive wounds."<sup>[1]</sup></p>
<p>Respondent offered no evidence. Her sole defense was the argument made by her attorney that Sewell had initially attacked her with the knife, and that her actions had all been directed toward saving her own life. The support for this self-defense theory was based on the fact that she had screamed for help. Sewell was on top of her when help arrived, and his possession of two knives indicated that he was a violence-prone person.<sup>[2]</sup> It took the jury about 25 minutes to elect a foreman and return a verdict.</p>
<p>Three months later defense counsel filed a motion for a new trial asserting that he had discovered (1) that Sewell had a prior criminal record that would have further evidenced his violent character; (2) that the prosecutor had failed to disclose this information to the defense; and (3) that a recent opinion of the United States Court of Appeals for the District of Columbia Circuit made it clear that such evidence was admissible even if not known to the defendant.<sup>[3]</sup> Sewell's prior record included a plea of guilty to a charge of assault and carrying <span class="star-pagination">*101</span> a deadly weapon in 1963, and another guilty plea to a charge of carrying a deadly weapon in 1971. Apparently both weapons were knives.</p>
<p>The Government opposed the motion, arguing that there was no duty to tender Sewell's prior record to the defense in the absence of an appropriate request; that the evidence was readily discoverable in advance of trial and hence was not the kind of "newly discovered" evidence justifying a new trial; and that, in all events, it was not material.</p>
<p>The District Court denied the motion. It rejected the Government's argument that there was no duty to disclose material evidence unless requested to do so,<sup>[4]</sup><span class="star-pagination">*102</span> assumed that the evidence was admissible, but held that it was not sufficiently material. The District Court expressed the opinion that the prior conviction shed no light on Sewell's character that was not already apparent from the uncontradicted evidence, particularly the fact that he carried two knives; the court stressed the inconsistency between the claim of self-defense and the fact that Sewell had been stabbed repeatedly while respondent was unscathed.</p>
<p>The Court of Appeals reversed.<sup>[5]</sup> The court found no lack of diligence on the part of the defense and no misconduct by the prosecutor in this case. It held, however, that the evidence was material, and that its nondisclosure required a new trial because the jury might have returned a different verdict if the evidence had been received.<sup>[6]</sup></p>
<p>The decision of the Court of Appeals represents a significant departure from this Court's prior holding; because we believe that that court has incorrectly interpreted the constitutional requirement of due process, we reverse.</p>
<p></p>
<h2>
<span class="star-pagination">*103</span> II</h2>
<p>The rule of <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span>, arguably applies in three quite different situations. Each involves the discovery, after trial, of information which had been known to the prosecution but unknown to the defense.</p>
<p>In the first situation, typified by <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span>, the undisclosed evidence demonstrates that the prosecution's case includes perjured testimony and that the prosecution knew, or should have known, of the perjury.<sup>[7]</sup> In a series of subsequent cases, the Court has consistently held that a conviction obtained by the knowing use of perjured testimony is fundamentally unfair,<sup>[8]</sup> and must be set aside if there is any reasonable likelihood that the false testimony could have affected the judgment of the jury.<sup>[9]</sup> It is this line of cases on which the <span class="star-pagination">*104</span> Court of Appeals placed primary reliance. In those cases the Court has applied a strict standard of materiality, not just because they involve prosecutorial misconduct, but more importantly because they involve a corruption of the truth-seeking function of the trial process. Since this case involves no misconduct, and since there is no reason to question the veracity of any of the prosecution witnesses, the test of materiality followed in the <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Mooney</a></span></i> line of cases is not necessarily applicable to this case.</p>
<p>The second situation, illustrated by the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> case itself, is characterized by a pretrial request for specific evidence. In that case defense counsel had requested the extrajudicial statements made by Brady's accomplice, one Boblit. This Court held that the suppression of one of Boblit's statements deprived Brady of due process, noting specifically that the statement had been requested and that it was "material."<sup>[10]</sup> A fair analysis of the holding in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> indicates that implicit in the requirement of materiality is a concern that the suppressed evidence might have affected the outcome of the trial.</p>
<p>Brady was found guilty of murder in the first degree. Since the jury did not add the words "without capital punishment" to the verdict, he was sentenced to death. At his trial Brady did not deny his involvement in the deliberate killing, but testified that it was his accomplice, <span class="star-pagination">*105</span> Boblit, rather than he, who had actually strangled the decedent. This version of the event was corroborated by one of several confessions made by Boblit but not given to Brady's counsel despite an admittedly adequate request.</p>
<p>After his conviction and sentence had been affirmed on appeal,<sup>[11]</sup> Brady filed a motion to set aside the judgment, and later a post-conviction proceeding, in which he alleged that the State had violated his constitutional rights by suppressing the Boblit confession. The trial judge denied relief largely because he felt that Boblit's confession would have been inadmissible at Brady's trial. The Maryland Court of Appeals disagreed;<sup>[12]</sup> it ordered a new trial on the issue of punishment. It held that the withholding of material evidence, even "without guile," was a denial of due process and that there were valid theories on which the confession might have been admissible in Brady's defense.</p>
<p>This Court granted certiorari to consider Brady's contention that the violation of his constitutional right to a fair trial vitiated the entire proceeding.<sup>[13]</sup> The holding that the suppression of exculpatory evidence violated Brady's right to due process was affirmed, as was the separate holding that he should receive a new trial on the issue of punishment but not on the issue of guilt or innocence. The Court interpreted the Maryland Court <span class="star-pagination">*106</span> of Appeals opinion as ruling that the confession was inadmissible on that issue. For that reason, the confession could not have affected the outcome on the issue of guilt but could have affected Brady's punishment. It was material on the latter issue but not the former. And since it was not material on the issue of guilt, the entire trial was not lacking in due process.</p>
<p>The test of materiality in a case like <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> in which specific information has been requested by the defense is not necessarily the same as in a case in which no such request has been made.<sup>[14]</sup> Indeed, this Court has not yet decided whether the prosecutor has any obligation to provide defense counsel with exculpatory information when no request has been made. Before addressing that question, a brief comment on the function of the request is appropriate.</p>
<p>In <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> the request was specific. It gave the prosecutor notice of exactly what the defense desired. Although there is, of course, no duty to provide defense counsel with unlimited discovery of everything known by the prosecutor, if the subject matter of such a request is material, or indeed if a substantial basis for claiming materiality exists, it is reasonable to require the prosecutor to respond either by furnishing the information or by submitting the problem to the trial judge. When the prosecutor receives a specific and relevant request, the failure to make any response is seldom, if ever, excusable.</p>
<p>In many cases, however, exculpatory information in the possession of the prosecutor may be unknown to defense counsel. In such a situation he may make no request at all, or possibly ask for "all <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material" or for "anything exculpatory." Such a request really gives the prosecutor no better notice than if no request is <span class="star-pagination">*107</span> made. If there is a duty to respond to a general request of that kind, it must derive from the obviously exculpatory character of certain evidence in the hands of the prosecutor. But if the evidence is so clearly supportive of a claim of innocence that it gives the prosecution notice of a duty to produce, that duty should equally arise even if no request is made. Whether we focus on the desirability of a precise definition of the prosecutor's duty or on the potential harm to the defendant, we conclude that there is no significant difference between cases in which there has been merely a general request for exculpatory matter and cases, like the one we must now decide, in which there has been no request at all. The third situation in which the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> rule arguably applies, typified by this case, therefore embraces the case in which only a general request for "<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> material" has been made.</p>
<p>We now consider whether the prosecutor has any constitutional duty to volunteer exculpatory matter to the defense, and if so, what standard of materiality gives rise to that duty.</p>
<p></p>
<h2>III</h2>
<p>We are not considering the scope of discovery authorized by the Federal Rules of Criminal Procedure, or the wisdom of amending those Rules to enlarge the defendant's discovery rights. We are dealing with the defendant's right to a fair trial mandated by the Due Process Clause of the Fifth Amendment to the Constitution. Our construction of that Clause will apply equally to the comparable clause in the Fourteenth Amendment applicable to trials in state courts.</p>
<p>The problem arises in two principal contexts. First, in advance of trial, and perhaps during the course of a trial as well, the prosecutor must decide what, if anything, he should voluntarily submit to defense counsel. <span class="star-pagination">*108</span> Second, after trial a judge may be required to decide whether a nondisclosure deprived the defendant of his right to due process. Logically the same standard must apply at both times. For unless the omission deprived the defendant of a fair trial, there was no constitutional violation requiring that the verdict be set aside; and absent a constitutional violation, there was no breach of the prosecutor's constitutional duty to disclose.</p>
<p>Nevertheless, there is a significant practical difference between the pretrial decision of the prosecutor and the post-trial decision of the judge. Because we are dealing with an inevitably imprecise standard, and because the significance of an item of evidence can seldom be predicted accurately until the entire record is complete, the prudent prosecutor will resolve doubtful questions in favor of disclosure. But to reiterate a critical point, the prosecutor will not have violated his constitutional duty of disclosure unless his omission is of sufficient significance to result in the denial of the defendant's right to a fair trial.</p>
<p>The Court of Appeals appears to have assumed that the prosecutor has a constitutional obligation to disclose any information that might affect the jury's verdict. That statement of a constitutional standard of materiality approaches the "sporting theory of justice" which the Court expressly rejected in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i><sup>[15]</sup> For a jury's <span class="star-pagination">*109</span> appraisal of a case "might" be affected by an improper or trivial consideration as well as by evidence giving rise to a legitimate doubt on the issue of guilt. If everything that might influence a jury must be disclosed, the only way a prosecutor could discharge his constitutional duty would be to allow complete discovery of his files as a matter of routine practice.</p>
<p>Whether or not procedural rules authorizing such broad discovery might be desirable, the Constitution surely does not demand that much. While expressing the opinion that representatives of the State may not "suppress substantial material evidence," former Chief Justice Traynor of the California Supreme Court has pointed out that "they are under no duty to report sua sponte to the defendant all that they learn about the case and about their witnesses." <i>In re Imbler,</i> <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#569" aria-description="Citation for case: In Re Imbler">60 Cal. 2d 554, 569</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#14" aria-description="Citation for case: In Re Imbler">387 P. 2d 6, 14</a></span> (1963). And this Court recently noted that there is "no constitutional requirement that the prosecution make a complete and detailed accounting to the defense of all police investigatory work on a case." <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span>.<sup>[16]</sup> The mere possibility that an item of undisclosed information <span class="star-pagination">*110</span> might have helped the defense, or might have affected the outcome of the trial, does not establish "materiality" in the constitutional sense.</p>
<p>Nor do we believe the constitutional obligation is measured by the moral culpability, or the willfulness, of the prosecutor.<sup>[17]</sup> If evidence highly probative of innocence is in his file, he should be presumed to recognize its significance even if he has actually overlooked it. Cf. <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span>. Conversely, if evidence actually has no probative significance at all, no purpose would be served by requiring a new trial simply because an inept prosecutor incorrectly believed he was suppressing a fact that would be vital to the defense. If the suppression of evidence results in constitutional error, it is because of the character of the evidence, not the character of the prosecutor.</p>
<p>As the District Court recognized in this case, there are situations in which evidence is obviously of such substantial value to the defense that elementary fairness requires it to be disclosed even without a specific request.<sup>[18]</sup> For though the attorney for the sovereign must prosecute the accused with earnestness and vigor, he <span class="star-pagination">*111</span> must always be faithful to his client's overriding interest that "justice shall be done." He is the "servant of the law, the twofold aim of which is that guilt shall not escape or innocence suffer." <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span>. This description of the prosecutor's duty illuminates the standard of materiality that governs his obligation to disclose exculpatory evidence.</p>
<p>On the one hand, the fact that such evidence was available to the prosecutor and not submitted to the defense places it in a different category than if it had simply been discovered from a neutral source after trial. For that reason the defendant should not have to satisfy the severe burden of demonstrating that newly discovered evidence probably would have resulted in acquittal.<sup>[19]</sup> If the standard applied to the usual motion for a new trial based on newly discovered evidence were the same when the evidence was in the State's possession as when it was found in a neutral source, there would be no special significance to the prosecutor's obligation to serve the cause of justice.</p>
<p>On the other hand, since we have rejected the suggestion that the prosecutor has a constitutional duty routinely to deliver his entire file to defense counsel, we cannot consistently treat every nondisclosure as though it were error. It necessarily follows that the judge should not order a new trial every time he is unable to <span class="star-pagination">*112</span> characterize a nondisclosure as harmless under the customary harmless-error standard. Under that standard when error is present in the record, the reviewing judge must set aside the verdict and judgment unless his "conviction is sure that the error did not influence the jury, or had but very slight effect." <i>Kotteakos</i> v. <i>United States,</i> <span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/#764" aria-description="Citation for case: Kotteakos v. United States">328 U. S. 750, 764</a></span>. Unless every nondisclosure is regarded as automatic error, the constitutional standard of materiality must impose a higher burden on the defendant.</p>
<p>The proper standard of materiality must reflect our overriding concern with the justice of the finding of guilt.<sup>[20]</sup> Such a finding is permissible only if supported by evidence establishing guilt beyond a reasonable doubt. It necessarily follows that if the omitted evidence creates a reasonable doubt that did not otherwise exist, constitutional error has been committed. This means that the omission must be evaluated in the context of the entire record.<sup>[21]</sup> If there is no reasonable doubt about <span class="star-pagination">*113</span> guilt whether or not the additional evidence is considered, there is no justification for a new trial. On the other hand, if the verdict is already of questionable validity, additional evidence of relatively minor importance might be sufficient to create a reasonable doubt.</p>
<p>This statement of the standard of materiality describes the test which courts appear to have applied in actual cases although the standard has been phrased in different language.<sup>[22]</sup> It is also the standard which the trial judge applied in this case. He evaluated the significance of Sewell's prior criminal record in the context of the full trial which he recalled in detail. Stressing in particular the incongruity of a claim that Sewell was the aggressor with the evidence of his multiple wounds and respondent's unscathed condition, the trial judge indicated his unqualified opinion that respondent was guilty. He <span class="star-pagination">*114</span> noted that Sewell's prior record did not contradict any evidence offered by the prosecutor, and was largely cumulative of the evidence that Sewell was wearing a bowie knife in a sheath and carrying a second knife in his pocket when he registered at the motel.</p>
<p>Since the arrest record was not requested and did not even arguably give rise to any inference of perjury, since after considering it in the context of the entire record the trial judge remained convinced of respondent's guilt beyond a reasonable doubt, and since we are satisfied that his firsthand appraisal of the record was thorough and entirely reasonable, we hold that the prosecutor's failure to tender Sewell's record to the defense did not deprive respondent of a fair trial as guaranteed by the Due Process Clause of the Fifth Amendment. Accordingly, the judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>The Court today holds that the prosecutor's constitutional duty to provide exculpatory evidence to the defense is not limited to cases in which the defense makes a request for such evidence. But once having recognized the existence of a duty to volunteer exculpatory evidence, the Court so narrowly defines the category of "material" evidence embraced by the duty as to deprive it of all meaningful content.</p>
<p>In considering the appropriate standard of materiality governing the prosecutor's obligation to volunteer exculpatory evidence, the Court observes:</p>
<blockquote>"[T]he fact that such evidence was available to the prosecutor and not submitted to the defense places it in a different category than if it had simply been <span class="star-pagination">*115</span> discovered from a neutral source after trial. For that reason the defendant should not have to satisfy the severe burden of demonstrating that newly discovered evidence probably would have resulted in acquittal [the standard generally applied to a motion under Fed. Rule Crim. Proc. 33 based on newly discovered evidence.<sup>[1]</sup>]. If the standard applied to the usual motion for a new trial based on newly discovered evidence were the same when the evidence was in the State's possession as when it was found in a neutral source, there would be no special significance to the prosecutor's obligation to serve the cause of justice." <i>Ante,</i> at 111 (footnote omitted).</blockquote>
<p>I agree completely.</p>
<p>The Court, however, seemingly forgets these precautionary words when it comes time to state the proper standard of materiality to be applied in cases involving neither the knowing use of perjury nor a specific defense request for an item of information. In such cases, the prosecutor commits constitutional error, the Court holds, "if the omitted evidence creates a reasonable doubt that did not otherwise exist." <i>Ante,</i> at 112. As the Court's subsequent discussion makes clear, the defendant challenging the prosecutor's failure to disclose evidence is entitled to relief, in the Court's view, only if the withheld evidence actually creates a reasonable doubt as to guilt in the judge's mind. The burden thus imposed on the defendant is at least as "severe" as, if not more <span class="star-pagination">*116</span> "severe" than,<sup>[2]</sup> the burden he generally faces on a Rule 33 motion. Surely if a judge is able to say that evidence actually creates a reasonable doubt as to guilt in his mind (the Court's standard), he would also conclude that the evidence "probably would have resulted in acquittal" (the general Rule 33 standard). In short, in spite of its own salutary precaution, the Court treats the case in which the prosecutor withholds evidence no differently from the case in which evidence is newly discovered from a neutral source. The "prosecutor's obligation to serve the cause of justice" is reduced to a status, to borrow the Court's words, of "no special significance." <i>Ante,</i> at 111.</p>
<p>Our overriding concern in cases such as the one before us is the defendant's right to a fair trial. One of the most basic elements of fairness in a criminal trial is that available evidence tending to show innocence, as well as that tending to show guilt, be fully aired before the jury; more particularly, it is that the State in its zeal to convict a defendant not suppress evidence that might exonerate him. See <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#810" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 810</a></span> (1972) (opinion of MARSHALL, J.). This fundamental notion of fairness does not pose any irreconcilable conflict for the prosecutor, for as the Court reminds us, the prosecutor "must always be faithful to his client's overriding interest that `justice shall be done.' " <i>Ante,</i> at 111. No interest of the State is served, and no duty of the prosecutor advanced, by the suppression of evidence favorable to the defendant. On the contrary, the prosecutor fulfills his most basic responsibility when he fully airs all the relevant evidence at his command.</p>
<p>I recognize, of course, that the exculpatory value to the defense of an item of information will often not be apparent to the prosecutor in advance of trial. And <span class="star-pagination">*117</span> while the general obligation to disclose exculpatory information no doubt continues during the trial, giving rise to a duty to disclose information whose significance becomes apparent as the case progresses, even a conscientious prosecutor will fail to appreciate the significance of some items of information. See <i>United States</i> v. <i>Keogh,</i> <span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/#147" aria-description="Citation for case: United States v. James Vincent Keogh">391 F. 2d 138, 147</a></span> (CA2 1968). I agree with the Court that these consideration, as well as the general interest in finality of judgments, preclude the granting of a new trial in every case in which the prosecutor has failed to disclose evidence of some value to the defense. But surely these considerations do not require the rigid rule the Court intends to be applied to all but a relatively small number of such cases.</p>
<p>Under today's ruling, if the prosecution has not made knowing use of perjury, and if the defense has not made a specific request for an item of information, the defendant is entitled to a new trial only if the withheld evidence actually creates a reasonable doubt as to guilt in the judge's mind. With all respect, this rule is completely at odds with the overriding interest in assuring that evidence tending to show innocence is brought to the jury's attention. The rule creates little, if any, incentive for the prosecutor conscientiously to determine whether his files contain evidence helpful to the defense. Indeed, the rule reinforces the natural tendency of the prosecutor to overlook evidence favorable to the defense, and creates an incentive for the prosecutor to resolve close questions of disclosure in favor of concealment.</p>
<p>More fundamentally, the Court's rule usurps the function of the jury as the trier of fact in a criminal case. The Court's rule explicitly establishes the judge as the trier of fact with respect to evidence withheld by the prosecution. The defendant's fate is sealed so long as the evidence does not create a reasonable doubt as to guilt in the judge's mind, regardless of whether the <span class="star-pagination">*118</span> evidence is such that reasonable men could disagree as to its importregardless, in other words, of how "close" the case may be.<sup>[3]</sup></p>
<p>The Court asserts that this harsh standard of materiality is the standard that "courts appear to have applied in actual cases although the standard has been phrased in different language." <i>Ante,</i> at 113 (footnote omitted). There is no basis for this assertion. None of the cases cited by the Court in support of its statement suggests that a judgment of conviction should be sustained so long as the judge remains convinced beyond a reasonable doubt of the defendant's guilt.<sup>[4]</sup> The prevailing <span class="star-pagination">*119</span> view in the federal courts of the standard of materiality for cases involving neither a specific request for information nor other indications of deliberate misconducta standard with which the cases cited by the Court are fully consistentis quite different. It is essentially the following: If there is a significant chance that the withheld evidence, developed by skilled counsel, would have induced a reasonable doubt in the minds of enough jurors to avoid a conviction, then the judgment of conviction must be set aside.<sup>[5]</sup> This standard, unlike the Court's reflects a recognition that the determination must be in terms of the impact of an item of evidence on the jury, and that this determination cannot always be made with certainty.<sup>[6]</sup></p>
<p><span class="star-pagination">*120</span> The Court approvesbut only for a limited category of casesa standard virtually identical to the one I have described as reflecting the prevailing view. In cases in which "the undisclosed evidence demonstrates that the prosecution's case includes perjured testimony and that the prosecution knew, or should have known, of the perjury," <i>ante,</i> at 103, the judgment of conviction must be set aside "if there is any reasonable likelihood that the false testimony could have affected the judgment of the jury." <i><span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/" aria-description="Citation for case: United States v. James Vincent Keogh">Ibid.</a></span></i> This lesser burden on the defendant is appropriate, the Court states, primarily because the withholding of evidence contradicting testimony offered by witnesses called by the prosecution "involve[s] a corruption of the truth-seeking function of the trial process." <i>Ante,</i> at 104. But surely the truth-seeking process is corrupted by the withholding of evidence favorable to the defense, regardless of whether the evidence is directly contradictory to evidence offered by the prosecution. An example offered by Mr. Justice Fortas serves to illustrate the point. "[L]et us assume that the State possesses information that blood was found on the victim, and that this blood is of a type which does not match that of the accused or of the victim. Let us assume that no related testimony was offered by the State." <i>Giles</i> v. <i>Maryland,</i> <span class="citation" data-id="9423353"><a href="/opinion/107361/giles-v-maryland/#100" aria-description="Citation for case: Giles v. Maryland">386 U. S. 66, 100</a></span> (1967) (concurring in judgment). The suppression of the information unquestionably corrupts the truth-seeking process, and the burden on the defendant in establishing his entitlement to a new trial ought be no different from the burden he would face if related testimony had been elicited by the prosecution. See <span class="citation" data-id="9423353"><a href="/opinion/107361/giles-v-maryland/#99" aria-description="Citation for case: Giles v. Maryland"><i>id.,</i> at 99-101</a></span>.</p>
<p>The Court derives its "reasonable likelihood" standard for cases involving perjury from cases such as <i>Napue</i> v. <span class="star-pagination">*121</span> <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), and <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972). But surely the results in those cases, and the standards applied, would have been no different if perjury had not been involved. In <i><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span></i> and <i><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">Giglio</a></span>,</i> co-conspirators testifying against the defendants testified falsely, in response to questioning by defense counsel, that they had not received promises from the prosecution. The prosecution failed to disclose that promises had in fact been made. The corruption of the truth-seeking process stemmed from the suppression of evidence affecting the overall credibility of the witnesses, see <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois"><i>Napue, supra,</i> at 269</a></span>; <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States"><i>Giglio, supra,</i> at 154</a></span>, and that corruption would have been present whether or not defense counsel had elicited statements from the witnesses denying that promises had been made.</p>
<p>It may be that contrary to the Court's insistence, its treatment of perjury cases reflects simply a desire to deter deliberate prosecutorial misconduct. But if that were the case, we might reasonably expect a rule imposing a lower threshold of materiality than the Court imposes perhaps a harmless-error standard. And we would certainly expect the rule to apply to a broader category of misconduct than the failure to disclose evidence that contradicts testimony offered by witnesses called by the prosecution. For the prosecutor is guilty of misconduct when he deliberately suppresses evidence that is clearly relevant and favorable to the defense, regardless, once again, of whether the evidence relates directly to testimony given in the course of the Government's case.</p>
<p>This case, however, does not involve deliberate prosecutorial misconduct. Leaving open the question whether a different rule might appropriately be applied in cases involving deliberate misconduct,<sup>[7]</sup> I would hold that the <span class="star-pagination">*122</span> defendant in this case had the burden of demonstrating that there is a significant chance that the withheld evidence, developed by skilled counsel, would have induced a reasonable doubt in the minds of enough jurors to avoid a conviction. This is essentially the standard applied by the Court of Appeals, and I would affirm its judgment.</p>
<h2>NOTES</h2>
<p>[1]  The alcohol level in Sewell's blood was slightly below the legal definition of intoxication.</p>
<p>[2]  Moreover, the motel clerk testified that Sewell's wife had said he "would use a knife"; however, Mrs. Sewell denied making this statement. There was no dispute about the fact that Sewell carried the bowie knife when he registered.</p>
<p>[3]  See <i>United States</i> v. <i>Burks,</i> 152 U. S. App. D. C. 284, 286, <span class="citation" data-id="9458954"><a href="/opinion/307051/united-states-v-james-h-burks/#434" aria-description="Citation for case: United States v. James H. Burks">470 F. 2d 432, 434</a></span> (1972).</p>
<p>[4]  "THE COURT: What are you saying? How can you request that which you don't know exists. That is the very essence of Brady.
</p>
<p>.....</p>
<p>"THE COURT: Are you arguing to the Court that the status of the law is that if you have a report indicating that fingerprints were taken and that the fingerprints on the item . . . which the defendant is alleged to have assaulted somebody turn out not to be the defendant's, that absent a specific request for that information, you do not have any obligation to defense counsel?</p>
<p>"MR. CLARKE: No, Your Honor. There is another aspect which comes to this, and that is whether or not the Government knowingly puts on perjured testimony. It has an obligation to correct that perjured testimony.</p>
<p>"THE COURT: I am not talking about perjured testimony. You don't do anything about it. You say nothing about it. You have got the report there. You know that possibly it could be exculpatory. Defense counsel doesn't know about it. He has been misinformed about it. Suppose he doesn't know about it. And because he has made no specific request for that information, you say that the status of the law under Brady is that you have no obligation as a prosecutor to open your mouth?</p>
<p>"MR. CLARKE: No. Your Honor . . . .</p>
<p>"But as the materiality of the items becomes less to the point where it is not material, there has to be a request, or else the Government, just like the defense, is not on notice." App. 147-149.</p>
<p>[5]  167 U. S. App. D. C. 28, <span class="citation" data-id="325310"><a href="/opinion/325310/united-states-v-linds-agurs-united-states-of-america-v-linda-v-agurs/" aria-description="Citation for case: United States v. Linds Agurs, United States of America v....">510 F. 2d 1249</a></span> (1975). The opinion of the Court of Appeals disposed of the direct appeal filed after respondent was sentenced as well as the two additional appeals taken from the two orders denying motions for new trial. After the denial of the first motion, respondent's counsel requested leave to withdraw in order to enable substitute counsel to file a new motion for a new trial on the ground that trial counsel's representation had been ineffective because he did not request Sewell's criminal record for the reason that he incorrectly believed that it was inadmissible. The District Court denied that motion. Although that action was challenged on appeal, the Court of Appeals did not find it necessary to pass on the validity of that ground. We think it clear, however, that counsel's failure to obtain Sewell's prior criminal record does not demonstrate ineffectiveness.</p>
<p>[6]  Although a majority of the active judges of the Circuit, as well as one of the members of the panel, expressed doubt about the validity of the panel's decision, the court refused to rehear the case en banc.</p>
<p>[7]  In <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Mooney</a></span></i> it was alleged that the petitioner's conviction was based on perjured testimony "which was knowingly used by the prosecuting authorities in order to obtain that conviction, and also that these authorities deliberately suppressed evidence which would have impeached and refuted the testimony thus given against him." <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#110" aria-description="Citation for case: Mooney v. Holohan">294 U. S., at 110</a></span>.
</p>
<p>The Court held that such allegations, if true, would establish such fundamental unfairness as to justify a collateral attack on petitioner's conviction.</p>
<p>"It is a requirement that cannot be deemed to be satisfied by mere notice and hearing if a State has contrived a conviction through the pretense of a trial which in truth is but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury by the presentation of testimony known to be perjured. Such a contrivance by a State to procure the conviction and imprisonment of a defendant is as inconsistent with the rudimentary demands of justice as is the obtaining of a like result by intimidation." <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan"><i>Id.,</i> at 112</a></span>.</p>
<p>[8]  <i>Pyle</i> v. <i>Kansas,</i> <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213</a></span>; <i>Alcorta</i> v. <i>Texas,</i> <span class="citation" data-id="105566"><a href="/opinion/105566/alcorta-v-texas/" aria-description="Citation for case: Alcorta v. Texas">355 U. S. 28</a></span>; <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span>; <i>Miller</i> v. <i>Pate,</i> <span class="citation" data-id="107354"><a href="/opinion/107354/miller-v-pate/" aria-description="Citation for case: Miller v. Pate">386 U. S. 1</a></span>; <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span>; <i>Donnelly</i> v. <i>DeChristoforo,</i> <span class="citation" data-id="9425708"><a href="/opinion/109024/donnelly-v-dechristoforo/" aria-description="Citation for case: Donnelly v. DeChristoforo">416 U. S. 637</a></span>.</p>
<p>[9]  See <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States"><i>Giglio, supra,</i> at 154</a></span>, quoting from <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois"><i>Napue, supra,</i> at 271</a></span>.</p>
<p>[10]  "We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. Although in <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Mooney</a></span></i> the Court had been primarily concerned with the willful misbehavior of the prosecutor, in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> the Court focused on the harm to the defendant resulting from nondisclosure. See discussions of this development in Note, The Prosecutor's Constitutional Duty to Reveal Evidence to the Defendant, 74 Yale L. J. 136 (1964); and Comment, <i>Brady</i> v. <i>Maryland</i> and The Prosecutor's Duty to Disclose, <span class="citation no-link">40 U. Chi. L. Rev. 112</span> (1972).</p>
<p>[11]  <span class="citation" data-id="1505680"><a href="/opinion/1505680/boblit-v-state/" aria-description="Citation for case: Boblit v. State">220 Md. 454</a></span>, <span class="citation" data-id="1505680"><a href="/opinion/1505680/boblit-v-state/" aria-description="Citation for case: Boblit v. State">154 A. 2d 434</a></span> (1959).</p>
<p>[12]  <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/" aria-description="Citation for case: Brady v. State">226 Md. 422</a></span>, 174 A. 2d. 167 (1961).</p>
<p>[13]  "The petitioner was denied due process of law by the State's suppression of evidence before his trial began. The proceeding must commence again from the stage at which the petitioner was overreached. The denial of due process of law vitiated the verdict and the sentence. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#545" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 545</a></span>. The verdict is not saved because other competent evidence would support it. <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#621" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 621</a></span>." Brief for Petitioner in <i>Brady</i> v. <i>Maryland</i><i>,</i> No. 490, O. T. 1962, p. 6.</p>
<p>[14]  See Comment, 40 U. Chi. L. Rev., <i>supra,</i> n. 10, at 115-117.</p>
<p>[15]  "In the present case a unanimous Court of Appeals has said that nothing in the suppressed confession `could have reduced the appellant Brady's offense below murder in the first degree.' We read that statement as a ruling on the admissibility of the confession on the issue of innocence or guilt. A sporting theory of justice might assume that if the suppressed confession had been used at the first trial, the judge's ruling that it was not admissible on the issue of innocence or guilt might have been flouted by the jury just as might have been done if the court had first admitted a confession and then stricken it from the record. But we cannot raise that trial strategy to the dignity of a constitutional right and say that the deprival of this defendant of that sporting chance through the use of a bifurcated trial (cf. <i>Williams</i> v. <i>New York,</i> <span class="citation" data-id="9420330"><a href="/opinion/104681/williams-v-new-york/" aria-description="Citation for case: Williams v. New York">337 U. S. 241</a></span>) denies him due process or violates the Equal Protection Clause of the Fourteenth Amendment." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#90" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 90-91</a></span> (footnote omitted).</p>
<p>[16]  In his opinion concurring in the judgment in <i>Giles</i> v. <i>Maryland,</i> <span class="citation" data-id="9423353"><a href="/opinion/107361/giles-v-maryland/#98" aria-description="Citation for case: Giles v. Maryland">386 U. S. 66, 98</a></span>, Mr. Justice Fortas stated:
</p>
<p>"This is not to say that convictions ought to be reversed on the ground that information merely repetitious, cumulative, or embellishing of facts otherwise known to the defense or presented to the court, or without importance to the defense for purposes of the preparation of the case or for trial was not disclosed to defense counsel. It is not to say that the State has an obligation to communicate preliminary, challenged, or speculative information."</p>
<p>[17]  In <i>Brady</i> this Court, as had the Maryland Court of Appeals, expressly rejected the good faith or the bad faith of the prosecutor as the controlling consideration: "We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, <i>irrespective of the good faith or bad faith of the prosecution.</i> The principle of <i>Mooney</i> v. <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Holohan</a></span></i> is not punishment of society for misdeeds of a prosecutor but avoidance of an unfair trial to the accused." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. (Emphasis added.) If the nature of the prosecutor's conduct is not controlling in a case like <i>Brady,</i> surely it should not be controlling when the prosecutor has not received a specific request for information.</p>
<p>[18]  The hypothetical example given by the District Judge in this case was fingerprint evidence demonstrating that the defendant could not have fired the fatal shot.</p>
<p>[19]  This is the standard generally applied by lower courts in evaluating motions for new trial under Fed. Rule Crim. Proc. 33 based on newly discovered evidence. See, <i>e. g., </i><i>Ashe</i> v. <i>United States,</i> <span class="citation" data-id="253599"><a href="/opinion/253599/neil-w-ashe-v-united-states-of-america-two-cases/#733" aria-description="Citation for case: Neil W. Ashe v. United States of America, (Two Cases)">288 F. 2d 725, 733</a></span> (CA6 1961); <i>United States</i> v. <i>Thompson,</i> <span class="citation" data-id="317641"><a href="/opinion/317641/united-states-v-carl-thompson-united-states-of-america-v-steven-teresi/#310" aria-description="Citation for case: United States v. Carl Thompson, United States of America...">493 F. 2d 305, 310</a></span> (CA9 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/834/">419 U. S. 834</a></span>; <i>United States</i> v. <i>Houle,</i> <span class="citation" data-id="9460174"><a href="/opinion/316285/united-states-v-joseph-g-houle-and-victor-diodato/#171" aria-description="Citation for case: United States v. Joseph G. Houle and Victor Diodato">490 F. 2d 167, 171</a></span> (CA2 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./417/970/">417 U. S. 970</a></span>; <i>United States</i> v. <i>Meyers,</i> <span class="citation" data-id="313335"><a href="/opinion/313335/united-states-v-irving-h-meyers-two-cases/#116" aria-description="Citation for case: United States v. Irving H. Meyers (Two Cases)">484 F. 2d 113, 116</a></span> (CA3 1973); <i>Heald</i> v. <i>United States,</i> <span class="citation" data-id="1474384"><a href="/opinion/1474384/heald-v-united-states/#883" aria-description="Citation for case: Heald v. United States">175 F. 2d 878, 883</a></span> (CA10 1949). See also 2 C. Wright, Federal Practice and Procedure § 557 (1969).</p>
<p>[20]  It has been argued that the standard should focus on the impact of the undisclosed evidence on the defendant's ability to prepare for trial, rather than the materiality of the evidence to the issue of guilt or innocence. See Note, The Prosecutor's Constitutional Duty to Reveal Evidence to the Defense, 74 Yale L. J. 136 (1964). Such a standard would be unacceptable for determining the materiality of what has been generally recognized as "<i>Brady</i> material" for two reasons. First, that standard would necessarily encompass incriminating evidence as well as exculpatory evidence, since knowledge of the prosecutor's entire case would always be useful in planning the defense. Second, such an approach would primarily involve an analysis of the adequacy of the notice given to the defendant by the State, and it has always been the Court's view that the notice component of due process refers to the charge rather than the evidentiary support for the charge.</p>
<p>[21]  "If, for example, one of only two eyewitnesses to a crime had told the prosecutor that the defendant was definitely not its perpetrator and if this statement was not disclosed to the defense, no court would hesitate to reverse a conviction resting on the testimony of the other eyewitness. But if there were fifty eyewitnesses, fortynine of whom identified the defendant, and the prosecutor neglected to reveal that the other, who was without his badly needed glasses on the misty evening of the crime, had said that the criminal looked something like the defendant but he could not be sure as he had only had a brief glimpse, the result might well be different." Comment, 40 U. Chi. L. Rev., <i>supra,</i> n. 10, at 125.</p>
<p>[22]  See, <i>e. g., </i><i>Stout</i> v. <i>Cupp,</i> <span class="citation" data-id="290286"><a href="/opinion/290286/wayne-l-stout-v-hoyt-c-cupp-warden/#882" aria-description="Citation for case: Wayne L. Stout v. Hoyt C. Cupp, Warden">426 F. 2d 881, 882-883</a></span> (CA9 1970); <i>Peterson</i> v. <i>United States,</i> <span class="citation" data-id="285177"><a href="/opinion/285177/gerald-d-peterson-v-united-states/#1079" aria-description="Citation for case: Gerald D. Peterson v. United States">411 F. 2d 1074, 1079</a></span> (CA8 1969); <i>Lessard</i> v. <i>Dickson,</i> <span class="citation" data-id="9453575"><a href="/opinion/279966/albert-lessard-v-fred-r-dickson-warden-california-state-prison-san/#90" aria-description="Citation for case: Albert Lessard v. Fred R. Dickson, Warden California...">394 F. 2d 88, 90-92</a></span> (CA9 1968), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./393/1004/">393 U. S. 1004</a></span>; <i>United States</i> v. <i>Tomaiolo,</i> <span class="citation" data-id="276039"><a href="/opinion/276039/united-states-v-charles-tomaiolo/#28" aria-description="Citation for case: United States v. Charles Tomaiolo">378 F. 2d 26, 28</a></span> (CA2 1967). One commentator has identified three different standards this way:
</p>
<p>"As discussed previously, in earlier cases the following standards for determining materiality for disclosure purposes were enunciated: (1) evidence which may be merely helpful to the defense; (2) evidence which raised a reasonable doubt as to defendant's guilt; (3) evidence which is of such a character as to create a substantial likelihood of reversal." Comment, Materiality and Defense Requests: Aids in Defining the Prosecutor's Duty of Disclosure, <span class="citation no-link">59 Iowa L. Rev. 433</span>, 445 (1973).</p>
<p>See also Note, The Duty of the Prosecutor to Disclose Exculpatory Evidence, 60 Col. L. Rev. 858 (1960).</p>
<p>[1]  The burden generally imposed upon such a motion has also been described as a burden of demonstrating that the newly discovered evidence would probably produce a different verdict in the event of a retrial. See, <i>e. g., </i><i>United States</i> v. <i>Kahn,</i> <span class="citation" data-id="307845"><a href="/opinion/307845/united-states-v-irving-b-kahn-and-teleprompter-corporation/#287" aria-description="Citation for case: United States v. Irving B. Kahn and Teleprompter Corporation">472 F. 2d 272, 287</a></span> (CA2 1973); <i>United States</i> v. <i>Rodriguez,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/437/940/">437 F. 2d 940</a></span>, 942 (CA5 1971); <i>United States</i> v. <i>Curran,</i> <span class="citation" data-id="305106"><a href="/opinion/305106/united-states-v-m-prial-curran/#264" aria-description="Citation for case: United States v. M. Prial Curran">465 F. 2d 260, 264</a></span> (CA7 1972).</p>
<p>[2]  See <i>United States</i> v. <i>Keogh,</i> <span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/#148" aria-description="Citation for case: United States v. James Vincent Keogh">391 F. 2d 138, 148</a></span> (CA2 1968), in which Judge Friendly implies that the standard the Court adopts is more severe than the standard the Court rejects.</p>
<p>[3]  To emphasize the harshness of the Court's rule, the defendant's fate is determined finally by the judge only if the judge does not entertain a reasonable doubt as to guilt. If evidence withheld by the prosecution does create a reasonable doubt as to guilt in the judge's mind, that does not end the caserather, the defendant (one might more accurately say the prosecution) is "entitled" to have the case decided by a jury.</p>
<p>[4]  In <i>Stout</i> v. <i>Cupp,</i> <span class="citation" data-id="290286"><a href="/opinion/290286/wayne-l-stout-v-hoyt-c-cupp-warden/" aria-description="Citation for case: Wayne L. Stout v. Hoyt C. Cupp, Warden">426 F. 2d 881</a></span> (CA9 1970), a habeas proceeding, the court simply quoted the District Court's finding that if the suppressed evidence had been introduced, "the jury would not have reached a different result." <span class="citation" data-id="290286"><a href="/opinion/290286/wayne-l-stout-v-hoyt-c-cupp-warden/#883" aria-description="Citation for case: Wayne L. Stout v. Hoyt C. Cupp, Warden"><i>Id.,</i> at 883</a></span>. There is no indication that the quoted language was intended as anything more than a finding of fact, which would, quite obviously, dispose of the defendant's claim under any standard that might be suggested. In <i>Peterson</i> v. <i>United States,</i> <span class="citation" data-id="285177"><a href="/opinion/285177/gerald-d-peterson-v-united-states/" aria-description="Citation for case: Gerald D. Peterson v. United States">411 F. 2d 1074</a></span> (CA8 1969), the court appeared to require a showing that the withheld evidence "was `material' and would have aided the defense." <span class="citation" data-id="285177"><a href="/opinion/285177/gerald-d-peterson-v-united-states/#1079" aria-description="Citation for case: Gerald D. Peterson v. United States"><i>Id.,</i> at 1079</a></span>. The court in <i>Lessard</i> v. <i>Dickson,</i> <span class="citation" data-id="9453575"><a href="/opinion/279966/albert-lessard-v-fred-r-dickson-warden-california-state-prison-san/" aria-description="Citation for case: Albert Lessard v. Fred R. Dickson, Warden California...">394 F. 2d 88</a></span> (CA9 1968), found it determinative that the withheld evidence "could hardly be regarded as being able to have much force against the inexorable array of incriminating circumstances with which [the defendant] was surrounded." <span class="citation" data-id="9453575"><a href="/opinion/279966/albert-lessard-v-fred-r-dickson-warden-california-state-prison-san/#91" aria-description="Citation for case: Albert Lessard v. Fred R. Dickson, Warden California..."><i>Id.,</i> at 91</a></span>. The jury, the court noted, would not have been "likely to have had any [difficulty]" with the argument defense counsel would have made with the withheld evidence. <span class="citation" data-id="9453575"><a href="/opinion/279966/albert-lessard-v-fred-r-dickson-warden-california-state-prison-san/#92" aria-description="Citation for case: Albert Lessard v. Fred R. Dickson, Warden California..."><i>Id.,</i> at 92</a></span>. Finally, <i>United States</i> v. <i>Tomaiolo,</i> <span class="citation" data-id="276039"><a href="/opinion/276039/united-states-v-charles-tomaiolo/" aria-description="Citation for case: United States v. Charles Tomaiolo">378 F. 2d 26</a></span> (CA2 1967), required the defendant to show that the evidence was "material and of some substantial use to the defendant." <span class="citation" data-id="276039"><a href="/opinion/276039/united-states-v-charles-tomaiolo/#28" aria-description="Citation for case: United States v. Charles Tomaiolo"><i>Id.,</i> at 28</a></span>.</p>
<p>[5]  See, <i>e. g., </i><i>United States</i> v. <i>Morell,</i> <span class="citation" data-id="9462216"><a href="/opinion/330694/united-states-v-pedro-morell-and-ramon-bruzon/#553" aria-description="Citation for case: United States v. Pedro Morell and Ramon Bruzon">524 F. 2d 550, 553</a></span> (CA2 1975); <i>Ogden</i> v. <i>Wolff,</i> <span class="citation" data-id="8897326"><a href="/opinion/8909699/ogden-v-wolff/#822" aria-description="Citation for case: Ogden v. Wolff">522 F. 2d 816, 822</a></span> (CA8 1975); <i>Woodcock</i> v. <i>Amaral,</i> <span class="citation" data-id="325594"><a href="/opinion/325594/lyle-s-woodcock-v-r-w-amaral/#991" aria-description="Citation for case: Lyle S. Woodcock v. R. W. Amaral">511 F. 2d 985, 991</a></span> (CA1 1974); <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="320391"><a href="/opinion/320391/united-states-of-america-charles-l-miller/#744" aria-description="Citation for case: United States of America, Charles L. Miller">499 F. 2d 736, 744</a></span> (CA10 1974); <i>Shuler</i> v. <i>Wainwright,</i> <span class="citation" data-id="316953"><a href="/opinion/316953/robert-shuler-and-jerry-chatman-v-louie-l-wainwright-direcotor-division/#1223" aria-description="Citation for case: Robert Shuler and Jerry Chatman v. Louie L. Wainwright,...">491 F. 2d 1213, 1223</a></span> (CA5 1974); <i>United States</i> v. <i>Kahn,</i> <span class="citation" data-id="307845"><a href="/opinion/307845/united-states-v-irving-b-kahn-and-teleprompter-corporation/#287" aria-description="Citation for case: United States v. Irving B. Kahn and Teleprompter Corporation">472 F. 2d, at 287</a></span>; <i>Clarke</i> v. <i>Burke,</i> <span class="citation" data-id="295841"><a href="/opinion/295841/charles-robert-clarke-v-john-c-burke/#855" aria-description="Citation for case: Charles Robert Clarke v. John C. Burke">440 F. 2d 853, 855</a></span> (CA7 1971); <i>Hamric</i> v. <i>Bailey,</i> <span class="citation" data-id="277986"><a href="/opinion/277986/bonnie-june-hamric-v-june-r-bailey-superintendent-of-the-west-virginia/#393" aria-description="Citation for case: Bonnie June Hamric v. June R. Bailey, Superintendent of...">386 F. 2d 390, 393</a></span> (CA4 1967).</p>
<p>[6]  That there is a significant difference between the Court's standards and what has been described as the prevailing view is made clear by Judge Friendly, writing for the court in <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9454610"><a href="/opinion/285114/united-states-v-james-miller/" aria-description="Citation for case: United States v. James Miller">411 F. 2d 825</a></span> (CA2 1969). After stating the court's conclusion that a new trial was required because of the Government's failure to disclose to the defense the pretrial hypnosis of its principal witness, Judge Friendly observed:
</p>
<p>"We have reached this conclusion with some reluctance, particularly in light of the considered belief of the able and conscientious district judge, who has lived with this case for years, that review of the record in light of all the defense new trial motions left him `convinced of the correctness of the jury's verdict.' We, who also have had no small exposure to the facts, are by no means convinced otherwise. The test, however, is not how the newly discovered evidence concerning the hypnosis would affect the trial judge or ourselves but whether, with the Government's case against [the defendant] already subject to serious attack, there was a significant chance that this added item, developed by skilled counsel as it would have been, could have induced a reasonable doubt in the minds of enough jurors to avoid a conviction. We cannot conscientiously say there was not." <span class="citation" data-id="9454610"><a href="/opinion/285114/united-states-v-james-miller/#832" aria-description="Citation for case: United States v. James Miller"><i>Id.,</i> at 832</a></span> (footnote omitted).</p>
<p>[7]  It is the presence of deliberate prosecutorial misconduct and a desire to deter such misconduct, presumably, that leads the Court to recognize a rule more readily permitting new trials in cases involving a specific defense request for information. The significance of the defense request, the Court states, is simply that it gives the prosecutor notice of what is important to the defense; once such notice is received, the failure to disclose is "seldom, if ever, excusable." <i>Ante,</i> at 106. It would seem to follow that if an item of information is of such obvious importance to the defense that it could not have escaped the prosecutor's attention, its suppression should be treated in the same manner as if there had been a specific request. This is precisely the approach taken by some courts. See, <i>e. g., </i><i>United States</i> v. <i>Morell,</i> <span class="citation" data-id="9462216"><a href="/opinion/330694/united-states-v-pedro-morell-and-ramon-bruzon/#553" aria-description="Citation for case: United States v. Pedro Morell and Ramon Bruzon">524 F. 2d, at 553</a></span>; <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="320391"><a href="/opinion/320391/united-states-of-america-charles-l-miller/#744" aria-description="Citation for case: United States of America, Charles L. Miller">499 F. 2d, at 744</a></span>; <i>United States</i> v. <i>Kahn,</i> <span class="citation" data-id="307845"><a href="/opinion/307845/united-states-v-irving-b-kahn-and-teleprompter-corporation/#287" aria-description="Citation for case: United States v. Irving B. Kahn and Teleprompter Corporation">472 F. 2d, at 287</a></span>; <i>United States</i> v. <i>Keogh,</i> <span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/#146" aria-description="Citation for case: United States v. James Vincent Keogh">391 F. 2d, at 146-147</a></span>.</p>

</div>
```

---
