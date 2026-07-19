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

## GROUP: content/cases/United States v. Cotterman.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Cotterman"
type: case
citation: "709 F.3d 952 (2013)"
parallel_cite: ""
neutral_cite: "2013 WL 856292; 2013 U.S. App. LEXIS 4731"
court: "U.S. Court of Appeals, 9th Circuit (en banc)"
court_level: coa
circuit: 9th
year: 2013
date_decided: 2013-03-08
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2013-03-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Cotterman
  varies_by_point: false
  scope_note: "Good law in-circuit; later clarified by United States v. Cano (reasonable suspicion = suspicion of digital contraband) and part of a circuit split with the 11th Cir. (Touset)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/854692/united-states-v-howard-cotterman/"
  cluster_id: 854692
  opinion_id: 854692
  identity_checked: false
homes:
  - page: "[[Border Searches]]"
    role: "Illustrates a circuit split"
related: ["[[United States v. Cano]]", "[[Riley v. California]]", "[[Carpenter v. United States]]"]
aliases: ["United States v. Howard Cotterman"]
tags: ["case", "fourth-amendment", "border-search", "digital-privacy"]
holding: "A forensic (comprehensive) examination of an electronic device seized at the border requires reasonable suspicion; it is the…"
lake:
  record_id: United States v. Cotterman
  status: under_review
  projected_at: 2026-07-06
---

# United States v. Cotterman

*709 F.3d 952 (9th Cir. 2013) (en banc)* · U.S. Court of Appeals, 9th Circuit (en banc) · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At the U.S.-Mexico border, agents flagged Cotterman based in part on a prior child-molestation conviction and conducted an initial manual review of his laptop, which turned up nothing. They then detained the laptop, shipped it roughly 170 miles to Tucson, and subjected it to a comprehensive forensic examination using software that recovered password-protected and deleted files — revealing child pornography. Cotterman moved to suppress.

## Issue
Whether a comprehensive forensic examination of an electronic device seized at the border requires reasonable suspicion, or whether it is a routine border search needing no suspicion.

## Rule
A forensic examination of a device requires reasonable suspicion, triggered by the search's intrusiveness rather than its location: "It is the comprehensive and intrusive nature of a forensic examination—not the location of the examination—that is the key factor triggering the requirement of reasonable suspicion here." — slip op., at 17. ^pin-op17

The [[Reading and Citing Cases#en-banc|en banc]] court accordingly held that the forensic examination of Cotterman's computer required a showing of reasonable suspicion — a modest requirement — distinguishing such a search from the routine, suspicionless manual inspection permitted at the border. (The follow-on examination was not an "extended border search," because the laptop never cleared customs.)

## Application
The forensic imaging and analysis of Cotterman's laptop — recovering hidden, encrypted, and deleted files and exposing the most intimate details of his digital life — was so comprehensive and intrusive that it required reasonable suspicion, regardless of being performed 170 miles inland. On the facts, the agents had reasonable suspicion (the prior conviction, a border-alert hit, and password-protected files), so the forensic search was reasonable and the child-pornography evidence was admissible; the suppression order was reversed.

## Conclusion
Forensic examination of a device seized at the border requires reasonable suspicion, which the agents had here; the suppression was reversed. The intrusiveness of a comprehensive forensic search — not where it occurs — is what triggers the reasonable-suspicion requirement.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.** Clarified by [[United States v. Cano]], which held that the "reasonable suspicion" *Cotterman* requires means suspicion that the device contains digital contraband and confined such searches to that purpose.
- *Cotterman* reflects the digital-privacy concerns later voiced by SCOTUS in [[Riley v. California]] and [[Carpenter v. United States]]; it anchors a circuit split — the Eleventh Circuit (*[[United States v. Touset]]*) requires no suspicion even for forensic border device searches.

## Appears on
- [[Border Searches]] — *Illustrates a circuit split*

## Sources
- *United States v. Cotterman*, 709 F.3d 952 (9th Cir. 2013) (en banc) — https://www.courtlistener.com/opinion/854692/united-states-v-howard-cotterman/ — pinpoint: slip op., at 17 (CL carries the slip opinion; cluster 854692).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "33229d0d6cc74ada", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "709 F.3d 952 (2013)", "court": "U.S. Court of Appeals, 9th Circuit (en banc)", "neutral_cite": "2013 WL 856292; 2013 U.S. App. LEXIS 4731", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Cotterman", "year": "2013"}}
{"assertion_id": "b1138187f1458c3b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A forensic (comprehensive) examination of an electronic device seized at the border requires reasonable suspicion; it is the…", "title": "United States v. Cotterman"}}
{"assertion_id": "c3be41032d30f309", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Illustrates a circuit split", "title": "United States v. Cotterman"}}
{"assertion_id": "2cb5bc869df9515e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Cotterman"}}
{"assertion_id": "fdf04ae1714c2575", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2013-03-08", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Cotterman", "field_i_validity": "good_law", "scope_note": "Good law in-circuit; later clarified by United States v. Cano (reasonable suspicion = suspicion of digital contraband) and part of a circuit split with the 11th Cir. (Touset).", "title": "United States v. Cotterman", "varies_by_point": "false"}}
```

### lake record — United States v. Cotterman

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Cotterman",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Howard Cotterman",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Howard Wesley COTTERMAN, Defendant-Appellee",
    "input_case_name": "United States v. Cotterman",
    "court": "U.S. Court of Appeals, 9th Circuit (en banc)",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2013-03-08",
    "year": 2013,
    "docket": null,
    "cluster_id": 854692,
    "lead_opinion_id": 854692,
    "sibling_ids": [
      854692,
      9505756,
      9505757,
      9505758
    ],
    "absolute_url": "/opinion/854692/united-states-v-howard-cotterman/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "709 F.3d 952",
      "volume": "709",
      "reporter": "F.3d",
      "page": "952",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2013 WL 856292",
        "volume": "2013",
        "reporter": "WL",
        "page": "856292",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. App. LEXIS 4731",
        "volume": "2013",
        "reporter": "U.S. App. LEXIS",
        "page": "4731",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "709 F.3d 952",
        "volume": "709",
        "reporter": "F.3d",
        "page": "952",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 856292",
        "volume": "2013",
        "reporter": "WL",
        "page": "856292",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. App. LEXIS 4731",
        "volume": "2013",
        "reporter": "U.S. App. LEXIS",
        "page": "4731",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "709 F.3d 952",
    "official_selection": {
      "court_class": "coa",
      "selected": "709 F.3d 952",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op17",
      "page": null,
      "quote": "--- # United States v. Cotterman *709 F.3d 952 (9th Cir. 2013) (en banc)* \u00b7 U.S. Court of Appeals, 9th Circuit (en banc) \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the U.S.-Mexico border, agents flagged Cotterman based in part on a prior child-molestation conviction and conducted an initial manual review of his laptop, which turned up nothing. They then detained the laptop, shipped it roughly 170 miles to Tucson, and subjected it to a comprehensive forensic examination using software that recovered password-protected and deleted files \u2014 revealing child pornography. Cotterman moved to suppress. ## Issue Whether a comprehensive forensic examination of an electronic device seized at the border requires reasonable suspicion, or whether it is a routine border search needing no suspicion. ## Rule A forensic examination of a device requires reasonable suspicion, triggered by the search's intrusiveness rather than its location:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-03-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Cotterman",
    "varies_by_point": false,
    "scope_note": "Good law in-circuit; later clarified by United States v. Cano (reasonable suspicion = suspicion of digital contraband) and part of a circuit split with the 11th Cir. (Touset).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charles Skaggs, Jr.",
          "cluster_id": 6247820,
          "cite": [
            "25 F.4th 494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Haitao Xiang",
          "cluster_id": 9397097,
          "cite": [
            "67 F.4th 895"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fischer v SSA",
          "cluster_id": 10699387,
          "cite": [
            "2014 DNH 227"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abidor v. Napolitano",
          "cluster_id": 8730636,
          "cite": [
            "990 F. Supp. 2d 260",
            "2013 WL 6912654"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kitzhaber",
          "cluster_id": 8442802,
          "cite": [
            "828 F.3d 1083",
            "2016 WL 3745541"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524074,
          "cite": [
            "103 F.4th 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramos",
          "cluster_id": 7320653,
          "cite": [
            "190 F. Supp. 3d 992",
            "2016 U.S. Dist. LEXIS 73571",
            "2016 WL 3552140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Caballero",
          "cluster_id": 7319742,
          "cite": [
            "178 F. Supp. 3d 1008",
            "2016 U.S. Dist. LEXIS 51132",
            "2016 WL 1546731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Phillips",
          "cluster_id": 7305585,
          "cite": [
            "9 F. Supp. 3d 1130",
            "2014 U.S. Dist. LEXIS 42294",
            "2014 WL 1275916"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lustig",
          "cluster_id": 7305087,
          "cite": [
            "3 F. Supp. 3d 808",
            "2014 WL 902502",
            "2014 U.S. Dist. LEXIS 31554"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Cano",
          "cluster_id": 4781994,
          "cite": [
            "973 F.3d 966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Javier Hernandez",
          "cluster_id": 10796167,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bejar-Guizar",
          "cluster_id": 10625883,
          "cite": [
            "142 F.4th 1188"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524075,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Molina-Isidoro",
          "cluster_id": 7326797,
          "cite": [
            "267 F. Supp. 3d 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cano",
          "cluster_id": 7323106,
          "cite": [
            "222 F. Supp. 3d 876",
            "2016 WL 6920449",
            "2016 U.S. Dist. LEXIS 163675"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Saffarinia",
          "cluster_id": 4695910,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(854692 OR 9505756 OR 9505757 OR 9505758) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      },
      "lane2_top_cited": {
        "query": "cites:(854692 OR 9505756 OR 9505757 OR 9505758)",
        "reviewed": 19,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 18,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(854692 OR 9505756 OR 9505757 OR 9505758)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(854692 OR 9505756 OR 9505757 OR 9505758)",
    "indexed_citing_opinions": 19,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 854692,
        "count": 8,
        "count_source": "search"
      },
      {
        "opinion_id": 9505756,
        "count": 11,
        "count_source": "search"
      },
      {
        "opinion_id": 9505757,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9505758,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 93,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-cotterman.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 19,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 854692,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 112037,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 112877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 145640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 145768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 148280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 183026,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 204312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 213651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 279144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 363605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 365925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 409244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 411245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 450644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 456285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 463360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 479793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 500701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 591454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 625692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 626454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 678602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 679542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 768288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 770213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 773999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 776460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 776810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 777177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 777268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 787918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 788746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 792062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 794720,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 795398,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 795859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1234252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1235958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1390224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1448376,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1448445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1458074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1589964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 2246387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 2538573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 2620876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 111635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 145640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 145768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 148280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 183026,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 204312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 213651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 363605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 409244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 411245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 456285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 479793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 500701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 591454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 625692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 678602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 679542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 770213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 773999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 777177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 777268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 787918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 792062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 795859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1234252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1235958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1390224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1448445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 9426823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 9430181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 112037,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 148280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 450644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 463360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 776460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 788746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 788904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 791557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 792062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 795398,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 1234252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 1448376,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 1448445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 2538573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 2620876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 3052128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 9248165,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 9434573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 112877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 183026,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 279144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 365925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 450644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 456285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 626454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 768288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 776460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 776810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 777176,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 788746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 794720,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 1234252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 1589964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 2246387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 3024820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 3037708,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T23:22:08Z",
    "date_modified": "2026-07-06T09:03:53Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:22:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:22:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:25:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:22:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Cotterman (truncated)

```
                     FOR PUBLICATION

     UNITED STATES COURT OF APPEALS
          FOR THE NINTH CIRCUIT

 UNITED STATES OF AMERICA ,                        No. 09-10139
                Plaintiff-Appellant,
                                                      D.C. No.
                      v.                           4:07-cr-01207-
                                                    RCC-CRP-1
 HOWARD WESLEY COTTERMAN ,
             Defendant-Appellee.                      OPINION

         Appeal from the United States District Court
                  for the District of Arizona
          Raner C. Collins, District Judge, Presiding

               Argued and Submitted En Banc
             June 19, 2012—Pasadena, California

                       Filed March 8, 2013

Before: Alex Kozinski, Chief Judge, Sidney R. Thomas, M.
Margaret McKeown, Kim McLane Wardlaw, Raymond C.
Fisher, Ronald M. Gould, Richard R. Clifton, Consuelo M.
   Callahan, Milan D. Smith, Jr., Mary H. Murguia, and
            Morgan Christen, Circuit Judges.1

              Opinion by Judge McKeown;
Partial Concurrence and Partial Dissent by Judge Callahan;
           Dissent by Judge Milan D. Smith, Jr.


 1
   Judge Betty B. Fletcher was a member of the en banc panel but passed
away after argument of the case. Judge W ardlaw was drawn as her
replacement.
2               UNITED STATES V . COTTERMAN

                           SUMMARY*


                           Criminal Law

    The en banc court reversed the district court’s order
suppressing evidence of child pornography obtained from a
forensic examination of the defendant’s laptop, which was
seized by agents at the U.S.-Mexico border in response to an
alert based in part on a prior conviction for child molestation.

     The en banc court explained that a border search of a
computer is not transformed into an “extended border search”
requiring particularized suspicion simply because the device
is transported and examined beyond the border. The en banc
court wrote that the fact that the forensic examination
occurred 170 miles away from the border did not heighten the
interference with the defendant’s privacy, and the extended
border search doctrine does not apply, in this case in which
the defendant’s computer never cleared customs and the
defendant never regained possession.

    The en banc court held that the forensic examination of
the defendant’s computer required a showing of reasonable
suspicion, a modest requirement in light of the Fourth
Amendment. The en banc court wrote that it is the
comprehensive and intrusive nature of forensic examination
– not the location of the examination – that is the key factor
triggering the requirement of reasonable suspicion here. The
en banc court wrote that the uniquely sensitive nature of data
on electronic devices, which often retain information far

  *
    This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
              UNITED STATES V . COTTERMAN                    3

beyond the perceived point of erasure, carries with it a
significant expectation of privacy and thus renders an
exhaustive exploratory search more intrusive than with other
forms of property.

    The en banc court held that the border agents had
reasonable suspicion to conduct an initial search at the border
(which turned up no incriminating material) and the forensic
examination. The en banc court wrote that the defendant’s
Treasury Enforcement Communication System alert, prior
child-related conviction, frequent travels, crossing from a
country known for sex tourism, and collection of electronic
equipment, plus the parameters of the Operation Angel Watch
program aimed at combating child sex tourism, taken
collectively, gave rise to reasonable suspicion of criminal
activity.

    The en banc court wrote that password protection of files,
which is ubiquitous among many law-abiding citizens, will
not in isolation give rise to reasonable suspicion, but that
password protection may be considered in the totality of the
circumstances where, as here, there are other indicia of
criminal activity. The en banc court wrote that the existence
of password-protected files is also relevant to assessing the
reasonableness of the scope and duration of the search of the
defendant’s computer.

    The en banc court concluded that the examination of the
defendant’s electronic devices was supported by reasonable
suspicion and that the scope and manner of the search were
reasonable under the Fourth Amendment.

    Concurring in part, dissenting in part, and concurring in
the judgment, Judge Callahan (with whom Judge Clifton
4              UNITED STATES V . COTTERMAN

joined and with whom Judge M. Smith joined as to all but
Part II.A) wrote that the majority’s new rule requiring
reasonable suspicion for any thorough search of electronic
devices entering the United States flouts more than a century
of Supreme Court precedent, is unworkable and unnecessary,
and will severely hamstring the government’s ability to
protect our borders.

     Judge M. Smith (with whom Judges Clifton and Callahan
joined with respect to Part I) dissented. Judge Smith wrote
that the majority’s decision to create a reasonable suspicion
requirement for some property searches at the border so
muddies current border search doctrine that border agents will
be left to divine on an ad hoc basis whether a property search
is sufficiently “comprehensive and intrusive” to require
suspicion, or sufficiently “unintrusive” to come within the
traditional border search exception. Judge Smith also wrote
that the majority’s determination that reasonable suspicion
exists under the exceedingly weak facts of this case
undermines the liberties of U.S. citizens generally – not just
at the border, and not just with regard to our digital data – but
on every street corner, in every vehicle, and wherever else we
rely on the doctrine of reasonable suspicion to safeguard our
legitimate privacy interests.
              UNITED STATES V . COTTERMAN                 5

                       COUNSEL

Dennis K. Burke, Christina M. Cabanillas, Carmen F. Corbin,
John S. Leonardo, John J. Tuchi, United States Attorney’s
Office for the District of Arizona, Tucson, Arizona, for
Appellant.

William J. Kirchner, Law Office of Nash & Kirchner, P.C.,
Tucson, Arizona, for Appellee.

David M. Porter, Malia N. Brink, National Association of
Criminal Defense Lawyers, Washington, D.C.; Michael Price,
Brennan Center for Justice, New York, New York; Hanni M.
Fakhoury, Electronic Frontier Foundation, San Francisco,
California, for Amicus Curiae National Association of
Criminal Defense Lawyers and Electronic Frontier
Foundation.

Christopher T. Handman, Mary Helen Wimberly, Hogan
Lovells US LLP, Washington, D.C.; Sharon Bradford
Franklin, The Constitution Project, Washington, D.C., for
Amicus Curiae The Constitution Project.


                        OPINION

McKEOWN, Circuit Judge:

    Every day more than a million people cross American
borders, from the physical borders with Mexico and Canada
to functional borders at airports such as Los Angeles (LAX),
Honolulu (HNL), New York (JFK, LGA), and Chicago
(ORD, MDW). As denizens of a digital world, they carry
with them laptop computers, iPhones, iPads, iPods, Kindles,
6             UNITED STATES V . COTTERMAN

Nooks, Surfaces, tablets, Blackberries, cell phones, digital
cameras, and more. These devices often contain private and
sensitive information ranging from personal, financial, and
medical data to corporate trade secrets. And, in the case of
Howard Cotterman, child pornography.

    Agents seized Cotterman’s laptop at the U.S.-Mexico
border in response to an alert based in part on a fifteen-year-
old conviction for child molestation. The initial search at the
border turned up no incriminating material. Only after
Cotterman’s laptop was shipped almost 170 miles away and
subjected to a comprehensive forensic examination were
images of child pornography discovered.

    This watershed case implicates both the scope of the
narrow border search exception to the Fourth Amendment’s
warrant requirement and privacy rights in commonly used
electronic devices. The question we confront “is what limits
there are upon this power of technology to shrink the realm
of guaranteed privacy.” Kyllo v. United States, 533 U.S. 27,
34 (2001). More specifically, we consider the reasonableness
of a computer search that began as a cursory review at the
border but transformed into a forensic examination of
Cotterman’s hard drive.

    Computer forensic examination is a powerful tool capable
of unlocking password-protected files, restoring deleted
material, and retrieving images viewed on web sites. But
while technology may have changed the expectation of
privacy to some degree, it has not eviscerated it, and certainly
not with respect to the gigabytes of data regularly maintained
as private and confidential on digital devices. Our Founders
were indeed prescient in specifically incorporating “papers”
within the Fourth Amendment’s guarantee of “[t]he right of
                UNITED STATES V . COTTERMAN                          7

the people to be secure in their persons, houses, papers, and
effects.” U.S. Const. amend. IV. The papers we create and
maintain not only in physical but also in digital form reflect
our most private thoughts and activities.

    Although courts have long recognized that border
searches constitute a “historically recognized exception to the
Fourth Amendment’s general principle that a warrant be
obtained,” United States v. Ramsey, 431 U.S. 606, 621
(1977), reasonableness remains the touchstone for a
warrantless search. Even at the border, we have rejected an
“anything goes” approach. See United States v. Seljan,
547 F.3d 993, 1000 (9th Cir. 2008) (en banc).

    Mindful of the heavy burden on law enforcement to
protect our borders juxtaposed with individual privacy
interests in data on portable digital devices, we conclude that,
under the circumstances here, reasonable suspicion was
required for the forensic examination of Cotterman’s laptop.
Because border agents had such a reasonable suspicion, we
reverse the district court’s order granting Cotterman’s motion
to suppress the evidence of child pornography obtained from
his laptop.

I. FACTUAL BACKGROUND AND PROCEDURAL HISTORY 2

    Howard Cotterman and his wife were driving home to the
United States from a vacation in Mexico on Friday morning,
April 6, 2007, when they reached the Lukeville, Arizona, Port
of Entry. During primary inspection by a border agent, the



  2
    The facts related here are drawn from the record of the evidentiary
hearing held before the magistrate judge.
8                UNITED STATES V . COTTERMAN

Treasury Enforcement Communication System (“TECS”)3
returned a hit for Cotterman. The TECS hit indicated that
Cotterman was a sex offender—he had a 1992 conviction for
two counts of use of a minor in sexual conduct, two counts of
lewd and lascivious conduct upon a child, and three counts of
child molestation—and that he was potentially involved in
child sex tourism. Because of the hit, Cotterman and his wife
were referred to secondary inspection, where they were
instructed to exit their vehicle and leave all their belongings
in the car. The border agents called the contact person listed
in the TECS entry and, following that conversation, believed
the hit to reflect Cotterman’s involvement “in some type of
child pornography.” The agents searched the vehicle and
retrieved two laptop computers and three digital cameras.
Officer Antonio Alvarado inspected the electronic devices
and found what appeared to be family and other personal
photos, along with several password-protected files.

     Border agents contacted Group Supervisor Craig Brisbine
at the Immigration and Customs Enforcement (“ICE”) office
in Sells, Arizona, and informed him about Cotterman’s entry
and the fact that he was a sex offender potentially involved in
child sex tourism. The Sells Duty Agent, Mina Riley, also
spoke with Officer Alvarado and then contacted the ICE
Pacific Field Intelligence Unit, the office listed on the TECS
hit, to get more information. That unit informed Riley that
the alert was part of Operation Angel Watch, which was
aimed at combating child sex tourism by identifying
registered sex offenders in California, particularly those who
travel frequently outside the United States. She was advised


    3
    The TECS is an investigative tool of the Department of Homeland
Security that keeps track of individuals entering and exiting the country
and of individuals involved in or suspected to be involved in crimes.
                  UNITED STATES V . COTTERMAN                 9

to review any media equipment, such as computers, cameras,
or other electronic devices, for potential evidence of child
pornography. Riley then spoke again to Alvarado, who told
her that he had been able to review some of the photographs
on the Cottermans’ computers but had encountered password-
protected files that he was unable to access.

    Agents Brisbine and Riley departed Sells for Lukeville at
about 1:30 p.m. and decided en route to detain the
Cottermans’ laptops for forensic examination. Upon their
arrival, they gave Cotterman and his wife Miranda warnings
and interviewed them separately. The interviews revealed
nothing incriminating. During the interview, Cotterman
offered to help the agents access his computer. The agents
declined the offer out of concern that Cotterman might be
able to delete files surreptitiously or that the laptop might be
“booby trapped.”

    The agents allowed the Cottermans to leave the border
crossing around 6 p.m., but retained the Cottermans’ laptops
and a digital camera.4 Agent Brisbine drove almost 170 miles
from Lukeville to the ICE office in Tucson, Arizona, where
he delivered both laptops and one of the three digital cameras
to ICE Senior Special Agent & Computer Forensic Examiner
John Owen. Agent Owen began his examination on Saturday,
the following day. He used a forensic program to copy the
hard drives of the electronic devices. He determined that the
digital camera did not contain any contraband and released
the camera that day to the Cottermans, who had traveled to
Tucson from Lukeville and planned to stay there a few days.
Agent Owen then used forensic software that often must run
for several hours to examine copies of the laptop hard drives.

 4
     The other two cameras were returned to the Cottermans.
10               UNITED STATES V . COTTERMAN

He began his personal examination of the laptops on Sunday.
That evening, Agent Owen found seventy-five images of
child pornography within the unallocated space of
Cotterman’s laptop.5

    Agent Owen contacted the Cottermans on Sunday evening
and told them he would need Howard Cotterman’s assistance
to access password-protected files he found on Cotterman’s
laptop. Cotterman agreed to provide the assistance the
following day, but never showed up. When Agent Brisbine
called again to request Cotterman’s help in accessing the
password-protected files, Cotterman responded that the
computer had multiple users and that he would need to check
with individuals at the company from which he had retired in
order to get the passwords. The agents had no further contact
with Cotterman, who boarded a flight to Mexico from Tucson
the next day, April 9, and then flew onward to Sydney,
Australia. On April 11, Agent Owen finally managed to open
twenty-three password-protected files on Cotterman’s laptop.
The files revealed approximately 378 images of child
pornography. The vast majority of the images were of the
same girl, approximately 7–10 years of age, taken over a two-
to three-year period. In many of the images, Cotterman was
sexually molesting the child. Over the next few months,
Agent Owen discovered hundreds more pornographic images,
stories, and videos depicting children.




 5
   “Unallocated space is space on a hard drive that contains deleted data,
usually emptied from the operating system’s trash or recycle bin folder,
that cannot be seen or accessed by the user without the use of forensic
software. Such space is available to be written over to store new
information.” United States v. Flyer, 633 F.3d 911, 918 (9th Cir. 2011).
              UNITED STATES V . COTTERMAN                    11

    A grand jury indicted Cotterman for a host of offenses
related to child pornography. Cotterman moved to suppress
the evidence gathered from his laptop and the fruits of that
evidence. The magistrate judge filed a Report and
Recommendation finding that the forensic examination was
an “extended border search” that required reasonable
suspicion. He found that the TECS hit and the existence of
password-protected files on Cotterman’s laptop were
suspicious, but concluded that those facts did not suffice to
give rise to reasonable suspicion of criminal activity. The
district judge adopted the Report and Recommendation and
granted Cotterman’s motion to suppress.

    In its interlocutory appeal of that order, the government
characterized the issue as follows: “Whether the authority to
search a laptop computer without reasonable suspicion at a
border point of entry permits law enforcement to take it to
another location to be forensically examined, when it has
remained in the continuous custody of the government.” A
divided panel of this court answered that question in the
affirmative and reversed. United States v. Cotterman,
637 F.3d 1068 (9th Cir. 2011). The panel concluded that
reasonable suspicion was not required for the search and that
“[t]he district court erred in suppressing the evidence lawfully
obtained under border search authority.” Id. at 1084. In
dissent, Judge Betty B. Fletcher wrote that “officers must
have some level of particularized suspicion in order to
conduct a seizure and search like the one at issue here.” Id.
(B. Fletcher, J., dissenting). By a vote of a majority of
nonrecused active judges, rehearing en banc was ordered.
673 F.3d 1206 (9th Cir. 2012). Following en banc oral
argument, we requested supplemental briefing on the issue of
whether reasonable suspicion existed at the time of the
search.
12            UNITED STATES V . COTTERMAN

II. WAIVER

    The government argued below that the forensic
