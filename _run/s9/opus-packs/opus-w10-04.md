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

## GROUP: _overhaul2/lake/cases/Saucier v. Katz.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "83631ee1cc631d73", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Saucier v. Katz"}, "payload": {"all": [{"cite": "533 U.S. 194", "page": "194", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "533"}, {"cite": "121 S. Ct. 2151", "page": "2151", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "121"}, {"cite": "150 L. Ed. 2d 272", "page": "272", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "150"}, {"cite": "2001 U.S. LEXIS 4664", "page": "4664", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2001"}], "display": "533 U.S. 194", "official": {"cite": "533 U.S. 194", "page": "194", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "533"}, "official_selection_present": true, "record_id": "Saucier v. Katz"}}
{"assertion_id": "66c014958782c29b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-201a", "record_id": "Saucier v. Katz"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-201a", "pinpoint_status": "slip-only", "quote": "[I]f a violation could be made out on a favorable view of the parties' submissions, the next, sequential step is to ask whether the right was clearly established. . . . [in] light of the specific context of the case, not as a broad general proposition.", "quote_fidelity": "mismatch", "record_id": "Saucier v. Katz", "star_marker": null}}
{"assertion_id": "f07e33e8de730fb3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-201", "record_id": "Saucier v. Katz"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-201", "pinpoint_status": "slip-only", "quote": "--- # Saucier v. Katz *533 U.S. 194 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — sequence no longer mandatory per [[Pearson v. Callahan]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Saucier, a military police officer providing security at a base where Vice President Gore was speaking, removed Katz — an animal-rights protester who tried to display a banner — and allegedly shoved him roughly while putting him into a van. Katz sued under *Bivens* for excessive force. Saucier asserted qualified immunity; the Ninth Circuit denied it, treating the qualified-immunity inquiry as identical to the Fourth Amendment excessive-force merits. ## Issue How a court must analyze qualified immunity in an excessive-force case, and whether that inquiry collapses into the Fourth Amendment merits. ## Rule A court analyzes qualified immunity in a fixed sequence.", "quote_fidelity": "mismatch", "record_id": "Saucier v. Katz", "star_marker": null}}
{"assertion_id": "c352bf6a25283c15", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Saucier v. Katz"}, "payload": {"as_of_content": "2001-06-18", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "Saucier v. Katz", "scope_note": "Pearson v. Callahan (2009) held that Saucier's two-step sequence is no longer mandatory; Saucier's two-part qualified-immunity test survives.", "varies_by_point": true}}
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

## GROUP: _overhaul2/lake/cases/Schmerber v. California.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Schmerber v. California"
type: case
citation: "384 U.S. 757 (1966)"
parallel_cite: "86 S. Ct. 1826; 16 L. Ed. 2d 908"
neutral_cite: 1966 U.S. LEXIS 1129
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-06-20
docket: 658
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1966-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Schmerber v. California
  varies_by_point: false
  scope_note: "Foundational warrantless-blood-draw / bodily-intrusion case; good law. Missouri v. McNeely (2013) clarified that the natural dissipation of alcohol is not a per se exigency (exigency is case-by-case), and Birchfield v. North Dakota (2016) held blood tests are not justified as a search incident to arrest (breath tests are). Schmerber's own fact-bound holding stands."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107262/schmerber-v-california/"
  cluster_id: 107262
  opinion_id: 107262
  identity_checked: true
homes:
  - page: "[[Destruction of Evidence]]"
    role: "Key — Anchor"
  - page: "[[SIA Alcohol Tests]]"
    role: "Related (cross-doctrine)"
related: ["[[Missouri v. McNeely]]", "[[Birchfield v. North Dakota]]"]
aliases: []
tags: ["case", "fourth-amendment", "fifth-amendment", "exigent-circumstances", "blood-draw", "dui", "bodily-intrusion"]
holding: "Compelled blood/BAC evidence is physical, not testimonial, so it does not violate the Fifth Amendment; and a warrantless blood draw on probable cause is reasonable where exigency — dissipating alcohol plus time already lost — leaves no time to obtain a warrant."
lake:
  record_id: Schmerber v. California
  status: verified
  projected_at: 2026-07-09
---

# Schmerber v. California

*384 U.S. 757 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Schmerber was arrested for driving under the influence at a hospital where he was being treated for injuries from a car accident he had apparently caused. At the direction of the arresting officer and over Schmerber's refusal, a physician drew a blood sample, and its analysis (showing intoxication) was admitted at his trial. He argued the compelled blood draw violated, among other things, his Fifth Amendment privilege against self-incrimination and his Fourth Amendment right against unreasonable searches.

## Issue
Whether the compelled, warrantless withdrawal and chemical analysis of a DUI arrestee's blood violates (1) the Fifth Amendment privilege against self-incrimination, and (2) the Fourth Amendment.

## Rule
**Fifth Amendment** — blood-alcohol evidence is physical, not testimonial: "the privilege protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature, and that the withdrawal of blood and use of the analysis in question in this case did not involve compulsion to these ends." — 384 U.S. at 761. ^pin-761

**Fourth Amendment** — a warrantless blood draw on probable cause is reasonable when [[Exigent Circumstances and Hot Pursuit|exigency]] leaves no time for a warrant. Because alcohol diminishes after drinking stops and time was lost transporting the accused and investigating the scene, "there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case was an appropriate incident to petitioner's arrest." — [*Id.* at 770–771](https://www.courtlistener.com/opinion/107262/schmerber-v-california/#:~:text=there%20was%20no%20time%20to). ^pin-770

## Application
Schmerber's blood-alcohol level was naturally falling as his body metabolized the alcohol, and the officer — who had probable cause to believe he had been driving while intoxicated — had spent the available time bringing him to the hospital and investigating the accident, leaving no opportunity to obtain a warrant. On those special facts the warrantless extraction of blood was a reasonable response to the threatened loss of evidence, and a blood test performed by a physician in a hospital was a reasonable means of obtaining it.

## Conclusion
Neither the Fifth nor the Fourth Amendment was violated; the conviction was affirmed. *Schmerber* anchors the warrantless-blood-draw/bodily-intrusion line later refined by [[Missouri v. McNeely]] (no [[Common Legal Terms#per-se|per se]] DUI [[Exigent Circumstances and Hot Pursuit|exigency]]) and [[Birchfield v. North Dakota]] (breath, not blood, as a [[Search Incident to Arrest|search incident to arrest]]).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- [[Missouri v. McNeely]] (2013) **clarified** that the natural dissipation of alcohol does **not** create a [[Common Legal Terms#per-se|per se]] [[Exigent Circumstances and Hot Pursuit|exigency]] justifying a warrantless DUI blood draw; [[Exigent Circumstances and Hot Pursuit|exigency]] is judged case-by-case on the totality — consistent with *Schmerber*'s own fact-bound analysis.
- [[Birchfield v. North Dakota]] (2016) held a warrantless **blood** test is **not** justified as a search incident to a DUI arrest (a **breath** test is), so post-*[[Birchfield v. North Dakota|Birchfield]]* a warrantless blood draw rests on [[Exigent Circumstances and Hot Pursuit|exigency]] or another exception, not SITA.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Anchor*
- [[SIA Alcohol Tests]] — *Related (cross-doctrine)*

## Sources
- *Schmerber v. California*, 384 U.S. 757 (1966) — https://www.courtlistener.com/opinion/107262/schmerber-v-california/ — pinpoints: 761, 770–771.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6740d5acbd2935d7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Schmerber v. California"}, "payload": {"all": [{"cite": "384 U.S. 757", "page": "757", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "384"}, {"cite": "86 S. Ct. 1826", "page": "1826", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "86"}, {"cite": "16 L. Ed. 2d 908", "page": "908", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "16"}, {"cite": "1966 U.S. LEXIS 1129", "page": "1129", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1966"}], "display": "384 U.S. 757", "official": {"cite": "384 U.S. 757", "page": "757", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "384"}, "official_selection_present": true, "record_id": "Schmerber v. California"}}
{"assertion_id": "abaf2e6bd2afe4eb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-761", "record_id": "Schmerber v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-761", "pinpoint_status": "slip-only", "quote": "--- # Schmerber v. California *384 U.S. 757 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Schmerber was arrested for driving under the influence at a hospital where he was being treated for injuries from a car accident he had apparently caused. At the direction of the arresting officer and over Schmerber's refusal, a physician drew a blood sample, and its analysis (showing intoxication) was admitted at his trial. He argued the compelled blood draw violated, among other things, his Fifth Amendment privilege against self-incrimination and his Fourth Amendment right against unreasonable searches. ## Issue Whether the compelled, warrantless withdrawal and chemical analysis of a DUI arrestee's blood violates (1) the Fifth Amendment privilege against self-incrimination, and (2) the Fourth Amendment. ## Rule **Fifth Amendment** — blood-alcohol evidence is physical, not testimonial:", "quote_fidelity": "mismatch", "record_id": "Schmerber v. California", "star_marker": null}}
{"assertion_id": "b026715f949f054a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-770", "record_id": "Schmerber v. California"}, "payload": {"fragment": "#:~:text=there%20was%20no%20time%20to", "page": null, "pin_id": "pin-770", "pinpoint_status": "star-verified", "quote": "there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case was an appropriate incident to petitioner's arrest.", "quote_fidelity": "matched", "record_id": "Schmerber v. California", "star_marker": "771"}}
{"assertion_id": "bface561efa1a3f9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Schmerber v. California"}, "payload": {"as_of_content": "1966-06-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Schmerber v. California", "scope_note": "Foundational warrantless-blood-draw / bodily-intrusion case; good law. Missouri v. McNeely (2013) clarified that the natural dissipation of alcohol is not a per se exigency (exigency is case-by-case), and Birchfield v. North Dakota (2016) held blood tests are not justified as a search incident to arrest (breath tests are). Schmerber's own fact-bound holding stands.", "varies_by_point": false}}
```

### lake record — Schmerber v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Schmerber v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Schmerber v. California",
    "case_name_short": "Schmerber",
    "case_name_full": "Schmerber v. California",
    "input_case_name": "Schmerber v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-06-20",
    "year": 1966,
    "docket": "658",
    "cluster_id": 107262,
    "lead_opinion_id": 107262,
    "sibling_ids": [
      107262,
      9423255,
      9423256,
      9423257,
      9423258,
      9423259,
      9423260
    ],
    "absolute_url": "/opinion/107262/schmerber-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "384 U.S. 757",
      "volume": "384",
      "reporter": "U.S.",
      "page": "757",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "86 S. Ct. 1826",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1826",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 908",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "908",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 1129",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "1129",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "384 U.S. 757",
        "volume": "384",
        "reporter": "U.S.",
        "page": "757",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 S. Ct. 1826",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1826",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 908",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "908",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 1129",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "1129",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "384 U.S. 757",
    "official_selection": {
      "court_class": "scotus",
      "selected": "384 U.S. 757",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-761",
      "page": null,
      "quote": "--- # Schmerber v. California *384 U.S. 757 (1966)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Schmerber was arrested for driving under the influence at a hospital where he was being treated for injuries from a car accident he had apparently caused. At the direction of the arresting officer and over Schmerber's refusal, a physician drew a blood sample, and its analysis (showing intoxication) was admitted at his trial. He argued the compelled blood draw violated, among other things, his Fifth Amendment privilege against self-incrimination and his Fourth Amendment right against unreasonable searches. ## Issue Whether the compelled, warrantless withdrawal and chemical analysis of a DUI arrestee's blood violates (1) the Fifth Amendment privilege against self-incrimination, and (2) the Fourth Amendment. ## Rule **Fifth Amendment** \u2014 blood-alcohol evidence is physical, not testimonial:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-770",
      "page": null,
      "quote": "there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case was an appropriate incident to petitioner's arrest.",
      "star_marker": "771",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 24817,
      "fragment": "#:~:text=there%20was%20no%20time%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1966-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Schmerber v. California",
    "varies_by_point": false,
    "scope_note": "Foundational warrantless-blood-draw / bodily-intrusion case; good law. Missouri v. McNeely (2013) clarified that the natural dissipation of alcohol is not a per se exigency (exigency is case-by-case), and Birchfield v. North Dakota (2016) held blood tests are not justified as a search incident to arrest (breath tests are). Schmerber's own fact-bound holding stands.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Bell",
          "cluster_id": 10747468,
          "cite": [
            "2025 ND 201"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9493043,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9473742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bohigian",
          "cluster_id": 4806187,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Dennis",
          "cluster_id": 4679939,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
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
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Gutierrez",
          "cluster_id": 6240355,
          "cite": [
            "245 Cal. Rptr. 3d 143",
            "33 Cal. App. Supp. 5th 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ingraham v. Wright",
          "cluster_id": 109635,
          "cite": [
            "51 L. Ed. 2d 711",
            "97 S. Ct. 1401",
            "430 U.S. 651",
            "1977 U.S. LEXIS 74"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nobles",
          "cluster_id": 109292,
          "cite": [
            "45 L. Ed. 2d 141",
            "95 S. Ct. 2160",
            "422 U.S. 225",
            "1975 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. Harper",
          "cluster_id": 112381,
          "cite": [
            "108 L. Ed. 2d 178",
            "110 S. Ct. 1028",
            "494 U.S. 210",
            "1990 U.S. LEXIS 1174"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107262 OR 9423255 OR 9423256 OR 9423257 OR 9423258 OR 9423259 OR 9423260) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI4MjQzMjAwMDAwJnM9NDUwNTAzMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107262+OR+9423255+OR+9423256+OR+9423257+OR+9423258+OR+9423259+OR+9423260%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107262 OR 9423255 OR 9423256 OR 9423257 OR 9423258 OR 9423259 OR 9423260)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTcmcz0xMDg2NTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107262+OR+9423255+OR+9423256+OR+9423257+OR+9423258+OR+9423259+OR+9423260%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107262 OR 9423255 OR 9423256 OR 9423257 OR 9423258 OR 9423259 OR 9423260)",
        "reviewed": 51,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 51,
        "triage_read": 3,
        "triage_snippet_classified": 48
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107262 OR 9423255 OR 9423256 OR 9423257 OR 9423258 OR 9423259 OR 9423260)",
    "indexed_citing_opinions": 4034,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107262,
        "count": 3693,
        "count_source": "search"
      },
      {
        "opinion_id": 9423255,
        "count": 457,
        "count_source": "search"
      },
      {
        "opinion_id": 9423256,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423257,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423258,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423259,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423260,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6073,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/schmerber-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjcyMSZzPTEwMzYwOTgxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107262+OR+9423255+OR+9423256+OR+9423257+OR+9423258+OR+9423259+OR+9423260%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107262,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 103557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 271964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1212162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1347242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1421285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1421344,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1440868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1447648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1923442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 3579530,
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
    "date_created": "2026-07-05T18:39:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:39:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:39:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:41:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:39:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Schmerber v. California

```
<div>
<center><b><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S. 757</a></span> (1966)</b></center>
<center><h1>SCHMERBER<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 658.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 25, 1966.</center>
<center>Decided June 20, 1966.</center>
CERTIORARI TO THE APPELLATE DEPARTMENT OF THE SUPERIOR COURT OF CALIFORNIA, COUNTY OF LOS ANGELES.
<p><span class="star-pagination">*758</span> <i>Thomas M. McGurrin</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Edward L. Davenport</i> argued the cause for respondent. On the brief were <i>Roger Arnebergh</i> and <i>Philip E. Grey.</i></p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>Petitioner was convicted in Los Angeles Municipal Court of the criminal offense of driving an automobile while under the influence of intoxicating liquor.<sup>[1]</sup> He had been arrested at a hospital while receiving treatment for injuries suffered in an accident involving the automobile that he had apparently been driving.<sup>[2]</sup> At the direction of a police officer, a blood sample was then withdrawn from petitioner's body by a physician at the hospital. <span class="star-pagination">*759</span> The chemical analysis of this sample revealed a percent by weight of alcohol in his blood at the time of the offense which indicated intoxication, and the report of this analysis was admitted in evidence at the trial. Petitioner objected to receipt of this evidence of the analysis on the ground that the blood had been withdrawn despite his refusal, on the advice of his counsel, to consent to the test. He contended that in that circumstance the withdrawal of the blood and the admission of the analysis in evidence denied him due process of law under the Fourteenth Amendment, as well as specific guarantees of the Bill of Rights secured against the States by that Amendment: his privilege against self-incrimination under the Fifth Amendment; his right to counsel under the Sixth Amendment; and his right not to be subjected to unreasonable searches and seizures in violation of the Fourth Amendment. The Appellate Department of the California Superior Court rejected these contentions and affirmed the conviction.<sup>[3]</sup> In view of constitutional decisions since we last considered these issues in <i>Breithaupt</i> v. <i>Abram,</i> 352 U. S. 432see <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>; <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span>, and <i>Mapp</i> v. <i>Ohio,</i> 367 U. S. 643we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./382/971/">382 U. S. 971</a></span>. We affirm.</p>
<p></p>
<h2>I.</h2>
<p></p>
<h2>THE DUE PROCESS CLAUSE CLAIM.</h2>
<p><i>Breithaupt</i> was also a case in which police officers caused blood to be withdrawn from the driver of an automobile involved in an accident, and in which there was ample justification for the officer's conclusion that the driver was under the influence of alcohol. There, as here, the extraction was made by a physician in a simple, medically acceptable manner in a hospital environment. <span class="star-pagination">*760</span> There, however, the driver was unconscious at the time the blood was withdrawn and hence had no opportunity to object to the procedure. We affirmed the conviction there resulting from the use of the test in evidence, holding that under such circumstances the withdrawal did not offend "that `sense of justice' of which we spoke in <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span>." 352 U. S., at 435. <i>Breithaupt</i> thus requires the rejection of petitioner's due process argument, and nothing in the circumstances of this case<sup>[4]</sup> or in supervening events persuades us that this aspect of <i>Breithaupt</i> should be overruled.</p>
<p></p>
<h2>II.</h2>
<p></p>
<h2>THE PRIVILEGE AGAINST SELF-INCRIMINATION CLAIM.</h2>
<p><i>Breithaupt</i> summarily rejected an argument that the withdrawal of blood and the admission of the analysis report involved in that state case violated the Fifth Amendment privilege of any person not to "be compelled in any criminal case to be a witness against himself," citing <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>. But that case, holding that the protections of the Fourteenth Amendment do not embrace this Fifth Amendment privilege, has been succeeded by <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span>. We there held that "[t]he Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringement the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, <span class="star-pagination">*761</span> and to suffer no penalty . . . for such silence." We therefore must now decide whether the withdrawal of the blood and admission in evidence of the analysis involved in this case violated petitioner's privilege. We hold that the privilege protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature,<sup>[5]</sup> and that the withdrawal of blood and use of the analysis in question in this case did not involve compulsion to these ends.</p>
<p>It could not be denied that in requiring petitioner to submit to the withdrawal and chemical analysis of his blood the State compelled him to submit to an attempt to discover evidence that might be used to prosecute him for a criminal offense. He submitted only after the police officer rejected his objection and directed the physician to proceed. The officer's direction to the physician to administer the test over petitioner's objection constituted compulsion for the purposes of the privilege. The critical question, then is whether petitioner was thus compelled "to be a witness against himself."<sup>[6]</sup></p>
<p><span class="star-pagination">*762</span> If the scope of the privilege coincided with the complex of values it helps to protect, we might be obliged to conclude that the privilege was violated. In <i>Miranda</i> v. <i>Arizona, ante,</i> at 460, the Court said of the interests protected by the privilege: "All these policies point to one overriding thought: the constitutional foundation underlying the privilege is the respect a governmentstate or federal must accord to the dignity and integrity of its citizens. To maintain a `fair state-individual balance,' to require the government `to shoulder the entire load' . . . to respect the inviolability of the human personality, our accusatory system of criminal justice demands that the government seeking to punish an individual produce the evidence against him by its own independent labors, rather than by the cruel, simple expedient of compelling it from his own mouth." The withdrawal of blood necessarily involves puncturing the skin for extraction, and the percent by weight of alcohol in that blood, as established by chemical analysis, is evidence of criminal guilt. Compelled submission fails on one view to respect the "inviolability of the human personality." Moreover, since it enables the State to rely on evidence forced from the accused, the compulsion violates at least one meaning of the requirement that the State procure the evidence against an accused "by its own independent labors."</p>
<p>As the passage in <i>Miranda</i> implicitly recognizes, however, the privilege has never been given the full scope which the values it helps to protect suggest. History <span class="star-pagination">*763</span> and a long line of authorities in lower courts have consistently limited its protection to situations in which the State seeks to submerge those values by obtaining the evidence against an accused through "the cruel, simple expedient of compelling it from his own mouth. . . . In sum, the privilege is fulfilled only when the person is guaranteed the right `to remain silent unless he chooses to speak in the unfettered exercise of his own will.' " <i><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Ibid.</a></span></i> The leading case in this Court is <i>Holt</i> v. <i>United States,</i> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span>. There the question was whether evidence was admissible that the accused, prior to trial and over his protest, put on a blouse that fitted him. It was contended that compelling the accused to submit to the demand that he model the blouse violated the privilege. Mr. Justice Holmes, speaking for the Court, rejected the argument as "based upon an extravagant extension of the Fifth Amendment," and went on to say: "[T]he prohibition of compelling a man in a criminal court to be witness against himself is a prohibition of the use of physical or moral compulsion to extort communications from him, not an exclusion of his body as evidence when it may be material. The objection in principle would forbid a jury to look at a prisoner and compare his features with a photograph in proof." <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#252" aria-description="Citation for case: Holt v. United States">218 U. S., at 252-253</a></span>.<sup>[7]</sup></p>
<p>It is clear that the protection of the privilege reaches an accused's communications, whatever form they might <span class="star-pagination">*764</span> take, and the compulsion of responses which are also communications, for example, compliance with a subpoena to produce one's papers. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>. On the other hand, both federal and state courts have usually held that it offers no protection against compulsion to submit to fingerprinting, photographing, or measurements, to write or speak for identification, to appear in court, to stand, to assume a stance, to walk, or to make a particular gesture.<sup>[8]</sup> The distinction which has emerged, often expressed in different ways, is that the privilege is a bar against compelling "communications" or "testimony," but that compulsion which makes a suspect or accused the source of "real or physical evidence" does not violate it.</p>
<p>Although we agree that this distinction is a helpful framework for analysis, we are not to be understood to agree with past applications in all instances. There will be many cases in which such a distinction is not readily drawn. Some tests seemingly directed to obtain "physical evidence," for example, lie detector tests measuring changes in body function during interrogation, may actually be directed to eliciting responses which are essentially testimonial. To compel a person to submit to testing in which an effort will be made to determine his guilt or innocence on the basis of physiological responses, whether willed or not, is to evoke the spirit and history of the Fifth Amendment. Such situations call to mind the principle that the protection of the privilege "is as broad as the mischief against which it seeks to guard," <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span>.</p>
<p><span class="star-pagination">*765</span> In the present case, however, no such problem of application is presented. Not even a shadow of testimonial compulsion upon or enforced communication by the accused was involved either in the extraction or in the chemical analysis. Petitioner's testimonial capacities were in no way implicated; indeed, his participation, except as a donor, was irrelevant to the results of the test, which depend on chemical analysis and on that alone.<sup>[9]</sup> Since the blood test evidence, although an incriminating product of compulsion, was neither petitioner's testimony nor evidence relating to some communicative act or writing by the petitioner, it was not inadmissible on privilege grounds.</p>
<p></p>
<h2>III.</h2>
<p></p>
<h2>THE RIGHT TO COUNSEL CLAIM.</h2>
<p>This conclusion also answers petitioner's claim that, in compelling him to submit to the test in face of the fact that his objection was made on the advice of counsel, <span class="star-pagination">*766</span> he was denied his Sixth Amendment right to the assistance of counsel. Since petitioner was not entitled to assert the privilege, he has no greater right because counsel erroneously advised him that he could assert it. His claim is strictly limited to the failure of the police to respect his wish, reinforced by counsel's advice, to be left inviolate. No issue of counsel's ability to assist petitioner in respect of any rights he did possess is presented. The limited claim thus made must be rejected.</p>
<p></p>
<h2>IV.</h2>
<p></p>
<h2>THE SEARCH AND SEIZURE CLAIM.</h2>
<p>In <i>Breithaupt,</i> as here, it was also contended that the chemical analysis should be excluded from evidence as the product of an unlawful search and seizure in violation of the Fourth and Fourteenth Amendments. The Court did not decide whether the extraction of blood in that case was unlawful, but rejected the claim on the basis of <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>. That case had held that the Constitution did not require, in state prosecutions for state crimes, the exclusion of evidence obtained in violation of the Fourth Amendment's provisions. We have since overruled <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> in that respect, holding in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, that the exclusionary rule adopted for federal prosecutions in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, must also be applied in criminal prosecutions in state courts. The question is squarely presented therefore, whether the chemical analysis <span class="star-pagination">*767</span> introduced in evidence in this case should have been excluded as the product of an unconstitutional search and seizure.</p>
<p>The overriding function of the Fourth Amendment is to protect personal privacy and dignity against unwarranted intrusion by the State. In <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> we recognized "[t]he security of one's privacy against arbitrary intrusion by the police" as being "at the core of the Fourth Amendment" and "basic to a free society." <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 27</a></span>. We reaffirmed that broad view of the Amendment's purpose in applying the federal exclusionary rule to the States in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>.</i></p>
<p>The values protected by the Fourth Amendment thus substantially overlap those the Fifth Amendment helps to protect. History and precedent have required that we today reject the claim that the Self-Incrimination Clause of the Fifth Amendment requires the human body in all circumstances to be held inviolate against state expeditions seeking evidence of crime. But if compulsory administration of a blood test does not implicate the Fifth Amendment, it plainly involves the broadly conceived reach of a search and seizure under the Fourth Amendment. That Amendment expressly provides that "[t]he right of the people to be secure in their <i>persons,</i> houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . ." (Emphasis added.) It could not reasonably be argued, and indeed respondent does not argue, that the administration of the blood test in this case was free of the constraints of the Fourth Amendment. Such testing procedures plainly constitute searches of "persons," and depend antecedently upon seizures of "persons," within the meaning of that Amendment.</p>
<p>Because we are dealing with intrusions into the human body rather than with state interferences with property relationships or private papers"houses, papers, and <span class="star-pagination">*768</span> effects"we write on a clean slate. Limitations on the kinds of property which may be seized under warrant,<sup>[10]</sup> as distinct from the procedures for search and the permissible scope of search,<sup>[11]</sup> are not instructive in this context. We begin with the assumption that once the privilege against self-incrimination has been found not to bar compelled intrusions into the body for blood to be analyzed for alcohol content, the Fourth Amendment's proper function is to constrain, not against all intrusions as such, but against intrusions which are not justified in the circumstances, or which are made in an improper manner. In other words, the questions we must decide in this case are whether the police were justified in requiring petitioner to submit to the blood test, and whether the means and procedures employed in taking his blood respected relevant Fourth Amendment standards of reasonableness.</p>
<p>In this case, as will often be true when charges of driving under the influence of alcohol are pressed, these questions arise in the context of an arrest made by an officer without a warrant. Here, there was plainly probable cause for the officer to arrest petitioner and charge him with driving an automobile while under the influence of intoxicating liquor.<sup>[12]</sup> The police officer who arrived <span class="star-pagination">*769</span> at the scene shortly after the accident smelled liquor on petitioner's breath, and testified that petitioner's eyes were "bloodshot, watery, sort of a glassy appearance." The officer saw petitioner again at the hospital, within two hours of the accident. There he noticed similar symptoms of drunkenness. He thereupon informed petitioner "that he was under arrest and that he was entitled to the services of an attorney, and that he could remain silent, and that anything that he told me would be used against him in evidence."</p>
<p>While early cases suggest that there is an unrestricted "right on the part of the Government, always recognized under English and American law, to search the person of the accused when legally arrested to discover and seize the fruits or evidences of crime," <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>; <i>People</i> v. <i>Chiagles,</i> <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/" aria-description="Citation for case: People v. . Chiagles">237 N. Y. 193</a></span>, <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/" aria-description="Citation for case: People v. . Chiagles">142 N. E. 583</a></span> (1923) (Cardozo, J.), the mere fact of a lawful arrest does not end our inquiry. The suggestion of these cases apparently rests on two factorsfirst, there may be more immediate danger of concealed weapons or of destruction of evidence under the direct control of the accused, <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#72" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 72-73</a></span> (Frankfurter, J., dissenting); second, once a search of the arrested person for weapons is permitted, it would be both impractical and unnecessary to enforcement of the Fourth Amendment's purpose to attempt to confine the search to those objects alone. <i>People</i> v. <i>Chiagles,</i> <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#197" aria-description="Citation for case: People v. . Chiagles">237 N. Y., at 197-198</a></span>, <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#584" aria-description="Citation for case: People v. . Chiagles">142 N. E., at 584</a></span>. Whatever the validity of these considerations in general, they have little applicability with respect to searches involving intrusions beyond the body's surface. The interests in <span class="star-pagination">*770</span> human dignity and privacy which the Fourth Amendment protects forbid any such intrusions on the mere chance that desired evidence might be obtained. In the absence of a clear indication that in fact such evidence will be found, these fundamental human interests require law officers to suffer the risk that such evidence may disappear unless there is an immediate search.</p>
<p>Although the facts which established probable cause to arrest in this case also suggested the required relevance and likely success of a test of petitioner's blood for alcohol, the question remains whether the arresting officer was permitted to draw these inferences himself, or was required instead to procure a warrant before proceeding with the test. Search warrants are ordinarily required for searches of dwellings, and, absent an emergency, no less could be required where intrusions into the human body are concerned. The requirement that a warrant be obtained is a requirement that the inferences to support the search "be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span>; see also <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#110" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 110-111</a></span>. The importance of informed, detached and deliberate determinations of the issue whether or not to invade another's body in search of evidence of guilt is indisputable and great.</p>
<p>The officer in the present case, however, might reasonably have believed that he was confronted with an emergency, in which the delay necessary to obtain a warrant, under the circumstances, threatened "the destruction of evidence," <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span>. We are told that the percentage of alcohol in the blood begins to diminish shortly after drinking stops, as the body functions to eliminate it from the system. Particularly in a case such as this, where time had <span class="star-pagination">*771</span> to be taken to bring the accused to a hospital and to investigate the scene of the accident, there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case was an appropriate incident to petitioner's arrest.</p>
<p>Similarly, we are satisfied that the test chosen to measure petitioner's blood-alcohol level was a reasonable one. Extraction of blood samples for testing is a highly effective means of determining the degree to which a person is under the influence of alcohol. See <i>Breithaupt</i> v. <i>Abram,</i> 352 U. S., at 436, n. 3. Such tests are a commonplace in these days of periodic physical examinations<sup>[13]</sup> and experience with them teaches that the quantity of blood extracted is minimal, and that for most people the procedure involves virtually no risk, trauma, or pain. Petitioner is not one of the few who on grounds of fear, concern for health, or religious scruple might prefer some other means of testing, such as the "breathalyzer" test petitioner refused, see n. 9, <i>supra.</i> We need not decide whether such wishes would have to be respected.<sup>[14]</sup></p>
<p>Finally, the record shows that the test was performed in a reasonable manner. Petitioner's blood was taken by a physician in a hospital environment according to accepted medical practices. We are thus not presented with the serious questions which would arise if a search involving use of a medical technique, even of the most <span class="star-pagination">*772</span> rudimentary sort, were made by other than medical personnel or in other than a medical environmentfor example, if it were administered by police in the privacy of the stationhouse. To tolerate searches under these conditions might be to invite an unjustified element of personal risk of infection and pain.</p>
<p>We thus conclude that the present record shows no violation of petitioner's right under the Fourth and Fourteenth Amendments to be free of unreasonable searches and seizures. It bears repeating, however, that we reach this judgment only on the facts of the present record. The integrity of an individual's person is a cherished value of our society. That we today hold that the Constitution does not forbid the States minor intrusions into an individual's body under stringently limited conditions in no way indicates that it permits more substantial intrusions, or intrusions under other conditions.</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE STEWART joins, concurring.</p>
<p>In joining the Court's opinion I desire to add the following comment. While agreeing with the Court that the taking of this blood test involved no testimonial compulsion, I would go further and hold that apart from this consideration the case in no way implicates the Fifth Amendment. Cf. my dissenting opinion and that of MR. JUSTICE WHITE in <i>Miranda</i> v. <i>Arizona, ante,</i> pp. 504, 526.</p>
<p>MR. CHIEF JUSTICE WARREN, dissenting.</p>
<p>While there are other important constitutional issues in this case, I believe it is sufficient for me to reiterate my dissenting opinion in <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#440" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 440</a></span>, as the basis on which to reverse this conviction.</p>
<p><span class="star-pagination">*773</span> MR. JUSTICE BLACK with whom MR. JUSTICE DOUGLAS joins, dissenting.</p>
<p>I would reverse petitioner's conviction. I agree with the Court that the Fourteenth Amendment made applicable to the States the Fifth Amendment's provision that "No person . . . shall be compelled in any criminal case to be a witness against himself . . . ." But I disagree with the Court's holding that California did not violate petitioner's constitutional right against self-incrimination when it compelled him, against his will, to allow a doctor to puncture his blood vessels in order to extract a sample of blood and analyze it for alcoholic content, and then used that analysis as evidence to convict petitioner of a crime.</p>
<p>The Court admits that "the State compelled [petitioner] to submit to an attempt to discover evidence [in his blood] that might be [and was] used to prosecute him for a criminal offense." To reach the conclusion that compelling a person to give his blood to help the State convict him is not equivalent to compelling him to be a witness against himself strikes me as quite an extraordinary feat. The Court, however, overcomes what had seemed to me to be an insuperable obstacle to its conclusion by holding that</p>
<blockquote>". . . the privilege protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature, and that the withdrawal of blood and use of the analysis in question in this case did not involve compulsion to these ends." (Footnote omitted.)</blockquote>
<p>I cannot agree that this distinction and reasoning of the Court justify denying petitioner his Bill of Rights' guarantee that he must not be compelled to be a witness against himself.</p>
<p><span class="star-pagination">*774</span> In the first place it seems to me that the compulsory extraction of petitioner's blood for analysis so that the person who analyzed it could give evidence to convict him had both a "testimonial" and a "communicative nature." The sole purpose of this project which proved to be successful was to obtain "testimony" from some person to prove that petitioner had alcohol in his blood at the time he was arrested. And the purpose of the project was certainly "communicative" in that the analysis of the blood was to supply information to enable a witness to communicate to the court and jury that petitioner was more or less drunk.</p>
<p>I think it unfortunate that the Court rests so heavily for its very restrictive reading of the Fifth Amendment's privilege against self-incrimination on the words "testimonial" and "communicative." These words are not models of clarity and precision as the Court's rather labored explication shows. Nor can the Court, so far as I know, find precedent in the former opinions of this Court for using these particular words to limit the scope of the Fifth Amendment's protection. There is a scholarly precedent, however, in the late Professor Wigmore's learned treatise on evidence. He used "testimonial" which, according to the latest edition of his treatise revised by McNaughton, means "communicative" (8 Wigmore, Evidence § 2263 (McNaughton rev. 1961), p. 378), as a key word in his vigorous and extensive campaign designed to keep the privilege against self-incrimination "within limits the strictest possible." 8 Wigmore, Evidence § 2251 (3d ed. 1940), p. 318. Though my admiration for Professor Wigmore's scholarship is great, I regret to see the word he used to narrow the Fifth Amendment's protection play such a major part in any of this Court's opinions.</p>
<p>I am happy that the Court itself refuses to follow Professor Wigmore's implication that the Fifth Amendment <span class="star-pagination">*775</span> goes no further than to bar the use of forced self-incrimination statements coming from a "person's own lips." It concedes, as it must so long as <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, stands, that the Fifth Amendment bars a State from compelling a person to produce papers he has that might tend to incriminate him. It is a strange hierarchy of values that allows the State to extract a human being's blood to convict him of a crime because of the blood's content but proscribes compelled production of his lifeless papers. Certainly there could be few papers that would have any more "testimonial" value to convict a man of drunken driving than would an analysis of the alcoholic content of a human being's blood introduced in evidence at a trial for driving while under the influence of alcohol. In such a situation blood, of course, is not oral testimony given by an accused but it can certainly "communicate" to a court and jury the fact of guilt.</p>
<p>The Court itself, at page 764, expresses its own doubts, if not fears, of its own shadowy distinction between compelling "physical evidence" like blood which it holds does not amount to compelled self-incrimination, and "eliciting responses which are essentially testimonial." And in explanation of its fears the Court goes on to warn that</p>
<blockquote>"To compel a person to submit to testing [by lie detectors for example] in which an effort will be made to determine his guilt or innocence on the basis of physiological responses, whether willed or not, is to evoke the spirit and history of the Fifth Amendment. Such situations call to mind the principle that the protection of the privilege `is as broad as the mischief against which it seeks to guard.' <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span>."</blockquote>
<p>A basic error in the Court's holding and opinion is its failure to give the Fifth Amendment's protection against <span class="star-pagination">*776</span> compulsory self-incrimination the broad and liberal construction that <i><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span></i> and other opinions of this Court have declared it ought to have.</p>
<p>The liberal construction given the Bill of Rights' guarantee in <i>Boyd</i> v. <i>United States, supra</i><i>,</i> which Professor Wigmore criticized severely, see 8 Wigmore, Evidence, § 2264 (3d ed. 1940), pp. 366-373, makes that one among the greatest constitutional decisions of this Court. In that case, at 634-635, all the members of the Court decided that civil suits for penalties and forfeitures incurred for commission of offenses against the law,</p>
<blockquote>". . . are within the reason of criminal proceedings for all the purpose of . . . that portion of the Fifth Amendment which declares that no person shall be compelled in any criminal case to be a witness against himself; . . . within the meaning of the Fifth Amendment to the Constitution . . . ."<sup>[*]</sup></blockquote>
<p>Obviously the Court's interpretation was not completely supported by the literal language of the Fifth Amendment. Recognizing this, the Court announced a rule of constitutional interpretation that has been generally followed ever since, particularly in judicial construction of Bill of Rights guarantees:</p>
<blockquote>"A close and literal construction [of constitutional provisions for the security of persons and property] deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments <span class="star-pagination">*777</span> thereon." <i>Boyd</i> v. <i>United States, supra,</i> at 635.</blockquote>
<p>The Court went on to say, at 637, that to require "an owner to produce his private books and papers, in order to prove his breach of the laws, and thus to establish the forfeiture of his property, is surely compelling him to furnish evidence against himself." The Court today departs from the teachings of <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>.</i> Petitioner Schmerber has undoubtedly been compelled to give his blood "to furnish evidence against himself," yet the Court holds that this is not forbidden by the Fifth Amendment. With all deference I must say that the Court here gives the Bill of Rights' safeguard against compulsory self-incrimination a construction that would generally be considered too narrow and technical even in the interpretation of an ordinary commercial contract.</p>
<p>The Court apparently, for a reason I cannot understand, finds some comfort for its narrow construction of the Fifth Amendment in this Court's decision in <i>Miranda</i> v. <i>Arizona, ante,</i> p. 436. I find nothing whatever in the majority opinion in that case which either directly or indirectly supports the holding in this case. In fact I think the interpretive constitutional philosophy used in <i>Miranda,</i> unlike that used in this case, gives the Fifth Amendment's prohibition against compelled self-incrimination a broad and liberal construction in line with the wholesome admonitions in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case. The closing sentence in the Fifth Amendment section of the Court's opinion in the present case is enough by itself, I think, to expose the unsoundness of what the Court here holds. That sentence reads:</p>
<blockquote>"Since the blood test evidence, although an incriminating product of compulsion, was neither petitioner's testimony nor evidence relating to some communicative act or writing by the petitioner, it was not inadmissible on privilege grounds."</blockquote>
<p><span class="star-pagination">*778</span> How can it reasonably be doubted that the blood test evidence was not in all respects the actual equivalent of "testimony" taken from petitioner when the result of the test was offered as testimony, was considered by the jury as testimony, and the jury's verdict of guilt rests in part on that testimony? The refined, subtle reasoning and balancing process used here to narrow the scope of the Bill of Rights' safeguard against self-incrimination provides a handy instrument for further narrowing of that constitutional protection, as well as others, in the future. Believing with the Framers that these constitutional safeguards broadly construed by independent tribunals of justice provide our best hope for keeping our people free from governmental oppression, I deeply regret the Court's holding. For the foregoing reasons as well as those set out in concurring opinions of BLACK and DOUGLAS, JJ., in <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#174" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 174, 177</a></span>, and my concurring opinion in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 661</a></span>, and the dissenting opinions in <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#440" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 440, 442</a></span>, I dissent from the Court's holding and opinion in this case.</p>
<p>MR. JUSTICE DOUGLAS, dissenting.</p>
<p>I adhere to the views of THE CHIEF JUSTICE in his dissent in <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#440" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 440</a></span>, and to the views I stated in my dissent in that case (<span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#442" aria-description="Citation for case: Breithaupt v. Abram"><i>id.,</i> 442</a></span>) and add only a word.</p>
<p>We are dealing with the right of privacy which, since the <i><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">Breithaupt</a></span></i> case, we have held to be within the penumbra of some specific guarantees of the Bill of Rights. <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span>. Thus, the Fifth Amendment marks "a zone of privacy" which the Government may not force a person to surrender. <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/#484" aria-description="Citation for case: Griswold v. Connecticut"><i>Id.,</i> 484</a></span>. Likewise the Fourth Amendment recognizes that right when it guarantees the right of the people to be <span class="star-pagination">*779</span> secure "in their persons." <i><span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">Ibid.</a></span></i> No clearer invasion of this right of privacy can be imagined than forcible bloodletting of the kind involved here.</p>
<p>MR. JUSTICE FORTAS, dissenting.</p>
<p>I would reverse. In my view, petitioner's privilege against self-incrimination applies. I would add that, under the Due Process Clause, the State, in its role as prosecutor, has no right to extract blood from an accused or anyone else, over his protest. As prosecutor, the State has no right to commit any kind of violence upon the person, or to utilize the results of such a tort, and the extraction of blood, over protest, is an act of violence. Cf. CHIEF JUSTICE WARREN'S dissenting opinion in <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#440" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 440</a></span>.</p>
<h2>NOTES</h2>
<p>[1]  California Vehicle Code § 23102 (a) provides, in pertinent part, "It is unlawful for any person who is under the influence of intoxicating liquor . . . to drive a vehicle upon any highway. . . ." The offense is a misdemeanor.</p>
<p>[2]  Petitioner and a companion had been drinking at a tavern and bowling alley. There was evidence showing that petitioner was driving from the bowling alley about midnight November 12, 1964, when the car skidded, crossed the road and struck a tree. Both petitioner and his companion were injured and taken to a hospital for treatment.</p>
<p>[3]  This was the judgment of the highest court of the State in this proceeding since certification to the California District Court of Appeal was denied. See <i>Edwards</i> v. <i>California,</i> <span class="citation" data-id="9419178"><a href="/opinion/103557/edwards-v-california/" aria-description="Citation for case: Edwards v. California">314 U. S. 160</a></span>.</p>
<p>[4]  We "cannot see that it should make any difference whether one states unequivocally that he objects or resorts to physical violence in protest or is in such condition that he is unable to protest." <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#441" aria-description="Citation for case: Breithaupt v. Abram">352 U. S., at 441</a></span> (WARREN, C. J., dissenting). It would be a different case if the police initiated the violence, refused to respect a reasonable request to undergo a different form of testing, or responded to resistance with inappropriate force. Compare the discussion at Part IV, <i>infra.</i></p>
<p>[5]  A dissent suggests that the report of the blood test was "testimonial" or "communicative," because the test was performed in order to obtain the testimony of others, communicating to the jury facts about petitioner's condition. Of course, all evidence received in court is "testimonial" or "communicative" if these words are thus used. But the Fifth Amendment relates only to acts on the part of the person to whom the privilege applies, and we use these words subject to the same limitations. A nod or head-shake is as much a "testimonial" or "communicative" act in this sense as are spoken words. But the terms as we use them do not apply to evidence of acts noncommunicative in nature as to the person asserting the privilege, even though, as here, such acts are compelled to obtain the testimony of others.</p>
<p>[6]  Many state constitutions, including those of most of the original Colonies, phrase the privilege in terms of compelling a person to give "evidence" against himself. But our decision cannot turn on the Fifth Amendment's use of the word "witness." "[A]s the manifest purpose of the constitutional provisions, both of the States and of the United States, is to prohibit the compelling of testimony of a self-incriminating kind from a party or a witness, the liberal construction which must be placed upon constitutional provisions for the protection of personal rights would seem to require that the constitutional guaranties, however differently worded, should have as far as possible the same interpretation . . . ." <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#584" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 584-585</a></span>. 8 Wigmore, Evidence § 2252 (McNaughton rev. 1961).</p>
<p>[7]  Compare Wigmore's view, "that the privilege is limited to testimonial disclosures. It was directed at the employment of legal process to <i>extract from the person's own lips</i> an admission of guilt, which would thus take the place of other evidence." 8 Wigmore, Evidence § 2263 (McNaughton rev. 1961). California adopted the Wigmore formulation in <i>People</i> v. <i>Trujillo,</i> <span class="citation" data-id="9630742"><a href="/opinion/1440868/people-v-trujillo/" aria-description="Citation for case: People v. Trujillo">32 Cal. 2d 105</a></span>, <span class="citation" data-id="9630742"><a href="/opinion/1440868/people-v-trujillo/" aria-description="Citation for case: People v. Trujillo">194 P. 2d 681</a></span> (1948); with specific regard to blood tests, see <i>People</i> v. <i>Haeussler,</i> <span class="citation" data-id="9632176"><a href="/opinion/1447648/people-v-haeussler/" aria-description="Citation for case: People v. Haeussler">41 Cal. 2d 252</a></span>, <span class="citation" data-id="9632176"><a href="/opinion/1447648/people-v-haeussler/" aria-description="Citation for case: People v. Haeussler">260 P. 2d 8</a></span> (1953); <i>People</i> v. <i>Duroncelay,</i> <span class="citation" data-id="9563990"><a href="/opinion/1212162/people-v-duroncelay/" aria-description="Citation for case: People v. Duroncelay">48 Cal. 2d 766</a></span>, <span class="citation" data-id="9563990"><a href="/opinion/1212162/people-v-duroncelay/" aria-description="Citation for case: People v. Duroncelay">312 P. 2d 690</a></span> (1957). Our holding today, however, is not to be understood as adopting the Wigmore formulation.</p>
<p>[8]  The cases are collected in 8 Wigmore, Evidence § 2265 (McNaughton rev. 1961). See also <i>United States</i> v. <i>Chibbaro,</i> <span class="citation" data-id="8875889"><a href="/opinion/8889735/united-states-v-chibbaro/" aria-description="Citation for case: United States v. Chibbaro">361 F. 2d 365</a></span> (C. A. 3d Cir. 1966); <i>People</i> v. <i>Graves,</i> <span class="citation" data-id="9592244"><a href="/opinion/1347242/people-v-graves/" aria-description="Citation for case: People v. Graves">64 Cal. 2d 208</a></span>, , <span class="citation" data-id="9592244"><a href="/opinion/1347242/people-v-graves/#116" aria-description="Citation for case: People v. Graves">411 P. 2d 114, 116</a></span> (1966); Weintraub, Voice Identification, Writing Exemplars and the Privilege Against Self-Incrimination, <span class="citation no-link">10 Vand. L. Rev. 485</span> (1957).</p>
<p>[9]  This conclusion would not necessarily govern had the State tried to show that the accused had incriminated himself when told that he would have to be tested. Such incriminating evidence may be an unavoidable by-product of the compulsion to take the test, especially for an individual who fears the extraction or opposes it on religious grounds. If it wishes to compel persons to submit to such attempts to discover evidence, the State may have to forgo the advantage of any <i>testimonial</i> products of administering the testproducts which would fall within the privilege. Indeed, there may be circumstances in which the pain, danger, or severity of an operation would almost inevitably cause a person to prefer confession to undergoing the "search," and nothing we say today should be taken as establishing the permissibility of compulsion in that case. But no such situation is presented in this case. See text at n. 13 <i>infra.</i>
</p>
<p>Petitioner has raised a similar issue in this case, in connection with a police request that he submit to a "breathalyzer" test of air expelled from his lungs for alcohol content. He refused the request, and evidence of his refusal was admitted in evidence without objection.</p>
<p>He argues that the introduction of this evidence and a comment by the prosecutor in closing argument upon his refusal is ground for reversal under <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span>. We think general Fifth Amendment principles, rather than the particular holding of <i><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span>,</i> would be applicable in these circumstances, see <i>Miranda</i> v. <i>Arizona, ante,</i> at 468, n. 37. Since trial here was conducted after our decision in <i>Malloy</i> v. <i><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Hogan, supra</a></span></i><i>,</i> making those principles applicable to the States, we think petitioner's contention is foreclosed by his failure to object on this ground to the prosecutor's question and statements.</p>
<p>[10]  See, <i>e. g., </i><i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>; contra, <i>People</i> v. <i>Thayer,</i> <span class="citation" data-id="1421285"><a href="/opinion/1421285/people-v-thayer/" aria-description="Citation for case: People v. Thayer">63 Cal. 2d 635</a></span>, <span class="citation" data-id="1421285"><a href="/opinion/1421285/people-v-thayer/" aria-description="Citation for case: People v. Thayer">408 P. 2d 108</a></span> (1965); <i>State</i> v. <i>Bisaccia,</i> 45 N. J. 504, <span class="citation" data-id="1923442"><a href="/opinion/1923442/state-v-bisaccia/" aria-description="Citation for case: State v. Bisaccia">213 A. 2d 185</a></span> (1965); Note, Evidentiary Searches: The Rule and the Reason, 54 Geo. L. J. 593 (1966).</p>
<p>[11]  See, <i>e. g., </i><i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>; <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#235" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 235</a></span>; <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>.</p>
<p>[12]  California law authorizes a peace officer to arrest "without a warrant . . . [w]henever he has reasonable cause to believe that the person to be arrested has committed a felony, whether or not a felony has in fact been committed." <span class="citation no-link">Cal. Penal Code § 836.3</span>. Although petitioner was ultimately prosecuted for a misdemeanor, he was subject to prosecution for the felony since a companion in his car was injured in the accident, which apparently was the result of traffic law violations. <span class="citation no-link">Cal. Vehicle Code § 23101</span>. California's test of probable cause follows the federal standard. <i>People</i> v. <i>Cockrell,</i> <span class="citation" data-id="1421344"><a href="/opinion/1421344/people-v-cockrell/" aria-description="Citation for case: People v. Cockrell">63 Cal. 2d 659</a></span>, <span class="citation" data-id="1421344"><a href="/opinion/1421344/people-v-cockrell/" aria-description="Citation for case: People v. Cockrell">408 P. 2d 116</a></span> (1965).</p>
<p>[13]  "The blood test procedure has become routine in our everyday life. It is a ritual for those going into the military service as well as those applying for marriage licenses. Many colleges require such tests before permitting entrance and literally millions of us have voluntarily gone through the same, though a longer, routine in becoming blood donors." <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#436" aria-description="Citation for case: Breithaupt v. Abram">352 U. S., at 436</a></span>.</p>
<p>[14]  See Karst, Legislative Facts in Constitutional Litigation, <span class="citation no-link">1960 Sup. Ct. Rev. 75</span>, 82-83.</p>
<p>[*]  A majority of the Court applied the same constitutional interpretation to the search and seizure provisions of the Fourth Amendment over the dissent of Mr. Justice Miller, concurred in by Chief Justice Waite.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Schneckloth v. Bustamonte.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Schneckloth v. Bustamonte"
type: case
citation: "412 U.S. 218 (1973)"
parallel_cite: "93 S. Ct. 2041; 36 L. Ed. 2d 854"
neutral_cite: 1973 U.S. LEXIS 6
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-05-29
docket: 71-732
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Schneckloth v. Bustamonte
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108800/schneckloth-v-bustamonte/"
  cluster_id: 108800
  opinion_id: 108800
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Anchor"
related: ["[[Florida v. Bostick]]", "[[United States v. Drayton]]", "[[Georgia v. Randolph]]", "[[Florida v. Jimeno]]", "[[Illinois v. Rodriguez]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent-searches", "voluntariness", "totality-of-circumstances"]
holding: "The voluntariness of consent to search is a question of fact determined from the TOTALITY OF ALL THE CIRCUMSTANCES; the government need…"
lake:
  record_id: Schneckloth v. Bustamonte
  status: verified
  projected_at: 2026-07-06
---

# Schneckloth v. Bustamonte

*412 U.S. 218 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A police officer stopped a car for burned-out lights. When the driver could not produce a license, the officer asked a passenger — Joe Alcala, brother of the car's owner — for permission to search the car. Alcala said "Sure, go ahead," and helped open the trunk, where stolen checks were found. Bustamonte, another occupant, was convicted; he argued the consent was invalid because no one had been told of a right to refuse.

## Issue
Whether, to establish that consent to a search was voluntary, the State must prove that the person consenting knew he had a right to refuse.

## Rule
Voluntariness is judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and knowledge of the right to refuse is not required. "[T]he question whether a consent to a search was in fact 'voluntary' or was the product of duress or coercion, express or implied, is a question of fact to be determined from the totality of all the circumstances." — 412 U.S. at 227. ^pin-227

"While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the *sine qua non* of an effective consent." — *Id.* ^pin-227a

## Application
The consent to search the car was given by Alcala after a routine traffic stop, with several officers present but no evidence of coercion. Because voluntariness turns on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] and the State need not prove that Alcala knew he could refuse, his consent was voluntary on these facts, and the stolen checks discovered in the trunk were admissible.

## Conclusion
Consent voluntariness is determined from the totality of all the circumstances, without any requirement that the consenter be told of the right to refuse; the Court of Appeals' contrary rule was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Schneckloth* is the foundational consent-search voluntariness standard, applied in later consent cases such as [[Florida v. Bostick]] and [[United States v. Drayton]].

## Appears on
- [[Consent Searches]] — *Key — Anchor*

## Sources
- *Schneckloth v. Bustamonte*, 412 U.S. 218 (1973) — https://www.courtlistener.com/opinion/108800/schneckloth-v-bustamonte/ — pinpoint: 227.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "24eae06c73ec711c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Schneckloth v. Bustamonte"}, "payload": {"all": [{"cite": "412 U.S. 218", "page": "218", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "412"}, {"cite": "93 S. Ct. 2041", "page": "2041", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "36 L. Ed. 2d 854", "page": "854", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "36"}, {"cite": "1973 U.S. LEXIS 6", "page": "6", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1973"}], "display": "412 U.S. 218", "official": {"cite": "412 U.S. 218", "page": "218", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "412"}, "official_selection_present": true, "record_id": "Schneckloth v. Bustamonte"}}
{"assertion_id": "6c24b7ed5f9a238b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-227", "record_id": "Schneckloth v. Bustamonte"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-227", "pinpoint_status": "slip-only", "quote": "and helped open the trunk, where stolen checks were found. Bustamonte, another occupant, was convicted; he argued the consent was invalid because no one had been told of a right to refuse. ## Issue Whether, to establish that consent to a search was voluntary, the State must prove that the person consenting knew he had a right to refuse. ## Rule Voluntariness is judged on the totality of the circumstances, and knowledge of the right to refuse is not required.", "quote_fidelity": "mismatch", "record_id": "Schneckloth v. Bustamonte", "star_marker": null}}
{"assertion_id": "d6738626789a267a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-227a", "record_id": "Schneckloth v. Bustamonte"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-227a", "pinpoint_status": "slip-only", "quote": "While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the *sine qua non* of an effective consent.", "quote_fidelity": "mismatch", "record_id": "Schneckloth v. Bustamonte", "star_marker": null}}
{"assertion_id": "f7d781fe8541abf4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Schneckloth v. Bustamonte"}, "payload": {"as_of_content": "1973-05-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Schneckloth v. Bustamonte", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Schneckloth v. Bustamonte

```json
{
  "schema_version": "s2.v1",
  "record_id": "Schneckloth v. Bustamonte",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Schneckloth v. Bustamonte",
    "case_name_short": "Schneckloth",
    "case_name_full": "Schneckloth, Conservation Center Superintendent v. Bustamonte",
    "input_case_name": "Schneckloth v. Bustamonte",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-05-29",
    "year": 1973,
    "docket": "71-732",
    "cluster_id": 108800,
    "lead_opinion_id": 108800,
    "sibling_ids": [
      108800,
      9425314,
      9425315,
      9425316,
      9425317,
      9425318,
      9425319
    ],
    "absolute_url": "/opinion/108800/schneckloth-v-bustamonte/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "412 U.S. 218",
      "volume": "412",
      "reporter": "U.S.",
      "page": "218",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2041",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2041",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 L. Ed. 2d 854",
        "volume": "36",
        "reporter": "L. Ed. 2d",
        "page": "854",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 6",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "412 U.S. 218",
        "volume": "412",
        "reporter": "U.S.",
        "page": "218",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2041",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2041",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 L. Ed. 2d 854",
        "volume": "36",
        "reporter": "L. Ed. 2d",
        "page": "854",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 6",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "412 U.S. 218",
    "official_selection": {
      "court_class": "scotus",
      "selected": "412 U.S. 218",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-227",
      "page": null,
      "quote": "and helped open the trunk, where stolen checks were found. Bustamonte, another occupant, was convicted; he argued the consent was invalid because no one had been told of a right to refuse. ## Issue Whether, to establish that consent to a search was voluntary, the State must prove that the person consenting knew he had a right to refuse. ## Rule Voluntariness is judged on the totality of the circumstances, and knowledge of the right to refuse is not required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-227a",
      "page": null,
      "quote": "While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the *sine qua non* of an effective consent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Schneckloth v. Bustamonte",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 10658752,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane1_negative"
      },
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
        "journal_ref": "Schneckloth v. Bustamonte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Baez",
          "cluster_id": 10283156,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane1_negative"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teague v. Lane",
          "cluster_id": 112206,
          "cite": [
            "103 L. Ed. 2d 334",
            "109 S. Ct. 1060",
            "489 U.S. 288",
            "1989 U.S. LEXIS 1043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bounds v. Smith",
          "cluster_id": 109643,
          "cite": [
            "52 L. Ed. 2d 72",
            "97 S. Ct. 1491",
            "430 U.S. 817",
            "1977 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blackledge v. Allison",
          "cluster_id": 109648,
          "cite": [
            "52 L. Ed. 2d 136",
            "97 S. Ct. 1621",
            "431 U.S. 63",
            "1977 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Engle v. Isaac",
          "cluster_id": 110692,
          "cite": [
            "71 L. Ed. 2d 783",
            "102 S. Ct. 1558",
            "456 U.S. 107",
            "1982 U.S. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCleskey v. Zant",
          "cluster_id": 112573,
          "cite": [
            "113 L. Ed. 2d 517",
            "111 S. Ct. 1454",
            "499 U.S. 467",
            "1991 U.S. LEXIS 2218",
            "59 U.S.L.W. 4288",
            "91 Cal. Daily Op. Serv. 2680",
            "91 Daily Journal DAR 4340"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108800 OR 9425314 OR 9425315 OR 9425316 OR 9425317 OR 9425318 OR 9425319) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjc1MjA5NjAwMDAwJnM9OTM3MjI2NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108800+OR+9425314+OR+9425315+OR+9425316+OR+9425317+OR+9425318+OR+9425319%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108800 OR 9425314 OR 9425315 OR 9425316 OR 9425317 OR 9425318 OR 9425319)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDgxJnM9MTE4NDY4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108800+OR+9425314+OR+9425315+OR+9425316+OR+9425317+OR+9425318+OR+9425319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108800 OR 9425314 OR 9425315 OR 9425316 OR 9425317 OR 9425318 OR 9425319)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjk4NjI0MDAwMDAwJnM9OTQzODk5NCZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108800+OR+9425314+OR+9425315+OR+9425316+OR+9425317+OR+9425318+OR+9425319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108800 OR 9425314 OR 9425315 OR 9425316 OR 9425317 OR 9425318 OR 9425319)",
    "indexed_citing_opinions": 7588,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108800,
        "count": 6834,
        "count_source": "search"
      },
      {
        "opinion_id": 9425314,
        "count": 913,
        "count_source": "search"
      },
      {
        "opinion_id": 9425315,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425316,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425317,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425318,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425319,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 11786,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/schneckloth-v-bustamonte.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1NzQ0NjUmcz0xMDY5MjE3OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108800+OR+9425314+OR+9425315+OR+9425316+OR+9425317+OR+9425318+OR+9425319%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108800,
        "cited_id": 85668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 90687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 94093,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 96504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 98441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 102823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 102830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105306,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106721,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 227607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 252628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 258899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 259180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 265436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 267291,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 273438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 276566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 278364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 278813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 279301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 280244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 281169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 286049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 287694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 289231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 291168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 296899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 298163,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 299112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1100260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1140144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1149746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1165751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1207365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1222379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1297467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1607433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1687619,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1750377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1818084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 2112687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 2614149,
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
    "date_created": "2026-07-05T18:41:45Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:41:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:41:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:44:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:41:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Schneckloth v. Bustamonte (truncated)

```
<div>
<center><b><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218</a></span> (1973)</b></center>
<center><h1>SCHNECKLOTH, CONSERVATION CENTER SUPERINTENDENT<br>
v.<br>
BUSTAMONTE.</h1></center>
<center>No. 71-732.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 10, 1972.</center>
<center>Decided May 29, 1973.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><i>Robert R. Granucci,</i> Deputy Attorney General of California, argued the cause for petitioner. With him on the briefs were <i>Evelle J. Younger,</i> Attorney General, <i>Herbert L. Ashby,</i> Chief Assistant Attorney General, <i>Doris H. Maier,</i> Assistant Attorney General, and <i>Edward P. O'Brien,</i> Deputy Attorney General</p>
<p><i>Stuart P. Tobisman,</i> by appointment of the Court, <span class="star-pagination">*219</span> <span class="citation multiple-matches"><a href="/c/U.%20S./405/1062/">405 U. S. 1062</a></span>, argued the cause and filed a brief for respondent <i>pro hac vice.</i><sup>[*]</sup></p>
<p><i>Melvin L. Wulf, Sanford J. Rosen, Joel M. Gora, A. L. Wirin, Fred Okrand,</i> and <i>Lawrence R. Sperber</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.</p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>It is well settled under the Fourth and Fourteenth Amendments that a search conducted without a warrant issued upon probable cause is "<i>per se</i> unreasonable . . . subject only to a few specifically established and well-delineated exceptions." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span>; <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 51</a></span>. It is equally well settled that one of the specifically established exceptions to the requirements of both a warrant and probable cause is a search that is conducted pursuant to consent. <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#593" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 593-594</a></span>; <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#630" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 630</a></span>. The constitutional question in the present case concerns the definition of "consent" in this Fourth and Fourteenth Amendment context.</p>
<p></p>
<h2>I</h2>
<p>The respondent was brought to trial in a California court upon a charge of possessing a check with intent to defraud.<sup>[1]</sup> He moved to suppress the introduction of certain material as evidence against him on the ground that the material had been acquired through an unconstitutional search and seizure. In response to the motion, the trial judge conducted an evidentiary hearing <span class="star-pagination">*220</span> where it was established that the material in question had been acquired by the State under the following circumstances:</p>
<p>While on routine patrol in Sunnyvale, California, at approximately 2:40 in the morning, Police Officer James Rand stopped an automobile when he observed that one headlight and its license plate light were burned out. Six men were in the vehicle. Joe Alcala and the respondent, Robert Bustamonte, were in the front seat with Joe Gonzales, the driver. Three older men were seated in the rear. When, in response to the policeman's question, Gonzales could not produce a driver's license, Officer Rand asked if any of the other five had any evidence of identification. Only Alcala produced a license, and he explained that the car was his brother's. After the six occupants had stepped out of the car at the officer's request and after two additional policemen had arrived, Officer Rand asked Alcala if he could search the car. Alcala replied, "Sure, go ahead." Prior to the search no one was threatened with arrest and, according to Officer Rand's uncontradicted testimony, it "was all very congenial at this time." Gonzales testified that Alcala actually helped in the search of the car, by opening the trunk and glove compartment. In Gonzales' words: "[T]he police officer asked Joe [Alcala], he goes, `Does the trunk open?' And Joe said, `Yes.' He went to the car and got the keys and opened up the trunk." Wadded up under the left rear seat, the police officers found three checks that had previously been stolen from a car wash.</p>
<p>The trial judge denied the motion to suppress, and the checks in question were admitted in evidence at Bustamonte's trial. On the basis of this and other evidence he was convicted, and the California Court of Appeal for the First Appellate District affirmed the conviction. <span class="star-pagination">*221</span> <span class="citation" data-id="2198772"><a href="/opinion/2198772/people-v-bustamonte/" aria-description="Citation for case: People v. Bustamonte">270 Cal. App. 2d 648</a></span>, <span class="citation" data-id="2198772"><a href="/opinion/2198772/people-v-bustamonte/" aria-description="Citation for case: People v. Bustamonte">76 Cal. Rptr. 17</a></span>. In agreeing that the search and seizure were constitutionally valid, the appellate court applied the standard earlier formulated by the Supreme Court of California in an opinion by then Justice Traynor: "Whether in a particular case an apparent consent was in fact voluntarily given or was in submission to an express or implied assertion of authority, is a question of fact to be determined in the light of all the circumstances." <i>People</i> v. <i>Michael,</i> <span class="citation" data-id="1140144"><a href="/opinion/1140144/people-v-michael/#753" aria-description="Citation for case: People v. Michael">45 Cal. 2d 751, 753</a></span>, <span class="citation" data-id="1140144"><a href="/opinion/1140144/people-v-michael/#854" aria-description="Citation for case: People v. Michael">290 P. 2d 852, 854</a></span>. The appellate court found that "[i]n the instant case the prosecution met the necessary burden of showing consent . . . since there were clearly circumstances from which the trial court could ascertain that consent had been freely given without coercion or submission to authority. Not only officer Rand, but Gonzales, the driver of the automobile, testified that Alcala's assent to the search of his brother's automobile was freely, even casually given. At the time of the request to search the automobile the atmosphere, according to Rand, was `congenial' and there had been no discussion of any crime. As noted, Gonzales said Alcala even attempted to aid in the search." <span class="citation" data-id="2198772"><a href="/opinion/2198772/people-v-bustamonte/#652" aria-description="Citation for case: People v. Bustamonte">270 Cal. App. 2d, at 652</a></span>, <span class="citation" data-id="2198772"><a href="/opinion/2198772/people-v-bustamonte/#20" aria-description="Citation for case: People v. Bustamonte">76 Cal. Rptr., at 20</a></span>. The California Supreme Court denied review.<sup>[2]</sup></p>
<p>Thereafter, the respondent sought a writ of habeas corpus in a federal district court. It was denied.<sup>[3]</sup> On appeal, the Court of Appeals for the Ninth Circuit, relying on its prior decisions in <i>Cipres</i> v. <i>United States,</i> <span class="citation" data-id="267291"><a href="/opinion/267291/ramona-cipres-and-juan-montes-deoca-v-united-states/" aria-description="Citation for case: Ramona Cipres and Juan Montes Deoca v. United States">343 F. 2d 95</a></span>, and <i>Schoepflin</i> v. <i>United States,</i> <span class="citation" data-id="279301"><a href="/opinion/279301/emil-schoepflin-and-william-smith-v-united-states/" aria-description="Citation for case: Emil Schoepflin and William Smith v. United States">391 F. 2d 390</a></span>, set aside the District Court's order. <span class="citation" data-id="299112"><a href="/opinion/299112/robert-bustamonte-v-merle-r-schneckloth-superintendent-california/" aria-description="Citation for case: Robert Bustamonte v. Merle R. Schneckloth,...">448 F. 2d 699</a></span>. The appellate court reasoned that a consent was a waiver of a person's Fourth and Fourteenth Amendment rights, and that the State was under an obligation to demonstrate, <span class="star-pagination">*222</span> not only that the consent had been uncoerced, but that it had been given with an understanding that it could be freely and effectively withheld. Consent could not be found, the court held, solely from the absence of coercion and a verbal expression of assent. Since the District Court had not determined that Alcala had <i>known</i> that his consent could have been withheld and that he could have refused to have his vehicle searched, the Court of Appeals vacated the order denying the writ and remanded the case for further proceedings. We granted certiorari to determine whether the Fourth and Fourteenth Amendments require the showing thought necessary by the Court of Appeals. <span class="citation multiple-matches"><a href="/c/U.%20S./405/953/">405 U. S. 953</a></span>.</p>
<p></p>
<h2>II</h2>
<p>It is important to make it clear at the outset what is not involved in this case. The respondent concedes that a search conducted pursuant to a valid consent is constitutionally permissible. In <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#358" aria-description="Citation for case: Katz v. United States">389 U. S., at 358</a></span>, and more recently in <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#35" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 35</a></span>, we recognized that a search authorized by consent is wholly valid. See also <i>Davis</i> v. <i>United States,</i> 328 U. S., at 593-594; <i>Zap</i> v. <i>United States,</i> 328 U. S., at 630.<sup>[4]</sup> And similarly the State concedes that "[w]hen a prosecutor seeks to rely upon consent to justify the lawfulness of a search, he has the burden of proving that the consent was, in fact, freely and voluntarily given." <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 548</a></span>. See also <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>; <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>.</p>
<p><span class="star-pagination">*223</span> The precise question in this case, then, is what must the prosecution prove to demonstrate that a consent was "voluntarily" given. And upon that question there is a square conflict of views between the state and federal courts that have reviewed the search involved in the case before us. The Court of Appeals for the Ninth Circuit concluded that it is an essential part of the State's initial burden to prove that a person knows he has a right to refuse consent. The California courts have followed the rule that voluntariness is a question of fact to be determined from the totality of all the circumstances, and that the state of a defendant's knowledge is only one factor to be taken into account in assessing the voluntariness of a consent. See, <i>e. g., </i><i>People</i> v. <i>Tremayne,</i> <span class="citation" data-id="2112687"><a href="/opinion/2112687/people-v-tremayne/" aria-description="Citation for case: People v. Tremayne">20 Cal. App. 3d 1006</a></span>, <span class="citation" data-id="2112687"><a href="/opinion/2112687/people-v-tremayne/" aria-description="Citation for case: People v. Tremayne">98 Cal. Rptr. 193</a></span>; <i>People</i> v. <i>Roberts,</i> <span class="citation" data-id="2186736"><a href="/opinion/2186736/people-v-roberts/" aria-description="Citation for case: People v. Roberts">246 Cal. App. 2d 715</a></span>, <span class="citation" data-id="2186736"><a href="/opinion/2186736/people-v-roberts/" aria-description="Citation for case: People v. Roberts">55 Cal. Rptr. 62</a></span>.</p>
<p></p>
<h2>A</h2>
<p>The most extensive judicial exposition of the meaning of "voluntariness" has been developed in those cases in which the Court has had to determine the "voluntariness" of a defendant's confession for purposes of the Fourteenth Amendment. Almost 40 years ago, in <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>, the Court held that a criminal conviction based upon a confession obtained by brutality and violence was constitutionally invalid under the Due Process Clause of the Fourteenth Amendment. In some 30 different cases decided during the era that intervened between <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Brown</a></span></i> and <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, the Court was faced with the necessity of determining whether in fact the confessions in issue had been "voluntarily" given.<sup>[5]</sup> It is to that body <span class="star-pagination">*224</span> of case law to which we turn for initial guidance on the meaning of "voluntariness" in the present context.<sup>[6]</sup></p>
<p>Those cases yield no talismanic definition of "voluntariness," mechanically applicable to the host of situations where the question has arisen. "The notion of `voluntariness,' " Mr. Justice Frankfurter once wrote, "is itself an amphibian." <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#604" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 604-605</a></span>. It cannot be taken literally to mean a "knowing" choice. "Except where a person is unconscious or drugged or otherwise lacks capacity for conscious choice, all incriminating statementseven those made under brutal treatmentare `voluntary' in the sense of representing a choice of alternatives. On the other hand, if `voluntariness' incorporates notions of `but-for' cause, the question should be whether the statement would have been made even absent inquiry or other official action. Under such a test, virtually no statement would be voluntary because very few people give incriminating statements in the absence of official action of some kind."<sup>[7]</sup> It is thus evident that neither linguistics nor epistemology will provide a ready definition of the meaning of "voluntariness."</p>
<p>Rather, "voluntariness" has reflected an accommodation of the complex of values implicated in police questioning <span class="star-pagination">*225</span> of a suspect. At one end of the spectrum is the acknowledged need for police questioning as a tool for the effective enforcement of criminal laws. See <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#578" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 578-580</a></span>. Without such investigation, those who were innocent might be falsely accused, those who were guilty might wholly escape prosecution, and many crimes would go unsolved. In short, the security of all would be diminished. <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span>. At the other end of the spectrum is the set of values reflecting society's deeply felt belief that the criminal law cannot be used as an instrument of unfairness, and that the possibility of unfair and even brutal police tactics poses a real and serious threat to civilized notions of justice. "[I]n cases involving involuntary confessions, this Court enforces the strongly felt attitude of our society that important human values are sacrificed where an agency of the government, in the course of securing a conviction, wrings a confession out of an accused against his will." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206-207</a></span>. See also <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#581" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 581-584</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#235" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 235-238</a></span>.</p>
<p>This Court's decisions reflect a frank recognition that the Constitution requires the sacrifice of neither security nor liberty. The Due Process Clause does not mandate that the police forgo all questioning, or that they be given carte blanche to extract what they can from a suspect. "The ultimate test remains that which has been the only clearly established test in Anglo-American courts for two hundred years: the test of voluntariness. Is the confession the product of an essentially free and unconstrained choice by its maker? If it is, if he has willed to confess, it may be used against him. If it is not, if his will has been overborne and his capacity for self-determination critically impaired, the use of his <span class="star-pagination">*226</span> confession offends due process." <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#602" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 602</a></span>.</p>
<p>In determining whether a defendant's will was overborne in a particular case, the Court has assessed the totality of all the surrounding circumstancesboth the characteristics of the accused and the details of the interrogation. Some of the factors taken into account have included the youth of the accused, <i>e. g., </i><i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596</a></span>; his lack of education, <i>e. g., </i><i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>; or his low intelligence, <i>e. g., </i><i>Fikes</i> v. <i>Alabama,</i> <span class="citation" data-id="9421354"><a href="/opinion/105436/fikes-v-alabama/" aria-description="Citation for case: Fikes v. Alabama">352 U. S. 191</a></span>; the lack of any advice to the accused of his constitutional rights, <i>e. g., </i><i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span>; the length of detention, <i>e. g., </i><i>Chambers</i> v. <i><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">Florida, supra</a></span></i><i>;</i> the repeated and prolonged nature of the questioning, <i>e. g., </i><i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; and the use of physical punishment such as the deprivation of food or sleep, <i>e. g., </i><i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span>.<sup>[8]</sup> In all of these cases, the Court determined the factual circumstances surrounding the confession, assessed the psychological impact on the accused, and evaluated the legal significance of how the accused reacted. <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#603" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 603</a></span>.</p>
<p>The significant fact about all of these decisions is that none of them turned on the presence or absence of a single controlling criterion; each reflected a careful scrutiny of all the surrounding circumstances. See <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#508" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 508</a></span> (Harlan, J., dissenting); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#534" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 534-535</a></span> (WHITE, J., dissenting). In none of them did the Court rule that the Due Process Clause required the prosecution to prove as part of its <span class="star-pagination">*227</span> initial burden that the defendant knew he had a right to refuse to answer the questions that were put. While the state of the accused's mind, and the failure of the police to advise the accused of his rights, were certainly factors to be evaluated in assessing the "voluntariness" of an accused's responses, they were not in and of themselves determinative. See, <i>e. g., </i><i>Davis</i> v. <i>North Carolina, supra</i><i>; </i><i>Haynes</i> v. <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#510" aria-description="Citation for case: Haynes v. Washington"><i>Washington, supra,</i> at 510-511</a></span>; <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#610" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 610</a></span>; <i>Turner</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9420381"><a href="/opinion/104711/turner-v-pennsylvania/#64" aria-description="Citation for case: Turner v. Pennsylvania">338 U. S. 62, 64</a></span>.</p>
<p></p>
<h2>B</h2>
<p>Similar considerations lead us to agree with the courts of California that the question whether a consent to a search was in fact "voluntary" or was the product of duress or coercion, express or implied, is a question of fact to be determined from the totality of all the circumstances. While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the <i>sine qua non</i> of an effective consent. As with police questioning, two competing concerns must be accommodated in determining the meaning of a "voluntary" consentthe legitimate need for such searches and the equally important requirement of assuring the absence of coercion.</p>
<p>In situations where the police have some evidence of illicit activity, but lack probable cause to arrest or search, a search authorized by a valid consent may be the only means of obtaining important and reliable evidence.<sup>[9]</sup> In the present case for example, while the police had reason to stop the car for traffic violations, the State does not contend that there was probable cause to search the vehicle or that the search was incident to a valid arrest <span class="star-pagination">*228</span> of any of the occupants.<sup>[10]</sup> Yet, the search yielded tangible evidence that served as a basis for a prosecution, and provided some assurance that others, wholly innocent of the crime, were not mistakenly brought to trial. And in those cases where there is probable cause to arrest or search but where the police lack a warrant, a consent search may still be valuable. If the search is conducted and proves fruitless, that in itself may convince the police that an arrest with its possible stigma and embarrassment is unnecessary, or that a far more extensive search pursuant to a warrant is not justified. In short, a search pursuant to consent may result in considerably less inconvenience for the subject of the search, and properly conducted, is a constitutionally permissible and wholly legitimate aspect of effective police activity.</p>
<p>But the Fourth and Fourteenth Amendments require that a consent not be coerced, by explicit or implicit means, by implied threat or covert force. For, no matter how subtly the coercion was applied, the resulting "consent" would be no more than a pretext for the unjustified police intrusion against which the Fourth Amendment is directed. In the words of the classic admonition in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, 635:</p>
<blockquote>"It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close <span class="star-pagination">*229</span> and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon."</blockquote>
<p>The problem of reconciling the recognized legitimacy of consent searches with the requirement that they be free from any aspect of official coercion cannot be resolved by any infallible touchstone. To approve such searches without the most careful scrutiny would sanction the possibility of official coercion; to place artificial restrictions upon such searches would jeopardize their basic validity. Just as was true with confessions, the requirement of a "voluntary" consent reflects a fair accommodation of the constitutional requirements involved. In examining all the surrounding circumstances to determine if in fact the consent to search was coerced, account must be taken of subtly coercive police questions, as well as the possibly vulnerable subjective state of the person who consents. Those searches that are the product of police coercion can thus be filtered out without undermining the continuing validity of consent searches. In sum, there is no reason for us to depart in the area of consent searches, from the traditional definition of "voluntariness."</p>
<p>The approach of the Court of Appeals for the Ninth Circuit finds no support in any of our decisions that have attempted to define the meaning of "voluntariness." Its ruling, that the State must affirmatively prove that the subject of the search knew that he had a right to refuse consent, would, in practice, create serious doubt whether consent searches could continue to be conducted. There might be rare cases where it could be proved from the record that a person in fact affirmatively knew of his <span class="star-pagination">*230</span> right to refusesuch as a case where he announced to the police that if he didn't sign the consent form, "you [police] are going to get a search warrant;"<sup>[11]</sup> or a case where by prior experience and training a person had clearly and convincingly demonstrated such knowledge.<sup>[12]</sup> But more commonly where there was no evidence of any coercion, explicit or implicit, the prosecution would nevertheless be unable to demonstrate that the subject of the search in fact had known of his right to refuse consent.</p>
<p>The very object of the inquirythe nature of a person's subjective understandingunderlines the difficulty of the prosecution's burden under the rule applied by the Court of Appeals in this case. Any defendant who was the subject of a search authorized solely by his consent could effectively frustrate the introduction into evidence of the fruits of that search by simply failing to testify that he in fact knew he could refuse to consent. And the near impossibility of meeting this prosecutorial burden suggests why this Court has never accepted any such litmus-paper test of voluntariness. It is instructive to recall the fears of then Justice Traynor of the California Supreme Court:</p>
<blockquote>"[I]t is not unreasonable for officers to seek interviews with suspects or witnesses or to call upon them at their homes for such purposes. Such inquiries, although courteously made and not accompanied with any assertion of a right to enter or search or secure answers, would permit the criminal to defeat his prosecution by voluntarily revealing all of the evidence against him and then contending that he acted only in response to an implied assertion of <span class="star-pagination">*231</span> unlawful authority." <i>People</i> v. <i>Michael,</i> <span class="citation" data-id="1140144"><a href="/opinion/1140144/people-v-michael/#754" aria-description="Citation for case: People v. Michael">45 Cal. 2d, at 754</a></span>, <span class="citation" data-id="1140144"><a href="/opinion/1140144/people-v-michael/#854" aria-description="Citation for case: People v. Michael">290 P. 2d, at 854</a></span>.</blockquote>
<p>One alternative that would go far toward proving that the subject of a search did know he had a right to refuse consent would be to advise him of that right before eliciting his consent. That, however, is a suggestion that has been almost universally repudiated by both federal<sup>[13]</sup> and state courts,<sup>[14]</sup> and, we think, rightly so. For it would be thoroughly impractical to impose on the normal consent search the detailed requirements of an effective warning. Consent searches are part of the standard investigatory techniques of law enforcement <span class="star-pagination">*232</span> agencies. They normally occur on the highway, or in a person's home or office, and under informal and unstructured conditions. The circumstances that prompt the initial request to search may develop quickly or be a logical extension of investigative police questioning. The police may seek to investigate further suspicious circumstances or to follow up leads developed in questioning persons at the scene of a crime. These situations are a far cry from the structured atmosphere of a trial where, assisted by counsel if he chooses, a defendant is informed of his trial rights. Cf. <i>Boykin</i> v. <i>Alabama,</i> <span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/#243" aria-description="Citation for case: Boykin v. Alabama">395 U. S. 238, 243</a></span>. And, while surely a closer question, these situations are still immeasurably far removed from "custodial interrogation" where, in <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra</a></span></i><i>,</i> we found that the Constitution required certain now familiar warnings as a prerequisite to police interrogation. Indeed, in language applicable to the typical consent search, we refused to extend the need for warnings:</p>
<blockquote>"Our decision is not intended to hamper the traditional function of police officers in investigating crime. . . . When an individual is in custody on probable cause, the police may, of course, seek out evidence in the field to be used at trial against him. Such investigation may include inquiry of persons not under restraint. General on-the-scene questioning as to facts surrounding a crime or other general questioning of citizens in the fact-finding process is not affected by our holding. It is an act of responsible citizenship for individuals to give whatever information they may have to aid in law enforcement." 384 U. S., at 477-478.</blockquote>
<p>Consequently, we cannot accept the position of the Court of Appeals in this case that proof of knowledge of the right to refuse consent is a necessary prerequisite <span class="star-pagination">*233</span> to demonstrating a "voluntary" consent. Rather, it is only by analyzing all the circumstances of an individual consent that it can be ascertained whether in fact it was voluntary or coerced. It is this careful sifting of the unique facts and circumstances of each case that is evidenced in our prior decisions involving consent searches.</p>
<p>For example, in <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">328 U. S. 582</a></span>, federal agents enforcing wartime gasoline-rationing regulations, arrested a filling station operator and asked to see his rationing coupons. He eventually unlocked a room where the agents discovered the coupons that formed the basis for his conviction. The District Court found that the petitioner had consented to the searchthat although he had at first refused to turn the coupons over, he had soon been persuaded to do so and that force or threat of force had not been employed to persuade him. Concluding that it could not be said that this finding was erroneous, this Court, in an opinion by MR. JUSTICE DOUGLAS that looked to all the circumstances surrounding the consent, affirmed the judgment of conviction: "The public character of the property, the fact that the demand was made during business hours at the place of business where the coupons were required to be kept, the existence of the right to inspect, the nature of the request, the fact that the initial refusal to turn the coupons over was soon followed by acquiescence in the demandthese circumstances all support the conclusion of the District Court." <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#593" aria-description="Citation for case: Davis v. United States"><i>Id.,</i> at 593-594</a></span>. See also <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">328 U. S. 624</a></span>.</p>
<p>Conversely, if under all the circumstances it has appeared that the consent was not given voluntarilythat it was coerced by threats or force, or granted only in submission to a claim of lawful authoritythen we have found the consent invalid and the search unreasonable. See, <i>e. g., </i><i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S., at 548-549</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>; <i>Amos</i> v. <span class="star-pagination">*234</span> <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>. In <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span>,</i> a 66-year-old Negro widow, who lived in a house located in a rural area at the end of an isolated mile-long dirt road, allowed four white law enforcement officials to search her home after they asserted they had a warrant to search the house. We held the alleged consent to be invalid, noting that "[w]hen a law enforcement officer claims authority to search a home under a warrant, he announces in effect that the occupant has no right to resist the search. The situation is instinct with coercionalbeit colorably lawful coercion. Where there is coercion there cannot be consent." <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#550" aria-description="Citation for case: Bumper v. North Carolina">391 U. S., at 550</a></span>.</p>
<p>Implicit in all of these cases is the recognition that knowledge of a right to refuse is not a prerequisite of a voluntary consent. If the prosecution were required to demonstrate such knowledge, <i>Davis</i> and <i><span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">Zap</a></span></i> could not have found consent without evidence of that knowledge. And similarly if the failure to prove such knowledge were sufficient to show an ineffective consent, the <i>Amos, Johnson,</i> and <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span></i> opinions would surely have focused upon the subjective mental state of the person who consented. Yet they did not.</p>
<p>In short, neither this Court's prior cases, nor the traditional definition of "voluntariness" requires proof of knowledge of a right to refuse as the <i>sine qua non</i> of an effective consent to a search.<sup>[15]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*235</span> C</h2>
<p>It is said, however, that a "consent" is a "waiver" of a person's rights under the Fourth and Fourteenth Amendments. The argument is that by allowing the police to conduct a search, a person "waives" whatever right he had to prevent the police from searching. It is argued that under the doctrine of <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span>, to establish such a "waiver" the State must demonstrate "an intentional relinquishment or abandonment of a known right or privilege."</p>
<p>But these standards were enunciated in <i>Johnson</i> in the context of the safeguards of a fair criminal trial. Our cases do not reflect an uncritical demand for a knowing and intelligent waiver in every situation where a person has failed to invoke a constitutional protection. As Mr. Justice Black once observed for the Court: " `Waiver' is a vague term used for a great variety of purposes, good and bad, in the law." <i>Green</i> v. <i>United States,</i> <span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/#191" aria-description="Citation for case: Green v. United States">355 U. S. 184, 191</a></span>. With respect to procedural due process, for example, the Court has acknowledged that waiver is possible, while explicitly leaving open the question whether a "knowing and intelligent" waiver need be shown.<sup>[16]</sup> See <i>D. H. Overmyer Co.</i> v. <i>Frick Co.,</i> <span class="star-pagination">*236</span> <span class="citation" data-id="9424754"><a href="/opinion/108474/d-h-overmyer-co-inc-of-ohio-v-frick-co/#185" aria-description="Citation for case: D. H. Overmyer Co., Inc. of Ohio v. Frick Co.">405 U. S. 174, 185-186</a></span>; <i>Fuentes</i> v. <i>Shevin,</i> <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#94" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 94-96</a></span>.<sup>[17]</sup></p>
<p>The requirement of a "knowing" and "intelligent" waiver was articulated in a case involving the validity of a defendant's decision to forgo a right constitutionally guaranteed to protect a fair trial and the reliability of the truth-determining process. <i>Johnson</i> v. <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst, supra</a></span></i><i>,</i> dealt with the denial of counsel in a federal criminal trial. There the Court held that under the Sixth Amendment a criminal defendant is entitled to the assistance of counsel, and that if he lacks sufficient funds to retain counsel, it is the Government's obligation to furnish him with a lawyer. As Mr. Justice Black wrote for the Court: "The Sixth Amendment stands as a constant admonition that if the constitutional safeguards it provides be lost, justice will not `still be done.' It embodies a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself when brought before a tribunal with power to take his life or liberty, wherein the prosecution is presented by experienced and learned counsel. That which is simple, orderly and necessary to the lawyer, to the untrained layman may appear intricate, complex and mysterious." <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S., at 462-463</a></span> (footnote omitted). To preserve the fairness of the trial process the Court established an appropriately heavy burden on the Government before waiver could be found"an intentional <span class="star-pagination">*237</span> relinquishment or abandonment of a known right or privilege." <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><i>Id.,</i> at 464</a></span>.</p>
<p>Almost without exception, the requirement of a knowing and intelligent waiver has been applied only to those rights which the Constitution guarantees to a criminal defendant in order to preserve a fair trial.<sup>[18]</sup> Hence, and hardly surprisingly in view of the facts of <i>Johnson</i> itself, the standard of a knowing and intelligent waiver has most often been applied to test the validity of a waiver of counsel, either at trial.<sup>[19]</sup> or upon a guilty plea.<sup>[20]</sup> And the Court has also applied the <i>Johnson</i> criteria to assess the effectiveness of a waiver of other trial rights such as the right to confrontation,<sup>[21]</sup> to a jury trial,<sup>[22]</sup> and to a speedy trial,<sup>[23]</sup> and the right to be free from <span class="star-pagination">*238</span> twice being placed in jeopardy.<sup>[24]</sup> Guilty pleas have been carefully scrutinized to determine whether the accused knew and understood all the rights to which he would be entitled at trial, and that he had intentionally chosen to forgo them.<sup>[25]</sup> And the Court has evaluated the knowing and intelligent nature of the waiver of trial rights in trial-type situations, such as the waiver of the privilege against compulsory self-incrimination before an administrative agency<sup>[26]</sup> or a congressional committee,<sup>[27]</sup> or the waiver of counsel in a juvenile proceeding.<sup>[28]</sup></p>
<p>The guarantees afforded a criminal defendant at trial also protect him at certain stages before the actual trial, and any alleged waiver must meet the strict standard of an intentional relinquishment of a "known" right. But the "trial" guarantees that have been applied to the "pretrial" <span class="star-pagination">*239</span> stage of the criminal process are similarly designed to protect the fairness of the trial itself.</p>
<p>Hence, in <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>, and <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>, the Court held "that a post-indictment pretrial lineup at which the accused is exhibited to identifying witnesses is a critical stage of the criminal prosecution; that police conduct of such a lineup without notice to and in the absence of his counsel denies the accused his Sixth [and Fourteenth] Amendment right to counsel . . . ." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#272" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 272</a></span>. Accordingly, the Court indicated that the standard of a knowing and intelligent waiver must be applied to test the waiver of counsel at such a lineup. See <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#237" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 237</a></span>. The Court stressed the necessary interrelationship between the presence of counsel at a postindictment lineup before trial and the protection of the trial process itself:</p>
<blockquote>"Insofar as the accused's conviction may rest on a courtroom identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination which is an essential safeguard to his right to confront the witnesses against him. <i>Pointer</i> v. <i>Texas,</i> <span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span>. And even though cross-examination is a precious safeguard to a fair trial, it cannot be viewed as an absolute assurance of accuracy and reliability. Thus in the present context, where so many variables and pitfalls exist, the first line of defense must be the prevention of unfairness and the lessening of the hazards of eyewitness identification at the lineup itself. The trial which might determine the accused's fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused the <span class="star-pagination">*240</span> witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no effective appeal from the judgment there rendered by the witness`that's the man.' " <i>Id.,</i> at 235-236.</blockquote>
<p>And in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, the Court found that <i>custodial</i> interrogation by the police was inherently coercive, and consequently held that detailed warnings were required to protect the privilege against compulsory self-incrimination. The Court made it clear that the basis for decision was the need to protect the fairness of the trial itself:</p>
<blockquote>"That counsel is present when statements are taken from an individual during interrogation obviously enhances the integrity of the fact-finding processes in court. The presence of an attorney, and the warnings delivered to the individual, enable the defendant under otherwise compelling circumstances to tell his story without fear, effectively, and in a way that eliminates the evils in the interrogation process. Without the protections flowing from adequate warnings and the rights of counsel, `all the careful safeguards erected around the giving of testimony, whether by an accused or any other witness, would become empty formalities in a procedure where the most compelling possible evidence of guilt, a confession, would have already been obtained at the unsupervised pleasure of the police.' " <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#466" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 466</a></span>.</blockquote>
<p>The standards of <i>Johnson</i> were, therefore, found to be a necessary prerequisite to a finding of a valid waiver. See 384 U. S., at 475-479. Cf. <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S., at 490</a></span> n. 14.<sup>[29]</sup></p>
<p><span class="star-pagination">*241</span> There is a vast difference between those rights that protect a fair criminal trial and the rights guaranteed under the Fourth Amendment. Nothing, either in the purposes behind requiring a "knowing" and "intelligent" waiver of trial rights, or in the practical application of such a requirement suggests that it ought to be extended to the constitutional guarantee against unreasonable searches and seizures.</p>
<p>A strict standard of waiver has been applied to those rights guaranteed to a criminal defendant to insure that he will be accorded the greatest possible opportunity to utilize every facet of the constitutional model of a fair criminal trial. Any trial conducted in derogation of that model leaves open the possibility that the trial reached an unfair result precisely because all the protections specified in the Constitution were not provided. A prime example is the right to counsel. For without that right, a wholly innocent accused faces the real and substantial danger that simply because of his lack of legal expertise he may be convicted. As Mr. Justice Harlan once wrote: "The sound reason why [the right to counsel] is so freely extended for a criminal trial is the severe injustice risked by confronting an untrained defendant with a range of technical points of law, evidence, and tactics familiar to the prosecutor but not to <span class="star-pagination">*242</span> himself." <i>Miranda</i> v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#514" aria-description="Citation for case: Miranda v. Arizona"><i>Arizona, supra,</i> at 514</a></span> (dissenting opinion). The Constitution requires that every effort be made to see to it that a defendant in a criminal case has not unknowingly relinquished the basic protections that the Framers thought indispensable to a fair trial.<sup>[30]</sup></p>
<p>The protections of the Fourth Amendment are of a wholly different order, and have nothing whatever to do with promoting the fair ascertainment of truth at a criminal trial. Rather, as Mr. Justice Frankfurter's opinion for the Court put it in <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>, the Fourth Amendment protects the "security of one's privacy against arbitrary intrusion by the police . . . ." In declining to apply the exclusionary rule of <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, to convictions that had become final before rendition of that decision, the Court emphasized that "there is no likelihood of unreliability or coercion present in a search-and-seizure case," <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#638" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 638</a></span>. In <i><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span>,</i> the Court indicated that those cases that had been given retroactive effect went to "the fairness of the trialthe very integrity of the fact-finding process. Here . . . the fairness of the trial is not under attack." <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#639" aria-description="Citation for case: Linkletter v. Walker"><i>Id.,</i> at 639</a></span>. The Fourth Amendment "is not an adjunct to the ascertainment of truth." The guarantees of the Fourth Amendment stand "as a protection of quite different constitutional valuesvalues reflecting the concern of our society for the right of each individual to be let alone. To recognize this is no more than to accord those values undiluted respect." <i>Tehan</i> v. <i>United States ex rel. Shott,</i> <span class="citation" data-id="9423130"><a href="/opinion/107148/tehan-v-united-states-ex-rel-shott/#416" aria-description="Citation for case: Tehan v. United States Ex Rel. Shott">382 U. S. 406, 416</a></span>.</p>
<p>Nor can it even be said that a search, as opposed to an eventual trial, is somehow "unfair" if a person consents to a search. While the Fourth and Fourteenth <span class="star-pagination">*243</span> Amendments limit the circumstances under which the police can conduct a search, there is nothing constitutionally suspect in a person's voluntarily allowing a search. The actual conduct of the search may be precisely the same as if the police had obtained a warrant. And unlike those constitutional guarantees that protect a defendant at trial, it cannot be said every reasonable presumption ought to be indulged against voluntary relinquishment. We have only recently stated: "[I]t is no part of the policy underlying the Fourth and Fourteenth Amendments to discourage citizens from aiding to the utmost of their ability in the apprehension of criminals." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#488" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 488</a></span>. Rather, the community has a real interest in encouraging consent, for the resulting search may yield necessary evidence for the solution and prosecution of crime, evidence that may insure that a wholly innocent person is not wrongly charged with a criminal offense.</p>
<p>Those cases that have dealt with the application of the <i>Johnson</i> v. <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> rule make clear that it would be next to impossible to apply to a consent search the standard of "an intentional relinquishment or abandonment of a known right or privilege."<sup>[31]</sup> To be true to <i>Johnson</i> <span class="star-pagination">*244</span> and its progeny, there must be examination into the knowing and understanding nature of the waiver, an examination that was designed for a trial judge in the structured atmosphere of a courtroom. As the Court expressed it in <i>Johnson:</i></p>
<blockquote>"The constitutional right of an accused to be represented by counsel invokes, of itself, the protection of a trial court, in which the accusedwhose life or liberty is at stakeis without counsel. This protecting duty imposes the serious and weighty responsibility upon the trial judge of determining whether there is an intelligent and competent waiver by the accused. While an accused may waive the right to counsel, whether there is a proper waiver should be clearly determined by the trial court, and it would be fitting and appropriate for that determination to appear upon the record." <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#465" aria-description="Citation for case: Johnson v. Zerbst">304 U. S., at 465</a></span>.<sup>[32]</sup></blockquote>
<p><span class="star-pagination">*245</span> It would be unrealistic to expect that in the informal, unstructured context of a consent search, a policeman, upon pain of tainting the evidence obtained, could make the detailed type of examination demanded by <i>Johnson.</i> And, if for this reason a diluted form of "waiver" were found acceptable, that would itself be ample recognition of the fact that there is no universal standard that must be applied in every situation where a person forgoes a constitutional right.<sup>[33]</sup></p>
<p>Similarly, a "waiver" approach to consent searches would be thoroughly inconsistent with our decisions that have approved "third party consents." In <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 487-490</a></span>, where a wife surrendered to the police guns and clothing belonging to her husband, we found nothing constitutionally impermissible in the admission of that evidence at trial since the wife had not been coerced. <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#740" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 740</a></span>, held that evidence seized from the defendant's duffel bag in a search authorized by his cousin's consent was admissible at trial. We found that the defendant had assumed the risk that his cousin, with whom he shared the bag, would allow the police to search it. See also <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span>. And <span class="star-pagination">*246</span> in <i>Hill</i> v. <i>California,</i> <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#802" aria-description="Citation for case: Hill v. California">401 U. S. 797, 802-805</a></span>, we held that the police had validly seized evidence from the petitioner's apartment incident to the arrest of a third party, since the police had probable cause to arrest the petitioner and reasonably, though mistakenly, believed the man they had arrested was he. Yet it is inconceivable that the Constitution could countenance the waiver of a defendant's right to counsel by a third party, or that a waiver could be found because a trial judge reasonably, though mistakenly, believed a defendant had waived his right to plead not guilty.<sup>[34]</sup></p>
<p>In short, there is nothing in the purposes or application of the waiver requirements of <i>Johnson</i> v. <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> that justifies, much less compels, the easy equation of a knowing waiver with a consent search. To make such an equation is to generalize from the broad rhetoric of some of our decisions, and to ignore the substance of the differing constitutional guarantees. We decline to follow what one judicial scholar has termed "the domino method of constitutional adjudication . . . wherein every explanatory statement in a previous opinion is made the basis for extension to a wholly different situation."<sup>[35]</sup></p>
<p></p>
<h2>D</h2>
<p>Much of what has already been said disposes of the argument that the Court's decision in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case requires the conclusion that knowledge of a right to refuse is an indispensable element of a valid consent. The considerations that informed the Court's holding in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are simply inapplicable in the present case. <span class="star-pagination">*247</span> In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> the Court found that the techniques of police questioning and the nature of custodial surroundings produce an inherently coercive situation. The Court concluded that "[u]nless adequate protective devices are employed to dispel the compulsion inherent in custodial surroundings, no statement obtained from the defendant can truly be the product of his free choice." 384 U. S., at 458. And at another point the Court noted that "without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <i>Id.,</i> at 467.</p>
<p>In this case, there is no evidence of any inherently coercive tacticseither from the nature of the police questioning or the environment in which it took place. Indeed, since consent searches will normally occur on a person's own familiar territory, the specter of incommunicado police interrogation in some remote station house is simply inapposite.<sup>[36]</sup> There is no reason to believe, under circumstances such as are present here, that the response to a policeman's question is presumptively coerced; and there is, therefore, no reason to reject the traditional test for determining the voluntariness of a person's response. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> of course, did not reach investigative questioning of a person not in custody, which is most directly analogous to the situation of a consent search, and it assuredly did not indicate that such questioning ought to be deemed inherently coercive. See <i>supra,</i> at 232.</p>
<p>It is also argued that the failure to require the Government to establish knowledge as a prerequisite to a valid <span class="star-pagination">*248</span> consent, will relegate the Fourth Amendment to the special province of "the sophisticated, the knowledgeable and the privileged." We cannot agree. The traditional definition of voluntariness we accept today has always taken into account evidence of minimal schooling, low intelligence, and the lack of any effective warnings to a person of his rights; and the voluntariness of any statement taken under those conditions has been carefully scrutinized to determine whether it was in fact voluntarily given.<sup>[37]</sup></p>
<p></p>
<h2>E</h2>
<p>Our decision today is a narrow one. We hold only that when the subject of a search is not in custody and the State attempts to justify a search on the basis of his consent, the Fourth and Fourteenth Amendments require that it demonstrate that the consent was in fact voluntarily given, and not the result of duress or coercion, express or implied. Voluntariness is a question of fact <span class="star-pagination">*249</span> to be determined from all the circumstances, and while the subject's knowledge of a right to refuse is a factor to be taken into account, the prosecution is not required to demonstrate such knowledge as a prerequisite to establishing a voluntary consent.<sup>[38]</sup> Because the California court followed these principles in affirming the respondent's conviction, and because the Court of Appeals for the Ninth Circuit in remanding for an evidentiary hearing required more, its judgment must be reversed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I join the Court's opinion and its judgment.</p>
<p>At the time <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217</a></span> (1969), was decided, I, as a member of the Court of Appeals (but not of its panel) whose order was there reversed, found myself in agreement with the views expressed by Mr. Justice Harlan, writing for himself and my Brother STEWART in dissent. <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#242" aria-description="Citation for case: Kaufman v. United States"><i>Id.,</i> at 242</a></span>. My attitude has not changed in the four years that have passed since <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span></i> was decided.</p>
<p>Although I agree with nearly all that MR. JUSTICE POWELL has to say in his detailed and persuasive concurring opinion, <i>post,</i> p. 250, I refrain from joining it at this time because, as MR. JUSTICE STEWART'S opinion reveals, it is not necessary to reconsider <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span></i> in order to decide the present case.</p>
<p><span class="star-pagination">*250</span> MR. JUSTICE POWELL, with whom THE CHIEF JUSTICE and MR. JUSTICE REHNQUIST join, concurring.</p>
<p>While I join the opinion of the Court, it does not address what seems to me the overriding issue briefed and argued in this case: the extent to which federal habeas corpus should be available to a state prisoner seeking to exclude evidence from an allegedly unlawful search and seizure. I would hold that federal collateral review of a state prisoner's Fourth Amendment claimsclaims which rarely bear on innocenceshould be confined solely to the question of whether the petitioner was provided a fair opportunity to raise and have adjudicated the question in state courts. In view of the importance of this issue to our system of criminal justice, I think it appropriate to express my views.</p>
<p></p>
<h2>I</h2>
<p>Although petitions for federal habeas corpus assert a wide variety of constitutional questions, we are concerned in this case only with a Fourth Amendment claim that an unlawful search occurred and that the state court erred in failing to exclude the evidence obtained therefrom. A divided court in <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217</a></span> (1969), held that collateral review of search-and-seizure claims was appropriate on motions filed by federal prisoners under <span class="citation no-link">28 U. S. C. § 2255</span>. Until <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span>,</i> a substantial majority of the federal courts of appeals had considered that claims of unlawful search and seizure " `are not proper matters to be presented by a motion to vacate sentence under § 2255 . . . .' " <i>Id.,</i> at 220. The rationale of this view was fairly summarized by the Court:</p>
<blockquote>"The denial of Fourth Amendment protection against unreasonable searches and seizures, the Government's <span class="star-pagination">*251</span> argument runs, is of a different nature from denials of other constitutional rights which we have held subject to collateral attack by federal prisoners. For unlike a claim of denial of effective counsel or of violation of the privilege against self incrimination, as examples, a claim of illegal search and seizure does not impugn the integrity of the fact-finding process or challenge evidence as inherently unreliable; rather, the exclusion of illegally seized evidence is simply a prophylactic device intended generally to deter Fourth Amendment violations by law enforcement officers." <i>Id.,</i> at 224.</blockquote>
<p>In rejecting this rationale, the Court noted that under prior decisions "the federal habeas remedy extends to state prisoners alleging that unconstitutionally obtained evidence was admitted against them at trial,"<sup>[1]</sup> and concluded that there was no basis for restricting "access by federal prisoners with illegal search-and-seizure claims to federal collateral remedies, while placing no similar restriction on access by state prisoners." <i>Id.,</i> at 225-226. In short, on petition for habeas corpus or collateral review filed in a federal district court, whether by state prisoners under <span class="citation no-link">28 U. S. C. § 2254</span> or federal prisoners under § 2255, the present rule is that Fourth Amendment claims may be asserted and the exclusionary rule must be applied in precisely the same manner as on direct review. Neither the history or purpose of habeas corpus, the desired prophylactic utility of the exclusionary rule as applied to Fourth Amendment claims, nor any sound reason relevant to the administration of criminal justice in our federal system justifies such a power.</p>
<p></p>
<h2>
<span class="star-pagination">*252</span> II</h2>
<p>The federal review involved in this Fourth Amendment case goes well beyond the traditional purpose of the writ of habeas corpus. Much of the present perception of habeas corpus stems from a revisionist view of the historic function that writ was meant to perform. The critical historical argument has focused on the nature of the writ at the time of its incorporation in our Constitution and at the time of the Habeas Corpus Act of 1867, the direct ancestor of contemporary habeas corpus statutes.<sup>[2]</sup> In <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#426" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 426</a></span> (1963), the Court interpreted the writ's historic position as follows:</p>
<blockquote>"At the time the privilege of the writ was written into the Federal Constitution it was settled that the writ lay to test any restraint contrary to fundamental law, which in England stemmed ultimately from Magna Charta but in this country was embodied in the written Constitution. Congress in 1867 sought to provide a federal forum for state prisoners having constitutional defenses by extending the habeas corpus powers of the federal courts to their constitutional maximum. Obedient to this purpose, we have consistently held that federal court <span class="star-pagination">*253</span> jurisdiction is conferred by the allegation of an unconstitutional restraint and is not defeated by anything that may occur in the state court proceedings."</blockquote>
<p>If this were a correct interpretation of the relevant history, the present wide scope accorded the writ would have arguable support, despite the impressive reasons to the contrary. But recent scholarship has cast grave doubt on <i>Fay's</i> version of the writ's historic function.</p>
<p>It has been established that both the Framers of the Constitution and the authors of the 1867 Act expected that the scope of habeas corpus would be determined with reference to the writ's historic, common-law development.<sup>[3]</sup> Mr. Chief Justice Marshall early referred to the common-law conception of the writ in determining its constitutional and statutory scope, <i>Ex parte Bollman,</i> <span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/#93" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch 75, 93-94</a></span> (1807); <i>Ex parte Watkins,</i> <span class="citation" data-id="85668"><a href="/opinion/85668/ex-parte-tobias-watkins/#201" aria-description="Citation for case: Ex Parte Tobias Watkins">3 Pet. 193, 201-202</a></span> (1830), and Professor Oaks has noted that "when the 1867 Congress provided that persons restrained of their liberty in violation of the Constitution could obtain a writ of habeas corpus from a federal court, it undoubtedly intendedexcept to the extent the legislation provided otherwiseto incorporate the common-law uses and functions of this remedy."<sup>[4]</sup></p>
<p>It thus becomes important to understand exactly what was the common-law scope of the writ both when embraced by our Constitution and incorporated into the Habeas Corpus Act of 1867. Two respected scholars have recently explored precisely these questions.<sup>[5]</sup> Their efforts <span class="star-pagination">*254</span> have been both meticulous and revealing. Their conclusions differ significantly from those of the Court in <i>Fay</i> v. <i><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Noia</a></span></i><i>,</i> that habeas corpus traditionally has been available "to remedy any kind of governmental restraint contrary to fundamental law." <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#405" aria-description="Citation for case: Fay v. Noia">372 U. S., at 405</a></span>.</p>
<p>The considerable evidence marshaled by these scholars need not be restated here. Professor Oaks makes a convincing case that under the common law of habeas corpus at the time of the adoption of the Constitution, "once a person had been convicted by a superior court of general jurisdiction, a court disposing of a habeas corpus petition could not go behind the conviction for any purpose other than to verify the formal jurisdiction of the committing court."<sup>[6]</sup> Certainly that was what Mr. Chief Justice Marshall understood when he stated:</p>
<blockquote>"This writ [habeas corpus] is, as has been said, in the nature of a writ of error which brings up the body of the prisoner with the cause of commitment. The court can undoubtedly inquire into the sufficiency of that cause; but if it be the judgment of a court of competent jurisdiction, especially a judgment withdrawn by law from the revision of this court, is not that judgment in itself sufficient cause? Can the court, upon this writ, look beyond the judgment, and re-examine the charges on which it was rendered. A judgment, in its nature, concludes the subject on which it is rendered, and pronounces the law of the case. The judgment of a court of record whose jurisdiction is final, is as conclusive on all the world as the judgment of this court would be. It is as conclusive on this court as it is on other courts. It puts an end to inquiry concerning the fact, by deciding it." <i>Ex parte Watkins,</i> <span class="citation" data-id="85668"><a href="/opinion/85668/ex-parte-tobias-watkins/#202" aria-description="Citation for case: Ex Parte Tobias Watkins">3 Pet., at 202-203</a></span>.</blockquote>
<p><span class="star-pagination">*255</span> The respect shown under common law for the finality of the judgment of a committing court at the time of the Constitution and in the early 19th century did not, of course, explicitly contemplate the operation of habeas corpus in the context of federal-state relations. Federal habeas review for state prisoners was not available until passage of the Habeas Corpus Act of 1867. Yet there is no evidence that Congress intended that Act to jettison the respect theretofore shown by a reviewing court for prior judgments by a court of proper jurisdiction. The Act "received only the most perfunctory attention and consideration in the Congress; indeed, there were complaints that its effects could not be understood at all."<sup>[7]</sup> In fact, as Professor Bator notes, it would require overwhelming evidence, which simply is not present, to conclude that the 1867 Congress intended "to tear habeas corpus entirely out of the context of its historical meaning and scope and convert it into an ordinary writ of error with respect to all federal questions in all criminal cases."<sup>[8]</sup> Rather, the House Judiciary Committee when it reviewed the Act in 1884 understood that it was not "contemplated by its framers or . . . properly . . . construed to authorize the overthrow of the final judgments of the State courts of general jurisdiction, by the inferior Federal judges. . . ."<sup>[9]</sup></p>
<p>Much, of course, has transpired since that first Habeas Corpus Act. See <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#449" aria-description="Citation for case: Fay v. Noia">372 U. S., at 449-463</a></span> (Harlan, J., dissenting). The scope of federal habeas corpus for state prisoners has evolved from a quite limited inquiry into whether the committing state court had jurisdiction, <i>Andrews</i> v. <i>Swartz,</i> <span class="citation" data-id="94093"><a href="/opinion/94093/andrews-v-swartz/" aria-description="Citation for case: Andrews v. Swartz">156 U. S. 272</a></span> (1895); <i>In re</i> <span class="star-pagination">*256</span> <i>Moran,</i> <span class="citation" data-id="96504"><a href="/opinion/96504/matter-of-moran/" aria-description="Citation for case: Matter of Moran">203 U. S. 96</a></span> (1906), to whether the applicant had been given an adequate opportunity in state court to raise his constitutional claims, <i>Frank</i> v. <i>Mangum,</i> <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309</a></span> (1915); and finally to actual redetermination in federal court of state court rulings on a wide variety of constitutional contentions, <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span> (1953). No one would now suggest that this Court be imprisoned by every particular of habeas corpus as it existed in the late 18th and 19th centuries. But recognition of that reality does not liberate us from all historical restraint. The historical evidence demonstrates that the purposes of the writ, at the time of the adoption of the Constitution, were tempered by a due regard for the finality of the judgment of the committing court. This regard was maintained substantially intact when Congress, in the Habeas Corpus Act of 1867, first extended federal habeas review to the delicate interrelations of our dual court systems.</p>
<p></p>
<h2>III</h2>
<p>Recent decisions, however, have tended to depreciate the importance of the finality of prior judgments in criminal cases. <i>Kaufman,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#228" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 228</a></span>; <i>Sanders</i> v. <i>United States,</i> <span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/#8" aria-description="Citation for case: Sanders v. United States">373 U. S. 1, 8</a></span> (1963); <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#424" aria-description="Citation for case: Fay v. Noia"><i>Fay, supra,</i> at 424</a></span>. This trend may be a justifiable evolution of the use of habeas corpus where the one in state custody raises a constitutional claim bearing on his innocence. But the justification for disregarding the historic scope and function of the writ is measurably less apparent in the typical Fourth Amendment claim asserted on collateral attack. In this latter case, a convicted defendant is most often asking society to redetermine a matter with no bearing at all on the basic justice of his incarceration.</p>
<p>Habeas corpus indeed <i>should</i> provide the added assurance for a free society that no innocent man suffers an unconstitutional loss of liberty. The Court in <i><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Fay</a></span></i> described <span class="star-pagination">*257</span> habeas corpus as a remedy for "whatever society deems to be intolerable restraints," and recognized that those to whom the writ should be granted "are persons whom society has grievously wronged and for whom belated liberation is little enough compensation." <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#401" aria-description="Citation for case: Fay v. Noia"><i>Id.,</i> at 401-402, 441</a></span>. The Court there acknowledged that the central reason for the writ lay in remedying injustice to the individual. Recent commentators have recognized the same core concept, one noting that "where <i>personal liberty</i> is involved, a democratic society . . . insists that it is less important to reach an unshakable decision than to <i>do justice</i> (emphasis added),"<sup>[10]</sup> and another extolling the use of the writ in <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span> (1954), with the assertion that "[b]ut for federal habeas corpus, these two men would have gone to their deaths for crimes of which they were found not guilty."<sup>[11]</sup></p>
<p>I am aware that history reveals no exact tie of the writ of habeas corpus to a constitutional claim relating to innocence or guilt. Traditionally, the writ was unavailable even for many constitutional pleas grounded on a claimant's innocence, while many contemporary proponents of expanded employment of the writ would permit its issuance for one whose deserved confinement was never in doubt. We are now faced, however, with the task of accommodating the historic respect for the finality of the judgment of a committing court with recent Court expansions of the role of the writ. This accommodation can best be achieved, with due regard to all of the values implicated, by recourse to the central reason for habeas corpus: the affording of means, <span class="star-pagination">*258</span> through an extraordinary writ, of redressing an <i>unjust</i> incarceration.</p>
<p>Federal habeas review of search and seizure claims is rarely relevant to this reason. Prisoners raising Fourth Amendment claims collaterally usually are quite <i>justly</i> detained. The evidence obtained from searches and seizures is often "the clearest proof of guilt" with a very high content of reliability.<sup>[12]</sup> Rarely is there any contention that the search rendered the evidence unreliable or that its means cast doubt upon the prisoner's guilt. The words of Mr. Justice Black drive home the point:</p>
<blockquote>"A claim of illegal search and seizure under the Fourth Amendment is crucially different from many other constitutional rights; ordinarily the evidence seized can in no way have been rendered untrustworthy by the means of its seizure and indeed often this evidence alone establishes beyond virtually any shadow of a doubt that the defendant is guilty." <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#237" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 237</a></span> (1969) (dissenting opinion).</blockquote>
<p>Habeas corpus review of search and seizure claims thus brings a deficiency of our system of criminal justice into sharp focus: a convicted defendant asserting no constitutional claim bearing on innocence and relying solely on an alleged unlawful search, is now entitled to federal habeas review of state conviction and the likelihood of release if the reviewing court concludes that the search was unlawful. That federal courts would actually redetermine constitutional claims bearing no relation to the prisoner's innocence with the possibility of releasing him from custody if the search is held unlawful not only defeats our societal interest in a rational legal system but serves no compensating ends of personal justice.</p>
<p></p>
<h2>
<span class="star-pagination">*259</span> IV</h2>
<p>This unprecedented extension of habeas corpus far beyond its historic bounds and in disregard of the writ's central purpose is an anomaly in our system sought to be justified only by extrinsic reasons which will be addressed in Part V of this opinion. But first let us look at the costs of this anomalycosts in terms of serious intrusions on other societal values. It is these other values that have been subordinatednot to further justice on behalf of arguably innocent persons but all too often to serve mechanistic rules quite unrelated to justice in a particular case. Nor are these neglected values unimportant to justice in the broadest sense or to our system of Government. They include (i) the most effective utilization of limited judicial resources, (ii) the necessity of finality in criminal trials, (iii) the minimization of friction between our federal and state systems of justice, and (iv) the maintenance of the constitutional balance upon which the doctrine of federalism is founded.</p>
<p>When raised on federal habeas, a claim generally has been considered by two or more tiers of state courts. It is the solemn duty of these courts, no less than federal ones, to safeguard personal liberties and consider federal claims in accord with federal law. The task which federal courts are asked to perform on habeas is thus most often one that has or should have been done before. The presumption that "if a job can be well done once, it should not be done twice" is sound and one calculated to utilize best "the intellectual, moral, and political resources involved in the legal system."<sup>[13]</sup></p>
<p><span class="star-pagination">*260</span> Those resources are limited but demand on them constantly increases. There is an insistent call on federal courts both in civil actions, many novel and complex, which affect intimately the lives of great numbers of people and in original criminal trials and appeals which deserve our most careful attention.<sup>[14]</sup> To the extent the federal courts are required to re-examine claims on collateral <span class="star-pagination">*261</span> attack,<sup>[15]</sup> they deprive primary litigants of their prompt availability and mature reflection. After all, the resources of our system are finite: their overextension jeopardizes the care and quality essential to fair adjudication.</p>
<p>The present scope of federal habeas corpus also has worked to defeat the interest of society in a rational point of termination for criminal litigation. Professor Amsterdam has identified some of the finality interests at stake in collateral proceedings:</p>
<blockquote>"They involve (a) duplication of judicial effort; (b) delay in setting the criminal proceeding at rest; (c) inconvenience and possibly danger in transporting a prisoner to the sentencing court for hearing; (d) postponed litigation of fact, hence litigation which will often be less reliable in reproducing the facts (i) respecting the postconviction claim itself, and (ii) respecting the issue of guilt if the collateral attack succeeds in a form which allows retrial. . . ."</blockquote>
<p>He concluded that:</p>
<blockquote>"[I]n combination, these finality considerations amount to a more or less persuasive argument against the cognizability of any particular collateral <span class="star-pagination">*262</span> claim, the strength of the argument depending upon the nature of the claim, the manner of its treatment (if any) in the conviction-proceedings, and the circumstances under which collateral litigation must be had."<sup>[16]</sup></blockquote>
<p>No effective judicial system can afford to concede the continuing theoretical possibility that there is error in every trial and that every incarceration is unfounded. At some point the law must convey to those in custody that a wrong has been committed, that consequent punishment has been imposed, that one should no longer look back with the view to resurrecting every imaginable basis for further litigation but rather should look forward to rehabilitation and to becoming a constructive citizen.<sup>[17]</sup></p>
<p>Nowhere should the merit of this view be more self-evident than in collateral attack on an allegedly unlawful search and seizure, where the petitioner often asks society to <i>redetermine</i> a claim with no relationship at all to the justness of his confinement. Professor Amsterdam has noted that "for reasons which are common to all search and seizure claims," he "would hold even a slight finality interest sufficient to deny the collateral remedy."<sup>[18]</sup> But, in fact, a strong finality interest militates against allowing <span class="star-pagination">*263</span> collateral review of search-and-seizure claims. Apart from the duplication of resources inherent in most habeas corpus proceedings, the validity of a search-and-seizure claim frequently hinges on a complex matrix of events which may be difficult indeed for the habeas court to disinter especially where, as often happens, the trial occurred years before the collateral attack and the state record is thinly sketched.<sup>[19]</sup></p>
<p>Finally, the present scope of habeas corpus tends to undermine the values inherent in our federal system of government. To the extent that every state criminal judgment is to be subject indefinitely to broad and repetitive federal oversight, we render the actions of state courts a serious disrespect in derogation of the constitutional balance between the two systems.<sup>[20]</sup> The present expansive scope of federal habeas review has prompted no small friction between state and federal judiciaries. Justice Paul C. Reardon of the Massachusetts Supreme <span class="star-pagination">*264</span> Judicial Court and then President of the National Center for State Courts, in identifying problems between the two systems, noted bluntly that "[t]he first, without question, is the effect of Federal habeas corpus proceedings on State courts." He spoke of the "humiliation of review from the full bench of the highest State appellate court to a single United States District Court judge." Such broad federal habeas powers encourage in his view the "growing denigration of the State courts and their functions in the public mind."<sup>[21]</sup> In so speaking Justice Reardon echoed the words of Professor Bator:</p>
<blockquote>"I could imagine nothing more subversive of a judge's sense of responsibility, of the inner subjective conscientiousness which is so essential a part of the difficult and subtle art of judging well, than an indiscriminate <span class="star-pagination">*265</span> acceptance of the notion that all the shots will always be called by someone else."<sup>[22]</sup></blockquote>
<p>In my view, this Court has few more pressing responsibilities than to restore the mutual respect and the balanced sharing of responsibility between the state and federal courts which our tradition and the Constitution itself so wisely contemplate. This can be accomplished without retreat from our inherited insistence that the writ of habeas corpus retain its full vitality as a means of redressing injustice.</p>
<p>This case involves only a relatively narrow aspect of the appropriate reach of habeas corpus. The specific issue before us, and the only one that need be decided at this time, is the extent to which a state prisoner may obtain federal habeas corpus review of a Fourth Amendment claim. Whatever may be formulated as a more comprehensive answer to the important broader issues (whether by clarifying legislation or in subsequent decisions), Mr. Justice Black has suggested what seems to me to be the appropriate threshold requirement in a case of this kind:</p>
<blockquote>"I would always require that the convicted defendant raise the kind of constitutional claim that casts some shadow of a doubt on his guilt." <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#242" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 242</a></span> (dissenting opinion).</blockquote>
<p>In a perceptive analysis, Judge Henry J. Friendly expressed a similar view. He would draw the line against habeas corpus review in the absence of a "colorable claim of innocence":</p>
<blockquote>"[W]ith a few important exceptions, convictions should be subject to collateral attack only when <span class="star-pagination">*266</span> the prisoner supplements his constitutional plea with a colorable claim of innocence."<sup>[23]</sup></blockquote>
<p>Where there is no constitutional claim bearing on innocence, the inquiry of the federal court on habeas review of a state prisoner's Fourth Amendment claim should be confined solely to the question whether the defendant was provided a fair opportunity in the state courts to raise and have adjudicated the Fourth Amendment claim. Limiting the scope of habeas review in this manner would reduce the role of the federal courts in determining the merits of constitutional claims with no relation to a petitioner's innocence and contribute to the restoration of recently neglected values to their proper place in our criminal justice system.</p>
<p></p>
<h2>V</h2>
<p>The importance of the values referred to above is not questioned. What, then, is the reason which has prompted this Court in recent decisions to extend habeas corpus to Fourth Amendment claims largely in disregard of its history as well as these values? In addressing Mr. Justice Black's dissenting view that constitutional claims raised collaterally should be relevant to the petitioner's innocence, the majority in <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span></i> noted:</p>
<blockquote>"It [Mr. Justice Black's view] brings into question <i>the propriety of the exclusionary rule itself.</i> The application of that rule is not made to turn on the <span class="star-pagination">*267</span> existence of a possibility of innocence; rather, exclusion of illegally obtained evidence is deemed necessary to protect the right of all citizens, not merely the citizen on trial, to be secure against unreasonable searches and seizures." 394 U. S., at 229. (Emphasis added.)</blockquote>
<p>The exclusionary rule has occasioned much criticism, largely on grounds that its application permits guilty defendants to go free and law-breaking officers to go unpunished.<sup>[24]</sup> The oft-asserted reason for the rule is to deter illegal searches and seizures by the police, <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960); <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 656</a></span> (1961); <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#636" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 636</a></span> (1965); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 29</a></span> (1968).<sup>[25]</sup><span class="star-pagination">*268</span> The efficacy of this deterrent function, however, has been brought into serious question by recent empirical research. Whatever the rule's merits on an initial trial and appeal<sup>[26]</sup>a question not in issue herethe case for <span class="star-pagination">*269</span> collateral application of the rule is an anemic one. On collateral attack, the exclusionary rule retains its major liabilities while the asserted benefit of the rule dissolves. For whatever deterrent function the rule may serve when applied on trial and appeal becomes greatly attenuated when, months or years afterward, the claim surfaces for collateral review. The impermissible conduct has long since occurred, and the belated wrist slap of state police by federal courts harms no one but society on whom the convicted criminal is newly released.<sup>[27]</sup></p>
<p>Searches and seizures are an opaque area of the law: flagrant Fourth Amendment abuses will rarely escape detection but there is a vast twilight zone with respect to which one Justice has stated that our own "decisions . . . are hardly notable for their predictability,"<sup>[28]</sup> and another has observed that this Court was " `bifurcating elements too infinitesimal to be split.' "<sup>[29]</sup> Serious Fourth Amendment infractions can be dealt with by state judges or by this Court on direct review. But the nonfrivolous Fourth Amendment claims that survive for collateral attack are most likely to be in this grey, twilight area, where the law is difficult for courts to apply, let alone for the policeman on the beat to understand. This is <span class="star-pagination">*270</span> precisely the type of case where the deterrent function of the exclusionary rule is least efficacious, and where there is the least justification for freeing a duly convicted defendant.<sup>[30]</sup></p>
<p>Our decisions have not encouraged the thought that what may be an appropriate constitutional policy in one context automatically becomes such for all times and all seasons. In <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 629</a></span>, the Court recognized the compelling practical considerations against retroactive application of the exclusionary rule. Rather than viewing the rule as having eternal constitutional verity, the Court decided to</p>
<blockquote>"weigh the merits and demerits in each case by looking to the prior history of the rule in question, its purpose and effect, and whether retrospective operation will further or retard its operation. We believe that this approach is particularly correct with reference to the Fourth Amendment's prohibitions as to unreasonable searches and seizures." <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker"><i>Id.,</i> at 629</a></span>.</blockquote>
<p>Such a pragmatic approach compelled the Court to conclude that the rule's deterrent function would not be advanced by its retrospective application:</p>
<blockquote>"The misconduct of the police prior to <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> has already occurred and will not be corrected by releasing the prisoners involved. . . . Finally, the ruptured privacy of the victims' homes and effects cannot be restored. Reparation comes too late." <i>Id.,</i> at 637.</blockquote>
<p>See also <i>Desist</i> v. <i>United States,</i> <span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/" aria-description="Citation for case: Desist v. United States">394 U. S. 244</a></span> (1969).</p>
<p>The same practical, particularized analysis of the exclusionary rule's necessity also was evident in <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), when the Court permitted <span class="star-pagination">*271</span> the Government to utilize unlawfully seized evidence to impeach the credibility of a defendant who had first testified broadly in his own defense. The Court held, in effect, that the policies protected by the exclusionary rule were outweighed in this case by the need to prevent perjury and assure the integrity of proceedings at trial. The Court concluded that to apply the exclusionary rule in such circumstances "would be a perversion of the Fourth Amendment." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States"><i>Id.,</i> at 65</a></span>. The judgment in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> revealed most pointedly that the policies behind the exclusionary rule are neither absolute nor allencompassing, but rather must be weighed and balanced against a competing and more compelling policy, namely the need for effective determination of truth at trial.</p>
<p>In sum: the case for the exclusionary rule varies with the setting in which it is imposed. It makes little sense to extend the <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> exclusionary rule to a federal habeas proceeding where its asserted deterrent effect must be least efficacious, and its obvious harmful consequences persist in full force.</p>
<p></p>
<h2>VI</h2>
<p>The final inquiry is whether the above position conforms to <span class="citation no-link">28 U. S. C. § 2254</span> (a) which provides:</p>
<blockquote>"The Supreme Court, a Justice thereof, a circuit judge, or a district court shall entertain an application for a writ of habeas corpus in behalf of a person in custody pursuant to the judgment of a State court only on the ground that he is in custody in violation of the Constitution or laws or treaties of the United States."</blockquote>
<p>The trend in recent years has witnessed a proliferation of constitutional rights, "a vast expansion of the claims of error in criminal cases for which a resourceful defense lawyer can find a constitutional basis."<sup>[31]</sup> Federal habeas <span class="star-pagination">*272</span> jurisdiction has been extended far beyond anyone's expectation or intendment when the concept of "custody in violation of the Constitution," now in § 2254 (a), first appeared in federal law over a century ago.<sup>[32]</sup></p>
<p>Mr. Justice Black was clearly correct in noting that "not every conviction based in part on a denial of a constitutional right is subject to attack by habeas corpus or § 2255 proceedings after a conviction has become final." <i>Kaufman,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#232" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 232</a></span> (dissenting opinion). No evidence exists that Congress intended every allegation of a constitutional violation to afford an appropriate basis for collateral review: indeed, the latest revisions of the Federal Habeas Corpus statute in 1966<sup>[33]</sup> and the enactment of § 2254 (a) came at the time a majority of the courts of appeals held that claims of unlawful search and seizure " `are not proper matters to be presented by a motion to vacate sentence under § 2255 but can only be properly presented by appeal from the conviction.' " <i>Id.,</i> at 220, quoting <i>Warren</i> v. <i>United States,</i> <span class="citation" data-id="259180"><a href="/opinion/259180/alphonse-warren-v-united-states/#675" aria-description="Citation for case: Alphonse Warren v. United States">311 F. 2d 673, 675</a></span> (CA8 1963).<sup>[34]</sup> Though the precise discussion in <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span></i> concerned the claims of federal prisoners under § 2255, the then-existing principle of a distinction between review of search-and-seizure claims in direct and collateral proceedings clearly existed.</p>
<p>There is no indication that Congress intended to wipe out this distinction. Indeed, the broad purpose of the 1966 amendments pointed in the opposite direction. The report of the Senate Judiciary Committee notes that:</p>
<blockquote>"Although only a small number of these [habeas] applications have been found meritorious, the applications <span class="star-pagination">*273</span> in their totality have imposed a heavy burden on the Federal courts. . . . The bill seeks to alleviate the unnecessary burden by introducing a greater degree of finality of judgments in habeas corpus proceedings." S. Rep. No. 1797, 89th Cong., 2d Sess., 2 (1966).<sup>[35]</sup></blockquote>
<p>The House Report states similarly that:</p>
<blockquote>"While in only a small number of these applications have the petitioners been successful, they nevertheless have not only imposed an unnecessary burden on the work of the Federal courts but have also greatly interfered with the procedures and processes of the State courts by delaying, in many cases, the proper enforcement of their judgments." H. R. Rep. No. 1892, 89th Cong., 2d Sess., 5 (1966).</blockquote>
<p>This most recent congressional expression on the scope of federal habeas corpus reflected the sentiment, shared alike by judges and legislators, that the writ has overrun its historical banks to inundate the dockets of federal courts and denigrate the role of state courts. Though Congress did not address the precise question at hand, nothing in § 2254 (a), the state of the law at the time of its adoption, or the historical uses of the language "custody in violation of the Constitution" from which § 2254 (a) is derived,<sup>[36]</sup> compels a holding that rulings of state courts on claims of unlawful search and <span class="star-pagination">*274</span> seizure must be reviewed and redetermined in collateral proceedings.</p>
<p></p>
<h2>VII</h2>
<p>Perhaps no single development of the criminal law has had consequences so profound as the escalating use, over the past two decades, of federal habeas corpus to reopen and readjudicate state criminal judgments. I have commented in Part IV above on the far-reaching consequences: the burden on the system,<sup>[37]</sup> in terms of demands on the courts, prosecutors, defense attorneys, and other personnel and facilities; the absence of efficiency and finality in the criminal process, frustrating both the deterrent function of the law and the effectiveness of rehabilitation; the undue subordination of state courts, with the resulting exacerbation of state-federal relations; and the subtle erosion of the doctrine of federalism itself. Perhaps the single most disquieting consequence of openended habeas review is reflected in the prescience of Mr. Justice Jackson's warning that "[i]t must prejudice the occasional meritorious application to be buried in a flood of worthless ones."<sup>[38]</sup></p>
<p>If these consequences flowed from the safeguarding of constitutional claims of innocence they should, of course, be accepted as a tolerable price to pay for cherished standards of justice at the same time that efforts are pursued to find more rational procedures. Yet, as illustrated by the case before us today, the question on habeas corpus is <span class="star-pagination">*275</span> too rarely whether the prisoner was innocent of the crime for which he was convicted<sup>[39]</sup> and too frequently whether some evidence of undoubted probative value has been admitted in violation of an exclusionary rule ritualistically applied without due regard to whether it has the slightest likelihood of achieving its avowed prophylactic purpose.</p>
<p>It is this paradox of a system, which so often seems to subordinate substance to form, that increasingly provokes criticism and lack of confidence. Indeed, it is difficult to explain why a system of criminal justice deserves respect which allows repetitive reviews of convictions long since held to have been final at the end of the normal process of trial and appeal where the basis for re-examination is not even that the convicted defendant was innocent. There has been a halo about the "Great Writ" that no one would wish to dim. Yet one must wonder whether the stretching of its use far beyond any justifiable purpose will not in the end weaken rather than strengthen the writ's vitality.</p>
<p>MR. JUSTICE DOUGLAS, dissenting.</p>
<p>I agree with the Court of Appeals that "verbal assent" to a search is not enough, that the fact that consent was given to the search does not imply that the suspect knew that the alternative of a refusal existed. <span class="citation" data-id="299112"><a href="/opinion/299112/robert-bustamonte-v-merle-r-schneckloth-superintendent-california/#700" aria-description="Citation for case: Robert Bustamonte v. Merle R. Schneckloth,...">448 F. 2d 699, 700</a></span>. As that court stated:</p>
<blockquote>"[U]nder many circumstances a reasonable person might read an officer's `May I' as the courteous expression <span class="star-pagination">*276</span> of a demand backed by force of law." <span class="citation" data-id="299112"><a href="/opinion/299112/robert-bustamonte-v-merle-r-schneckloth-superintendent-california/#701" aria-description="Citation for case: Robert Bustamonte v. Merle R. Schneckloth,..."><i>Id.,</i> at 701</a></span>.</blockquote>
<p>A considerable constitutional guarantee rides on this narrow issue. At the time of the search there was no probable cause to believe that the car contained contraband or other unlawful articles. The car was stopped only because a headlight and the license plate light were burned out. The car belonged to Alcala's brother, from whom it was borrowed, and Alcala had a driver's license. Traffic citations were appropriately issued. The car was searched, the present record showing that Alcala consented. But whether Alcala knew he had the right to refuse, we do not know. All the Court of Appeals did was to remand the case to the District Court for a finding and if necessary, a hearing on that issue.</p>
<p>I would let the case go forward on that basis. The long, time-consuming contest in this Court might well wash out. At least we could be assured that, if it came back, we would not be rendering an advisory opinion. Had I voted to grant this petition, I would suggest we dismiss it as improvidently granted. But, being in the minority, I am bound by the Rule of Four.</p>
<p>MR. JUSTICE BRENNAN, dissenting.</p>
<p>The Fourth Amendment specifically guarantees "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . ." We have consistently held that governmental searches conducted pursuant to a validly obtained warrant or reasonably incident to a valid arrest do not violate this guarantee. Here, however, as the Court itself recognizes, no search warrant was obtained and the State does not even suggest "that there was probable cause to search the vehicle or that the search was incident to a valid arrest of any of the occupants." <i>Ante,</i> <span class="star-pagination">*277</span> at 227-228. As a result, the search of the vehicle can be justified solely on the ground that the owner's brother gave his consentthat is, that he waived his Fourth Amendment right "to be secure" against an otherwise "unreasonable" search. The Court holds today that an individual can effectively waive this right even though he is totally ignorant of the fact that, in the absence of his consent, such invasions of his privacy would be constitutionally prohibited. It wholly escapes me how our citizens can meaningfully be said to have waived something as precious as a constitutional guarantee without ever being aware of its existence. In my view, the Court's conclusion is supported neither by "linguistics." nor by "epistemology," nor, indeed, by "common sense." I respectfully dissent.</p>
<p>MR. JUSTICE MARSHALL, dissenting.</p>
<p>Several years ago, MR. JUSTICE STEWART reminded us that "[t]he Constitution guarantees . . . a society of free choice. Such a society presupposes the capacity of its members to choose." <i>Ginsberg</i> v. <i>New York,</i> <span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/#649" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629, 649</a></span> (1968) (concurring in result). I would have thought that the capacity to choose necessarily depends upon knowledge that there is a choice to be made. But today the Court reaches the curious result that one can choose to relinquish a constitutional right the right to be free of unreasonable searcheswithout knowing that he has the alternative of refusing to accede to a police request to search.<sup>[1]</sup> I cannot agree, and therefore dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*278</span> I</h2>
<p>I believe that the Court misstates the true issue in this case. That issue is not, as the Court suggests, whether the police overbore Alcala's will in eliciting his consent, but rather, whether a simple statement of assent to search, without more,<sup>[2]</sup> should be sufficient to permit the police to search and thus act as a relinquishment of Alcala's constitutional right to exclude the police.<sup>[3]</sup> This Court has always scrutinized with great care claims that a person has forgone the opportunity to assert constitutional rights. See, <i>e. g., </i><i>Fuentes</i> v. <i>Shevin,</i> <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972); <i>D. H. Overmyer Co.</i> v. <i>Frick Co.,</i> <span class="citation" data-id="9424754"><a href="/opinion/108474/d-h-overmyer-co-inc-of-ohio-v-frick-co/" aria-description="Citation for case: D. H. Overmyer Co., Inc. of Ohio v. Frick Co.">405 U. S. 174</a></span> (1972); <i>Boykin</i> v. <i>Alabama,</i> <span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/" aria-description="Citation for case: Boykin v. Alabama">395 U. S. 238</a></span> (1969); <i>Carnley</i> v. <i>Cochran,</i> <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506</a></span> (1962). I see no reason to give the claim that a person consented to a search any less rigorous scrutiny. Every case in this Court involving this kind of search has heretofore spoken <span class="star-pagination">*279</span> of consent as a waiver.<sup>[4]</sup> See <i>e. g., </i><i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#317" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 317</a></span> (1921); <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#628" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 628</a></span> (1946); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13</a></span> (1948).<sup>[5]</sup> Perhaps one skilled in linguistics <span class="star-pagination">*280</span> or epistemology can disregard those comments, but I find them hard to ignore.</p>
<p>To begin, it is important to understand that the opinion of the Court is misleading in its treatment of the issue here in three ways. First, it derives its criterion for determining when a verbal statement of assent to search operates as a relinquishment of a person's right to preclude entry from a justification of consent searches that is inconsistent with our treatment in earlier cases of exceptions to the requirements of the Fourth Amendment, and that is not responsive to the unique nature of the consent-search exception. Second, it applies a standard of voluntariness that was developed in a very different context, where the standard was based on policies different from those involved in this case. Third, it mischaracterizes our prior cases involving consent searches.</p>
<p></p>
<h2>A</h2>
<p>The Court assumes that the issue in this case is: what are the standards by which courts are to determine that consent is voluntarily given? It then imports into the law of search and seizure standards developed to decide entirely different questions about coerced confessions.<sup>[6]</sup></p>
<p>The Fifth Amendment, in terms, provides that no person "shall be compelled in any criminal case to be a witness against himself." Nor is the interest protected by the Due Process Clause of the Fourteenth Amendment any different. The inquiry in a case where a confession is challenged as having been elicited in an unconstitutional manner is, therefore, whether the behavior <span class="star-pagination">*281</span> of the police amounted to compulsion of the defendant.<sup>[7]</sup> Because of the nature of the right to be free of compulsion, it would be pointless to ask whether a defendant knew of it before he made a statement; no sane person would knowingly relinquish a right to be free of compulsion. Thus, the questions of compulsion and of violation of the right itself are inextricably intertwined. The cases involving coerced confessions, therefore, pass over the question of knowledge of that right as irrelevant, and turn directly to the question of compulsion.</p>
<p><i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), confirms this analysis. There the Court held that certain warnings must be given to suspects prior to their interrogation so that the inherently coercive nature of in-custody questioning would be diminished by the suspect's knowledge that he could remain silent. But, although those warnings, of course, convey information about various rights of the accused, the information is intended only to protect the suspect against acceding to the other coercive aspects of police interrogation. While we would not ordinarily think that a suspect could waive his right to be free of coercion, for example, we do permit suspects to waive the rights they are informed of by police warnings, on the belief that such information in itself sufficiently decreases the chance that a statement would be elicited by compulsion. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-

[...TRUNCATED 83133 of 203133 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Scott v. Harris.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "f52e917d4be7f446", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Scott v. Harris"}, "payload": {"all": [{"cite": "550 U.S. 372", "page": "372", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "550"}, {"cite": "127 S. Ct. 1769", "page": "1769", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "127"}, {"cite": "167 L. Ed. 2d 686", "page": "686", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "167"}, {"cite": "2007 U.S. LEXIS 4748", "page": "4748", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2007"}], "display": "550 U.S. 372", "official": {"cite": "550 U.S. 372", "page": "372", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "550"}, "official_selection_present": true, "record_id": "Scott v. Harris"}}
{"assertion_id": "e43c5029a74d513b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1777", "record_id": "Scott v. Harris"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1777", "pinpoint_status": "slip-only", "quote": "--- # Scott v. Harris *550 U.S. 372 (2007)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Deputy Timothy Scott ended a high-speed chase of Victor Harris—who had fled a traffic stop and reached roughly 85 m.p.h. on two-lane roads—by ramming the rear of Harris's car, causing a crash that left Harris a quadriplegic. A police video captured the pursuit. Harris sued under 42 U.S.C. § 1983 for excessive force; the lower courts denied Scott qualified immunity. ## Issue Whether an officer's ramming of a fleeing motorist's vehicle to terminate a dangerous high-speed chase is an unreasonable seizure under the Fourth Amendment, and whether the deadly-force preconditions of *Tennessee v. Garner* rigidly control that question. ## Rule The reasonableness of force is judged under the Fourth Amendment's objective-reasonableness standard, and *Garner* does not impose rigid preconditions.", "quote_fidelity": "mismatch", "record_id": "Scott v. Harris", "star_marker": null}}
{"assertion_id": "fd4843498e826c8d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1779", "record_id": "Scott v. Harris"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1779", "pinpoint_status": "slip-only", "quote": "was simply an application of the Fourth Amendment's 'reasonableness' test ... to the use of a particular type of force in a particular situation.", "quote_fidelity": "mismatch", "record_id": "Scott v. Harris", "star_marker": null}}
{"assertion_id": "edd8f66cbfa7468f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Scott v. Harris"}, "payload": {"as_of_content": "2007-04-30", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Scott v. Harris", "scope_note": "Reads Tennessee v. Garner as an application of Graham reasonableness, not a rigid test.", "varies_by_point": false}}
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
