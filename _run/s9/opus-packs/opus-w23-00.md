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

## GROUP: _overhaul2/lake/cases/carman-v-carroll--8693292.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d547aec67277806f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "carman-v-carroll--8693292"}, "payload": {"all": [{"cite": "588 F. App'x 183", "page": "183", "reporter": "F. App'x", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "588"}], "display": "588 F. App'x 183", "official": {"cite": "588 F. App'x 183", "page": "183", "reporter": "F. App'x", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "588"}, "official_selection_present": true, "record_id": "carman-v-carroll--8693292"}}
{"assertion_id": "0adca4b436165483", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "carman-v-carroll--8693292"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "carman-v-carroll--8693292", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — carman-v-carroll--8693292

```json
{
  "schema_version": "s2.v1",
  "record_id": "carman-v-carroll--8693292",
  "stub": true,
  "status": "folded-alias",
  "identity": {
    "case_name": "Carman v. Carroll",
    "case_name_short": "Carman",
    "case_name_full": "Andrew CARMAN and Karen Carman v. Jeremy CARROLL",
    "input_case_name": "Carman v. Carroll",
    "court": "3d Cir. 2014",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": 8693292,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": "/opinion/8693292/carman-v-carroll/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "588 F. App'x 183",
      "volume": "588",
      "reporter": "F. App'x",
      "page": "183",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "588 F. App'x 183",
        "volume": "588",
        "reporter": "F. App'x",
        "page": "183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "588 F. App'x 183",
    "official_selection": {
      "court_class": "state",
      "selected": "588 F. App'x 183",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:44:11Z",
    "date_modified": "2026-07-07T01:43:35Z",
    "warnings": [
      "folded-alias: subsumed into carroll-v-carman--2750102 (packet-A Group-2); see _manifest.json folded_into + journal s6-dedupe-pointer"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:44:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:44:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:44:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:44:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/chapman-v-california--8428427.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5eefb05fe2468830", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "chapman-v-california--8428427"}, "payload": {"all": [{"cite": "137 S. Ct. 389", "page": "389", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "196 L. Ed. 2d 306", "page": "306", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "196"}, {"cite": "85 U.S.L.W. 3209", "page": "3209", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "85"}, {"cite": "2016 WL 4733855", "page": "4733855", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2016"}, {"cite": "2016 U.S. LEXIS 6528", "page": "6528", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2016"}], "display": null, "official": null, "official_selection_present": false, "record_id": "chapman-v-california--8428427"}}
{"assertion_id": "7e05e8113804bda4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "chapman-v-california--8428427"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "chapman-v-california--8428427", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — chapman-v-california--8428427

```json
{
  "schema_version": "s2.v1",
  "record_id": "chapman-v-california--8428427",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Chapman v. California",
    "case_name_short": "Chapman",
    "case_name_full": "Carl CHAPMAN v. CALIFORNIA.",
    "input_case_name": "Chapman v. California",
    "court": "unknown",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": "1967-03-27",
    "year": 1967,
    "docket": null,
    "cluster_id": 107359,
    "lead_opinion_id": 9423348,
    "sibling_ids": [
      107359,
      9423348,
      9423349,
      9423350
    ],
    "absolute_url": "/opinion/107359/chapman-v-california/",
    "identity_method": "panel-cluster-rekey",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "386 U.S. 18",
      "volume": "386",
      "reporter": "U.S.",
      "page": "18",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 824",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "824",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 705",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "705",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2198",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2198",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "386 U.S. 18",
        "volume": "386",
        "reporter": "U.S.",
        "page": "18",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 824",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "824",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 705",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "705",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2198",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2198",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "386 U.S. 18",
    "official_selection": {
      "court_class": "scotus",
      "selected": "386 U.S. 18",
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
    "date_created": "2026-07-06T05:44:36Z",
    "date_modified": "2026-07-11T05:53:27Z",
    "warnings": [
      "panel cluster re-key -> cluster 107359 (evidence: _run/s9/adjudications.jsonl F-S9-P2-CHAPMANCAL (UPHELD); 6 lake treatment-edges cluster 107359; cached merits text 107359.txt; prime GET clusters/107359 confirmed 386 U.S. 18/87 S. Ct. 824/1967)"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:44:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:44:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:44:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:44:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/coleman-v-alabama--108182.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7261085a64b01003", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "coleman-v-alabama--108182"}, "payload": {"all": [{"cite": "399 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "399"}, {"cite": "90 S. Ct. 1999", "page": "1999", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "90"}, {"cite": "26 L. Ed. 2d 387", "page": "387", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "1970 U.S. LEXIS 17", "page": "17", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1970"}], "display": null, "official": null, "official_selection_present": false, "record_id": "coleman-v-alabama--108182"}}
{"assertion_id": "d40340418c73d01e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "coleman-v-alabama--108182"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "coleman-v-alabama--108182", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — coleman-v-alabama--108182

```json
{
  "schema_version": "s2.v1",
  "record_id": "coleman-v-alabama--108182",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Coleman v. Alabama",
    "case_name_short": "Coleman",
    "case_name_full": "COLEMAN Et Al. v. ALABAMA",
    "input_case_name": "Coleman v. Alabama",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-06-22",
    "year": 1970,
    "docket": null,
    "cluster_id": 108182,
    "lead_opinion_id": 9424314,
    "sibling_ids": [],
    "absolute_url": "/opinion/108182/coleman-v-alabama/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "399 U.S. 1",
        "volume": "399",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1999",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1999",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 387",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "387",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 17",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "17",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "399 U.S. 1",
        "volume": "399",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1999",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1999",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 387",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "387",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 17",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "17",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:U.S."
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
    "date_created": "2026-07-06T13:52:25Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:52:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:52:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — coleman-v-alabama--108182

```
<opinion type="majority">
<author id="b39-4"><page-number citation-index="1" label="3">*3</page-number>Mr. Justice Brennan</author>
<p id="AoM">announced the judgment of the Court and delivered the following opinion.</p>
<p id="b39-5">Petitioners were convicted in an Alabama Circuit Court of assault with intent to murder in the shooting of one Reynolds after he and his wife parked their car on an Alabama highway to change a flat tire. The Alabama Court of Appeals affirmed, <span class="citation multiple-matches"><a href="/c/Ala.%20App./44/429/">44 Ala. App. 429</a></span>, <span class="citation" data-id="9689699"><a href="/opinion/1861967/coleman-v-state/" aria-description="Citation for case: Coleman v. State">211 So. 2d 917</a></span> (1968), and the Alabama Supreme Court denied review, <span class="citation multiple-matches"><a href="/c/Ala./282/725/">282 Ala. 725</a></span>, <span class="citation" data-id="7373473"><a href="/opinion/7452725/coleman-v-state/" aria-description="Citation for case: Coleman v. State">211 So. 2d 927</a></span> (1968). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./394/916/">394 U. S. 916</a></span> (1969). We vacate and remand.</p>
<p id="b39-6">Petitioners make two claims in this Court. First, they argue that they were subjected to a station-house lineup in circumstances so unduly prejudicial and conducive to irreparable misidentification as fatally to taint Reynolds’ in-court identifications of them at the trial. Second, they argue that the preliminary hearing prior to their indictment was a “critical stage” of the prosecution and that Alabama’s failure to provide them with appointed counsel at the hearing therefore unconstitutionally denied them the assistance of counsel.</p>
<p id="b39-7">I<footnotemark>1</footnotemark></p>
<p id="b39-8">The lineup of which petitioners complain was conducted on October 1, 1966, about two months after the assault and seven months before petitioners’ trial. Petitioners concede that since the lineup occurred before <em>United States </em>v. Wade, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>, and <em>Gilbert </em>v. <em>California, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>, were decided on June 12, 1967, they cannot invoke the holding of those cases requiring the exclusion of in-court identification evidence which is tainted by exhibiting the accused to identifying witnesses before trial in the absence of coun<page-number citation-index="1" label="4">*4</page-number>sel. <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#296" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 296-301</a></span> (1967). Rather, they argue that in the circumstances here the conduct of the lineup was so unduly prejudicial as fatally to taint Reynolds’ in-court identification of them. This is a claim that must be determined on the totality of the surrounding circumstances. <em>Stovall </em>v. <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#301" aria-description="Citation for case: Stovall v. Denno"><em>Denno, supra, </em>at 301-302</a></span>; <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968); <em>Foster </em>v. <em>California, </em><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U. S. 440</a></span> (1969).</p>
<p id="b40-6">At the trial Reynolds testified that at about 11:30 p. m. on July 24, 1966, he was engaged in changing a tire when three men approached from across the highway. One of them shot him from a short distance away. The three then ran up to within three or four feet. Reynolds arose from his stooped position and held on to his wife, who had left the car to watch him as he worked. One of the men put his hand on Mrs. Reynolds’ shoulder. Reynolds testified that this was Coleman. Within a few seconds a car with its lights on approached, and the three men turned and “ran across the road . . . .” As they turned to go, Reynolds was shot a second time. He identified petitioner Stephens as the gunman, stating that he saw him “in the car lights” while “looking straight at him.” Reynolds repeated on cross-examination his testimony on direct; he said he saw Coleman “face to face”; “I looked into his face,” “got a real good look at him.”</p>
<p id="b40-7">At the pretrial hearing on petitioners’ motion to suppress identification evidence, Detective Fordham testified that he had spoken briefly to Reynolds at the hospital two days after the assault and about two weeks later, and that on neither occasion was Reynolds able to provide much information about his assailants. At the hospital he gave a vague description — that the attackers were “young, black males, close to the same age and height.” Petitioners are both Negro; but Stephens was 18 and <em>6'2", </em>and Coleman, 28 and 5'4%". However, <page-number citation-index="1" label="5">*5</page-number>Detective Fordham also testified that at the time Reynolds gave this description he was in considerable pain, and that consequently the questioning was very brief. The detective further stated that Reynolds did not identify any of his assailants from mug shots, but it does not appear whether pictures of petitioners were among those shown him. Detective Hart testified that a lineup was held on October 1 at the request of the police. He stated that Reynolds identified petitioner Stephens spontaneously before the formal lineup even began. “[T]he six men were brought in by the warden, up on the stage, and as Otis Stephens — he didn’t get to his position on the stage, which was number one, when Mr. Reynolds identified him as being one of his assailants.” Reynolds gave similar testimony: “As soon as he stepped inside the door — I hadn’t seen him previous to then until he stepped inside the door, and I recognized him . . . . Just as soon as he stepped up on the stage, I said, ‘That man, there, is the one; he is the one that shot me.’ ” Reynolds also testified that he identified Coleman at the lineup before Coleman could act on a request Reynolds had made that the lineup participants speak certain words used by the attackers. Reynolds admitted that he did not tell Detective Hart of his identification until later during the lineup, and the detective stated he could not recall whether Reynolds told him of the identification before or after Coleman spoke the words.</p>
<p id="b41-5">It cannot be said on this record that the trial court erred in finding that Reynolds’ in-court identification of the petitioners did not stem from an identification procedure at the lineup “so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification.” <em>Simmons </em>v. <em>United States, supra, </em>at 384. Indeed, the court could find on the evidence adduced at the suppression hearing that Reynolds’ identifications were entirely based upon observations at the <page-number citation-index="1" label="6">*6</page-number>time of the assault and not at all induced by the conduct of the lineup. There is no merit in the three arguments offered by petitioners for a contrary conclusion.</p>
<p id="b42-5">First, Reynolds testified that when the police asked him to go to the city jail he “took [it] for granted” that the police had caught his assailants. But the record is utterly devoid of evidence that anything the police said or did prompted Reynolds' virtually spontaneous identification of petitioners among the lineup participants as the proceeding got under way.</p>
<p id="b42-6">Petitioners next contend that the lineup was unfair because they and their codefendant were the only ones required to say the words used by one of the attackers. There is some conflict in the testimony on this point. Petitioner Stephens testified that petitioners and their codefendant were the only ones who spoke the words. Reynolds testified that not all the men in the lineup spoke them. But Detective Hart stated that all the participants spoke the words. In any case, the court could find on the evidence that Reynolds identified both petitioners before either said anything, and that therefore any failure to require the other participants to say the same words did not aid or influence his identifications.</p>
<p id="b42-7">Finally, petitioner Coleman contends that he was unfairly singled out to wear a hat though all the other participants were bareheaded. One of the attackers had worn a hat. Although the record demonstrates that Coleman did in fact wear a hat at the lineup, nothing in the record shows that he was required to do so. Moreover, it does not appear that Reynolds’ identification of Coleman at the lineup was based on the fact that he remembered that Coleman had worn a hat at the time of the assault. On the contrary, the court could conclude from his testimony that Reynolds “asked them to make John Henry Coleman to take his hat off, or move it back,” because he wanted to see Coleman’s face more clearly.</p>
<p id="b43-4"><page-number citation-index="1" label="7">*7</page-number>II<footnotemark>2</footnotemark></p>
<p id="b43-5">This Court has held that a person accused of crime “requires the guiding hand of counsel at every step in the proceedings against him,” <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#69" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 69</a></span> (1932), and that that constitutional principle is not limited to the presence of counsel at trial. “It is central to that principle that in addition to counsel’s presence at trial, the accused is guaranteed that he need not stand alone against the State at any stage of the prosecution, formal or informal, in court or out, where counsel’s absence might derogate from the accused’s right to a fair trial.” <em>United States </em>v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#226" aria-description="Citation for case: United States v. Wade"><em>Wade, supra, </em>at 226</a></span>. Accordingly, “the principle of <em>Powell </em>v. <em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Alabama</a></span> </em>and succeeding cases requires that we scrutinize <em>any </em>pretrial confrontation of the accused to determine whether the presence of his counsel is necessary to preserve the defendant’s basic right to a fair trial as affected by his right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself. It calls upon us to analyze whether potential substantial prejudice to defendant’s rights inheres in the particular confrontation and the ability of counsel to help avoid that prejudice.” <em>Id., </em>at 227. Applying this test, the Court has held that “critical stages” include the pretrial type of arraignment where certain rights may be sacrificed or lost, <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/#54" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52, 54</a></span> (1961), see <em>White </em>v. <em>Maryland, </em><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span> (1963), and the pretrial lineup, <em>United States </em>v. <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra;</a></span> Gilbert </em>v. <em>California, supra. </em>Cf. <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), where the Court held that the privilege against compulsory self-incrimination includes a right to counsel at a pretrial custodial interrogation. See also <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964).</p>
<p id="b44-4"><page-number citation-index="1" label="8">*8</page-number>The preliminary hearing is not a required step in an Alabama prosecution. The prosecutor may seek an indictment directly from the grand jury without a preliminary hearing. <em>Ex parte Campbell, </em><span class="citation" data-id="1586036"><a href="/opinion/1586036/ex-parte-campbell/" aria-description="Citation for case: Ex Parte Campbell">278 Ala. 114</a></span>, <span class="citation" data-id="1586036"><a href="/opinion/1586036/ex-parte-campbell/" aria-description="Citation for case: Ex Parte Campbell">176 So. 2d 242</a></span> (1965). The opinion of the Alabama Court of Appeals in this case instructs us that under Alabama law the sole purposes of a preliminary hearing are to determine whether there is sufficient evidence against the accused to warrant presenting his case to the grand jury, and, if so, to fix bail if the offense is bailable. <span class="citation" data-id="9689699"><a href="/opinion/1861967/coleman-v-state/#433" aria-description="Citation for case: Coleman v. State">44 Ala. App., at 433</a></span>, 211 So. 2d, at 920. See Ala. Code, Tit. 15, §§ 139, 140, 151.<footnotemark>3</footnotemark> The court continued:</p>
<blockquote id="b44-5">“At the preliminary hearing . . . the accused is not required to advance any defenses, and failure to do so does not preclude him from availing himself of every defense he may have upon the trial of the case. Also Pointer v. State of Texas [<span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span> (1965)] bars the admission of testimony given at a pre-trial proceeding where the accused did not have the benefit of cross-examination by and through counsel. Thus, nothing occurring at the preliminary hearing in absence of counsel can substantially prejudice the rights of the accused on trial.” <span class="citation" data-id="9689699"><a href="/opinion/1861967/coleman-v-state/#433" aria-description="Citation for case: Coleman v. State">44 Ala. App., at 433</a></span>, 211 So. 2d, at 921.</blockquote>
<p id="b45-3"><page-number citation-index="1" label="9">*9</page-number>This Court is of course bound by this construction of the governing Alabama law, <em>Kingsley International Pictures Corp. </em>v. <em>Regents, </em><span class="citation" data-id="9421871"><a href="/opinion/105937/kingsley-international-pictures-corp-v-regents-of-the-university/#688" aria-description="Citation for case: Kingsley International Pictures Corp. v. Regents of the...">360 U. S. 684, 688</a></span> (1959); <em>Albertson </em>v. <em>Millard, </em><span class="citation" data-id="9420914"><a href="/opinion/105105/albertson-v-millard-attorney-general/#244" aria-description="Citation for case: Albertson v. Millard, Attorney General">345 U. S. 242, 244</a></span> (1953). However, from the fact that in cases where the accused has no lawyer at the hearing the Alabama courts prohibit the State’s use at trial of anything that occurred at the hearing, it does not follow that the Alabama preliminary hearing is not a “critical stage” of the State’s criminal process. The determination whether the hearing is a “critical stage” requiring the provision of counsel depends, as noted, upon an analysis “whether potential substantial prejudice to defendant’s rights inheres in the . . . confrontation and the ability of counsel to help avoid that prejudice.” <em>United States </em>v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#227" aria-description="Citation for case: United States v. Wade"><em>Wade, supra, </em>at 227</a></span>. Plainly the guiding hand of counsel at the preliminary hearing is essential to protect the indigent accused against an erroneous or improper prosecution. First, the lawyer’s skilled examination and cross-examination of witnesses may expose fatal weaknesses in the State’s case that may lead the magistrate to refuse to bind the accused over. Second, in any event, the skilled interrogation of witnesses by an experienced lawyer can fashion a vital impeachment tool for use in cross-examination of the State’s witnesses at the trial, or preserve testimony favorable to the accused of a witness who does not appear at the trial. Third, trained counsel can more effectively discover the case the State has against his client and make possible the preparation of a proper defense to meet that case at the trial. Fourth, counsel can also be influential at the preliminary hearing in making effective arguments for the accused on such matters as the necessity for an early psychiatric examination or bail.</p>
<p id="b45-4">The inability of the indigent accused on his own to realize these advantages of a lawyer’s assistance compels <page-number citation-index="1" label="10">*10</page-number>the conclusion that the Alabama preliminary hearing is a "critical- stage” of the State’s criminal process at which the accused is "as much entitled to such aid [of counsel] ... as at the trial itself.” <em>Powell </em>v. <em>Alabama, supra, </em>at 57.</p>
<p id="b46-4">Ill<footnotemark>4</footnotemark></p>
<p id="b46-5">There remains, then, the question of the relief to which petitioners are entitled. The trial transcript indicates that the prohibition against use by the State at trial of anything that occurred at the preliminary hearing was scrupulously observed.<footnotemark>5</footnotemark> Cf. <em>White </em>v. <em><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">Maryland, supra.</a></span> </em>But on the record it cannot be said <page-number citation-index="1" label="11">*11</page-number>whether or not petitioners were otherwise prejudiced by the absence of counsel at the preliminary hearing. That inquiry in the first instance should more properly be made by the Alabama courts. The test to be applied is whether the denial of counsel at the preliminary hearing was harmless error under <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). See <em>United States </em>v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#242" aria-description="Citation for case: United States v. Wade"><em>Wade, supra, </em>at 242</a></span>.</p>
<p id="b47-5">We accordingly vacate the petitioners’ convictions and remand the case to the Alabama courts for such proceedings not inconsistent with this opinion as they may deem appropriate to determine whether such denial of counsel was harmless error, see <em>Gilbert </em>v. <em>California, supra, </em>at 272, and therefore whether the convictions should be reinstated or a new trial ordered.</p>
<p id="b47-6">
<em>It is so ordered.</em>
</p>
<judges id="b47-7">Mr. Justice Blacicmun took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b39-9">Mr. Justice Douglas, Me. Justice White, and Mr. Justice Marshall join this Part I.</p>
</footnote>
<footnote label="2">
<p id="b43-6"> Mr. Justice Douglas, Mr. Justice White, and Mr. Justice Marshall join this Part II.</p>
</footnote>
<footnote label="3">
<p id="b44-6"> A textbook, Criminal Procedure in Alabama, by M. Clinton McGee (University of Alabama Press 1954), p. 41, states:</p>
<blockquote id="b44-7">“A preliminary hearing or examination is not a trial in its ordinary sense nor is it a final determination of guilt. It is a proceeding whereby an accused is discharged or held to answer, as the facts warrant. It seeks to determine whether there is probable cause for believing that a crime has been committed and whether the accused is probably guilty, in order that he may be informed of the nature of such charge and to allow the state to take the necessary steps to bring him to trial. Such hearing also serves to perpetuate evidence and to keep the necessary witnesses within the control of the state. It also safeguards the accused against groundless and vindictive prosecutions, and avoids for both the accused and the state the expense and inconvenience of a public trial.”</blockquote>
</footnote>
<footnote label="4">
<p id="b46-6"> Mr. Justice Black, Mr. Justice Douglas, Mr. Justice White, and Mr. Justice Marshall join this Part III.</p>
</footnote>
<footnote label="5">
<p id="b46-7"> The trial judge held a hearing two months before the trial on motions on behalf of petitioners to suppress “any evidence or discovery whatsoever obtained ... on the preliminary hearing . . . and further any statements relating to any identification . . . during any line-up . . . .” The State conceded that the motion should be granted as to any statements of either petitioner taken by the police upon their arrests, and written and oral confessions made by them were therefore not offered at the trial. At an early stage of the hearing on the motions, the trial judge said:</p>
<blockquote id="b46-8">“It has been my consistent ruling, and I don’t know of any law to the contrary, that, on the basis of what happened at the preliminary hearing, that if a lawyer was not representing the defendant that anything that may have occurred at that preliminary which might work against the defendant, whether it be anything he said there, assuming he might have taken the stand, anything of that nature, would, on the trial of the case on the merits, be inadmissible.</blockquote>
<blockquote id="b46-9">“I wouldn’t anticipate the State offering anything like that, but that has been my ruling on that ever since we changed some of our ways of doing things.</blockquote>
<blockquote id="b46-10">“It wouldn’t be material from the standpoint that a man down there, when not represented by counsel on the preliminary, made some statement, said, 'I am guilty.’ You know, a lot of times he might say, T am guilty.’</blockquote>
<blockquote id="b46-11">“That that would not be admissible if he weren’t represented by counsel, and that sort of thing.”</blockquote>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/commonwealth-v-serge--2074658.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ee7d03293581de70", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "commonwealth-v-serge--2074658"}, "payload": {"all": [{"cite": "896 A.2d 1170", "page": "1170", "reporter": "A.2d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "896"}, {"cite": "586 Pa. 671", "page": "671", "reporter": "Pa.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "586"}, {"cite": "2006 Pa. LEXIS 561", "page": "561", "reporter": "Pa. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2006"}], "display": null, "official": null, "official_selection_present": false, "record_id": "commonwealth-v-serge--2074658"}}
{"assertion_id": "51b669280d4742e8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "commonwealth-v-serge--2074658"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "commonwealth-v-serge--2074658", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — commonwealth-v-serge--2074658

```json
{
  "schema_version": "s2.v1",
  "record_id": "commonwealth-v-serge--2074658",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Commonwealth v. Serge",
    "case_name_short": "Com.",
    "case_name_full": "COMMONWEALTH of Pennsylvania, Appellee v. Michael SERGE, Appellant",
    "input_case_name": "Commonwealth v. Serge",
    "court": "Pa. 2006",
    "court_id": "pa",
    "court_level": "state",
    "circuit": null,
    "state": "pa",
    "date_decided": "2006-04-25",
    "year": 2006,
    "docket": "150 MAP 2004",
    "cluster_id": 2074658,
    "lead_opinion_id": 9711444,
    "sibling_ids": [],
    "absolute_url": "/opinion/2074658/commonwealth-v-serge/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "896 A.2d 1170",
        "volume": "896",
        "reporter": "A.2d",
        "page": "1170",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "586 Pa. 671",
        "volume": "586",
        "reporter": "Pa.",
        "page": "671",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 Pa. LEXIS 561",
        "volume": "2006",
        "reporter": "Pa. LEXIS",
        "page": "561",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "896 A.2d 1170",
        "volume": "896",
        "reporter": "A.2d",
        "page": "1170",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "586 Pa. 671",
        "volume": "586",
        "reporter": "Pa.",
        "page": "671",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 Pa. LEXIS 561",
        "volume": "2006",
        "reporter": "Pa. LEXIS",
        "page": "561",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "state",
      "selected": null,
      "reason": "same_rank_tie"
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
    "date_created": "2026-07-06T05:44:50Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:45:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:45:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:45:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:45:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — commonwealth-v-serge--2074658

```
<opinion type="majority">
<p id="b884-14">
<em>OPINION</em>
</p>
<author id="b884-15">Justice NEWMAN.</author>
<p id="b884-16">Michael Serge (Appellant) appeals the sentence of life imprisonment entered by the Court of Common Pleas of Lacka<page-number citation-index="1" label="677">*677</page-number>wanna County (trial court) following his conviction for first-degree murder, 18 Pa.C.S. § 2502(a). We granted allowance of appeal in this case to consider the admissibility of a computer-generated animation (CGA) illustrating the Commonwealth’s theory of the homicide. For the reasons discussed herein, we hold that the trial court properly admitted the CGA as demonstrative evidence.</p>
<p id="b885-4">
<em>FACTS AND PROCEDURAL HISTORY</em>
</p>
<p id="b885-5">On the morning of January 15, 2001, Appellant shot his wife, Jennifer Serge (Victim), three times, killing her inside their home in Scott Township, Lackawanna County. Appellant was arrested that morning and charged with one count of first-degree murder, 18 Pa.C.S. § 2502(a), and one count of third-degree murder, 18 Pa.C.S. § 2502(c).</p>
<p id="b885-6">On June 18, 2001, prior to trial, the Commonwealth filed a Motion <em>in limine, </em>seeking to present the prosecution’s theory of the fatal shooting through a CGA based on both forensic and physical evidence.<footnotemark>1</footnotemark> On September 14, 2001, <page-number citation-index="1" label="678">*678</page-number>following an evidentiary hearing, the trial court granted the Commonwealth’s Motion <em>in limine </em>provided that certain evidentiary foundations were established at trial.<footnotemark>2</footnotemark> <em>Common</em><page-number citation-index="1" label="679">*679</page-number><em>wealth v. Serge, </em><span class="citation" data-id="6388367"><a href="/opinion/6514793/commonwealth-v-serge/" aria-description="Citation for case: Commonwealth v. Serge">58 Pa. D. &amp; C.4th 52</a></span> (C.P. Lackawanna 2001). The trial court required the Commonwealth to authenticate the animation as both a fair and accurate depiction of expert reconstructive testimony and exclude any inflammatory features that may cause unfair prejudice. To safeguard against potential prejudice, the trial court required the pre-trial disclosure of the CGA.</p>
<p id="b887-4">At his jury trial held January 29, 2002 to February 12, 2002, Appellant alleged that he had acted in self-defense as his wife attacked him with a knife. He further asserted that he should be acquitted on the grounds of justifiable self-defense. Alternatively, Appellant argued that his extreme intoxication at the time of the shooting rendered him incapable of formulating the specific intent to kill.</p>
<p id="b887-5">The Commonwealth countered that the killing was intentional, and that Appellant, a former Lieutenant of Detectives with the Scranton Police Department, “used his decades of experience as a police officer to tamper with the crime scene to stage a self-defense setting.” Trial Ct. Op. 8/19/05 p. 5. In particular, the Commonwealth asserted that Appellant had moved his wife’s body and strategically positioned her near a knife that he had placed on the floor, as depicted in the CGA.</p>
<p id="b887-6">On February 7, 2002, during its case-in-chief, the Commonwealth presented a CGA as demonstrative evidence to illustrate the expert opinions of its forensic pathologist, Gary W. Ross, M.D. (Dr. Ross), and crime scene reconstructionist, Trooper Brad R. Beach (Trooper Beach). The CGA showed the theory of the Commonwealth based upon the forensic and physical evidence, of how Appellant shot his wife first in the lower back and then through the heart as she knelt on the living room floor of their home. More importantly, the animation showed the location of Appellant and his wife within the living room, the positioning of their bodies, and the sequence, <page-number citation-index="1" label="680">*680</page-number>path, trajectory, and impact sites of the bullets fired from the handgun.</p>
<p id="b888-5">The trial court thoroughly instructed the jury of the purely demonstrative nature of the CGA both before the animation was presented and during the jury charge prior to deliberation. In particular, the court noted that the CGA was a demonstrative exhibit, not substantive evidence, and it was being offered solely as an illustration of the Commonwealth’s version of the events as recreated by Dr. Ross and Trooper Beach. Finally, the court informed the jury that they should not confuse art with reality and should not view the CGA as a definitive recreation of the actual incident.</p>
<p id="b888-6">On February 12, 2002, the jury found Appellant guilty of first-degree murder and the trial court immediately sentenced him to life imprisonment. Appellant filed a timely appeal, challenging several of the jury instructions and evidentiary rulings of the trial court. In a published Opinion filed December 3, 2002, the Superior Court affirmed the trial court’s Judgment of Sentence. <em>Commonwealth v. Serge, </em><span class="citation" data-id="1991045"><a href="/opinion/1991045/commonwealth-v-serge/" aria-description="Citation for case: Commonwealth v. Serge">837 A.2d 1255</a></span> (Pa.Super.2003). On August 25, 2004, we granted allowance of appeal limited solely to the issue of whether the admission of the CGA depicting the Commonwealth’s theory of the case was proper. The admissibility of a CGA is an issue of first impression in the Commonwealth.</p>
<p id="b888-7">
<em>DISCUSSION</em>
</p>
<p id="b888-8">We determine that, for the reasons below, a CGA is admissible evidence in this Commonwealth. In particular, CGA evidence must be weighed by the same criteria of admissibility; namely, probative value versus prejudicial effect to which all other evidence is subject. Notably, certain concerns prior to admission carry more weight and deserve closer scrutiny when admitting CGA evidence than more traditional forms of evidence.</p>
<p id="b888-9">Appellant argues that the trial court erred in allowing the Commonwealth to present a CGA, which was used to introduce evidence of the Commonwealth’s theory of the killing. <page-number citation-index="1" label="681">*681</page-number>Appellant alleges that the Commonwealth’s use of the CGA: (1) lacked proper authentication; (2) lacked proper foundation; and (8) was, essentially, cumulative and unfairly prejudicial. The Commonwealth counters this argument and posits that the trial court properly admitted the CGA as demonstrative evidence used to explain or illustrate the testimony of its expert witnesses and should be subject to the same rules of admissibility as any other demonstrative evidence.</p>
<p id="b889-5">Society has become increasingly dependent upon computers in business and in our personal lives. With each technological advancement, the practice of law becomes more sophisticated and, commensurate with this progress, the legal system must adapt. Courts are facing the need to shed any technophobia and become more willing to embrace the advances that have the ability to enhance the efficacy of the legal system. However, before we are too quick to differentiate CGA’s or create a special test for their admission, it must be noted that the rules for analyzing the admission of such evidence have been previously established. In particular, a CGA should be treated equivalently to any other demonstrative exhibit or graphic representation and, thus, a CGA should be admissible if it satisfies the requirements of Pa.R.E. 401, 402, 403, and 901.<footnotemark>3</footnotemark> <em>See State v. Tollardo, </em><span class="citation" data-id="2584030"><a href="/opinion/2584030/state-v-tollardo/" aria-description="Citation for case: State v. Tollardo">134 N.M. 430</a></span>, <span class="citation" data-id="2584030"><a href="/opinion/2584030/state-v-tollardo/#1029" aria-description="Citation for case: State v. Tollardo">77 P.3d 1023, 1029</a></span> (Ct.App.2003) (opining that, “[wjhen the [CGA] is used to illustrate an opinion that an expert has arrived at without using the computer, the fact that the visual aid was generated by a computer ... does not matter because the witness can be questioned and cross-examined concerning <page-number citation-index="1" label="682">*682</page-number>the perceptions or opinions to which the witness testifies. In that situation, the computer is no more or less than a drafting device.”); <em>People v. McHugh, </em><span class="citation" data-id="6204462"><a href="/opinion/6335881/people-v-mchugh/" aria-description="Citation for case: People v. McHugh">124 Misc.2d 559</a></span>, <span class="citation" data-id="6204462"><a href="/opinion/6335881/people-v-mchugh/#722" aria-description="Citation for case: People v. McHugh">476 N.Y.S.2d 721, 722</a></span> (N.Y.Sup. Gen. Term 1984) (“Whether a diagram is hand drawn or mechanically drawn by means of a computer is of no importance.”).</p>
<p id="b890-5">There are three basic types of evidence that are admitted into court: (1) testimonial evidence; (2) documentary evidence; and (3) demonstrative evidence. 2 McCormick on Evidence § 212 (5th ed. 1999). Presently, at issue is demonstrative evidence, which is “tendered for the purpose of rendering other evidence more comprehensible to the trier of fact.” <em>Id. </em>As in the admission of any other evidence, a trial court may admit demonstrative evidence whose relevance outweighs any potential prejudicial effect. <em>Commonwealth v. Reid, </em><span class="citation" data-id="9757161"><a href="/opinion/2348536/commonwealth-v-reid/" aria-description="Citation for case: Commonwealth v. Reid">571 Pa. 1</a></span>, <span class="citation" data-id="9757161"><a href="/opinion/2348536/commonwealth-v-reid/#552" aria-description="Citation for case: Commonwealth v. Reid">811 A.2d 530, 552</a></span> (2002), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./540/850/">540 U.S. 850</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./124/131/">124 S.Ct. 131</a></span>, <span class="citation" data-id="131807"><a href="/opinion/131807/brown-v-hanks-superintendent-wabash-valley-correctional-facility/" aria-description="Citation for case: Brown v. Hanks, Superintendent, Wabash Valley...">157 L.Ed.2d 92</a></span> (2003). The offering party must authenticate such evidence. “The requirement of authentication or identification as a condition precedent to admissibility is satisfied by evidence sufficient to support a finding that the matter in question is what its proponent claims.” Pa.R.E. 901(a). Demonstrative evidence may be authenticated by testimony from a witness who has knowledge “that a matter is what it is claimed to be.” Pa.R.E. 901(b)(1). Demonstrative evidence such as photographs, motion pictures, diagrams, and models have long been permitted to be entered into evidence provided that the demonstrative evidence fairly and accurately represents that which it purports to depict. <em>See Nyce v. Muffley, </em><span class="citation" data-id="9762077"><a href="/opinion/2379041/nyce-v-muffley/" aria-description="Citation for case: Nyce v. Muffley">384 Pa. 107</a></span>, <span class="citation" data-id="9762077"><a href="/opinion/2379041/nyce-v-muffley/#532" aria-description="Citation for case: Nyce v. Muffley">119 A.2d 530, 532</a></span> (1956).</p>
<p id="b890-6">The overriding principle in determining if any evidence, including demonstrative, should be admitted involves a weighing of the probative value versus prejudicial effect. We have held that the trial court must decide first if the evidence is relevant and, if so, whether its probative value outweighs its prejudicial effect. <em>Commonwealth v. Hawk, </em><span class="citation" data-id="9710461"><a href="/opinion/2070811/commonwealth-v-hawk/" aria-description="Citation for case: Commonwealth v. Hawk">551 Pa. 71</a></span>, <span class="citation" data-id="9710461"><a href="/opinion/2070811/commonwealth-v-hawk/#376" aria-description="Citation for case: Commonwealth v. Hawk">709 A.2d 373, 376</a></span> (1998). This Commonwealth defines relevant evidence as “having any tendency to make the existence of any fact that is of consequence to the determination of the action <page-number citation-index="1" label="683">*683</page-number>more probable or less probable than it would be without the evidence.” Pa.R.E. 401. Relevant evidence may nevertheless be excluded “if its probative value is outweighed by the danger of unfair prejudice, confusion of the issues, or misleading the jury, or by considerations of undue delay, waste of time, or needless presentation of cumulative evidence.” Pa.R.E. 403.</p>
<p id="b891-5">At issue is both the basis and form of the demonstrative evidence offered. An expert witness may offer testimony other than opinions. Pa.R.E. 702 provides that an expert witness may testify “in the form of an opinion or otherwise.” (Emphasis added). An important function of an expert witness is to educate the jury on a subject about which the witness has specialized knowledge but the jury does not. <em>See Binder on Pennsylvania Evidence, </em>Third Ed., § 7.02, p. 314 (Pa.Bar.Inst. 2003). To help perform the function of educating a jury, an expert witness may use various forms of demonstrative evidence.</p>
<p id="b891-6">Demonstrative evidence continues to evolve as society advances technologically. Medical witnesses use computerized axial tomography, i.e. CAT scans, and magnetic resonance imaging instead of, or with, traditional x-rays. Forensic pathologists previously used only blood types in an attempt to bolster their testimony and implicate a defendant, but now use specific DNA matches to prove the statistical probability that a defendant was, by virtue of biological evidence at the scene of a crime, present at some point in time. <em>See Commonwealth v. Blasioli, </em><span class="citation" data-id="1902378"><a href="/opinion/1902378/commonwealth-v-blasioli/" aria-description="Citation for case: Commonwealth v. Blasioli">552 Pa. 149</a></span>, <span class="citation" data-id="1902378"><a href="/opinion/1902378/commonwealth-v-blasioli/" aria-description="Citation for case: Commonwealth v. Blasioli">713 A.2d 1117</a></span> (1998) (accepting the use of DNA matching of blood and semen to prove the statistical probability that the blood and semen found on the victim after an alleged rape was that of the defendant).</p>
<p id="b891-7">The law has been flexible enough to accommodate scientific progress and technological advances in all fields, and should continue to do so.<footnotemark>4</footnotemark> Pa.R.E. 702 permits expert testimony if it <page-number citation-index="1" label="684">*684</page-number>“will assist the .trier of fact to understand the evidence or to determine a fact in issue[.]” Such expert testimony is not limited to that which is purely verbal; rather, it includes pertinent illustrative adjuncts that help explain the testimony of one or more expert witnesses.<footnotemark>5</footnotemark></p>
<p id="b892-4">Presently, had the Commonwealth’s experts, a crime scene reconstructionist and a pathologist, used traditional methods, they may have drawn chalk diagrams or sketches on a blackboard to help explain the basis for their opinions. Instead, they used a CGA to more concisely and more clearly present their opinion. The difference is one of mode, not meaning. The law does not, and should not, prohibit proficient professional employment of new technology in the courtroom. This is, after all, the twenty-first century. As such, we must turn to the traditional factors considered in determining if a particular CGA is admissible.</p>
<p id="b893-3"><page-number citation-index="1" label="685">*685</page-number>Therefore, despite the relative novelty of CGA evidence, the evaluation of its admissibility relates back to this long-standing evaluation of probative value versus prejudicial value. G. Joseph, <em>A Simplified Approach to Computer-Generated Evidence and Animations, </em>43 N.Y.L. Sch. L.Rev. 875 (1999-2000) (stating that, “[a]t its simplest, an animation is merely a sequence of illustrations that, when filmed, videotaped or computer-generated, creates the illusion that the illustrated objects are in motion. Traditionally — because they are drawings — animations have been subjected to the fair-and-accurate-portrayal test and have been admitted, within the trial judge’s discretion, generally for illustrative purposes.”) As a preliminary matter, a CGA should be deemed admissible as demonstrative evidence if it: (1) is properly authenticated pursuant to Pa.R.E. 901 as a fair and accurate representation of the evidence it purports to portray; (2) is relevant pursuant to Pa.R.E. 401 and 402; and (3) has a probative value that is not outweighed by the danger of unfair prejudice pursuant to Pa.R.E. 403. However, new factors must be considered when evaluating a CGA. In particular, in determining the admissibility of a CGA the courts must address the additional dangers and benefits this particular type of demonstrative evidence presents as compared with more traditional demonstrative evidence.<footnotemark>6</footnotemark> As a result, the court must, as discussed <em>infra, </em>issue limiting instructions to the jury explaining the nature of the specific CGA.</p>
<p id="b893-4">It should be noted that conspicuously absent among the factors to be considered in determining the relevancy and <page-number citation-index="1" label="686">*686</page-number>prejudice of evidence is the potency of the evidence. Thus, although the use of illustrative demonstrative evidence by an expert, such as a CGA, may help explain his or her opinion and make the testimony more persuasive than it otherwise might have been, it is not proper grounds for excluding this relevant evidence.</p>
<p id="b894-4">Here, both the trial court and the Superior Court determined that the Commonwealth had satisfied all foundational requirements for admitting the animation and therefore it was properly admitted as demonstrative evidence. After applying the three-prong test noted above, we agree.</p>
<p id="b894-5">Appellant initially argues that the Commonwealth did not properly authenticate the CGA. Pa.R.E. 901(a) provides, “The requirement of authentication or identification as a condition precedent to admissibility is satisfied by evidence sufficient to support a finding that the matter in question is what its proponent claims.” <em>See also </em>A. Albrecht, <em>Laying a Proper Foundation for Computer-Generated Demonstrative Evidence, </em><span class="citation no-link">90 Ill. B.J. 261</span> (2002) (stating that “courts have said that computer-generated demonstrative evidence must be relevant and authenticated by testimony that (a) the witness has personal knowledge of the exhibit’s subject matter and (b) the exhibit is accurate____To lay a proper foundation for computer-generated visual evidence, the proponent must first establish through witness testimony the accuracy of the exhibit’s portrayal of the substantive information in question.”)</p>
<p id="b894-7">In authenticating the CGA, the Commonwealth presented the testimony of multiple individuals, including: (1) Randy Matzkanin (Matzkanin), the Director of Operations for 21st Century Forensic Animations; (2) Trooper Beach; and (3) Dr. Ross. Additionally, Patrolman Jared Ganz, Patrolman Joseph Zegalia, Trooper George Scochin, Trooper Connie Devens, and Trooper Gustas testified at trial concerning the physical evidence and the measurements taken at the crime scene, both of which were used in creating the CGA. Further, the creator of the CGA testified at the Motion <em>in limine </em>hearing that the CGA was a graphical presentation of another expert’s opinion, <page-number citation-index="1" label="687">*687</page-number>not the conclusions or calculations of a computer or himself. N.T. 7/30/01 at 25-27, 36, 54-55, 59, 63-64, 72, 77.</p>
<p id="b895-4">Matzkanin described the process employed in making the animation and testified that it was a strict depiction of the Commonwealth’s forensic evidence and expert opinions. Matzkanin stated that he used the expert opinions provided by Trooper Beach and Dr. Ross as well as the measurements gathered at the crime scene. N.T. 2/7/02 p. 135-37. Moreover, Matzkanin discussed both the computer software and hardware that created the three dimensional CGA drawings and their general use in the field. <em>Id. </em>at 140-43. Matzkanin, at the questioning of the Commonwealth, carefully explained the differences between a CGA and a simulation. <em>Id. </em>at 141-42. Matzkanin stated that he began working on the project at the end of January 2001, or beginning of February 2001, and continued until December 20, 2001. <em>Id. </em>at 134-35. During his testimony, Matzkanin explained that photos are used to reconstruct the room, including color and the like, but the major factor in recreation is the measurements. <em>Id. </em>at 136. However, Matzkanin explained that the character depictions are more difficult because of the stock models used by the company to represent people. <em>Id. </em>He further testified that the models do not represent the defendants. <em>Id. </em>at 137. Next, the CGA is created in a rough draft and sent to the Commonwealth for further input. Matzkanin could not recall the exact number of versions created but specified that many changes were made to ensure that the CGA conformed to the opinions of Trooper Beach and Dr. Ross. Matzkanin further explained that drawings are recorded in time intervals of thirty frames per second and thereafter transferred onto a DVD or video tape to create the image of motion. <em>Id. </em>at 139, 141-42.</p>
<p id="b895-5">At trial, and in his brief, Appellant argues that various depictions within the CGA are unsupported by any evidence.<footnotemark>7</footnotemark> <page-number citation-index="1" label="688">*688</page-number>In particular, Appellant contends that the CGA was littered with choices unsupported by either the record or the opinions of Trooper Beach and Dr. Ross. These alleged liberties taken by the Commonwealth included: (1) depicting the victim as kneeling during one of the gun shots; (2) placing the victim’s left arm on the floor during the second shot; (3) the position of Appellant; (4) the two-handed grip on the gun by Appellant; (5) the combat-style crouch by Appellant; and (6) the appearance of a knife in the final scene of the CGA. Appellant emphasizes the fact that one image within the CGA shows the victim on her knees before Appellant fires the third bullet. Contradicting Appellant’s contention, Matzkanin testified that the poses, although not guaranteed to be 100% accurate, were within the confines of the findings and suggestions of the expert opinions of both Dr. Ross and Trooper Beach. Specifically, Dr. Ross testified that, concerning the distance between Appellant and the victim, based upon the lack of soot or gunpowder, the bullet path or trajectory for the various wounds, and that, as a result of the first shot, the victim would have collapsed to the floor in a kneeling position. N.T. 2/4/02 p. 177-215. In addition, Dr. Ross noted that he was able to surmise that the victim was kneeling and facing Appellant because of an abrasion on her left cheek consistent with falling onto her eyeglasses from a distance of approximately eighteen to twenty-four inches. <em>Id. </em>at 215-17.</p>
<p id="b896-5">Moreover, the depictions of the physical locations of Appellant and the victim were necessary within the overall framework of the presentation. Clearly, reconstruction will not reveal the exact pose of each finger, hair, distances precise to the micrometer, or other minor aspects of the individuals involved. As noted in the instructions to the jury, and during the cross-examination of Matzkanin and Trooper Beach, Appellant highlighted the alleged inconsistencies within the presentation and any flaws, thereby reducing the credibility the jury might assign to the CGA. However, the CGA is still <page-number citation-index="1" label="689">*689</page-number>properly authenticated as a demonstrative piece of evidence illustrating the opinions of the Commonwealth’s expert witnesses. As noted by the trial court, any continued objection to how the video was created is merely appropriate fodder for cross-examination.</p>
<p id="b897-4">Appellant had many opportunities to, and did, cross-examine Matzkanin and to try to undermine the credibility of the video and the opinions of the expert witnesses. The cross-examination highlighted the purpose of a CGA. Specifically, Appellant’s trial counsel asked Matzkanin if he had any idea if the measurements were accurate and whether errors in the report would render the CGA incorrect. <em>Id. </em>at 171-75. In addition, Matzkanin was questioned about a knife that appeared in the last scene of the animation, but never appeared in the victim’s hands. Despite attempting to emphasize an apparent facial illogicality to this sequence, the CGA was merely representing the theory of the Commonwealth. In particular, it was the contention of the Commonwealth that Appellant placed the knife there after firing the shots in an attempt to stage the crime scene and create a claim of self-defense. The Commonwealth also theorized that Appellant had moved the victim’s right arm because the blood evidence indicated to Dr. Ross that Appellant had moved the arm of the victim after death in an attempt to create a self-defense claim. N.T. 2/4/04 at 217-19. Appellant, through cross-examination, highlighted the information that actually was either unfounded or that represented an arbitrary choice where the data was unknown, such as the exact positions of each body part. In accordance with the purpose of the CGA, the trial court instructed the jury that the CGA did not represent fact, but the theory of the Commonwealth and was meant to demonstrate the opinions of the Commonwealth experts.</p>
<p id="b897-5">The CGA is not meant to represent the theories of both parties; rather, as noted by both the trial court and Matzkanin, the sole purpose of the CGA and role of Matzkanin was to represent the findings of Trooper Beach and Dr. Ross. Matzkanin made no active decisions, rather, he merely interpreted the data and made corrections to the CGA based on the <page-number citation-index="1" label="690">*690</page-number>recommendations given to him by the two experts. The CGA is, ultimately, a representation of the expert opinions and demonstrative evidence. The line of questions presented by Appellant highlighted the alleged uncertainty regarding specific facts within the CGA and alerted the jury to the possible lack of credibility of Trooper Beach, Dr. Ross, and, by extension, the CGA. However, the jury ultimately found the testimony of the Commonwealth experts, and the CGA, to be credible. As such, the foundation was properly laid and the CGA was, in fact, what the Commonwealth purported it to be, a depiction of the various testimonies of the Commonwealth witnesses concerning their theory about the chain of events. <em>See </em>Pa.R.E. 901(a); Trial Ct. Op. at 12-13 (noting that the foundational requirements set forth by the court in its pretrial ruling on the Motion <em>in limine, Serge, </em><span class="citation" data-id="6388367"><a href="/opinion/6514793/commonwealth-v-serge/" aria-description="Citation for case: Commonwealth v. Serge">58 Pa. D. &amp; C.4th 52</a></span> (Pa.Com.P1.2001), were met). As such, the CGA was properly authenticated pursuant to Pa.R.E. 901.</p>
<p id="b898-5">Because the CGA was properly authenticated, we must turn to the second prong of the three-part test, which involves a question of its relevancy. The CGA was relevant because it clearly, concisely, and accurately depicted the Commonwealth’s theory of the case and aided the jury in the comprehension of the collective testimonies of the witnesses without use of extraneous graphics or information.</p>
<p id="b898-6">The Pennsylvania Rules of Evidence define relevant evidence as, “having any tendency to make the existence of the fact that is of consequence to the determination of the action more probable or less probable than would be without the evidence.” Pa.R.E. 401. As stated by the Superior Court, “The animation’s relevance under Pa.R.E. 401 lay in its clear, concise, and accurate depiction of the Commonwealth’s theory of the case, which included the rebuttal of Appellant’s self-defense theory, without use of extraneous graphics or information.” <em>Serge, </em><span class="citation" data-id="1991045"><a href="/opinion/1991045/commonwealth-v-serge/#1262" aria-description="Citation for case: Commonwealth v. Serge">837 A.2d at 1262</a></span>. In addition, it melded the theories of the various Commonwealth experts into a concise presentation that removed the testimony from the abstract into a concise and clear explanation of the individual testimony <page-number citation-index="1" label="691">*691</page-number>and how that testimony fits within the overall framework and consistency of all of the expert testimony.</p>
<p id="b899-5">Appellant argues that, in the alternative, even if the CGA is relevant, it is cumulative. However, as noted by the Superior Court, although the evidence did not offer anything inherently original, it presented a clear and precise depiction of the Commonwealth’s theory and evidence as presented by its experts. Pursuant to Pa.R.E. 702, demonstrative depictions of the testimony of an expert have long been allowed into evidence, including drawings or depictions of bullet trajectories as here. Therefore, the cumulative argument carries no weight. Rather, the question is whether the evidence presented by the CGA is relevant and whether its probative value outweighs its prejudicial effect. Pa.R.E. 401, 403.</p>
<p id="b899-6">Accordingly, we must turn to the third and final prong, prejudice. It is within this prong that a CGA has the potential danger due to the visual nature of the presentation. Various jurisdictions that have been faced with the issue of CGA-evidence have noted the potentially powerful impact based upon its visual nature, but, nonetheless, have permitted CGA evidence. <em>See </em>fn. 3, <em>supra. </em>Despite this potential power,<footnotemark>8</footnotemark> even inflammatory evidence may be admissible if it is relevant and helpful to a jury’s understanding of the facts and the probative value outweighs the prejudicial effect. <em>See Commonwealth v. Jacobs, </em><span class="citation" data-id="2197204"><a href="/opinion/2197204/commonwealth-v-jacobs/" aria-description="Citation for case: Commonwealth v. Jacobs">536 Pa. 402</a></span>, <span class="citation" data-id="2197204"><a href="/opinion/2197204/commonwealth-v-jacobs/" aria-description="Citation for case: Commonwealth v. Jacobs">639 A.2d 786</a></span> (1994) (holding that the evidentiary value of photographs taken at one victim’s autopsy and photographs showing position of bodies at crime scene outweighed their prejudicial effect, where blood and tissue had been cleaned from body before color photographs had been taken, photographs exposed exceedingly malicious manner of murders, bolstered prosecution’s theory that killings were intentional, not just result of <page-number citation-index="1" label="692">*692</page-number>defendant’s brief loss of control, and provided evidence regarding dispute as to weapons used against one of the victims); <em>Commonwealth v. Rush, </em><span class="citation" data-id="2200503"><a href="/opinion/2200503/commonwealth-v-rush/" aria-description="Citation for case: Commonwealth v. Rush">538 Pa. 104</a></span>, <span class="citation" data-id="2200503"><a href="/opinion/2200503/commonwealth-v-rush/" aria-description="Citation for case: Commonwealth v. Rush">646 A.2d 557</a></span> (1994) (holding that even though condition of victim’s body had been described by medical examiner, photographs depicting the position of a victim’s body were admissible to provide the jury with a better understanding of crime scene and to expose the malicious manner in which the murder was committed).</p>
<p id="b900-5">Presently, the content of the CGA was neither inflammatory nor unfairly prejudicial. Any prejudice derived from viewing the CGA resulted not from the on-screen depiction of the Commonwealth’s theory, but rather was inherent to the reprehensible act of murder. The possible unnecessary and prejudicial aspects of a CGA were not present. In particular, the CGA did not include: (1) sounds; (2) facial expressions; (3) evocative or even life-like movements; (4) transition between the scenes to suggest a story line or add a subconscious prejudicial effect; or (5) evidence of injury such as blood or other wounds. Instead, much like a two-dimensional hand drawing of bullet trajectories, the CGA merely highlighted the trajectory of the three bullets fired, concluding from ballistics and blood splatter that the body had been moved after the victim died as part of Appellant’s attempt to stage his self-defense. The CGA was devoid of drama so as to prevent the jury from improperly relying on an emotional basis. <em>See People v. Hood, </em><span class="citation" data-id="2284483"><a href="/opinion/2284483/people-v-hood/#972" aria-description="Citation for case: People v. Hood">53 Cal.App.4th 965, 972</a></span>, <span class="citation" data-id="2284483"><a href="/opinion/2284483/people-v-hood/" aria-description="Citation for case: People v. Hood">62 Cal.Rptr.2d 137</a></span> (1997) (permitting a CGA in a murder trial, in part because “[t]he animation was clinical and emotionless. This, combined with the instruction given the jurors about how they were to utilize both animations, persuades us that the trial court did not [err in permitting the CGA].”) The major difference between a traditional chart or drawing of bullet trajectories and the instant presentation lays in the three-dimensional nature that enabled the Commonwealth experts to present their exact theory and the underlying mathematics used in formulating its case. In particular, the ability to rotate the view allowed the Commonwealth’s experts to explain the exact path of the bullets and show why the evidence suggested that <page-number citation-index="1" label="693">*693</page-number>it was not a killing in self-defense. As such, it was a clearly relevant and helpful tool for an expert to present an informed opinion to the jury. <em>See </em>Pa.R.E. 703.</p>
<p id="b901-5">Within his argument concerning prejudice, Appellant, in this appeal, additionally raises the issue that public policy should prevent the presentation of a CGA, which, allegedly, costs between $10,000.00 and $20,000.00 to make.<footnotemark>9</footnotemark> He notes that his entire defense fund, provided by the Commonwealth due to his <em>in forma pauperis </em>status, was limited to $10,000.00. (Brief of Appellant, p. 44). Any additional expenditure would then come from Appellant.<footnotemark>10</footnotemark></p>
<p id="b901-6">This argument is waived because it was not raised at the trial court level. Pa.R.A.P. 302(a) (stating that issues not raised in the lower court are waived and cannot be raised for the first time on appeal). However, Appellant argues that we should consider this factor because of the implications of permitting the Commonwealth to present expensive CGA productions at trial against an indigent defendant.</p>
<p id="b901-7">Precedent exists concerning the admission of expert testimony that is beyond the means of an indigent defendant. This Court recently addressed the rights of an indigent defendant when the prohibitively expensive expert was a psychiatrist. Specifically, in <em>Commonwealth v. Fisher, </em><span class="citation" data-id="9748377"><a href="/opinion/2275499/commonwealth-v-fisher/" aria-description="Citation for case: Commonwealth v. Fisher">572 Pa. 105</a></span>, <span class="citation" data-id="9748377"><a href="/opinion/2275499/commonwealth-v-fisher/" aria-description="Citation for case: Commonwealth v. Fisher">813 A.2d 761</a></span>, (2002), this Court opined that in <em>Ake v. Oklahoma, </em><span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/" aria-description="Citation for case: Ake v. Oklahoma">470 U.S. 68</a></span>, <span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/" aria-description="Citation for case: Ake v. Oklahoma">105 S.Ct. 1087</a></span>, <span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/" aria-description="Citation for case: Ake v. Oklahoma">84 L.Ed.2d 53</a></span> (1985), the U.S. Supreme Court held “that when a capital defendant’s mental health is at issue, ‘the Constitution requires that an <page-number citation-index="1" label="694">*694</page-number>indigent defendant have access to the psychiatric examination and assistance necessary to prepare an effective defense.’ ”. <em>Fisher, </em><span class="citation" data-id="9748377"><a href="/opinion/2275499/commonwealth-v-fisher/" aria-description="Citation for case: Commonwealth v. Fisher">813 A.2d at 765</a></span> (quoting <em>Ake, </em><span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/#70" aria-description="Citation for case: Ake v. Oklahoma">470 U.S. at 70</a></span>, <span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/" aria-description="Citation for case: Ake v. Oklahoma">105 S.Ct. 1087</a></span>). However, this Court limited access to those funds to circumstances where the defendant’s sanity at the time of the offense was a significant factor at trial. “The Court in <em><span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/" aria-description="Citation for case: Ake v. Oklahoma">Ake</a></span> </em>held that indigent defendants are entitled to cost-free access to psychiatric experts only in very limited circumstances where the defendant’s, sanity at the time of the offense was a significant factor at trial. In <em><span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/" aria-description="Citation for case: Ake v. Oklahoma">Ake</a></span>, </em>there was a defense of insanity, not ... questions of mitigation relevant to a sentencing determination.” <em>Fisher, </em><span class="citation" data-id="9748377"><a href="/opinion/2275499/commonwealth-v-fisher/#765" aria-description="Citation for case: Commonwealth v. Fisher">813 A.2d at 765</a></span>.</p>
<p id="b902-5">This Court in <em>Commonwealth v. Bardo, </em><span class="citation" data-id="2070992"><a href="/opinion/2070992/commonwealth-v-bardo/" aria-description="Citation for case: Commonwealth v. Bardo">551 Pa. 140</a></span>, <span class="citation" data-id="2070992"><a href="/opinion/2070992/commonwealth-v-bardo/" aria-description="Citation for case: Commonwealth v. Bardo">709 A.2d 871</a></span> (1998), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./525/936/">525 U.S. 936</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./119/350/">119 S.Ct. 350</a></span>, <span class="citation" data-id="9173245"><a href="/opinion/9178526/xuan-huynh-v-forte-airport-services-inc/" aria-description="Citation for case: Xuan Huynh v. Forte Airport Services, Inc.">142 L.Ed.2d 289</a></span> (1998), held that a defendant does not have an absolute right to a court appointed investigator based on <em><span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/" aria-description="Citation for case: Ake v. Oklahoma">Ake, supra.</a></span> </em>“ ‘[Traditionally’ the appointment of an investigator has been a matter vested in the discretion of the court.” <em>Id. </em>at 875. <em>See also Commonwealth v. Howard, </em><span class="citation" data-id="1528587"><a href="/opinion/1528587/commonwealth-v-howard/" aria-description="Citation for case: Commonwealth v. Howard">553 Pa. 266</a></span>, <span class="citation" data-id="1528587"><a href="/opinion/1528587/commonwealth-v-howard/" aria-description="Citation for case: Commonwealth v. Howard">719 A.2d 233</a></span> (1998) (holding that a request for professional assistance need not be granted where the defendant, appellant, or postconviction petitioner fails to identify particularized need for such assistance related to a colorable issue presented in his defense, appeal, or petition, or where an adequate alternative to the requested form of professional assistance is available). In <em>Commonwealth v. Carter, </em><span class="citation" data-id="2319144"><a href="/opinion/2319144/commonwealth-v-carter/" aria-description="Citation for case: Commonwealth v. Carter">537 Pa. 233</a></span>, <span class="citation" data-id="2319144"><a href="/opinion/2319144/commonwealth-v-carter/" aria-description="Citation for case: Commonwealth v. Carter">643 A.2d 61</a></span> (1994), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./514/1005/">514 U.S. 1005</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./115/1317/">115 S.Ct. 1317</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/131/198/">131 L.Ed.2d 198</a></span> (1995), this Court upheld the denial of Commonwealth funds to assist an indigent defendant in hiring experts in the fields of toxicology, neurology, statistics, jury selection, hand writing analysis, and sociology/criminology. This Court opined that:</p>
<blockquote id="b902-6">The decision to appoint an expert witness is within the sound discretion of the trial court and will not be disturbed except for a clear abuse of that discretion. <em>United States ex rel Dessus v. Pennsylvania, </em><span class="citation" data-id="1951708"><a href="/opinion/1951708/united-states-ex-rel-dessus-v-commonwealth-of-pa/" aria-description="Citation for case: United States Ex Rel. Dessus v. Commonwealth of Pa.">316 F.Supp. 411</a></span> (E.D.Pa.1970), <em>affirmed, </em><span class="citation" data-id="300435"><a href="/opinion/300435/united-states-of-america-ex-rel-ronald-james-dessus-v-commonwealth-of/" aria-description="Citation for case: United States of America Ex Rel. Ronald James Dessus v....">452 F.2d 557</a></span> (3rd Cir.1971), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./409/853/">409 U.S. 853</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./93/184/">93 S.Ct. 184</a></span>, <span class="citation no-link">34 L.Ed.2d 96</span> (1972); <em>Commonwealth v. </em><page-number citation-index="1" label="695">*695</page-number><em>Gelormo, </em><span class="citation" data-id="2182314"><a href="/opinion/2182314/commonwealth-v-gelormo/" aria-description="Citation for case: Commonwealth v. Gelormo">327 Pa.Super. 219</a></span>, <span class="citation" data-id="2182314"><a href="/opinion/2182314/commonwealth-v-gelormo/" aria-description="Citation for case: Commonwealth v. Gelormo">475 A.2d 765</a></span> (1984). There is no obligation on the part of the Commonwealth to pay for the services of an expert. <em>Commonwealth v. Williams, </em><span class="citation" data-id="2312831"><a href="/opinion/2312831/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">522 Pa. 287</a></span>, <span class="citation" data-id="2312831"><a href="/opinion/2312831/commonwealth-v-williams/#718" aria-description="Citation for case: Commonwealth v. Williams">561 A.2d 714, 718</a></span> (1989) (citing <em>Commonwealth v. Box, </em><span class="citation" data-id="9700965"><a href="/opinion/1957040/commonwealth-v-box/" aria-description="Citation for case: Commonwealth v. Box">481 Pa. 62</a></span>, <span class="citation no-link">891 A.2d 1316</span> (1978)); <em>Commonwealth v. Rochester, </em><span class="citation" data-id="2314707"><a href="/opinion/2314707/commonwealth-v-rochester/" aria-description="Citation for case: Commonwealth v. Rochester">305 Pa.Super. 364</a></span>, <span class="citation" data-id="2314707"><a href="/opinion/2314707/commonwealth-v-rochester/" aria-description="Citation for case: Commonwealth v. Rochester">451 A.2d 690</a></span> (1982). However, in a capital case, an accused is entitled to the assistance of experts necessary to prepare a defense. <em>United States ex rel. Dessus, </em><span class="citation" data-id="1951708"><a href="/opinion/1951708/united-states-ex-rel-dessus-v-commonwealth-of-pa/#418" aria-description="Citation for case: United States Ex Rel. Dessus v. Commonwealth of Pa.">316 F.Supp. at 418</a></span>.</blockquote>
<p id="b903-4"><em>Carter, </em><span class="citation" data-id="2319144"><a href="/opinion/2319144/commonwealth-v-carter/#73" aria-description="Citation for case: Commonwealth v. Carter">643 A.2d at 73</a></span> (citations modified); <em>see also Commonwealth v. Howard, </em><span class="citation" data-id="1528587"><a href="/opinion/1528587/commonwealth-v-howard/" aria-description="Citation for case: Commonwealth v. Howard">553 Pa. 266</a></span>, <span class="citation" data-id="1528587"><a href="/opinion/1528587/commonwealth-v-howard/" aria-description="Citation for case: Commonwealth v. Howard">719 A.2d 233</a></span> (1998) (stating that, in a capital case, “it is clear that a request for professional assistance need not be granted where the defendant ... fails to identify a particularized need for such assistance related to a colorable issue presented in his defense ... or where an adequate alternative to the requested form of professional assistance is available.”). Similarly, there can be no obligation to provide the defendant the finances necessary to create a CGA of his or her own.<footnotemark>11</footnotemark> Chief Justice Cappy’s <page-number citation-index="1" label="696">*696</page-number>concurring Opinion accurately summarizes the ultimate concerns regarding the economic disparity between the Commonwealth and an indigent defendant. <em>See </em>Concurring Opinion (Cappy, C.J.), at 700, 896 A.2d at 1188 (“In many cases this will require the trial court to give money to the defense to procure a CGA. This monetary disparity between the Commonwealth and defense in obtaining a CGA is a relevant factor when considering the prejudice to the defense.”) Thus, we ultimately conclude that the relative monetary positions of the parties are relevant for the trial court to consider when ruling on whether or not to admit a CGA into evidence. Such a question and determination are within the province of the trial court and should not be overturned absent an abuse of discretion. In particular, the trial court sitting with all facts before it, including the monetary disparity of the parties, must determine if the potentially powerful effect of the CGA and the inability of a defendant to counter with his or her own CGA should lead to its preclusion. Nevertheless, as noted above, this specific argument is waived in the instant matter.</p>
<blockquote id="b904-5">It is argued that the uniquely dangerous aspect of a CGA is in its visual appeal to a jury resulting in an acceptance of the CGA as fact. However, such a danger is vitiated by thorough cautionary instructions that educate the jury on the exact nature and role of a CGA. Presently, the trial court safeguarded against the possibility of jury confusion over the animation or potential prejudice by supplying a thorough and extensive cautionary instruction before playing the CGA. Those instructions were:</blockquote>
<blockquote id="b904-6">Members of the jury, parties in a case are permitted to use photographs, drawings and other exhibits to illustrate a point they are attempting to make in a case. This is what we refer to as demonstrative evidence. We refer to this type of evidence as demonstrative evidence, as opposed to <page-number citation-index="1" label="697">*697</page-number>substantive evidence, since it is offered merely to demonstrate or illustrate a point rather than as actual proof of that point.</blockquote>
<blockquote id="b905-5">With the advent of the digital age, computers are now used to produce this type of demonstrative evidence. You heard testimony from Dr. Gary Ross and Trooper Brad Beach that the computer-generated animation, which will now be shown to you, is a fair and accurate illustration of the opinions that they formed as to how this shooting allegedly occurred. You also heard this witness describe how he produced the three-dimensional drawings with computer software to depict those opinions, and thereafter transform them onto this DVD to produce moving images, which will be played for you. What you are about to be shown is commonly referred to as a computer-generated exhibit. There are two types of computer-generated exhibits, and you heard the witness refer to them. The first is what we call a simulation, and the second is what we refer to as an animation.</blockquote>
<blockquote id="b905-6">In a simulation, data is entered into a computer, which is preprogrammed to perform certain calculations by applying, for example, the laws of physics, mathematical formulas, and other scientific principles in order for the computer itself to draw conclusions and to attempt to recreate an incident. The end product of a simulation represents the computer program’s conclusion of what happened. And the results of the computer simulation serve as the basis for the testifying expert’s opinion of what happened.</blockquote>
<blockquote id="b905-7">In contrast, an animation is simply a graphic depiction, or illustration, of an opinion that an expert has already formed based upon his or her own independent investigation, computations, and analysis. With an animation, the computer does not perform any scientific calculations or develop any opinions, as is the case with the simulation. An animation consists of computer-generated drawings which are assembled frame by frame, and, when viewed sequentially, produce the image of motion. Thus, an animation is merely a graphic depiction or illustration of an opinion or recreation <page-number citation-index="1" label="698">*698</page-number>which an expert witness in the case has already devised through his or her own independent calculations and analysis.</blockquote>
<blockquote id="b906-5">Please understand that what you are about to view is an animation, not a simulation. This computer-generated animation is a demonstrative exhibit, not substantive evidence, and it is being offered solely as an illustration of the Commonwealth’s version of events as recreated by Dr. Gary Ross and Trooper Brad Beach. You should not confuse art with reality and should not view the animation as a definitive recreation of the actual incident. The series of pictures which have been drawn by the computer and transferred on to the tape for your review are no different from a witness sketching a series of drawings on paper and then fanning those pages to portray moving images of his or her opinion. Remember, the demonstrative animation is only as good as the underlying testimony, data, assumptions, and opinions that serve as the basis for its images, and the computer maxim, “garbage in, garbage out,” applies equally to computer animations. Like all other evidence in the case, you may accept it or reject it, that is, the computer-generated animation, in whole or in part. I caution you again that the animation may only be considered for demonstrative purposes to illustrate the opinions of Dr. Gary Ross and Trooper Bradley Beach. Always bear in mind that the Commonwealth must still meet its burden of proving all of the elements of the offense charged beyond a reasonable doubt.</blockquote>
<p id="b906-6"><em>Serge, </em><span class="citation" data-id="1991045"><a href="/opinion/1991045/commonwealth-v-serge/" aria-description="Citation for case: Commonwealth v. Serge">837 A.2d at 1263</a></span>-64 (citing Notes of Testimony 2/7/02 at 153-56). Although limiting instructions may not be necessary, such cautionary instructions limit the prejudice or confusion that could surround a CGA.<footnotemark>12</footnotemark> <em>See Harris, </em>13 P.3d at 495 <page-number citation-index="1" label="699">*699</page-number>(requiring cautionary jury instructions when using a CGA and noting South Carolina’s requirement of the same in <em>Clark, supra). </em>Additionally, the trial court reiterated the same concerns and instructions during its closing jury charge. In so doing, the trial court duly minimized any possible prejudice by insisting that the jury not make more of the CGA than what it was — an illustration of expert witness testimony. The repetition of the instructions in the case <em>sub judice </em>ensured that the jury comprehended the nature of the CGA and would not mistake it for fact, but could only rely upon it to the extent they credited the underlying testimony.</p>
<p id="b907-4">
<em>CONCLUSION</em>
</p>
<p id="b907-5">In a question of first impression in this Commonwealth, we hold that a CGA is potentially admissible as demonstrative evidence, as long as the animation is properly authenticated, it is relevant, and its probative value outweighs the danger of unfair prejudice or confusion. Therefore, because in the instant matter: (1) the Commonwealth satisfied all of the foundational requirements for admitting the CGA as demonstrative evidence; (2) the CGA was relevant evidence that enabled the Commonwealth experts to illustrate their opinions and educate the jury on the forensic and physical data; and (3) the alleged prejudicial effect of the CGA does not outweigh its relevance, we conclude that the admission of this evidence was proper. Hence, the admission of a CGA depicting the theory of the Commonwealth in this case was proper. Accordingly, we affirm the decision of the Superior Court.</p>
<judges id="b908-3"><page-number citation-index="1" label="700">*700</page-number>Justice SAYLOR and BAER join the opinion.</judges>
<judges id="b908-4">Former Justice NIGRO did not participate in the decision of this case.</judges>
<judges id="b908-5">Chief Justice CAPPY files a concurring opinion.</judges>
<judges id="b908-6">Justice CASTILLE files a concurring opinion.</judges>
<judges id="b908-7">Justice EAKIN files a concurring opinion. .</judges>
<footnote label="1">
<p id="b885-7">. A CGA is a drawing, or drawings, created by a computer that, when assembled frame-by frame, produce the image of motion. The image is merely a graphic representation depicting the previously formed opinion of a witness or witnesses, in this case the Commonwealth experts. F. Galves, <em>Where the Not So Wild Things Are: Computers in the Courtroom, the Federal Rules of Evidence, and the Need for Institutional Reform and More Judicial Acceptance, </em><span class="citation no-link">13 Harv. J.L. &amp; Tech. 161</span>, 227-30 (2000). Presently, the CGA is akin to the traditionally permitted drawings used by crime scene reconstructionists to show bullet path trajectory. Accordingly, a CGA is only as credible as the underlying testimony that it represents and the computer plays no part in calculating an outcome or presenting its own conclusions. Conversely, computer-generated simulations do not depict witness opinion; rather, the computer program, based upon the data entered, draws a conclusion. As such, a computer simulation presents not only the testimony of an expert regarding the programming and data input but also a conclusion of the computer based upon the formulas programmed to use the raw data entered. For example, scientists use computer simulations to predict the effects of earthquakes on a building's structure by inputting factors such as: (1) wind; (2) magnitude of earthquake; (3) proximity of earthquake; (4) building materials; (5) building height; (6) amplitude of the earthquakes waves; and so forth. However, the simulation creates a result that nobody can testify to with personal knowledge nor is it the representation of an individual's opinion. Rather it is the <page-number citation-index="1" label="678">*678</page-number>outcome of the program’s mathematical formulas based on the various inputted data and the laws of physics as entered by the programmers. As noted by Justice Castille in his concurring Opinion, the program used for either a CGA or a simulation is a human product and may be subjected to scrutiny regarding its programming bias and soundness in principles of both math and physics. At that point, a proper determination of the appropriate weight to be assigned to its output can occur. Further, as discussed <em>infra, </em>jury instructions may help in reducing or eliminating the potential for a jury to assign undue weight to a CGA by clarifying that it is, in actuality, a graphic representation of biased testimony of one party and not a product of neutral infallible artificial intelligence. Today, we address only the admissibility of CGA evidence as defined above and not that of computer simulations.</p>
</footnote>
<footnote label="2">
<p id="b886-6">. Chief Justice Cappy urges this Court to adopt a standard in which the Commonwealth would be required to file a pre-trial motion <em>in limine </em>whenever CGA evidence is involved. Although this is a recommended procedure to reduce potential prejudice, we hold that the moving party, be it the Commonwealth or a defendant, should file a motion <em>in limine </em>and seek permission of the trial court to admit the evidence as soon as possible, even if after the start of trial. It is conceivable that a party may find, after the start of trial, that a CGA would be helpful to rebut evidence or new testimony set forth by the opposing party. Should a party discover that a CGA would be helpful at that point in time that party should not be precluded from asking the trial court to admit a CGA into evidence. The timing of the request must be weighed along with the various other factors involved in determining if the prejudicial effect of the CGA outweighs its probative value. As one example, an eyewitness may testify for the defendant that they were able to see the crime scene from a certain location. Such testimony may come as a surprise to the Commonwealth, which would wish, at that time, to introduce a CGA showing the viewpoint from that location at various heights and angles in order to rebut the testimony that the witness could see what they claimed. Such a CGA would be relatively benign, with no depiction of the defendant or victim and would be used merely to impeach the credibility of the eyewitness. Most likely, in this circumstance, no prejudice would result from its admission even after the start of trial. Moreover, the Commonwealth should not be penalized for being unable to foresee the testimony of all parties by being prevented, as a <em>per se </em>rule, from admitting a CGA into evidence after the start of trial. The rules of evidence must still be applied to each situation and, thus, Pa.R.E. 403 should still be employed in determining the admissibility of a CGA at a later point in trial; however, the further along the trial is, the more likely it is that the prejudicial effect will outweigh the probative value of a CGA because the opposing party has less time to examine the CGA or prepare its own CGA. This concern would be heightened in criminal cases where the defendant may have scarce resources to properly examine a CGA and prepare his or her <page-number citation-index="1" label="679">*679</page-number>own. Certainly, in a case such as this, where the CGA is not benign but rather represents the actual crime, a cold-hearted killing, a failure to file a pre-trial motion <em>in limine </em>could create a prejudicial effect to such an extent that it could foreclose the possibility of midtrial admittance of the CGA into evidence.</p>
</footnote>
<footnote label="3">
<p id="b889-6">. Because a CGA is a graphic illustration of an expert's reconstruction rather than a simulation based upon scientific principles and computerized calculations, it is not subject to the <em>Frye </em>test governing the admissibility of scientific evidence in Pennsylvania. <em>See Frye v. United </em>States, <span class="citation" data-id="8833029"><a href="/opinion/8847721/frye-v-united-states/" aria-description="Citation for case: Frye v. United States">293 F. 1013</a></span> (D.C.Cir.1923). Of course, the underlying expert opinion that the animation seeks to illustrate must satisfy Pa.R.E. 702 and be premised upon principles and methodology that are generally accepted in the relevant scientific community. Moreover, in accordance with Pa.R.E. 703, the facts or data on which the expert has relied in forming the opinion, which is illustrated by the computer animation, must be "of a type reasonably relied upon by experts in the particular field.” <em><span class="citation" data-id="8833029"><a href="/opinion/8847721/frye-v-united-states/" aria-description="Citation for case: Frye v. United States">Id.</a></span> </em>However, the issue of applying the <em><span class="citation" data-id="8833029"><a href="/opinion/8847721/frye-v-united-states/" aria-description="Citation for case: Frye v. United States">Frye</a></span> </em>test to a computer simulation must await another day.</p>
</footnote>
<footnote label="4">
<p id="b891-8">. CGA evidence has been admitted in most states that have considered the matter, including in the criminal context. <em>See Pierce v. State, </em><span class="citation" data-id="1105871"><a href="/opinion/1105871/pierce-v-state/" aria-description="Citation for case: Pierce v. State">718 So.2d 806</a></span> (Fla.App.1997) (holding that a CGA of an automobile accident was admissible when the testimony of three accident-reconstruction experts established that the: (1) computer program used was <page-number citation-index="1" label="684">*684</page-number>accepted in engineering field as one of the leading computer-aided design programs in the world; (2) CGA fairly and accurately reflected expert opinion of how accident occurred; (3) CGA was fair and accurate representation of what it purported to depict; and (4) data, information, and evidence utilized was of type reasonably relied upon by experts in field of forensic animation); <em>See also State v. Clark, </em><span class="citation" data-id="3699768"><a href="/opinion/3950893/state-v-clark/" aria-description="Citation for case: State v. Clark">101 Ohio App.3d 389</a></span>, <span class="citation" data-id="3699768"><a href="/opinion/3950893/state-v-clark/" aria-description="Citation for case: State v. Clark">655 N.E.2d 795</a></span> (8 Dist.1995), <em>State v. Swinton, </em><span class="citation" data-id="7848541"><a href="/opinion/7900194/state-v-swinton/" aria-description="Citation for case: State v. Swinton">268 Conn. 781</a></span>, <span class="citation" data-id="7848541"><a href="/opinion/7900194/state-v-swinton/" aria-description="Citation for case: State v. Swinton">847 A.2d 921</a></span>, 945 n. 30 (2004) (citing, among others, <em>Cleveland v. Bryant, </em><span class="citation" data-id="1383501"><a href="/opinion/1383501/cleveland-v-bryant/" aria-description="Citation for case: Cleveland v. Bryant">236 Ga.App. 459</a></span>, <span class="citation" data-id="1383501"><a href="/opinion/1383501/cleveland-v-bryant/" aria-description="Citation for case: Cleveland v. Bryant">512 S.E.2d 360</a></span> (1999) (allowing a CGA as illustrative evidence); <em>Harris v. State, </em><span class="citation" data-id="9786809"><a href="/opinion/2585350/harris-v-state/#495" aria-description="Citation for case: Harris v. State">13 P.3d 489, 495</a></span> (Okla.Crim.App.2000) (same), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./532/1025/">532 U.S. 1025</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./121/1971/">121 S.Ct. 1971</a></span>, <span class="citation no-link">149 L.Ed.2d 764</span> (2001); <em>Mintun v. State, </em><span class="citation" data-id="2609330"><a href="/opinion/2609330/mintun-v-state/#959" aria-description="Citation for case: Mintun v. State">966 P.2d 954, 959</a></span> (Wyo.1998) (same); F. Galves, <em>Where the Not So Wild Things Are: Computers in the Courtroom, the Federal Rules of Evidence, and the Need for Institutional Reform and More Judicial Acceptance, </em><span class="citation no-link">13 Harv. J.L. &amp; Tech. 161</span>, 227-30 (2000) (comparing differing admission standards for animations and simulations)).</p>
</footnote>
<footnote label="5">
<p id="b892-6">. For example, the Commonwealth Court recently approved the use of a CGA as an illustrative adjunct to the testimony of two expert witnesses in a motor vehicle accident case. <em>Harsh v. Petroll, </em><span class="citation" data-id="2328404"><a href="/opinion/2328404/harsh-v-petroll/#423" aria-description="Citation for case: Harsh v. Petroll">840 A.2d 404, 423-24</a></span> (Pa.Cmwlth.2003), <em>allowance of appeal granted, </em><span class="citation" data-id="2351655"><a href="/opinion/2351655/harsh-v-petroll/" aria-description="Citation for case: Harsh v. Petroll">580 Pa. 546</a></span>, <span class="citation multiple-matches"><a href="/c/A.2d/862/581/">862 A.2d 581</a></span> (2004) (granting allowance of appeal on other grounds). In that case, three decedents died from smoke inhalation and burns when a Chevrolet Lumina was rear-ended by a tractor-trailer. The Commonwealth Court affirmed the admission into evidence of a CGA depicting the combined testimony of a mechanical engineer and an accident reconstructionist, which showed: (1) the Lumina’s fuel tank and anti-spit back valves; (2) the underside of the car; and (3) the accident sequence.</p>
</footnote>
<footnote label="6">
<p id="b893-5">. Appellant argues that a CGA or computer simulation has the potential to influence unduly a jury due to its visual impact. However, at least one controlled study suggests that a CGA, although helpful, has a negligible measurable impact upon a jury when the CGA does not present new information. R. Bennett, Jr., J. Leibman, R. Fetter, <em>Seeing is Believing; or is it? An Empirical Study of Computer Simulations as Evidence, </em>34 Wake Forest L.Rev. 257, 285 (1999) (“[T]he extraordinary possibilities inherent in computer animations and computer simulations raised hopes — and fears — that juries would find computer-generated displays more persuasive or convincing than other forms of evidence. These hopes and fears seem to be unwarranted, at least within the context of the empirical results of this study. In other words, computer-generated evidence is not a "silver bullet" which guarantees victory.”)</p>
</footnote>
<footnote label="7">
<p id="b895-6">. Appellant also argues that Trooper Beach was not qualified as an expert in the field of crime reconstruction, despite acknowledging that the trial court admitted him as such. To support his position, Appellant points to language of the trial court that stated that there is a first time for everything, including testifying as an expert witness in the Court of Common Pleas. N.T. 2/6/02, p. 198-98. However, this issue is not <page-number citation-index="1" label="688">*688</page-number>before us. We are asked only to determine the propriety of admitting CGA evidence, and not to revisit the discretion of the trial court to determine the qualifications of an expert witness.</p>
</footnote>
<footnote label="8">
<p id="b899-7">. At least one empirical study, <em>see </em>fn. 5, supra, has shown that the use of CGA evidence is not the deciding factor for a jury. Rather, the evidence and opinions underlying the CGA are the ultimate determinants of the jury's decision. The CGA merely facilitates the jury's understanding of the evidence and opinions without shifting the weight a juty assigns to the presenting side's testimony.</p>
</footnote>
<footnote label="9">
<p id="b901-8">. As noted previously, Appellant did not raise the issue of cost in the courts below and, therefore, it is waived. Pa.R.A.P. 302(a). As a result, the record was not developed on this issue and does not contain the exact final cost. However, both Appellant's brief and the Commonwealth during oral argument before this Court indicated the cost to be between $10,000.00 and $20,000.00. (Brief of Appellant, p. 44).</p>
</footnote>
<footnote label="10">
<p id="b901-9">. However, although cost is a consideration, this issue will lessen over time because of the inevitable reduction in cost as technology advances. This fact has been acknowledged from the inception of CGA usage. <em>See </em>R. Sherman, <em>Moving Graphics: Computer Animation Enters Criminal Cases, </em>Nat'l L.J., p. 32 (Apr. 6, 1992) (noting that, in 1992, the overall cost of computer animations had already dropped dramatically, thereby increasing their usage, including in criminal trials).</p>
</footnote>
<footnote label="11">
<p id="b903-5">. We must respectfully disagree with Justice Castille's suggestion that the "wisest course” is excluding such evidence where the defendant cannot secure an equivalent production. Concurring Opinion (Castille, J.), at 703, 896 A.2d at 1190. As in the fields of toxicology, neurology, statistics, jury selection, hand writing analysis, and sociology/criminology a defendant is not entitled under any existing precedent to matching funds. However, should the trial court determine that undue prejudice would result from the defendant's inability to examine the methodology used in creating what is merely a depiction of the Commonwealth’s expert testimony, the court may either exclude the evidence pursuant to Pa.R.E. 403 or provide the necessary funds to the defendant. Such a concern is certainly more relevant when discussing a computer-generated simulation where the underlying programming is relevant to the results received and does not merely graphically depict expert testimony as in a CGA. Moreover, the economic efficacy demonstrated by the Commonwealth is irrelevant as it is not the role of the trial court or this Court to advise the Commonwealth on how best to spend its money for trial. Thus, whether or not "the cost was worth the expenditure of scarce public financial resources,” <em>Id. </em>at 702, 896 A.2d at 1189, is not a question for this Court. Further, reviews of fiscal sagacity are not conducted concerning other Commonwealth expert testimony using psychologists, DNA forensic experts, and the like. A discussion of a court’s subjective opinion regarding the relative bargain received by the Commonwealth in procuring a CGA factor into a Pa.R.E. 403 test weighing its probative versus prejudicial value should also not be a <page-number citation-index="1" label="696">*696</page-number>question for the trial court or this Court. Ultimately, the amount of money spent may be a concern because of an increase in the prejudicial effect of the CGA due to the inability of a defendant to expend the same amount of money; however, the value received by the Commonwealth for its expenditure is irrelevant to the prejudicial effect or probative value of the CGA.</p>
</footnote>
<footnote label="12">
<p id="b906-8">. Chief Justice Cappy opines that limiting instructions are necessary in all cases involving the admission of a CGA into evidence. Although we agree that such instructions are a powerful tool in limiting prejudice, and a trial court would be wise to issue them, Pennsylvania Rule of Evidence 105 states that a non-admitting party may request jury instructions regarding the admission of evidence. Pa.R.E. 105. Of course, a trial court may issue instructions on its own initiative. <page-number citation-index="1" label="699">*699</page-number>"Though the trial court may, on its own initiative, give a limiting instruction to the jury, the onus is on a party who is entitled to such an instruction to ask for one. Otherwise, the party may waive an objection to the jury's use of evidence for an improper purpose.” David F. Binder, <em>Binder on Pennsylvania Evidence </em>§ 1.05, p. 22 (4th Ed. 2005). Today, we hesitate to create a new rule of evidence applying only to CGA evidence in criminal or civil cases; instead, we hold that such instructions are recommended on the part of the trial court to reduce prejudice. However, in accord with long-standing Pennsylvania law, a failure to ask for such instructions could result in waiver of any objection. <em>Keefer v. Byers, </em><span class="citation" data-id="1950044"><a href="/opinion/1950044/keefer-v-byers/" aria-description="Citation for case: Keefer v. Byers">398 Pa. 447</a></span>, <span class="citation" data-id="1950044"><a href="/opinion/1950044/keefer-v-byers/" aria-description="Citation for case: Keefer v. Byers">159 A.2d 477</a></span> (1960) (holding that the failure to object to the lack of jury instructions constitutes waiver of the claim).</p>
</footnote>
</opinion>
```

---