examination was part of a routine border search not requiring
heightened suspicion and, alternatively, that reasonable
suspicion justified the search. Before the district court, the
government maintained “the facts of this case clearly
establish that there was reasonable suspicion.” However,
having failed to obtain a favorable ruling on that ground, the
government did not challenge on appeal the conclusion that
there was no reasonable suspicion. Rather, it sought a broad
ruling that no suspicion of any kind was required. Cotterman
thus argued in his answering brief that the government had
waived the issue—an assertion that the government did not
address in its reply brief. Cotterman contends that the
government has abandoned and conceded the issue of
reasonable suspicion and that this court may not address that
issue. We disagree.

    We review de novo the ultimate question of whether a
warrantless search was reasonable under the Fourth
Amendment. United States v. Johnson, 256 F.3d 895, 905
(9th Cir. 2001) (en banc).         Our review necessarily
encompasses a determination as to the applicable standard: no
suspicion, reasonable suspicion or probable cause. That the
government may hope for the lowest standard does not alter
our de novo review, particularly when the issue was fully
briefed and argued below. Further, we may consider an issue
that has not been adequately raised on appeal if such a failure
will not prejudice the opposing party. United States v. Ullah,
976 F.2d 509, 514 (9th Cir. 1992). Where, as here, we
“called for and received supplemental briefs by both parties,”
Alcarez v. INS, 384 F.3d 1150, 1161 (9th Cir. 2004), the
government’s failure to address the issue does not prejudice
               UNITED STATES V . COTTERMAN                     13

Cotterman. See also United States v. Resendiz-Ponce,
549 U.S. 102, 103–04 (2007).

III.    THE BORDER SEARCH

    The broad contours of the scope of searches at our
international borders are rooted in “the long-standing right of
the sovereign to protect itself by stopping and examining
persons and property crossing into this country.” Ramsey,
431 U.S. at 616. Thus, border searches form “a narrow
exception to the Fourth Amendment prohibition against
warrantless searches without probable cause.” Seljan,
547 F.3d at 999 (internal quotation marks and citation
omitted). Because “[t]he Government’s interest in preventing
the entry of unwanted persons and effects is at its zenith at the
international border,” United States v. Flores-Montano,
541 U.S. 149, 152 (2004), border searches are generally
deemed “reasonable simply by virtue of the fact that they
occur at the border.” Ramsey, 431 U.S. at 616.

    This does not mean, however, that at the border “anything
goes.” Seljan, 547 F.3d at 1000. Even at the border,
individual privacy rights are not abandoned but “[b]alanced
against the sovereign’s interests.” United States v. Montoya
de Hernandez, 473 U.S. 531, 539 (1985). That balance “is
qualitatively different . . . than in the interior” and is “struck
much more favorably to the Government.” Id. at 538, 540.
Nonetheless, the touchstone of the Fourth Amendment
analysis remains reasonableness.            Id. at 538.        The
reasonableness of a search or seizure depends on the totality
of the circumstances, including the scope and duration of the
deprivation. See United States v. Jacobsen, 466 U.S. 109,
124 (1984); see also United States v. Duncan, 693 F.2d 971,
977 (9th Cir. 1982).
14               UNITED STATES V . COTTERMAN

    In view of these principles, the legitimacy of the initial
search of Cotterman’s electronic devices at the border is not
in doubt. Officer Alvarado turned on the devices and opened
and viewed image files while the Cottermans waited to enter
the country. It was, in principle, akin to the search in Seljan,
where we concluded that a suspicionless cursory scan of a
package in international transit was not unreasonable.
547 F.3d at 1004. Similarly, we have approved a quick look
and unintrusive search of laptops. United States v. Arnold,
533 F.3d 1003, 1009 (9th Cir. 2008) (holding border search
reasonable where “CBP officers simply ‘had [traveler] boot
[the laptop] up, and looked at what [he] had inside.’”) (second
alteration in original).6 Had the search of Cotterman’s laptop
ended with Officer Alvarado, we would be inclined to
conclude it was reasonable even without particularized
suspicion. See id. But the search here transformed into
something far different. The difficult question we confront is
the reasonableness, without a warrant, of the forensic
examination that comprehensively analyzed the hard drive of
the computer.

     A. The Forensic Examination Was Not An Extended
        Border Search

    Cotterman urges us to treat the examination as an
extended border search that requires particularized suspicion.

 6
   Although the Arnold decision expressed its conclusion in broad terms,
stating that, “reasonable suspicion is not needed for customs officials to
search a laptop or other personal electronic storage devices at the border,”
Arnold, 533 F.3d at 1008, the facts do not support such an unbounded
holding. As an en banc court, we narrow Arnold to approve only the
relatively simple search at issue in that case, not to countenance
suspicionless forensic examinations. The dissent’s extensive reliance on
Arnold is misplaced in the en banc environment.
              UNITED STATES V . COTTERMAN                    15

Although the semantic moniker “extended border search”
may at first blush seem applicable here, our jurisprudence
does not support such a claim. We have “define[d] an
extended border search as any search away from the border
where entry is not apparent, but where the dual requirements
of reasonable certainty of a recent border crossing and
reasonable suspicion of criminal activity are satisfied.”
United States v. Guzman-Padilla, 573 F.3d 865, 878–79 (9th
Cir. 2009) (internal quotation marks and citations omitted).
The key feature of an extended border search is that an
individual can be assumed to have cleared the border and thus
regained an expectation of privacy in accompanying
belongings. See United States v. Abbouchi, 502 F.3d 850,
855 (9th Cir. 2007) (“Because the delayed nature of an
extended border search . . . necessarily entails a greater level
of intrusion on legitimate expectations of privacy than an
ordinary border search, the government must justify an
extended border search with reasonable suspicion that the
search may uncover contraband or evidence of criminal
activity.”) (internal quotation marks omitted) (emphasis
added).

    Cotterman’s case is different. Cotterman was stopped and
searched at the border. Although he was allowed to depart
the border inspection station after the initial search, some of
his belongings, including his laptop, were not. The follow-on
forensic examination was not an “extended border search.”
A border search of a computer is not transformed into an
extended border search simply because the device is
transported and examined beyond the border.

    To be sure, our case law has not always articulated the
“extended border search” doctrine with optimal clarity. But
the confusion has come in distinguishing between facts
16               UNITED STATES V . COTTERMAN

describing a functional border search and those describing an
extended border search, not in defining the standard for a
search at the border. See, e.g., United States v. Cardona,
769 F.2d 625, 628 (9th Cir. 1985) (“We have recently
recognized the difficulty of making sharp distinctions
between searches at the functional equivalent of the border
and extended border searches.”). The “functional equivalent”
doctrine effectively extends the border search doctrine to all
ports of entry, including airports. See Almeida-Sanchez v.
United States, 413 U.S. 266, 273 (1973). A routine customs
search at the “functional equivalent” of the border is
“analyzed as a border search” and requires neither probable
cause nor reasonable suspicion. Seljan, 547 F.3d at 999.
This case involves a search initiated at the actual border and
does not encounter any of the difficulties surrounding
identification of a “functional” border. As to the extended
border search doctrine, we believe it is best confined to cases
in which, after an apparent border crossing or functional
entry, an attenuation in the time or the location of conducting
a search reflects that the subject has regained an expectation
of privacy.7

    In his dissent, Judge Smith advocates applying the
extended border search doctrine because the forensic
examination occurred 170 miles from the border and days
after Cotterman’s entry. Moving the laptop to a specialized

 7
   This characterization is consistent with how our circuit and others have
articulated the doctrine. See, e.g., United States v. Villasenor, 608 F.3d
467, 471–72 (9th Cir. 2010); United States v. Yang, 286 F.3d 940, 945–46
(7th Cir. 2002); United States v. Hyde, 37 F.3d 116, 120 n.2 (3d Cir.
1994); United States v. Santiago, 837 F.2d 1545, 1548 (11th Cir. 1988);
United States v. Gaviria, 805 F.2d 1108, 1112 (2d Cir. 1986); United
States v. Niver, 689 F.2d 520, 526 (5th Cir. 1982); United States v. Bilir,
592 F.2d 735, 739–40 (4th Cir. 1979).
                 UNITED STATES V . COTTERMAN                         17

lab at a distant location might highlight that the search
undertaken there was an extensive one, but it is not the
dispositive factor here. Because Cotterman never regained
possession of his laptop, the fact that the forensic
examination occurred away from the border, in Tucson, did
not heighten the interference with his privacy. Time and
distance become relevant to determining whether there is an
adequate nexus to a recent border crossing only after the
subject or items searched have entered. See Villasenor,
608 F.3d at 471 (explaining that reasonableness of extended
border search depends on “whether the totality of the
surrounding circumstances, including the time and distance
elapsed” establish that items to be searched have recently
entered the country) (internal quotation marks omitted).
Cotterman’s computer never cleared customs so entry was
never effected. In short, the extended border search doctrine
does not fit the search here.

     B. Forensic Examination At The Border Requires
        Reasonable Suspicion

    It is the comprehensive and intrusive nature of a forensic
examination—not the location of the examination—that is the
key factor triggering the requirement of reasonable suspicion
here.8 See Cotterman, 637 F.3d at 1086–87 n.6 (B. Fletcher,
J., dissenting) (recognizing that “[a] computer search in a
forensic lab will always be equivalent to an identical search
at the border. The duration of a computer search is not


 8
   The concurrence goes to great lengths to “refute any such notion” that
location and duration contributed to our holding reasonable suspicion
required here. Concurrence at 40–43. W e see no reason for such an
exegesis; our opinion is clear on the point that these factors are not at
issue.
18               UNITED STATES V . COTTERMAN

controlled by where the search is conducted. The duration of
a computer search is controlled by what one is looking for
and how one goes about searching for it.”) (emphasis in
original). The search would have been every bit as intrusive
had Agent Owen traveled to the border with his forensic
equipment. Indeed, Agent Owen had a laptop with forensic
software that he could have used to conduct an examination
at the port of entry itself, although he testified it would have
been a more time-consuming effort. To carry out the
examination of Cotterman’s laptop, Agent Owen used
computer forensic software to copy the hard drive and then
analyze it in its entirety, including data that ostensibly had
been deleted. This painstaking analysis is akin to reading a
diary line by line looking for mention of criminal
activity—plus looking at everything the writer may have
erased.9

    Notwithstanding a traveler’s diminished expectation of
privacy at the border, the search is still measured against the
Fourth Amendment’s reasonableness requirement, which
considers the nature and scope of the search. Significantly,
the Supreme Court has recognized that the “dignity and
privacy interests of the person being searched” at the border
will on occasion demand “some level of suspicion in the case
of highly intrusive searches of the person.” Flores-Montano,
541 U.S. at 152. Likewise, the Court has explained that
“some searches of property are so destructive,” “particularly
offensive,” or overly intrusive in the manner in which they


 9
   Agent Owen used a software program called EnCase that exhibited the
distinctive features of computer forensic examination. The program
copied, analyzed, and preserved the data stored on the hard drive and gave
the examiner access to far more data, including password-protected,
hidden or encrypted, and deleted files, than a manual user could access.
              UNITED STATES V . COTTERMAN                   19

are carried out as to require particularized suspicion. Id. at
152, 154 n.2, 155–56; Montoya de Hernandez, 473 U.S. at
541. The Court has never defined the precise dimensions of
a reasonable border search, instead pointing to the necessity
of a case-by-case analysis. As we have emphasized,
“[r]easonableness, when used in the context of a border
search, is incapable of comprehensive definition or of
mechanical application.” Duncan, 693 F.2d at 977 (internal
quotation marks and citation omitted).

    Over the past 30-plus years, the Supreme Court has dealt
with a handful of border cases in which it reaffirmed the
border search exception while, at the same time, leaving open
the question of when a “particularly offensive” search might
fail the reasonableness test. The trail begins with United
States v. Ramsey, where the Court reserved judgment on this
question: “We do not decide whether, and under what
circumstances, a border search might be deemed
‘unreasonable’ because of the particularly offensive manner
in which it is carried out.” 431 U.S. at 618 n.13. Of note, the
Court cited two cases, albeit non-border cases, as examples:
Kremen v. United States, 353 U.S. 346, 347–48 (1957)
(holding unconstitutional an exhaustive warrantless search of
a cabin and seizure of its entire contents that were moved 200
miles away for examination) and Go-Bart Importing Co. v.
United States, 282 U.S. 344, 358 (1931) (condemning as
“lawless invasion of the premises and a general exploratory
search” a warrantless “unlimited search, ransacking the desk,
safe, filing cases and other parts of [an] office”).

    Less than ten years later, in 1985, the Court observed that
it had “not previously decided what level of suspicion would
justify a seizure of an incoming traveler for purposes other
than a routine border search” and then went on to hold in the
20            UNITED STATES V . COTTERMAN

context of an alimentary canal search that reasonable
suspicion was required for “the detention of a traveler at the
border, beyond the scope of a routine customs search and
inspection.” Montoya de Hernandez, 473 U.S. at 540–41.
The Court’s reference to “routine border search” was parsed
in a later case, Flores-Montano, where the Court explained
that “the reasons that might support a requirement of some
level of suspicion in the case of highly intrusive searches of
the person—dignity and privacy interests of the person being
searched—simply do not carry over to vehicles,” and, more
specifically, to the gas tank of a car. 541 U.S. at 152.
Accordingly, the Court rejected a privacy claim vis-a-vis an
automobile gas tank.

    We are now presented with a case directly implicating
substantial personal privacy interests.           The private
information individuals store on digital devices—their
personal “papers” in the words of the Constitution—stands in
stark contrast to the generic and impersonal contents of a gas
tank. See, e.g., United States v. Jones, 132 S. Ct. 945, 957
(2012) (Sotomayor, J., concurring) (expressing “doubt that
people would accept without complaint the warrantless
disclosure to the Government of a list of every Web site they
had visited in the last week, or month, or year”). We rest our
analysis on the reasonableness of this search, paying
particular heed to the nature of the electronic devices and the
attendant expectation of privacy.

    The amount of private information carried by
international travelers was traditionally circumscribed by the
size of the traveler’s luggage or automobile. That is no
longer the case. Electronic devices are capable of storing
warehouses full of information. The average 400-gigabyte
laptop hard drive can store over 200 million pages—the
                 UNITED STATES V . COTTERMAN                          21

equivalent of five floors of a typical academic library. See
Orin S. Kerr, Searches and Seizures in a Digital World,
119 Harv. L. Rev. 531, 542 (2005) (explaining that an 80 GB
hard drive is equivalent to 40 million pages or one floor of an
academic library); see also LexisNexis, How Many Pages in
a Gigabyte?, http://www.lexisnexis.com/applieddiscovery/
lawlibrary/whitePapers/ADI_FS_PagesInAGigabyte.pdf.
Even a car full of packed suitcases with sensitive documents
cannot hold a candle to the sheer, and ever-increasing,
capacity of digital storage.10

    The nature of the contents of electronic devices differs
from that of luggage as well. Laptop computers, iPads and
the like are simultaneously offices and personal diaries. They
contain the most intimate details of our lives: financial
records, confidential business documents, medical records
and private emails. This type of material implicates the
Fourth Amendment’s specific guarantee of the people’s right
to be secure in their “papers.” U.S. Const. amend. IV. The
express listing of papers “reflects the Founders’ deep concern
with safeguarding the privacy of thoughts and ideas—what
we might call freedom of conscience—from invasion by the
government.” Seljan, 547 F.3d at 1014 (Kozinski, C.J.,
dissenting); see also New York v. P.J. Video, Inc., 475 U.S.
868, 873 (1986). These records are expected to be kept


   10
      W e are puzzled by the dissent’s speculation about “how many
gigabytes of storage [one must] buy to secure the guarantee that
reasonable suspicion will be required before one’s devices are searched.”
Dissent at 68. We discuss the typical storage capacity of electronic
devices simply to highlight the features that generally distinguish them
from traditional baggage. Indeed, we do not and need not determine
whether Cotterman’s laptop possessed unusually large or simply
“average” capacity in order to resolve that the forensic examination of it
required reasonable suspicion.
22               UNITED STATES V . COTTERMAN

private and this expectation is “one that society is prepared to
recognize as ‘reasonable.’” Katz v. United States, 389 U.S.
347, 361 (1967) (Harlan, J., concurring).11

     Electronic devices often retain sensitive and confidential
information far beyond the perceived point of erasure,
notably in the form of browsing histories and records of
deleted files. This quality makes it impractical, if not
impossible, for individuals to make meaningful decisions
regarding what digital content to expose to the scrutiny that
accompanies international travel. A person’s digital life
ought not be hijacked simply by crossing a border. When
packing traditional luggage, one is accustomed to deciding
what papers to take and what to leave behind. When carrying
a laptop, tablet or other device, however, removing files
unnecessary to an impending trip is an impractical solution
given the volume and often intermingled nature of the files.
It is also a time-consuming task that may not even effectively
erase the files.

    The present case illustrates this unique aspect of
electronic data. Agents found incriminating files in the
unallocated space of Cotterman’s laptop, the space where the
computer stores files that the user ostensibly deleted and
maintains other “deleted” files retrieved from web sites the
user has visited. Notwithstanding the attempted erasure of
material or the transient nature of a visit to a web site,

  11
    The dissent’s discussion about Facebook and other platforms where
the user voluntarily transmits personal data over the Internet, often
oblivious to privacy issues, Dissent at 65–66, is a red herring. Of course,
willful disclosure of electronic data, like disclosure of other material,
undercuts an individual’s expectation of privacy. But there was no such
disclosure here. Nor does the border search implicate such an affirmative
disclosure.
                  UNITED STATES V . COTTERMAN                            23

computer forensic examination was able to restore the files.
It is as if a search of a person’s suitcase could reveal not only
what the bag contained on the current trip, but everything it
had ever carried.

    With the ubiquity of cloud computing, the government’s
reach into private data becomes even more problematic.12 In
the “cloud,” a user’s data, including the same kind of highly
sensitive data one would have in “papers” at home, is held on
remote servers rather than on the device itself. The digital
device is a conduit to retrieving information from the cloud,
akin to the key to a safe deposit box. Notably, although the
virtual “safe deposit box” does not itself cross the border, it
may appear as a seamless part of the digital device when
presented at the border. With access to the cloud through
forensic examination, a traveler’s cache is just a click away
from the government.

    As Justice Scalia wrote, “It would be foolish to contend
that the degree of privacy secured to citizens by the Fourth
Amendment has been entirely unaffected by the advance of
technology.” Kyllo, 533 U.S. at 33–34. Technology has the
dual and conflicting capability to decrease privacy and
augment the expectation of privacy. While the thermal
imaging device in Kyllo threatened to expose the hour at


  12
     “The term ‘cloud computing’ is based on the industry usage of a cloud
as a metaphor for the ethereal internet. . . . An external cloud platform is
storage or software access that is essentially rented from (or outsourced to)
a remote public cloud service provider, such as Amazon or Google. . . .
By contrast, an internal or private cloud is a cluster of servers that is
networked behind an individual or company’s own firewall.” David A.
Couillard, Defogging the Cloud: Applying Fourth Amendment Principles
to Evolving Privacy Expectations in Cloud Computing, 93 Minn. L. Rev.
2205, 2216 (2009) (internal citations omitted).
24              UNITED STATES V . COTTERMAN

which “the lady of the house” took her daily “sauna and
bath,” id. at 38, digital devices allow us to carry the very
papers we once stored at home.

    The point is technology matters. The Department of
Homeland Security has acknowledged as much in the context
of international travelers:

        Where someone may not feel that the
        inspection of a briefcase would raise
        significant privacy concerns because the
        volume of information to be searched is not
        great, that same person may feel that a search
        of their laptop increases the possibility of
        privacy risks due to the vast amount of
        information potentially available on electronic
        devices.

DHS, Privacy Impact Assessment for the Border Searches of
Electronic Devices 2 (Aug. 25, 2009), available at
h t t p : / / w w w . d hs.gov/ x li brary/ ass e t s / p r i v a c y
/privacy_pia_cbp_laptop.pdf.

     This is not to say that simply because electronic devices
house sensitive, private information they are off limits at the
border. The relevant inquiry, as always, is one of
reasonableness. But that reasonableness determination must
account for differences in property. See Samson v.
California, 547 U.S. 843, 848 (2006) (“Under our general
Fourth Amendment approach, we examine the totality of the
circumstances to determine whether a search is reasonable
. . . .”) (internal quotation marks, citation, and alterations
omitted) (emphasis added). Unlike searches involving a
reassembled gas tank, Flores-Montano, 541 U.S. at 150, or
              UNITED STATES V . COTTERMAN                    25

small hole in the bed of a pickup truck, United States v.
Chaudhry, 424 F.3d 1051, 1054 (9th Cir. 2005), which have
minimal or no impact beyond the search itself—and little
implication for an individual’s dignity and privacy
interests—the exposure of confidential and personal
information has permanence.           It cannot be undone.
Accordingly, the uniquely sensitive nature of data on
electronic devices carries with it a significant expectation of
privacy and thus renders an exhaustive exploratory search
more intrusive than with other forms of property.

    After their initial search at the border, customs agents
made copies of the hard drives and performed forensic
evaluations of the computers that took days to turn up
contraband. It was essentially a computer strip search. An
exhaustive forensic search of a copied laptop hard drive
intrudes upon privacy and dignity interests to a far greater
degree than a cursory search at the border. It is little comfort
to assume that the government—for now—does not have the
time or resources to seize and search the millions of devices
that accompany the millions of travelers who cross our
borders. It is the potential unfettered dragnet effect that is
troublesome.

     We recognize the important security concerns that prevail
at the border. The government’s authority to protect the
nation from contraband is well established and may be
“heightened” by “national cris[e]s,” such as the smuggling of
illicit narcotics, Montoya de Hernandez, 473 U.S. at 538, the
current threat of international terrorism and future threats yet
to take shape. But even in the face of heightened concerns,
we must account for the Fourth Amendments rights of
travelers. Id. at 539.
26                UNITED STATES V . COTTERMAN

    The effort to interdict child pornography is also a
legitimate one. But legitimate concerns about child
pornography do not justify unfettered crime-fighting searches
or an unregulated assault on citizens’ private information.
Reasonable suspicion is a modest, workable standard that is
already applied in the extended border search, Terry stop,13
and other contexts.       Its application to the forensic
examination here will not impede law enforcement’s ability
to monitor and secure our borders or to conduct appropriate
searches of electronic devices.

    Nor does applying this standard impede the deterrent
effect of suspicionless searches, which the dissent contends
is critical to thwarting savvy terrorists and other criminals.
Dissent at 63. The Supreme Court has never endorsed the
proposition that the goal of deterring illegal contraband at the
border suffices to justify any manner of intrusive search.
Rather, reasonableness remains the touchstone and the Court
has expressed support for the deterrence value of
suspicionless searches of a routine nature, such as vehicle
checkpoints near the border.           See United States v.
Martinez-Fuerte, 428 U.S. 543, 556 (1976) (“We note here
only the substantiality of the public interest in the practice of
routine stops for inquiry at permanent checkpoints, a practice
which the Government identifies as the most important of the
traffic-checking operations.”) (emphasis added). In practical
terms, suspicionless searches of the type approved in Arnold
will continue; border officials will conduct further, forensic
examinations where their suspicions are aroused by what they
find or by other factors. Reasonable suspicion leaves ample
room for agents to draw on their expertise and experience to
pick up on subtle cues that criminal activity may be afoot.

 13
      Terry v. Ohio, 392 U.S. 1, 30 (1983).
                 UNITED STATES V . COTTERMAN                           27

See United States v. Tiong, 224 F.3d 1136, 1140 (9th Cir.
2000).14

     We have confidence in the ability of law enforcement to
distinguish a review of computer files from a forensic
examination. We do not share the alarm expressed by the
concurrence and the dissent that the standard we announce
will prove unmanageable or give border agents a “Sophie’s
choice” between thorough searches and Bivens actions.
Concurrence at 48–49; Dissent at 65. Determining whether
reasonable suspicion is required does not necessitate a
“complex legal determination[]” to be made on a “moment-
by-moment basis.” Dissent at 61. Rather, it requires that
officers make a commonsense differentiation between a
manual review of files on an electronic device and application
of computer software to analyze a hard drive, and utilize the
latter only when they possess a “particularized and objective



  14
     The greatest obstacle to ferreting out contraband at the border has
always been the sheer number of international travelers. Any contention
that national security will be critically hampered by stripping border
agents of a critical law enforcement tool— suspicionless forensic
examinations of electronics— is undermined by the fact that, as a matter
of commonsense and resources, it is only when reasonable suspicion is
aroused that such searches typically take place. See, e.g., Chaudhry,
424 F.3d at 1054 (B. Fletcher, J., concurring) (“As a practical matter,
border agents are too busy to do extensive searches (removing gas tanks
and door panels, boring holes in truck beds) unless they have suspicion.”).
As Judge Callahan acknowledges in her separate opinion, the record
suggests that “remote and/or intensive searches of electronic devices
crossing the border do not occur all that often.” Concurrence at 50 n.11.
The reference that only a small fraction of travelers at the border have
their devices searched simply reinforces our point— our ruling will not
place an undue burden on border agents who already rely on a degree of
suspicion in referring travelers to secondary inspection.
28            UNITED STATES V . COTTERMAN

basis for suspecting the person stopped of criminal activity.”
Tiong, 224 F.3d at 1140 (internal quotation marks omitted).

    International travelers certainly expect that their property
will be searched at the border. What they do not expect is
that, absent some particularized suspicion, agents will mine
every last piece of data on their devices or deprive them of
their most personal property for days (or perhaps weeks or
even months, depending on how long the search takes).
United States v. Ramos-Saenz, 36 F.3d 59, 61 n.3 (9th Cir.
1994) (“Intrusiveness includes both the extent of a search as
well as the degree of indignity that may accompany a
search.”). Such a thorough and detailed search of the most
intimate details of one’s life is a substantial intrusion upon
personal privacy and dignity. We therefore hold that the
forensic examination of Cotterman’s computer required a
showing of reasonable suspicion, a modest requirement in
light of the Fourth Amendment.

IV.    REASONABLE SUSPICION

    Reasonable suspicion is defined as “a particularized and
objective basis for suspecting the particular person stopped of
criminal activity.” United States v. Cortez, 449 U.S. 411,
417–18 (1981). This assessment is to be made in light of “the
totality of the circumstances.” Id. at 417. “[E]ven when
factors considered in isolation from each other are susceptible
to an innocent explanation, they may collectively amount to
a reasonable suspicion.” United States v. Berber-Tinoco,
510 F.3d 1083, 1087 (9th Cir. 2007). We review reasonable
suspicion determinations de novo, reviewing findings of
historical fact for clear error and giving “due weight to
inferences drawn from those facts by resident judges and
               UNITED STATES V . COTTERMAN                    29

local law enforcement officers.” Ornelas v. United States,
517 U.S. 690, 699 (1996).

   In the district court and in supplemental briefing, the
government argued that the border agents had reasonable
suspicion to conduct the initial search and the forensic
examination of Cotterman’s computer. We agree.

    The objective facts reflect that both the agents at the
border and the agents who arrived later from Sells based their
decision to search Cotterman’s belongings on the TECS hit.
Officer Alvarado was told by those in charge of administering
the TECS database that he should search Cotterman’s
property because the TECS hit indicated “that [Cotterman]
appeared to [have] been involved in some type of child
pornography.” Agent Riley also looked up Cotterman’s
criminal record and understood that he had a prior conviction
for child pornography. As it turned out, Cotterman’s
previous conviction was not for pornography, but for child
molestation. Nonetheless, the agents’ understanding of the
objective facts, albeit mistaken, is the baseline for
determining reasonable suspicion. See Liberal v. Estrada,
632 F.3d 1064, 1077 (9th Cir. 2011) (“Even if an officer
makes a mistake of fact, that mistake ‘will not render a stop
illegal, if the objective facts known to the officer gave rise to
a reasonable suspicion that criminal activity was afoot.’”
(quoting United States v. Mariscal, 285 F.3d 1127, 1131 (9th
Cir. 2002))).

    By itself, Cotterman’s 1992 conviction for child
molestation does not support reasonable suspicion to conduct
an extensive forensic search of his electronic devices.
“Although a prior criminal history cannot alone establish
reasonable suspicion . . . it is permissible to consider such a
30                UNITED STATES V . COTTERMAN

fact as part of the total calculus of information in th[at]
determination[].” Burrell v. McIlroy, 464 F.3d 853, 858 n.3
(9th Cir. 2006). The TECS alert was not based merely on
Cotterman’s conviction—the agents were aware that the alert
targeted Cotterman because he was a sex offender “who
travel[ed] frequently out of the country” and who was
“possibly involved in child sex tourism.” Further, Agent
Riley testified that an examination of Cotterman’s passport
confirmed that he had traveled in and out of the country
frequently since his conviction in 1992.

    In further support of reasonable suspicion, the
government asserts that Mexico, from which the Cottermans
were returning, is “a country associated with sex tourism.”15
The ICE field office specifically informed Agent Riley that
the alert was part of Operation Angel Watch, which targeted
individuals potentially involved in sex tourism and alerted
officials to be on the lookout for laptops, cameras and other
paraphernalia of child pornography. See 156 Cong. Rec.
S9581-03 (daily ed. Dec. 14, 2010) (describing Operation
Angel Watch as a program “help[ing] ICE [to] identify travel
patterns of convicted sex offenders who may attempt to
exploit children in foreign countries”). Cotterman’s TECS
alert, prior child-related conviction, frequent travels, crossing
from a country known for sex tourism, and collection of
electronic equipment, plus the parameters of the Operation


 15
    It is ironic that the dissent expresses concern that, by factoring in the
incidence of crime in particular countries, “thousands of individuals . . .
will now be forced to reconsider traveling to entire countries . . . or will
need to leave all their electronic equipment behind, to avoid arousing a
‘reasonable’ suspicion,” Dissent at 78, when, if forensic examination of
those travelers’ electronics occurs at the border, the dissent would require
no suspicion at all.
                 UNITED STATES V . COTTERMAN                           31

Angel Watch program, taken collectively, gave rise to
reasonable suspicion of criminal activity.

    To these factors, the government adds another—the
existence of password-protected files on Cotterman’s
computer.16 We are reluctant to place much weight on this
factor because it is commonplace for business travelers,
casual computer users, students and others to password
protect their files. Law enforcement “cannot rely solely on
factors that would apply to many law-abiding citizens,”
Berber-Tinoco, 510 F.3d at 1087, and password protection is
ubiquitous. National standards require that users of mobile
electronic devices password protect their files. See generally
United States Department of Commerce, Computer Security
Division, National Institute of Standards and Technology,
Computer Security (2007) (NIST Special Publication
800-111). Computer users are routinely advised—and in
some cases, required by employers—to protect their files
when traveling overseas. See, e.g., Michael Price, National
Security Watch, 34-MAR Champion 51, 52 (March 2010)
(“[T]here is one relatively simple thing attorneys can do
[when crossing the border] to protect their privacy and the
rights of their clients: password-protect the computer login
and any sensitive files or folders.”).

    Although password protection of files, in isolation, will
not give rise to reasonable suspicion, where, as here, there are
other indicia of criminal activity, password protection of files




 16
    Agent Riley testified that Alvarado told her that he had “encounter[ed]
some files that were password protected,” while Agent Alvarado testified
that he found one file.
32               UNITED STATES V . COTTERMAN

may be considered in the totality of the circumstances.17 To
contribute to reasonable suspicion, encryption or password
protection of files must have some relationship to the
suspected criminal activity. Here, making illegal files
difficult to access makes perfect sense for a suspected holder
of child pornography. When combined with the other
circumstances, the fact that Officer Alvarado encountered at
least one password protected file on Cotterman’s computer
contributed to the basis for reasonable suspicion to conduct
a forensic examination.

    The existence of the password-protected files is also
relevant to assessing the reasonableness of the scope and
duration of the search of Cotterman’s computer. The search
was necessarily protracted because of the password protection
that Cotterman employed. After Cotterman failed to provide
agents with the passwords to the protected files and fled the
country, it took Agent Owen days to override the computer
security and open the image files of child pornography.

     Although we must take into account factors weighing
both in favor and against reasonable suspicion, Cotterman’s
innocent explanation does not tip the balance. See Tiong,
224 F.3d at 1140 (recognizing that “innocent possibilities
. . . do not undermine reasonable suspicion”). The dissent
suggests that Cotterman’s offer at the border “to help the
agents access his computer” counsels against a finding of
reasonable suspicion. Dissent at 80. The agents were


  17
      W e do not suggest that password protecting an entire device—as
opposed to files within a device— can be a factor supporting a reasonable
suspicion determination. Using a password on a device is a basic means
of ensuring that the device cannot be accessed by another in the event it
is lost or stolen.
               UNITED STATES V . COTTERMAN                    33

appropriately wary of such an offer due to concerns that
Cotterman could tamper with the devices. Nor did the
agents’ discovery of vacation photos eliminate the suspicion
that Cotterman had engaged in criminal activity while abroad
or might be importing child pornography into the country.
Because the first examination of Cotterman’s laptop, by
Officer Alvarado, turned up nothing incriminating, Cotterman
urges that any suspicion prompted by the TECS alert was
dispelled by this initial failure. But the nature of the alert on
Cotterman, directing agents to review media and electronic
equipment for child pornography, justified conducting the
forensic examination despite the failure of the first search to
yield any contraband.

     Collectors of child pornography can hardly be expected
to clearly label such files and leave them in readily visible
and accessible sections of a computer’s hard drive,
particularly when they are traveling through border crossings,
where individuals ordinarily anticipate confronting at least a
cursory inspection. Officer Alvarado, who was responsible
for conducting the initial search, was specifically looking for
photographs as described in the TECS hit but testified that he
had only a slightly above-average familiarity with laptops.
He could do no more than open a file, look at it and see if he
could access it. He testified that “[i]f [he] encountered
something that [he] could not access, then [he] would
reference it to somebody that may have that ability to look at
[it].” That is precisely what occurred here. Officer Alvarado
came across password-protected files but, unable to open
them, moved on to other files. Alvarado told Agent Riley
about the password protection, and she and Agent Brisbine
decided to seize the computers for further examination. The
border agents “certainly had more than an inchoate and
unparticularized suspicion or hunch” of criminal activity to
34             UNITED STATES V . COTTERMAN

support their decision to more carefully search for evidence
of child pornography. Montoya de Hernandez, 473 U.S. at
542 (internal quotation marks and citation omitted). An alert
regarding possession of this type of criminal contraband
justified obtaining additional resources, here available in
Tucson, to properly determine whether illegal files were
present.

    Unlike the dissent, we credit the agents’ observations and
experience in acting upon significant myriad factors that
support reasonable suspicion. It is not our province to nitpick
the factors in isolation but instead to view them in the totality
of the circumstances. For the above reasons, we conclude
that the examination of Cotterman’s electronic devices was
supported by reasonable suspicion and that the scope and
manner of the search were reasonable under the Fourth
Amendment. Cotterman’s motion to suppress therefore was
erroneously granted.

     REVERSED.



CALLAHAN, Circuit Judge, concurring in part, dissenting in
part, and concurring in the judgment, with whom CLIFTON,
Circuit Judge, joins, and with whom M. SMITH, Circuit
Judge, joins as to all but Part II.A:

     Whether it is drugs, bombs, or child pornography, we
charge our government with finding and excluding any and
all illegal and unwanted articles and people before they cross
our international borders. Accomplishing that Herculean task
requires that the government be mostly free from the Fourth
Amendment’s usual restraints on searches of people and their
               UNITED STATES V . COTTERMAN                    35

property. Today the majority ignores that reality by erecting
a new rule requiring reasonable suspicion for any thorough
search of electronic devices entering the United States. This
rule flouts more than a century of Supreme Court precedent,
is unworkable and unnecessary, and will severely hamstring
the government’s ability to protect our borders.

    I therefore dissent from Part III of the majority’s opinion.
I concur in Parts I, II, and IV, and in particular the majority’s
conclusion in Part IV that the government had reasonable
suspicion to conduct the forensic examination of Howard
Cotterman’s electronic devices. I therefore also concur in the
judgment.

                               I.

    Over the last 125 years, the Supreme Court has explained
that the United States and its people have a “paramount
interest” in national self-protection and an “inherent” right to
exclude illegal and “unwanted persons and effects.” United
States v. Flores-Montano, 541 U.S. 149, 152–53 (2004); see
also United States v. Montoya de Hernandez, 473 U.S. 531,
537–40 (1985); United States v. Ramsey, 431 U.S. 606,
616–18 (1977); United States v. Thirty-Seven (37)
Photographs, 402 U.S. 363, 376 (1971); Carroll v. United
States, 267 U.S. 132, 154 (1925); Boyd v. United States,
116 U.S. 616, 623 (1886). Accordingly, “[t]he Government’s
interest in preventing the entry of unwanted persons and
effects is at its zenith at the international border.” Flores-
Montano, 541 U.S. at 152.

    To effectuate this interest, the Supreme Court has
recognized a broad exception to the Fourth Amendment’s
requirement of probable cause or a warrant for searches
36               UNITED STATES V . COTTERMAN

conducted at the border. Under that exception, searches of
people and their property at the United States borders and
their functional equivalents are per se reasonable, meaning
that they typically do not require a warrant, probable cause,
or even reasonable suspicion. Montoya de Hernandez,
473 U.S. at 538; see also Flores-Montano, 541 U.S. at
152–53; Ramsey, 431 U.S. at 616–18; United States v. Seljan,
547 F.3d 993, 999–1000 (9th Cir. 2008) (en banc), cert.
denied, 129 S. Ct. 1368 (2009).

    In the long time that the Court has recognized the border
search doctrine, the Court has found just one search at the
border that required reasonable suspicion. See Montoya de
Hernandez, 473 U.S. at 541 (upholding the 24-hour detention
of a woman suspected of smuggling illegal drugs in her
digestive system, followed by a pregnancy test and rectal
examination, based on reasonable suspicion). In the
remaining cases, the Court consistently has described the
government’s border search authority in very broad terms1


   1
     See, e.g., Flores-Montano, 541 U.S. at 152 (“The Government’s
interest in preventing the entry of unwanted persons and effects is at its
zenith at the international border.”); id. at 153 (“It is axiomatic that the
United States, as sovereign, has the inherent authority to protect, and a
paramount interest in protecting, its territorial integrity.”); Ramsey,
431 U.S. at 617 (“This interpretation, that border searches were not
subject to the warrant provisions of the Fourth Amendment and were
‘reasonable’ within the meaning of that Amendment, has been faithfully
adhered to by this Court.”); id. at 620 (“The border-search exception is
grounded in the recognized right of the sovereign to control, subject to
substantive limitations imposed by the Constitution, who and what may
enter the country.”); Thirty-Seven (37) Photographs, 402 U.S. at 376 (“[A
traveler’s] right to be let alone neither prevents the search of his luggage
nor the seizure of unprotected, but illegal, materials when his possession
of them is discovered during such a search.               Customs officers
characteristically inspect luggage and their power to do so is not
                 UNITED STATES V . COTTERMAN                            37

and overturned the lower courts’ attempts to cabin that
authority.2 The Court also repeatedly has gone out of its way
to explain that border searches generally are exempt from the
limits it imposes on domestic searches. See, e.g., Flores-
Montano, 541 U.S. at 154 (“[O]n many occasions, we have
noted that the expectation of privacy is less at the border than
it is in the interior.”); Montoya de Hernandez, 473 U.S. at
539–40 (“But not only is the expectation of privacy less at the
border than in the interior, the Fourth Amendment balance
between the interests of the Government and the privacy right
of the individual is also struck much more favorably to the
Government at the border.” (internal and external citations
omitted)); United States v. 12 200-Foot Reels of Super 8mm.
Film, 413 U.S. 123, 125 (1973) (“Import restrictions and
searches of persons or packages at the national borders rest on




questioned in this case; it is an old practice and is intimately associated
with excluding illegal articles from the country.”); Carroll, 267 U.S. at
154 (“Travelers may be so stopped in crossing an international boundary
because of national self-protection reasonably requiring one entering the
country to identify himself as entitled to come in, and his belongings as
effects which may be lawfully brought in.”). Even in Montoya de
Hernandez the Court described the government’s border search authority
expansively. See 473 U.S. at 539–40, 542–44.

 2
   See, e.g., Flores-Montano, 541 U.S. at 152–55 (overturning the Ninth
Circuit’s conclusion that the border search of a gas tank required
reasonable suspicion); Ramsey, 431 U.S. at 616–22 (overturning the D.C.
Circuit’s conclusion that the search of international mail required probable
cause); Thirty-Seven (37) Photographs, 402 U.S. at 376 (relying in part on
border search doctrine to overturn lower court’s decision that statute
barring the importation of obscene material was unconstitutional).
38               UNITED STATES V . COTTERMAN

different considerations and different rules of constitutional
law from domestic regulations.”).3

                                    II.

    It is against this legal backdrop that we must assess the
constitutionality of the government’s search in this case. As
with all searches subject to Fourth Amendment review, the
constitutionality of a border search turns on whether it is
reasonable. See Brigham City, Utah v. Stuart, 547 U.S. 398,
403 (2006) (“[T]he ultimate touchstone of the Fourth
Amendment is ‘reasonableness.’”). Under the border search
doctrine, suspicionless border searches are per se reasonable.
However, the Supreme Court has identified three situations
in which they might not be per se reasonable, i.e., at least
reasonable suspicion is required: (1) “highly intrusive
searches of the person;” (2) destructive searches of property;



   3
     See also City of Indianapolis v. Edmond, 531 U.S. 32, 47–48 (2000)
(explaining that decision barring domestic drug interdiction checkpoints
“does not affect the validity of border searches or searches at places like
airports”); United States v. Ross, 456 U.S. 798, 823 (1982) (explaining
that while the Fourth Amendment gives protection to containers in
domestic vehicles, “[t]he luggage carried by a traveler entering the country
may be searched at random by a customs officer”); Torres v. Puerto Rico,
442 U.S. 465, 472–74 (1979) (distinguishing between United
States–Puerto Rico border and international borders in holding
unconstitutional the search of a traveler’s luggage without “articulable
suspicion”); United States v. Brignoni-Ponce, 422 U.S. 873, 884 (1975)
(“Except at the border and its functional equivalents, officers on roving
patrol may stop vehicles” only with reasonable suspicion they contain
illegal aliens); Almeida-Sanchez v. United States, 413 U.S. 266, 272–76
(1973) (distinguishing searches of vehicles at the border from a search that
occurred 25 miles away); Carroll, 267 U.S. at 151–54 (distinguishing
between interior and border searches of vehicles and persons).
                 UNITED STATES V . COTTERMAN                            39

and (3) searches conducted in a “particularly offensive”
manner. Flores-Montano, 541 U.S. at 152–56 & n.2.

     Although its opinion is not entirely clear, the majority
appears to rely on the first and third exceptions to hold that
the search at issue in this case required reasonable suspicion.
(There is no claim that the government damaged or destroyed
Cotterman’s property.) But the exception for “highly
intrusive searches of the person,” Flores-Montano, 541 U.S.
at 152, cannot apply here; “papers,” even private ones in
electronic format, are not a “person.” See id. (“The reasons
that might support a requirement of some level of suspicion
in the case of highly intrusive searches of the person—dignity
and privacy interests of the person being searched—simply
do not carry over to vehicles.”). That leaves the exception for
searches conducted in a “particularly offensive” manner. Id.
at 154 n.2. The majority relies primarily on the notion that
electronic devices are special to conclude that reasonable
suspicion was required. Majority at 20–28. The majority is
mistaken.

                                    A.

    The majority correctly concludes that the government’s
forensic search in Tucson was not an extended border search,
as the border agents retained custody of Cotterman’s laptop.4

  4
    I agree with the majority that this case does not involve an extended
border search. Unlike a border search, an extended border search takes
place at a location “away from the border where entry is not apparent, but
where the dual requirements of reasonable certainty of a recent border
crossing and reasonable suspicion of criminal activity are satisfied.”
United States v. Guzman-Padilla, 573 F.3d 865, 878–79 (9th Cir. 2009)
(internal quotation marks and citation omitted), cert. denied, 131 S. Ct. 67
(2010). Reasonable suspicion is required precisely because the individual
40               UNITED STATES V . COTTERMAN

Id. at 9, 14–15. The majority also states that “[i]t is the
comprehensive and intrusive nature of a forensic
examination—not the location of the examination—that is the
key factor triggering the requirement of reasonable suspicion
here.” Majority at 17. The inclusion of the word “key” might
be read to imply that some other factor, such as the location
and duration of the search, contributed to its purported
unreasonableness. I write to refute any such notion.

    First consider the facts. The border agents took
Cotterman’s electronic devices to the nearest computing
center (to Tucson, where Cotterman and his wife were
already traveling), before clearing them for entry into the
United States. The computer specialist moved the search
ahead of his other work and conducted it over the weekend.
Although the forensic search lasted five days, it took only 48
hours to discover the initial 75 images of child pornography.
The agents were reasonably reluctant to rely on Cotterman’s
offer to help, since he might have deleted or otherwise made
unrecoverable any contraband that his devices contained.
The agents returned the devices as soon as they cleared them.




has regained an expectation of privacy by moving away from the border.
See United States v. Villasenor, 608 F.3d 467, 471–72 (9th Cir.), cert.
denied, 131 S. Ct. 547 (2010); United States v. Whiting, 781 F.2d 692, 695
(9th Cir. 1986). Here, there was no attenuation between Cotterman’s
border crossing and the forensic search of his electronic property; the
government conducted that search before clearing the property for entry
and before Cotterman could regain an expectation of privacy in that
property. See 19 U.S.C. § 1499 (providing that imported goods are
permitted entry only after Customs clears them); United States v. Alfonso,
759 F.2d 728, 734 (9th Cir. 1985) (“Extended border searches occur after
the actual entry has been effected and intrude more on an individual’s
normal expectation of privacy.”).
               UNITED STATES V . COTTERMAN                    41

    Now consider the law. The Supreme Court has upheld the
constitutionality of a police search of packages retrieved from
an automobile, even though the police conducted their search
three days after the police stopped the vehicle and at the
police station. United States v. Johns, 469 U.S. 478, 485–88
(1985). The Court rejected the argument that “searches of
containers discovered in the course of a vehicle search are
subject to temporal restrictions not applicable to the vehicle
search itself.” Id. at 485. Although Johns involved a
domestic automobile search based on probable cause, it still
stands for the proposition, equally applicable to this case, that
“the legality of the search was determined by reference to the
[applicable] exception to the warrant requirement.” Id.

     In the border search context, the Supreme Court, in
upholding the lengthy detention of a person reasonably
suspected of smuggling drugs in her digestive system at an
airport, addressed whether that detention was “reasonably
related in scope to the circumstances which justified it
initially.” Montoya de Hernandez, 473 U.S. at 542. The
Court explained that: (1) “courts should not indulge in
unrealistic second-guessing” when answering this question,
as “[a]uthorities must be allowed to graduate their response
to the demands of any particular situation;” (2) the Court
consistently has “refused to charge police with delays in
investigatory detention attributable to the suspect’s evasive
actions;” and (3) “we have also consistently rejected hard-
and-fast time limits.” Id. at 542–43 (quotation marks and
citations omitted). The Court emphasized that, at the
international border, “the Fourth Amendment balance of
interests leans heavily to the Government” because the
government is charged not just with investigating crime but
with “protecting this Nation from entrants who may bring
anything harmful into this country.” Id. at 544. Finally, any
42                UNITED STATES V . COTTERMAN

“length” or “discomfort” associated with a border search does
not offend the Fourth Amendment when it “result[s] solely
from the method by which [a traveler] cho[oses] to smuggle
[contraband] into this country.” Id.

    Any suggestion that the government’s search here was
“particularly offensive” due to the location and duration of
the search runs counter to the Supreme Court’s admonitions
in Johns and Montoya de Hernandez. It also effectively
requires the government to supply every port of entry with the
equipment and staff needed to conduct forensic electronic
searches, or at least to have such equipment and staff waiting
at a nearby location. Such a requirement is unreasonable,
particularly since the record in this case suggests that a
forensic search of Cotterman’s electronic devices at the
border station would have taken longer than the search at the
Tucson computing center.5 See United States v. Hill,
459 F.3d 966, 974–75 (9th Cir. 2006), cert. denied, 127 S. Ct.
1863 (2007) (discussing problems inherent in requiring police
to bring with them equipment to search electronic media); cf.
Johns, 469 U.S. at 486–87 (explaining that requiring police


 5
   The district court found that the government could have conducted the
forensic search at the Lukeville border station. United States v.
Cotterman, No. CR 07-1207-TUC-RCC, 2009 WL 465028, at *1 (D. Ariz.
Feb. 24, 2009). The court presumably based this finding on testimony that
the computer specialist who conducted the forensic examination had a
specially-equipped laptop. However, the specialist testified that using his
laptop at the border station, rather than transporting Cotterman’s electronic
devices to the Tucson computer center, would have taken “a lot longer”
because the laptop was “not nearly as extensive as what I have in my lab,”
the “processor in my laptop is much slower” than the lab equipment, and
“I could only do one computer at a time with the laptop.” Technical
difficulties also could have slowed down an examination conducted at the
border station.
              UNITED STATES V . COTTERMAN                   43

officers to immediately inspect all packages “would be of
little benefit to the person whose property is searched”).

                              B.

    The majority’s opinion turns primarily on the notion that
electronic devices deserve special consideration because they
are ubiquitous and can store vast quantities of personal
information. That idea is fallacious and has no place in the
border search context.

    The Supreme Court has been willing to distinguish only
between border searches of people and property, not between
different types of property. In 2004, in Flores-Montano, the
Court explained that

       the reasons that might support a requirement
       of some level of suspicion in the case of
       highly intrusive searches of the
       person—dignity and privacy interests of the
       person being searched—simply do not carry
       over to vehicles. Complex balancing tests to
       determine what is a “routine” search of a
       vehicle, as opposed to a more “intrusive”
       search of a person, have no place in border
       searches of vehicles.

541 U.S. at 152. We have since applied Flores-Montano to
hold that any distinction between “routine” and “nonroutine”
searches does not apply to searches of property, and that there
can be no “least restrictive means” test for border searches.
United States v. Chaudhry, 424 F.3d 1051, 1054 (9th Cir.
2005), cert. denied, 547 U.S. 1083 (2006); United States v.
Cortez-Rocha, 394 F.3d 1115, 1122–23 (9th Cir. 2004), cert.
44               UNITED STATES V . COTTERMAN

denied, 546 U.S. 849 (2005).6 Put another way, the Supreme
Court—and, reluctantly, this court—have refused to adopt a
sliding “intrusiveness” scale for border searches of property.
Thus, the Court has all but held that property that crosses the
border, whatever it is, does not merit Fourth Amendment
protection.

    Of course, Flores-Montano, Chaudhry, and Cortez-Rocha
involved vehicles or parts of vehicles, not electronic devices,
and the other border search cases that have reached the
Supreme Court all involved containers of some sort. See,
e.g., Ramsey, 431 U.S. at 616–22 (mail); Thirty-Seven (37)
Photographs, 402 U.S. at 376 (luggage). And yes, the Court
has left open the possibility that a border search might be
“‘‘unreasonable’ because of the particularly offensive manner
in which it is carried out.’” Flores-Montano, 541 U.S. at 154
n.2 (quoting Ramsey, 431 U.S. at 618 n.13). But is the mere
fact that Cotterman chose to save his child pornography
electronically, rather than print it out on paper, enough to
invoke that exception?

   The two courts of appeals—including this court—that
have had occasion to address whether electronic devices


  6
    In 1985, the Supreme Court wrote about the government’s “plenary
authority to conduct routine searches and seizures at the border.”
Montoya de Hernandez, 473 U.S. at 537 (emphasis added); see also id. at
541 n.4 (“Because the issues are not presented today we suggest no view
on what level of suspicion, if any, is required for nonroutine border
searches such as strip, body-cavity, or involuntary x-ray searches.”)
(emphasis added). W e unfortunately seized on the word “routine” to
establish a sliding scale of intrusiveness, with more intrusive (i.e., less
“routine”) searches requiring reasonable suspicion. See, e.g., United
States v. Molina-Tarazon, 279 F.3d 709, 711–13 (9th Cir. 2002). Flores-
Montano plainly repudiated that approach.
              UNITED STATES V . COTTERMAN                  45

deserve special consideration have correctly concluded that
they do not. In United States v. Arnold, 533 F.3d 1003,
1008–10 (9th Cir. 2008), cert. denied, 555 U.S. 1176 (2009),
we held that laptops are like other property, relying on the
reasoning and language in Flores-Montano, Chaudhry, and
Cortez-Rocha discussed above (among other cases).
Similarly, in United States v. Ickes, 393 F.3d 501, 503–07
(4th Cir. 2005), the Fourth Circuit upheld an extensive border
search of the defendant’s laptop that revealed child
pornography. Notably, the court held that the border agents
had reasonable suspicion to search the defendant’s laptop, but
explained why that did not matter:

       The agents did not inspect the contents of
       Ickes’s computer until they had already
       discovered marijuana paraphernalia, photo
       albums of child pornography, a disturbing
       video focused on a young ball boy, and an
       outstanding warrant for Ickes’s arrest. As a
       practical matter, computer searches are most
       likely to occur where—as here—the traveler’s
       conduct or the presence of other items in his
       possession suggest the need to search further.
       However, to state the probability that
       reasonable suspicions will give rise to more
       intrusive searches is a far cry from enthroning
       this notion as a matter of constitutional law.
       The essence of border search doctrine is a
       reliance upon the trained observations and
       judgments of customs officials, rather than
       upon constitutional requirements applied to
       the inapposite context of this sort of search.
46               UNITED STATES V . COTTERMAN

Id. at 507. Thus, the Fourth Circuit has recognized what the
majority does not: electronic devices are like any other
container that the Supreme Court has held may be searched
at the border without reasonable suspicion.7 Though we are
not bound by Arnold nor Ickes in this en banc proceeding, we
are bound by what the Supreme Court has said: in the unique
context of border searches, property is property and we may
not chip away at the government’s authority to search it by
adopting a sliding scale of intrusiveness. It’s the border, not
the technology, that “matters.” Majority at 24; cf. Ramsey,
431 U.S. at 620 (“It is clear that there is nothing in the
rationale behind the border-search exception which suggests
that the mode of entry will be critical.”).

    Logic and commonsense, not just Supreme Court
precedent, reveal the flaws in the majority’s opinion. The
fact that electronic devices are capable of storing a lot of
personal information does not make an extensive search of
them “particularly offensive.” We have squarely rejected the
idea that the “intrusiveness” of a search depends in whole or
in part on the nature of the property being searched. In
United States v. Giberson, 527 F.3d 882 (9th Cir. 2008), we
specifically rebuffed the argument that computers are special
for Fourth Amendment purposes by virtue of how much
information they store; “neither the quantity of information,
nor the form in which it is stored, is legally relevant in the
Fourth Amendment context.” Id. at 888; see also California
v. Carney, 471 U.S. 386, 393–94 (1985) (rejecting applying




  7
    I agree with Judge Smith that the majority’s opinion appears to create
an imprudent split with the Fourth Circuit. See Dissent at 58.
                 UNITED STATES V . COTTERMAN                            47

Fourth Amendment protection to property (a mobile home)
that is “capable of functioning as a home” simply on account
of the property’s size or “worth[iness]” as a container);
United States v. Payton, 573 F.3d 859, 864 (9th Cir. 2009)
(“Giberson held that computers were not entitled to a special
categorical protection of the Fourth Amendment.”); Kyllo v.
United States, 533 U.S. 27, 41 (2001) (Stevens, J., dissenting)
(explaining that Fourth Amendment exceptions and
distinctions based solely on a type of technology are
“unwise[ ] and inconsistent with the Fourth Amendment”).

     While Giberson and Carney involved domestic searches,
their reasoning applies equally in the border search context.
If the government may search the contents of a briefcase, car,
or mobile home that transits the border, there is no reason it
should not also be able to search the contents of a camera,
tablet, or laptop that enters the country. All of those things
are capable of storing, and often do store, private information.
See Ross, 456 U.S. at 823 (“The luggage carried by a traveler
entering the country may be searched at random by a customs
officer; the luggage may be searched no matter how great the
traveler’s desire to conceal the contents may be.” (emphasis
added)). The majority points out that electronic devices can
and usually do store much more private information than their
non-electronic counterparts. Majority at 17–24. But “a port
of entry is not a traveler’s home,” Thirty-Seven (37)
Photographs, 402 U.S. at 376, even if a traveler chooses to
carry a home’s worth of personal information across it.8


 8
    The element of choice is crucial. The fact that border searches occur
at fixed times and checkpoints makes them inherently less intrusive; a
person “with advance notice of the location of a permanent checkpoint has
an opportunity to avoid the search entirely, or at least to prepare for, and
limit, the intrusion on her privacy.” Mich. Dep’t of State Police v. Sitz,
48               UNITED STATES V . COTTERMAN

Moreover, a bright-line rule distinguishing electronic from
non-electronic devices—of the sort the Supreme Court has
made clear has no place in Fourth Amendment jurisprudence,
Ohio v. Robinette, 519 U.S. 33, 39 (1996)—is arbitrary; there
is no reason someone carrying a laptop should receive greater
privacy protection than someone who chooses (or can only
afford) to convey his or her personal information on paper.

    In short, today the court erects a new bright-line rule:
“forensic examination” of electronic devices “at the border
requires reasonable suspicion.” Majority at 17; see also id. at
21 n.10. The majority never defines “forensic,” leaving
border agents to wonder exactly what types of searches are




496 U.S. 444, 463 (1990) (Stevens, J., dissenting); see also Montoya de
Hernandez, 473 U.S. at 544 (“Respondent’s detention was long,
uncomfortable, indeed, humiliating; but both its length and its discomfort
resulted solely from the method by which she chose to smuggle illicit
drugs into this country.”).

     The element of choice goes to the more fundamental issue of whether
someone can have any reasonable expectation of privacy when he or she
voluntarily carries electronic equipment across the border. Border officers
are permitted to examine a written diary, and someone who wants to keep
the contents of a diary secret should know not to take it across the border.
The same should be true for personal data stored on a laptop or other
electronic device rather than a written diary.

      Moreover, the fact that the Fourth Amendment does not apply in
foreign countries further weakens any claim to a reasonable expectation
of privacy in property that crosses the United States border. Carrying an
electronic device outside the United States almost always entails carrying
it into another country, making it subject to search under that country’s
laws. Travelers expect these intrusions, or at least their possibility.
                 UNITED STATES V . COTTERMAN                            49

off-limits.9 Even if the majority means to require reasonable
suspicion for any type of digital forensic border search, no
court has ever erected so categorical a rule, based on so
general a type of search or category of property, and the
Supreme Court has rightly slapped down anything remotely
similar. The majority invites—indeed, requires—the Court
to do so again.10

                                   III.

    The majority’s holding contravenes Supreme Court
precedent, defies logic and commonsense, and is unworkable.
It is also unnecessary and will impair the federal
government’s ability to protect our borders.

    As Judge Smith points out in his dissent, “[b]order patrol
agents process hundreds of thousands of travelers each day
and conduct thousands of searches on electronic devices each
year.” Dissent at 61–62 (citation omitted). All the evidence
in this case suggests that the government does not have the
resources—time, personnel, facilities, or technology—to
exhaustively search every (or even a majority) of the
electronic devices that cross our borders. Cf. Ickes, 393 F.3d
at 507. Unless we somehow manage to solve our fiscal
problems, and unless the government somehow manages to


 9
   See Darrin J. Behr, Anti-Forensics: What it Does and Why You Need
to Know, 255 N.J. Law. 9, 10 (Dec. 2008) (“Due to the fact that there are
hundreds of digital forensic investigation procedures developed all over
the world, digital forensics has yet to be defined.”).

  10
     I note that a case currently pending in the Sixth Circuit appears to
raise similar issues as this case. See United States v. Stewart, No. 12-1427
(6th Cir. filed Apr. 5, 2012); see also United States v. Stewart, 715 F.
Supp. 2d 750 (E.D. Mich. 2010).
50                UNITED STATES V . COTTERMAN

acquire better technology at a faster pace than the rest of us,
these restraints will continue. That means border agents must
prioritize who, what, and how they search. By and large,
border agents will conduct forensic electronic searches of
people who, like Howard Cotterman, the agents reasonably
suspect may be trying to carry illegal articles into, or
themselves illegally enter, the country.11 That agents
typically will have reasonable suspicion is, of course, “a far
cry from enthroning this notion as a matter of constitutional
law.” Ickes, 393 F.3d at 507.

    The majority finds this reality check to be of “little
comfort[;] [i]t is the potential unfettered dragnet effect that is
troublesome.” Majority at 25. But that abstract risk, which
exists with any exception to the Fourth Amendment, does not
justify a bright-line rule requiring reasonable suspicion for
any thorough search of electronic devices entering the United


  11
      Testimony from the suppression hearing in this case suggests that
remote and/or intensive searches of electronic devices crossing the border
do not occur all that often. For example, the computer specialist who
conducted the forensic search of Cotterman’s laptop testified that the
search was the first one he was asked to conduct in his 18 months on the
job at the Tucson computer center. (He added that at his previous post at
San Francisco International Airport, forensic searches were done right at
the airport.) Similarly, one of the border agents testified that this was the
first case he was aware of in which electronic devices were turned over to
Immigrations and Customs Enforcement for forensic examination, and
that even cursory reviews of laptops for information about illegal drug
trading occurred “no more than five” times during agent’s three-plus years
at the Lukeville border station. See Michael Chertoff, Secretary of
Homeland Security, Searches Are Legal, Essential, USA Today, July 16,
2008 (“Of the approximately 400 million travelers who entered the
country last year, only a tiny percentage were referred to secondary
baggage inspection for a more thorough examination. Of those, only a
fraction had electronic devices that may have been checked.”).
                UNITED STATES V . COTTERMAN                          51

States. See Robinette, 519 U.S. at 39 (“[W]e have
consistently eschewed bright-line rules, instead emphasizing
the fact-specific nature of the reasonableness inquiry.”); see
also Lyng v. Nw. Indian Cemetery Protective Ass’n, 485 U.S.
439, 445 (1988) (“A fundamental and longstanding principle
of judicial restraint requires that courts avoid reaching
constitutional questions in advance of the necessity of
deciding them.”).

    Moreover, border agents are not free to undertake
“unfettered crime-fighting searches or an unregulated assault
on citizens’ private information.” Majority at 26. As I
explained in my concurrence in Seljan, Congress and the
Executive Branch have (and have exercised) the authority to
restrict when and how border agents conduct searches. See
Seljan, 547 F.3d at 1012 (Callahan, J., concurring) (citing,
e.g., 19 U.S.C. § 1583; 19 C.F.R. § 145.3(b)-(c)); see also
Yule Kim, Cong. Research Serv. RL34404, Border Searches
of Laptop Computers and Other Electronic Storage Devices,
13–14 (2009) (describing recent legislative proposals to limit
border searches of electronic devices). In a similar vein,
Justice Breyer has noted that “Customs keeps track of the
border searches its agents conduct, including the reasons for
the searches. This administrative process should help
minimize concerns that [border] searches might be
undertaken in an abusive manner.” Flores-Montano,
541 U.S. at 156 (Breyer, J., concurring) (internal citation
omitted).12



 12
   See also U.S. Customs & Border Protection, Directive No. 3340-049,
Border Search of Electronic Devices Containing Information, 3–9 (2009)
(describing procedures for, and limits on, border searches of electronic
devices).
52             UNITED STATES V . COTTERMAN

    Apart from being unnecessary, the majority’s new limits
on the government’s border search authority will make it
much harder for border agents to do their jobs, for at least two
reasons. First, it is common knowledge that border agents at
security checkpoints conduct more thorough searches not
simply of those persons who arouse suspicion but also of a
percentage of travelers on a random basis. Otherwise, a
person who appears entirely innocent will have nothing to
fear and will not be deterred from carrying something that
should not be brought into the country. A checkpoint limited
to searches that can be justified by articulable grounds for
“reasonable suspicion” is bound to be less effective.

    Second, courtesy of the majority’s decision, criminals
now know they can hide their child pornography or terrorist
connections in the recesses of their electronic devices, while
border agents, fearing Fourth Amendment or Bivens actions,
will avoid conducting the searches that could find those
illegal articles. The result will be that people and things we
wish to keep out of our country will get in—a result hardly in
keeping with our “inherent authority to protect, and a
paramount interest in protecting,” the “territorial integrity” of
the United States. Flores-Montano, 541 U.S. at 153. The
border search doctrine must account for the fact that border
agents may need time and forensics to bypass “evasive
actions” a criminal has taken to hide contraband or other
illegal articles from plain view. Montoya de Hernandez,
473 U.S. at 542–43. I would rather leave those difficult
decisions “to the discretion of the officers in the field who
confront myriad circumstances we can only begin to imagine
from the relative safety of our chambers.” United States v.
                 UNITED STATES V . COTTERMAN                           53

Williams, 419 F.3d 1029, 1034 (9th Cir.), cert. denied,
546 U.S. 1081 (2005).13

                                   IV.

    The border search exception to the Fourth Amendment
may be just that—an exception—but it is, and must be, a
mighty one. The government’s right and duty to protect our
nation’s territorial integrity demand that the government have
clear authority to exclude—and thus to find—those people
and things we have decided are offensive, threatening, or
otherwise unwanted. Recognizing this, the Supreme Court
has only once required reasonable suspicion for border
searches in the 125 years it has been reviewing them. In the
remaining cases, the Court has eschewed bright-line rules,
balancing tests, and sliding intrusiveness scales, alluding to
the possibility of, but never finding, a “particularly offensive”


 13
    The majority insists that reasonable suspicion is a “modest, workable
standard” that is applied in domestic stops of automobiles “and other
contexts,” and that still allows “agents to draw on their expertise and
experience.” Majority at 26, 27 n.14. The majority is wrong for at least
three reasons. First, in making this argument, the majority reveals that it
does not appreciate the crucial differences between domestic and border
searches, despite those differences being spelled out in a century of case
law. Those differences range from the legitimate expectation of privacy
that people have in their property to the constraints government officials
face in searching it. Second, a reasonable suspicion standard injects
unnecessary judicial review where previously it was absent. Third, just
because border agents could apply the reasonable suspicion standard does
not mean they are, or should be, constitutionally compelled to do so. See
Ickes, 393 F.3d at 507; cf. Seljan, 547 F.3d at 1011 (Callahan, J.
concurring) (explaining that requiring border agents to apply a First
Amendment exception to border searches “would require them to engage
in the sort of decision-making process that the Supreme Court wished to
avoid in sanctioning expansive border searches”).
54            UNITED STATES V . COTTERMAN

search. The fact that electronic devices can store large
amounts of private information, or that the government can
search them forensically, does not make a thorough search of
such devices “particularly offensive.” Rather, the Supreme
Court and this court have wisely avoided making the
reasonableness of a search turn on the nature of the property
being searched, for the many reasons discussed above. The
result has been a clear, well-understood, efficient, and
effective rule that border searches are per se reasonable.

    Regrettably the majority, dispensing with these well-
settled, sensible, and binding principles, lifts our anchor and
charts a course for muddy waters. Now border agents,
instead of knowing that they may search any and all property
that crosses the border for illegal articles, must ponder
whether their searches are sufficiently “comprehensive and
intrusive,” Majority at 17, to require reasonable suspicion,
and whether they have such suspicion. In most cases the
answer is going to be as clear as, well, mud. We’re due for
another course correction.



M. SMITH, Circuit Judge, dissenting, with whom CLIFTON
and CALLAHAN, Circuit Judges, join with respect to Part I:

    I respectfully dissent. Until today, federal courts have
consistently upheld suspicionless searches of electronic
storage devices at the border. See United States v. Arnold,
533 F.3d 1003, 1008 (9th Cir. 2008), cert. denied, 555 U.S.
1176 (2009) (“[R]easonable suspicion is not needed for
customs officials to search a laptop or other personal
electronic storage devices at the border.”); see also United
States v. Ickes, 393 F.3d 501, 507 (4th Cir. 2005) (no finding
              UNITED STATES V . COTTERMAN                   55

of reasonable suspicion required to search personal computers
and disks at border); United States v. Linarez-Delgado,
259 Fed. Appx. 506, 508 (3d Cir. 2007); United States v.
McAuley, 563 F. Supp. 2d 672, 677–78 (W.D. Tex. 2008);
United States v. Bunty, 617 F. Supp. 2d 359, 365 (E.D. Pa.
2008). Yet the majority ignores these cases, rewrites long
standing Fourth Amendment jurisprudence, and, in narrowing
Arnold, creates a circuit split.

    While I share some of the majority’s concerns about the
steady erosion of our personal privacy in this digital age, the
majority’s decision to create a reasonable suspicion
requirement for some property searches at the border so
muddies current border search doctrine that border agents will
be left to divine on an ad hoc basis whether a property search
is sufficiently “comprehensive and intrusive” to require
reasonable suspicion, or sufficiently “unintrusive” to come
within the traditional border search exception. Requiring
border patrol agents to determine that reasonable suspicion
exists prior to performing a basic forensic examination of a
laptop or other electronic devices discourages such searches,
leaving our borders open to electronically savvy terrorists and
criminals who may hereafter carry their equipment and data
across our borders with little fear of detection. In fact, the
majority opinion makes such a legal bouillabaisse out of the
previously unambiguous border search doctrine, that I
sincerely hope the Supreme Court will grant certiorari, and
reverse the holding in this case regarding the level of
suspicion necessary to search electronic devices at the border,
for the sake of our national security, and the consistency of
our national border search law.

   The Supreme Court rejected our last attempt to narrow the
border search exception, cautioning us not to create “complex
56            UNITED STATES V . COTTERMAN

balancing tests” for border searches of property except in the
rarest of cases, where the search is “so destructive as to
require” reasonable suspicion. United States v. Flores-
Montano, 541 U.S. 149, 152, 156 (2004) (rejecting our
proposed reasonable suspicion requirement in United States
v. Molina-Tarazon, 279 F.3d 709, 713–17 (9th Cir. 2002)).
“Time and again” the Court has concluded that border
searches are “‘reasonable simply by virtue of the fact that
they occur at the border.’” Id. at 152–53 (quoting United
States v. Ramsey, 431 U.S. 606, 616 (1977)).

    Despite the Court’s clear ruling on the issue, the majority
again seeks to whittle away at the border search exception,
this time by conjuring a reasonable suspicion requirement for
border searches that employ computer software to search an
electronic storage device. Why the use of computer software
to analyze a hard drive triggers a reasonable suspicion
requirement while a “manual review” of the same hard drive
requires no suspicion, is left unexplained. Although
technology may serve as a useful proxy for the intrusiveness
of a search today, in the future even cursory searches might
be more efficiently conducted by the use of such technology.
Under the majority’s reasonable suspicion standard,
individuals’ privacy rights are only as secure as the
sophistication of the government’s current search mechanism.

    Moreover, the task of distinguishing these
“comprehensive and intrusive” laptop searches from the
“unintrusive search” of a laptop affirmed in Arnold, 533 F.3d
at 1008, or the search of a private letter affirmed in United
States v. Seljan, 547 F.3d 993, 1003 (9th Cir. 2008) (en banc),
leaves border patrol officers with a difficult choice: either
protect our nation from those who mean us harm, or risk their
own jobs and livelihood in a Bivens action, or disciplinary
              UNITED STATES V . COTTERMAN                   57

proceedings. Apart from being administratively impractical,
the majority’s reasonable suspicion requirement disregards
well established border search jurisprudence, and undermines
vital national security interests. Ironically, the majority did
not even need to consider the border search doctrine in this
case because the search at issue in this case did not occur at
the border.

    Separately, but importantly, the majority’s application of
the reasonable suspicion requirement to Cotterman is also
troubling. The majority purports to be concerned with
travelers’ “personal privacy and dignity,” but its
determination that reasonable suspicion exists under the
exceedingly weak facts of this case undermines the liberties
of U.S. citizens generally—not just at the border, and not just
with regard to our digital data—but on every street corner, in
every vehicle, and wherever else we rely on the doctrine of
reasonable suspicion to safeguard our legitimate privacy
interests.

I. The Border Search Doctrine

    The majority heralds this as a “watershed” case that
requires a narrowing of the border search exception to
accommodate the privacy interests allegedly created by new
technologies. Yet despite the majority’s attempts to avoid the
fact, the border search exception is clear and inflexible. The
Supreme Court has repeatedly affirmed the breadth of the
border search doctrine, extending a reasonable suspicion
requirement only to: (1) “highly intrusive searches of the
person”; (2) “searches of property [that] are so destructive as
to require” reasonable suspicion; and (3) searches carried out
in a “particularly offensive manner”—of which the Court has
yet to find an example. Flores-Montano, 541 U.S. at 152,
58            UNITED STATES V . COTTERMAN

154 n.2, 156 (quotations and citations omitted) (emphasis
added).

    The majority misconstrues these narrowly-defined
exceptions, reading Flores-Montano to require reasonable
suspicion whenever a search of property is deemed “overly
intrusive.” Majority at 18–19. Yet, the exceptions articulated
in Flores-Montano are far more circumscribed—applying not
to “overly intrusive” searches of property, like the search of
Cotterman’s computer, but only to “highly intrusive searches
of the person.” Flores-Montano, 541 U.S. at 152 (emphasis
added). The majority’s adoption of a reasonable suspicion
requirement to “comprehensive forensic examination[s]” of
property is irreconcilable with Flores-Montano. Majority at
6.

    We have consistently rejected a reasonable suspicion
requirement for border searches of expressive materials, such
as papers and their modern-day equivalent—the data
contained on electronic storage devices. See, e.g., Seljan,
547 F.3d at 1003 (“An envelope containing personal
correspondence is not uniquely protected from search at the
border.”); Arnold, 533 F.3d at 1008 (“[R]easonable suspicion
is not needed for customs officials to search a laptop or other
personal electronic storage devices at the border.”). The
majority states that its en banc decision narrows Arnold to
permit only “relatively simple” border searches of laptops,
and “not to countenance suspicionless forensic
examinations.” Majority at 14 n.6. In narrowing Arnold,
however, the court creates a circuit split regarding the
application of reasonable suspicion to border searches of
electronic devices. See United States v. Ickes, 393 F.3d 501
(4th Cir. 2005); see also United States v. Linarez-Delgado,
259 Fed. Appx. 506, 508 (3d Cir. 2007).
              UNITED STATES V . COTTERMAN                  59

    For instance, in Ickes (as in Arnold) the defendant-
appellant argued that a reasonable suspicion requirement was
necessary for laptop searches at the border because otherwise
“any person carrying a laptop computer [] on an international
flight would be subject to a search of the files on the
computer hard drive.” Ickes, 393 F.3d at 506–07. The Fourth
Circuit rejected this argument, noting that

       “[a]s a practical matter, computer searches are
       most likely to occur where—as here—the
       traveler’s conduct or the presence of other
       items in his possession suggest the need to
       search further.      However, to state the
       probability that reasonable suspicions will
       give rise to more intrusive searches is a far
       cry from enthroning this notion as a matter of
       constitutional law. The essence of border
       search doctrine is a reliance upon the trained
       observations and judgments of customs
       officials, rather than upon constitutional
       requirements applied to the inapposite context
       of this sort of search.”

Id. at 507 (emphasis added). The Third Circuit similarly
rejected a reasonable suspicion requirement for border
searches of electronic data, albeit in an unpublished opinion.
See United States v. Linarez-Delgado, 259 Fed. Appx. 506,
508 (3d Cir. 2007) (“Data storage media and electronic
equipment, such as films, computer devices, and videotapes,
may be inspected and viewed during a reasonable border
search.”) (citing Ickes, 393 F.3d 501). Because the majority
has narrowed our holding in Arnold that “reasonable
suspicion is not needed for customs officials to search a
laptop or other personal electronic storage devices at the
60             UNITED STATES V . COTTERMAN

border,” Arnold, 533 F.3d at 1008, the Ninth Circuit stands
alone, as it so often does.

    The majority likens the search of Cotterman’s laptop to a
“computer strip search,” Majority at 25, and proceeds to
conflate the law regarding property searches with that
regarding “highly intrusive searches of the person.” Flores-
Montano, 541 U.S. at 152. However, the “reasons that might
support a requirement of some level of suspicion in the case
of highly intrusive searches of the person—dignity and
privacy interests of the person being searched—simply do not
carry over” to laptops, which know no dignity or shame, and
thus have neither of those interests. Flores-Montano,
541 U.S. at 152 (emphasis added). Moreover, even genuine
strip searches do not necessarily require reasonable suspicion
at the border. See United States v. Montoya de Hernandez,
473 U.S. 531, 541 n.4 (1985) (expressly declining to decide
“what level of suspicion, if any, is required for . . . strip, body
cavity, or involuntary x-ray searches”) (emphasis added).

    The majority’s decision to insulate electronic storage
devices from the border search exception unsettles the border
search doctrine, places inappropriate burdens on law
enforcement, reduces deterrence, and raises serious national
security concerns. It also ignores the realities of electronic
data transmission and the reduced privacy expectations that
accompany much of this data, particularly at the border where
“[t]he government’s interest in preventing the entry of
unwanted persons and effects is at its zenith.” Flores-
Montano, 541 U.S. at 152.
               UNITED STATES V . COTTERMAN                    61

    A. Burdens on Law Enforcement

    The majority’s holding cripples law enforcement at the
border by depriving border patrol agents of the clear
administrative guidance they need to carry out core law
enforcement activities. “Officers who interact with those
suspected of violating the law have an essential interest in
readily administrable rules.” Florence v. Bd. of Chosen
Freeholders of Cnty. of Burlington, 132 S. Ct. 1510, 1522
(2012). Yet the majority’s holding requires border patrol
agents to determine on a case-by-case and moment-by-
moment basis whether a search of digital data remains
“unintrusive,” a la Arnold, or has become “comprehensive
and intrusive,” a la Cotterman. Majority at 14, 17.
Requiring law enforcement to make such complex legal
determinations on the spot, and in the face of potentially
grave national security threats, strips agents of their necessary
discretion and deprives them of an efficient and administrable
rule.

    The majority dismisses the burden its reasonable
suspicion requirement places on law enforcement, asserting
that agents can simply “draw on their expertise and
experience” to make the necessary judgment calls. Majority
at 26. Yet rather than actually deferring to this expertise and
experience, the majority forces border patrol agents to justify
their decisions under a heightened standard that has never
before been applied to border searches of property.

    Border patrol agents process hundreds of thousands of
travelers each day and conduct thousands of searches on
62             UNITED STATES V . COTTERMAN

electronic devices each year.1 Identifying national security
and criminal threats at the border requires a high level of
experience and discretion in order to recognize and respond
to the ever-changing tactics of those who seek to enter our
country with nefarious intent. In recognition of these crucial
interests, the border search exception provides law
enforcement with broad discretion to conduct border searches
of property without resorting to case-by-case determinations
of reasonable suspicion—determinations border patrol agents
are ill-equipped to handle. See generally Florence, 132 S. Ct.
at 1522 (rejecting reasonable suspicion requirement for prison
strip-searches under this rationale). Moreover, as a practical
matter, suspicionless border searches of property make sense,
in light of the sheer number of individuals crossing the border
with electronic devices each day. See United States v.
Martinez-Fuerte, 428 U.S. 543, 557 (1976) (requiring
reasonable suspicion for vehicle checkpoints near the
Mexican border “would be impractical because the flow of
traffic tends to be too heavy to allow the particularized study
of a given car”). Given these realities of law enforcement at
the border, a reasonable suspicion requirement for all “overly
intrusive” electronic searches is simply not practicable.

     B. National Security Concerns

    The majority’s decision to insulate electronic devices
from search at the border creates serious national security
concerns. An “ever present threat exists from the potential
for terrorists to employ the same smuggling and
transportation networks, infrastructure, drop houses, and
other support” as other illegal aliens. U.S. Customs and

 1
   Department of Homeland Security Privacy Office, Annual Report to
Congress 54 (2009).
                 UNITED STATES V . COTTERMAN                          63

Border Protection, National Border Patrol Strategy 5 (2005).
The Department of Homeland Security has found that border
searches of electronic storage devices are “essential” for
“detect[ing] evidence relating to terrorism and other national
security matters.”2 Terrorists rely on electronic storage
devices, for example, to copy and alter passports and other
travel documents.3 By providing special privacy protections
for electronic devices at the border, the majority eliminates
the powerful deterrent of suspicionless searches and
significantly aids technologically savvy terrorists and
criminals who rely on encryption and other surreptitious
forms of data storage in their efforts to do harm. See
Martinez-Fuerte, 428 U.S. at 557 (rejecting reasonable
suspicion requirement for vehicle checkpoints near the
Mexican border because to hold otherwise “would largely
eliminate any deterrent to the conduct of well-disguised
smuggling operations”).

    The majority contends that the goal of deterrence does not
justify “any manner of intrusive search” at the border.
Majority at 26. Although I certainly agree with the majority
that a policy objective like deterrence cannot justify an
otherwise unconstitutional “highly intrusive search[] of the
person” at the border, Flores-Montano, 541 U.S. at 152, the
crucial role of deterrence cannot, and should not, be
understated. In fact, the Supreme Court recently affirmed the
importance of deterrence in upholding suspicionless strip


     2
   U.S. Customs and Border Protection, Border Search of Electronic
Devices Containing Information, CBP Directive No. 3340-049 § 1 (2009).

 3
   Thomas R. Eldridge, et al., 9/11 and Terrorist Travel: Staff Report of
the National Commission on Terrorist Attacks Upon the United States 60
(2004).
64            UNITED STATES V . COTTERMAN

searches—the apotheosis of an intrusive search. Florence,
132 S. Ct. at 1516 (rejecting reasonable suspicion
requirement for prison strip searches and reasoning that
“deterring the possession of contraband depends in part on
the ability to conduct searches without predictable
exceptions”). The suspicionless strip search upheld in
Florence, which included a close visual inspection of “the
buttocks or genital areas,” was unquestionably more intrusive
than the so-called “computer strip search” at issue here. Id.
at 1515.

    The majority contends that the deterrence function of
suspicionless searches will not be hampered by the
requirement of reasonable suspicion because, “as a matter of
commonsense and resources, it is only when reasonable
suspicion is aroused that such searches typically take place.”
Majority at 27 n.14. This is, of course, the very argument
rejected by the Fourth Circuit in Ickes. See Ickes, 393 F.3d at
507 (“As a practical matter, computer searches are most
likely to occur where—as here—the traveler’s conduct or the
presence of other items in his possession suggest the need to
search further. However, to state the probability that
reasonable suspicions will give rise to more intrusive
searches is a far cry from enthroning this notion as a matter
of constitutional law.”).

    In addition to undermining deterrence, a reasonable
suspicion requirement will likely disincentivize agents to
conduct laptop searches in close cases. See Florence, 132
S. Ct. at 1522 (“To avoid liability” if required to find
reasonable suspicion, “officers might be inclined not to
conduct a thorough search in any close case, thus creating
unnecessary risk for the entire jail population.”). Border
patrol agents accused of conducting an “unreasonable” search
                 UNITED STATES V . COTTERMAN                       65

face very real consequences—as federal officials, for
example, they may be sued in their individual capacities for
civil damages, as part of a Bivens4 action. See Ronald J.
Sievert, Meeting the Twenty-First Century Terrorist Threat
Within the Scope of Twentieth Century Constitutional Law,
37 Hous. L. Rev. 1421, 1424 (2000). The majority’s
reasonable suspicion requirement saddles border patrol agents
with a “Sophie’s choice” between securing our nation, and
protecting their own livelihoods. These misaligned incentives
create unnecessary risk, not just for a prison population, as in
Florence, 132 S. Ct. at 1522, but for our entire nation.

      C. Expectation of Privacy in Electronic Data at the
         Border

    The majority suggests that travelers at the border have a
heightened expectation of privacy in their electronic storage
devices, due to the “uniquely sensitive nature of [this] data.”
Majority at 25. There is no question that searches of
electronic data are protected by the Fourth Amendment, but
we have never found this data to be immune from the border
search exception. In fact, these electronic storage devices are
hardly a bastion of privacy. When connected to the Internet,
they transmit a massive amount of intimate data to the public
on an almost constant basis, rendering it unremarkable that
they can be searched at the border, where “[t]he government’s
interest in preventing the entry of unwanted persons and
effects is at its zenith.” Flores-Montano, 541 U.S. at 152.

    Indeed, Facebook, for example, now has more than 500
million users, who share

[...TRUNCATED 30934 of 150934 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/United States v. Crews.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Crews"
type: case
citation: "445 U.S. 463 (1980)"
parallel_cite: "100 S. Ct. 1244; 63 L. Ed. 2d 537"
neutral_cite: 1980 U.S. LEXIS 1293
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-03-25
docket: 78-777
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Crews
  varies_by_point: false
  scope_note: "The independent-source analysis of an in-court identification, and the rule that a defendant's presence is not a suppressible fruit, remain good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110230/united-states-v-crews/"
  cluster_id: 110230
  opinion_id: 9427838
  identity_checked: true
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Key — Progeny (independent source)"
  - page: "[[Eyewitness Identification]]"
    role: "Related (cross-doctrine)"
related: ["[[Wong Sun v. United States]]", "[[Silverthorne Lumber Co. v. United States]]", "[[United States v. Wade]]", "[[Stovall v. Denno]]", "[[United States v. Ceccolini]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "independent-source", "eyewitness-identification"]
holding: "A victim's in-court identification of the accused is not a suppressible fruit of his illegal arrest where the victim's presence and her ability to identify him have an independent source predating the police misconduct."
lake:
  record_id: United States v. Crews
  status: verified
  projected_at: 2026-07-09
---

# United States v. Crews

*445 U.S. 463 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A woman was robbed at gunpoint; she immediately notified police, gave a full description, and the next day voluntarily viewed photographs. Crews was later detained without probable cause, photographed while in custody, and the victim identified his photo and then him at a lineup. The pretrial photographic and lineup identifications were conceded to be suppressible fruits of the illegal arrest; the disputed question was whether the victim's identification of Crews at trial must also be suppressed.

## Issue
Whether a crime victim's in-court identification of the accused must be suppressed as a fruit of the defendant's unlawful arrest.

## Rule
No, where the identification's components have an [[Inevitable Discovery and Independent Source|independent source]] that antedates the illegality. "A victim's in-court identification of the accused has three distinct elements" — the victim's presence to testify, her ability to reconstruct the crime and identify the defendant, and the defendant's own physical presence in the courtroom — and on these facts "none of these three elements 'has been come at by exploitation' of the violation of the defendant's Fourth Amendment rights." — 445 U.S. at 471 (quoting *Wong Sun v. United States*, 371 U.S. 471, 488). ^pin-471

## Application
Each element traced to a source independent of the illegal arrest. The victim's presence was "not traceable to any Fourth Amendment violation," because "the victim's identity was known long before there was any official misconduct." — *Id.* at 472. ^pin-472

Her capacity to identify rested on an independent recollection of the crime itself, uninfluenced by the suppressible pretrial procedures: "the victim's capacity to identify her assailant in court neither resulted from nor was biased by the unlawful police conduct committed long after she had developed that capacity." — *Id.* at 473. ^pin-473

As to the third element, the defendant could not "claim immunity from prosecution simply because his appearance in court was precipitated by an unlawful arrest." — [*Id.* at 474](https://www.courtlistener.com/opinion/110230/united-states-v-crews/#:~:text=claim%20immunity%20from%20prosecution%20simply). ^pin-474

## Conclusion
Because the in-court identification was not the product of the Fourth Amendment violation, it was not a suppressible fruit; the District of Columbia Court of Appeals was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Crews* applies the [[Wong Sun v. United States]] / [[Silverthorne Lumber Co. v. United States]] independent-source principle to identification evidence, and dovetails with the [[United States v. Wade]] / [[Stovall v. Denno]] independent-source test for an in-court identification following a tainted pretrial procedure.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny ([[Inevitable Discovery and Independent Source|independent source]])*
- [[Eyewitness Identification]] — *Related (cross-doctrine)*

## Sources
- *United States v. Crews*, 445 U.S. 463 (1980) — https://www.courtlistener.com/opinion/110230/united-states-v-crews/ — pinpoints: 471, 472, 473, 474.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2412ab579b992cf0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "445 U.S. 463 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 1293", "official_citation_present": true, "parallel_cite": "100 S. Ct. 1244; 63 L. Ed. 2d 537", "title": "United States v. Crews", "year": "1980"}}
{"assertion_id": "5bda9883eb3b2c41", "dimension": "support", "kind": "home_role", "locator": {"home": "Inevitable Discovery & Independent Source"}, "payload": {"home": "Inevitable Discovery & Independent Source", "role": "Key — Progeny (independent source)", "title": "United States v. Crews"}}
{"assertion_id": "5d2096ed8aba3dcc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A victim's in-court identification of the accused is not a suppressible fruit of his illegal arrest where the victim's presence and her ability to identify him have an independent source predating the police misconduct.", "title": "United States v. Crews"}}
{"assertion_id": "c539a6edd25faf08", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Related (cross-doctrine)", "title": "United States v. Crews"}}
{"assertion_id": "9b72ef883b60e865", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Crews"}}
{"assertion_id": "f0cee190096c8c30", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-03-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Crews", "field_i_validity": "good_law", "scope_note": "The independent-source analysis of an in-court identification, and the rule that a defendant's presence is not a suppressible fruit, remain good law.", "title": "United States v. Crews", "varies_by_point": "false"}}
```

### lake record — United States v. Crews

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Crews",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Crews",
    "case_name_short": "Crews",
    "case_name_full": "United States v. Crews",
    "input_case_name": "United States v. Crews",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-03-25",
    "year": 1980,
    "docket": "78-777",
    "cluster_id": 110230,
    "lead_opinion_id": 9427838,
    "sibling_ids": [
      110230,
      9427838,
      9427839,
      9427840
    ],
    "absolute_url": "/opinion/110230/united-states-v-crews/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "445 U.S. 463",
      "volume": "445",
      "reporter": "U.S.",
      "page": "463",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1244",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1244",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 537",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "537",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 1293",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "1293",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "445 U.S. 463",
        "volume": "445",
        "reporter": "U.S.",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1244",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1244",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 537",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "537",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 1293",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "1293",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "445 U.S. 463",
    "official_selection": {
      "court_class": "scotus",
      "selected": "445 U.S. 463",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-471",
      "page": null,
      "quote": "--- # United States v. Crews *445 U.S. 463 (1980)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A woman was robbed at gunpoint; she immediately notified police, gave a full description, and the next day voluntarily viewed photographs. Crews was later detained without probable cause, photographed while in custody, and the victim identified his photo and then him at a lineup. The pretrial photographic and lineup identifications were conceded to be suppressible fruits of the illegal arrest; the disputed question was whether the victim's identification of Crews at trial must also be suppressed. ## Issue Whether a crime victim's in-court identification of the accused must be suppressed as a fruit of the defendant's unlawful arrest. ## Rule No, where the identification's components have an independent source that antedates the illegality.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-472",
      "page": null,
      "quote": "not traceable to any Fourth Amendment violation,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-473",
      "page": null,
      "quote": "the victim's capacity to identify her assailant in court neither resulted from nor was biased by the unlawful police conduct committed long after she had developed that capacity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-474",
      "page": null,
      "quote": "claim immunity from prosecution simply because his appearance in court was precipitated by an unlawful arrest.",
      "star_marker": "474",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15824,
      "fragment": "#:~:text=claim%20immunity%20from%20prosecution%20simply",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Crews",
    "varies_by_point": false,
    "scope_note": "The independent-source analysis of an in-court identification, and the rule that a defendant's presence is not a suppressible fruit, remain good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Parker Chad Ross v. Commonwealth of Virginia",
          "cluster_id": 1061425,
          "cite": [
            "61 Va. App. 752",
            "739 S.E.2d 910",
            "2013 WL 1564533",
            "2013 Va. App. LEXIS 115"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Young v. Conway",
          "cluster_id": 810124,
          "cite": [
            "698 F.3d 69",
            "2012 U.S. App. LEXIS 21502",
            "2012 WL 4876235"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 5901088,
          "cite": [
            "53 A.D.3d 1151",
            "860 N.Y.S.2d 780"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 6356597,
          "cite": [
            "19 Misc. 3d 675"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Olivarez v. State",
          "cluster_id": 1560637,
          "cite": [
            "171 S.W.3d 283",
            "2005 WL 1385355"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Martin",
          "cluster_id": 6588047,
          "cite": [
            "63 Mass. App. Ct. 587",
            "827 N.E.2d 1263",
            "2005 Mass. App. LEXIS 489"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Henderson v. State",
          "cluster_id": 1745593,
          "cite": [
            "82 S.W.3d 750",
            "2002 WL 1590495"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leonard Henderson v. State",
          "cluster_id": 2920338,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Astuto",
          "cluster_id": 6173483,
          "cite": [
            "263 A.D.2d 459",
            "694 N.Y.S.2d 407",
            "1999 N.Y. App. Div. LEXIS 7765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. MacOn",
          "cluster_id": 111477,
          "cite": [
            "86 L. Ed. 2d 370",
            "105 S. Ct. 2778",
            "472 U.S. 463",
            "1985 U.S. LEXIS 110",
            "53 U.S.L.W. 4783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pablo Escoboza Vega",
          "cluster_id": 403767,
          "cite": [
            "678 F.2d 376",
            "1982 U.S. App. LEXIS 18982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Geisler",
          "cluster_id": 7894925,
          "cite": [
            "222 Conn. 672",
            "610 A.2d 1225",
            "61 U.S.L.W. 2093",
            "1992 Conn. LEXIS 214"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1377787,
          "cite": [
            "751 P.2d 395",
            "44 Cal. 3d 883",
            "245 Cal. Rptr. 336",
            "1988 Cal. LEXIS 74"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Henderson",
          "cluster_id": 1057155,
          "cite": [
            "2013 IL 114040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dodt",
          "cluster_id": 5686979,
          "cite": [
            "61 N.Y.2d 408",
            "462 N.E.2d 1159",
            "474 N.Y.S.2d 441",
            "1984 N.Y. LEXIS 4120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vanderbilt v. State",
          "cluster_id": 2459138,
          "cite": [
            "629 S.W.2d 709",
            "1981 Tex. Crim. App. LEXIS 1156"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thurman",
          "cluster_id": 1367765,
          "cite": [
            "846 P.2d 1256",
            "203 Utah Adv. Rep. 18",
            "1993 Utah LEXIS 40",
            "1993 WL 4794"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brnja",
          "cluster_id": 5684289,
          "cite": [
            "50 N.Y.2d 366",
            "406 N.E.2d 1066",
            "429 N.Y.S.2d 173",
            "1980 N.Y. LEXIS 2356"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fleming v. State",
          "cluster_id": 1702179,
          "cite": [
            "604 So. 2d 280",
            "1992 WL 132439"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Acosta-Colon",
          "cluster_id": 198134,
          "cite": [
            "157 F.3d 9",
            "1998 U.S. App. LEXIS 24862",
            "1998 WL 671324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Oliver L. North",
          "cluster_id": 552750,
          "cite": [
            "920 F.2d 940",
            "287 U.S. App. D.C. 146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daugherty",
          "cluster_id": 1777786,
          "cite": [
            "931 S.W.2d 268",
            "1996 Tex. Crim. App. LEXIS 88",
            "1996 WL 350804"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George Terzado-Madruga",
          "cluster_id": 537704,
          "cite": [
            "897 F.2d 1099",
            "1990 WL 27249"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powell v. Nevada",
          "cluster_id": 117833,
          "cite": [
            "128 L. Ed. 2d 1",
            "114 S. Ct. 1280",
            "511 U.S. 79",
            "1994 U.S. LEXIS 2655"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane3_recency"
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
        "journal_ref": "United States v. Crews:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110230 OR 9427838 OR 9427839 OR 9427840) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MjIwNjA4MDAwMDAmcz0xMTk5NjAxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110230+OR+9427838+OR+9427839+OR+9427840%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(110230 OR 9427838 OR 9427839 OR 9427840)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzAmcz01Njg2MTk2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110230+OR+9427838+OR+9427839+OR+9427840%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110230 OR 9427838 OR 9427839 OR 9427840)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 2,
        "triage_snippet_classified": 16
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110230 OR 9427838 OR 9427839 OR 9427840)",
    "indexed_citing_opinions": 738,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110230,
        "count": 643,
        "count_source": "search"
      },
      {
        "opinion_id": 9427838,
        "count": 111,
        "count_source": "search"
      },
      {
        "opinion_id": 9427839,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427840,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1155,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-crews.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5NDQwNyZzPTgyNDQ5NzEmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28110230+OR+9427838+OR+9427839+OR+9427840%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110230,
        "cited_id": 91772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 104977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 108639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 237954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 250068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 332396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 1920133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 2073438,
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
    "date_created": "2026-07-05T23:25:11Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:25:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:25:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:36:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:25:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Crews

```
<opinion type="majority">
<author id="b525-5">Mr. Justice Brennan</author>
<p id="AKJ">delivered the opinion of the Court, except as to Part II-D.</p>
<p id="b525-6">We are called upon to decide whether in the circumstances of this case an in-court identification of the accused by the victim of a crime should be suppressed as the fruit of the defendant’s unlawful arrest.</p>
<p id="b525-7">I</p>
<p id="b525-8">On the morning of January 3, 1974, a woman was accosted and robbed at gunpoint by a young man in the women’s restroom on the grounds of the Washington Monument. Her assailant, peering at her through a 4-inch crack between the wall and the door of the stall she occupied, asked for $10 and demanded that he be let into the stall. When the woman refused, the robber pointed a pistol over the top of the door and repeated his ultimatum. The victim then surrendered the money, but the youth demanded an additional $10. When the woman opened her purse and showed her assailant that she had no more cash, he gained entry to her stall and made sexual advances upon her. She tried to resist and pleaded with him to leave. He eventually did, warning his victim that he would shoot her if she did not wait at least 20 minutes before following him out of the restroom. The woman complied, and upon leaving the restroom 20 minutes later, immediately reported the incident to the police.</p>
<p id="b525-9">On January 6, two other women were assaulted and robbed in a similar episode in the same restroom. A young man threatened the women with a broken bottle, forced them to hand over $20, and then departed, again cautioning his victims not to leave for 20 minutes. The description of the <page-number citation-index="1" label="466">*466</page-number>robber given to the police by these women matched that given by the first victim: All three described their assailant as a young black male, 15-18 years old, approximately 5'5" to 5'8" tall, slender in build, with a very dark complexion and smooth skin.</p>
<p id="b526-5">Three days later, on January 9, Officer David Rayfield of the United States Park Police observed respondent in the area of the Washington Monument concession stand and restrooms. Aware of the robberies of the previous week and noting respondent’s resemblance to the police “lookout” that described the perpetrator, the officer and his partner approached respondent.<footnotemark>1</footnotemark> Respondent gave the officers his name and said that he was 16 years old. When asked why he was not in school, respondent replied that he had just “walked away from school.” <footnotemark>2</footnotemark> The officers informed respondent of his likeness to the suspect’s description, but there was no further questioning about those events. Respondent was allowed to leave, and the officers watched as he entered the nearby restrooms.</p>
<p id="b526-6">While respondent was still inside, Officer Rayfield saw and spoke to James Dickens, a tour guide who had previously reported having seen a young man hanging around the area of the Monument on the day of the January 3d robbery. In response to the officer’s request to observe respondent as he left the restroom, Dickens tentatively identified him as the individual he had seen on the day of the robbery.</p>
<p id="b526-7">On the basis of this additional information, the officers again approached respondent and detained him. Detective Earl Ore, the investigator assigned to the robberies, was immediately summoned. Upon his arrival some 10 or 15 minutes later, Detective Ore attempted to take a Polaroid photo<page-number citation-index="1" label="467">*467</page-number>graph of respondent, but the inclement weather conditions frustrated his several efforts to produce a picture suitable for display to the robbery victims. Respondent was therefore taken into custody, ostensibly because he was a suspected truant. He was then transported to Park Police headquarters, where the police briefly questioned him, obtained the desired photograph, telephoned his school, and released him. Respondent was never formally arrested or charged with any offense, and his detention at the station lasted no more than an hour.</p>
<p id="b527-5">On the following day, January 10, the police showed the victim of the first robbery an array of eight photographs, including one of respondent. Although she had previously viewed over 100 pictures of possible suspects without identifying any of them as her assailant, she immediately selected respondent’s photograph as that of the man who had robbed her. On January 13, one of the other victims made a similar identification.<footnotemark>3</footnotemark> Respondent was again taken into custody, and at a court-ordered lineup held on January 21, he was positively identified by the two women who had made the photographic identifications.</p>
<p id="b527-6">The grand jury returned an indictment against respondent on February 22, 1974, charging him with two counts of armed robbery, two counts of robbery, one count of attempted armed robbery, and three counts of assault with a dangerous weapon.<footnotemark>4</footnotemark> Respondent filed a pretrial motion to suppress all identification testimony, contending that his detention on the truancy charges had been merely a pretext to allow the police to obtain evidence for the robbery investigation. After hearing extensive testimony from the three victims, the police officers, and respondent, the trial court found that the respondent’s detention at Park Police headquarters on January 9 consti<page-number citation-index="1" label="468">*468</page-number>tuted an arrest without probable cause.<footnotemark>5</footnotemark> Accordingly, the court ruled that the products of that arrest — the photographic and lineup identifications — could not be introduced at trial. But the judge concluded that the victims’ ability to identify respondent in court was based upon independent recollection untainted by the intervening identifications, and therefore held such testimony admissible. At trial, all three victims identified respondent as their assailant. On April 23, the jury convicted him of armed robbery of the first victim, but returned verdicts of not guilty on all other charges.<footnotemark>6</footnotemark> Respondent was sentenced to four years’ probation under the Federal Youth Corrections Act, <span class="citation no-link">18 U. S. C. § 5010</span> (a).</p>
<p id="b528-5">On appeal, the District of Columbia Court of Appeals, sitting en banc, reversed respondent’s conviction and ordered the suppression of the first robbery victim’s in-court identi<page-number citation-index="1" label="469">*469</page-number>fication.<footnotemark>7</footnotemark> <span class="citation" data-id="9711085"><a href="/opinion/2073438/crews-v-united-states/" aria-description="Citation for case: Crews v. United States">389 A. 2d 277</a></span> (1978). The court viewed its decision to be a wholly conventional application of the familiar “fruit of the poisonous tree” doctrine. See <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963); <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920). After upholding the trial court’s finding that respondent was detained without probable cause — a determination that is not challenged in this Court<footnotemark>8</footnotemark> — the Court of Appeals turned to consideration of what evidentiary consequences ought to flow from that Fourth Amendment violation. In deciding whether the in-court identification should have been suppressed, the court observed that the analysis must focus on whether the evidence was obtained by official “exploitation” of the “primary illegality” within the meaning of <em>Wong <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Sun, supra,</a></span></em><footnotemark><em>9</em></footnotemark><em> </em>and that the principal issue was whether the unlawful police behavior bore a causal relationship to the acquisition of the challenged testimony. The court answered that question in the affirmative, reasoning that but for respondent’s unlawful arrest, the police would not have obtained the photograph that led to his subsequent identification by the complaining witnesses and, ultimately, prosecution of the case.<footnotemark>10</footnotemark> Satisfied that the <page-number citation-index="1" label="470">*470</page-number>in-court identification was thus at least indirectly the product of official misconduct, the court then considered whether any of three commonly advanced exceptions to the exclusionary rule — the “independent source,” “inevitable discovery,” or “attentuation” doctrines<footnotemark>11</footnotemark> — nonetheless justified its admission. Finding these exceptions inapplicable, the Court of Appeals concluded that, the in-court identification testimony should have been excluded as a product of the violation of respondent’s Fourth Amendment rights. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./440/907/">440 U. S. 907</a></span> (1979). We reverse.</p>
<p id="b530-5">II</p>
<p id="b530-6"><em>Wong <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Sun, supra,</a></span> </em>articulated the guiding principle for determining whether evidence derivatively obtained from a violation of the Fourth Amendment is admissible against the accused at trial: “The exclusionary prohibition extends as well to the indirect as the direct products of such invasions.” <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 484</a></span>. See <em>Silverthome Lumber Co. </em>v. <em>United States, supra; Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914). As subsequent cases have confirmed, the exclusionary sanction applies to any “fruits” of a constitutional violation — whether such evidence be tangible, physical material actually seized in an illegal search,<footnotemark>12</footnotemark> items observed or words overheard in the course of the unlawful activity,<footnotemark>13</footnotemark> or confessions or statements of the accused obtained during an illegal arrest and detention.<footnotemark>14</footnotemark></p>
<p id="b531-4"><page-number citation-index="1" label="471">*471</page-number>In the typical “fruit of the poisonous tree” case, however, the challenged evidence was acquired by the police <em>after </em>some initial Fourth Amendment violation, and the question before the court is whether the chain of causation proceeding from the unlawful conduct has become so attenuated or has been interrupted by some intervening circumstance so as to remove the “taint” imposed upon that evidence by the original illegality. Thus most cases begin with the premise that the challenged evidence is in some sense the product of illegal governmental activity. It is the Court of Appeals’ application of that premise to the facts of this case that we find erroneous.</p>
<p id="b531-5">A ,victim’s in-court identification of the accused has three distinct elements. First, the victim is present at trial to testify as to what transpired between her and the offender, and to identify the defendant as the culprit. Second, the victim possesses knowledge of and the ability to reconstruct the prior criminal occurrence and to identify the defendant from her observations of him at the time of the crime. And third, the defendant is also physically present in the courtroom, so that the victim can observe him and compare his appearance to that of the offender. In the present case, it is our conclusion that none of these three elements “has been come at by exploitation” of the violation of the defendant’s Fourth Amendment rights. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States"><em>Wong Sun, supra, </em>at 488</a></span>.</p>
<p id="b531-6">A</p>
<p id="b531-7">In this case, the robbery victim’s presence in the courtroom at respondent’s trial was surely not the product of any police misconduct. She had notified the authorities immediately after the attack and had given them a full description of her assailant. The very next day, she went to the police station to view photographs of possible suspects, and she voluntarily assisted the police in their investigation at all times. Thus this is not a case in which the witness’ identity was discovered or her cooperation secured only as a result of an unlawful <page-number citation-index="1" label="472">*472</page-number>search or arrest of the accused.<footnotemark>15</footnotemark> Here the victim’s identity was known long before there was any official misconduct, and her presence in court is thus not traceable to any Fourth Amendment violation.</p>
<p id="b532-5">B</p>
<p id="b532-6">Nor did the illegal arrest infect the victim’s ability to give accurate identification testimony. Based upon her observations at the time of the robbery, the victim constructed a mental image of her assailant. At trial, she retrieved this mnemonic representation, compared it to the figure of the defendant, and positively identified him as the robber.<footnotemark>16</footnotemark> No part of this process was affected by respondent’s illegal arrest. In the language of the “time-worn metaphor” of the poisonous tree, <em>Harrison </em>v. <em>United </em>States, <span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/#222" aria-description="Citation for case: Harrison v. United States">392 U. S. 219, 222</a></span> (1968), the toxin in this case was injected only after the evidentiary bud had blossomed; the fruit served at trial was not poisoned.</p>
<p id="b532-7">This is not to say that the intervening photographic and lineup identifications — both of which are conceded to be suppressible fruits of the Fourth Amendment violation — could not under some circumstances affect the reliability of the in-court identification and render it inadmissible as well. Indeed, given the vagaries of human memory and the inherent suggestibility of many identification procedures,<footnotemark>17</footnotemark> just <page-number citation-index="1" label="473">*473</page-number>the opposite may be true. But in the present case the trial court expressly found that the witness’ courtroom identification rested on an independent recollection of her initial encounter with the assailant, uninfluenced by the pretrial identifications, and this determination finds ample support in the record.<footnotemark>18</footnotemark> In short, the victim’s capacity to identify her assailant in court neither resulted from nor was biased by the unlawful police conduct committed long after she had developed that capacity.<footnotemark>19</footnotemark></p>
<p id="b534-3"><page-number citation-index="1" label="474">*474</page-number>c</p>
<p id="b534-4">Insofar as respondent challenges his own presence at trial, he cannot claim immunity from prosecution simply because his appearance in court was precipitated by an unlawful arrest. An illegal arrest, without more, has never been viewed as a bar to subsequent prosecution, nor as a defense to a valid conviction. <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 119</a></span> (1975); <em>Frisbie </em>v. <em>Collins, </em><span class="citation" data-id="104977"><a href="/opinion/104977/frisbie-v-collins/" aria-description="Citation for case: Frisbie v. Collins">342 U. S. 519</a></span> (1952); <em>Ker </em>v. <em>Illinois, </em><span class="citation" data-id="91772"><a href="/opinion/91772/ker-v-illinois/" aria-description="Citation for case: Ker v. Illinois">119 U. S. 436</a></span> (1886).<footnotemark>20</footnotemark> The exclusionary principle of <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>and <em>Silverthorne Lumber Co. </em>delimits what proof the Government may offer against the accused at trial, closing the courtroom door to evidence secured by official lawlessness. Respondent is not himself a suppressible “fruit,” and the illegality of his detention cannot deprive the Government of the opportunity to prove his guilt through the introduction of evidence wholly untainted by the police misconduct.</p>
<p id="b534-5">D<footnotemark>*</footnotemark></p>
<p id="b534-6">Respondent argues, however, that in one respect his corpus is itself a species of “evidence.” When the victim singles out respondent and declares, “That’s the man who robbed me,” his physiognomy becomes something of evidentary value, much like a photograph showing respondent at the scene of the <page-number citation-index="1" label="475">*475</page-number>crime.<footnotemark>21</footnotemark> And, as with, the introduction of such a photograph, he contends that the crucial inquiry for Fourth Amendment purposes is whether that evidence has become available only as a result of official misconduct. We read the Court of Appeals’ opinion as essentially adopting this analysis to support its suppression order. See <span class="citation" data-id="9711085"><a href="/opinion/2073438/crews-v-united-states/#285" aria-description="Citation for case: Crews v. United States">389 A. 2d, at 285-287</a></span>.</p>
<p id="b535-5">We need not decide whether respondent’s person should be considered evidence, and therefore a possible “fruit” of police misconduct. For in this case the record plainly discloses that prior to his illegal arrest, the police both knew respondent’s identity and had some basis to suspect his involvement in the very crimes with which he was charged. Moreover, before they approached respondent, the police had already obtained access to the “evidence” that implicated him in the robberies, <em>i. e., </em>the mnemonic representations of the criminal retained by the victims and related to the police in the form of their agreement upon his description. In short, the Fourth Amendment violation in this case yielded nothing of evidentiary value that the police did not already have in their grasp.<footnotemark>22</footnotemark> Rather, respondent’s unlawful arrest served merely to link together two extant ingredients in his identification. The exclusionary rule enjoins the Government from benefiting from evidence it has unlawfully obtained; it does not reach backward to taint information that was in official hands prior to any illegality.</p>
<p id="b535-6">Accordingly, this case is very different from one like <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), in which the defendant’s identity and connection to the illicit activity were only first discovered through an illegal arrest or search. In that case, the defendant’s fingerprints were ordered suppressed as the <page-number citation-index="1" label="476">*476</page-number>fruits of an unlawful detention. A woman had been raped in her home, and during the next 10 days, the local police rounded up scores of black youths, randomly stopping, interrogating, and fingerprinting them. Davis’ prints were discovered to match a set found at the scene of the crime, and on that basis he was arrested and convicted. Had it not been for Davis’ illegal detention, however, his prints would not have been obtained and he would never have become a suspect.' Here, in contrast, the robbery investigation had already focused on respondent, and the police had independent reasonable grounds to suspect his culpability.</p>
<p id="b536-5">We find <em>Bynum </em>v. <em>United States, </em>104 U. S. App. D. C. 368, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d 465</a></span> (1958), cited with approval in <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#724" aria-description="Citation for case: Davis v. Mississippi"><em>Davis, supra, </em>at 724</a></span>, helpful in our analysis as well. In <em><span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">Bynum</a></span>, </em>the defendant voluntarily came down to the police station to look for his brother, who had been arrested earlier that day while driving an auto sought in connection with a robbery. After telling one of the officers that he owned the car, Bynum was arrested and fingerprinted. Those prints were later found to match a set at the scene of the robbery, and Bynum was convicted based in part on that evidence. The Court of Appeals held that the police lacked probable cause at the time of Bynum’s arrest, and it ordered the prints suppressed as “something of evidentiary value which the public authorities have caused an arrested person to yield to them during illegal detention.” 104 U. S. App. D. C., at 370, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#467" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d, at 467</a></span>. As this Court noted in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>, </em>however, <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#725" aria-description="Citation for case: Davis v. Mississippi">394 U. S., at 725-726, n. 4</a></span>, Bynum was subsequently reindicted for the same offense, and the Government on retrial introduced an older set of his fingerprints, taken from an FBI file, that were in no' way connected with his unlawful arrest. The Court of Appeals affirmed that conviction, holding that the fingerprint identification made on the basis of information already in the FBI’s possession was not tainted by the subsequent illegality and was therefore admissible. <em>Bynum </em>v. <em>United States, </em>107 U. S. App. D. C. 109, <span class="citation" data-id="250068"><a href="/opinion/250068/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">274 F. 2d 767</a></span> (1960).</p>
<p id="b537-4"><page-number citation-index="1" label="477">*477</page-number>The parallels between <em>Bynum </em>and this case are apparent: The pretrial identification obtained through use of the photograph taken during respondent’s illegal detention cannot be <em>introduced; </em>but the in-court identification is admissible, even if respondent’s argument be accepted, because the police’s knowledge of respondent’s identity and the victim’s independent recollections of him both antedated the unlawful arrest and were thus untainted by the constitutional violation. The judgment of the Court of Appeals is accordingly</p>
<p id="b537-5">
<em>Reversed.</em>
</p>
<judges id="b537-6">Mr. Justice Marshall took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b526-8"> Officer Rayfield testified that his suspicions were further aroused both by respondent’s presence on the almost deserted park grounds and by his apparently aimless meanderings around the restroom and concessions area.</p>
</footnote>
<footnote label="2">
<p id="b526-9"><em> </em>Tr. 52. References are to the transcript of the suppression hearing and trial held on April 22 and 23, 1974, in the Superior Court of the District of Columbia.</p>
</footnote>
<footnote label="3">
<p id="b527-7"> The third victim did not review the photographic array, nor did she attend the subsequent lineup.</p>
</footnote>
<footnote label="4">
<p id="b527-8"> See D. C. Code §§ 22-502, 22-2901, and 22-3202 (1973).</p>
</footnote>
<footnote label="5">
<p id="b528-6"> The suppression hearing produced conflicting testimony as to the reasons for the attempt to photograph respondent. Officer Rayfield asserted that respondent was processed as a routine juvenile truant, a procedure that involves photographing the suspect and then calling his school and home to determine whether he is in fact truant. Tr. 53-54. Rayfield did acknowledge, however, that he had some suspicion that respondent was the robber described in the police description. <em>Id., </em>at 55, 57. Similarly, Detective Ore, while maintaining that respondent was apprehended and taken down to Park Police headquarters as a suspected truant, <em>id., </em>at 61, 63, admitted that his intent in trying to photograph him was to obtain a picture that could be shown to the complaining witnesses. <em>Id., </em>at 59.</p>
<p id="b528-7">The Government does not now attempt to justify respondent’s detention on the truancy charge, nor did it raise that argument in the court below. The Court of Appeals found that the procedures followed in respondent’s case did not conform to the typical truancy practices described by the police and that the officers never even superficially pursued the truancy matter. By the same token, the court expressly disavowed the existence of a “sham” or “pretext” arrest, and it analyzed respondent’s apprehension as a traditional arrest for armed robbery and assault without probable cause. <span class="citation" data-id="9711085"><a href="/opinion/2073438/crews-v-united-states/#299" aria-description="Citation for case: Crews v. United States">389 A. 2d 277, 299-300, n. 32</a></span> (DC 1978).</p>
</footnote>
<footnote label="6">
<p id="b528-8"> Because respondent was acquitted of all charges in connection with the robberies of January 6, the only issue raised on his appeal was the admissibility of the first robbery victim’s in-court identification.</p>
</footnote>
<footnote label="7">
<p id="b529-5"> On February 16, 1977, a division of the Court of Appeals originally affirmed respondent’s conviction, <span class="citation" data-id="9695751"><a href="/opinion/1920133/crews-v-united-states/" aria-description="Citation for case: Crews v. United States">369 A. 2d 1063</a></span>. Three months later, however, the full court granted respondent’s motion for rehearing and vacated its earlier judgment. Record 356.</p>
</footnote>
<footnote label="8">
<p id="b529-6"> See Brief for United States 5, n. 4.</p>
</footnote>
<footnote label="9">
<p id="b529-7"> “We need not hold that all evidence is ‘fruit of the poisonous tree’ simply because it would not have come to light but for the illegal actions of the police. Rather, the more apt question in such a ease is 'whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.’ Maguire, Evidence of Guilt, 221 (1959).” <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 487-488</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b529-8"> “[T]he unlawful arrest produced photographs which were shown to the complaining witnesses who, as a result, identified [respondent); this resulted in his reapprehension, which yielded a court-ordered lineup iden<page-number citation-index="1" label="470">*470</page-number>tification and, eventually, in-court identification testimony during prosecution of the case.” <span class="citation" data-id="9711085"><a href="/opinion/2073438/crews-v-united-states/#289" aria-description="Citation for case: Crews v. United States">389 A. 2d, at 289</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b530-8"> See <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939) (attenuation); <em>Silverthome Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920) (independent source); <em>United States ex rel. Owens </em>v. <em>Twomey, </em><span class="citation" data-id="324383"><a href="/opinion/324383/united-states-of-america-ex-rel-jesse-owens-v-john-j-twomey-warden/#865" aria-description="Citation for case: United States of America Ex Rel. Jesse Owens v. John J....">508 F. 2d 858, 865</a></span> (CA7 1974) (inevitable discovery).</p>
</footnote>
<footnote label="12">
<p id="b530-9"> <em>E. g., Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971); <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968); <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964).</p>
</footnote>
<footnote label="13">
<p id="b530-10"> <em>E. g., United States </em>v. <em>Giordano, </em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">416 U. S. 505</a></span> (1974).; see <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961); <em>McGinnis </em>v. <em>United States, </em><span class="citation" data-id="6912304"><a href="/opinion/7011844/mcginnis-v-united-states/" aria-description="Citation for case: McGinnis v. United States">227 F. 2d 598</a></span> (CA1 1955).</p>
</footnote>
<footnote label="14">
<p id="b530-11"> <em>E. g., Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979); <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975).</p>
</footnote>
<footnote label="15">
<p id="b532-8"> See generally Ruffin, Out on a Limb of the Poisonous Tree: The Tainted Witness, <span class="citation no-link">15 UCLA L. Rev. 32</span> (1967).</p>
</footnote>
<footnote label="16">
<p id="b532-9"> At oral argument, the Government compared the witness’ mental image to an undeveloped photograph of the robber that is given to the police immediately after the crime, but which becomes visible only at the trial. Tr. of Oral Arg. 11-12. Although this analogy may not comport precisely with current psychological theories of perception, see, <em>e. g., </em>Buckout, Eyewitness Testimony, Scientific American 23 (Dec. 1974), it is apt for purposes of analysis.</p>
</footnote>
<footnote label="17">
<p id="b532-10"> See, e. <em>g., </em>P. Wall, Eye-Witness Identification in Criminal Cases 40-64 (1965); Note,. Did Your Eyes Deceive You? Expert Psychological Testimony on the Unreliability of Eyewitness Identification, <span class="citation no-link">29 Stan. L. Rev. 969</span>, 974-989 (1977).</p>
</footnote>
<footnote label="18">
<p id="b533-5"> <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), enumerated several factors for consideration in applying the “independent origins” test. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#241" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 241</a></span>. Cf. <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U. S. 98</a></span> (1977); <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span> (1972). We attach particular significance to the following circumstances which support the trial court’s determination in this case: the victim viewed her assailant at close range for a period of 5-10 minutes under excellent lighting conditions and with no distractions, Tr. 4, 7, 111; respondent closely matched the description given by the victim immediately after the robbery, <em>id., </em>at 52, 59; the victim failed to identify anyone other than respondent, <em>id., </em>at 8, but twice selected respondent without hesitation in nonsuggestive pretrial identification procedures, <em>id., </em>at 9-11; and only a week had passed between the victim’s initial observation of respondent and her first identification of him, <em>id., </em>at 8-9.</p>
<p id="b533-6">Our reliance on the fact that the witness twice identified respondent in out-of-court confrontations is not intended to assign any independent evidentiary value to those identifications for to do so would undermine the exclusionary rule’s objectives in denying the Government the benefit of any evidence wrongfully obtained. Rather, the accurate pretrial identifications assume significance only to the extent that they indicate that the witness’ ability to identify respondent antedated any police misconduct, and hence that her in-court identification had an “independent source.”</p>
</footnote>
<footnote label="19">
<p id="b533-7"> Respondent contends that the “independent source” test of <em>United States </em>v. <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra,</a></span> </em>and <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967), although derived from an identical formulation in <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>, </em>see 388 U. S., at 241, seeks only to determine whether the in-court identification is sufficiently reliable to satisfy due process, and is thus inapplicable in the context of this Fourth Amendment violation. We agree that a satisfactory resolution of the reliability issue does not provide a complete answer to the considerations underlying <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>, </em>but note only that in the present case both concerns are met.</p>
</footnote>
<footnote label="20">
<p id="b534-7"> Cf. <em>United States </em>v. <em>Blue, </em><span class="citation" data-id="107238"><a href="/opinion/107238/united-states-v-blue/#255" aria-description="Citation for case: United States v. Blue">384 U. S. 251, 255</a></span> (1966):</p>
<blockquote id="b534-8">“Our numerous precedents ordering the exclusion of such illegally obtained evidence assume implicitly that the remedy does not extend to barring the prosecution altogether. So drastic a step might advance marginally some of the ends served by exclusionary rules, but it would also increase to an intolerable degree interference with the public interest in having the guilty brought to book.”</blockquote>
<p id="b534-9">In some cases, of course, prosecution may effectively be foreclosed by the absence of the challenged evidence. But this contemplated consequence is the product of the exclusion of specific evidence tainted by the Fourth Amendment violation and is not the result of a complete bar to prosecution.</p>
</footnote>
<footnote label="*">
<p id="b534-10">This part is joined only by Mb. Justice Stewart and Mr. Justice Stevens.</p>
</footnote>
<footnote label="21">
<p id="b535-7"> Cf. <em>Stevenson </em>v. <em>Mathews, </em><span class="citation" data-id="332396"><a href="/opinion/332396/kurt-stevenson-v-james-w-mathews-warden-wisconsin-correctional-camp/#63" aria-description="Citation for case: Kurt Stevenson v. James W. Mathews, Warden, Wisconsin...">529 F. 2d 61, 63</a></span> (CA7 1976).</p>
</footnote>
<footnote label="22">
<p id="b535-8"> Thus we are not called upon in this ease to hypothesize about whether routine investigatory procedures would eventually have led the police to discover respondent’s culpability. His involvement in the robberies was already suspected, and no new evidence was acquired through the violation of his Fourth Amendment rights.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Crumble.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Crumble
type: case
citation: "878 F.3d 656 (2018)"
parallel_cite: ""
neutral_cite: ""
court: 8th Cir.
court_level: coa
circuit: ca8
year: 2018
date_decided: 2018-01-02
docket: 16-4114
authority_weight: "Binding in-circuit — 8th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4456532/united-states-v-prentiss-anthony-crumble/"
  cluster_id: 4456532
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Crumble
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Abandonment]]"
    role: Key
related:
  - "[[Abandonment]]"
  - "[[Riley v. California]]"
  - "[[Minnesota v. Carter]]"
tags:
  - case
  - fourth-amendment
  - abandonment
  - reasonable-expectation-of-privacy
  - cell-phone
  - standing
  - eighth-circuit
holding: "A person who flees a wrecked car and leaves his cell phone behind, then denies any knowledge of the vehicle, abandons the phone and forfeits any reasonable expectation of privacy in it — judged by the objective facts available to officers, not the owner's subjective intent — and the abandonment doctrine applies to cell phones notwithstanding Riley v. California, so the warrantless seizure and later search of the phone did not violate the Fourth Amendment."
aliases:
  - United States v. Crumble
  - "United States v. Crumble (8th Cir. 2018)"
  - United States v. Prentiss Anthony Crumble
---

# United States v. Crumble

*878 F.3d 656 (8th Cir. 2018)* · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4456532 → majority opinion 4233785 (Shepherd, J.; 878 F.3d 656, decided Jan. 2, 2018). Re-keyed in the pre-W5 identity audit from a wrong-case namesake (Rehaif felon-in-possession Crumble) to the intended abandonment Crumble; identity re-verified on read 2026-07-07. Rule quote string-matched to the CL opinion text; slip-style pin (the CL text carries a page-image map, not 878 F.3d reporter star-pagination) — S9 verifies the reporter pincite. -->

## Background
After a shooting between two cars in St. Paul, one vehicle — a tan Buick — crashed into a house, and its two occupants fled on foot. Officers found the wrecked Buick with the key in the ignition, a shot-out rear window, a handgun on the floorboard, and a cell phone on the driver's seat. A witness's description led officers to Prentiss Crumble, hiding nearby; taken to the scene, he denied any knowledge of the shooting or the Buick. An officer later seized the phone and, under a warrant, found a video of Crumble with a similar handgun shortly before the shooting. The district court held Crumble had abandoned the phone and denied suppression.

## Issue
Whether Crumble abandoned his cell phone — forfeiting any [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in it — when he fled the wrecked car and disclaimed knowledge of the vehicle, and whether the abandonment doctrine applies to cell phones after *[[Riley v. California]]*.

## Rule
A defendant "does not have a reasonable expectation of privacy in abandoned property"; the question is whether, "in leaving the property," he "relinquished [his] reasonable expectation of privacy," judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] by "the objective facts available to the investigating officers, not ... the owner's subjective intent," with "two important factors [being] denial of ownership and physical relinquishment of the property." Rejecting a categorical carve-out, the court held: "Crumble urges this Court to categorically deny application of the abandonment doctrine to cell phones. We decline to do so." — slip op. at 3. ^pin-slip3

## Application
Objectively, Crumble fled the crash, left the phone on the seat of a wrecked car with the key in the ignition and the rear window shot out (open to anyone), and then affirmatively denied knowing anything about the Buick — conduct demonstrating both physical relinquishment and denial of ownership. His later admission, made after the phone was seized, did not reassert a privacy interest already forfeited. *[[Riley v. California|Riley]]* did not help him: its holding is limited to [[Search Incident to Arrest|searches incident to arrest]] and expressly leaves other case-specific exceptions — including abandonment — intact.

## Conclusion
**Affirmed.** Judge Shepherd wrote for the panel; the district court's abandonment finding was not [[Common Legal Terms#clear-error|clearly erroneous]], and the phone evidence was admissible.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Crumble* is a clean circuit application of the *[[Abandonment]]* doctrine to a modern device: fleeing and disclaiming ownership objectively forfeits the [[Reasonable Expectation of Privacy|reasonable expectation of privacy]], and *[[Riley v. California|Riley]]*'s special solicitude for phones does not exempt them from abandonment. Read it against the standing threshold of *[[Minnesota v. Carter]]*.

## Appears on
- [[Abandonment]] — *Key*

## Sources
- [*United States v. Crumble*, 878 F.3d 656 (8th Cir. 2018)](https://www.courtlistener.com/opinion/4456532/united-states-v-prentiss-anthony-crumble/) — pinpoint: slip op. at 3 (abandonment forfeits the reasonable expectation of privacy; the doctrine applies to cell phones despite *Riley*). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text carries a page-image map, not 878 F.3d reporter star-pagination, so the reporter page is not asserted here.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "61f335d4346c3344", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "878 F.3d 656 (2018)", "court": "8th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Crumble", "year": "2018"}}
{"assertion_id": "1be3da739179ab64", "dimension": "support", "kind": "home_role", "locator": {"home": "Abandonment"}, "payload": {"home": "Abandonment", "role": "Key", "title": "United States v. Crumble"}}
{"assertion_id": "3c8cddc647864680", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A person who flees a wrecked car and leaves his cell phone behind, then denies any knowledge of the vehicle, abandons the phone and forfeits any reasonable expectation of privacy in it — judged by the objective facts available to officers, not the owner's subjective intent — and the abandonment doctrine applies to cell phones notwithstanding Riley v. California, so the warrantless seizure and later search of the phone did not violate the Fourth Amendment.", "title": "United States v. Crumble"}}
{"assertion_id": "d765bf8ec5d634db", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 8th Cir.", "title": "United States v. Crumble"}}
{"assertion_id": "f59aee07aa8eac15", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Crumble", "varies_by_point": "false"}}
```

### lake record — United States v. Crumble

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Crumble",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Prentiss Anthony Crumble",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee v. Prentiss Anthony CRUMBLE, Defendant-Appellant",
    "input_case_name": "United States v. Crumble",
    "court": "8th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": "2018-01-02",
    "year": 2018,
    "docket": "16-4114",
    "cluster_id": 4456532,
    "lead_opinion_id": 4233785,
    "sibling_ids": [],
    "absolute_url": "/opinion/4456532/united-states-v-prentiss-anthony-crumble/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "878 F.3d 656",
      "volume": "878",
      "reporter": "F.3d",
      "page": "656",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "878 F.3d 656",
        "volume": "878",
        "reporter": "F.3d",
        "page": "656",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "878 F.3d 656",
    "official_selection": {
      "court_class": "coa",
      "selected": "878 F.3d 656",
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
    "date_created": "2026-07-07T18:16:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:16:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:16:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-crumble--4456532",
      "to_record_id": "United States v. Crumble",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Crumble

```
                 United States Court of Appeals
                            For the Eighth Circuit
                        ___________________________

                                No. 16-4308
                        ___________________________

                             United States of America

                        lllllllllllllllllllPlaintiff - Appellee

                                          v.

                            Prentiss Anthony Crumble

                      lllllllllllllllllllll Defendant - Appellant
                                      ____________

                    Appeal from United States District Court
                     for the District of Minnesota - St. Paul
                                 ____________

                           Submitted: October 20, 2017
                              Filed: January 2, 2018
                                 ____________

Before WOLLMAN and SHEPHERD, Circuit Judges, and GOLDBERG,1 Judge.
                         ____________

SHEPHERD, Circuit Judge.

      On October 21, 2014, at approximately 1:28 p.m., police received reports of
shots being fired between two vehicles in St. Paul, Minnesota. Dispatch informed
responding officers that one of the vehicles—a tan Buick—had crashed into a house


      1
       The Honorable Richard W. Goldberg, Judge for the United States Court of
International Trade, sitting by designation.
and its two male occupants had fled on foot. Officers arrived at the scene to find the
wrecked Buick with bullet holes along its passenger side and a shot-out rear window.
They noticed the Buick’s key in its ignition and a handgun on the driver’s side
floorboard. A witness informed the officers that after the crash the other vehicle’s
shooter continued to fire at the Buick. The witness stated that the Buick’s two
occupants fled the scene on foot heading west, describing one as a black male, in his
early 20s, wearing a white t-shirt. Another witness also reported seeing an
approximately 25-year-old black male in a white t-shirt running westward from the
Buick. Officers found a man matching this description hiding behind a shed a block
and a half away. That man was appellant Prentiss Crumble.

       Officers took Crumble into custody and drove him to the scene of the wrecked
Buick—where he denied any knowledge of the shooting or the Buick. When an
officer searched the Buick later that day, he found a cell phone on the driver’s seat,
which he secured into evidence. The following day, the officer applied for a search
warrant to search the cell phone for “information as to the second occupant in the
Buick or further information related to the crime.” A county judge issued a warrant
to search “[a]ll electronic data (including but not limited to contacts, calenders, call
records, voice messages, text messages, photo and video files) stored in” the phone.
In the subsequent search, the officer found a video of Crumble inside a vehicle
wearing a white t-shirt and brandishing a handgun similar to that recovered from the
Buick. The video was recorded shortly before the shooting on October 21, 2014 at
1:15 p.m.

      Crumble was charged with being a felon in possession of a firearm in violation
of 18 U.S.C. §§ 922(g)(1) and 924(e). Crumble moved to suppress the evidence
recovered from the cell phone. The magistrate judge recommended granting
Crumble’s motion to suppress, finding Crumble had not abandoned his Fourth
Amendment rights in the phone. The district court rejected the magistrate judge’s
recommendation, concluding that the evidence from the cell phone was admissible

                                          -2-
because Crumble abandoned the Buick and the phone left in it when he fled and
subsequently denied any knowledge of the vehicle. The district court alternatively
held that the search warrant was supported by probable cause and did not lack
particularity or amount to a general warrant. Finally, even if there were no probable
cause or a lack of particularity, the good-faith exception applied because it was
objectively reasonable for the police to rely on the warrant.

       Crumble entered a conditional guilty plea, reserving his right to appeal the
district court’s denial of his motion to suppress the evidence obtained in the search
of his cell phone. At sentencing, the government sought application of the Armed
Career Criminal Act (“ACCA”) based on Crumble’s prior felony convictions under
Minnesota law, which included a conviction for second-degree assault, a conviction
for second-degree burglary, and two convictions for third-degree burglary. Crumble
argued the burglary convictions were not violent felonies under the ACCA. The
district court disagreed and imposed the ACCA mandatory minimum sentence of 15
years in prison. Crumble now appeals his conviction and sentence.

                                           I.

       We first take up Crumble’s Fourth Amendment challenge to the search of the
cell phone. The Fourth Amendment protects “against unreasonable searches and
seizures.” U.S. Const. amend. IV. “[I]n order to claim the protection of the Fourth
Amendment, a defendant must demonstrate that he personally has [a reasonable]
expectation of privacy in the place searched . . . . ” Minnesota v. Carter, 525 U.S. 83,
88 (1998). Therefore, we must initially consider whether Crumble had a reasonable
expectation of privacy in the cell phone he left behind in the Buick.

       It is well-established that a defendant does not have a reasonable expectation
of privacy in abandoned property. See United States v. Tugwell, 125 F.3d 600, 602
(8th Cir. 1997). Thus, if Crumble abandoned the cell phone, he forfeited his

                                          -3-
expectation of privacy and cannot raise a Fourth Amendment challenge to the
subsequent search. See id. (“A warrantless search of abandoned property does not
implicate the Fourth Amendment, for any expectation of privacy in the item searched
is forfeited upon its abandonment.”). “The issue is not abandonment in the strict
property right sense, but rather, whether the defendant in leaving the property has
relinquished [his] reasonable expectation of privacy . . . . ” Id. (internal quotation
marks omitted). A finding of abandonment depends on the totality of the
circumstances, with “two important factors [being] denial of ownership and physical
relinquishment of the property.” Id. (internal quotation marks omitted). Courts
consider only “the objective facts available to the investigating officers, not . . . the
owner’s subjective intent.” United States v. Nowak, 825 F.3d 946, 948 (8th Cir.
2016) (per curiam) (internal quotation marks omitted).

      Here, the district court found that Crumble abandoned the cell phone. We
review this factual finding for clear error, “affirm[ing] the district court’s
abandonment finding unless its decision is ‘unsupported by substantial evidence,
based on an erroneous interpretation of applicable law, or, in light of the entire
record, we are left with a firm and definite conviction that a mistake has been made.’”
United States v. Ruiz, 935 F.2d 982, 984 (8th Cir. 1991) (quoting United States v.
Meirovitz, 918 F.2d 1376, 1379 (8th Cir. 1990)).

       Based on the totality of the circumstances, we cannot say that the district court
clearly erred in finding Crumble abandoned the cell phone in the Buick. After the
crash, Crumble fled the scene, leaving the Buick wrecked on a stranger’s lawn. The
Buick’s key was in the ignition and its back window was shot out—allowing for easy
access to the vehicle and its contents—which included a gun on the floorboard and
the cell phone on the driver’s seat. Crumble claims he was not fleeing from police,
but rather attempting to get away from the shooter in the other vehicle.
Abandonment, however, does not turn on Crumble’s subjective intent, but rather “the
objective facts available to the investigating officers.” Nowak, 825 F.3d at 948

                                          -4-
(internal quotation marks omitted). Based on these objective facts, the district court
did not clearly err in concluding Crumble had abandoned the vehicle and its contents,
including the cell phone. See United States v. Taylor, 462 F.3d 1023, 1025-26 (8th
Cir. 2006) (finding defendant abandoned cell phone when he dropped it on street
while fleeing vehicle); see also United States v. Smith, 648 F.3d 654, 660 (8th Cir.
2011) (finding defendant abandoned vehicle and contents when he fled, leaving door
open, key in ignition, and motor running); United States v. Tate, 821 F.2d 1328, 1330
(8th Cir. 1987) (finding defendant abandoned vehicle and contents when he fled,
leaving vehicle unoccupied and unlocked).

       Moreover, Crumble initially denied any knowledge of the wrecked Buick,
evincing his intent to abandon the vehicle and its contents. See United States v.
Nordling, 804 F.2d 1466, 1470 (8th Cir. 1986) (finding defendant’s “denials
objectively demonstrate an intent to abandon the property”). Only the following
day—after police had already seized the cell phone—did Crumble admit to having
been in the Buick. This admission did not constitute a reassertion of a privacy
interest in the abandoned cell phone. See id.

       Crumble urges this Court to categorically deny application of the abandonment
doctrine to cell phones. We decline to do so. Crumble points to Riley v. California,
where the Supreme Court held that the search incident to arrest exception does not
apply to cell phone searches, in part because cell phones hold “the privacies of life.”
134 S. Ct. 2473, 2494-95 (2014) (internal quotation marks omitted). However,
Riley’s holding is limited to cell phones seized incident to arrest. Id. at 2495. Riley
was explicit that “other case-specific exceptions may still justify a warrantless search
of a particular phone.” Id. at 2494. Other courts have found abandonment to be one
such exception. See, e.g., United States v. Quashie, 162 F. Supp. 3d 135, 141-42
(E.D.N.Y. 2016) (finding Riley does not eliminate abandonment exception for cell
phones).



                                          -5-
      We conclude the district court did not clearly err in finding abandonment and
denying Crumble’s motion to suppress. Because we affirm the district court’s
holding based on abandonment, we need not consider whether the warrant was valid.
Cf. Tugwell, 125 F.3d at 602 (“warrantless search of abandoned property does not
implicate the Fourth Amendment”).

                                          II.

       We next turn to Crumble’s sentencing challenge. The district court sentenced
Crumble to the ACCA mandatory minimum of 15 years imprisonment. The ACCA
applies when a defendant convicted under 18 U.S.C. § 922(g) has three prior
convictions “for a violent felony or a serious drug offense.” 18 U.S.C. § 924(e)(1).
As noted earlier, Crumble’s prior felony convictions include a Minnesota conviction
for second-degree assault, a Minnesota conviction for second-degree burglary, and
two Minnesota convictions for third-degree burglary. Crumble argues his burglary
convictions do not qualify as violent felonies under the ACCA, and the government
agrees. We review whether a prior conviction qualifies as a violent felony de novo.
United States v. Shockley, 816 F.3d 1058, 1062 (8th Cir. 2016).

       The ACCA’s definition of “violent felony” includes burglary. 18 U.S.C.
§ 924(e)(2)(B)(ii). To determine whether a state burglary conviction qualifies as
burglary under the ACCA, we must first determine whether to apply the categorical
approach (used when an indivisible statute lists alternative means of committing a
single crime) or the modified categorical approach (used when a divisible statute lists
alternative elements to define multiple crimes). See Mathis v. United States, 136 S.
Ct. 2243, 2248-49 (2016). Under the categorical approach, a state burglary
conviction qualifies only if its statute’s elements are the same as, or narrower than,
those of generic burglary, which is an “‘unlawful or unprivileged entry into, or
remaining in, a building or structure, with intent to commit a crime.’” Descamps v.



                                         -6-
United States, 133 S. Ct. 2276, 2283 (2013) (quoting Taylor v. United States, 495
U.S. 575, 599 (1990)).

      Minnesota’s third-degree burglary statute provides that:

      Whoever enters a building without consent and with intent to steal or
      commit any felony or gross misdemeanor while in the building, or enters
      a building without consent and steals or commits a felony or gross
      misdemeanor while in the building . . . commits burglary in the third
      degree . . . .

Minn. Stat. § 609.582, subdiv. 3. In determining whether Minnesota third-degree
burglary qualifies as a violent felony under the ACCA, this Court’s decision in
United States v. McArthur, 850 F.3d 925 (8th Cir. 2017) is controlling. There, this
Court found Minnesota’s third-degree burglary statute to be indivisible and applied
the categorical approach. Id. at 938. While the first alternative means in the
Minnesota statute (entering with intent to commit a crime) qualifies as generic
burglary, the second alternative means (unlawful entry followed by the commission
of a crime) does not. Id. at 938-40. That is because the second alternative means
“does not require that the defendant have formed the ‘intent to commit a crime’ at the
time of the nonconsensual entry or remaining in,” as is required by the definition of
generic burglary in Taylor. Id. at 940. Thus, Minnesota third-degree burglary “is
broader than generic burglary” and does not qualify as a predicate conviction under
the ACCA. Id.

      Minnesota’s second-degree burglary statute provides that:

      Whoever enters a building without consent and with intent to commit a
      crime, or enters a building without consent and commits a crime while
      in the building . . . commits burglary in the second degree . . . .



                                         -7-
Minn. Stat. § 609.582, subdiv. 2(a). Both parties agree that because this statute
includes the same overbroad second alternative means as Minnesota’s third-degree
burglary statute (unlawful entry followed by the commission of a crime), Minnesota
second-degree burglary does not qualify as a violent felony under the ACCA. Indeed,
this Court’s analysis of Minnesota’s third-degree burglary statute in McArthur applies
with equal force to Minnesota’s second-degree burglary statute. The statute is
indivisible, so we apply the categorical approach. See McArthur, 850 F.3d at 938
(citing State v. Gonzales, No. A15-0975, 2016 WL 3222795, at *2-3 (Minn. Ct. App.
June 13, 2016)). Because a conviction under the second alternative means of the
statute “does not require that the defendant have formed the ‘intent to commit a
crime’ at the time of the nonconsensual entry or remaining in,” Minnesota second-
degree burglary “is broader than generic burglary” and does not qualify as a predicate
conviction under the ACCA. See id. at 940.

       Because Crumble’s Minnesota burglary convictions do not qualify as violent
felonies, Crumble has no more than one predicate conviction. The ACCA mandatory
minimum, therefore, does not apply. We vacate his sentence and remand to the
district court for resentencing.

                                         III.

     For the foregoing reasons, we affirm the district court’s denial of Crumble’s
motion to suppress and remand for resentencing in accordance with this opinion.
                      ______________________________




                                         -8-

```

---

## GROUP: content/cases/United States v. Drayton.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Drayton"
type: case
citation: "536 U.S. 194 (2002)"
parallel_cite: "122 S. Ct. 2105; 153 L. Ed. 2d 242"
neutral_cite: 2002 U.S. LEXIS 4420
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Drayton
  varies_by_point: false
  scope_note: "Good law; bus-sweep questioning and consent requests are not a per se seizure, and officers need not advise of the right to refuse."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/121153/united-states-v-drayton/"
  cluster_id: 121153
  opinion_id: 121153
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Key — Progeny / Refinement"
related: ["[[Florida v. Bostick]]", "[[Schneckloth v. Bustamonte]]", "[[Ohio v. Robinette]]", "[[California v. Hodari D.]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "seizure"]
holding: "A bus sweep with consent-to-search requests is not a seizure, and consent can be voluntary even though officers do not advise passengers…"
lake:
  record_id: United States v. Drayton
  status: verified
  projected_at: 2026-07-09
---

# United States v. Drayton

*536 U.S. 194 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Three officers boarded a stopped interstate bus as part of a drug interdiction sweep. One stationed himself at the front, another at the rear, and a third worked his way down the aisle, leaning toward passengers and asking about their travel and luggage. He asked Drayton and Brown for permission to search their persons; both consented, and officers found drugs taped to their legs. The officer did not tell passengers they were free to refuse to cooperate.

## Issue
Whether the bus passengers were seized when officers questioned them and requested consent to search, and whether their consent was involuntary because officers did not advise them of their right to refuse.

## Rule
Bus-sweep questioning is not a [[Common Legal Terms#per-se|per se]] seizure; the test is objective: "Applying the *Bostick* framework to the facts of this particular case, we conclude that the police did not seize respondents when they boarded the bus and began questioning passengers." — 536 U.S. at 203. ^pin-203

The inquiry is "whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter." — [*Id.* at 202](https://www.courtlistener.com/opinion/121153/united-states-v-drayton/#:~:text=whether%20a%20reasonable%20person%20would) (quoting *Florida v. Bostick*). ^pin-202

And officers need not warn of the right to refuse: "The Court has rejected in specific terms the suggestion that police officers must always inform citizens of their right to refuse when seeking permission to conduct a warrantless consent search." — [*Id.* at 206](https://www.courtlistener.com/opinion/121153/united-states-v-drayton/#:~:text=The%20Court%20has%20rejected%20in). ^pin-206

## Application
On these facts the officers gave passengers no reason to believe they were required to cooperate: they did not brandish weapons, block the aisle, or use a commanding tone, and Drayton was free to refuse. The encounter was therefore not a seizure. And although the officer never told Drayton he could refuse the search, he did request permission to search rather than demand it, and under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] Drayton's consent was voluntary. The failure to advise of the right to refuse was one factor, not a disqualifier, so the searches were reasonable.

## Conclusion
The bus passengers were not seized, and their consent to search was voluntary despite the absence of any advice of the right to refuse; the suppression below was reversed. Officers may work a bus and request consent without effecting a seizure, and need not warn passengers that they may decline.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Drayton* applies the free-to-decline test of [[Florida v. Bostick]] and the totality-of-circumstances voluntariness rule of [[Schneckloth v. Bustamonte]] and [[Ohio v. Robinette]] (no warning of the right to refuse required); on when a show of authority becomes a seizure, compare [[California v. Hodari D.]].

## Appears on
- [[Knock and Talk]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Drayton*, 536 U.S. 194 (2002) — https://www.courtlistener.com/opinion/121153/united-states-v-drayton/ — pinpoints: 202, 203, 206.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "642edd8f64eec07c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "536 U.S. 194 (2002)", "court": "U.S. Supreme Court", "neutral_cite": "2002 U.S. LEXIS 4420", "official_citation_present": true, "parallel_cite": "122 S. Ct. 2105; 153 L. Ed. 2d 242", "title": "United States v. Drayton", "year": "2002"}}
{"assertion_id": "01a1c315eca848ef", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Key — Progeny / Refinement", "title": "United States v. Drayton"}}
{"assertion_id": "d6803dba857516f2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A bus sweep with consent-to-search requests is not a seizure, and consent can be voluntary even though officers do not advise passengers…", "title": "United States v. Drayton"}}
{"assertion_id": "18a7eb3d6d62f0aa", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Drayton"}}
{"assertion_id": "a39da738500f12b0", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2002-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Drayton", "field_i_validity": "good_law", "scope_note": "Good law; bus-sweep questioning and consent requests are not a per se seizure, and officers need not advise of the right to refuse.", "title": "United States v. Drayton", "varies_by_point": "false"}}
```

### lake record — United States v. Drayton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Drayton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Drayton",
    "case_name_short": "Drayton",
    "case_name_full": "UNITED STATES v. DRAYTON Et Al.",
    "input_case_name": "United States v. Drayton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-17",
    "year": 2002,
    "docket": null,
    "cluster_id": 121153,
    "lead_opinion_id": 121153,
    "sibling_ids": [
      121153,
      9434276,
      9434277
    ],
    "absolute_url": "/opinion/121153/united-states-v-drayton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "536 U.S. 194",
      "volume": "536",
      "reporter": "U.S.",
      "page": "194",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 2105",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2105",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 242",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4420",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4420",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 194",
        "volume": "536",
        "reporter": "U.S.",
        "page": "194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2105",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2105",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 242",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4420",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4420",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "536 U.S. 194",
    "official_selection": {
      "court_class": "scotus",
      "selected": "536 U.S. 194",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-203",
      "page": null,
      "quote": "--- # United States v. Drayton *536 U.S. 194 (2002)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Three officers boarded a stopped interstate bus as part of a drug interdiction sweep. One stationed himself at the front, another at the rear, and a third worked his way down the aisle, leaning toward passengers and asking about their travel and luggage. He asked Drayton and Brown for permission to search their persons; both consented, and officers found drugs taped to their legs. The officer did not tell passengers they were free to refuse to cooperate. ## Issue Whether the bus passengers were seized when officers questioned them and requested consent to search, and whether their consent was involuntary because officers did not advise them of their right to refuse. ## Rule Bus-sweep questioning is not a per se seizure; the test is objective:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-202",
      "page": null,
      "quote": "whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter.",
      "star_marker": "202",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13873,
      "fragment": "#:~:text=whether%20a%20reasonable%20person%20would",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-206",
      "page": null,
      "quote": "The Court has rejected in specific terms the suggestion that police officers must always inform citizens of their right to refuse when seeking permission to conduct a warrantless consent search.",
      "star_marker": "206",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28368,
      "fragment": "#:~:text=The%20Court%20has%20rejected%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Drayton",
    "varies_by_point": false,
    "scope_note": "Good law; bus-sweep questioning and consent requests are not a per se seizure, and officers need not advise of the right to refuse.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Morris Wise",
          "cluster_id": 4448990,
          "cite": [
            "877 F.3d 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Parker",
          "cluster_id": 4440893,
          "cite": [
            "807 S.E.2d 617",
            "256 N.C. App. 319"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Patrick Daniel White",
          "cluster_id": 4322612,
          "cite": [
            "887 N.W.2d 172",
            "2016 Iowa Sup. LEXIS 105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 3203547,
          "cite": [
            "823 F.3d 20",
            "2016 U.S. App. LEXIS 8834",
            "2016 WL 2821485"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moises Donjuan v. State",
          "cluster_id": 2980860,
          "cite": [
            "461 S.W.3d 611",
            "2015 Tex. App. LEXIS 1618",
            "2015 WL 732640"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Camp",
          "cluster_id": 2774669,
          "cite": [
            "2015 Ohio 329"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
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
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
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
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zamudio",
          "cluster_id": 2634388,
          "cite": [
            "181 P.3d 105",
            "75 Cal. Rptr. 3d 289",
            "43 Cal. 4th 327",
            "2008 Cal. LEXIS 4431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crain v. State",
          "cluster_id": 2353970,
          "cite": [
            "315 S.W.3d 43",
            "2010 Tex. Crim. App. LEXIS 794",
            "2010 WL 2595077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
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
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tully",
          "cluster_id": 844166,
          "cite": [
            "54 Cal. 4th 952",
            "282 P.3d 173",
            "145 Cal. Rptr. 3d 146",
            "2012 WL 3064338",
            "2012 Cal. LEXIS 7247"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
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
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Luedemann",
          "cluster_id": 2008176,
          "cite": [
            "857 N.E.2d 187",
            "222 Ill. 2d 530",
            "306 Ill. Dec. 94",
            "2006 Ill. LEXIS 1641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gherna",
          "cluster_id": 2252587,
          "cite": [
            "784 N.E.2d 799",
            "203 Ill. 2d 165",
            "271 Ill. Dec. 245",
            "2003 Ill. LEXIS 2"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A.M. Ex Rel. F.M. v. Holmes",
          "cluster_id": 4241340,
          "cite": [
            "830 F.3d 1123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
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
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Randall Lee Pals",
          "cluster_id": 4472392,
          "cite": [
            "805 N.W.2d 767",
            "2011 Iowa Sup. LEXIS 87"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Castleberry",
          "cluster_id": 2282066,
          "cite": [
            "332 S.W.3d 460",
            "2011 Tex. Crim. App. LEXIS 283",
            "2011 WL 709697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Caraballo",
          "cluster_id": 78534,
          "cite": [
            "595 F.3d 1214",
            "2010 WL 297146"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 2623710,
          "cite": [
            "166 P.3d 1015",
            "284 Kan. 763",
            "2007 Kan. LEXIS 487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Monterroso",
          "cluster_id": 2507854,
          "cite": [
            "101 P.3d 956",
            "22 Cal. Rptr. 3d 1",
            "34 Cal. 4th 743",
            "2004 Daily Journal DAR 14707",
            "2004 Cal. Daily Op. Serv. 10899",
            "2004 Cal. LEXIS 11763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Hicks, M., Aplt.",
          "cluster_id": 4625130,
          "cite": [
            "208 A.3d 916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Harris v. Kimberly Klare",
          "cluster_id": 4532638,
          "cite": [
            "902 F.3d 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jennings v. Jones",
          "cluster_id": 8440132,
          "cite": [
            "499 F.3d 2",
            "2007 U.S. App. LEXIS 19583",
            "2007 WL 2339195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jordan",
          "cluster_id": 212479,
          "cite": [
            "635 F.3d 1181",
            "2011 U.S. App. LEXIS 5235",
            "2011 WL 891075"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trafton v. City of Woodbury",
          "cluster_id": 2150404,
          "cite": [
            "799 F. Supp. 2d 417",
            "2011 U.S. Dist. LEXIS 70682",
            "2011 WL 2610747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cox",
          "cluster_id": 1058221,
          "cite": [
            "171 S.W.3d 174",
            "2005 Tenn. LEXIS 683",
            "2005 WL 2051278"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 2200827,
          "cite": [
            "789 N.E.2d 260",
            "204 Ill. 2d 220",
            "273 Ill. Dec. 360",
            "2003 Ill. LEXIS 765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Romain",
          "cluster_id": 201394,
          "cite": [
            "393 F.3d 63",
            "2004 WL 2997954"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(121153 OR 9434276 OR 9434277) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEyNDE2MDAwMDAwJnM9MzEyMjU1NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28121153+OR+9434276+OR+9434277%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(121153 OR 9434276 OR 9434277)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OSZzPTc3OTI3MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28121153+OR+9434276+OR+9434277%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(121153 OR 9434276 OR 9434277)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(121153 OR 9434276 OR 9434277)",
    "indexed_citing_opinions": 594,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 121153,
        "count": 502,
        "count_source": "search"
      },
      {
        "opinion_id": 9434276,
        "count": 101,
        "count_source": "search"
      },
      {
        "opinion_id": 9434277,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1085,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-drayton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0NDA5NzMmcz05NDI1NzQ5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28121153+OR+9434276+OR+9434277%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 121153,
        "cited_id": 72919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 73082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 771014,
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
    "date_created": "2026-07-05T23:36:24Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:36:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:36:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:42:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:36:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Drayton

```
<div>
<center><b><span class="citation" data-id="9434276"><a href="/opinion/121153/united-states-v-drayton/" aria-description="Citation for case: United States v. Drayton">536 U.S. 194</a></span> (2002)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
DRAYTON et al.</h1></center>
<center>No. 01-631.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued April 16, 2002.</center>
<center>Decided June 17, 2002.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE ELEVENTH CIRCUIT
<p><span class="star-pagination">*196</span> <span class="star-pagination">*196</span> Kennedy, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Scalia, Thomas, and Breyer, JJ., joined. Souter, J., filed a dissenting opinion, in which Stevens and Ginsburg, JJ., joined, <i>post,</i> p. 208.</p>
<p><i>Larry D. Thompson</i> argued the cause for the United States. On the briefs were <i>Solicitor General Olson, Assistant Attorney General Chertoff, Deputy Solicitor General Dreeben, Jeffrey A. Lamken,</i> and <i>Kathleen A. Felton.</i> </p>
<p><i>Gwendolyn Spivey,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./535/903/">535 U. S. 903</a></span>, argued the cause for respondents. With her on the brief were <i>Randolph P. Murrell, Steven L. Seliger,</i> by appointment <span class="star-pagination">*197</span> of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./535/903/">535 U. S. 903</a></span>, <i>Jeffrey T. Green,</i> and <i>Jacqueline G. Cooper.</i><sup>[*]</sup></p>
<p>Justice Kennedy, delivered the opinion of the Court.</p>
<p>The Fourth Amendment permits police officers to approach bus passengers at random to ask questions and to request their consent to searches, provided a reasonable person would understand that he or she is free to refuse. <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991). This case requires us to determine whether officers must advise bus passengers during these encounters of their right not to cooperate.</p>
<p></p>
<h2>I</h2>
<p>On February 4, 1999, respondents Christopher Drayton and Clifton Brown, Jr., were traveling on a Greyhound bus en route from Ft. Lauderdale, Florida, to Detroit, Michigan. The bus made a scheduled stop in Tallahassee, Florida. The passengers were required to disembark so the bus could be refueled and cleaned. As the passengers reboarded, the driver checked their tickets and then left to complete paperwork inside the terminal. As he left, the driver allowed three members of the Tallahassee Police Department to board the bus as part of a routine drug and weapons interdiction effort. The officers were dressed in plain clothes and carried concealed weapons and visible badges.</p>
<p>Once on board Officer Hoover knelt on the driver's seat and faced the rear of the bus. He could observe the passengers <span class="star-pagination">*198</span> and ensure the safety of the two other officers without blocking the aisle or otherwise obstructing the bus exit. Officers Lang and Blackburn went to the rear of the bus. Blackburn remained stationed there, facing forward. Lang worked his way toward the front of the bus, speaking with individual passengers as he went. He asked the passengers about their travel plans and sought to match passengers with luggage in the overhead racks. To avoid blocking the aisle, Lang stood next to or just behind each passenger with whom he spoke.</p>
<p>According to Lang's testimony, passengers who declined to cooperate with him or who chose to exit the bus at any time would have been allowed to do so without argument. In Lang's experience, however, most people are willing to cooperate. Some passengers go so far as to commend the police for their efforts to ensure the safety of their travel. Lang could recall five to six instances in the previous year in which passengers had declined to have their luggage searched. It also was common for passengers to leave the bus for a cigarette or a snack while the officers were on board. Lang sometimes informed passengers of their right to refuse to cooperate. On the day in question, however, he did not.</p>
<p>Respondents were seated next to each other on the bus. Drayton was in the aisle seat, Brown in the seat next to the window. Lang approached respondents from the rear and leaned over Drayton's shoulder. He held up his badge long enough for respondents to identify him as a police officer. With his face 12-to-18 inches away from Drayton's, Lang spoke in a voice just loud enough for respondents to hear:</p>
<blockquote>"I'm Investigator Lang with the Tallahassee Police Department. We're conducting bus interdiction <i>[sic],</i>  attempting to deter drugs and illegal weapons being transported on the bus. Do you have any bags on the bus?" App. 55.</blockquote>
<p><span class="star-pagination">*199</span> Both respondents pointed to a single green bag in the overhead luggage rack. Lang asked, "Do you mind if I check it?," and Brown responded, "Go ahead." <i>Id.,</i> at 56. Lang handed the bag to Officer Blackburn to check. The bag contained no contraband.</p>
<p>Officer Lang noticed that both respondents were wearing heavy jackets and baggy pants despite the warm weather. In Lang's experience drug traffickers often use baggy clothing to conceal weapons or narcotics. The officer thus asked Brown if he had any weapons or drugs in his possession. And he asked Brown: "Do you mind if I check your person?" Brown answered, "Sure," and cooperated by leaning up in his seat, pulling a cell phone out of his pocket, and opening up his jacket. <i>Id.,</i> at 61. Lang reached across Drayton and patted down Brown's jacket and pockets, including his waist area, sides, and upper thighs. In both thigh areas, Lang detected hard objects similar to drug packages detected on other occasions. Lang arrested and handcuffed Brown. Officer Hoover escorted Brown from the bus.</p>
<p>Lang then asked Drayton, "Mind if I check you?" <i>Id.,</i>  at 65. Drayton responded by lifting his hands about eight inches from his legs. Lang conducted a patdown of Drayton's thighs and detected hard objects similar to those found on Brown. He arrested Drayton and escorted him from the bus. A further search revealed that respondents had ducttaped plastic bundles of powder cocaine between several pairs of their boxer shorts. Brown possessed three bundles containing 483 grams of cocaine. Drayton possessed two bundles containing 295 grams of cocaine.</p>
<p>Respondents were charged with conspiring to distribute cocaine, in violation of <span class="citation no-link">21 U. S. C. §§ 841</span>(a)(1) and 846, and with possessing cocaine with intent to distribute it, in violation of § 841(a)(1). They moved to suppress the cocaine, arguing that the consent to the patdown search was invalid. Following a hearing at which only Officer Lang testified, the <span class="star-pagination">*200</span> United States District Court for the Northern District of Florida denied their motions to suppress. The District Court determined that the police conduct was not coercive and respondents' consent to the search was voluntary. The District Court pointed to the fact that the officers were dressed in plain clothes, did not brandish their badges in an authoritative manner, did not make a general announcement to the entire bus, and did not address anyone in a menacing tone of voice. It noted that the officers did not block the aisle or the exit, and stated that it was "obvious that [respondents] can get up and leave, as can the people ahead of them." App. 132. The District Court concluded: "[E]verything that took place between Officer Lang and Mr. Drayton and Mr. Brown suggests that it was cooperative. There was nothing coercive, there was nothing confrontational about it." <i>Ibid.</i> </p>
<p>The Court of Appeals for the Eleventh Circuit reversed and remanded with instructions to grant respondents' motions to suppress. <span class="citation" data-id="771014"><a href="/opinion/771014/united-states-of-amercia-v-christopher-drayton-clifton-brown-jr/" aria-description="Citation for case: United States of Amercia v. Christopher Drayton &amp; Clifton...">231 F. 3d 787</a></span> (2000). The court held that this disposition was compelled by its previous decisions in <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/" aria-description="Citation for case: United States v. Washington">151 F. 3d 1354</a></span> (1998), and <i>United States</i> v. <i>Guapi,</i> <span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">144 F. 3d 1393</a></span> (1998). Those cases had held that bus passengers do not feel free to disregard police officers' requests to search absent "some positive indication that consent could have been refused." <span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/#1357" aria-description="Citation for case: United States v. Washington"><i>Washington, supra,</i> at 1357</a></span>.</p>
<p>We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./534/1074/">534 U. S. 1074</a></span> (2002). The respondents, we conclude, were not seized and their consent to the search was voluntary; and we reverse.</p>
<p></p>
<h2>II</h2>
<p>Law enforcement officers do not violate the Fourth Amendment's prohibition of unreasonable seizures merely by approaching individuals on the street or in other public places and putting questions to them if they are willing to listen. See, <i>e. g., </i><i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 497</a></span> (1983) <span class="star-pagination">*201</span> (plurality opinion); see <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#523" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 523, n. 3</a></span> (Rehnquist, J., dissenting); <i>Florida</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#5" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1, 5-6</a></span> (1984) <i>(per curiam)</i> (holding that such interactions in airports are "the sort of consensual encounter[s] that implicat[e] no Fourth Amendment interest"). Even when law enforcement officers have no basis for suspecting a particular individual, they may pose questions, ask for identification, and request consent to search luggageprovided they do not induce cooperation by coercive means. See <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#434" aria-description="Citation for case: Florida v. Bostick">501 U. S., at 434-435</a></span> (citations omitted). If a reasonable person would feel free to terminate the encounter, then he or she has not been seized.</p>
<p>The Court has addressed on a previous occasion the specific question of drug interdiction efforts on buses. In <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span>,</i> two police officers requested a bus passenger's consent to a search of his luggage. The passenger agreed, and the resulting search revealed cocaine in his suitcase. The Florida Supreme Court suppressed the cocaine. In doing so it adopted a <i>per se</i> rule that due to the cramped confines onboard a bus the act of questioning would deprive a person of his or her freedom of movement and so constitute a seizure under the Fourth Amendment.</p>
<p>This Court reversed. <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> first made it clear that for the most part <i>per se</i> rules are inappropriate in the Fourth Amendment context. The proper inquiry necessitates a consideration of "all the circumstances surrounding the encounter." <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#439" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 439</a></span>. The Court noted next that the traditional rule, which states that a seizure does not occur so long as a reasonable person would feel free "to disregard the police and go about his business," <i>California</i> v. <i>Hodari D.,</i>  <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#628" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621, 628</a></span> (1991), is not an accurate measure of the coercive effect of a bus encounter. A passenger may not want to get off a bus if there is a risk it will depart before the opportunity to reboard. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#434" aria-description="Citation for case: Florida v. Bostick">501 U. S., at 434-436</a></span>. A bus rider's movements are confined in this sense, but this is the natural result of choosing to take the bus; it says nothing <span class="star-pagination">*202</span> about whether the police conduct is coercive. <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#436" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 436</a></span>. The proper inquiry "is whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter." <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Ibid.</a></span></i> Finally, the Court rejected Bostick's argument that he must have been seized because no reasonable person would consent to a search of luggage containing drugs. The reasonable person test, the Court explained, is objective and "presupposes an <i>innocent</i> person." <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 437-438</a></span>.</p>
<p>In light of the limited record, <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> refrained from deciding whether a seizure occurred. <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 437</a></span>. The Court, however, identified two factors "particularly worth noting" on remand. <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#432" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 432</a></span>. First, although it was obvious that an officer was armed, he did not remove the gun from its pouch or use it in a threatening way. Second, the officer advised the passenger that he could refuse consent to the search. <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Ibid.</a></span></i> </p>
<p>Relying upon this latter factor, the Eleventh Circuit has adopted what is in effect a <i>per se</i> rule that evidence obtained during suspicionless drug interdiction efforts aboard buses must be suppressed unless the officers have advised passengers of their right not to cooperate and to refuse consent to a search. In <i>United States</i> v. <i><span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">Guapi, supra</a></span></i><i>,</i> the Court of Appeals described "[t]he most glaring difference" between the encounters in <i><span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">Guapi</a></span></i> and in <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> as "the complete lack of any notification to the passengers that they were in fact free to decline the search request. . . . Providing [this] simple notification . . . is perhaps the most efficient and effective method to ensure compliance with the Constitution." <span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/#1395" aria-description="Citation for case: United States v. Guapi">144 F. 3d, at 1395</a></span>. The Court of Appeals then listed other factors that contributed to the coerciveness of the encounter: (1) the officer conducted the interdiction before the passengers disembarked from the bus at a scheduled stop; (2) the officer explained his presence in the form of a general announcement to the entire bus; (3) the officer wore a police uniform; and (4) the officer questioned passengers as he <span class="star-pagination">*203</span> moved from the front to the rear of the bus, thus obstructing the path to the exit. <span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/#1396" aria-description="Citation for case: United States v. Guapi"><i>Id.,</i> at 1396</a></span>.</p>
<p>After its decision in <i><span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">Guapi</a></span></i> the Court of Appeals decided <i>United States</i> v. <i><span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/" aria-description="Citation for case: United States v. Washington">Washington</a></span></i> and the instant case. The court suppressed evidence obtained during similar drug interdiction efforts despite the following facts: (1) the officers in both cases conducted the interdiction after the passengers had reboarded the bus; (2) the officer in the present case did not make a general announcement to the entire bus but instead spoke with individual passengers; (3) the officers in both cases were not in uniform; and (4) the officers in both cases questioned passengers as they moved from the rear to the front of the bus and were careful not to obstruct passengers' means of egress from the bus.</p>
<p>Although the Court of Appeals has disavowed a <i>per se</i> requirement, the lack of an explicit warning to passengers is the only element common to all its cases. See <i>Washington,</i>  <span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/#1357" aria-description="Citation for case: United States v. Washington">151 F. 3d, at 1357</a></span> ("It seems obvious to us that if police officers genuinely want to ensure that their encounters with bus passengers remain absolutely voluntary, they can simply say so. Without such notice in this case, we do not feel a reasonable person would have felt able to decline the agents' requests"); <span class="citation" data-id="771014"><a href="/opinion/771014/united-states-of-amercia-v-christopher-drayton-clifton-brown-jr/#790" aria-description="Citation for case: United States of Amercia v. Christopher Drayton &amp; Clifton...">231 F. 3d, at 790</a></span> (noting that "[t]his case is controlled by" <i><span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">Guapi</a></span></i> and <i><span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/" aria-description="Citation for case: United States v. Washington">Washington</a></span>,</i> and dismissing any factual differences between the three cases as irrelevant). Under these cases, it appears that the Court of Appeals would suppress any evidence obtained during suspicionless drug interdiction efforts aboard buses in the absence of a warning that passengers may refuse to cooperate. The Court of Appeals erred in adopting this approach.</p>
<p>Applying the <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> framework to the facts of this particular case, we conclude that the police did not seize respondents when they boarded the bus and began questioning passengers. The officers gave the passengers no reason to believe that they were required to answer the officers' questions. When Officer Lang approached respondents, he <span class="star-pagination">*204</span> did not brandish a weapon or make any intimidating movements. He left the aisle free so that respondents could exit. He spoke to passengers one by one and in a polite, quiet voice. Nothing he said would suggest to a reasonable person that he or she was barred from leaving the bus or otherwise terminating the encounter.</p>
<p>There were ample grounds for the District Court to conclude that "everything that took place between Officer Lang and [respondents] suggests that it was cooperative" and that there "was nothing coercive [or] confrontational" about the encounter. App. 132. There was no application of force, no intimidating movement, no overwhelming show of force, no brandishing of weapons, no blocking of exits, no threat, no command, not even an authoritative tone of voice. It is beyond question that had this encounter occurred on the street, it would be constitutional. The fact that an encounter takes place on a bus does not on its own transform standard police questioning of citizens into an illegal seizure. See <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#439" aria-description="Citation for case: Florida v. Bostick">501 U. S., at 439-440</a></span>. Indeed, because many fellow passengers are present to witness officers' conduct, a reasonable person may feel even more secure in his or her decision not to cooperate with police on a bus than in other circumstances.</p>
<p>Respondents make much of the fact that Officer Lang displayed his badge. In <i>Florida</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#5" aria-description="Citation for case: Florida v. Rodriguez">469 U. S., at 5-6</a></span>, however, the Court rejected the claim that the defendant was seized when an officer approached him in an airport, showed him his badge, and asked him to answer some questions. Likewise, in <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#212" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 212-213</a></span> (1984), the Court held that Immigration and Naturalization Service (INS) agents' wearing badges and questioning workers in a factory did not constitute a seizure. And while neither Lang nor his colleagues were in uniform or visibly armed, those factors should have little weight in the analysis. Officers are often required to wear uniforms and in many circumstances this is cause for assurance, not discomfort. <span class="star-pagination">*205</span> Much the same can be said for wearing sidearms. That most law enforcement officers are armed is a fact well known to the public. The presence of a holstered firearm thus is unlikely to contribute to the coerciveness of the encounter absent active brandishing of the weapon.</p>
<p>Officer Hoover's position at the front of the bus also does not tip the scale in respondents' favor. Hoover did nothing to intimidate passengers, and he said nothing to suggest that people could not exit and indeed he left the aisle clear. In <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>,</i> the Court determined there was no seizure even though several uniformed INS officers were stationed near the exits of the factory. <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#219" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Id.,</i> at 219</a></span>. The Court noted: "The presence of agents by the exits posed no reasonable threat of detention to these workers, . . . the mere possibility that they would be questioned if they sought to leave the buildings should not have resulted in any reasonable apprehension by any of them that they would be seized or detained in any meaningful way." <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Ibid.</a></span></i> </p>
<p>Finally, the fact that in Officer Lang's experience only a few passengers have refused to cooperate does not suggest that a reasonable person would not feel free to terminate the bus encounter. In Lang's experience it was common for passengers to leave the bus for a cigarette or a snack while the officers were questioning passengers. App. 70, 81. And of more importance, bus passengers answer officers' questions and otherwise cooperate not because of coercion but because the passengers know that their participation enhances their own safety and the safety of those around them. "While most citizens will respond to a police request, the fact that people do so, and do so without being told they are free not to respond, hardly eliminates the consensual nature of the response." <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Delgado, supra,</i> at 216</a></span>.</p>
<p>Drayton contends that even if Brown's cooperation with the officers was consensual, Drayton was seized because no reasonable person would feel free to terminate the encounter with the officers after Brown had been arrested. The Court <span class="star-pagination">*206</span> of Appeals did not address this claim; and in any event the argument fails. The arrest of one person does not mean that everyone around him has been seized by police. If anything, Brown's arrest should have put Drayton on notice of the consequences of continuing the encounter by answering the officers' questions. Even after arresting Brown, Lang addressed Drayton in a polite manner and provided him with no indication that he was required to answer Lang's questions.</p>
<p>We turn now from the question whether respondents were seized to whether they were subjected to an unreasonable search, <i>i. e.,</i> whether their consent to the suspicionless search was involuntary. In circumstances such as these, where the question of voluntariness pervades both the search and seizure inquiries, the respective analyses turn on very similar facts. And, as the facts above suggest, respondents' consent to the search of their luggage and their persons was voluntary. Nothing Officer Lang said indicated a command to consent to the search. Rather, when respondents informed Lang that they had a bag on the bus, he asked for their permission to check it. And when Lang requested to search Brown and Drayton's persons, he asked first if they objected, thus indicating to a reasonable person that he or she was free to refuse. Even after arresting Brown, Lang provided Drayton with no indication that he was required to consent to a search. To the contrary, Lang asked for Drayton's permission to search him ("Mind if I check you?"), and Drayton agreed.</p>
<p>The Court has rejected in specific terms the suggestion that police officers must always inform citizens of their right to refuse when seeking permission to conduct a warrantless consent search. See, <i>e. g., </i><i>Ohio</i> v. <i>Robinette,</i> <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U. S. 33, 39-40</a></span> (1996); <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 227</a></span> (1973). "While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the <i>sine qua non</i> of an effective <span class="star-pagination">*207</span> consent." <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Ibid.</a></span></i> Nor do this Court's decisions suggest that even though there are no <i>per se</i> rules, a presumption of invalidity attaches if a citizen consented without explicit notification that he or she was free to refuse to cooperate. Instead, the Court has repeated that the totality of the circumstances must control, without giving extra weight to the absence of this type of warning. See, <i>e. g., </i><i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth, supra</a></span></i><i>; </i><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette"><i>Robinette, supra,</i> at 39-40</a></span>. Although Officer Lang did not inform respondents of their right to refuse the search, he did request permission to search, and the totality of the circumstances indicates that their consent was voluntary, so the searches were reasonable.</p>
<p>In a society based on law, the concept of agreement and consent should be given a weight and dignity of its own. Police officers act in full accord with the law when they ask citizens for consent. It reinforces the rule of law for the citizen to advise the police of his or her wishes and for the police to act in reliance on that understanding. When this exchange takes place, it dispels inferences of coercion.</p>
<p>We need not ask the alternative question whether, after the arrest of Brown, there were grounds for a <i>Terry</i> stop and frisk of Drayton, <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), though this may have been the case. It was evident that Drayton and Brown were traveling togetherOfficer Lang observed the pair reboarding the bus together; they were each dressed in heavy, baggy clothes that were ill-suited for the day's warm temperatures; they were seated together on the bus; and they each claimed responsibility for the single piece of green carry-on luggage. Once Lang had identified Brown as carrying what he believed to be narcotics, he may have had reasonable suspicion to conduct a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop and frisk on Drayton as well. That question, however, has not been presented to us. The fact the officers may have had reasonable suspicion does not prevent them from relying on a citizen's consent to the search. It would be a paradox, and one most puzzling to law enforcement officials and courts alike, were <span class="star-pagination">*208</span> we to say, after holding that Brown's consent was voluntary, that Drayton's consent was ineffectual simply because the police at that point had more compelling grounds to detain him. After taking Brown into custody, the officers were entitled to continue to proceed on the basis of consent and to ask for Drayton's cooperation.</p>
<p>The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Souter, with whom Justice Stevens and Justice Ginsburg join, dissenting.</p>
<p>Anyone who travels by air today submits to searches of the person and luggage as a condition of boarding the aircraft. It is universally accepted that such intrusions are necessary to hedge against risks that, nowadays, even small children understand. The commonplace precautions of air travel have not, thus far, been justified for ground transportation, however, and no such conditions have been placed on passengers getting on trains or buses. There is therefore an air of unreality about the Court's explanation that bus passengers consent to searches of their luggage to "enhanc[e] their own safety and the safety of those around them." <i>Ante,</i> at 205. Nor are the other factual assessments underlying the Court's conclusion in favor of the Government more convincing.</p>
<p>The issue we took to review is whether the police's examination of the bus passengers, including respondents, amounted to a suspicionless seizure under the Fourth Amendment.<sup>[1]</sup> If it did, any consent to search was plainly <span class="star-pagination">*209</span> invalid as a product of the illegal seizure. See <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#507" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 507-508</a></span> (1983) (plurality opinion) ("[T]he consent was tainted by the illegality and . . . ineffective to justify the search"); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#509" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 509</a></span> (Powell, J., concurring); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#509" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 509</a></span> (Brennan, J., concurring in result).</p>
<p><i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991), established the framework for determining whether the bus passengers were seized in the constitutional sense. In that case, we rejected the position that police questioning of bus passengers was a <i>per se</i> seizure, and held instead that the issue of seizure was to be resolved under an objective test considering all circumstances: whether a reasonable passenger would have felt "free to decline the officers' requests or otherwise terminate the encounter," <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#436" aria-description="Citation for case: Florida v. Bostick"><i>id.,</i> at 436</a></span>. We thus applied to a bus passenger the more general criterion, whether the person questioned was free "to ignore the police presence and go about his business," <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">id.,</a></span></i> at 437 (quoting <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#569" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 569</a></span> (1988)).</p>
<p>Before applying the standard in this case, it may be worth getting some perspective from different sets of facts. A perfect example of police conduct that supports no colorable claim of seizure is the act of an officer who simply goes up to a pedestrian on the street and asks him a question. See <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer">460 U. S., at 497</a></span>; see <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#523" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 523, n. 3</a></span> (Rehnquist, J., dissenting). A pair of officers questioning a pedestrian, <span class="star-pagination">*210</span> without more, would presumably support the same conclusion. Now consider three officers, one of whom stands behind the pedestrian, another at his side toward the open sidewalk, with the third addressing questions to the pedestrian a foot or two from his face. Finally, consider the same scene in a narrow alley. On such bare bones facts, one may not be able to say a seizure occurred, even in the last case, but one can say without qualification that the atmosphere of the encounters differed significantly from the first to the last examples. In the final instance there is every reason to believe that the pedestrian would have understood, to his considerable discomfort, what Justice Stewart described as the "threatening presence of several officers," <i>United States</i>  v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554</a></span> (1980) (opinion of Stewart, J.). The police not only carry legitimate authority but also exercise power free from immediate check, and when the attention of several officers is brought to bear on one civilian the imbalance of immediate power is unmistakable. We all understand this, as well as we understand that a display of power rising to Justice Stewart's "threatening" level may overbear a normal person's ability to act freely, even in the absence of explicit commands or the formalities of detention. As common as this understanding is, however, there is little sign of it in the Court's opinion. My own understanding of the relevant facts and their significance follows.</p>
<p>When the bus in question made its scheduled stop in Tallahassee, the passengers were required to disembark while the vehicle was cleaned and refueled. App. 104. When the passengers returned, they gave their tickets to the driver, who kept them and then left himself, after giving three police officers permission to board the bus in his absence. <i>Id.,</i> at 77-78. Although they were not in uniform, the officers displayed badges and identified themselves as police. One stationed himself in the driver's seat by the door at the front, facing back to observe the passengers. The two others went to the rear, from which they worked their way forward, <span class="star-pagination">*211</span> with one of them speaking to passengers, the other backing him up. <i>Id.,</i> at 47-48. They necessarily addressed the passengers at very close range; the aisle was only 15 inches wide, and each seat only 18.<sup>[2]</sup> The quarters were cramped further by the overhead rack, 19 inches above the top of the passenger seats. The passenger by the window could not have stood up straight, <i>id.,</i> at 55, and the face of the nearest officer was only a foot or 18 inches from the face of the nearest passenger being addressed, <i>id.,</i> at 57. During the exchanges, the officers looked down, and the passengers had to look up if they were to face the police. The officer asking the questions spoke quietly. He prefaced his requests for permission to search luggage and do a body patdown by identifying himself by name as a police investigator "conducting bus interdiction" and saying, "`We would like for your cooperation. Do you have any luggage on the bus?'" <i>Id.,</i> at 82.</p>
<p>Thus, for reasons unexplained, the driver with the tickets entitling the passengers to travel had yielded his custody of the bus and its seated travelers to three police officers, whose authority apparently superseded the driver's own. The officers took control of the entire passenger compartment, one stationed at the door keeping surveillance of all the occupants, the others working forward from the back. With one officer right behind him and the other one forward, a third officer accosted each passenger at quarters extremely close and so cramped that as many as half the passengers could not even have stood to face the speaker. None was asked whether he was willing to converse with the police or to take part in the enquiry. Instead the officer said the police were "conducting bus interdiction," in the course of which they "would like . . . cooperation." <i>Ibid.</i> The reasonable inference was that the "interdiction" was not a consensual exercise, but one the police would carry out whatever <span class="star-pagination">*212</span> the circumstances; that they would prefer "cooperation" but would not let the lack of it stand in their way. There was no contrary indication that day, since no passenger had refused the cooperation requested, and there was no reason for any passenger to believe that the driver would return and the trip resume until the police were satisfied. The scene was set and an atmosphere of obligatory participation was established by this introduction. Later requests to search prefaced with "Do you mind . . ." would naturally have been understood in the terms with which the encounter began.</p>
<p>It is very hard to imagine that either Brown or Drayton would have believed that he stood to lose nothing if he refused to cooperate with the police, or that he had any free choice to ignore the police altogether. No reasonable passenger could have believed that, only an uncomprehending one. It is neither here nor there that the interdiction was conducted by three officers, not one, as a safety precaution. See <i>id.,</i> at 47. The fact was that there were three, and when Brown and Drayton were called upon to respond, each one was presumably conscious of an officer in front watching, one at his side questioning him, and one behind for cover, in case he became unruly, perhaps, or "cooperation" was not forthcoming. The situation is much like the one in the alley, with civilians in close quarters, unable to move effectively, being told their cooperation is expected. While I am not prepared to say that no bus interrogation and search can pass the <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> test without a warning that passengers are free to say no, the facts here surely required more from the officers than a quiet tone of voice. A police officer who is certain to get his way has no need to shout.</p>
<p>It is true of course that the police testified that a bus passenger sometimes says no, App. 81, but that evidence does nothing to cast the facts here in a different light. We have no way of knowing the circumstances in which a passenger elsewhere refused a request; maybe that has happened only <span class="star-pagination">*213</span> when the police have told passengers they had a right to refuse (as the officers sometimes advised them), <i>id.,</i> at 81-82. Nor is it fairly possible to see the facts of this case differently by recalling <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984), as precedent. In that case, a majority of this Court found no seizure when a factory force was questioned by immigration officers, with an officer posted at every door leading from the workplace. <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#219" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Id.,</i> at 219</a></span>. Whether that opinion was well reasoned or not, the facts as the Court viewed them differed from the case here. <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span></i> considered an order granting summary judgment in favor of respondents, with the consequence that the Court was required to construe the record and all issues of fact favorably to the Immigration and Naturalization Service. See <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#214" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>id.,</i> at 214</a></span>; <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#221" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>id.,</i> at 221</a></span> (Stevens, J., concurring). The Court therefore emphasized that even after "th[e] surveys were initiated, the employees were about their ordinary business, operating machinery and performing other job assignments." <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#218" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Id.,</i> at 218</a></span>. In this case, however, Brown and Drayton were seemingly pinned-in by the officers and the customary course of events was stopped flat. The bus was going nowhere, and with one officer in the driver's seat, it was reasonable to suppose no passenger would tend to his own business until the officers were ready to let him.</p>
<p>In any event, I am less concerned to parse this case against <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span></i> than to apply <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i>'s totality of circumstances test, and to ask whether a passenger would reasonably have felt free to end his encounter with the three officers by saying no and ignoring them thereafter. In my view the answer is clear. The Court's contrary conclusion tells me that the majority cannot see what Justice Stewart saw, and I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   <i>Daniel J. Popeo</i> and <i>Richard A. Samp</i> filed a brief for the Washington Legal Foundation et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>Leon Friedman</i> and <i>Joshua L. Dratel</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p><i>James P. Manak, Wayne W. Schmidt, Richard Weintraub, Bernard J. Farber,</i> and <i>Carl Milazzo</i> filed a brief for Americans For Effective Law Enforcement, Inc., et al. as <i>amici curiae.</i> </p>
<p>[1]  The Court proceeds to resolve the voluntariness issue on the heels of its seizure enquiry, but the voluntariness of respondents' consent was not within the question the Court accepted for review. Accord, Reply Brief for United States 20, n. 7 (stating that the consent issue "is not presented by this case; the question here is whether there was an illegal seizure in the first place"). While it is true that the Eleventh Circuit purported to address the question "whether the consent given by each defendant for the search was `uncoerced and legally voluntary,' " <span class="citation" data-id="771014"><a href="/opinion/771014/united-states-of-amercia-v-christopher-drayton-clifton-brown-jr/#788" aria-description="Citation for case: United States of Amercia v. Christopher Drayton &amp; Clifton...">231 F. 3d 787, 788</a></span> (2000), elsewhere the court made it clear that it was applying the test in <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991), which is relevant to the issue of seizure, <span class="citation" data-id="771014"><a href="/opinion/771014/united-states-of-amercia-v-christopher-drayton-clifton-brown-jr/#791" aria-description="Citation for case: United States of Amercia v. Christopher Drayton &amp; Clifton...">231 F. 3d, at 791, n. 6</a></span>. There is thus no occasion here to reach any issue of consent untainted by seizure. If there were, the consent would have to satisfy the voluntariness test of <i>Schneckloth</i> v. <i>Bustamonte,</i>  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), which focuses on "the nature of a person's subjective understanding," <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#230" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>id.,</i> at 230</a></span>, and requires consideration of "the characteristics of the accused [in addition to] the details of the interrogation," <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>id.,</i>  at 226</a></span>.</p>
<p>[2]  The figures are from a Lodging filed by respondents (available in Clerk of Court's case file). The Government does not dispute their accuracy.</p>

</div>
```

---
